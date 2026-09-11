"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Hecke associator: exact check of (T_m T_n) T_l vs T_m (T_n T_l)
# Product rule: T_m T_n = sum_{d | gcd(m,n)} d^{k-1} T_{m n / d^2}   (trivial character)
from math import gcd
from collections import defaultdict
from itertools import product

def mult(m, n, k):
    out = defaultdict(int)
    g = gcd(m, n)
    d = 1
    while d * d <= g:
        if g % d == 0:
            for dd in ({d} if d*d == g else {d, g//d}):
                out[m*n//(dd*dd)] += dd**(k-1)
        d += 1
    return out

def combine(A, B, k):
    """(sum_r A[r] T_r) * (sum_s B[s] T_s)"""
    out = defaultdict(int)
    for r, ar in A.items():
        for s, bs in B.items():
            for t, c in mult(r, s, k).items():
                out[t] += ar * bs * c
    return {r: c for r, c in out.items() if c != 0}

def check(triples, k):
    bad = 0; comm_bad = 0
    for m, n, l in triples:
        A = combine(mult(m, n, k), mult(l, 1, k), k)   # (T_m T_n) T_l
        B = combine(mult(m, 1, k), mult(n, l, k), k)   # T_m (T_n T_l)
        if A != B:
            bad += 1
            if bad <= 3: print(f"  NONASSOC k={k} ({m},{n},{l})")
        if mult(m, n, k) != mult(n, m, k):
            comm_bad += 1
    return bad, comm_bad

N = 14
triples = [(m, n, l) for m, n, l in product(range(1, N+1), repeat=3)]
print(f"triples tested: {len(triples)}  (m,n,l <= {N})")
for k in (2, 3, 4, 6, 12):
    bad, comm_bad = check(triples, k)
    print(f"k={k:2d}: associator nonzero in {bad}/{len(triples)} triples | commutator nonzero in {comm_bad}")

# also explicitly print one expansion pair coefficient-wise (m,n,l)=(2,6,3), k=2
print("\ncoefficient-wise (T_2 T_6) T_3  vs  T_2 (T_6 T_3), k=2:")
L = combine(mult(2, 6, 2), mult(3, 1, 2), 2)
R = combine(mult(2, 1, 2), mult(6, 3, 2), 2)
allr = sorted(set(L) | set(R))
print("  r :", "  ".join(f"{r:>4d}" for r in allr))
print("  L :", "  ".join(f"{L.get(r,0):>4d}" for r in allr))
print("  R :", "  ".join(f"{R.get(r,0):>4d}" for r in allr))
print("  identical:", L == R)

# non-multiplicativity contrast: T_m T_n vs T_{mn}
print("\nnon-multiplicativity control (k=2): T_m T_n == T_mn ?")
for (m, n) in [(2,3),(2,4),(6,6),(2,6),(3,9)]:
    lhs = mult(m, n, 2)
    rhs = {m*n: 1}
    print(f"  (m,n)=({m},{n}): T_m T_n = {dict(sorted(lhs.items()))}  vs  T_mn = {rhs}  equal={lhs==rhs}")
