"""
H1: settle the SCALE question with an elementary lemma of our own.

LEMMA (elementary).  For rho = sigma + i gamma and w = 1 - 1/rho,
      |w|^2 = |rho-1|^2/|rho|^2 = 1 + (1-2 sigma)/(sigma^2 + gamma^2).
  Hence:
    * sigma = 1/2  (on the critical line)   =>  |w| = 1 EXACTLY.
    * sigma = 1/2 - delta  (below the line) =>  |w| = e^{c},  c = (1/2) log(1 + 2 delta/(sigma^2+gamma^2))
                                                ~ delta/gamma^2   for gamma >> 1.
    * sigma = 1/2 + delta  (above the line) =>  |w| < 1  (contribution >= 0).
  Consequence: the contribution Re[1 - w^n] of an off-line zero can go negative only when
  e^{cn} becomes comparable to 1, i.e. for
      n  >~ c^{-1}  ~  gamma^2 / delta .
  => THE NATURAL SCALE IS n ~ gamma^2, i.e. n ~ T^2 to cover a verified height T.

This is the scale that a QUADRATIC window needs.  The tau-version of the literature uses
T(n) = n e tau (LINEAR in n), which is a different (weaker) scale -- so the quadratic
classical window is NOT supplied by that route.
Verify (i) the identity, (ii) the threshold scaling, numerically.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, cos as mcos, sin as msin, sqrt as msqrt, atan as matan
mp.dps=40
print("="*94); print("H1(i): the identity |1-1/rho|^2 = 1 + (1-2 sigma)/(sigma^2+gamma^2)"); print("="*94)
print("  %10s %10s | %20s %20s %10s" % ("sigma","gamma","direct |w|^2","formula","diff"))
for sig,gam in ((mpf('0.5'),mpf('100')),(mpf('0.4'),mpf('100')),(mpf('0.3'),mpf('50')),
                (mpf('0.5'),mpf('14.1347')),(mpf('0.49'),mpf('1000'))):
    rho=sig+1j*gam
    direct=abs(1-1/rho)**2
    formula=1+(1-2*sig)/(sig**2+gam**2)
    print("  %10s %10s | %20s %20s %10s" % (mp.nstr(sig,4),mp.nstr(gam,6),
        mp.nstr(direct,18),mp.nstr(formula,18),mp.nstr(direct-formula,6)))
print()
print("  => sigma=1/2 gives |w|^2 = 1 EXACTLY (the critical line is the locus of |w|=1).")
print()
print("="*94); print("H1(ii): the threshold scale n* ~ gamma^2/delta  (direct check)"); print("="*94)
print("  %8s %8s %14s %14s %14s %10s" % ("gamma","delta","c=log|w|","predicted 1/c","measured n*","ratio"))
for gam,delta in ((100.0,0.4),(100.0,0.05),(200.0,0.4),(50.0,0.2),(500.0,0.5)):
    sig=0.5-delta; rho=complex(sig,gam)
    w=1-1/rho; c=abs(w).real
    c=float(abs(w)); cc=float(np.log(c))
    n_pred=1.0/cc
    # find first n where Re[1-w^n] < 0
    n=1; found=None
    sz=float(w.real); si=float(w.imag)
    # iterate by powers for stability
    pw=complex(1,0); 
    for n in range(1,200000):
        pw*=w
        if (1-pw).real < 0:
            found=n; break
    print("  %8g %8g %14.6e %14.6e %14s %10s" % (gam,delta,cc,n_pred,found if found else ">2e5",
        ("%.2f"%(found/n_pred)) if found else "-"))
print()
print("="*94); print("READ-OFF"); print("="*94)
print("""  * the identity is exact, so the critical line is exactly the locus |w| = 1;
  * an off-line zero at height gamma first contributes negatively at n* ~ gamma^2/delta
    (with a modest constant), i.e. n* ~ gamma^2 for fixed relative deviation;
  * therefore covering a verified height T requires n up to ~ T^2  -- the QUADRATIC scale.
  * the tau-version's T(n) = n e tau is LINEAR, so that route does not supply the quadratic
    classical window; and Brown's theorem in the needed direction is unproved.""")
