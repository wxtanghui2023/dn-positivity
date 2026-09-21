# c380_58_B1alpha2_subdiff.py -- B1-alpha-2: subdifferential (convex-combination) KKT
import numpy as np, itertools
from scipy.optimize import linprog
rng = np.random.default_rng(5921)
SIG = [np.array(list(b)+[1], dtype=float) for b in itertools.product([-1,1], repeat=4)]

def cheb(deg, Y):
    N, m = Y.shape
    out = [np.ones((N, m)), Y.copy()]
    for k in range(2, deg+1): out.append(2*Y*out[-1]-out[-2])
    return np.stack(out, axis=1)

def parts(X, s):
    Y = 2*X-1
    E = cheb(24, Y)[:, [2*r for r in range(1,13)], :].sum(2)             # (N,12)
    C = np.sqrt(np.clip(X,0,1))
    O = cheb(25, C)[:, [2*r+1 for r in range(13)], :]                    # (N,13,5)
    F = (O * s[None,None,:]).sum(2)                                      # (N,13)
    return F, E

def descent(s, N=2500, iters=420, step0=0.25):
    X = rng.uniform(0,1,size=(N,5)); best = np.full(N, 1e9); bestX = X.copy(); step = step0
    def obj(Z):
        F, E = parts(Z, s)
        pen = 500.0*np.maximum(E-0.5,0).sum(1)
        return np.abs(F).max(1) + pen
    cur = obj(X)
    for it in range(iters):
        j = it % 5
        for d in (step,-step):
            Z = X.copy(); Z[:,j] = np.clip(X[:,j]+d,0,1)
            v = obj(Z); imp = v < cur
            cur = np.where(imp,v,cur); X = np.where(imp[:,None],Z,X)
        imp = cur < best; best = np.where(imp,cur,best); bestX[imp] = X[imp]
        if it % 50 == 49: step *= 0.75
    return best, bestX

# analytic gradients in phi coordinates
def gradphi(X, which, r, s=None):
    C = np.sqrt(np.clip(X,0,1)); phi = np.arccos(np.clip(C,-1,1))
    if which == 'even': return -2*r*np.sin(2*r*phi)
    return -(2*r+1)*s*np.sin((2*r+1)*phi)

def value_vectors(X):
    out = {}
    for s in SIG:
        F, E = parts(X[None,:], s)
        out[tuple(s.astype(int))] = (F[0], E[0])
    return out

print("=== B1-alpha-2: subdifferential KKT search over the 16 sign classes ===", flush=True)
TOL_ODD, TOL_EVEN = 1e-7, 1e-6
report = []
for si, s in enumerate(SIG):
    b, bX = descent(s)
    k = int(np.argmin(b)); X = bX[k]
    F, E = parts(X[None,:], s); F = F[0]; E = E[0]
    g = np.abs(F).max()
    I = [r for r in range(13) if abs(abs(F[r])-g) <= TOL_ODD]
    marg = 0.5 - E
    A = [q for q in range(1,13) if marg[q-1] <= TOL_EVEN]
    W = np.array([np.sign(F[r])*gradphi(X,'odd',r,s=s) for r in I])          # (|I|,5)
    G = np.array([gradphi(X,'even',q) for q in A]) if A else np.zeros((0,5)) # (|A|,5)
    # feasibility LP: [W|G]^T [w;lam] = 0 , sum w = 1 , w,lam >= 0
    m, n = len(I), len(A)
    if m == 0: continue
    Aeq = np.vstack([np.hstack([W.T, G.T]), np.hstack([np.ones(m), np.zeros(n)])])
    beq = np.concatenate([np.zeros(5), [1.0]])
    res = linprog(np.zeros(m+n), A_eq=Aeq, b_eq=beq,
                  bounds=[(0,None)]*(m+n), method='highs')
    ok = bool(res.status == 0)
    resid = float(np.linalg.norm(W.T @ res.x[:m] + (G.T @ res.x[m:] if n else 0))) if ok else float('nan')
    report.append((g, si, s, X, I, A, ok, resid, res.x if ok else None))
    print("  sigma=%s : g=%.6f | |I|=%d (r=%s) | A=%s | margin_max=%.2e | subdiff-KKT=%s residual=%.2e"
          % (s.astype(int), g, m, I, A, marg.max(), ok, resid), flush=True)

report.sort(key=lambda u: u[0])
print("\n=== surviving subdifferential-KKT candidates (sorted) ===", flush=True)
cnt = 0
for g, si, s, X, I, A, ok, resid, xw in report[:6]:
    print("  g=%.6f sigma=%s |I|=%d A=%s KKT=%s resid=%.2e" % (g, s.astype(int), len(I), A, ok, resid), flush=True)
    print("     x = %s" % np.round(X,6), flush=True)
    if ok and xw is not None:
        print("     omega = %s ; lambda = %s" % (np.round(xw[:len(I)],4), np.round(xw[len(I):],4)), flush=True)
        cnt += 1
print("   total surviving (subdiff-KKT feasible) = %d / 16" % cnt, flush=True)
print("DONE", flush=True)
