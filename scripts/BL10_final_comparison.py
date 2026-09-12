#!/usr/bin/env python3
"""
BL10 (A1/E3): the final comparison -- explicit difference between the proved bound and the RHS.

Claim being verified here
-------------------------
With
  LHS  := sum_{|I(rho)|>H} [ (1+1/gamma^2)^{k/2} + (1+1/gamma^2)^{-k/2} - 2 ]
  RHS  := 2 (r_H^k + r_H^{-k} - 2) [ (a/3) H log H + (4a/9) H + 2c log H + 2d + c/4 ]
  a = 1/(2 pi),  b = -(1+log 2pi)/(2 pi),  c, d  from the explicit S(T) bound,
the proof chain gives (Lemmas 1-5)
  LHS <= (k^2/4) r_H^{(k-4)+} S4plus(H),
  S4plus(H) = (2a/3) H^-3 log H + (8a/9 + 2b/3) H^-3 + (4c log H + c/2 + 4d) H^-4 ,
and division by k^2/4 together with the exact Taylor factor
  (r^k + r^-k - 2)/(k^2/4) = u^2 (1 - u + O(u^2)),   u = 1/H^2
produces the EXPLICIT DIFFERENCE (all k >= 2, because r_H^{(k-4)+} >= 1 works against us):
  RHS_side - LHS_side = -(2b/3) H^-3 + [4c log H + 4d + c/2 - (4c log H + c/2 + 4d)] H^-4 + O(H^-5 log H)
                      = (2/3)|b| H^-3 - O(H^-5 log H)   > 0    for H > e, since b < 0.
So the positive margin comes from the NEGATIVE linear coefficient b of the counting function.

Inputs / Outputs
----------------
  data/zeros_odlyzko_2M.npy  ->  scripts/BL10_final_comparison.txt
"""
import os, numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, pi as mpi, exp as mexp
mp.dps=40
ZD=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
ZP=os.path.join(ZD,'zeros_odlyzko_2M.npy'); ZEROS_PATH=ZP if os.path.exists(ZP) else 'data/zeros_odlyzko_2M.npy'
g=np.sort(np.load(ZEROS_PATH).astype(np.float64).ravel()); GMAX=g[-1]
a=1/(2*mpi); b=-(1+mlog(2*mpi))/(2*mpi); c=mpf('0.112'); d=mpf('2.5')
print("="*104)
print("BL10: the explicit difference RHS_side - LHS_side, and the exact Taylor factor")
print("="*104)
print("  a = 1/(2pi) = %.10f | b = -(1+log2pi)/(2pi) = %.10f  (b < 0: %s)" % (a,b,b<0))
print("  => the margin (2/3)|b| = %.10f" % (float(2*mpf(abs(b))/3)))
print()
print("  (i) exact Taylor factor  G(u) := ((1+u)^{k/2}+(1+u)^{-k/2}-2)/(k^2/4)  vs  u^2(1-u)")
print("  %6s %10s %16s %16s %10s" % ("k","u=1/H^2","G(u)","u^2(1-u)","G/[u^2(1-u)]"))
for k in (2,4,8):
    for H in (10.0,100.0,1000.0):
        u=mpf(1)/mpf(H)**2
        G=(mexp(mpf(k)*mlog1p(u)/2)+mexp(-mpf(k)*mlog1p(u)/2)-2)/(mpf(k)**2/4)
        t=u*u*(1-u)
        print("  %6d %10g %16.6e %16.6e %10.6f" % (k,H,G,t,float(G/t)))
print()
print("  (ii) the difference RHS_side - LHS_side (proved form), for a range of (k,H)")
print("  %5s %9s %16s %16s %16s %10s" % ("k","H","LHS_side","RHS_side","difference","diff/bound"))
bad=0
for k in (2,4):
    for H in (3.0,5.0,7.0,10.0,20.0,100.0,1000.0,10000.0):
        Hm=mpf(H)
        S4p=(mpf(2)*a/3)*Hm**-3*mlog(Hm)+(8*a/9+2*b/3)*Hm**-3+(4*c*mlog(Hm)+c/2+4*d)*Hm**-4
        lr=mpf('0.5')*mlog1p(1/Hm**2)
        fac=(mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2)/(mpf(k)**2/4)   # exact Taylor factor (r^k = exp(k*lr))
        T=(a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4
        rpow=mexp(max(k-4,0)*lr)            # r_H^{(k-4)+}  (the factor BL10 originally dropped)
        LHS_side=rpow*S4p; RHS_side=2*fac*T
        diff=RHS_side-LHS_side
        if diff<=0: bad+=1
        print("  %5d %9g %16.6e %16.6e %+16.6e %10s" % (k,H,LHS_side,RHS_side,diff,"OK" if diff>0 else "FAIL"))
print()
print("  entries with RHS_side - LHS_side <= 0 : %d" % bad)
print("  [small-H sweep: e < H < 14, where the zero table starts at gamma_1 = 14.13]")
for k in (2,4):
    for H in (3.0,5.0,7.0,10.0,14.0):
        Hm=mpf(H); S4p=(mpf(2)*a/3)*Hm**-3*mlog(Hm)+(8*a/9+2*b/3)*Hm**-3+(4*c*mlog(Hm)+c/2+4*d)*Hm**-4
        lr=mpf("0.5")*mlog1p(1/Hm**2); fac=(mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2)/(mpf(k)**2/4)
        rpow=mexp(max(k-4,0)*lr); T=(a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4
        d_=float(2*fac*T-rpow*S4p)
        print("      k=%d H=%5.1f  difference = %+12.6e   %s" % (k,H,d_,"OK" if d_>0 else "FAIL"))
print()
print("="*104); print("READ-OFF"); print("="*104)
print("  CONCLUSION (conditional on the numbers above):")
print("    entries with a non-positive difference: %d" % bad)
print("    * if 0: the comparison holds on the whole tested range, the margin being driven by the" )
print("      NEGATIVE linear coefficient b of the counting function;")
print("    * if >0: the comparison fails somewhere and must be re-examined (do NOT claim success).")
