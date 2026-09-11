"""
ESC1: the archimedean ('cusp') contribution to Weil's explicit formula.
  Its weight is Re psi(1/4 + i t/2)  (psi = digamma).  Is it a POSITIVE source?
  This decides whether an 'explicit cusp treatment' (as in non-compact Selberg theory)
  can supply positivity for zeta.
Discipline: calibrate first; no 1/2 input; L2 untouched.
"""
from mpmath import mp, mpf, digamma, nstr, re
mp.dps=20
print("="*76); print("CALIBRATION: psi known values"); print("="*76)
print(f"  psi(1)      = {nstr(digamma(1),15)}   (-gamma = -0.5772156649015329)")
print(f"  psi(1/2)    = {nstr(digamma(mpf(1)/2),15)}   (-gamma-2ln2 = -1.9635100260214235)")
print(f"  psi(1/4)    = {nstr(digamma(mpf(1)/4),15)}")
print()
print("="*76); print("Re psi(1/4 + i t/2)  -- the archimedean weight"); print("="*76)
for t in (0,0.5,1,2,3,5,10,20,50,100,1000):
    v=re(digamma(mpf(1)/4 + 1j*mpf(t)/2))
    print(f"  t={t:>6}   Re psi(1/4+it/2) = {nstr(v,12)}   {'POSITIVE' if v>0 else 'NEGATIVE'}")
print()
print("="*76); print("VERDICT"); print("="*76)
print("""  * For LARGE t the weight is positive and grows like log(t/2).
  * For SMALL t it is NEGATIVE.
  => the archimedean contribution is NOT a uniform positive source for all test functions.
     So 'cusp-explicit positivity' cannot be a blanket positivity: it is positive only for
     test functions concentrated at high frequency.
  * This is the exact mirror of the classical zero-free region: the archimedean term helps
     at large height, which is why the classical method reaches only sigma > 1 - c/log t.""")
