"""
CONV1: verify the LOCALIZATION threshold of Li's criterion (our own asset) and assemble
       the conversion "RH verified up to height T  =>  lambda_n >= 0 for n <= 2T^2".
  Li: lambda_n = sum_rho [1 - (1 - 1/rho)^n]   (nontrivial zeros),  lambda_n >= 0 for all n <=> RH.
  For a zero rho = beta + i*gamma with delta = beta - 1/2:
      |1 - 1/rho|^2 = 1 - 2*delta/|rho|^2   => |1-1/rho| < 1 iff beta > 1/2.
  So only zeros with beta < 1/2 can make the term negative, and it turns negative once
  n*|delta|/|rho|^2 ~ 1, i.e.  n* ~ gamma^2/|delta| = 2*gamma^2/|2beta-1|.
Discipline: calibrate (on-line zero must give a non-negative term); no 1/2 input; L2 untouched.
"""
import numpy as np
print("="*80); print("CALIBRATION"); print("="*80)
# on-line zero: rho = 1/2 + i*gamma  => |1-1/rho| = 1  => term = 1 - (unit complex) , Re >= 0
for g in (14.1347, 100.0):
    rho=complex(0.5,g); w=1-1/rho
    print(f"  on-line rho=0.5+{g}i :  |1-1/rho| = {abs(w):.12f}  (expect exactly 1)")
print()
print("="*80); print("OFF-LINE zero: beta=0.4 (delta=-0.1), gamma=100  ->  n* should be ~ 1e5"); print("="*80)
rho=complex(0.4,100.0); delta=rho.real-0.5; w=1-1/rho
print(f"  |1-1/rho| = {abs(w):.8f}  (>1 since beta<1/2)   |rho|^2 = {abs(rho)**2:.2f}")
print(f"  predicted threshold n* ~ 2*gamma^2/|2beta-1| = {2*100.0**2/abs(2*rho.real-1):.1f}")
print()
print(f"  {'n':>10} | {'Re[1-(1-1/rho)^n]':>22}")
for n in (10**3,10**4,3*10**4,10**5,3*10**5,10**6):
    v=1-w**n
    print(f"  {n:>10} | {v.real:>22.6e}   {'NEGATIVE' if v.real<0 else 'non-negative'}")
print()
print("="*80); print("THE CONVERSION (assembly)"); print("="*80)
print("""  Let RH be verified (numerically) for all zeros with |Im rho| <= T.  Then any zero
  violating RH has |gamma| > T.  Its Li-contribution only turns negative for
  n > 2*gamma^2/|2beta-1| > 2*T^2   (since |2beta-1| <= 1 in the strip).
  Hence:      RH verified up to height T   ==>   lambda_n >= 0  for all n <= 2*T^2.
  With Platt's T = 3.06e10 :  n <= 2*(3.06e10)^2  ~  1.9e21.
  Compare the published Jensen conversion d <= floor(T)^2 = 9.4e20  -- the SAME T^2 shape.""")
