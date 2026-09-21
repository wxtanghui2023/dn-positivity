# c380_60_B1alpha3_bundle.py -- B1-alpha-3: cutting-plane/bundle descent + interior/boundary KKT audit
import numpy as np, itertools
from scipy.optimize import linprog
rng = np.random.default_rng(6031)
SIG = [np.array(list(b)+[1], dtype=float) for b in itertools.product([-1,1], repeat=4)]
HALF = np.pi/2

def Fodd(phi, s, r): return float(np.sum(s*np.cos((2*r+1)*phi)))
def Feven(phi, r):   return float(np.sum(np.cos(4*r*phi)))
def godd(phi, s, r): return -(2*r+1)*s*np.sin((2*r+1)*phi)
def geven(phi, r):   return -4*r*np.sin(4*r*phi)

def objective(phi, s): return max(abs(Fodd(phi, s, r)) for r in range(13))
def maxviol(phi): return max(Feven(phi, r) - 0.5 for r in range(1, 13))

def solve_sigma(s, maxit=70, tol=1e-11):
    best = None
    for trial in range(60):
        phi = rng.uniform(0.02, HALF-0.02, 5); Delta = 0.4
        for it in range(maxit):
            g = objective(phi, s)
            I = [r for r in range(13) if abs(abs(Fodd(phi, s, r)) - g) <= 1e-6*g + 1e-9]
            # master LP: min t s.t. |F_r| + sgn*grad.d <= t (r in I) ; F_2q + grad.d <= 1/2 (all q) ; |d|<=Delta
            n = 5
            A_ub, b_ub = [], []
            for r in I:
                w = np.sign(Fodd(phi, s, r)) * godd(phi, s, r)
                A_ub.append(np.concatenate([w, [-1.0]])); b_ub.append(-abs(Fodd(phi, s, r)))
            for q in range(1, 13):
                A_ub.append(np.concatenate([geven(phi, q), [0.0]])); b_ub.append(0.5 - Feven(phi, q))
            for j in range(5):   # keep phi_j >= 0  (boundary allowed)
                row = np.zeros(6); row[j] = -1.0
                A_ub.append(row); b_ub.append(phi[j])
            c = np.zeros(6); c[5] = 1.0
            bounds = [(-Delta, Delta)]*5 + [(None, None)]
            r_ = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=bounds, method='highs')
            if not r_.success: break
            d = r_.x[:5]
            if np.linalg.norm(d) < 1e-12: break
            # line search on the true objective with feasibility repair
            t = 1.0; moved = False
            for _ in range(30):
                cand = np.clip(phi + t*d, 0.0, HALF)
                if objective(cand, s) < g - 1e-14 and maxviol(cand) <= 1e-12:
                    phi = cand; moved = True; break
                t *= 0.5
            if moved: Delta = min(0.5, Delta*1.25)
            else:
                Delta *= 0.5
                if Delta < 1e-9: break
        g = objective(phi, s)
        if best is None or g < best[0]: best = (g, phi.copy())
    return best

print("=== B1-alpha-3: cutting-plane multistart per sigma (objective = min over x, sigma fixed) ===", flush=True)
res = {}
for si, s in enumerate(SIG):
    out = solve_sigma(s)
    res[si] = out
    print("  sigma=%s : g=%.9f  feasible(margin=%.2e)  boundary(phi_j~0)=%s"
          % (s.astype(int), out[0], -maxviol(out[1]), bool(np.any(out[1] < 1e-6))), flush=True)

si = min(res, key=lambda k: res[k][0]); g, phi = res[si]; s = SIG[si]
print("\n=== best sigma = %s ; g = %.9f ===" % (s.astype(int), g), flush=True)
marg = np.array([0.5 - Feven(phi, r) for r in range(1,13)])
ties = [r for r in range(13) if abs(abs(Fodd(phi, s, r)) - g) <= 1e-7]
bnd = [j for j in range(5) if phi[j] < 1e-8]
print("   even margins:", np.round(marg, 8), flush=True)
print("   active even A (tol 1e-6) =", [q for q in range(1,13) if marg[q-1] <= 1e-6],
      "| tied odd =", ties, "| boundary indices (phi=0) =", bnd, flush=True)
print("   phi/pi = %s ; x = %s" % (np.round(phi/np.pi,8), np.round(np.cos(phi)**2,8)), flush=True)

print("\n=== interior/boundary-separated subdifferential LP audit ===", flush=True)
for tol in (1e-7, 1e-6, 1e-5):
    I = [r for r in range(13) if abs(abs(Fodd(phi, s, r)) - g) <= tol]
    A = [q for q in range(1,13) if marg[q-1] <= tol]
    W = np.array([np.sign(Fodd(phi, s, r))*godd(phi, s, r) for r in I])
    G = np.array([geven(phi, q) for q in A]) if A else np.zeros((0,5))
    N = np.array([-np.eye(5)[j] for j in bnd]) if bnd else np.zeros((0,5))   # boundary normal cone (-e_j), mu>=0
    cols = [W.T, G.T, N.T]
    Aeq = np.vstack([np.hstack(cols), np.hstack([np.ones(len(I)), np.zeros(G.shape[0]+N.shape[0])])])
    beq = np.concatenate([np.zeros(5), [1.0]])
    rr = linprog(np.zeros(Aeq.shape[1]), A_eq=Aeq, b_eq=beq,
                 bounds=[(0,None)]*Aeq.shape[1], method='highs')
    ok = rr.status == 0
    resid = float(np.linalg.norm(Aeq[:-1] @ rr.x)) if ok else float('nan')
    print("   tol=%.0e : |I|=%d A=%s bnd=%s -> KKT=%s residual=%.2e %s"
          % (tol, len(I), A, bnd, ok, resid, ("(INTERIOR)" if not bnd else "(BOUNDARY)")), flush=True)
print("DONE", flush=True)
