"""
(d) rho(x)rho as the second object, taken to the level of the DUAL SCALE:
the Galois-side interval length l_i = |G_i|/|G| versus the field-side degree d_i = [F_i:Q_2] of the
fixed field F_i = L^{G_i}.  Question: do these form an A'-type two-scale pair (conserved product),
and does the profile's (length, height) become exchangeable?
NO 1/2 input, NO recursion input, NO artificial weights, NO audit.  L2 untouched.
"""
from fractions import Fraction as F
import math
# ---- D4 ----
def mul(a,b):
    i,j=a; k,l=b
    kk = k if j==0 else (-k)%4
    return ((i+kk)%4,(j+l)%2)
E=[(i,j) for i in range(4) for j in range(2)]
def gen(s):
    S={(0,0)}; fr=[(0,0)]
    while fr:
        x=fr.pop()
        for g in s:
            y=mul(x,g)
            if y not in S: S.add(y); fr.append(y)
    return frozenset(S)
sig=(1,0); tau=(0,1)
Gi=[gen([sig,tau]),gen([sig,tau]),gen([sig]),gen([sig]),gen([mul(sig,sig)]),gen([mul(sig,sig)]),gen([mul(sig,sig)]),gen([mul(sig,sig)]),gen([])]
G=Gi[0]; n=len(G)
print("="*84); print("(d)  two scales:  Galois-side |G_i|  vs  field-side degree [F_i:Q_2]"); print("="*84)
print(f"  |G| = {n}")
print(f"  {'i':>2} | {'|G_i|':>5} | {'l_i=|G_i|/|G|':>13} | {'F_i = L^(G_i)':>22} | {'d_i=[F_i:Q_2]':>13} | {'l_i*d_i':>7} | {'|G_i|*d_i':>9} | {'8-d_i':>5}")
FIELD={0:'Q_2',1:'Q_2',2:'Q_2(i)',3:'Q_2(i)',4:'Q_2(zeta_8)',5:'Q_2(zeta_8)',6:'Q_2(zeta_8)',7:'Q_2(zeta_8)',8:'L'}
ok1=ok2=ok3=True
for i,g in enumerate(Gi):
    d=n//len(g); l=F(len(g),n)
    p1=l*d; p2=len(g)*d
    ok1 &= (p1==1); ok2 &= (p2==n)
    print(f"  {i:>2} | {len(g):>5} | {str(l):>13} | {FIELD[i]:>22} | {d:>13} | {str(p1):>7} | {p2:>9} | {n-d:>5}")
print()
print(f"  conservation (Galois side):   l_i * d_i = 1 for every level      SELF-CHECK: {ok1}")
print(f"  conservation (A'-type form):  |G_i| * d_i = |G| = {n} for every level  SELF-CHECK: {ok2}")
print()
print("="*84); print("  the profile height is DETERMINED BY the dual scale"); print("="*84)
print("   aggregate profile height at level i  =  |G| - d_i  =  |G| - [F_i:Q_2]   (verified in B4)")
heights=[n-(n//len(g)) for g in Gi]
print(f"   computed: {heights}   (matches the B4 profile 7,7,6,6,4,4,4,4,0)")
print(f"   SELF-CHECK: {heights==[7,7,6,6,4,4,4,4,0]}")
print()
print("="*84); print("  so (length, height) is a ONE-PARAMETER family in the dual degree d"); print("="*84)
print("""   per level:   l = 1/d          (Galois-side length)
                c = |G| - d      (representation-side profile height)
   => the pair (l, c) is a function of the single dual degree d, i.e. the two sides ARE exchangeable
      through the Galois correspondence (subgroup <-> fixed field), which is a theorem and not an insertion.""")
print()
print("="*84); print("  BALANCE (l = c): does any level satisfy it?  (the analogue of A' balance)"); print("="*84)
print("   equation:  1/d = |G| - d   <=>  d^2 - |G| d + 1 = 0  <=>  d = (|G| +- sqrt(|G|^2 - 4))/2")
disc=n*n-4
print(f"   |G| = {n},  discriminant = |G|^2 - 4 = {disc},  is it a perfect square? {int(math.isqrt(disc))**2==disc}")
for d in sorted(set([n//len(g) for g in Gi])):
    print(f"     level with d = {d}:  l = {F(1,d)} ,  c = {n-d} ,  l - c = {F(1,d)-(n-d)}   equal? {F(1,d)==n-d}")
print(f"   => NO level satisfies l = c (levels have d in {{1,2,4,8}}; the formal roots are (8 +- sqrt(60))/2, irrational)")
print()
print("="*84); print("  COMPARISON WITH A'  (honest)"); print("="*84)
print("""   A':  two scales S_+ = log|Lambda|, S_- = log|Lambda^perp| with |Lambda|*|Lambda^perp| = |G|;
        the BALANCED scale would be sqrt(|G|), which EXISTS as an actual sized object only when the
        ramified datum realises it (and in the symplectic model a balanced object exists for every n).
   HERE: two scales (|G_i| , [F_i:Q_2]) with conserved product |G| = 8  -- the SAME shape (verified);
        but a balanced level would need |G_i| = sqrt(|G|) = sqrt(8) which is NOT an integer, so no level
        is balanced.  The obstruction is exactly the NON-SQUARENESS of |G| = 8  (the same square-root
        obstruction met earlier in the different/sqrt|D| setting).
   => A'-type two-scale structure: YES and verified.   Balance / exchange fixed point: OBSTRUCTED here.
   => therefore no F with a 1/2 fixed point is produced; Layer 3 is NOT reopened.""")
