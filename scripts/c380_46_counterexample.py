# c380_46_counterexample.py -- explicit exact feasibility certificate for E_0 (four unit nodes)
import mpmath as mp
from itertools import combinations
mp.mp.dps = 60

def qk(S, k, n):
    w = mp.e**(2j * mp.pi / n)
    return sum(w**(j * k) for j in S)

def report(S, n, tag):
    q = [qk(S, k, n) for k in range(1, 10)]
    Q = [mp.re(z) for z in q]
    print("%s  n=%d S=%s" % (tag, n, S))
    print("   Q_k (k=1..9) =", [mp.nstr(z, 15) for z in Q])
    print("   q_k (k=1..4) =", [mp.nstr(z, 8) for z in q[:4]])
    ok6 = all(Q[k] <= mp.mpf(-1) / 2 + mp.mpf('1e-40') for k in range(6))
    ok8 = all(Q[k] <= mp.mpf(-1) / 2 + mp.mpf('1e-40') for k in range(8))
    print("   <=-1/2 for k<=6 :", ok6, "  for k<=8 :", ok8)
    return ok6, ok8

print("=== A. candidate: 9th roots of unity, S={1,4,6,7} ===")
report([1, 4, 6, 7], 9, "candidate")
print("   note: 1+4+6+7=18 => e4=omega^18=1 ; S vs -S =", sorted([(-j) % 9 for j in [1, 4, 6, 7]]))
print("   QR mod 9 =", sorted({(j * j) % 9 for j in range(1, 9)}), " units =", [j for j in range(1, 9) if __import__("math").gcd(j, 9) == 1])

print()
print("=== B. exhaustive scan: all 4-subsets of n-th roots, n <= 12 ===")
for n in range(3, 13):
    hits6 = []; hits8 = []
    for S in combinations(range(n), 4):
        Q = [mp.re(qk(S, k, n)) for k in range(1, 9)]
        if all(Q[k] <= mp.mpf(-1) / 2 + mp.mpf('1e-40') for k in range(6)): hits6.append(S)
    print("  n=%2d : #subsets with Q_k<=-1/2 (k<=6) = %d  %s" % (n, len(hits6), hits6[:6]))

print()
print("=== C. exactness check at 120 digits ===")
mp.mp.dps = 120
S = [1, 4, 6, 7]
w = mp.e**(2j * mp.pi / 9)
for k in range(1, 10):
    z = sum(w**(j * k) for j in S)
    print("   k=%d  q_k=%s   Re q_k + 1/2 = %s" % (k, mp.nstr(z, 25), mp.nstr(mp.re(z) + mp.mpf(1) / 2, 8)))
