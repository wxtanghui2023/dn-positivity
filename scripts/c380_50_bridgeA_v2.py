# c380_50_bridgeA_v2.py -- Bridge A first cut (vectorised)
import numpy as np, itertools

def cheb(deg, Y):
    # Y: (N,m) -> (N, deg+1) Chebyshev T_0..T_deg
    N, m = Y.shape
    out = [np.ones((N, m)), Y.copy()]
    for k in range(2, deg + 1):
        out.append(2 * Y * out[-1] - out[-2])
    return np.stack(out, axis=1)          # (N, deg+1, m)

def evenF(X):
    Y = 2 * X - 1
    T = cheb(24, Y)                        # T[k] for k = 0..24
    idx = [2 * r for r in range(1, 13)]
    return T[:, idx, :].sum(axis=2)        # (N,12) : F_2 .. F_24

def oddF(X, s):
    C = np.sqrt(np.clip(X, 0, 1))
    T = cheb(25, C)
    idx = [2 * r + 1 for r in range(0, 13)]
    return (s[None, :] * T[:, idx, :]).sum(axis=2)   # (N,13) : F_1 .. F_25

rng = np.random.default_rng(2026)
N = 20000
X = rng.uniform(0, 1, size=(N, 5))
def pen(X):
    return np.maximum(evenF(X) - 0.5, 0.0).sum(1)

print("=== A. feasible x in E_even (vectorised multistart descent, N=%d) ===" % N, flush=True)
best_p = pen(X); best_X = X.copy()
step = 0.25
for it in range(700):
    j = it % 5
    for d in (step, -step):
        Xt = X.copy(); Xt[:, j] = np.clip(X[:, j] + d, 0, 1)
        p = pen(Xt)
        imp = p < best_p
        best_p[imp] = p[imp]; best_X[imp] = Xt[imp]
        X = np.where(imp[:, None], Xt, X)
    if it % 70 == 69: step *= 0.6
print("   feasible starts: %d / %d  (pen == 0)" % (int((pen(best_X) <= 1e-12).sum()), N), flush=True)
ok = best_X[pen(best_X) <= 1e-12]
if len(ok):
    print("   empirical min_j x_j over feasible samples : %.6f" % float(ok.min()), flush=True)

print()
print("=== B. odd-frequency probe over the 16 sign classes ===", flush=True)
SIG = [np.array(list(b) + [1], dtype=float) for b in itertools.product([-1, 1], repeat=4)]
sample = ok if len(ok) else best_X[np.argsort(pen(best_X))[:200]]
g = np.full(len(sample), 1e9); bestsig = np.zeros((len(sample), 5))
for s in SIG:
    v = np.abs(oddF(sample, s)).max(1)
    imp = v < g
    g[imp] = v[imp]; bestsig[imp] = s
o = np.argsort(g)
print("   best 5 (g, x, sigma):", flush=True)
for i in o[:5]:
    print("     g = %.6f   x = %s   sigma = %s" % (g[i], np.round(sample[i], 5), bestsig[i].astype(int)), flush=True)
print("   BEST g = %.6f      (Bridge A target: inf g > 1/2)" % g[o[0]], flush=True)
print("   any g <= 1/2 (would REFUTE Bridge A) : %s" % bool(g[o[0]] <= 0.5), flush=True)

print()
print("=== C. local minimisation of g over x in E_even (vectorised, M=3000 starts) ===", flush=True)
M = 3000
Xc = np.clip(sample[rng.integers(0, len(sample), M)] + rng.normal(0, 0.03, (M, 5)), 0, 1)
def obj(Xc):
    G = np.full(len(Xc), 1e9)
    for s in SIG:
        G = np.minimum(G, np.abs(oddF(Xc, s)).max(1))
    return G + 3.0 * pen(Xc)
cur = obj(Xc); bestv = cur.copy(); bestX = Xc.copy(); step = 0.03
for it in range(700):
    j = it % 5
    for d in (step, -step):
        Xt = Xc.copy(); Xt[:, j] = np.clip(Xc[:, j] + d, 0, 1)
        v = obj(Xt)
        imp = v < cur
        cur = np.where(imp, v, cur); Xc = np.where(imp[:, None], Xt, Xc)
    if it % 70 == 69: step *= 0.6
k = int(np.argmin(cur))
print("   BEST g (penalised objective) = %.6f" % cur[k], flush=True)
print("   x = %s" % np.round(Xc[k], 6), flush=True)
print("   max(F_2r - 1/2) at that x = %.3e  (feasible if <= 0)" % float(np.max(evenF(Xc[k:k+1]) - 0.5)), flush=True)
print("   min_j x_j = %.6f" % float(Xc[k].min()), flush=True)
print("DONE", flush=True)
