"""
ER-1 : EQUALITY RIGIDITY -- premise test.
ABD-0 left the claim: alpha_* = 1/2 is attained exactly at the AM-GM balance point (a=b).
That claim came from the UNIFORM k-child refinement: k*m^alpha = 1 with m = r(1-r), r = a/c.
Setting alpha_* = 1/2 gives:   1/(r(1-r)) = k^2   <=>   r(1-r) = 1/k^2.
Here we solve that exactly and ask: does alpha_*=1/2 FORCE r = 1/2 (balance)?
"""
from math import sqrt, log

print("="*86); print("ER-1 : does alpha_*=1/2 force the BALANCED child ratio r=1/2 ?"); print("="*86)
print("  uniform k-child refinement:  k * m^alpha = 1,  m = r(1-r),  r = a/c")
print("  alpha_* = 1/2   <=>   r(1-r) = 1/k^2   <=>   r = (1 +- sqrt(1 - 4/k^2))/2")
print()
print(f"  {'k':>3} | {'r_minus':>12} {'r_plus':>12} | {'|r-1/2| (min of the two)':>24} | {'check k*m^(1/2)':>16}")
print("  " + "-"*80)
bal_cases=[]
for k in range(2, 11):
    disc = 1.0 - 4.0/(k*k)
    if disc < 0:
        print(f"  {k:>3} | {'-- no real r --':>26} | {'--':>24} | {'--':>16}")
        continue
    rm = (1.0 - sqrt(disc))/2.0
    rp = (1.0 + sqrt(disc))/2.0
    for r in (rm, rp):
        m = r*(1-r)
        chk = k*(m**0.5)
        if abs(r-0.5) < 1e-12: bal_cases.append((k, r, 'EXACT BALANCE'))
    dmin = min(abs(rm-0.5), abs(rp-0.5))
    m = rm*(1-rm); chk = k*(m**0.5)
    print(f"  {k:>3} | {rm:>12.9f} {rp:>12.9f} | {dmin:>24.6e} | {chk:>16.12f}")
print()
print("="*86); print("EXACT SOLUTIONS AND THEIR DISTANCE FROM BALANCE"); print("="*86)
for k in (2,3,4,5,6):
    disc=1.0-4.0/(k*k)
    if disc<0: continue
    rm=(1.0-sqrt(disc))/2.0; rp=(1.0+sqrt(disc))/2.0
    print(f"  k={k}:  r- = {rm:.9f}  (dist from 1/2 = {abs(rm-0.5):.6f})   r+ = {rp:.9f}  (dist = {abs(rp-0.5):.6f})")
print()
print("="*86); print("VERDICT ON THE PREMISE"); print("="*86)
print("""  k = 2 : r(1-r) = 1/4 has the UNIQUE root r = 1/2  ==> exact AM-GM balance.
          BUT: two children, both with ratio r = 1/2, means both children ARE the balanced
          state (c/2, c/2) -- the refinement collapses the parent to two copies of its own
          balance point.  That is exactly the SYMMETRISATION / non-injective projection that
          ABD-1 already classified as (c) NON-INJECTIVE = insertion (fibre c-1), NOT dynamics.
  k >= 3: r(1-r) = 1/k^2 has TWO roots, both strictly OFF balance:
             k=3: r ~ 0.127 and 0.873   (dist from 1/2 ~ 0.373)
             k=4: r ~ 0.067 and 0.933   (dist ~ 0.433)
          and they still give alpha_* = 1/2 exactly, because alpha_* = log k / log(1/m)
          and m = 1/k^2 makes it log k / (2 log k) = 1/2.
  ==> CONCLUSION: alpha_* = 1/2 does NOT characterise the balanced child ratio.
      The claim 'alpha_* = 1/2 is attained exactly at AM-GM balance' holds ONLY for the
      uniform 2-child refinement, and in that case the refinement is degenerate
      (both children coincide with the balance point = symmetrisation).
      For k >= 3, alpha_* = 1/2 is achieved by UNBALANCED child ratios.
  ==> Therefore 'EQUALITY RIGIDITY' (1/2 forces equality) is NOT available:
      either the 1/2-attaining refinement is degenerate/symmetrising (k=2), or it is
      unbalanced (k>=3).  The route from alpha_*=1/2 to the AM-GM equality manifold is closed.
""")
