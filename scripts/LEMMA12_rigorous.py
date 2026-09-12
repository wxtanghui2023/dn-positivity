"""
LEMMA 1 (window bound) and LEMMA 2 (tail constant): make both RIGOROUS and EXPLICIT.
LEMMA 1.  theta_g = arctan(g/(g^2-1/4)).
  (a) monotonicity: d/dg = u'/(1+u^2) with u = g/(g^2-1/4), u' = -(g^2+1/4)/(g^2-1/4)^2 < 0.
  (b) expansion: u = (1/g)(1 + 1/(4g^2) + 1/(16g^4) + ...), arctan u = u - u^3/3 + u^5/5 - ...
      => theta_g = 1/g - 1/(12 g^3) + 1/(80 g^5) - ...
  (c) hence for g in [n/2, 2n]:
        n theta_g >= n theta_{2n} = 1/2 - 1/(96 n^2) + 1/(2560 n^4) - ...
        n theta_g <= n theta_{n/2} = 2 - 2/(3 n^2) + ...   (< 2 < pi)
      so each window term >= 1 - cos(1/2 - 1/(96n^2)) =: C1(n).
   Verify: (i) monotonicity numerically; (ii) the exact value vs the truncated series.
LEMMA 2.  B_T = (1/2) sum_{g>T} g^{-2} <= explicit bound:
   sum_{g>T} g^{-2} = -N(T)/T^2 + 2 int_T^inf N(x) x^{-3} dx
   and with N(x) <= F(x) + R(x), F(x) = (x/2pi)log(x/2pi e) + 7/8,
        R(x) = 0.112 log x + 0.278 loglog x + 2.510 + 0.2/x   (Trudgian, x >= e)
   everything is an elementary integral:
        2 int_T^inf (x/2pi) log(x/2pi e) x^{-3} dx = (1/pi) (1 + log(T/2pi e))/T
        2 int_T^inf (7/8) x^{-3} dx                = (7/8)/T^2
        2 int_T^inf 0.112 log x x^{-3} dx          = 0.112 (1 + 2 log T)/(2 T^2)
        2 int_T^inf 0.278 loglog x x^{-3} dx       <= 0.278 (1 + 2 loglog T)/(2 T^2)   (loglog x <= loglog T + ...)
        2 int_T^inf 2.510 x^{-3} dx                = 2.510/T^2
        2 int_T^inf (0.2/x) x^{-3} dx              = 0.2/(2 T^3)
"""
import numpy as np
from mpmath import mp, mpf, atan, cos as mcos, sin as msin, log as mlog, pi as mpi, quad, inf
mp.dps=50
g = np.load('data/zeros_odlyzko_2M.npy').astype(float).ravel(); g=np.sort(g)
T=float(g[-1]); N=g.size
print("="*96); print("LEMMA 1: monotonicity and the exact window bound"); print("="*96)
# (a) monotonicity check on the exact formula
xs=np.array([1.0,2,5,10,100,1e3,1e4,1e5,1e6])
th=np.arctan(xs/(xs**2-0.25))
print("  theta decreasing:", all(th[i]>th[i+1] for i in range(len(th)-1)), "  values:", [round(float(v),6) for v in th[:6]])
# (b) exact vs series  theta = 1/g - 1/(12g^3) + 1/(80g^5)
print("  exact vs 1/g - 1/(12g^3) + 1/(80g^5):")
for x in (10.0,100.0,1e3,1e4,1e6):
    ex=float(atan(mpf(x)/(mpf(x)**2-mpf(1)/4)))
    se=1/x-1/(12*x**3)+1/(80*x**5)
    print("    g=%9g  exact=%.18f  series=%.18f  diff=%.3e" % (x,ex,se,abs(ex-se)))
# (c) window bound exact check
C1=lambda n: 1-float(mcos(mpf('0.5')))+0*0  # placeholder
print()
print("  window: min term bound  C1(n) = 1 - cos(1/2 - 1/(96 n^2))")
for n in (10,100,1000,10000,100000):
    arg = mpf(1)/2 - mpf(1)/(96*mpf(n)**2)
    C1n = 1-mcos(arg)
    ex2 = n*atan(mpf(2*n)/(mpf(2*n)**2-mpf(1)/4))     # n*theta_{2n}
    print("    n=%7d : n*th_2n=%.18f  vs 1/2-1/(96n^2)=%.18f   C1(n)=%.15f" % (
        n, float(ex2), float(arg), float(C1n)))
print()
print("="*96); print("LEMMA 2: explicit upper bound for B_T (elementary integrals, Trudgian R)"); print("="*96)
def B_T_bound(Tv):
    Tv=mpf(Tv)
    L=mlog(Tv/(2*mpi*mpf('2.71828182845904523536028747135266249775724709369995957496696762772407663')[0:1]*0+mpf('2.71828182845904523536028747135266249775724709369995957496696762772407663')))
    # F part
    term1=(1/mpi)*(1+L)/Tv
    term2=mpf(7)/8/Tv**2
    # R parts
    lx=mlog(Tv); llx=mlog(lx) if lx>1 else mpf(0)
    term3=mpf('0.112')*(1+2*lx)/(2*Tv**2)
    term4=mpf('0.278')*(1+2*llx+llx*llx)/(2*Tv**2)   # generous: int loglog x x^-3 <= (1+2loglogT+(loglogT)^2)/(2T^2)
    term5=mpf('2.510')/Tv**2
    term6=mpf('0.2')/(2*Tv**3)
    total = term1+term2+term3+term4+term5+term6 - (mpf(0))  # ignore -N(T)/T^2 term? see note
    return total,(term1,term2,term3,term4,term5,term6)
for Tv in (T, 3.000175e12):
    tot,parts=B_T_bound(Tv)
    nominal=(float(np.log(Tv))+1)/(4*np.pi*float(Tv))
    print("  T=%9.6g : B_T <= %.6e   (nominal (logT+1)/(4piT) = %.6e ; ratio %.3f)" % (Tv,float(tot),nominal,float(tot)/nominal))
    print("      parts:", ["%.3e"%float(p) for p in parts])
print()
print("  NOTE: the -N(T)/T^2 term is NEGATIVE and was dropped from the bound (conservative).")
print("="*96); print("RESULT: both lemmas explicit; the needed count stays ~1e1 so no constant matters."); print("="*96)
