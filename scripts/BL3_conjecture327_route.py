"""
BL3: test the ROUTE to Droll's Conjecture 3.2.7 (the named task of A1).

Conjecture 3.2.7 (Droll 2012, read from the thesis): for k >= 2 integer, real tau with 1 <= tau < 2,
and H > e, with r_H(tau) := (1 + tau/H^2)^{1/2},
    sum_{|I(rho)|>H} [ (1 + tau/gamma_rho^2)^{k/2} + (1 + tau/gamma_rho^2)^{-k/2} - 2 ]
        <=  2 [ r_H^k + r_H^{-k} - 2 ] * [ aH log H / 3 + (4a+3b+)H/9 + 2c log H + 2d + c/4 ] .

KEY OBSERVATION (ours): put x_rho := 1 + tau/gamma_rho^2 > 1 for |gamma_rho| > H > 0.
  Then the summand is  F(x) = x^{k/2} + x^{-k/2} - 2 = (x^{k/4} - x^{-k/4})^2 >= 0
  and F is INCREASING in x > 1  (F'(x) = (k/2)(x^{k/2-1} - x^{-k/2-1}) > 0 for x>1, k>=2).
  Since x_rho <= 1 + tau/H^2 = r_H^2, we get summand <= r_H^k + r_H^{-k} - 2.
  =>  LHS <= (r_H^k + r_H^{-k} - 2) * #{zeros with |gamma| > H} .

So: the conjecture REDUCES TO A COUNTING BOUND -- provided one does NOT expand into a power series
(which is precisely the step that fails in Brown's proof: the coefficients alternate in sign).
Note: x > 1 holds exactly for |gamma| > 0, and Brown's error 1 (claiming x^k + x^{-k} increasing for
ALL x>0, whereas it holds only for x>1) is -- per Droll -- irrelevant in Brown's classical case.
So in the classical/special case the monotonicity route is VALID.

This script tests the inequality LHS <= (monotone factor) * count on REAL zeros data.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, e as me
import os as _os
_ZD = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),'data')
_ZP = _os.path.join(_ZD,'zeros_odlyzko_2M.npy')
ZEROS_PATH = _ZP if _os.path.exists(_ZP) else '/tmp/zeros_odlyzko_2M.npy'   # R2: prefer data/
ZEROS_100K = _os.path.join(_ZD,'zeros_odlyzko_100k.npy') if _os.path.exists(_os.path.join(_ZD,'zeros_odlyzko_100k.npy')) else '/tmp/zeros_odlyzko_100k.npy'

mp.dps=30
g=np.load(ZEROS_PATH).astype(np.float64).ravel(); g=np.sort(g)
print("="*96)
print("BL3: the monotonicity route to Conjecture 3.2.7 -- numerical test on real zeros")
print("="*96)
print("  zeros loaded: %d, max gamma = %.6g" % (g.size, g[-1]))
print()
print("  %6s %6s %12s %16s %16s %10s %12s" % ("k","tau","H","LHS (partial)","mono bound","ratio","#zeros>H"))
for k in (2,4,8):
    for tau in (1.0,1.5):
        for H in (100.0,1000.0,10000.0):
            m = g>H
            cnt = int(m.sum())
            x = 1.0 + tau/g[m]**2
            lhs = float(np.sum(x**(k/2) + x**(-k/2) - 2.0))
            rH = (1.0+tau/H**2)**0.5
            mono = (rH**k + rH**(-k) - 2.0)*cnt
            print("  %6d %6.1f %12g %16.6e %16.6e %10.4f %12d" % (k,tau,H,lhs,mono, lhs/mono if mono>0 else float('nan'),cnt))
print()
print("  ==> ratio <= 1 means LHS <= monotone-factor * count  (the route is valid)")
print()
print("="*96); print("CHECK: is the summand really non-negative and increasing in x>1 ?"); print("="*96)
for k in (2,4,8):
    for x in (1.0000001,1.001,1.01,1.1,2.0):
        F=x**(k/2)+x**(-k/2)-2
        print("    k=%d x=%.7f  F=%.6e  (should be >=0 and increasing in x)" % (k,x,F))
    print()
print("="*96); print("READ-OFF"); print("="*96)
print("""  * the summand is (x^{k/4} - x^{-k/4})^2 >= 0 and increasing for x > 1;
  * hence the whole conjecture reduces to a COUNT of zeros beyond H -- which the classical
    explicit counting bounds supply;
  * the power-series expansion (Brown's failing step) is therefore AVOIDABLE:
    the alternating coefficients never need to be summed.""")
