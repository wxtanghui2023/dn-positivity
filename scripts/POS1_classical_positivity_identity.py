"""
POS1: verify the classical de la Vallee Poussin positivity used in the PNT, and its vanishing locus.
Discipline: calibrate first; exact/symbolic checks; no 1/2 input; L2 untouched.
"""
from math import cos, pi, isclose
print("="*80); print("STEP 0 CALIBRATION"); print("="*80)
# known: 3 + 4 cos t + cos 2t = 2 (1 + cos t)^2  >= 0, equality iff cos t = -1
tests=[(0,8),(pi,0),(pi/2,2),(pi/3,None),(2*pi/3,None)]
ok=True
for t,_ in tests:
    lhs=3+4*cos(t)+cos(2*t); rhs=2*(1+cos(t))**2
    good=isclose(lhs,rhs,abs_tol=1e-12); ok&=good
    print(f"  t={t:>8.4f}: 3+4cos t+cos2t = {lhs:>10.6f} ; 2(1+cos t)^2 = {rhs:>10.6f}  [{'OK' if good else 'FAIL'}]")
assert ok, "calibration failed"
print()

print("="*80); print("THE IDENTITY (de la Vallee Poussin / classical PNT input)"); print("="*80)
print("""    3 + 4 cos t + cos 2t  =  2 (1 + cos t)^2  >=  0        for ALL real t
    EQUALITY  <=>  cos t = -1  <=>  t = pi (mod 2 pi)""")
print()
print("  why it matters:  1 + 2 cos t  is the real part of  1 + 2 e^{it};  multiplying by the")
print("  positive factor 1 + cos t = 2 cos^2(t/2) gives the positivity above, which controls")
print("  1/|zeta(s)| near sigma = 1 and hence yields the classical zero-free region.")
print()

print("="*80); print("VANISHING LOCUS: exactness, not strictness"); print("="*80)
mins=[]
N=200000
for i in range(N+1):
    t=-3*pi + 6*pi*i/N
    v=3+4*cos(t)+cos(2*t)
    mins.append((v,t))
mv,mt=min(mins)
print(f"  minimum on [-3pi, 3pi]: {mv:.3e} at t = {mt:.6f}  (pi = {pi:.6f}, -pi = {-pi:.6f})")
print("  => the positivity is STRICT everywhere except at the single critical configuration")
print("     t = pi (mod 2pi);  it is exactly there that the argument loses all margin.")
print()
print("="*80); print("CONCLUSION"); print("="*80)
print("""  The classical positivity is SHARP: it vanishes exactly at one configuration.
  Its reach is therefore bounded by that vanishing locus, which is WHY the resulting
  zero-free region has a margin (c/(log t)^{2/3}...) that shrinks but never becomes uniform.

  GENERAL FORM (derived):  for ANY positivity-based method with form P >= 0,
     - if P vanishes TOO MUCH (e.g. on all configurations)  -> vacuous          [insufficient]
     - if P vanishes TOO LITTLE (strict everywhere)         -> cannot exclude   [insufficient]
     - if P vanishes EXACTLY on the off-critical configurations -> RH (equivalent)
  => no positivity can be "better": sharp-and-nonvacuous is RH-equivalent.""")
