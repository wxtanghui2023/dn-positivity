# c380_52_c3852_C1C2.py -- C3852 C1+C2: zero set, rank, and the EXPLICIT local inverse constant
import numpy as np, itertools
from scipy.optimize import least_squares

def U(n, c):
    a, b = np.ones_like(c), 2 * c
    if n == 0: return a
    for _ in range(2, n + 1): a, b = b, 2 * c * b - a
    return b

def Gmat(x, s):
    c = np.sqrt(np.clip(x, 0, 1))
    return np.vstack([s * (2 * r + 1) * U(2 * r, c) / (2 * c) for r in range(4)])

def G(x, s):
    return (Gmat(x, s) * np.ones((1, 5))).sum(1) if False else np.array([np.sum(s * (2*r+1)*U(2*r, np.sqrt(np.clip(x,0,1)))/(2*np.sqrt(np.clip(x,0,1)))) for r in range(4)])

rng = np.random.default_rng(3852)
SIG = np.array([1.0, 1.0, -1.0, -1.0, 1.0])

print("=== C1: find zero points of G(.,sigma) (4 eqs, 5 unknowns -> 1-dim family) ===", flush=True)
zeros = []
for t in range(600):
    x0 = rng.uniform(0.02, 0.98, 5)
    try:
        r = least_squares(lambda x: G(x, SIG), x0, xtol=1e-14, ftol=1e-14)
    except Exception:
        continue
    if np.linalg.norm(G(r.x, SIG), np.inf) < 1e-10 and r.x.min() > 1e-6:
        if not any(np.allclose(r.x, z, atol=1e-5) for z in zeros):
            zeros.append(r.x)
print("   distinct zero points found :", len(zeros), flush=True)
if not zeros:
    print("   *** no zero found in the sampled region ***", flush=True)
for z in zeros[:6]:
    M = Gmat(z, SIG)
    rk = int(np.linalg.matrix_rank(M))
    print("   x = %s   min x_j = %.5f   rank DG = %d   distinct = %d"
          % (np.round(z, 6), z.min(), rk, len(set(np.round(z, 9)))), flush=True)

print()
print("=== C2: explicit constant chain and its numerical validation ===", flush=True)
def Cex(delta, Delta):        # crude explicit bound: C_x <= 2/m, m >= 1.307 delta^4.5 Delta^6
    return 1.53 / (delta ** 4.5 * Delta ** 6)
print("   chain: eta = 1.72032e6 * delta^3 Delta^6 ; ||DG|| <= 109.6/sqrt(delta) ;", flush=True)
print("          m >= |det|/||DG||^3 >= 1.307 * delta^4.5 Delta^6 ; C_x = 2/m <= 1.53/(delta^4.5 Delta^6)", flush=True)
worst = 0.0
for z in zeros[:8]:
    delta = float(z.min())
    c = np.sqrt(z); D = float(np.min([abs(c[i] - c[j]) for i in range(5) for j in range(i + 1, 5)]))
    if D <= 0: continue
    C = Cex(delta, D)
    M = Gmat(z, SIG); idx = list(range(5))
    jhat = max(itertools.combinations(range(5), 4), key=lambda I: abs(np.linalg.det(M[:, list(I)])))
    k = [j for j in range(5) if j not in jhat][0]
    for _ in range(60):
        x = z + rng.normal(0, 0.02, 5)
        x = np.clip(x, 1e-3, 1)
        r = least_squares(lambda y: G(np.array([y[j] if j < k else x[k] for j in range(5)]) if False else
                                      np.insert(y, k, x[k]), SIG), x[list(jhat)], xtol=1e-14, ftol=1e-14)
        psi = np.insert(r.x, k, x[k])
        dist = float(np.linalg.norm(x - psi))
        rhs = C * float(np.linalg.norm(G(x, SIG), np.inf))
        if rhs > 0: worst = max(worst, dist / rhs)
print("   max over samples of  dist(x,Z) / (C_explicit * ||G(x)||_inf)  = %.6f   (<= 1 means the bound holds)" % worst, flush=True)
print("DONE", flush=True)
