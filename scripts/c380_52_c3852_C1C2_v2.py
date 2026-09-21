# c380_52_c3852_C1C2_v2.py -- C3852 C1+C2 (fixed: values use T_{2r+1}, derivatives use U_{2r})
import numpy as np, itertools
from scipy.optimize import least_squares

def Trec(n, c):
    a, b = np.ones_like(c), c.copy()
    if n == 0: return a
    for k in range(2, n + 1): a, b = b, 2 * c * b - a
    return b
def Urec(n, c):
    a, b = np.ones_like(c), 2 * c
    if n == 0: return a
    for k in range(2, n + 1): a, b = b, 2 * c * b - a
    return b
def G(x, s):
    c = np.sqrt(np.clip(x, 1e-12, 1))
    return np.array([np.sum(s * Trec(2 * r + 1, c)) for r in range(4)])
def DG(x, s):
    c = np.sqrt(np.clip(x, 1e-12, 1))
    return np.vstack([s * (2 * r + 1) * Urec(2 * r, c) / (2 * c) for r in range(4)])

rng = np.random.default_rng(3852)
print("=== C1: regular zero points of G(.,sigma) over the 16 sign classes ===", flush=True)
found = []
for bits in itertools.product([-1, 1], repeat=4):
    s = np.array(list(bits) + [1], dtype=float)
    for t in range(60):
        x0 = rng.uniform(0.03, 0.97, 5)
        try:
            r = least_squares(lambda x: G(x, s), x0, xtol=1e-15, ftol=1e-15)
        except Exception:
            continue
        nx = float(np.linalg.norm(G(r.x, s), np.inf))
        if nx < 1e-10 and r.x.min() > 1e-4 and len(set(np.round(r.x, 8))) == 5:
            M = DG(r.x, s)
            if int(np.linalg.matrix_rank(M)) == 4:
                key = (tuple(np.round(s, 3)), tuple(np.round(r.x, 5)))
                if not any(np.allclose(r.x, z, atol=1e-4) for _, z in found):
                    found.append((s, r.x))
print("   regular zero points found (x>0, distinct, rank 4) :", len(found), flush=True)
for s, z in found[:6]:
    print("   sigma = %s   x = %s   min x_j = %.5f" % (s.astype(int), np.round(z, 6), z.min()), flush=True)

print()
print("=== C2: explicit constant chain + validation at any regular zero ===", flush=True)
print("   eta = 1.72032e6 delta^3 Delta^6 ; ||DG|| <= 109.6/sqrt(delta) ; m >= |det|/||DG||^3", flush=True)
print("   => m >= 1.307 delta^4.5 Delta^6 ; C_x = 2/m <= 1.53/(delta^4.5 Delta^6)", flush=True)
worst = 0.0; nsamp = 0
for s, z in found[:8]:
    delta = float(z.min()); c = np.sqrt(z)
    D = float(np.min([abs(c[i] - c[j]) for i in range(5) for j in range(i + 1, 5)]))
    if D <= 0: continue
    C = 1.53 / (delta ** 4.5 * D ** 6)
    M = DG(z, s)
    jhat = max(itertools.combinations(range(5), 4), key=lambda I: abs(np.linalg.det(M[:, list(I)])))
    k = [j for j in range(5) if j not in jhat][0]
    for _ in range(80):
        x = np.clip(z + rng.normal(0, 0.03, 5), 1e-3, 1)
        try:
            r = least_squares(lambda y: G(np.insert(y, k, x[k]), s), x[list(jhat)], xtol=1e-15, ftol=1e-15)
        except Exception:
            continue
        psi = np.insert(r.x, k, x[k])
        dist = float(np.linalg.norm(x - psi)); rhs = C * float(np.linalg.norm(G(x, s), np.inf))
        if rhs > 1e-12:
            worst = max(worst, dist / rhs); nsamp += 1
print("   samples = %d ; max dist/(C_explicit * ||G||_inf) = %.6f  (<=1 -> bound holds)" % (nsamp, worst), flush=True)

print()
print("=== C1b: does a regular zero exist AT ALL? (probe for structural obstruction) ===", flush=True)
best = 1e9
for bits in itertools.product([-1, 1], repeat=4):
    s = np.array(list(bits) + [1], dtype=float)
    for t in range(40):
        x0 = rng.uniform(0.05, 0.95, 5)
        r = least_squares(lambda x: G(x, s), x0)
        v = float(np.linalg.norm(G(r.x, s), np.inf))
        if v < best: best, bx, bs = v, r.x.copy(), s.copy()
print("   min over the probe of ||G||_inf = %.3e   at x = %s, sigma = %s (min x_j = %.4f)"
      % (best, np.round(bx, 5), bs.astype(int), bx.min()), flush=True)
print("DONE", flush=True)
