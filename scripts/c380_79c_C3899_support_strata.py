# c380_79c_C3899_support_strata.py -- C-3899: (a) independent KKT re-solve + stationarity polynomial roots
#                                            (b) support-stratum feasibility scan: can k = #{distinct u^2} be small?
# model: phi in (0,pi/2)^5 ; u=cos2phi=2x-1 ; z=u^2 ; even layer F_{2q}=sum_j T_{2q}(u_j) <= 1/2 (q=1..12)
#        stratum "k": multiset of |u| has k distinct values, with multiplicities n_1..n_k summing to 5
#        even layer on that stratum = sum_i n_i*T_q(2 z_i - 1)   (because T_{2q}(u)=T_q(2u^2-1))
import numpy as np, itertools
from scipy.optimize import root, minimize
from numpy.polynomial import chebyshev as C

HALF = np.pi/2
SIG = np.array([-1.,1.,1.,-1.,1.]); A = [3,4,7,9]
Fo = lambda phi, r: float(np.sum(SIG*np.cos((2*r+1)*phi)))
Fe = lambda phi, q: float(np.sum(np.cos(4*q*phi)))
go = lambda phi, r: -(2*r+1)*SIG*np.sin((2*r+1)*phi)
ge = lambda phi, q: -4*q*np.sin(4*q*phi)
def Tm(n, u): return np.cos(n*np.arccos(np.clip(u, -1, 1)))

print("=== (a) independent re-solve of the five-node KKT system (10x10, winner sigma) ===", flush=True)
def eqs(zv):
    phi = zv[:5]; om = zv[5]; lam = zv[6:10]
    F = [om*(-1)*go(phi,6) + (1-om)*(+1)*go(phi,9)]
    for i,q in enumerate(A): F[0] = F[0] + lam[i]*ge(phi,q)
    return np.array(list(F[0]) + [Fe(phi,q)-0.5 for q in A] + [(-1)*Fo(phi,6) - (+1)*Fo(phi,9)])
rng = np.random.default_rng(3899)
best = None
for _ in range(60):
    z0 = np.concatenate([rng.uniform(0.15, HALF-0.15, 5), [0.5, 0.1,0.1,0.1,0.1]])
    s_ = root(eqs, z0, method='lm', options={'xtol':1e-15,'ftol':1e-15})
    res = np.abs(eqs(s_.x)).max()
    if best is None or res < best[1]: best = (s_.x, res)
zv, res = best
phi = zv[:5]; om = zv[5]; lam = zv[6:10]; om2 = 1-om
print("  KKT residual (inf-norm of 10x10 system) = %.3e" % res, flush=True)
print("  omega1 = %.12f (for F_13, s1=-1) ; omega2 = %.12f (for F_19, s2=+1) ; lambda = %s"
      % (om, om2, np.round(lam,12)), flush=True)
print("  phi/pi = %s" % np.round(phi/np.pi,12), flush=True)
print("  x      = %s" % np.round(np.cos(phi)**2,12), flush=True)
u = np.cos(2*phi); z = u**2; c = SIG*np.sqrt(np.cos(phi)**2)   # signed nodes
print("  u      = %s" % np.round(u,12), flush=True)
print("  z=u^2  = %s ; k = %d" % (np.round(np.sort(z),12), len(set(np.round(z,10)))), flush=True)
print("  true-function active even A = %s (margins %s)" % ([q for q in range(1,13) if abs(0.5-Fe(phi,q))<1e-12],
      np.round([0.5-Fe(phi,q) for q in range(1,13)],12)), flush=True)
ov = np.array([Fo(phi,r) for r in range(13)])
print("  odd tie I = %s ; t = %.12f" % ([r for r in range(13) if abs(abs(ov[r])-abs(ov).max())<1e-12], abs(ov).max()), flush=True)

print("\n--- stationarity polynomial P(c) = sum_q lam_q T'_{4q}(c) + w1*s1*T'_{13}(c) + w2*s2*T'_{19}(c) ---", flush=True)
P = np.zeros(1)
for lam_q, q in zip(lam, A): P = np.polyadd(P, C.cheb2poly(C.chebder(np.eye(1, 4*q+1, 4*q)[0], 1)))
P = np.polyadd(P, om*(-1)*C.cheb2poly(C.chebder(np.eye(1, 14, 13)[0], 1)))
P = np.polyadd(P, om2*(+1)*C.cheb2poly(C.chebder(np.eye(1, 20, 19)[0], 1)))
print("  deg P = %d" % (len(P)-1), flush=True)
print("  P(c_j) at the 5 signed nodes = %s" % np.round(np.polyval(P, c), 8), flush=True)
rts = np.roots(P)
rr = np.sort(np.real(rts[np.abs(np.imag(rts)) < 1e-8]))
rr_in = rr[(rr > -1) & (rr < 1)]
print("  ALL complex roots: %d (%d real)" % (len(rts), len(rr)), flush=True)
print("  real roots inside (-1,1): %d -> %s" % (len(rr_in), np.round(rr_in, 10)), flush=True)
print("  sorted signed nodes c_j     : %s" % np.round(np.sort(c), 10), flush=True)
print("  max |root - node| = %.3e" % min(np.abs(np.sort(rr_in)-np.sort(c)).max(), 1e9) if len(rr_in)==len(c) else "  (count mismatch)", flush=True)

print("\n=== (b) support-stratum feasibility scan: exists even-feasible x with k distinct |u| values? ===", flush=True)
def gval(Z, n):
    """max over q=1..12 of sum_i n_i T_q(2z_i-1)"""
    Z = np.atleast_2d(Z)
    out = np.full(Z.shape[1], -1e9)
    for q in range(1,13):
        val = np.zeros(Z.shape[1])
        for i,ni in enumerate(n): val = val + ni*Tm(q, 2*Z[i]-1)
        out = np.maximum(out, val)
    return out
print("  (feasible iff min_Z max_q sum_i n_i T_q(2z_i-1) <= 1/2 ; T_{2q}(u)=T_q(2u^2-1))", flush=True)
for k in (1,2,3):
    for n in [t for t in itertools.product(range(1,6), repeat=k) if sum(t)==5]:
        if tuple(sorted(n)) != n: continue
        grid = [np.linspace(0.002, 0.998, {1:60001, 2:801, 3:121}[k])]*k
        if k == 1:
            Z = grid[0].reshape(1,-1); g = gval(Z, n); i = int(np.argmin(g))
            mn, at = float(g[i]), [float(grid[0][i])]
        elif k == 2:
            A2, B2 = np.meshgrid(grid[0], grid[1]); Z = np.vstack([A2.ravel(), B2.ravel()])
            g = gval(Z, n); i = int(np.argmin(g)); mn, at = float(g[i]), [float(Z[0,i]), float(Z[1,i])]
        else:
            n1 = np.linspace(0.002,0.998,121)
            bestmn, bestat = 1e9, None
            A3,B3 = np.meshgrid(n1, n1)
            for zi in n1[::4]:
                Z = np.vstack([A3.ravel(), B3.ravel(), np.full(A3.size, zi)])
                g = gval(Z, n); i = int(np.argmin(g))
                if g[i] < bestmn: bestmn, bestat = float(g[i]), [float(Z[0,i]), float(Z[1,i]), float(zi)]
            mn, at = bestmn, bestat
        print("  k=%d mults=%s : min max_q F_2q = %+.6f  at z=%s -> %s (needs <= +0.500000)"
              % (k, list(n), mn, np.round(at,6), "FEASIBLE" if mn <= 0.5 else "INFEASIBLE"), flush=True)
print("\nDONE-STRATA", flush=True)
