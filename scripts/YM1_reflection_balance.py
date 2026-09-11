"""
YM1: does the arithmetic reflection pairing (approximate functional equation) have its
     weight balance EXACTLY at sigma = 1/2 ?   -- the YM 'reflection positivity + balance' analogue
Discipline: calibrate first; Stirling-based complex gamma; no 1/2 input; L2 untouched.
"""
import cmath, math
print("="*84); print("STEP 0 CALIBRATION (complex gamma via Stirling, then known values)"); print("="*84)
def cgamma(s):
    """Stirling with shift for accuracy: Gamma(s) = Gamma(s+n)/((s)(s+1)...(s+n-1))"""
    n=12; z=s
    acc=1.0+0j
    for k in range(n):
        acc*= z+k
    z=z+n
    # Stirling series for ln Gamma(z)
    lg = (z-0.5)*cmath.log(z) - z + 0.5*math.log(2*math.pi) \
         + 1/(12*z) - 1/(360*z**3) + 1/(1260*z**5)
    return cmath.exp(lg)/acc
tests=[(1,1),(2,1),(3,2),(4,6),(5,24),(0.5,math.sqrt(math.pi))]
ok=True
for s,v in tests:
    g=cgamma(complex(s,0))
    good=abs(g-v)<1e-6*max(1,abs(v)); ok&=good
    print(f"  Gamma({s}) = {g.real:.8f}  expected {v:.8f}  [{'OK' if good else 'FAIL'}]")
assert ok, "calibration failed"
print()

print("="*84); print("THE ARITHMETIC REFLECTION FACTOR  chi(s)"); print("="*84)
print("  zeta(s) = chi(s) zeta(1-s) ,  chi(s) = pi^{s-1/2} Gamma((1-s)/2) / Gamma(s/2)")
def cloggamma(s):
    """log Gamma with shift + Stirling (avoids underflow).  ERR: cgamma underflowed for large t."""
    n=12; z=s; corr=0j
    for k in range(n):
        corr += cmath.log(z+k)
    z=z+n
    return (z-0.5)*cmath.log(z) - z + 0.5*math.log(2*math.pi) \
           + 1/(12*z) - 1/(360*z**3) + 1/(1260*z**5) - corr
def chi_log(s):
    return (s-0.5)*cmath.log(math.pi) + cloggamma((1-s)/2) - cloggamma(s/2)
def chi(s):
    return cmath.exp(chi_log(s))
print(f"  identity check chi(s)chi(1-s) = 1 :")
for s in [complex(0.3,7.0), complex(0.9,3.3), complex(0.5,14.134725)]:
    v=chi(s)*chi(1-s)
    print(f"    s={s}: chi(s)chi(1-s) = {v:.10f}  [{'OK' if abs(v-1)<1e-6 else 'FAIL'}]")
    assert abs(v-1)<1e-6
print("  => on the line chi(1/2+it)chi(1/2-it) = 1  =>  |chi(1/2+it)| = 1   (exactly)")
print()

print("="*84); print("THE BALANCE POINT: |chi(sigma+it)| vs t^{1/2-sigma}"); print("="*84)
print(f"  {'sigma':>7} | {'t':>8} | {'|chi|':>12} | {'t^(1/2-sigma)':>13} | {'ratio':>9}")
for sig in (0.0,0.25,0.5,0.75,1.0):
    for t in (100.0, 1000.0, 10000.0):
        v=math.exp(chi_log(complex(sig,t)).real)
        w=t**(0.5-sig)
        print(f"  {sig:>7.2f} | {t:>8.0f} | {v:>12.5f} | {w:>13.5f} | {v/w:>9.5f}")
print()
print("  NOTE the ratio is CONSTANT in t (up to the pi/2pi factor) and equals 1 exactly at sigma=1/2.")
print("  => the two terms of the approximate functional equation carry weights 1 and |chi|,")
print("     which are EQUAL precisely when sigma = 1/2.   The balance point IS the critical line.")
print()
print("="*84); print("WHAT THE TWO-TERM (REFLECTION) STRUCTURE LOOKS LIKE"); print("="*84)
print("""  approximate functional equation:   zeta(s) ~ sum_{n<=x} n^{-s}  +  chi(s) sum_{n<=y} n^{s-1}
     with  x*y = t/(2 pi)   (the reflection pairing  n  <->  t/n )
  * the two sums are the TWO HALVES of the dual variable, paired by the involution n -> t/n
  * their weights are 1 and |chi(1/2+it)|, i.e. equal exactly on the critical line
  * OFF the line the weights are unbalanced by the factor t^{1/2-sigma}
  => structurally: a REFLECTION PAIRING with a WEIGHT BALANCE whose balance locus is sigma=1/2
     This is the exact analogue of the YM/OS lattice situation:
        reflection of the lattice  <->  pairing n <-> t/n
        positive weights e^{-S} >= 0  <->  the two sums with non-negative coefficients n^{-sigma}
        reflection positivity      <->  ???  (the MISSING positivity)
""")
