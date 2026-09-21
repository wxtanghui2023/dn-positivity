# c380_51_c3851_AB_v2.py -- C3851 A+B with the corrected constant (prod (2r+1) = 105)
import numpy as np, itertools
def U(n, c):
    a, b = np.ones_like(c), 2 * c
    if n == 0: return a
    for _ in range(2, n + 1): a, b = b, 2 * c * b - a
    return b
def DG(x, s):
    c = np.sqrt(np.asarray(x, float))
    return np.vstack([s * (2 * r + 1) * U(2 * r, c) / (2 * c) for r in range(4)])
rng = np.random.default_rng(3851)
CONST = 105 * 4096
def closed(x, idx):
    c = np.sqrt(np.asarray(x, float))[list(idx)]; xj = np.asarray(x, float)[list(idx)]
    van = 1.0
    for i in range(4):
        for j in range(i + 1, 4): van *= abs(xj[i] - xj[j])
    return CONST * np.prod(1.0 / (2 * c)) * van
print("=== B (corrected closed form: |det| = 105*4096 * prod 1/(2c_j) * Vandermonde) ===", flush=True)
mx = 0.0; lo = 1e300; hi = 0.0; ratio_bound = 1e300
for _ in range(6000):
    x = rng.uniform(0.02, 1.0, 5)
    if len(set(np.round(x, 12))) < 5: continue
    s = rng.choice([-1.0, 1.0], 5); M = DG(x, s)
    best = 0.0
    for idx in itertools.combinations(range(5), 4):
        d = abs(np.linalg.det(M[:, list(idx)])); cf = closed(x, idx)
        mx = max(mx, abs(d - cf) / cf); lo = min(lo, d / cf); hi = max(hi, d / cf); best = max(best, d)
    c = np.sqrt(x); delta = float(x.min())
    D = float(np.min([abs(c[i] - c[j]) for i in range(5) for j in range(i + 1, 5)]))
    ratio_bound = min(ratio_bound, best / (1.72032e6 * delta ** 3 * D ** 6))
print("   max relative deviation from closed form = %.3e" % mx, flush=True)
print("   |det| / closed-form in [%.9f, %.9f]  -> closed form exact, sigma-independent" % (lo, hi), flush=True)
print("   min of max_jhat|det| / (1.72032e6 * delta_*^3 * Delta^6) = %.4f  (>= 1 -> uniform bound holds)" % ratio_bound, flush=True)
print("DONE", flush=True)
