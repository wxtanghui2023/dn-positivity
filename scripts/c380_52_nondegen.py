# c380_52_nondegen.py -- decisive test: do NON-degenerate 3+2 cancellation solutions exist?
# normalised b2 = 1; unknowns (a1,a2,a3,beta) all bounded below by eps > 0
import numpy as np
from scipy.optimize import least_squares

def res(v):
    a1, a2, a3, b = v
    return np.array([a1**n + a2**n + a3**n - (b**n + 1.0) for n in (1, 3, 5, 7)])

rng = np.random.default_rng(523)
print("=== min ||residual||_inf with all four unknowns bounded below by eps ===", flush=True)
for eps in (1e-1, 1e-2, 1e-3, 1e-4, 1e-6, 0.0):
    best = 1e9; bx = None
    for t in range(400):
        v0 = np.clip(rng.uniform(eps + 1e-3, 2.5, 4), eps + 1e-6, None)
        try:
            if eps > 0:
                r = least_squares(res, v0, bounds=(eps, 3.0), xtol=1e-14, ftol=1e-14, max_nfev=800)
            else:
                r = least_squares(res, v0, xtol=1e-14, ftol=1e-14, max_nfev=800)
        except Exception:
            continue
        val = float(np.linalg.norm(res(r.x), np.inf))
        if val < best: best, bx = val, r.x.copy()
    print("   eps=%.0e : min ||res||_inf = %.6e    argmin = %s" % (eps, best, np.round(bx, 6)), flush=True)

print()
print("=== structural check: the degenerate branch IS a solution family ===", flush=True)
def resdeg(b):
    return [1.0**n + b**n + 0.0**n * 0 - (b**n + 1.0) for n in (1, 3, 5, 7)]
for b in (0.5, 1.0, 2.0, 3.0):
    # careful: 0**n = 0 for n >= 1, so residual = 1 + b^n - (b^n + 1) = 0
    print("   beta=%.1f : residual = %s  (a3 = 0 -> degenerate, x3 = 0: weight collapse)" % (b, ["%.1e" % abs(z) for z in resdeg(b)]), flush=True)

print()
print("=== scaling check: the system is n-homogeneous, so solutions form rays ===", flush=True)
v = np.array([1.0, 1.7, 0.0, 1.7])
for lam in (0.3, 1.0, 4.0):
    print("   lam=%.1f : ||res(lam*v)||_inf = %.3e" % (lam, np.abs(res(lam * v)).max()), flush=True)
print("DONE", flush=True)
