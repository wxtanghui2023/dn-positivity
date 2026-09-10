"""
C1 verification: does a quadratic (Kummer) lift resolve the balance obstruction found in B4d?
Discipline: calibrate on known facts first; no 1/2 input; no recursion input; no audit; L2 untouched.
"""
from fractions import Fraction as F
import math
print("="*86); print("STEP 0  calibration: the two balance conditions must be kept apart"); print("="*86)
print("""  (A) A'-type balance   : the level carries an object of size sqrt(|G_i|... ) i.e. a subgroup of order
                          sqrt(|G|)  -- this is A''s condition Lambda = Lambda^perp, |Lambda| = sqrt(|G|)
  (B) the equation l = c: 1/d = |G| - d,  i.e. d^2 - |G| d + 1 = 0
      NOTE: (B) is NOT the same condition as (A).   This is a correction of my own B4d framing, where I
      presented (B) as the balance.  Both are computed below, separately.""")
print()
print("="*86); print("STEP 1  (A) at |G| = 8:  the obstruction is exactly 'odd 2-adic exponent'"); print("="*86)
print(f"  {'|G| = 2^n':>10} | {'sqrt(|G|) integer?':>18} | {'balanced level possible?':>24}")
for n in range(1,7):
    N=2**n; r=math.isqrt(N)
    print(f"  {str(N):>10} | {str(r*r==N):>18} | {str(r*r==N):>24}")
print("  => (A) holds iff n is EVEN.  For |G| = 8 = 2^3 the exponent 3 is ODD, so no balanced level.")
print()
print("="*86); print("STEP 2  one quadratic lift doubles the exponent: 3 -> 4, i.e. 8 -> 16 = 4^2"); print("="*86)
print("   |G| = 8 = 2^3  --(one quadratic lift)-->  2^4 = 16 = 4^2 : sqrt(|G'|) = 4 IS an integer")
print("   verify a subgroup of order 4 exists in a group of order 16 (p-group theorem, proof by centre):")
def center(Gs, mul):
    return [g for g in Gs if all(mul(g,h)==mul(h,g) for h in Gs)]
# the dihedral group of order 16, D8 = <r,s | r^8 = s^2 = 1, s r s = r^-1>
E=[(i,j) for i in range(8) for j in range(2)]
def mulD(a,b):
    i,j=a; k,l=b
    kk = k if j==0 else (-k)%8
    return ((i+kk)%8,(j+l)%2)
Z=center(E,mulD)
print(f"     D8 (order {len(E)}): centre = {Z}  (|Z| = {len(Z)}, non-trivial -> OK)")
print(f"     => normal subgroup of order 2 exists; quotient has order 8; its centre gives another;")
print(f"        pulling back gives a subgroup of order 4  -- verified by exhibiting one:")
sub=[g for g in E if g[0]%4==0 and g[1]==0]          # <r^2> hmm: r^2 has order 4 -> <r^2> = {1,r^2,r^4,r^6}
sub=[(i,0) for i in range(0,8,2)]
closed=all(mulD(a,b) in sub for a in sub for b in sub)
print(f"     <r^2> = {sub}, |.| = {len(sub)}, closed under multiplication: {closed}  -> order 4 EXISTS ✓")
print()
print("="*86); print("STEP 3  (B) is a DIFFERENT condition and is essentially never satisfiable"); print("="*86)
print("   (B): d^2 - |G| d + 1 = 0  =>  discriminant |G|^2 - 4 must be a perfect square")
for N in (8,16,32,64,256):
    D=N*N-4; r=math.isqrt(D)
    print(f"     |G| = {N:>4}:  discriminant = {D:>8},  perfect square? {r*r==D}")
print("   PROOF that only |G| = 2 works:  |G|^2 - k^2 = 4  =>  (|G|-k)(|G|+k) = 4")
print("     the only factorisation with both factors even and summing to 2|G| is (2,2) => |G| = 2, k = 0")
print("   => (B) fails for every group order > 2;  it is NOT the right balance criterion.")
print()
print("="*86); print("STEP 4  the arithmetic 2-cover obeys the SAME mechanism"); print("="*86)
print("""   different side :  v_(sqrt2)(D_K) = 3 (odd)  --one quadratic lift K -> K(sqrt(sqrt2))-->  6 (even)
   group side     :  |G| = 2^3 (odd exponent)  --one quadratic lift-->  2^4 : sqrt is an integer
   => both obstructions are 'the 2-adic exponent is odd', and ONE quadratic lift makes it even.
      This is the mechanism-level version of the 'same class' observation in B4d  (verified here,
      the arithmetic side having been verified earlier by the explicit element a' = (delta^-3)).""")
print()
print("="*86); print("STEP 5  what is NOT verified / what does NOT follow"); print("="*86)
print("""   - NOT verified: the ramification filtration of an actual order-16 lift of L/Q_2.  The balanced
     level requires the filtration to pass through a subgroup of order 4, which holds for L (8,4,2,1) but
     for the lift is only EXPECTED, not checked.
   - NOT produced: any F, any fixed point, any 1/2.  The balanced level would have l = 1/4, d = 4, c = 12;
     there is no one-half anywhere in this structure.
   => per the standing rule, Layer 3 is NOT reopened.""")
