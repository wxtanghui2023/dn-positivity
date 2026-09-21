# c380_62_polish_audit.py -- B1-alpha-3-POLISH + A1..A6 independent audit
import numpy as np, itertools
from scipy.optimize import root
import mpmath as mp
mp.mp.dps = 40
SIG = np.array([-1.,1.,1.,-1.,1.])          # winner sigma = (-1,1,1,-1,1)
XS = np.array([0.80093022, 0.5611432, 0.70245716, 0.6261014, 0.86884389])
PHI = np.arccos(np.sqrt(XS))

Fo = lambda phi, r: float(np.sum(SIG*np.cos((2*r+1)*phi)))
Fe = lambda phi, q: float(np.sum(np.cos(4*q*phi)))
go = lambda phi, r: -(2*r+1)*SIG*np.sin((2*r+1)*phi)
ge = lambda phi, q: -4*q*np.sin(4*q*phi)

print("=== step 0: identify the active structure at the candidate (independent scan) ===", flush=True)
vals = {r: Fo(PHI, r) for r in range(13)}
t0 = max(abs(v) for v in vals.values())
I = sorted([r for r in range(13) if abs(abs(vals[r]) - t0) <= 1e-7])
print("   t0 = %.12f ; I = %s (|I| = %d) ; signs = %s"
      % (t0, I, len(I), [int(np.sign(vals[r])) for r in I]), flush=True)
print("   all odd values:", np.round([vals[r] for r in range(13)], 6), flush=True)
A0 = [q for q in range(1, 13) if 0.5 - Fe(PHI, q) <= 1e-6]
print("   A = %s ; margins:" % A0, np.round([0.5 - Fe(PHI, q) for q in range(1,13)], 8), flush=True)
assert len(I) == 2, "expected two tied active odd frequencies"

r1, r2 = I; s1, s2 = np.sign(vals[r1]), np.sign(vals[r2])
A = [3, 4, 7, 9]

print("\n=== step 1: POLISH -- equalised active system + full KKT stationarity (10x10 Newton) ===", flush=True)
def eqs(z):
    phi = z[:5]; om = z[5]; lam = z[6:10]
    F = [om*s1*go(phi, r1) + (1-om)*s2*go(phi, r2)]
    for i, q in enumerate(A): F[0] = F[0] + lam[i]*ge(phi, q)
    out = list(F[0]) + [Fe(phi, q) - 0.5 for q in A] + [s1*Fo(phi, r1) - s2*Fo(phi, r2)]
    return np.array(out)

z0 = np.concatenate([[PHI], [0.5], np.full(4, 0.1)], axis=None)
sol = root(eqs, z0, method='lm', options={'xtol':1e-15, 'ftol':1e-15})
phi = sol.x[:5]; om = sol.x[5]; lam = sol.x[6:10]
res = np.linalg.norm(eqs(sol.x), np.inf)
print("   Newton residual = %.3e ; omega = %.9f (omega2 = %.9f) ; lambda = %s"
      % (res, om, 1-om, np.round(lam, 9)), flush=True)
print("   phi/pi = %s" % np.round(phi/np.pi, 10), flush=True)
print("   x = %s" % np.round(np.cos(phi)**2, 10), flush=True)

print("\n=== A1/A2: independent recomputation of t and the active sets ===", flush=True)
ov = np.array([Fo(phi, r) for r in range(13)])
t = np.abs(ov).max(); tie = [r for r in range(13) if abs(abs(ov[r]) - t) <= 1e-12]
ev = np.array([Fe(phi, q) for q in range(1, 13)]); marg = 0.5 - ev
actE = [q for q in range(1, 13) if abs(marg[q-1]) <= 1e-12]
print("   t = %.12f ; tied odd indices (tol 1e-12) = %s" % (t, tie), flush=True)
print("   active even (|F_2q-1/2| <= 1e-12) = %s" % actE, flush=True)
print("   inactive even margins (min) = %.3e (must be > 0)" % marg[[q-1 for q in range(1,13) if q not in actE]].min(), flush=True)

print("\n=== A3: interior check (normal cone terms must vanish) ===", flush=True)
print("   phi > 0 ? %s ; phi < pi/2 ? %s -> interior: mu_j = 0" % (bool((phi > 0).all()), bool((phi < np.pi/2).all())), flush=True)

print("\n=== A4: full KKT balance, computed directly (not via LP residual) ===", flush=True)
bal = om*s1*go(phi, r1) + (1-om)*s2*go(phi, r2)
for i, q in enumerate(A): bal = bal + lam[i]*ge(phi, q)
print("   ||stationarity balance||_inf = %.3e" % np.abs(bal).max(), flush=True)
print("   omega >= 0 ? %s ; lambda >= 0 ? %s" % (bool(om >= 0 and 1-om >= 0), bool((lam >= -1e-14).all())), flush=True)
print("   (sign convention: normal cone for F_2q <= 1/2 uses +lambda_q grad F_2q with lambda_q >= 0; boundary would add -mu_j e_j)", flush=True)

print("\n=== A5: complementarity ===", flush=True)
comp = [float(lam[i]*(Fe(phi, q) - 0.5)) for i, q in enumerate(A)]
print("   max |lambda_q (F_2q - 1/2)| = %.3e ; inactive lambda = 0 by construction ; mu_j = 0 (interior)"
      % max(abs(c) for c in comp), flush=True)

print("\n=== A6: stability across precision levels and under perturbation ===", flush=True)
rng = np.random.default_rng(6262)
for tol in (1e-7, 1e-9, 1e-11):
    tt = np.abs(ov).max()
    it = [r for r in range(13) if abs(abs(ov[r]) - tt) <= tol]
    at = [q for q in range(1, 13) if abs(marg[q-1]) <= tol]
    print("   tol=%.0e : I=%s A=%s" % (tol, it, at), flush=True)
jump = 0
for _ in range(40):
    p = phi + rng.normal(0, 1e-9, 5)
    tt = max(abs(Fo(p, r)) for r in range(13))
    it = [r for r in range(13) if abs(abs(Fo(p, r)) - tt) <= 1e-9]
    at = [q for q in range(1, 13) if abs(0.5 - Fe(p, q)) <= 1e-9]
    if set(it) != set(tie) or set(at) != set(actE): jump += 1
print("   perturbation stability (40 draws, sd=1e-9): active-set jumps = %d" % jump, flush=True)

print("\n=== high-precision (40 dps) certification of the residuals ===", flush=True)
mp_phi = [mp.mpf(float(v)) for v in phi]
def mpFo(r):
    return mp.fsum([mp.mpf(float(SIG[j]))*mp.cos((2*r+1)*mp_phi[j]) for j in range(5)])
def mpFe(q):
    return mp.fsum([mp.cos(4*q*mp_phi[j]) for j in range(5)])
print("   max |F_2q - 1/2| (40 dps) = %s" % mp.nstr(max(abs(mpFe(q) - mp.mpf(1)/2) for q in A), 5), flush=True)
print("   |F_r1| - |F_r2| (40 dps) = %s" % mp.nstr(abs(mpFo(r1)) - abs(mpFo(r2)), 5), flush=True)
print("   t (40 dps) = %s" % mp.nstr(max(abs(mpFo(r)) for r in range(13)), 20), flush=True)
print("DONE", flush=True)
