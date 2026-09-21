# c380_61_B1alpha3FR.py -- B1-alpha-3-FR: feasibility recovery (independent object) + per-sigma V_sigma
import numpy as np, itertools
from scipy.optimize import linprog, minimize
rng = np.random.default_rng(6133)
SIG = [np.array(list(b)+[1], dtype=float) for b in itertools.product([-1,1], repeat=4)]
HALF = np.pi/2

def Fodd(phi, s, r): return float(np.sum(s*np.cos((2*r+1)*phi)))
def Feven(phi, r):   return float(np.sum(np.cos(4*r*phi)))
def godd(phi, s, r): return -(2*r+1)*s*np.sin((2*r+1)*phi)
def geven(phi, r):   return -4*r*np.sin(4*r*phi)
def viol(phi):  return max(Feven(phi, r) - 0.5 for r in range(1, 13))
def obj(phi, s): return max(abs(Fodd(phi, s, r)) for r in range(13))

print("=== 0) feasibility certification of the known seeds (TRUE functions, item by item) ===", flush=True)
seeds = {
 'C-3850': np.arccos(np.sqrt(np.array([0.801874,0.561119,0.703473,0.627211,0.869546]))),
 'C-3855': np.arccos(np.sqrt(np.array([0.702989,0.873806,0.797976,0.551115,0.628434]))),
}
for k, phi in seeds.items():
    F = np.array([Feven(phi, r) for r in range(1,13)])
    print("  %s : max(F_2r - 1/2) = %+.3e  certified? %s | max F_2r = %.6f | min margin = %.3e"
          % (k, viol(phi), viol(phi) <= 1e-12, F.max(), (0.5 - F).min()), flush=True)

print("\n=== 1) feasibility recovery (independent object, on demand) ===", flush=True)
def recovery(phi0):
    f = lambda p: sum(max(0.0, Feven(p, r) - 0.5)**2 for r in range(1, 13))
    r = minimize(f, phi0, method='Nelder-Mead', options={'maxiter':4000,'xatol':1e-13,'fatol':1e-18})
    phi = np.clip(r.x, 0, HALF)
    # true-function per-item recheck
    return phi, f(phi), viol(phi)

print("\n=== 2) per-sigma bundle/trust-region from certified feasible points (true-function acceptance) ===", flush=True)
def bundle_sigma(s, starts):
    best = None
    for phi0 in starts:
        if viol(phi0) > 1e-12:                     # never start from an uncertified point
            continue
        phi = phi0.copy(); Delta = 0.05
        for it in range(80):
            g = obj(phi, s)
            I = [r for r in range(13) if abs(abs(Fodd(phi, s, r)) - g) <= 1e-6*max(g,1e-12)]
            A_ub, b_ub = [], []
            for r in I:
                w = np.sign(Fodd(phi, s, r))*godd(phi, s, r)
                A_ub.append(np.concatenate([w, [-1.0]])); b_ub.append(-abs(Fodd(phi, s, r)))
            for q in range(1, 13):
                A_ub.append(np.concatenate([geven(phi, q), [0.0]])); b_ub.append(0.5 - Feven(phi, q))
            for j in range(5):
                row = np.zeros(6); row[j] = -1.0; A_ub.append(row); b_ub.append(phi[j])
                row = np.zeros(6); row[j] = 1.0;  A_ub.append(row); b_ub.append(HALF - phi[j])
            c = np.zeros(6); c[5] = 1.0
            rr = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         bounds=[(-Delta,Delta)]*5+[(None,None)], method='highs')
            if not rr.success: break
            d = rr.x[:5]
            t = 1.0; moved = False
            for _ in range(40):
                cand = np.clip(phi + t*d, 0.0, HALF)
                # TRUE-function recheck of all 12 even constraints (LP feasibility is NOT acceptance)
                if viol(cand) <= 1e-12 and obj(cand, s) < g - 1e-15:
                    phi, moved = cand, True; break
                t *= 0.5
            if moved: Delta = min(0.2, Delta*1.2)
            else:
                Delta *= 0.5
                if Delta < 1e-10: break
        if best is None or obj(phi, s) < best[0]: best = (obj(phi, s), phi.copy())
    return best

seedlist = [seeds['C-3850'], seeds['C-3855']]
Vs = {}
for si, s in enumerate(SIG):
    starts = [p + (rng.normal(0, 0.01, 5) if i else 0.0) for i in range(24) for p in seedlist]
    out = bundle_sigma(s, starts)
    if out is None:
        print("  sigma=%s : no certified start -> VOID for this branch" % s.astype(int), flush=True); continue
    Vs[si] = out
    print("  sigma=%s : V_sigma >= %.9f | certified feasible (viol=%.1e) | boundary=%s"
          % (s.astype(int), out[0], viol(out[1]), bool(np.any(out[1] < 1e-9))), flush=True)

print("\n=== 3) gamma = min over sigma of V_sigma (order locked: min_sigma then min_x) ===", flush=True)
si = min(Vs, key=lambda k: Vs[k][0]); g, phi = Vs[si]; s = SIG[si]
print("   gamma^(13) upper bound (this run) = %.9f at sigma = %s" % (g, s.astype(int)), flush=True)
print("   x = %s ; min margin = %.3e" % (np.round(np.cos(phi)**2, 8), (0.5-np.array([Feven(phi,r) for r in range(1,13)])).min()), flush=True)

print("\n=== 4) KKT audit (subdifferential LP, interior/boundary separated) ===", flush=True)
marg = np.array([0.5 - Feven(phi, r) for r in range(1,13)])
ties = [r for r in range(13) if abs(abs(Fodd(phi, s, r)) - g) <= 1e-6]
bnd = [j for j in range(5) if phi[j] < 1e-9]
for tol in (1e-7, 1e-6, 1e-5):
    I = [r for r in range(13) if abs(abs(Fodd(phi, s, r)) - g) <= tol]
    A = [q for q in range(1,13) if marg[q-1] <= tol]
    W = np.array([np.sign(Fodd(phi, s, r))*godd(phi, s, r) for r in I])
    G = np.array([geven(phi, q) for q in A]) if A else np.zeros((0,5))
    N = np.array([-np.eye(5)[j] for j in bnd]) if bnd else np.zeros((0,5))
    Aeq = np.vstack([np.hstack([W.T, G.T, N.T]), np.hstack([np.ones(len(I)), np.zeros(G.shape[0]+N.shape[0])])])
    beq = np.concatenate([np.zeros(5), [1.0]])
    rr = linprog(np.zeros(Aeq.shape[1]), A_eq=Aeq, b_eq=beq, bounds=[(0,None)]*Aeq.shape[1], method='highs')
    ok = rr.status == 0
    print("   tol=%.0e : |I|=%d A=%s bnd=%s -> KKT=%s %s" % (tol, len(I), A, bnd, ok, "(INTERIOR)" if not bnd else "(BOUNDARY)"), flush=True)
print("DONE", flush=True)
