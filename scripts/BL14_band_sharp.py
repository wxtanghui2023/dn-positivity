#!/usr/bin/env python3
"""
BL14 (A1/E3): close the band lambda in (1,3.3) by using the EXACT summand identity.

The previous bound used F(1+u) <= exp(k u /2) with u = 1/t^2, which is loose by a factor
(1 - exp(-v))^{-2} with v = (k/2) log(1+u): at v = 1 that factor is about 2.5. Keeping the exact form
        F(1+u) = 4 sinh^2(v/2),      v = (k/2) log(1+u),
and integrating it against the zero density gives a much sharper near bound:
        near <= (1/pi) int_H^{2H} 4 sinh^2( v(t)/2 ) log(t/2pi) dt,     v(t) = (k/2) log(1+1/t^2).
This script compares that sharp bound (and the even sharper version that uses the ACTUAL zeros for the
count) with the conjectured right hand side, across the band.

Inputs : data/zeros_odlyzko_2M.npy ; Outputs : scripts/BL14_band_sharp.txt
"""
import os, numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, pi as mpi, quad as mquad, sinh as msinh
mp.dps=40
ZD=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
ZP=os.path.join(ZD,'zeros_odlyzko_2M.npy'); ZEROS_PATH=ZP if os.path.exists(ZP) else '/tmp/zeros_odlyzko_2M.npy'
g=np.sort(np.load(ZEROS_PATH).astype(np.float64).ravel()); GMAX=g[-1]
a=1/(2*mpi); b=-(1+mlog(2*mpi))/(2*mpi); c=mpf('0.112'); d=mpf('2.5')
def RHS(k,H):
    Hm=mpf(H); lr=mpf('0.5')*mlog1p(1/Hm**2)
    return float((mp_exp_k(lr,k))*2*((a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4))
def mp_exp_k(lr,k):     # r^k + r^-k - 2  with r = exp(lr)
    from mpmath import exp as mexp
    return mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2
print("="*104)
print("BL14: sharp near bound (exact 4 sinh^2 form) vs RHS across the band lambda in (1,3.3)")
print("="*104)
print("  %7s %8s %18s %18s %18s %10s %10s" % ("lambda","H","sharp bound","actual-count bound","RHS","sharp/RHS","act/RHS"))
worst_s=0.0; worst_a=0.0
for H in (100.0,1000.0,10000.0,100000.0):
    Hm=mpf(H)
    for lam in (0.8,1.0,1.5,2.0,2.5,3.0,3.3,4.0):
        k=max(2,int(round(lam*H*H)))
        if k>200000000: continue
        # sharp density-integral bound over [H,2H]
        def integ(t):
            v = mpf(k)/2*mlog1p(1/mpf(t)**2)
            return 4*msinh(v/2)**2*mlog(mpf(t)/(2*mpi))
        sb = float(mquad(integ, [H, 2*H], maxdegree=8)/mpi)
        # bound using the ACTUAL zeros in (H,2H] (removes the density overestimate, keeps the identity)
        m=(g>H)&(g<=2*H)
        vv=(k/2.0)*np.log1p(1.0/g[m]**2)
        act = 2*float(np.sum(4*np.sinh(vv/2)**2))     # one sign from table, doubled for conjugates
        R=RHS(k,H); ws=sb/R if R>0 else float('nan'); wa=act/R if R>0 else float('nan')
        worst_s=max(worst_s,ws) if np.isfinite(ws) else worst_s
        worst_a=max(worst_a,wa) if np.isfinite(wa) else worst_a
        print("  %7.1f %8g %18.6e %18.6e %18.6e %10.4f %10.4f" % (lam,H,sb,act,R,ws,wa))
    print()
print("  worst sharp-branch ratio: %.4f   worst actual-count ratio: %.4f" % (worst_s,worst_a))
print()
print("="*104); print("READ-OFF  (conclusion generated from the numbers above)"); print("="*104)
print("  * the sharp branch uses the exact identity 4 sinh^2(v/2) with the smooth zero density;")
print("  * the actual-count branch additionally uses the real zeros in the first dyadic block, which is")
print("    what a rigorous bookkeeping with the counting hypothesis' local bound would supply;")
print("  * if the worst sharp ratio is below 1, the band is closed by the density bound alone.")
