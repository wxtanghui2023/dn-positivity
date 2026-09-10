"""
S3 continuation-law survey: what NON-ARTIFICIAL arithmetic principles can force the next construction?
Tang's exclusion list: balance | g=gcd | current-value type | artificial alternation | artificial weights |
                         enumerate-all-continuations | existing group/semigroup action.
Candidate classes found: L1 arithmetic-identity rewrites (AC + distributivity); L2 FTA-forced decomposition.
This script MEASURES the natural scale of L2 (the only arrow-bearing candidate).
"""
from math import log, log as ln

def lpf(n):
    if n%2==0: return 2
    d=3
    while d*d<=n:
        if n%d==0: return d
        d+=2
    return n

def isprime(n):
    if n<2: return False
    if n%2==0: return n==2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def Omega(n):
    c=0; m=n; d=2
    while d*d<=m:
        while m%d==0: c+=1; m//=d
        d+=1
    if m>1: c+=1
    return c

# ---------- canonical FTA-forced construction tree ----------
# prime p      ->  p = (p-1) + 1        (additive leg; forced: only way to build a prime from smaller)
# composite n  ->  n = p * (n/p), p = least prime factor (forced: canonical factorization)
# state = AC-class of the derivation;  S(n) = number of nodes in this canonical tree
import sys
sys.setrecursionlimit(100000)
_memo={}
def S(n):
    if n in _memo: return _memo[n]
    if n<=1: r=1
    elif isprime(n): r=1+S(n-1)
    else:
        p=lpf(n); r=1+S(p)+S(n//p)
    _memo[n]=r; return r

print("="*88); print("PART 1  the ONLY arrow-bearing non-artificial law (L2: FTA-forced decomposition)"); print("="*88)
print("   prime p    -> p = (p-1) + 1        (additive leg, forced)")
print("   composite n-> n = p x (n/p), p = least prime factor (forced by FTA)")
print()
print(f"  {'X':>8} | {'max S(n), n<=X':>15} | {'max Omega':>10} | {'log X':>8} | {'log log X':>10} | S_max / log X")
print("  "+"-"*84)
for X in (100,1000,10000,20000,50000):
    mx=0; mo=0
    for n in range(2,X+1):
        s=S(n)
        if s>mx: mx=s
        o=Omega(n)
        if o>mo: mo=o
    print(f"  {X:>8} | {mx:>15} | {mo:>10} | {log(X):>8.3f} | {log(log(X)):>10.4f} | {mx/log(X):>10.3f}")
print()
print("  => if S_max grows like a fixed power of log X, the canonical law lives on the LOG scale")
print("     (the registered E3 wall: natural critical exponents sit in log variables, not in X^alpha)")
print()
print("="*88); print("PART 2  mean/max Omega (the size of the canonical multiplicative leg)"); print("="*88)
print(f"  {'X':>8} | {'mean Omega':>12} | {'mean loglog(n)':>15} | {'max Omega':>10} | {'max Omega/log2 X':>17}")
print("  "+"-"*84)
for X in (100,1000,10000,20000):
    tot=0; mo=0; tll=0
    for n in range(2,X+1):
        o=Omega(n); tot+=o
        if o>mo: mo=o
        tll+=log(log(n)) if n>2 else 0
    c=X-1
    print(f"  {X:>8} | {tot/c:>12.4f} | {tll/c:>15.4f} | {mo:>10} | {mo/log(X,2):>17.4f}")
print()
print("="*88); print("PART 3  scale fit: does S_max behave like a power of log X, or like a power of X?"); print("="*88)
pts=[]
for X in (1000,5000,10000,20000,50000):
    mx=max(S(n) for n in range(2,X+1)); pts.append((X,mx))
for (X1,s1),(X2,s2) in zip(pts,pts[1:]):
    bx=log(s2/s1)/log(X2/X1)                      # exponent if S ~ X^b
    bl=log(s2/s1)/log(log(X2)/log(X1))            # exponent if S ~ (log X)^c
    print(f"  X {X1:>6}->{X2:>6}:  S {s1:>6}->{s2:>6}   X-exponent b={bx:.4f}   (log X)-exponent c={bl:.4f}")
print("  => b ~ 0 means NOT a power of X; a moderate c means a power of log X (LOG SCALE)")
print()
print("="*88); print("PART 4  VERDICT ON THE SURVEY"); print("="*88)
print("""  L1  arithmetic-identity rewrites (AC + distributivity):
        value-preserving AND reversible  ==>  a GROUPOID, no intrinsic arrow
        (choosing expand-vs-contract is a choice ==> G1 fails); if oriented toward a normal form,
        the system TERMINATES ==> no asymptotics, no critical exponent.
  L2  FTA-forced decomposition (measured above):
        canonical, forced, non-artificial, arrow-bearing (not reversible: the prime multiset does not
        determine the derivation) -- BUT the natural scale is measured in PART 1-3.
  L3  primality-forced additive leg p -> (p-1)+1: part of L2's canonical tree; same scale.
  L4  everything else (alternation, weights, priorities, enumeration order):
        ARTIFICIAL ==> primitive legitimacy fails (Tang's ruling (1)).
  ==> the non-artificial candidates are exhausted by L1/L2(+L3); L1 has no arrow or terminates,
      L2 has an arrow but its scale is measured in PART 1-3.
""")
