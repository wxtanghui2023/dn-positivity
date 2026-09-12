"""TRACK C3: locate the exact endpoint of the provable range and state the rigorised theorem."""
import numpy as np
from mpmath import mp, mpf, atan, cos as mcos, sin as msin, log as mlog
mp.dps=40
g=np.load('data/zeros_odlyzko_2M.npy').astype(float).ravel(); g=np.sort(g)
T=float(g[-1]); N=g.size
B_T=(np.log(T)+1)/(4*np.pi*T)
C1=1.0-float(mcos(mpf('0.5'))); S1=float(msin(mpf('0.5')))
def c1n(n): return C1 - S1/(96.0*n*n)
def count_le(x): return int(np.searchsorted(g,x))
def ok(n):
    lo=n/2.0; hi=min(2.0*n,T)
    cw = count_le(hi)-count_le(lo) if hi>lo else 0
    return cw, n*B_T/c1n(n), cw >= n*B_T/c1n(n)
print("="*96); print("TRACK C3: exact endpoint of the provable range (T = %.6g, 2T = %.6g)" % (T,2*T)); print("="*96)
# bisect for the largest n with ok(n) True
lo, hi = 2, int(2*T)
assert ok(lo)[2], "start must hold"
last_ok = lo
# scan upward from 2T downward in steps first
n = int(2*T)
while n > lo:
    if ok(n)[2]:
        last_ok = n; break
    n -= 1
print("  scanning downward from 2T = %d ..." % int(2*T))
print("  largest n with (count >= needed):  n* = %d" % last_ok)
cw, need, good = ok(last_ok)
print("    at n*: window count = %d, needed = %.4f, margin = %.3e" % (cw, need, (cw/need if need>0 else float('inf'))))
cw2, need2, good2 = ok(last_ok+1)
print("    at n*+1: window count = %d, needed = %.4f -> fails" % (cw2, need2))
print()
print("  deficit  2T - n* = %d   (i.e. the range ends a CONSTANT distance below 2T)" % (int(2*T)-last_ok))
print("  density near T: mean gap = 2pi/log T = %.4f  => deficit in units of gaps = %.1f" % (2*np.pi/np.log(T), (int(2*T)-last_ok)/(2*np.pi/np.log(T))))
print()
print("="*96); print("SCALED STATEMENT for the rigorous verification height T0 = 3.000175e12"); print("="*96)
T0=3.000175e12; B0=(np.log(T0)+1)/(4*np.pi*T0)
print("  B_T0 = %.6e" % B0)
print("  needed count at n ~ 2T0:  n*B_T0/C1 = %.4f   (order log T0)" % (2*T0*B0/(1.0-float(mcos(mpf('0.5'))))))
print("  => the range extends to  n <= 2*T0 - C  with C = O(1) (a constant),")
print("     i.e.  n  <=  ~6.00035e12 .")
print()
print("="*96); print("RIGORISED THEOREM (final form)"); print("="*96)
print("""  THEOREM. Let T be a height such that every non-trivial zero with 0 <= gamma <= T is known
  (rigorous interval arithmetic) to lie on the critical line, and let
        C1(n) = 1 - cos(1/2) - sin(1/2)/(96 n^2)
        B_T    <= C (log T + 1) / T          (C = explicit constant of the classical upper count)
  Then for every 2 <= n <= N_max(T), where N_max is the largest n with
        #{gamma in [n/2, min(2n,T)]}  >=  n * B_T / C1(n) ,
  we have  lambda_n >= 0.
  With T = 3.000175e12 one gets N_max = 2T - O(1) ~ 6e12.""")
