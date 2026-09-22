# c380_80_k4_gate.py -- C-3900 Gate: k = 4 support-stratum gate (decisive), with k = 1..5 controls
# stratum with weights m (length k, sum 5): F_{2q}(z) = sum_i m_i * T_q(2 z_i - 1)     [z_i = u_i^2 in (0,1)]
#   because T_{2q}(u) = T_q(2u^2 - 1) and T_{2q} is even  ==> even layer is blind to signs and to which
#   absolute value carries which multiplicity beyond the multiset.
# objective g_m(z) = max_{q=1..12} F_{2q}(z) ; stratum is even-feasible iff  min g_m <= 0.5
# method: (i) chunked brute-force grid, (ii) SLSQP refinement with auxiliary variable, (iii) TRUE-function verify
import numpy as np, itertools, time
from scipy.optimize import minimize

def Tq(q, u): return np.cos(q*np.arccos(np.clip(u, -1.0, 1.0)))
def Fq_vec(Z, m, q):
    v = np.zeros(Z.shape[1])
    for i, mi in enumerate(m): v += mi*Tq(q, 2.0*Z[i]-1.0)
    return v
def g_vec(Z, m):
    out = np.full(Z.shape[1], -1e9)
    for q in range(1, 13): out = np.maximum(out, Fq_vec(Z, m, q))
    return out
def g_pt(z, m): return float(g_vec(np.asarray(z, float).reshape(-1, 1), m)[0])
def Fvec(z, m): return np.array([Fq_vec(np.asarray(z,float).reshape(-1,1), m, q)[0] for q in range(1,13)])

def grid_scan(m, N):
    k = len(m); ax = np.linspace(0.5/N, 1.0-0.5/N, N)
    best = (1e9, None)
    if k == 1:
        Z = ax.reshape(1, -1); g = g_vec(Z, m); i = int(g.argmin())
        return float(g[i]), [float(ax[i])]
    grids = np.meshgrid(*([ax]*(k-1)), indexing='ij')          # (k-1)-dim mesh
    flat = [G.ravel() for G in grids]; block = flat[0].size
    for xi in ax:                                              # chunk over the last axis
        Z = np.vstack(flat + [np.full(block, xi)])
        g = g_vec(Z, m); i = int(g.argmin())
        if g[i] < best[0]: best = (float(g[i]), [float(v) for v in Z[:, i]])
    return best

def refine(m, z0, tight=True):
    k = len(m); z0 = np.asarray(z0, float)
    t0 = g_pt(z0, m)
    cons = [{'type': 'ineq', 'fun': (lambda Z, q=q: Z[k] - Fq_vec(Z[:k].reshape(-1,1), m, q)[0])} for q in range(1,13)]
    r = minimize(lambda Z: Z[k], np.concatenate([z0, [t0]]), method='SLSQP',
                 bounds=[(1e-6, 1-1e-6)]*k + [(0.0, None)], constraints=cons,
                 options={'maxiter':400, 'ftol':1e-14})
    z = np.clip(r.x[:k], 1e-6, 1-1e-6)
    return z, g_pt(z, m)                       # TRUE-function verification

CERT = np.sort(np.cos(2*np.arccos(np.sqrt(np.array([0.80093022,0.5611432,0.70245716,0.6261014,0.86884389]))))**2)
cands = {1: [(5,)], 2: [(1,4), (2,3)], 3: [(1,1,3), (1,2,2)], 4: [(1,1,1,2)], 5: [(1,1,1,1,1)]}
rng = np.random.default_rng(3900)
t_start = time.time()
print("=== C-3900 Gate: support-stratum minima (threshold 0.5) ===", flush=True)
print("  control: certified k=5 configuration gives max_q F_2q = %.10f" % g_pt(CERT, (1,1,1,1,1)), flush=True)
results = {}
for k in (1,2,3,4,5):
    for m in cands[k]:
        N = {1: 40001, 2: 1501, 3: 121, 4: 47}[k]
        val, at = grid_scan(list(m), N) if k <= 4 else (1e9, None)
        best = (min(val, 1e9), at) if at is not None else (1e9, None)
        # structured + random multi-start refinement
        seeds = []
        if best[1] is not None: seeds.append(best[1])
        if k >= 4:                                   # merge two closest |u| of the certified config
            zz = np.sort(CERT); d = np.diff(zz); j = int(np.argmin(d))
            seeds.append(np.delete(zz, j+1))
        if k == 5: seeds.append(np.sort(CERT))
        for _ in range(2500 if k >= 4 else 400):
            seeds.append(rng.uniform(0.005, 0.995, k))
        bv, bz = 1e9, None
        for s in seeds:
            z, v = refine(list(m), s)
            if v < bv: bv, bz = v, z
        if best[1] is not None and g_pt(best[1], m) < bv: bv, bz = g_pt(best[1], m), best[1]
        results[(k, m)] = (bv, bz)
        act = [q for q in range(1,13) if abs(Fvec(bz, m)[q-1] - bv) < 1e-9]
        print("  k=%d m=%s : min max_q F_2q = %+.6f | grid %s | margin vs 0.5 = %+.6f | active q = %s | z = %s -> %s"
              % (k, list(m), bv, ("%+.3f" % val) if val < 1e8 else "n/a", bv-0.5, act, np.round(bz,6),
                 "FEASIBLE" if bv <= 0.5 else "INFEASIBLE"), flush=True)
        print("      F_2q at optimum = %s" % np.round(Fvec(bz, m), 6), flush=True)
print("\n=== VERDICT (numerical) ===", flush=True)
mins = {k: min(v for (kk, m), (v, z) in results.items() if kk == k) for k in range(1, 6)}
for k in range(1, 6): print("  min over k=%d stratum : %+.6f -> %s" % (k, mins[k], "FEASIBLE" if mins[k] <= 0.5 else "INFEASIBLE"), flush=True)
print("  ==> support lower bound (numerical): k >= %d" % min(k for k in range(1,6) if mins[k] <= 0.5), flush=True)
print("  elapsed = %.1f s" % (time.time()-t_start), flush=True)
print("DONE-K4-GATE", flush=True)
