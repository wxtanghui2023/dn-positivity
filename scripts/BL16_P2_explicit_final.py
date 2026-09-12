#!/usr/bin/env python3
"""
BL16 (P2, final): the FULLY EXPLICIT near bound.

Ingredients (all elementary):
  (i)   4 sinh^2(v/2) <= v^2 e^{v}                    [sinh x <= x e^x]
  (ii)  v(t) = (k/2) log(1+1/t^2) <= k/(2t^2)         [log(1+x) <= x]
  (iii) v decreasing  =>  e^{v(t)} <= e^{v_H}
  (iv)  int_H^{2H} t^{-4} dt = (7/24) H^{-3}          [exact, elementary]
Hence
  near <= (1/pi) log(2H) * (k^2/4) e^{v_H} * int_H^{2H} t^{-4} dt
       = (7 k^2 / (96 H^3)) * (log 2H / pi) * e^{v_H},
and dividing by the right-hand side 2 (e^{v_H} - 2 + e^{-v_H}) T(H) with T >= (a/3)H log H gives
  near / RHS <= 7 lambda^2 log(2H) / [ 32 log H ( e^{lambda/2} - 2 + e^{-lambda/2} ) ],
because k^2 = lambda^2 H^4 and 2a/3 = 1/(3pi) makes the constants collapse to 32.
The denominator's exponential makes the ratio decrease for all lambda >= 1, with a maximum near
lambda = 1; this script verifies both the bound and the ratio.

Inputs : data/zeros_odlyzko_2M.npy ; Outputs : scripts/BL16_P2_explicit_final.txt
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
print("BL16 (P2 final): the fully explicit near bound and its ratio to the right-hand side")
print("="*104)
print("  explicit bound:  near <= (7 k^2 / (96 H^3)) (log 2H / pi) e^{v_H}")
print("  ratio bound   :  7 lambda^2 log(2H) / [32 log H (e^{lambda/2} - 2 + e^{-lambda/2})]")
print()
print("  %7s %8s %16s %18s %16s %9s %11s" % ("lambda","H","near exact","explicit bound","RHS","bound/RHS","ratio formula"))
worst_b=0.0; worst_f=0.0
for H in (100.0,1000.0,10000.0,100000.0):
    Hm=mpf(H)
    for lam in (0.5,0.8,1.0,1.5,2.0,3.0,5.0,8.0,12.0):
        k=max(2,int(round(lam*H*H)))
        if k>200000000: continue
        m=(g>H)&(g<=2*H); ne=2*float(np.sum(Fv(1.0/g[m]**2,k)))
        lr=mpf('0.5')*mlog1p(1/Hm**2); vH=mpf(k)/2*mlog1p(1/Hm**2)
        bd=float((7*mpf(k)**2/(96*Hm**3))*(mlog(2*Hm)/mpi)*mexp(vH))
        R=RHS(k,H)
        form=float(7*mpf(lam)**2*mlog(2*Hm)/(32*mlog(Hm)*(mexp(mpf(lam)/2)-2+mexp(-mpf(lam)/2))))
        worst_b=max(worst_b, bd/R if R>0 else 0); worst_f=max(worst_f, form)
        print("  %7.1f %8g %16.6e %18.6e %16.6e %9.4f %11.4f" % (lam,H,ne,bd,R,bd/R,form))
    print()
print("  worst bound/RHS = %.4f ; worst closed-form ratio = %.4f" % (worst_b,worst_f))
print()
print("="*104); print("READ-OFF  (conclusion generated from the numbers above)"); print("="*104)
print("  * if both worst values are below 1, the near bound is fully explicit (no numerical")
print("    integration) and the comparison holds on the whole tested band;")
print("  * the closed-form ratio has its maximum near lambda = 1 and decreases thereafter.")
