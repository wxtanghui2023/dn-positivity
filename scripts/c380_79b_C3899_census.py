# c380_79b_C3899_census.py -- C-3899: bounded candidate census over the 16 sign layers (five-node problem)
# model: phi in (0,pi/2)^5 ; x=cos^2 phi ; u=cos2phi=2x-1 ; z=u^2
#   constr: F_{4q}(c)=sum_j cos(4q phi_j) <= 1/2 , q=1..12
#   obj   : f_sigma = max_{r=0..12} |sum_j sigma_j cos((2r+1) phi_j)|
# record: k = #{distinct z_j} for every candidate extremal configuration found.
import numpy as np, itertools, collections, time
from scipy.optimize import minimize
HALF = np.pi/2
rng = np.random.default_rng(7922)

def Fe(phi, q): return float(np.sum(np.cos(4*q*phi)))
def Fo(phi, s, r): return float(np.sum(s*np.cos((2*r+1)*phi)))
def viol(phi): return max(Fe(phi,q)-0.5 for q in range(1,13))

def solve_one(s, phi0, t0=None):
    """minimize t s.t. |F_odd,r| <= t, F_even <= 1/2, phi in [0,pi/2]"""
    if t0 is None: t0 = max(abs(Fo(phi0, s, r)) for r in range(13))
    z0 = np.concatenate([phi0, [t0]])
    cons = [{'type':'ineq','fun': (lambda z,q=q: 0.5 - Fe(z[:5],q))} for q in range(1,13)]
    cons += [{'type':'ineq','fun': (lambda z,r=r: z[5] - Fo(z[:5], s, r))} for r in range(13)]
    cons += [{'type':'ineq','fun': (lambda z,r=r: z[5] + Fo(z[:5], s, r))} for r in range(13)]
    r_ = minimize(lambda z: z[5], z0, method='SLSQP', bounds=[(0.0,HALF)]*5+[(0.0,None)],
                  constraints=cons, options={'maxiter':300,'ftol':1e-13})
    return r_.x[:5], float(r_.x[5])

def stats(phi, s):
    u = np.cos(2*phi); x = np.cos(phi)**2; z = u**2
    ov = np.array([Fo(phi,s,r) for r in range(13)]); t = float(np.abs(ov).max())
    marg = np.array([0.5-Fe(phi,q) for q in range(1,13)])
    ks = {}
    for tol in (1e-5, 1e-7, 1e-9):
        zs = np.sort(z); d=[]
        for v in zs:
            if not d or abs(v-d[-1]) > tol: d.append(v)
        ks[tol] = len(d)
    A = [q for q in range(1,13) if abs(marg[q-1]) <= 1e-6]
    I = [r for r in range(13) if abs(abs(ov[r])-t) <= 1e-6]
    return dict(u=u, x=x, z=z, t=t, ks=ks, A=A, I=I, viol=float(-marg.min()),
                minx=float(x.min()), pairgap=float(min(min(abs(u[i]-u[j]),abs(u[i]+u[j]))
                                                      for i in range(5) for j in range(i+1,5))))

SEEDS = [np.arccos(np.sqrt(np.array(v))) for v in
         ([0.80093022,0.5611432,0.70245716,0.6261014,0.86884389],
          [0.801874,0.561119,0.703473,0.627211,0.869546],
          [0.702989,0.873806,0.797976,0.551115,0.628434])]

t_start = time.time()
all_k = collections.Counter(); per_sigma = {}
best_overall = None
print("=== C-3899 candidate census: 16 sign layers x multi-start ===", flush=True)
for si, b in enumerate(itertools.product([-1,1], repeat=4)):
    s = np.array(list(b)+[1], dtype=float)
    cands = []
    starts = list(SEEDS)
    starts.append(np.full(5, np.pi/5))
    for _ in range(22):
        starts.append(rng.uniform(0.15, HALF-0.15, 5))
    for phi0 in starts:
        try:
            phi, t = solve_one(s, phi0)
        except Exception as e:
            continue
        st = stats(phi, s)
        if st['viol'] <= 1e-8:            # certified-feasible candidate
            cands.append(st)
            all_k[st['ks'][1e-7]] += 1
    if not cands:
        print("  sigma=%s : no certified candidate" % list(s.astype(int)), flush=True); continue
    best = min(cands, key=lambda d: d['t'])
    per_sigma[tuple(s.astype(int))] = best
    klist = sorted(collections.Counter(c['ks'][1e-7] for c in cands).items())
    print("  sigma=%s : n_cand=%2d | best t=%.9f k=%d (tol1e-9:%d) A=%s I=%s | k-hist=%s"
          % (list(s.astype(int)), len(cands), best['t'], best['ks'][1e-7], best['ks'][1e-9],
             best['A'], best['I'], klist), flush=True)
    if best['ks'][1e-7] <= 3:
        print("      *** COMPRESSED CANDIDATE *** z=%s u=%s minx=%.3e pairgap=%.3e"
              % (np.round(np.sort(best['z']),10), np.round(best['u'],10), best['minx'], best['pairgap']), flush=True)
    if best_overall is None or best['t'] < best_overall['t']: best_overall = best

print("\n=== summary ===", flush=True)
print("  global best t = %.9f ; k = %d ; A=%s ; I=%s" % (best_overall['t'], best_overall['ks'][1e-7],
      best_overall['A'], best_overall['I']), flush=True)
print("  z (sorted) = %s" % np.round(np.sort(best_overall['z']), 12), flush=True)
print("  u = %s" % np.round(best_overall['u'], 12), flush=True)
print("  k-histogram over all certified candidates (tol 1e-7): %s"
      % sorted(all_k.items()), flush=True)
print("  min k observed = %d ; any k<=3 ? %s" % (min(all_k), [kk for kk in all_k if kk<=3]), flush=True)
print("  elapsed = %.1f s" % (time.time()-t_start), flush=True)
print("DONE-CENSUS", flush=True)
