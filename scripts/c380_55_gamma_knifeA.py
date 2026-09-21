# c380_55_gamma_knifeA.py -- knife A (reconnaissance): tighten gamma^(13) under the even constraints
import numpy as np, itertools
rng = np.random.default_rng(20260921)

def cheb(deg, Y):
    N, m = Y.shape
    out = [np.ones((N, m)), Y.copy()]
    for k in range(2, deg + 1):
        out.append(2 * Y * out[-1] - out[-2])
    return np.stack(out, axis=1)          # (N, deg+1, m)

SIG = [np.array(list(b) + [1], dtype=float) for b in itertools.product([-1, 1], repeat=4)]
EVEN_IDX = [2 * r for r in range(1, 13)]
ODD_IDX = [2 * r + 1 for r in range(0, 13)]

def parts(X):
    Y = 2 * X - 1
    C = np.sqrt(np.clip(X, 0, 1))
    E = cheb(24, Y)[:, EVEN_IDX, :].sum(2)      # (N,12) F_2..F_24
    U = cheb(25, C)[:, ODD_IDX, :]              # (N,13,5) T_{2r+1}(c_j)
    G = np.full(X.shape[0], 1e9)
    for s in SIG:
        G = np.minimum(G, np.abs((s[None, None, :] * U).sum(2)).max(1))
    return G, E

def obj(X):
    G, E = parts(X)
    return G + 30.0 * np.maximum(E - 0.5, 0.0).sum(1), G, E

def run(X0, iters, step0, tag):
    X = X0.copy(); cur, _, _ = obj(X); best = cur.copy(); bestX = X.copy(); step = step0
    traj = []
    for it in range(iters):
        j = it % 5
        for d in (step, -step):
            Xt = X.copy(); Xt[:, j] = np.clip(X[:, j] + d, 0, 1)
            v, _, _ = obj(Xt)
            imp = v < cur
            cur = np.where(imp, v, cur); X = np.where(imp[:, None], Xt, X)
        if it % 100 == 99:
            step *= 0.7
            traj.append((it + 1, float(best.min())))
        imp = cur < best
        best = np.where(imp, cur, best); bestX[imp] = X[imp]
    print("   [%s] checkpoints: %s" % (tag, ["%d:%.4f" % t for t in traj]), flush=True)
    return best, bestX

def report(x, tag):
    G, E = parts(x[None, :])
    g = float(G[0]); emax = float(E[0].max()); nmax = int(np.argmax(E[0])) + 1
    c = np.sqrt(np.clip(x, 0, 1))
    sep_c = min(abs(c[i] - c[j]) for i in range(5) for j in range(i + 1, 5))
    sep_x = min(abs(x[i] - x[j]) for i in range(5) for j in range(i + 1, 5))
    print("   [%s] g = %.6f | min_j x_j = %.6f (dist to D_partial) | min sep in c = %.6f, in x = %.6f (dist to D_coll)"
          % (tag, g, float(x.min()), sep_c, sep_x), flush=True)
    print("        even slack: max_r F_2r = %.6f at r=%d ; margin to 1/2 = %+.6f" % (emax, nmax, 0.5 - emax), flush=True)
    print("        x = %s" % np.round(x, 6), flush=True)
    return g

print("=== phase 1: random starts (N=20000) ===", flush=True)
X0 = rng.uniform(0, 1, size=(20000, 5))
b1, bx1 = run(X0, 800, 0.25, "rand")
g1 = report(bx1[int(np.argmin(b1))], "phase1-best")

print()
print("=== phase 2: degenerate-biased starts (near D_partial / D_coll) ===", flush=True)
M = 20000
X0 = rng.uniform(0, 1, size=(M, 5))
h = M // 2
X0[:h] = rng.uniform(0, 0.08, size=(h, 5))                      # near x_j = 0
for i in range(h, M):                                            # near-coincident pairs
    base = rng.uniform(0.05, 0.95, 5)
    base[rng.integers(0, 5)] = base[rng.integers(0, 5)] + rng.normal(0, 1e-3)
    X0[i] = np.clip(base, 0, 1)
b2, bx2 = run(X0, 800, 0.10, "degen")
g2 = report(bx2[int(np.argmin(b2))], "phase2-best")

print()
print("=== refinement of the overall best (N=4000, fine steps) ===", flush=True)
allb = np.concatenate([b1, b2]); allX = np.vstack([bx1, bx2])
sel = np.argsort(allb)[:4000]
Xr = np.clip(allX[sel] + rng.normal(0, 0.02, (len(sel), 5)), 0, 1)
b3, bx3 = run(Xr, 2500, 0.03, "fine")
k = int(np.argmin(b3)); g3 = report(bx3[k], "refined-best")

print()
print("=== summary ===", flush=True)
print("   best g found = %.6f   (previous C-3850 value was 0.876069)" % min(g1, g2, g3), flush=True)
vals = np.sort(np.concatenate([b1, b2, b3]))
near = vals[vals < min(g1, g2, g3) + 1e-3]
print("   #configurations within 1e-3 of the best (multiplicity) = %d" % len(near), flush=True)
print("DONE", flush=True)
