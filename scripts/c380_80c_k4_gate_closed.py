# c380_80c_k4_gate_closed.py -- C-3900 Gate, corrected: minimisation over the CLOSED domain z in [0,1]^k
# (earlier runs used z in (0,1) and multi-start SLSQP, which missed boundary basins: a node with u = 0
#  contributes T_q(-1) = (-1)^q, i.e. an alternating sequence, which is a strong moment-cancelling tool.)
# stratum with weights m (sum 5): F_{2q}(z) = sum_i m_i T_q(2 z_i - 1) ; feasible iff min max_q F_2q <= 0.5
import numpy as np, time, itertools
from scipy.optimize import minimize, differential_evolution
def Tq(q, u): return np.cos(q*np.arccos(np.clip(u, -1.0, 1.0)))
def gv(Z, m):
    out = np.full(Z.shape[1], -1e9)
    for q in range(1, 13):
        v = np.zeros(Z.shape[1])
        for i, mi in enumerate(m): v += mi*Tq(q, 2.0*Z[i]-1.0)
        out = np.maximum(out, v)
    return out
def g(z, m): return float(gv(np.asarray(z, float).reshape(-1, 1), m)[0])
def Fv(z, m): return np.array([sum(m[i]*Tq(q, 2.0*z[i]-1.0) for i in range(len(m))) for q in range(1,13)])

def polish(z, m):
    k = len(m); z = np.asarray(z, float)
    cons = [{'type':'ineq','fun': (lambda Z,q=q: Z[k] - sum(m[i]*Tq(q, 2.0*Z[i]-1.0) for i in range(k)))} for q in range(1,13)]
    r = minimize(lambda Z: Z[k], np.concatenate([z,[g(z,m)]]), method='SLSQP',
                 bounds=[(0.0,1.0)]*k+[(None,None)], constraints=cons, options={'maxiter':600,'ftol':1e-15})
    zp = np.clip(r.x[:k], 0.0, 1.0)
    return zp, g(zp, m)

def stratum_min(m, N=49, topk=300, seed=0):
    k = len(m); ax = np.linspace(0.0, 1.0, N)
    if k == 1:
        Z = ax.reshape(1, -1); v = gv(Z, m); order = np.argsort(v)[:topk]
        best = (1e9, None)
        for j in order:
            zp, vv = polish(ax[j:j+1], m)
            if vv < best[0]: best = (vv, zp)
        return best
    grids = np.meshgrid(*([ax]*(k-1)), indexing='ij'); flat = [G.ravel() for G in grids]; blk = flat[0].size
    vals, pts = [], []
    for xi in ax:
        Z = np.vstack(flat+[np.full(blk, xi)]); v = gv(Z, m)
        idx = np.argsort(v)[:max(1, topk//N)]
        vals.append(v[idx]); pts.append(Z[:, idx])
    V = np.concatenate(vals); P = np.hstack(pts)
    order = np.argsort(V)[:topk]
    best = (1e9, None)
    for j in order:
        zp, v = polish(P[:, j], m)
        if v < best[0]: best = (v, zp)
    # global DE over the closed box as a cross-check
    de = differential_evolution(lambda z: g(z, m), [(0.0,1.0)]*k, maxiter=2500, tol=1e-13, popsize=45,
                                seed=seed+1, polish=False, init='sobol')
    vde = g(de.x, m)
    if vde < best[0]: best = (vde, de.x)
    return best

CASES = [(1,(5,)), (2,(1,4)), (2,(2,3)), (3,(1,1,3)), (3,(1,2,2)), (4,(2,1,1,1)), (5,(1,1,1,1,1))]
t0 = time.time()
print("=== C-3900 Gate (corrected): stratum minima over the CLOSED domain z in [0,1]^k ===", flush=True)
print("  note: z_i = 0 <-> u_i = 0 <-> x_i = 1/2 (an allowed interior point of the x-domain)", flush=True)
res = {}
for k, m in CASES:
    N = {1: 2001, 2: 401, 3: 121, 4: 49, 5: 1}[k]
    if k <= 4:
        v, z = stratum_min(list(m), N=N, topk=150 if k == 4 else 60)
    else:
        de = differential_evolution(lambda z: g(z, m), [(0.0,1.0)]*5, maxiter=3000, tol=1e-13, popsize=45,
                                    seed=5, polish=False, init='sobol')
        z, v = de.x, g(de.x, m); z, v = polish(z, m)
    res[(k,m)] = (v, z)
    act = [q for q in range(1,13) if abs(Fv(z, m)[q-1]-v) < 1e-8]
    print("  k=%d m=%s : min max_q F_2q = %+.6f | margin vs 0.5 = %+.6f | active q = %s | #z at 0 boundary = %d | z = %s -> %s"
          % (k, list(m), v, v-0.5, act, int(np.sum(np.array(z) < 1e-9)), np.round(z,6),
             "FEASIBLE" if v <= 0.5 else "INFEASIBLE"), flush=True)
    print("      F_2q = %s" % np.round(Fv(z, m), 6), flush=True)
print("\n=== VERDICT ===", flush=True)
mins = {k: min(v for (kk,m),(v,z) in res.items() if kk==k) for k in range(1,6)}
for k in range(1,6): print("  k=%d : %+.6f -> %s" % (k, mins[k], "FEASIBLE" if mins[k] <= 0.5 else "INFEASIBLE"), flush=True)
lb = min(k for k in range(1,6) if mins[k] <= 0.5)
print("  ==> support lower bound (numerical): k >= %d" % lb, flush=True)
print("  elapsed = %.1f s" % (time.time()-t0), flush=True)
print("DONE-CLOSED", flush=True)
