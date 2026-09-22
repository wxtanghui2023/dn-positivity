# c380_81_aset_census.py -- C-3900 analytic Gate:
#   (A) active-set enumeration census for every multiplicity pattern (systematic local-min catalogue)
#   (B) reduced z_i = 0 boundary sub-problems for the binding pattern (2,1,1,1)  [dense grid + refine]
#   (C) analytic remark on z_i = 1: contribution m_i*T_q(1) = m_i >= 1 > 1/2 for EVERY q  ==>  trivially infeasible
# Model: F_q(z) = sum_i m_i T_q(2 z_i - 1),  q = 1..12  (even layer on a stratum; T_{2q}(u) = T_q(2u^2-1))
#   feasible iff min max_q F_q <= 1/2.   At a local min with active set Q (|Q| = r):
#     F_q(z) = t (q in Q)                     : r eqs
#     sum_{q in Q} lam_q grad F_q(z) = 0      : k eqs   (lam >= 0, sum lam = 1)
#   unknowns [z (k), lam_1..lam_{r-1}, t] = k + r  ==> square system for every r.
import numpy as np, itertools, time
from scipy.optimize import root, minimize

def Tq(q, u): return np.cos(q*np.arccos(np.clip(u, -1.0, 1.0)))
def U(n, w):
    th = np.arccos(np.clip(w, -1.0, 1.0)); s = np.sin(th)
    return np.where(np.abs(s) < 1e-12, 0.0, np.sin((n+1)*th)/np.maximum(s, 1e-300))
def Fq(z, m, q): return float(sum(m[i]*Tq(q, 2.0*z[i]-1.0) for i in range(len(m))))
def Fv(z, m): return np.array([Fq(z, m, q) for q in range(1, 13)])
def gmax(z, m): return float(Fv(z, m).max())
def gradF(z, m, q): return np.array([m[i]*2.0*q*U(q-1, 2.0*z[i]-1.0) for i in range(len(m))])

def solve_active(m, Q, z0=None, seed=0):
    k = len(m); r = len(Q); rng = np.random.default_rng(seed)
    if z0 is None: z0 = rng.uniform(0.02, 0.98, k)
    lam0 = rng.uniform(0, 1, max(1, r-1)); lam0 = lam0/np.sum(lam0)*0.5 if r > 1 else np.array([])
    t0 = gmax(z0, m)
    x0 = np.concatenate([z0, lam0, [t0]])
    def f(x):
        z = x[:k]; lam = x[k:k+r-1]; t = x[k+r-1]
        L = np.append(lam, 1.0-np.sum(lam))
        res = [Fq(z, m, q) - t for q in Q]
        acc = np.zeros(k)
        for j, q in enumerate(Q): acc += L[j]*gradF(z, m, q)
        return np.concatenate([res, acc])
    try:
        s = root(f, x0, method='hybr')
    except Exception:
        return None
    if not np.all(np.isfinite(s.x)) or np.abs(f(s.x)).max() > 1e-9: return None
    z = np.clip(s.x[:k], 0.0, 1.0); lam = s.x[k:k+r-1]; L = np.append(lam, 1.0-np.sum(lam))
    if np.any(L < -1e-9): return None                      # not a min (wrong sign multipliers)
    if np.max(np.abs(z - s.x[:k])) > 1e-9: return None      # solution outside the box
    t = Fq(z, m, Q[0])
    if abs(t - gmax(z, m)) > 1e-8: return None              # some other constraint exceeds t
    return dict(z=z, lam=L, t=t, Q=Q)

def census(m, r_extra=(0,), nstart=25, seed=0):
    k = len(m); best = None; allpts = []
    for r in [k+j for j in r_extra]:
        if r > 12: continue
        for Q in itertools.combinations(range(1, 13), r):
            for s in range(nstart):
                c = solve_active(m, Q, seed=seed+1000*s+7*sum(Q)+r)
                if c is None: continue
                allpts.append(c)
                if best is None or c['t'] < best['t']: best = c
    return best, allpts

