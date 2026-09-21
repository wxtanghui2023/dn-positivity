# c380_46_probe_final.py -- solution characterization (lean)
from itertools import combinations
import numpy as np

def Qvec(S, n, K=9):
    th = np.array([2 * np.pi * j / n for j in S])
    return [float(np.sum(np.cos(k * th))) for k in range(1, K + 1)]

print("=== A. n-th roots, n=3..24 : #4-subsets with Q_k<=-1/2 (k<=6) ===", flush=True)
tot = {}
for n in range(3, 25):
    hits = [S for S in combinations(range(n), 4)
            if max(Qvec(S, n, 6)) <= -0.5 + 1e-12]
    if hits:
        tot[n] = hits
        print("  n=%2d : %3d hits : %s" % (n, len(hits), hits[:10]), flush=True)
print("  scanned n=3..24; n with hits:", sorted(tot.keys()), flush=True)

print()
print("=== B. all hits at n=9 with Q_k (k=1..9) ===", flush=True)
for S in tot.get(9, []):
    print("  %-14s Q=%s" % (str(S), ["%.6f" % z for z in Qvec(S, 9, 9)]), flush=True)

print()
print("=== C. isolation probe around S=(1,2,3,4) n=9 ===", flush=True)
rng = np.random.default_rng(1)
base = [2 * np.pi * j / 9 for j in (1, 2, 3, 4)]
print("   base Q_1..Q_6 =", ["%.6f" % z for z in Qvec((1, 2, 3, 4), 9, 6)], flush=True)
for eps in (1e-1, 1e-2, 1e-3, 1e-4, 1e-5):
    cnt = 0; N = 4000
    for _ in range(N):
        d = rng.normal(size=4); d /= np.linalg.norm(d)
        th = np.array(base) + eps * d
        if max(float(np.sum(np.cos(k * th))) for k in range(1, 7)) <= -0.5 + 1e-14:
            cnt += 1
    print("   eps=%.0e : feasible directions %d/%d" % (eps, cnt, N), flush=True)

print()
print("=== D. affine decomposition residual (20000 tuples) ===", flush=True)
import random
random.seed(3)
def T(k, x):
    a, b = 1.0, x
    for _ in range(2, k + 1):
        a, b = b, 2 * x * b - a
    return b
mx = [0.0, 0.0, 0.0]
for _ in range(20000):
    X = [random.uniform(-1, 1) for _ in range(4)]
    m = sum(X) / 4.0
    Y = [x - m for x in X]
    P2 = sum(y * y for y in Y); P3 = sum(y**3 for y in Y)
    e4 = Y[0] * Y[1] * Y[2] * Y[3]
    D4 = P2 * P2 / 16.0 - e4
    q3 = sum(T(3, x) for x in X); q4 = sum(T(4, x) for x in X); q5 = sum(T(5, x) for x in X)
    r3 = 16 * m**3 + 12 * m * P2 - 12 * m + 4 * P3
    r4 = 32 * m**4 + 48 * m * m * P2 + 2 * P2 * P2 - 32 * m * m - 8 * P2 + 4 + 32 * m * P3 + 32 * D4
    r5 = (64 * m**5 + 160 * m**3 * P2 + 20 * m * P2 * P2 - 80 * m**3 - 60 * m * P2 + 20 * m
          + (160 * m * m - 20 + (40.0 / 3.0) * P2) * P3 + 320 * m * D4)
    mx[0] = max(mx[0], abs(q3 - r3)); mx[1] = max(mx[1], abs(q4 - r4)); mx[2] = max(mx[2], abs(q5 - r5))
print("   max residual Q3,Q4,Q5 =", ["%.2e" % z for z in mx], flush=True)
print("DONE", flush=True)
