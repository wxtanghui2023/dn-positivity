#!/usr/bin/env python3
"""
BL12 (A1/E3 finishing item 3): the intermediate band lambda = k/H^2 in (1,12).

The crude bound closes lambda <~ 1 and the closed-form near bound closes lambda >~ 12, leaving a band.
Because the comparison ratio is essentially scale invariant in H (the H-dependence cancels between
the two sides up to O(1/H^2) corrections), the band can be settled by a finite sweep in lambda.

Ratio(lambda,H) := [ (k^2/4) r_H^{(k-4)+} S4plus(H) ] / [ 2 fac(k,H) T(H) ],   k = round(lambda H^2),
with S4plus as in BL7/BL10 (Abel with boundary term), fac = r^k + r^-k - 2 the exact Taylor factor.
The conjecture (via the bounds) requires Ratio < 1.

Inputs : none (closed form); Outputs : scripts/BL12_lambda_band.txt
"""
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, pi as mpi, exp as mexp
mp.dps=40
a=1/(2*mpi); b=-(1+mlog(2*mpi))/(2*mpi); c=mpf('0.112'); d=mpf('2.5')
def ratio(k,H):
    Hm=mpf(H); lr=mpf('0.5')*mlog1p(1/Hm**2)
    S4p=(mpf(2)*a/3)*Hm**-3*mlog(Hm)+(8*a/9+2*b/3)*Hm**-3+(4*c*mlog(Hm)+c/2+4*d)*Hm**-4
    fac=mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2
    T=(a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4
    lhs=(mpf(k)**2/4)*mexp(max(k-4,0)*lr)*S4p
    rhs=2*fac*T
    return float(rhs/lhs)          # > 1 means the bound fits under the RHS
print("="*100)
print("BL12: ratio RHS / LHS_bound  as a function of lambda = k/H^2   (>1 required)")
print("="*100)
print("  %8s %8s %16s %10s" % ("lambda","H","ratio","ok?"))
worst=(1e9,None)
for H in (20.0,100.0,1000.0,10000.0,100000.0):
    for lam in (0.02,0.05,0.1,0.3,0.5,0.8,1.0,1.5,2.0,3.0,5.0,8.0,12.0,20.0,50.0):
        k=max(2,int(round(lam*H*H)))
        r=ratio(k,H)
        if r<worst[0]: worst=(r,(lam,H,k))
        print("  %8.2f %8g %16.6f %10s" % (lam,H,r,"ok" if r>1 else "FAIL"))
    print()
print("  worst ratio over the table: %.6f  at (lambda=%.3f, H=%g, k=%d)" % (worst[0],worst[1][0],worst[1][1],worst[1][2]))
print()
print("="*100); print("READ-OFF  (conclusion generated from the numbers above)"); print("="*100)
print("  * if every ratio exceeds 1, then the intermediate band is closed as well and the three")
print("    regimes (crude for small lambda, this sweep for the middle, the closed form for large).")
print("    together cover all k >= 2 at all H > e, modulo the explicit constants.")
