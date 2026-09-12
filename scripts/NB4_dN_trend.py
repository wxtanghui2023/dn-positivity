#!/usr/bin/env python3
"""
NB4 (E24-full, part 2): the N-dependence of the Baez-Duarte distance d_N^2.

Purpose : turn the single value of NB3 into a TREND, so that the computed distance can be
          compared with Burnol's proved lower bound d_N^2 >= (C+o(1))/log N, C = 2+gamma-log(4pi).
Method  : reuse NB3's Fourier-kernel construction, but tabulate g on a grid of x = log(n/m)
          and interpolate, which makes the N^2 kernel entries cheap; then solve K a = l for a
          sequence of N and report d_N^2, d_N^2 log N, and the Mobius agreement at each N.
          The grid of zeta values is read from the cache written by NB3 (data/nb3_grid_*.npz),
          so this script runs in seconds rather than minutes.
Inputs  : data/nb3_grid_H0.050_T400.npz (written by NB3; if absent, NB3 must be run first)
Outputs : scripts/NB4_dN_trend.txt
"""
import os, glob
import numpy as np
from mpmath import mp, pi as mpi, log as mlog, euler as meuler

mp.dps = 26
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cands = sorted(glob.glob(os.path.join(ROOT, 'data', 'nb3_grid_*.npz')))
assert cands, "no cached grid: run NB3_dN_fourier_kernel.py first"
c = np.load(cands[-1])
ts, fvals, zvals = c['ts'], c['fvals'], c['zvals']
print("=" * 100)
print("NB4: N-dependence of d_N^2 (grid from %s, %d points)" % (os.path.basename(cands[-1]), len(ts)))
print("=" * 100)
C = 2 + float(meuler) - float(mlog(4 * mpi))
print("  Burnol constant C = %.12f ; prediction d_N^2 ~ C/log N" % C)

# tabulate g on a fine x-grid and interpolate
XS = np.arange(0.0, 6.0, 0.0025)
GS = np.array([float(np.trapz(fvals * np.cos(ts * x), ts)) / float(mpi) if x > 0
               else float(np.trapz(fvals, ts)) / float(mpi) for x in XS])
def gI(x):
    r = np.interp(np.abs(np.asarray(x, dtype=float)), XS, GS)
    return r if r.ndim else float(r)

def solve(N):
    K = np.empty((N, N)); lv = np.empty(N)
    lgn = np.log(np.arange(1, N + 1))
    for m in range(1, N + 1):
        K[m - 1] = gI(lgn - np.log(m)) / np.sqrt(np.arange(1, N + 1, dtype=float) * float(m))
        lv[m - 1] = float(np.trapz((zvals * np.exp(-1j * ts * np.log(m))).real, ts)) / float(mpi) / np.sqrt(m)
    a = np.linalg.solve(K, lv)
    return 1.0 - float(lv @ a), a

mu = np.zeros(201, dtype=int); mu[1] = 1
for i in range(1, 201):
    for j in range(2 * i, 201, i):
        mu[j] -= mu[i]

print()
print("  %5s %16s %14s %14s %12s %10s" % ("N", "d_N^2", "d^2*log N", "C/log N", "d^2/(C/logN)", "mu agree"))
for N in (2, 5, 10, 20, 40, 80, 120, 160):
    d2, a = solve(N)
    idx = [n for n in range(1, N + 1) if mu[n] != 0]
    agree = sum(1 for n in idx if np.sign(a[n - 1]) == mu[n] and abs(a[n - 1]) > 1e-9)
    print("  %5d %16.9f %14.9f %14.9f %12.4f %6d/%-4d" %
          (N, d2, d2 * float(mlog(N)), C / float(mlog(N)), d2 / (C / float(mlog(N))), agree, len(idx)))
print()
print("=" * 100); print("READ-OFF (conclusions generated from the numbers above)"); print("=" * 100)
print("  * the Mobius column is the known-answer check; it must stay near 100% for the numbers")
print("    to mean anything.")
print("  * if d_N^2 decreases with N, the computed distance behaves as the criterion requires;")
print("    the comparison column shows how far the finite-N value still is from the asymptotic")
print("    constant of Burnol's lower bound, which is expected to be approached only slowly.")