print("=== (A) active-set enumeration census (systematic local-min catalogue) ===", flush=True)
t0 = time.time(); summary = {}
for m in [(5,), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1)]:
    b, pts = census(list(m), r_extra=(0, 1) if len(m) <= 3 else (0,), nstart=20 if len(m) <= 4 else 12,
                    seed=int(sum(m)*13+len(m)))
    if b is None: print("  %s : no valid stationary point found" % (list(m),), flush=True); continue
    summary[tuple(m)] = b
    print("  m=%s : best stationary t = %+.8f | margin = %+.8f | active Q = %s | z = %s | #cands = %d | %s"
          % (list(m), b['t'], b['t']-0.5, list(b['Q']), np.round(b['z'], 8), len(pts),
             "FEASIBLE" if b['t'] <= 0.5 else "INFEASIBLE"), flush=True)
print("  (A) elapsed %.0f s" % (time.time()-t0), flush=True)

print("\n=== (B) reduced boundary sub-problems for the binding pattern (2,1,1,1): one coordinate pinned at z=0 ===", flush=True)
def g_pinned(z, m, pin_idx):
    zz = np.array(z, float); zz[pin_idx] = 0.0
    return gmax(zz, m)
for pin_idx, note in [(0, "weight-2 coordinate at 0  =>  2*(-1)^q + sum of three weight-1 terms"),
                      (1, "a weight-1 coordinate at 0  =>  (-1)^q + 2*T_q(u1) + two weight-1 terms")]:
    m = [2,1,1,1]; k = 4; free = [j for j in range(k) if j != pin_idx]
    # dense grid over the 3 free coordinates (closed box)
    N = 161; ax = np.linspace(0, 1, N)
    A, B = np.meshgrid(ax, ax); best = (1e9, None)
    for xi in ax:
        Z = np.vstack([A.ravel(), B.ravel(), np.full(A.size, xi)])
        zz = np.empty((4, Z.shape[1])); 
        for a, j in enumerate(free): zz[j] = Z[a]
        zz[pin_idx] = 0.0
        V = np.full(Z.shape[1], -1e9)
        for q in range(1, 13):
            v = np.zeros(Z.shape[1])
            for i, mi in enumerate(m): v += mi*Tq(q, 2.0*zz[i]-1.0)
            V = np.maximum(V, v)
        i = int(V.argmin())
        if V[i] < best[0]: best = (float(V[i]), zz[:, i].copy())
    # refine
    z0 = best[1]
    cons = [{'type':'ineq','fun': (lambda Z,q=q: Z[4]-sum(m[i]*Tq(q,2.0*Z[i]-1.0) for i in range(4)))} for q in range(1,13)]
    r_ = minimize(lambda Z: Z[4], np.concatenate([z0, [best[0]]]), method='SLSQP',
                  bounds=[(0.0,1.0)]*4+[(None,None)], constraints=cons, options={'maxiter':600,'ftol':1e-15})
    zr = np.clip(r_.x[:4], 0, 1); zr[pin_idx] = 0.0; vr = gmax(zr, m)
    if vr < best[0]: best = (vr, zr)
    # active-set census on the reduced (pinned) problem
    b2, _ = census(list(m), r_extra=(0,), nstart=25, seed=pin_idx+5)
    print("  pin z_%d = 0 : %s" % (pin_idx, note), flush=True)
    print("      dense grid(N=%d)+refine : min max_q F_2q = %+.8f | margin = %+.8f | z = %s -> %s"
          % (N, best[0], best[0]-0.5, np.round(best[1], 8), "FEASIBLE" if best[0] <= 0.5 else "INFEASIBLE"), flush=True)
    print("      (free census over the whole 4-box for reference: %+.8f)" % b2['t'], flush=True)
print("\n=== (C) z_i = 1 faces: contribution m_i*T_q(1) = m_i >= 1 > 1/2 for every q ==> rigorously INFEASIBLE ===", flush=True)
print("  (analytic; no computation needed).  Hence only the z = 0 faces need analysis.", flush=True)
print("\n=== SUMMARY ===", flush=True)
print("  best over all patterns/candidates : %s" % ", ".join("%s -> %+.6f" % (list(m), b['t']) for m, b in summary.items()), flush=True)
print("DONE-ASET-CENSUS", flush=True)
