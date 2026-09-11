"""
YM9: DESIGN CORRECTION + the correct level for the transfer.
  Kernel-level PF is the WRONG level: classical PF functions (Gaussian e^{-x^2}, e^{-|x|})
  have Fourier transforms with NO zeros at all (e^{-t^2/4}, 1/(1+t^2)), so kernel-PF cannot
  FORCE infinitely many real zeros.  (And YM8 verified the kernel is not TP5 anyway.)
  RIGHT LEVEL:  Xi(t) = 2 int_0^inf Phi(u) cos(ut) du = 2 sum_n (-1)^n M_n t^{2n}/(2n)!
     where M_n := int_0^inf Phi(u) u^{2n} du  are the MOMENTS of Phi.
  => the Taylor coefficients of Xi ARE (up to sign/factorial) the moments of Phi.
  Necessary condition for RH (even entire function with all real zeros): coefficients alternate
  in sign, i.e.  M_n > 0 for all n.  Stronger (Turán/Newton log-concavity): a_n^2 >= const*a_{n-1}a_{n+1}.
  We compute the moments in high precision and report the log-concavity ratio r_n = a_n^2/(a_{n-1}a_{n+1}).
"""
from mpmath import mp, mpf, exp, pi, quad, mpmathify
mp.dps=40
def Phi(u):
    u=mpf(u); s=mpf(0)
    for n in range(1,16):
        a=2*pi**2*mpf(n)**4*exp(mpf('4.5')*u) - 3*pi*mpf(n)**2*exp(mpf('2.5')*u)
        s+= a*exp(-pi*mpf(n)**2*exp(2*u))
    return s
print("="*84); print("STEP 0 CALIBRATION: M_0 = int_0^inf Phi  vs  Xi(0)/2 = 0.2485603891"); print("="*84)
M0=quad(Phi,[0,mpf('3')])
print(f"  M_0 = {mp.nstr(M0,12)}   (Xi(0)/2 = 0.2485603891)   [{'OK' if abs(M0-mpf('0.2485603891'))<1e-9 else 'CHECK'}]")
print()
print("="*84); print("MOMENTS M_n = int_0^inf Phi(u) u^{2n} du   (high precision)"); print("="*84)
Ms=[]
for n in range(0,11):
    f=lambda u,n=n: Phi(u)*(u**(2*n))
    v=quad(f,[0,mpf('1.5'),mpf('3')])
    Ms.append(v)
    print(f"  M_{n:<2} = {mp.nstr(v,14)}   {'>0 OK' if v>0 else '<0 SIGN FLIP'}")
print()
print("="*84); print("Xi coefficients: a_n = 2*(-1)^n*M_n/(2n)!  -> sign pattern + log-concavity"); print("="*84)
import math
from mpmath import factorial
a=[]
for n in range(0,11):
    a.append(2*((-1)**n)*Ms[n]/factorial(2*n))
print("  |a_n| :")
for n in range(0,11): print(f"    n={n:<2} |a_n| = {mp.nstr(abs(a[n]),10)}")
print()
print("  log-concavity ratio  r_n = a_n^2/(a_{n-1} a_{n+1})   (Turán-type; >1 = log-concave):")
for n in range(1,10):
    if abs(a[n-1]*a[n+1])>0:
        r=(a[n]**2)/(a[n-1]*a[n+1])
        print(f"    n={n:<2} r_n = {mp.nstr(r,12)}")
print()
print("="*84); print("INTERPRETATION"); print("="*84)
print("""  * M_n > 0 for all n  <=>  coefficients of Xi alternate in sign   (necessary for RH)
  * log-concavity ratio r_n > 1 with margin -> the Turán/Newton-type inequalities hold.
  * Under RH the classical expectation is r_n -> 1 with a margin vanishing like 1/n^2-ish,
    i.e. again a MARGIN that shrinks -- the recurring uniformity theme of this project.""")
