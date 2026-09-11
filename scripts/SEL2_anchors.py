"""
SEL2: two anchors for the Selberg dissection.
  (a) elementary: zeta(s) is real and NEGATIVE on (0,1)  => no real zeros in the strip (free!)
  (b) the Kim-Sarnak bound identity:  sqrt(1/4 - 975/4096) == 7/64 ??
      i.e. are the geometric spectral-gap bound and the arithmetic theta-bound the SAME theorem?
Discipline: calibrate; no 1/2 input beyond the statement being tested; L2 untouched.
"""
from mpmath import mp, mpf, zeta, sqrt, nstr
mp.dps=25
print("="*78); print("(a) real zeros of zeta in the strip?"); print("="*78)
for s in ('0.1','0.25','0.5','0.75','0.9'):
    v=zeta(mpf(s))
    print(f"  zeta({s}) = {nstr(v,12)}   {'NEGATIVE (real, no zero)' if v<0 else 'non-negative'}")
print("  => zeta(s) < 0 on (0,1): no REAL zeros in the strip.  [elementary: via eta>0 and 1-2^(1-s)<0]")
print("  => so for zeta, the 'exceptional real zeros' are excluded for FREE -- the opposite of the")
print("     Selberg situation, where small eigenvalues (exceptional zeros) are the HARD part.")
print()
print("="*78); print("(b) is sqrt(1/4 - 975/4096) equal to 7/64 ?"); print("="*78)
lam=mpf(975)/mpf(4096)
d=mpf(1)/mpf(4)-lam
print(f"  1/4 - 975/4096 = {nstr(d,12)}  =  {(mpf(1)/mpf(4)-lam)}")
print(f"  sqrt(...)      = {nstr(sqrt(d),12)}")
print(f"  7/64           = {nstr(mpf(7)/mpf(64),12)}")
print(f"  exact fractions: 1/4=1024/4096 ; 1024-975=49 ; sqrt(49/4096)=7/64  -> {'EQUAL' if sqrt(d)==mpf(7)/mpf(64) else 'NOT equal'}")
print()
print("  => the geometric bound  lambda_1 >= 975/4096 (Kim-Sarnak, congruence subgroups)")
print("     and the arithmetic bound  theta <= 7/64 (Kim-Sarnak, Maass forms over Q)")
print("     are the SAME numerical statement under  theta = sqrt(1/4 - lambda).")
print("  => ONE arithmetic input (symmetric-power lifts) governs BOTH the geometric analogue")
print("     and the number-field case.  Strong evidence that the wall is the same wall.")
