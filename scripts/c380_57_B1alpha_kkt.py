# c380_57_B1alpha_kkt.py -- B1-alpha: locate genuine KKT candidates
# min over phi of  sign * F_odd(sigma, r*)  s.t.  F_2r = 1/2 (r in A), F_2r <= 1/2
import numpy as np, itertools
from scipy.optimize import root
np.set_printoptions(precision=6, suppress=True)
rng = np.random.default_rng(57)

def Fe(phi, r): return float(np.sum(np.cos(2*r*phi)))
def Fo(phi, s, r): return float(np.sum(s*np.cos((2*r+1)*phi)))
def ge(phi, r): return -2*r*np.sin(2*r*phi)
def go(phi, s, r): return -(2*r+1)*s*np.sin((2*r+1)*phi)

SIG = [np.array(list(b)+[1], dtype=float) for b in itertools.product([-1,1], repeat=4)]

def res(z, s, rstar, A, sign):
    phi, lam = z[:5], z[5:]
    v = sign*go(phi, s, rstar)
    for i, r in enumerate(A): v = v + lam[i]*ge(phi, r)
    return np.concatenate([v, [Fe(phi, r)-0.5 for r in A]])

def maxodd(phi, s): return max(abs(Fo(phi, s, r)) for r in range(13))

scenarios = []
AS = [[3],[4],[9],[3,4],[3,9],[4,9],[3,4,9],[4,9,12],[3,4,9,12]]
for A in AS:
    for si, s in enumerate(SIG):
        for rstar in range(13):
            for sign in (1.0, -1.0):
                scenarios.append((A, si, s, rstar, sign))
print("scenarios:", len(scenarios), flush=True)

sols = []
for A, si, s, rstar, sign in scenarios:
    for t in range(3):
        z0 = np.concatenate([rng.uniform(0.05, np.pi/2-0.05, 5), rng.uniform(0.0, 2.0, len(A))])
        try:
            r = root(lambda z: res(z, s, rstar, A, sign), z0, method='hybr')
        except Exception:
            continue
        if not r.success: continue
        z = r.x; phi = z[:5]; lam = z[5:]
        if np.min(phi) < 1e-3 or np.max(phi) > np.pi/2 - 1e-3: continue
        if np.linalg.norm(res(z, s, rstar, A, sign), np.inf) > 1e-9: continue
        if np.min(lam) < -1e-9: continue
        marg = np.array([0.5 - Fe(phi, r) for r in range(1, 13)])
        if marg.min() < -1e-9: continue
        if abs(abs(Fo(phi, s, rstar)) - maxodd(phi, s)) > 1e-8: continue
        if maxodd(phi, s) > min(maxodd(phi, S) for S in SIG) + 1e-8: continue
        gv = abs(Fo(phi, s, rstar))
        dup = any(abs(gv-u[0]) < 1e-9 and np.allclose(np.sort(phi), np.sort(u[1]), atol=1e-6) for u in sols)
        if not dup:
            sols.append((gv, phi, lam, A, s.copy(), rstar))
sols.sort(key=lambda u: u[0])
print("surviving KKT candidates:", len(sols), flush=True)
for gv, phi, lam, A, s, rstar in sols[:8]:
    marg = np.array([0.5 - Fe(phi, r) for r in range(1, 13)])
    print("   g = %.6f | A = %s | r* = %d | sigma = %s | lambda = %s | max margin = %.3e"
          % (gv, A, rstar, s.astype(int), np.round(lam, 4), marg.max()), flush=True)
    print("        phi/pi = %s ; x = %s" % (np.round(phi/np.pi, 6), np.round(np.cos(phi)**2, 6)), flush=True)
print("DONE", flush=True)
