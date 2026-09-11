"""
BL5 FINAL: zeta's counting constants (C1 RESOLVED) and the definitive route check.

C1 (read from Droll 2012, Sec. 3.1): the counting hypothesis is
    N_F(T) = a T log T + b T + eps(T),   |eps(T)| <= c log^+ T + d,   a,c,d > 0,   3a + b > 0.
For zeta: N(T) = (T/2pi) log(T/2pi e) + 7/8 + S(T)
    => a = 1/(2pi) = 0.1591549431 ,  b = -(1+log 2pi)/(2pi) = -0.4516621630  => b+ = 0
    => 3a + b = 0.0258026663 > 0  (the hypothesis holds, barely).

Route: LHS <= (k^2 r_H^{k-1} tau^2 / 4) * S4(H)  vs  the conjecture's RHS with zeta's constants.
Also: the leading terms of the two sides match EXACTLY when a = 1/(2pi) (ratio -> 2 pi a = 1),
so the conjecture is asymptotically critical and decided by the subleading terms.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, sinh as msinh, pi as mpi
mp.dps=50
g=np.sort(np.load('/tmp/zeros_odlyzko_2M.npy').astype(np.float64).ravel()); GMAX=g[-1]
a = 1/(2*mpi); b = -(1+mlog(2*mpi))/(2*mpi)
print("a = 1/(2pi) = %.10f | b = %.10f | b+ = 0 | 3a+b = %.10f (>0: %s)"
      % (a, b, 3*a+b, 3*a+b>0))
def S4(H):
    m=g>H; s=float(np.sum(g[m]**-4.0)); X=mpf(max(GMAX,H))
    return s + float((1/mpi)*((X**-3/3)*mlog(X/(2*mpi))+X**-3/9))
def fac(k,tau,H):
    lr=mpf('0.5')*mlog1p(mpf(tau)/mpf(H)**2); return 4*msinh(mpf(k)*lr/2)**2
def RHS(k,tau,H,c,d):
    return float(2*fac(k,tau,H)*((mpf(1)/3)*a*mpf(H)*mlog(H)+(mpf(4)*a/9)*mpf(H)+2*mpf(c)*mlog(H)+2*mpf(d)+mpf(c)/4))
worst=1e9
for k in (2,4,8,16,32):
    for tau in (1.0,1.5,1.9):
        for H in (100.0,1000.0,10000.0,100000.0,1e6):
            rH=mpf(1+tau/H**2)**mpf('0.5')
            lhs=float(mpf(k)**2*rH**(k-1)*mpf(tau)**2/4)*S4(H)
            mT=RHS(k,tau,H,'0.112','2.5')/lhs; mR=RHS(k,tau,H,'0.137','3.5')/lhs
            if k==2: print("  k=%2d tau=%.1f H=%8g  LHS=%.4e  margin(Trudgian)=%.3f  margin(Rosser)=%.3f"
                           % (k,tau,H,lhs,mT,mR))
            worst=min(worst,mT)
print("worst margin over all (k=2..32, tau=1.0,1.5,1.9, H=1e2..1e6): %.3f x" % worst)
print("asymptotic identity: RHS/LHS -> 2*pi*a = %.6f  (exactly 1 for a = 1/(2pi))" % (2*mpi*a))
print("VERDICT: the rigorous bound fits the RHS on the whole tested range." if worst>1 else "VERDICT: FAILS")
