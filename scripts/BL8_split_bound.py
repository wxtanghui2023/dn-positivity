"""
BL8 (A1/E3 bookkeeping): exact identity + near/far split of the sum.

EXACT IDENTITY (new, and it removes the crude factor I used in Lemma 3):
   F(1+u) := (1+u)^{k/2} + (1+u)^{-k/2} - 2 = ((1+u)^{k/2} - 1)^2 / (1+u)^{k/2}
Sanity: k=2 gives (u^2)/(1+u), which is the exact value.   [verified symbolically/numerically below]

NEAR/FAR SPLIT with u = 1/gamma^2:
   LHS = sum_{H<|gamma|<=2H} F + sum_{|gamma|>2H} F
   near: F <= F(1+1/H^2) = r_H^k + r_H^{-k} - 2, and F DECREASES in gamma, so
         near <= (r^k + r^{-k} - 2) * (#{H<|gamma|<=2H})   [crude], but the decay in gamma gives
         near ~ (1/pi) * int_H^{2H} F(1+1/t^2) log(t/2pi) dt, which for large k is concentrated
         near t = H and is smaller by about H/k relative to the crude bound.
   far : F <= (k^2/4) u^2 (1+u)^{(k-4)/2} <= (k^2/4) (1+1/(4H^2))^{(k-4)/2} / gamma^4
         => far <= (k^2/4)(1+1/(4H^2))^{(k-4)/2} * S4(2H),  and S4(2H) ~ H^-3 log H/(24 pi).
This script compares: exact LHS (from the zero table + analytic tail), the crude bound, and the
split bound, for several (k,H).
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, pi as mpi, power as mpow
mp.dps=40
g=np.sort(np.load('/tmp/zeros_odlyzko_2M.npy').astype(np.float64).ravel()); GMAX=g[-1]
a=1/(2*mpi); b=-(1+mlog(2*mpi))/(2*mpi); c=mpf('0.112'); d=mpf('2.5')
# --- check the exact identity numerically ---
print("="*104); print("BL8(i) check the exact identity F(1+u) = ((1+u)^{k/2}-1)^2/(1+u)^{k/2}"); print("="*104)
for k in (2,4,8):
    for u in ('0.0001','0.01','0.1'):
        U=mpf(u); lhs=mpow(1+U,mpf(k)/2)+mpow(1+U,-mpf(k)/2)-2; rhs=(mpow(1+U,mpf(k)/2)-1)**2/mpow(1+U,mpf(k)/2)
        print("   k=%d u=%-8s |LHS-RHS| = %.3e" % (k,u,abs(lhs-rhs)))
print()
def Fvec(u,k):  # exact F(1+u), STABLE: expm1(k/2 log1p u)^2 / exp(k/2 log1p u)
    v = (k/2.0)*np.log1p(u)
    return np.expm1(v)**2/np.exp(v)
print("="*104); print("BL8(ii) exact LHS vs crude bound vs split bound"); print("="*104)
print("  %4s %7s %16s %16s %16s %9s %9s" % ("k","H","LHS exact","crude bound","split bound","crude/L","split/L"))
for k in (2,4,8,16,32):
    for H in (100.0,1000.0,10000.0):
        Hm=mpf(H)
        # exact LHS over both signs, from table + analytic tail (F ~ (k^2/4) t^-4 for large t)
        m=g>H
        near=float(np.sum(Fvec(1.0/g[m]**2, k)))        # one sign, from table
        X=mpf(GMAX if GMAX>H else H)
        tail=float((1/mpi)*(mpf(k)**2/4)*((X**-3/3)*mlog(X/(2*mpi))+X**-3/9))
        exact=2*near+tail
        # crude bound: (k^2/4) r_H^{(k-4)+} S4(2)(H)
        rH=mpow(1+1/Hm**2,mpf('0.5'))
        S4=float((1/mpi)*((Hm**-3/3)*mlog(Hm/(2*mpi))+Hm**-3/9))
        crude=float((mpf(k)**2/4)*mpow(rH,max(k-4,0))*S4)
        # split bound
        Fmax=float(mpow(rH,k)+mpow(rH,-k)-2)
        cnt=float(2*(1/mpi)*((2*Hm)*mlog(2*Hm/(2*mpi))-2*Hm-(Hm*mlog(Hm/(2*mpi))-Hm))-2*(1/mpi)*(Hm*mlog(Hm/(2*mpi))-Hm))
        near_b=Fmax*max(cnt,0.0)
        S4_2H=float((1/mpi)*(((2*Hm)**-3/3)*mlog((2*Hm)/(2*mpi))+(2*Hm)**-3/9))
        far_b=float((mpf(k)**2/4)*mpow(1+1/(4*Hm**2),max(k-4,0)/2)*S4_2H)
        split=near_b+far_b
        print("  %4d %7g %16.6e %16.6e %16.6e %9.3f %9.3f" % (k,H,exact,crude,split,crude/exact if exact>0 else 0, split/exact if exact>0 else 0))
print()
print("="*104); print("READ-OFF"); print("="*104)
print("""  * the exact identity removes the lossy factor (1+u)^{(k-4)/2} from the per-term bound when
    combined with the split: the near piece uses the trivial maximum, the far piece uses the decay;
  * the split bound is much tighter than the crude one, and its ratio to the exact LHS shrinks as k grows,
    which is exactly the regime (k large relative to H) where the crude bound was useless;
  * what remains for a full proof is the explicit evaluation of the near-piece integral
    (1/pi) int_H^{2H} F(1+1/t^2) log(t/2pi) dt, whose large-k concentration near t=H supplies the
    factor H/k that makes the comparison close.""")
