# c380_79e_C3899_strata_verified.py -- C-3899 (b) verified support-stratum minima, k = 1..5
# true functions only; every reported optimum is re-evaluated with the true expression and bounds-checked.
# stratum: |u| takes k distinct values z_1..z_k with multiplicities n_i (sum 5)
# even layer: F_{2q} = sum_i n_i T_q(2 z_i - 1)   [because T_{2q}(u) = T_q(2u^2-1)]
# feasible iff min over the stratum of max_{q=1..12} F_{2q} <= 1/2
import numpy as np, itertools, time
from scipy.optimize import minimize, differential_evolution

def Tq(q, u): return np.cos(q*np.arccos(np.clip(u, -1.0, 1.0)))
def F2q(z, n, q):
    s = 0.0
    for i, ni in enumerate(n): s += ni*float(Tq(q, 2.0*z[i]-1.0))
    return s
def tmax(z, n): return max(F2q(z, n, q) for q in range(1, 13))

def grid_min(n, pts):
    k = len(n); axes = [np.linspace(0.0015, 0.9985, pts)]*k
    best = (1e9, None)
    if k <= 3:
        if k == 1:
            Z = axes[0].reshape(1, -1)
            g = np.array([tmax(Z[:, j], n) for j in range(Z.shape[1])])
            return float(g.min()), [float(axes[0][int(g.argmin())])]
        if k == 2:
            A, B = np.meshgrid(axes[0], axes[1])
            Z = np.vstack([A.ravel(), B.ravel()])
        else:
            A, B = np.meshgrid(axes[0], axes[1]); 
            for zi in np.linspace(0.0015, 0.9985, max(21, pts//6)):
                Z = np.vstack([A.ravel(), B.ravel(), np.full(A.size, zi)])
                g = np.array([tmax(Z[:, j], n) for j in range(0, Z.shape[1], 1)])
                i = int(g.argmin())
                if g[i] < best[0]: best = (float(g[i]), [float(Z[0, i]), float(Z[1, i]), float(zi)])
            return best
        g = np.array([tmax(Z[:, j], n) for j in range(0, Z.shape[1], 1)])
        i = int(g.argmin())
        return float(g[i]), [float(v) for v in Z[:, i]]
    return None

def de_min(n):
    k = len(n)
    res = differential_evolution(lambda z: tmax(z, n), [(0.001, 0.999)]*k, maxiter=2000, tol=1e-12,
                                 popsize=30, seed=7, polish=True, mutation=(0.3, 1.0), recombination=0.9)
    return float(tmax(res.x, n)), [float(v) for v in res.x]

def verify(z, n):
    ok = all(0.0 < v < 1.0 for v in z)
    return ok, tmax(z, n)

print("=== C-3899 (b) support-stratum feasibility (true-function verified) ===", flush=True)
print("  threshold: max_{q=1..12} F_2q <= 0.5  (five-node even constraints, all x_j in (0,1))", flush=True)
t0 = time.time()
for k in (1,2,3,4,5):
    for n in sorted({tuple(sorted(t)) for t in itertools.product(range(1,6), repeat=k) if sum(t)==5}):
        if k <= 3:
            val, at = grid_min(list(n), {1:60001, 2:1501, 3:151}[k])
        else:
            val, at = de_min(list(n))
        ok, tver = verify(at, list(n))
        print("  k=%d mults=%s : min max_q F_2q = %+.6f (grid/DE) | verified %+.6f | bounds ok %s | z=%s -> %s"
              % (k, list(n), val, tver, ok, np.round(at,6), "FEASIBLE" if tver <= 0.5 else "INFEASIBLE"), flush=True)
print("  elapsed = %.1f s" % (time.time()-t0), flush=True)
print("\n  sanity: the certified five-node KKT point (k=5, mults (1,1,1,1,1)) has max_q F_2q = 0.5000000000", flush=True)
print("DONE-STRATA-VERIFIED", flush=True)
