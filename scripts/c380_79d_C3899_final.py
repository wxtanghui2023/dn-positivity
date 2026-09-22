# c380_79d_C3899_final.py -- C-3899: (a) reproduce the certified five-node KKT point + stationarity polynomial roots
#                                   (b) refined support-stratum minima for k = 1..5
import numpy as np, itertools
from scipy.optimize import root, minimize
from numpy.polynomial import chebyshev as C

HALF = np.pi/2
SIG = np.array([-1.,1.,1.,-1.,1.]); A = [3,4,7,9]
Fo = lambda phi, r: float(np.sum(SIG*np.cos((2*r+1)*phi)))
Fe = lambda phi, q: float(np.sum(np.cos(4*q*phi)))
go = lambda phi, r: -(2*r+1)*SIG*np.sin((2*r+1)*phi)
ge = lambda phi, q: -4*q*np.sin(4*q*phi)
XS = np.array([0.80093022,0.5611432,0.70245716,0.6261014,0.86884389])

print("=== (a) certified five-node KKT point (started from the C-3862 point) ===", flush=True)
def eqs(zv):
    phi = zv[:5]; om = zv[5]; lam = zv[6:10]
    F = [om*(-1)*go(phi,6) + (1-om)*(+1)*go(phi,9)]
    for i,q in enumerate(A): F[0] = F[0] + lam[i]*ge(phi,q)
    return np.array(list(F[0]) + [Fe(phi,q)-0.5 for q in A] + [(-1)*Fo(phi,6) - (+1)*Fo(phi,9)])
z0 = np.concatenate([np.arccos(np.sqrt(XS)), [0.903717944], [0.83791706,0.98971406,0.04185319,0.12728511]])
sol = root(eqs, z0, method='lm', options={'xtol':1e-15,'ftol':1e-15})
phi = sol.x[:5]; om = sol.x[5]; lam = sol.x[6:10]; om2 = 1-om
print("  residual = %.3e | omega = [%.12f, %.12f] (sum %.12f, both >= 0: %s) | lambda = %s (all >= 0: %s)"
      % (np.abs(eqs(sol.x)).max(), om, om2, om+om2, bool(om>=0 and om2>=0), np.round(lam,12), bool((lam>=-1e-13).all())), flush=True)
print("  x = %s" % np.round(np.cos(phi)**2, 14), flush=True)
u = np.cos(2*phi); z = u**2; c = SIG*np.sqrt(np.cos(phi)**2)
ov = np.array([Fo(phi,r) for r in range(13)]); t = np.abs(ov).max()
print("  t = %.14f | tied odd I = %s | active even A = %s" % (t, [r for r in range(13) if abs(abs(ov[r])-t)<1e-12],
      [q for q in range(1,13) if abs(0.5-Fe(phi,q))<1e-12]), flush=True)
print("  z = %s | k = %d" % (np.round(np.sort(z),12), len(set(np.round(z,9)))), flush=True)
print("  signed nodes c_j = %s" % np.round(c,12), flush=True)

print("\n--- stationarity polynomial P(c) (Chebyshev basis, P(c_j)=0 at the 5 nodes) ---", flush=True)
def cheb_deriv(n):
    e = np.zeros(n+1); e[n] = 1.0; return C.chebder(e, 1)
Pch = np.zeros(1)
for lam_q, q in zip(lam, A): Pch = C.chebadd(Pch, lam_q*cheb_deriv(4*q))
Pch = C.chebadd(Pch, om*(-1)*cheb_deriv(13))
Pch = C.chebadd(Pch, om2*(+1)*cheb_deriv(19))
print("  deg P = %d ; even/odd Chebyshev coefficient split: #even-deg coeffs != 0 -> %d ; #odd-deg != 0 -> %d"
      % (len(Pch)-1, int(np.sum(np.abs(Pch[0::2])>1e-12)), int(np.sum(np.abs(Pch[1::2])>1e-12))), flush=True)
print("  P(c_j) at the 5 nodes = %s" % np.round(C.chebval(c, Pch), 10), flush=True)
print("  P at 7 random test points = %s" % np.round(C.chebval(np.array([-0.9,-0.5,0.0,0.33,0.77,0.95,0.999]), Pch), 6), flush=True)
rts = C.chebroots(Pch)
real = np.sort(np.real(rts[np.abs(np.imag(rts)) < 1e-8]))
real_in = real[(real > -1) & (real < 1)]
print("  roots: %d total, %d real, %d real inside (-1,1)" % (len(rts), len(real), len(real_in)), flush=True)
print("  real roots inside (-1,1): %s" % np.round(real_in, 8), flush=True)
print("  => #distinct real roots of P in (-1,1) = %d  (nodes occupy %d of them)" % (len(np.unique(np.round(real_in,6))), len(c)), flush=True)

print("\n=== (b) refined support-stratum minima (t = max_q sum_i n_i T_q(2z_i-1) ; feasible iff <= 0.5) ===", flush=True)
def Tm(n, u): return np.cos(n*np.arccos(np.clip(u,-1,1)))
def solve_stratum(n):
    k = len(n)
    def vfun(zv, q):
        z = zv[:k]; val = 0.0
        for i,ni in enumerate(n): val += ni*Tm(q, 2*z[i]-1)
        return val
    best = (1e9, None)
    for _ in range(400):
        z0 = np.concatenate([np.random.default_rng().uniform(0.02,0.98,k), [0.0]])
        cons = [{'type':'ineq','fun': (lambda zv,q=q: zv[k] - vfun(zv,q))} for q in range(1,13)] \
             + [{'type':'ineq','fun': (lambda zv,i=i: zv[i])} for i in range(k)] \
             + [{'type':'ineq','fun': (lambda zv,i=i: 1.0-zv[i])} for i in range(k)]
        try:
            r_ = minimize(lambda zv: zv[k], z0, method='SLSQP', bounds=[(0.0,1.0)]*k+[(None,None)],
                          constraints=cons, options={'maxiter':200,'ftol':1e-14})
        except Exception: continue
        if r_.fun < best[0]: best = (float(r_.fun), r_.x[:k].copy())
    return best
for k in (1,2,3,4,5):
    for n in sorted({tuple(sorted(t)) for t in itertools.product(range(1,6), repeat=k) if sum(t)==5}):
        val, at = solve_stratum(list(n))
        print("  k=%d mults=%s : refined min max_q F_2q = %+.6f at z=%s -> %s"
              % (k, list(n), val, np.round(at,6), "FEASIBLE" if val <= 0.5 else "INFEASIBLE"), flush=True)
print("\nDONE-FINAL", flush=True)
