# c380_47_backfill_audit.py -- definition backfill: check 9th-root certificate against ORIGINAL E_0
# E_even = {x in [0,1]^5 : sum_j T_{2r}(2 x_j - 1) <= 1/2, r = 1..12};  E_0 = union_j {x_j = 0}
from itertools import combinations
import numpy as np
from fractions import Fraction as F

def Qr(S, n, R=12):
    th = np.array([2 * np.pi * j / n for j in S])
    return [float(np.sum(np.cos(r * th))) for r in range(1, R + 1)]

S = (1, 2, 3, 4)
print("=== A. certificate vs ORIGINAL E_0 (n=9, S={1,2,3,4}) ===", flush=True)
Q = Qr(S, 9, 12)
for r, v in enumerate(Q, 1):
    print("   r=%2d  Re sum z^r = %+.10f   need <= -0.5 : %s" % (r, v, "OK" if v <= -0.5 + 1e-12 else "*** VIOLATION ***"), flush=True)

print()
print("=== B. induced five-coordinate point (x_5 = 0) ===", flush=True)
ys = [np.cos(np.pi * j / 9) for j in S] + [-1.0]
xs = [(1 + y) / 2 for y in ys]
print("   y =", ["%.8f" % z for z in ys], flush=True)
print("   x =", ["%.8f" % z for z in xs], " in [0,1]:", all(0 <= z <= 1 for z in xs), flush=True)
s1 = sum(y * y for y in ys); s2 = sum(y**4 for y in ys)
print("   s1 = sum y^2 = %.10f   (need <= 11/4 = %.6f) %s" % (s1, 11 / 4, "OK" if s1 <= 11 / 4 + 1e-12 else "VIOL"), flush=True)
print("   s2 = sum y^4 = %.10f   (need <= s1 - 9/16 = %.6f) %s" % (s2, s1 - 9 / 16, "OK" if s2 <= s1 - 9 / 16 + 1e-12 else "VIOL"), flush=True)
print("   s2 >= 11/12 ?", s2 >= 11 / 12 - 1e-12, flush=True)
print("   F_2 = 2 s1 - 5 = %.10f (<=1/2: %s) ; F_4 = 8 s2 - 8 s1 + 5 = %.10f (<=1/2: %s)"
      % (2 * s1 - 5, 2 * s1 - 5 <= 0.5 + 1e-12, 8 * s2 - 8 * s1 + 5, 8 * s2 - 8 * s1 + 5 <= 0.5 + 1e-12), flush=True)

print()
print("=== C. sweep n=3..30 : 4-subsets with Re sum z^r <= -1/2 for ALL r=1..12 ===", flush=True)
any_hit = False
for n in range(3, 31):
    hits = [T for T in combinations(range(n), 4) if max(Qr(T, n, 12)) <= -0.5 + 1e-12]
    if hits:
        any_hit = True
        print("   n=%2d : %3d hits : %s" % (n, len(hits), hits[:6]), flush=True)
print("   -> any n with hits in 3..30 :", any_hit, flush=True)

print()
print("=== D. general probe: min over samples of max_{r<=6} vs max_{r<=12} (Re sum z^r + 1/2) ===", flush=True)
rng = np.random.default_rng(7)
N = 2000000
th = rng.uniform(0, 2 * np.pi, size=(N, 4))
Qall = np.stack([np.cos(r * th).sum(1) for r in range(1, 13)], axis=1)
for K in (6, 12):
    M = Qall[:, :K].max(1) + 0.5
    print("   K=%2d : min max = %+.6f   feasible frac = %.3e" % (K, M.min(), float((M <= 0).mean())), flush=True)
print("DONE", flush=True)
