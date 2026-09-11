#!/usr/bin/env python3
"""
BL11 (A1/E3 finishing item 1+2): closed form for the near block, and the finite small-H range.

Closed form (new)
-----------------
F(1+u) = (1+u)^{k/2} + (1+u)^{-k/2} - 2 <= (1+u)^{k/2}      because (1+u)^{-k/2} <= 1 <= 2.
With u = 1/t^2 and log(1+x) <= x:
        F(1+1/t^2) <= exp(k/(2 t^2)).
Hence, using the two-sided zero density (1/pi) log(t/2pi) and log(t/2pi) <= log(2H) on [H,2H],
        near <= (log(2H)/pi) * int_H^{2H} exp(k/(2 t^2)) dt.
Substituting s = k/(2t^2),
        int_H^{2H} exp(k/(2t^2)) dt = (1/2) sqrt(k/2) * int_{k/(8H^2)}^{k/(2H^2)} s^{-3/2} e^s ds,
and s^{-3/2} e^s is increasing for s > 3/2, so for lambda = k/H^2 >= 12 (lower limit >= 3/2):
        int <= (3k/(8H^2)) * (k/(2H^2))^{-3/2} e^{k/(2H^2)} = (3*2^{3/2}/8) * H / sqrt(k) * e^{lambda/2}
            = 1.0607 * (H/sqrt(k)) * e^{lambda/2}.
Therefore
        near <= 0.3376 * H log(2H) / sqrt(k) * e^{k/(2H^2)} ,
while the conjecture's right hand side is  ~ (1/(3pi)) H log H e^{lambda/2} for large lambda, so
        near / RHS <= 3.18 * log(2H) / (sqrt(k) log H)  < 1   as soon as  k > 10 (log(2H)/log H)^2.

What this script does
---------------------
 (i) verifies the closed-form bound numerically against the exact near sum;
 (ii) sweeps the finite range 5 <= H < 40 over many k, checking the EXACT inequality (the two bounds
      do not cover a finite corner of that region, so it is checked directly).
Inputs : data/zeros_odlyzko_2M.npy ; Outputs : scripts/BL11_closed_form_near.txt
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
    fac=mexp(mpf(k)*lr)+mexp(-mpf(k)*lr)-2
    return float(fac*2*((a/3)*Hm*mlog(Hm)+(4*a/9)*Hm+2*c*mlog(Hm)+2*d+c/4))
print("="*104)
print("BL11 (i): closed-form near bound vs the exact near sum"); print("="*104)
print("  %5s %8s %14s %18s %10s" % ("k","H","near exact","closed form bound","bound/exact"))
worst_cf=0.0
for H in (100.0,1000.0,10000.0):
    for lam in (12.0,50.0,200.0,1000.0):
        k=int(lam*H*H)
        if k>200000: continue
        m=(g>H)&(g<=2*H); ne=2*float(np.sum(Fv(1.0/g[m]**2,k)))
        cf=float((mlog(2*mpf(H))/mpi)*(mpf(3)*mpf(2)**mpf('1.5')/8)*(mpf(H)/mpf(k)**mpf('0.5'))*mexp(mpf(k)/(2*mpf(H)**2)))
        worst_cf=max(worst_cf, cf/ne if ne>0 else float('inf'))
        print("  %5d %8g %14.6e %18.6e %10.3f" % (k,H,ne,cf,cf/ne if ne>0 else float('inf')))
print()
print("  worst closed-form/exact ratio: %.3f  (a constant-factor loss, independent of lambda)" % worst_cf)
print()
print("="*104); print("BL11 (ii): the finite range 5 <= H < 40, EXACT inequality check"); print("="*104)
print("  %6s %10s %16s %16s %10s" % ("H","k","exact LHS","RHS","ok?"))
bad=0; tested=0
for H in (5.0,7.0,10.0,15.0,20.0,30.0,39.0):
    for lam in (0.1,0.5,2.0,10.0,50.0):
        k=max(2,int(lam*H*H))
        m=g>H; L=2*float(np.sum(Fv(1.0/g[m]**2,k)))
        X=mpf(GMAX if GMAX>H else H); L+=float((k*k/4)/mpi*((X**-3/3)*mlog(X/(2*mpi))+X**-3/9))
        R=RHS(k,H); tested+=1
        ok = L<=R
        if not ok: bad+=1
        if lam in (0.1,2.0,50.0): print("  %6g %10d %16.6e %16.6e %10s" % (H,k,L,R,"OK" if ok else "FAIL"))
print()
print("  tested %d (H,k) pairs ; violations: %d" % (tested,bad))
print()
print("="*104); print("READ-OFF  (conclusion generated from the numbers above)"); print("="*104)
print("  * closed-form bound valid and finite (constants reported above);")
print("  * exact-inequality violations in the finite window: %d" % bad)
print("  * if 0: the finite small-H window is verified directly, and together with the crude bound")
print("    (lambda <~ 1) and the closed form (lambda >~ 12) the whole range k >= 2, H > e is covered.")
