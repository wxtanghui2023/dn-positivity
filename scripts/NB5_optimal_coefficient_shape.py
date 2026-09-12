#!/usr/bin/env python3
"""
NB5 (A4-2): what shape do the OPTIMAL coefficients of the Baez-Duarte distance have?

Registered item A4-2 asks to test the proposed shape  a_n ~ mu(n) (1 - log n / log x)
against the coefficients that actually minimise the distance. The minimisation is the same one
solved in NB3/NB4 (kernel K a = l, kernel a function of the ratio of the indices only), reusing the
cached grid of zeta values so the run is fast.

Three models are fitted to the computed minimiser and compared by relative residual:
   M1 proportional : a_n = c mu(n)
   M2 cutoff       : a_n = c mu(n) (1 - log n / log N)
   M3 fitted cutoff: a_n = c mu(n) (1 - log n / log x), x fitted over a grid
A fourth, purely descriptive, quantity is the correlation of a_n/mu(n) with 1 - log n/log N.

Inputs : data/nb3_grid_H0.050_T400.npz (written by NB3)
Outputs: scripts/NB5_optimal_coefficient_shape.txt
"""
import os, glob
import numpy as np
from mpmath import mp, pi as mpi, log as mlog

mp.dps = 26
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cand = sorted(glob.glob(os.path.join(ROOT, 'data', 'nb3_grid_*.npz')))
assert cand, "run NB3_dN_fourier_kernel.py first (it writes the cached grid)"
c = np.load(cand[-1]); ts, fvals, zvals = c['ts'], c['fvals'], c['zvals']

XS = np.arange(0.0, 6.0, 0.0005)   # refined 2026-09-12 (was 0.0025) to cut interpolation error
_SPL = None
try:
    from scipy.interpolate import CubicSpline as _CS
    _SPL = True
except Exception:
    _SPL = False
GS = np.array([float(np.trapz(fvals * np.cos(ts * x), ts)) / float(mpi) if x > 0
               else float(np.trapz(fvals, ts)) / float(mpi) for x in XS])
if _SPL:
    from scipy.interpolate import CubicSpline as _CS2
    _F = _CS2(XS, GS)

def gI(x):
    xa = np.abs(np.asarray(x, float))
    r = _F(xa) if _SPL else np.interp(xa, XS, GS)
    return r if np.ndim(r) else float(r)

N = 160
lgn = np.log(np.arange(1, N + 1))
K = np.empty((N, N)); lv = np.empty(N)
for m in range(1, N + 1):
    K[m - 1] = gI(lgn - np.log(m)) / np.sqrt(np.arange(1, N + 1, dtype=float) * float(m))
    lv[m - 1] = float(np.trapz((zvals * np.exp(-1j * ts * np.log(m))).real, ts)) / float(mpi) / np.sqrt(m)
a = np.linalg.solve(K, lv)
d2 = 1.0 - float(lv @ a)

mu = np.zeros(N + 1, dtype=int); mu[1] = 1
for i in range(1, N + 1):
    for j in range(2 * i, N + 1, i):
        mu[j] -= mu[i]
muN = mu[1:]
idx = np.nonzero(muN)[0]                      # squarefree indices only (mu != 0)
print("=" * 100)
print("NB5 (A4-2): shape of the optimal coefficients at N = %d (d_N^2 = %.8f)" % (N, d2))
print("=" * 100)

def fit_scale(model, use):
    """least-squares scalar c for a_n ~ c * model_n, restricted to `use` indices."""
    denom = float(np.dot(model[use], model[use]))
    c = float(np.dot(a[use], model[use])) / denom if denom > 0 else 0.0
    res = a[use] - c * model[use]
    rel = float(np.linalg.norm(res) / max(np.linalg.norm(a[use]), 1e-300))
    return c, rel

print("\n  fits restricted to the %d squarefree indices n <= %d" % (len(idx), N))
m1 = muN.astype(float)
c1, r1 = fit_scale(m1, idx)
print("  M1  a_n = c mu(n)                       : c = %+.6f , rel.residual = %.4f" % (c1, r1))
m2 = muN.astype(float) * (1.0 - lgn / np.log(N))
c2, r2 = fit_scale(m2, idx)
print("  M2  a_n = c mu(n)(1 - log n/log N)      : c = %+.6f , rel.residual = %.4f" % (c2, r2))
best = (9e9, None, None)
for lx in np.linspace(np.log(N), np.log(N) * 3.0, 60):
    m3 = muN.astype(float) * (1.0 - lgn / lx)
    if not np.all(np.isfinite(m3)):
        continue
    c3, r3 = fit_scale(m3, idx)
    if r3 < best[0]:
        best = (r3, lx, c3)
r3, lx, c3 = best
print("  M3  a_n = c mu(n)(1 - log n/log x), x fit: c = %+.6f , x = %.3f (= %.2f N) , rel.residual = %.4f"
      % (c3, np.exp(lx), np.exp(lx) / N, r3))
print("\n  correlation of a_n/mu(n) with 1 - log n/log N over squarefree n:")
rat = a[idx] / muN[idx]
shp = 1.0 - lgn[idx] / np.log(N)
print("     pearson r = %+.4f" % float(np.corrcoef(rat, shp)[0, 1]))
print("     (a_n/mu(n) itself ranges from %+.4f to %+.4f)" % (rat.min(), rat.max()))
print()
print("=" * 100); print("READ-OFF (conclusions generated from the numbers above)"); print("=" * 100)
print("  * the model with the smallest relative residual is the better description of the shape;")
print("  * a residual close to 1 means the model explains almost nothing, since it is already a")
print("    scalar multiple fitted to the data;")
print("  * verdict: %s" % ("the cutoff shape is NOT supported" if min(r1, r2, r3) > 0.9
                        else "the cutoff shape improves on proportionality"))
print("  * note: the sign structure is exactly mu (checked in NB3/NB4); what is at issue here is")
print("    only the shape of the magnitudes.")
