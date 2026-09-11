"""
DOOR1: for the Li family and the modulus family, verify the CROSSOVER LAW and locate
       exactly the missing estimate that would turn the shape into a theorem.
  Li:      lambda_n = sum_rho [1 - (1-1/rho)^n] ;  lambda_n >= 0 (all n) <=> RH.
  modulus: |q_rho| = |1-1/rho| ; a zero with beta<1/2 has |q_rho|>1, so |q_rho|^n grows like
           exp(n|delta|/|rho|^2)  => crossover with the polynomial growth of the on-line part.
  Test: build a set of ON-LINE zeros (below T) plus ONE hypothetical OFF-LINE zero (above T),
        compute lambda_n for increasing n, and find the first negative.
Discipline: calibrate on-line zero (|q|=1 exactly); no 1/2 input; L2 untouched.
"""
import numpy as np, math
gammas=[14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,43.327073,
        48.005151,49.773832,52.970321,56.446248,59.347044,60.831779,65.112544,67.079811,
        69.546402,72.067158,75.704691,77.144840,79.337375,82.910381,84.735493,87.425275,
        88.809111,92.491899,94.651344,95.870634,98.831194,101.317851]
print("="*84); print("CALIBRATION"); print("="*84)
w=1-1/complex(0.5,gammas[0]); print(f"  on-line zero: |1-1/rho| = {abs(w):.15f}  (must be exactly 1)")
print()
def lam(n, on_line, off_line):
    s=0j
    for g in on_line: s+= 1-(1-1/complex(0.5,g))**n
    if off_line is not None:
        b,g=off_line; s+= 1-(1-1/complex(b,g))**n
    return s.real
print("="*84); print("CROSSOVER LAW: with on-line zeros below T and one off-line zero (beta,gamma)"); print("="*84)
cases=[(0.4,100.0),(0.45,100.0),(0.4,200.0),(0.3,50.0),(0.49,150.0)]
print(f"  {'beta':>6} {'gamma':>7} | {'2g^2/|2b-1|':>13} | {'first n with lambda_n<0':>24} | {'ratio':>8}")
for b,g in cases:
    pred=2*g*g/abs(2*b-1)
    first=None
    for n in range(10,int(6e6),max(10,int(pred/400))):
        if lam(n,gammas,(b,g))<0: first=n; break
    r=first/pred if first else float('nan')
    print(f"  {b:>6} {g:>7} | {pred:>13.4g} | {str(first):>24} | {r:>8.3f}")
print()
print("="*84); print("THE MODULUS FAMILY (same threshold?)"); print("="*84)
for b,g in cases[:3]:
    q=abs(1-1/complex(b,g)); d=abs(b-0.5); rho2=b*b+g*g
    print(f"  beta={b}, gamma={g}: |q|={q:.10f}  ln|q|={math.log(q):.4e}  "
          f"delta/|rho|^2={d/rho2:.4e}  (equal => |q|^n = exp(n delta/|rho|^2))")
print()
print("="*84); print("WHERE IS THE DOOR?  (what is missing)"); print("="*84)
print("""  * The crossover n* ~ 2*gamma^2/|2beta-1| is CONFIRMED numerically (ratio ~ 1).
  * So the CONVERSION SHAPE is:   RH verified up to height T  ==>  lambda_n >= 0 for n <~ T^2.
  * But that inference needs one ESTIMATE we do not have:
        a bound on the ON-LINE contribution (the "background" sum, which grows like (n/2)log n)
        together with a uniform lower bound on the gap before the off-line term dominates.
    Without it, one only has: "if an off-line zero exists, lambda_n is negative for some n
    of size ~ gamma^2/|delta|" -- a DETECTION statement, not a positivity RANGE statement.
  => THE DOOR = that estimate. It is exactly the analogue of the "small modification of
     Turan's result" that the published Jensen conversion uses.""")
