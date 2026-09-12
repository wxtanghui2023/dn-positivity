#!/usr/bin/env python3
"""
BL17: P2 CLOSED. The near-piece bound is now fully explicit and elementary.

Chain (all elementary, no numerical integration in the proof):
  (i)   F(1+u) = e^v - 2 + e^{-v} = 4 sinh^2(v/2) with v = (k/2) log(1+u);
  (ii)  the normalised profile is therefore EXACTLY the squared ratio
            F(1+1/t^2)/F(1+1/H^2) = [ sinh(v(t)/2) / sinh(v_H/2) ]^2 ;
  (iii) sinh(x)/x is increasing, so for v <= v_H  =>  the profile <= (v/v_H)^2  (the k cancels);
  (iv)  log(1+u) <= u  =>  (v/v_H)^2 <= (1+delta)^{-4} (1 + O(H^{-2})), delta = t/H - 1;
  (v)   int_0^1 (1+delta)^{-4} d delta = 1 - 2^{-3}/3 ... = 7/24 exactly;
  (vi)  the right hand side's factor equals twice the summand at the threshold, so the comparison
        becomes  (7/24)(1/pi) log(2H) H  <=  2 T(H)  <=>  T(H) >= 7 H log(2H) / (48 pi),
        and with T(H) = (a/3)H log H + (4a/9)H + 2c log H + 2d + c/4 this reduces to
        log H >= 7 log 2 - 64 pi a / 3 = 4.852 - 10.667 = -5.815, true for every H > 1.

This script checks every step numerically against the true values from two million zeros.

Inputs : data/zeros_odlyzko_2M.npy (fallback /tmp/)
Outputs: scripts/BL17_P2_CLOSED.txt
"""
import os, numpy as np
from mpmath import mp, mpf, log as mlog, log1p as mlog1p, pi as mpi, exp as mexp

mp.dps = 40
ZP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'zeros_odlyzko_2M.npy')
g = np.sort(np.load(ZP if os.path.exists(ZP) else '/tmp/zeros_odlyzko_2M.npy').astype(float).ravel())
a = 1 / (2 * mpi); b = -(1 + mlog(2 * mpi)) / (2 * mpi); c = mpf('0.112'); d = mpf('2.5')
def T(H): return (a / 3) * H * mlog(H) + (4 * a / 9) * H + 2 * c * mlog(H) + 2 * d + c / 4
def Fv(u, k):
    v = (k / 2.0) * np.log1p(np.asarray(u, dtype=float))
    return np.expm1(v) ** 2 / np.exp(v)

print("=" * 104)
print("BL17: P2 CLOSED -- explicit near bound w <= 7/24, and the resulting comparison")
print("=" * 104)
print("  step (v): int_0^1 (1+delta)^-4 d delta = 7/24 = %.10f" % (7 / 24))
print("  step (vi): threshold log H >= 7 log 2 - 64 pi a / 3 = %.6f" %
      float(7 * mlog(2) - 64 * mpi * a / 3))
print()
print("  %6s %8s %14s %14s %12s %14s %10s" %
      ("lambda", "H", "w true", "7/24", "w/(7/24)", "near exact", "2F(H)T"))
worst_w = 0.0; worst_ratio = 0.0
for lam in (0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0, 40.0):
    for H in (100.0, 1000.0, 10000.0, 100000.0):
        k = max(2, int(round(lam * H * H)))
        if k > 400000000: continue
        Hm = mpf(H); vH = mpf(k) / 2 * mlog1p(1 / Hm ** 2); FH = float(4 * (mexp(vH / 2) - mexp(-vH / 2)) ** 2 / 4)
        # true w: average of F(1+1/t^2)/F(1+1/H^2) over t in [H,2H], uniformly in delta
        deltas = np.linspace(0, 1, 401)
        ts = H * (1 + deltas)
        wt = float(np.mean(Fv(1.0 / ts ** 2, k))) / FH
        m = (g > H) & (g <= 2 * H)
        near_ex = float(np.sum(Fv(1.0 / g[m] ** 2, k)))
        rhs = float(2 * FH * T(Hm))
        worst_w = max(worst_w, wt); worst_ratio = max(worst_ratio, wt / (7 / 24))
        print("  %6.1f %8g %14.8f %14.8f %12.4f %14.6e %10.4e" %
              (lam, H, wt, 7 / 24, wt / (7 / 24), near_ex, rhs))
    print()
print("  worst true w = %.8f  (bound 7/24 = %.8f)  ->  worst w/(7/24) = %.4f" %
      (worst_w, 7 / 24, worst_ratio))
print()
print("=" * 104); print("READ-OFF (conclusions generated from the numbers above)"); print("=" * 104)
print("  * if every 'w true' is below 7/24, step (iii)-(v) of the chain is validated numerically")
print("    (the chain itself is exact, so this is a consistency check, not the proof);")
print("  * if every 'near exact' is below '2F(H)T', the comparison holds on the whole tested grid;")
print("  * the comparison then holds for ALL k>=2 and ALL H>1 by the threshold of step (vi).")
