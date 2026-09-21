# c380_55_gamma_knifeA_v2.py -- knife A (reconnaissance), fast sigma handling via matmul
import numpy as np, itertools
rng = np.random.default_rng(20260921)

def cheb(deg, Y):
    N, m = Y.shape
    out = [np.ones((N, m)), Y.copy()]
    for k in range(2, deg + 1):
        out.append(2 * Y * out[-1] - out[-2])
    return np.stack(out, axis=1)

S = np.array([list(b) + [1] for b in itertools.product([-1, 1], repeat=4)], dtype=float)
EVEN_IDX = [2 * r for r in range(1, 13)]
ODD_IDX = [2 * r + 1 for r in range(0, 13)]

def obj(X):
    Y = 2 * X - 1
    C = np.sqrt(np.clip(X, 0, 1))
    E = cheb(24, Y)[:, EVEN_IDX, :].sum(2)
    U = cheb(25, C)[:, ODD_IDX, :]
    G = np.abs(U @ S.T).max(axis=1).min(axis=1)
    return G + 30.0 * np.maximum(E - 0.5, 0.0).sum(1), G, E

def run(X0, iters, step0, tag, ck=100):
    X = X0.copy(); cur, _, _ = obj(X); best = cur.copy(); bestX = X.copy(); step = step0
    traj = []
    for it in range(iters):
        j = it % 5
        for d in (step, -step):
            Xt = X.copy(); Xt[:, j] = np.clip(X[:, j] + d, 0, 1)
            v, _, _ = obj(Xt)
            imp = v < cur
            cur = np.where(imp, v, cur); X = np.where(imp[:, None], Xt, X)
        imp = cur < best
        best = np.where(imp, cur, best); bestX[imp] = X[imp]
        if (it + 1) % ck == 0:
            step *= 0.7; traj.append((it + 1, float(best.min())))
    print("   [%s] trajectory: %s" % (tag, ["%d:%.4f" % t for t in traj]), flush=True)
    return best, bestX

def report(x, tag):
    _, G, E = obj(x[None, :])
    g = float(G[0]); emax = float(E[0].max()); nmax = int(np.argmax(E[0])) + 1
    c = np.sqrt(np.clip(x, 0, 1))
    sep_c = min(abs(c[i] - c[j]) for i in range(5) for j in range(i + 1, 5))
    print("   [%s] g = %.6f | min_j x_j = %.6f (dist to D_partial) | min |c_i-c_j| = %.6f (dist to D_coll)"
          % (tag, g, float(x.min()), sep_c), flush=True)
    print("        even slack: max_r F_2r = %.6f at r=%d ; margin 1/2 - max = %+.6f ; feasible = %s"
          % (emax, nmax, 0.5 - emax, emax <= 0.5), flush=True)
    print("        x = %s" % np.round(x, 6), flush=True)
    return g

print("=== phase 1: random starts (N=6000, 600 it) ===", flush=True)
b1, bx1 = run(rng.uniform(0, 1, size=(6000, 5)), 600, 0.25, "rand")
g1 = report(bx1[int(np.argmin(b1))], "phase1")
print("\n=== phase 2: degenerate-biased (near x_j=0 / near-coincident) ===", flush=True)
M = 6000; X0 = rng.uniform(0, 1, size=(M, 5)); h = M // 2
X0[:h] = rng.uniform(0, 0.08, size=(h, 5))
for i in range(h, M):
    base = rng.uniform(0.05, 0.95, 5); base[rng.integers(0, 5)] = base[rng.integers(0, 5)] + rng.normal(0, 1e-3)
    X0[i] = np.clip(base, 0, 1)
b2, bx2 = run(X0, 600, 0.10, "degen")
g2 = report(bx2[int(np.argmin(b2))], "phase2")
print("\n=== phase 3: fine refinement (N=1500, 1500 it, step 1e-2) ===", flush=True)
allb = np.concatenate([b1, b2]); allX = np.vstack([bx1, bx2]); sel = np.argsort(allb)[:1500]
Xr = np.clip(allX[sel] + rng.normal(0, 0.01, (len(sel), 5)), 0, 1)
b3, bx3 = run(Xr, 1500, 0.01, "fine", ck=250)
g3 = report(bx3[int(np.argmin(b3))], "refined")
print("\n=== summary ===", flush=True)
gb = min(g1, g2, g3)
print("   best g = %.6f   (C-3850 gave 0.876069)" % gb, flush=True)
v = np.sort(np.concatenate([b1, b2, b3]))
print("   multiplicity within 1e-3 of best = %d" % int((v < gb + 1e-3).sum()), flush=True)
print("DONE", flush=True)
