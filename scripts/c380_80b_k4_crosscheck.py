# c380_80b_k4_crosscheck.py -- independent cross-check of the support-stratum minima by differential evolution
# objective g_m(z) = max_{q=1..12} sum_i m_i T_q(2 z_i - 1)  (z_i = u_i^2 in (0,1)) ; feasible iff min <= 0.5
import numpy as np, time
from scipy.optimize import differential_evolution, minimize

def Tq(q, u): return np.cos(q*np.arccos(np.clip(u, -1.0, 1.0)))
def g(z, m):
    z = np.asarray(z, float)
    return max(sum(m[i]*Tq(q, 2.0*z[i]-1.0) for i in range(len(m))) for q in range(1, 13))
def Fv(z, m): return np.array([sum(m[i]*Tq(q, 2.0*z[i]-1.0) for i in range(len(m))) for q in range(1,13)])

CASES = [(1,(5,)), (2,(1,4)), (2,(2,3)), (3,(1,1,3)), (3,(1,2,2)), (4,(1,1,1,2)), (5,(1,1,1,1,1))]
t0 = time.time()
print("=== independent cross-check (differential evolution + SLSQP polish) ===", flush=True)
for k, m in CASES:
    res = differential_evolution(lambda z: g(z, m), [(1e-6, 1-1e-6)]*k, maxiter=3000, tol=1e-13,
                                 popsize=45, seed=k*100+len(m), polish=False, mutation=(0.3,1.1), recombination=0.85,
                                 init='sobol')
    z = res.x
    # SLSQP polish with auxiliary variable
    cons = [{'type':'ineq','fun': (lambda Z,q=q: Z[k] - sum(m[i]*Tq(q, 2.0*Z[i]-1.0) for i in range(k)))} for q in range(1,13)]
    r = minimize(lambda Z: Z[k], np.concatenate([z,[g(z,m)]]), method='SLSQP',
                 bounds=[(1e-6,1-1e-6)]*k+[(None,None)], constraints=cons, options={'maxiter':500,'ftol':1e-15})
    zp = r.x[:k]; v = g(zp, m)
    act = [q for q in range(1,13) if abs(Fv(zp,m)[q-1]-v) < 1e-8]
    print("  k=%d m=%s : DE min = %+.6f | polished = %+.6f | margin = %+.6f | active q = %s | z = %s -> %s"
          % (k, list(m), g(z,m), v, v-0.5, act, np.round(zp,6), "FEASIBLE" if v<=0.5 else "INFEASIBLE"), flush=True)
    print("      F_2q = %s" % np.round(Fv(zp,m),6), flush=True)
print("  elapsed = %.1f s" % (time.time()-t0), flush=True)
print("DONE-XCHECK", flush=True)
