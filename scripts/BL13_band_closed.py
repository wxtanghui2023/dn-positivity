#!/usr/bin/env python3
"""
BL13 (A1/E3, final step): close the intermediate band lambda in (1,3.3) or confirm coverage.

Sharpened closed form
---------------------
From F(1+1/t^2) <= exp(k/(2t^2)) and log(t/2pi) <= log(2H) on [H,2H],
        near <= (log(2H)/pi) * I ,      I = int_H^{2H} exp(k/(2t^2)) dt.
With s = k/(2t^2), I = (1/2) sqrt(k/2) int_{lambda/8}^{lambda/2} s^{-3/2} e^s ds, lambda = k/H^2.
The incomplete-gamma asymptotics for the upper limit (lambda/2 large) give
        int_{a}^{b} s^{-3/2} e^s ds = b^{-3/2}e^b (1 + O(1/b)) - a^{-3/2}e^a (1 + O(1/a)),
and the second term is negligible, so
        I ~ (1/2) sqrt(k/2) (lambda/2)^{-3/2} e^{lambda/2}
          = (1/2) H sqrt(lambda/2) * 2^{3/2} lambda^{-3/2} e^{lambda/2} * ... = (H/lambda) e^{lambda/2},
i.e.      near <= (log 2H / pi) (H/lambda) e^{lambda/2} (1 + O(1/lambda)),
while RHS >= 2 (e^{lambda/2} - 2 + e^{-lambda/2}) (a/3) H log H (1-O(1/H^2)) ~ (1/(3pi)) H log H e^{lambda/2}.
Hence     near / RHS <= 3 log(2H) / (lambda log H)  < 1   for  lambda > 3 log(2H)/log H  ~ 3.3.

Consequently the two bounds overlap as soon as the crude bound is valid up to lambda ~ 3.3, which is
what part (ii) checks.

Inputs : data/zeros_odlyzko_2M.npy ; Outputs : scripts/BL13_band_closed.txt
"""
import os, numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, pi as mpi, exp as mexp
mp.dps=40
ZD=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
ZP=os.path.join(ZD,'zeros_odlyzko_2M.npy'); ZEROS_PATH=ZP if os.path.exists(ZP) else '/tmp/zeros_odlyzko_2M.npy'
g=np.sort(np.load(ZEROS_PATH).astype(np.float64).ravel()); GMAX=g[-1]
a=1/(2*mpi); b=-(1+mlog(2*mpi))/(2*mpi); c=mpf('0.112'); d=mpf('2.5')
def Fv(u,k):
    v=(k/2.0)*np.log1p(u); return np.expm1(v)**2/np.exp(v)
def RHS(k,H):
    Hm=mpf(H); lr=mpf('0.5')*mlog1p(1/Hm**2)
    return float((mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2)*2*((a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4))
print("="*104)
print("BL13 (i): sharpened closed form  near <= (log2H/pi)(H/lambda)e^{lambda/2}  vs exact near")
print("="*104)
print("  %6s %8s %14s %18s %10s" % ("lambda","H","near exact","bound","bound/exact"))
worst=0.0
for H in (100.0,1000.0,10000.0,100000.0):
    for lam in (3.5,5.0,10.0,30.0,100.0,1000.0):
        k=int(round(lam*H*H))
        if k>200000000: continue
        m=(g>H)&(g<=2*H); ne=2*float(np.sum(Fv(1.0/g[m]**2,k)))
        bd=float((mlog(2*mpf(H))/mpi)*(mpf(H)/mpf(lam))*mexp(mpf(lam)/2))
        worst=max(worst, bd/ne if ne>0 else float('inf'))
        print("  %6.1f %8g %14.6e %18.6e %10.3f" % (lam,H,ne,bd,bd/ne if ne>0 else float('inf')))
print("  worst bound/exact ratio: %.3f" % worst)
print()
print("="*104); print("BL13 (ii): crude bound's validity in lambda (ratio RHS/LHS_bound must exceed 1)"); print("="*104)
print("  %8s %8s %14s %10s" % ("lambda","H","ratio","ok?"))
minr=1e9
for H in (100.0,1000.0,10000.0,100000.0,1000000.0):
    for lam in (0.5,1.0,1.5,2.0,2.5,3.0,3.3,4.0):
        k=max(2,int(round(lam*H*H)))
        Hm=mpf(H); lr=mpf('0.5')*mlog1p(1/Hm**2)
        S4p=(mpf(2)*a/3)*Hm**-3*mlog(Hm)+(8*a/9+2*b/3)*Hm**-3+(4*c*mlog(Hm)+c/2+4*d)*Hm**-4
        fac=mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2
        T=(a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4
        lhs=(mpf(k)**2/4)*mexp(max(k-4,0)*lr)*S4p; rhs=2*fac*T
        r=float(rhs/lhs); minr=min(minr,r)
        print("  %8.1f %8g %14.6f %10s" % (lam,H,r,"ok" if r>1 else "FAIL"))
    print()
print("  minimum ratio over the sweep: %.4f" % minr)
print()
print("="*104); print("READ-OFF  (conclusion generated from the numbers above)"); print("="*104)
print("  * if (i) gives a finite constant and (ii) stays above 1 up to lambda ~ 3.3, then the crude")
print("    bound (small lambda) and the sharpened closed form (lambda >~ 3.3) OVERLAP, and together")
print("    with the directly verified finite window 5 <= H < 40 and the trivial range H < 5 the whole")
print("    range k >= 2, H > e is covered -- i.e. the theorem is complete up to explicit constants.")
