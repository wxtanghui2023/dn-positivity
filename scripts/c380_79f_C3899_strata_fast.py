# c380_79f_C3899_strata_fast.py -- C-3899 (b) FINAL: vectorized verified support-stratum minima (k=1..5)
# stratum k with multiplicities n: F_{2q} = sum_i n_i * T_q(2 z_i - 1)  (T_{2q}(u) = T_q(2u^2-1), T_{2q} even)
# minimax g(z) = max_{q=1..12} F_{2q}(z) ; feasible iff min g <= 0.5
import numpy as np, itertools
from scipy.optimize import minimize

QS = np.arange(1, 13)
def Tq(q, u): return np.cos(q*np.arccos(np.clip(u, -1.0, 1.0)))
def g_vec(Z, n):
    """Z: (k, N) ; returns (N,) max over q"""
    out = np.full(Z.shape[1], -1e9)
    for q in QS:
        val = np.zeros(Z.shape[1])
        for i, ni in enumerate(n): val += ni*Tq(q, 2.0*Z[i]-1.0)
        out = np.maximum(out, val)
    return out
def g_pt(z, n): return float(g_vec(np.asarray(z).reshape(-1,1), n)[0])

def grid_min(n, pts, chunk=400_000):
    k = len(n)
    if k <= 3:
        ax = np.linspace(0.002, 0.998, pts)
        if k == 1:
            Z = ax.reshape(1,-1); g = g_vec(Z, n); i = int(g.argmin()); return float(g[i]), [float(ax[i])]
        if k == 2:
            A, B = np.meshgrid(ax, ax); Z = np.vstack([A.ravel(), B.ravel()])
        else:
            best = (1e9, None)
            A, B = np.meshgrid(ax, ax); AB = np.vstack([A.ravel(), B.ravel()])
            for zi in ax:
                Z = np.vstack([AB, np.full(AB.shape[1], zi)])
                g = g_vec(Z, n); i = int(g.argmin())
                if g[i] < best[0]: best = (float(g[i]), [float(Z[0,i]), float(Z[1,i]), float(zi)])
            return best
        g = np.empty(Z.shape[1])
        for s in range(0, Z.shape[1], chunk):
            e = min(s+chunk, Z.shape[1]); g[s:e] = g_vec(Z[:, s:e], n)
        i = int(g.argmin()); return float(g[i]), [float(v) for v in Z[:, i]]
    return None

def multistart(n, starts=None, n_rand=4000, seed=99):
    k = len(n); rng = np.random.default_rng(seed)
    cand = list(starts) if starts else []
    cand += [rng.uniform(0.02, 0.98, k) for _ in range(n_rand)]
    pen = lambda z: g_pt(z, n) + 1e6*(np.sum(np.maximum(0.0, -np.asarray(z))) + np.sum(np.maximum(0.0, np.asarray(z)-1.0)))
    best = (1e9, None)
    for z0 in cand:
        r_ = minimize(pen, z0, method='Nelder-Mead', options={'maxiter':1500,'xatol':1e-12,'fatol':1e-14})
        z = np.clip(r_.x, 0.0, 1.0)
        v = g_pt(z, n)                      # TRUE-function verification
        if v < best[0]: best = (v, list(z))
    return best

XS = np.array([0.80093022,0.5611432,0.70245716,0.6261014,0.86884389])
u_cert = np.cos(2*np.arccos(np.sqrt(XS))); z_cert = u_cert**2

print("=== C-3899 (b) FINAL: verified support-stratum minima (true function) ===", flush=True)
print("  threshold 0.5 ; stratum k = number of distinct |u_j| = number of distinct z_j", flush=True)
for k in (1,2,3,4,5):
    for n in sorted({tuple(sorted(t)) for t in itertools.product(range(1,6), repeat=k) if sum(t)==5}):
        if k == 1: val, at = grid_min(list(n), 60001)
        elif k == 2: val, at = grid_min(list(n), 2001)
        elif k == 3: val, at = grid_min(list(n), 201)
        else:
            st = [np.sort(z_cert)] if k == 5 else []
            val, at = multistart(list(n), starts=st, n_rand=3000 if k == 4 else 2500)
        ver = g_pt(at, n)
        print("  k=%d mults=%s : min max_q F_2q = %+.6f | verified %+.6f | z=%s -> %s"
              % (k, list(n), val, ver, np.round(at, 6), "FEASIBLE" if ver <= 0.5 else "INFEASIBLE"), flush=True)
print("\n  control: certified configuration z = %s -> max_q F_2q = %.10f (must be exactly 0.5)"
      % (np.round(np.sort(z_cert),8), g_pt(np.sort(z_cert), [1,1,1,1,1])), flush=True)
print("DONE-STRATA-FAST", flush=True)
