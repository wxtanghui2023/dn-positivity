# c380_51_c3851_AB_rank.py -- C3851 first cut (A+B): Jacobian rank + uniform minor, closed form
import numpy as np, itertools

def U(n, c):                      # Chebyshev U_n
    a, b = np.ones_like(c), 2 * c
    if n == 0: return a
    for _ in range(2, n + 1):
        a, b = b, 2 * c * b - a
    return b

def T(n, c):
    a, b = np.ones_like(c), c.copy()
    if n == 0: return a
    for _ in range(2, n + 1):
        a, b = b, 2 * c * b - a
    return b

def DG(x, s):
    c = np.sqrt(np.asarray(x, float))
    M = np.zeros((4, 5))
    for r in range(4):
        M[r, :] = s * (2 * r + 1) * U(2 * r, c) / (2 * c)
    return M

rng = np.random.default_rng(3851)
print("=== A0. sanity: derivative formula vs finite difference ===", flush=True)
x = rng.uniform(0.05, 0.95, 5); c = np.sqrt(x); s = rng.choice([-1.0, 1.0], 5)
mx = 0.0
for r in range(4):
    h = 1e-6
    fd = (T(2 * r + 1, np.sqrt(x + h)) - T(2 * r + 1, np.sqrt(x - h))) / (2 * h)
    an = (2 * r + 1) * U(2 * r, c) / (2 * c)
    mx = max(mx, float(np.max(np.abs(fd - an))))
print("   max |finite-diff  -  closed form| = %.3e" % mx, flush=True)

print()
print("=== A. rank claim: rank DG = min(4, #distinct x_j) ===", flush=True)
def rank_test(xs, tag):
    s = np.ones(5)
    r = int(np.linalg.matrix_rank(DG(xs, s)))
    print("   %-26s #distinct=%d  rank=%d  (predicted %d)"
          % (tag, len(set(np.round(xs, 9))), r, min(4, len(set(np.round(xs, 9))))), flush=True)
rank_test(np.array([0.1, 0.2, 0.3, 0.4, 0.5]), "5 distinct")
rank_test(np.array([0.1, 0.2, 0.3, 0.4, 0.4]), "1 coincidence (4 distinct)")
rank_test(np.array([0.1, 0.2, 0.3, 0.3, 0.4]), "1 coincidence (4 distinct)")
rank_test(np.array([0.1, 0.2, 0.3, 0.3, 0.3]), "2 coincidences (3 distinct)")

print()
print("=== B. closed form for the 4x4 minors ===", flush=True)
def closed(x, idx):
    c = np.sqrt(np.asarray(x, float))[list(idx)]
    xj = np.asarray(x, float)[list(idx)]
    van = 1.0
    for i in range(4):
        for j in range(i + 1, 4):
            van *= abs(xj[i] - xj[j])
    return 210 * 4096 * np.prod(1.0 / (2 * c)) * van
mx = 0.0; ratios = []
for _ in range(4000):
    x = rng.uniform(0.02, 1.0, 5)
    if len(set(np.round(x, 12))) < 5: continue
    s = rng.choice([-1.0, 1.0], 5)
    M = DG(x, s)
    for idx in itertools.combinations(range(5), 4):
        d = abs(np.linalg.det(M[:, list(idx)]))
        cf = closed(x, idx)
        mx = max(mx, abs(d - cf) / max(cf, 1e-300))
        ratios.append(d / cf)
print("   max relative deviation from closed form = %.3e" % mx, flush=True)
print("   min/max of |det| / closed-form = %.6f / %.6f  (closed form is |det| exactly, sigma-independent)"
      % (min(ratios), max(ratios)), flush=True)

print()
print("=== B2. explicit uniform bound: |det| >= 3.44064e6 * delta_*^3 * Delta^6 ===", flush=True)
worst = 1e300
for _ in range(4000):
    x = rng.uniform(0.02, 1.0, 5)
    if len(set(np.round(x, 12))) < 5: continue
    c = np.sqrt(x); s = rng.choice([-1.0, 1.0], 5)
    M = DG(x, s)
    delta = float(x.min()); D = float(np.min([abs(c[i] - c[j]) for i in range(5) for j in range(i + 1, 5)]))
    bound = 3.44064e6 * delta ** 3 * D ** 6
    best = max(abs(np.linalg.det(M[:, list(idx)])) for idx in itertools.combinations(range(5), 4))
    if bound > 0: worst = min(worst, best / bound)
print("   min over samples of  max_jhat|det| / (3.44064e6 delta_*^3 Delta^6) = %.6f  (>= 1 means bound valid)" % worst, flush=True)
print("DONE", flush=True)
