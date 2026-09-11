#!/usr/bin/env python3
"""
BL15 (P3): replace the smooth zero density in the near bound by the EXPLICIT local count of the
counting hypothesis, using Abel summation so that only the hypothesis' constants enter.

Naive substitution fails: the pointwise local count from (H) is
    N(t+1)-N(t) <= (a+2c) log(t+1) + (a+b+2d),
whose leading constant a+2c is about 2.4 times the smooth density's a, which would push the ratio in
the critical band above 1. The correct route keeps sharpness by integrating by parts, exactly as in the
evaluation of S4: with M(t):=#{|rho|: |gamma|<=t} = 2N(t) and F decreasing,

    near = int_{(H,2H]} F dM = [F M]_H^{2H} - int_H^{2H} F'(t) M(t) dt
         <= F(2H)M(2H) - F(H)M(H) + int_H^{2H} |F'(t)| M_upper(t) dt,

and M_upper(t) = 2[a t log t + b t + c log t + d] uses only a,b,c,d.

This script compares the exact near sum with (i) the smooth-density integral used so far and
(ii) the new explicit Abel bound, against the conjectured right-hand side, across the band.

Inputs : data/zeros_odlyzko_2M.npy ; Outputs : scripts/BL15_P3_abel_local_count.txt
"""
import os, numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, pi as mpi, quad as mquad, exp as mexp
mp.dps=40
ZD=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'data')
ZP=os.path.join(ZD,'zeros_odlyzko_2M.npy'); ZEROS_PATH=ZP if os.path.exists(ZP) else '/tmp/zeros_odlyzko_2M.npy'
g=np.sort(np.load(ZEROS_PATH).astype(np.float64).ravel()); GMAX=g[-1]
a=1/(2*mpi); b=-(1+mlog(2*mpi))/(2*mpi); c=mpf('0.112'); d=mpf('2.5')
def Fv(u,k):
    v=(k/2.0)*np.log1p(u); return np.expm1(v)**2/np.exp(v)
def Fm(t,k):
    v=mpf(k)/2*mlog1p(1/mpf(t)**2); return (mexp(v)-1)**2/mexp(v)
def dF(t,k):   # |F'(t)|
    return abs(mquad(lambda s: 0, [0,1])) if False else None
def RHS(k,H):
    Hm=mpf(H); lr=mpf('0.5')*mlog1p(1/Hm**2)
    return float((mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2)*2*((a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4))
def Mup(t):    # 2N(t) upper, from (H)
    tm=mpf(t); return 2*(a*tm*mlog(tm)+b*tm+c*mlog(tm)+d)
print("="*104)
print("BL15 (P3): explicit local count via Abel summation, vs the smooth-density bound")
print("="*104)
print("  %7s %8s %16s %16s %16s %9s %9s" % ("lambda","H","near exact","smooth bound","Abel bound","sm/RHS","ab/RHS"))
ws=wa=0.0
for H in (100.0,1000.0,10000.0):
    Hm=mpf(H)
    for lam in (0.8,1.5,2.5,4.0,10.0):
        k=max(2,int(round(lam*H*H)))
        if k>200000: continue
        m=(g>H)&(g<=2*H); ne=2*float(np.sum(Fv(1.0/g[m]**2,k)))
        # smooth-density bound (as before)
        sm=float(mquad(lambda t: Fm(t,k)*mlog(mpf(t)/(2*mpi)), [H,2*H], maxdegree=8)/mpi)
        # explicit Abel bound: F(2H)M(2H) - F(H)M(H) + int |F'| M_up
        FH=float(Fm(H,k)); F2H=float(Fm(2*H,k))
        inte=float(mquad(lambda t: abs(mpf(k)/2*mlog1p(1/mpf(t)**2)) * 0 + 0, [H,2*H])) if False else None
        # |F'(t)| computed numerically at nodes
        tn=np.linspace(float(H),2*float(H),201)
        dFv=np.array([float(abs((Fm(float(x)*1.000001,k)-Fm(float(x),k))/(float(x)*1e-6))) for x in tn[1:-1]])
        integ=np.trapz(np.array([Mup(float(x).__float__() if hasattr(float(x),'__float__') else x) for x in tn[1:-1]],dtype=float)*dFv, tn[1:-1])
        ab=F2H*float(Mup(2*H))-FH*float(Mup(H))+integ
        R=RHS(k,H)
        ws=max(ws,sm/R); wa=max(wa,ab/R)
        print("  %7.1f %8g %16.6e %16.6e %16.6e %9.4f %9.4f" % (lam,H,ne,sm,ab,sm/R,ab/R))
    print()
print("  worst smooth/RHS = %.4f ; worst Abel/RHS = %.4f" % (ws,wa))
print()
print("="*104); print("READ-OFF  (conclusion generated from the numbers above)"); print("="*104)
print("  * if the Abel column stays below 1, the near bound no longer needs the smooth density, and the")
print("    explicit constants of the counting hypothesis suffice;")
print("  * the pointwise local count was NOT used precisely because its constant a+2c is far larger.")
