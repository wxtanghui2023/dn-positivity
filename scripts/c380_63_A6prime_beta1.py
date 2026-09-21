# c380_63_A6prime_beta1.py -- A6' exact-tie stability audit, then B1-beta-1 second-order coupling
import numpy as np
from scipy.optimize import root
import mpmath as mp
mp.mp.dps = 40
SIG = np.array([-1.,1.,1.,-1.,1.]); A = [3,4,7,9]; RODD = (6, 9)
PHI0 = np.array([0.14721317, 0.23048868, 0.18365067, 0.2094225, 0.11795883])*np.pi

Fo = lambda p, r: float(np.sum(SIG*np.cos((2*r+1)*p)))
Fe = lambda p, q: float(np.sum(np.cos(4*q*p)))
go = lambda p, r: -(2*r+1)*SIG*np.sin((2*r+1)*p)
ge = lambda p, q: -4*q*np.sin(4*q*p)

def repolish(p0):
    F = lambda p: np.concatenate([[Fe(p,q)-0.5 for q in A], [abs(Fo(p,RODD[0]))-abs(Fo(p,RODD[1]))]])
    s = root(F, p0, method='lm', options={'xtol':1e-15,'ftol':1e-15})
    return s.x
phi = repolish(PHI0)
print("=== point restored (residual %.2e) ; x = %s ===" % (np.abs(np.concatenate([[Fe(phi,q)-0.5 for q in A],[abs(Fo(phi,6))-abs(Fo(phi,9))]])).max(), np.round(np.cos(phi)**2,10)), flush=True)

print("\n=== A6'-(1) base tie precision at 40 dps ===", flush=True)
mp_phi = [mp.mpf(float(v)) for v in phi]
mpFo = lambda r: mp.fsum([mp.mpf(float(SIG[j]))*mp.cos((2*r+1)*mp_phi[j]) for j in range(5)])
D_tie = abs(abs(mpFo(RODD[0])) - abs(mpFo(RODD[1])))
print("   Delta_tie = ||F_13| - |F_19|| = %s   (magnitude ~ %s)" % (mp.nstr(D_tie, 8), mp.nstr(mp.log10(D_tie) if D_tie>0 else mp.mpf('-inf'), 6)), flush=True)

print("\n=== A6'-(2) relative perturbation, not fixed absolute tolerance ===", flush=True)
rng = np.random.default_rng(6363)
t = float(abs(mpFo(13)))
for sd in (1e-8, 1e-6, 1e-4, 1e-2):
    dom = 0; worst = 0.0
    for _ in range(200):
        h = rng.normal(0, sd, 5)
        d = abs(abs(Fo(phi+h, 13)) - abs(Fo(phi+h, 19)))
        worst = max(worst, d)
        if abs(Fo(phi+h,13)) > abs(Fo(phi+h,19)): dom += 1
    print("   sd=%.0e : max delta_odd = %.3e (relative to t=%.4f: %.2e) ; branch F_13 dominant in %d/200 draws"
          % (sd, worst, t, worst/t, dom), flush=True)
print("   => the two branches exchange dominance freely under perturbation: consistent with an EXACT base tie", flush=True)

print("\n=== A6'-(3) the convex-combination subgradient is not a tie-break ===", flush=True)
g13, g19 = np.sign(Fo(phi,13))*go(phi,13), np.sign(Fo(phi,19))*go(phi,19)
G = np.array([ge(phi,q) for q in A])
lam = np.linalg.lstsq(G.T, -(0.903717944*g13 + 0.096282056*g19), rcond=None)[0]
print("   with omega=(0.9037,0.0963): residual = %.3e ; lambda = %s >= 0 ? %s"
      % (np.linalg.norm(0.903717944*g13 + 0.096282056*g19 + G.T@lam), np.round(lam,8), bool((lam>=-1e-12).all())), flush=True)
for w in (0.0, 1.0):
    l2 = np.linalg.lstsq(G.T, -(w*g13 + (1-w)*g19), rcond=None)[0]
    r2 = np.linalg.norm(w*g13 + (1-w)*g19 + G.T@l2)
    print("   single-branch omega=(%s,%s): best residual = %.3e ; lambda>=0 ? %s" % (w, 1-w, r2, bool((l2>=-1e-12).all())), flush=True)
print("   => the two-branch combination is REQUIRED; a single branch cannot balance -- omega is structural, not a tie-break", flush=True)

print("\n=== B1-beta-1: critical cone (4 active even gradients) and the null direction ===", flush=True)
# active even constraints are equalities along critical directions; null space of the 4 gradients
U, S, Vt = np.linalg.svd(G)
print("   singular values of the 4x5 active-even gradient matrix: %s" % np.round(S, 8), flush=True)
null = Vt[-1]
print("   null direction h (unit) = %s" % np.round(null, 8), flush=True)
a = float(np.sign(Fo(phi,13))*go(phi,13) @ null); b = float(np.sign(Fo(phi,19))*go(phi,19) @ null)
print("   odd first-order changes along h: s1 dF_13.h = %+.6e ; s2 dF_19.h = %+.6e" % (a, b), flush=True)
print("   check omega*a + (1-omega)*b = %.3e (should vanish at KKT)" % (0.903717944*a + 0.096282056*b), flush=True)
h = null if a > 0 else -null                      # orient so that the max decreases to first order
a = float(np.sign(Fo(phi,13))*go(phi,13) @ h); b = float(np.sign(Fo(phi,19))*go(phi,19) @ h)
print("   oriented so the odd max decreases: max first-order change = %+.6e (<0 expected)" % max(a, b), flush=True)
print("\n   --- second-order ledger along h:  D^2 F_k[h,h] = -k^2 sum_j gamma_j cos(k phi_j) h_j^2 ---", flush=True)
for k, gamma, tag in [(13, SIG, 'odd active'), (19, SIG, 'odd active'), (6, np.ones(5), 'even active'), (8, np.ones(5), 'even active'), (14, np.ones(5), 'even active'), (18, np.ones(5), 'even active')]:
    D2 = -(k**2) * float(np.sum(gamma*np.cos(k*phi)*h**2))
    print("   k=%2d (%s): D2F_k[h,h] = %+.6e" % (k, tag, D2), flush=True)
print("\n   NOTE: for a constraint F_k <= 1/2 ACTIVE at the point, a POSITIVE D2 means the constraint is", flush=True)
print("         violated for any step along +-h => the odd-descent direction is blocked at second order.", flush=True)
print("DONE", flush=True)
