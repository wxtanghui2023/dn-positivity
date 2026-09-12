#!/usr/bin/env python3
"""
NB3 (E24-full / A4-1): the Baez-Duarte distance d_N^2 via the FOURIER KERNEL.
Replaces the failed NB2 attempt at direct oscillatory quadrature.

Definition (Baez-Duarte form of the Nyman-Beurling criterion):
    d_N^2 = inf_{a_1..a_N real} (1/2pi) int_{-inf}^{inf}
            | 1 - zeta(1/2+it) sum_{n<=N} a_n n^{-1/2-it} |^2 dt/(1/4+t^2).
Expanding the square gives a quadratic minimisation,
    d_N^2 = 1 - l^T a + a^T K a ,   minimised by  K a = l ,  d_N^2 = 1 - l^T K^{-1} l ,
with a TRANSLATION-INVARIANT kernel (a function of the ratio only):
    K(m,n) = (1/2pi) int |zeta(1/2+it)|^2 (m/n)^{-it} dt/(1/4+t^2) = g(log(n/m)) ,
    l_n    = n^{-1/2} (1/2pi) int Re[ zeta(1/2+it) e^{-it log n} ] dt/(1/4+t^2) .
Both are one-pass Fourier transforms of the SAME grid values, so a single accurate sweep in t
suffices: that is precisely why the earlier two-dimensional oscillatory quadrature failed and this
does not. The remainder term is not oscillatory in a second variable.

VALUES OF ZETA ON THE GRID: zeta(1/2+it) = Z(t) exp(i theta(t)) with the Riemann-Siegel functions
(accurate for t >= 15); below that mpmath's zeta is used directly. This is what makes the sweep fast.

KNOWN-ANSWER CHECK (why the output can be trusted): the minimising coefficients must approximate the
Mobius function, a_n ~ mu(n), because 1/zeta(s) = sum mu(n) n^{-s} is exactly the object being
truncated. If the signs of a_n do not follow mu(n), the implementation is wrong and the value of
d_N^2 is meaningless. This check is the point of the script.

RH relevance: RH <=> d_N -> 0. Burnol proved d_N^2 >= (C+o(1))/log N with C = 2+gamma-log(4pi) =
0.0461914179..., the same constant independently verified in NB1 against two million zeros.

Inputs  : none (zeta values are computed on the grid; no data file needed)
Outputs : scripts/NB3_dN_fourier_kernel.txt
"""
import os
import numpy as np
from mpmath import mp, mpf, mpc, zeta as mzeta, log as mlog, pi as mpi, euler as meuler
from mpmath import siegelz, siegeltheta, exp as mexp

mp.dps = 26
H = 0.05           # grid step
T = 400.0          # truncation
NMAX = 40          # polynomial degree
C_burnol = 2 + float(meuler) - float(mlog(4 * mpi))

def zeta_half(t):
    """zeta(1/2 + i t) using Riemann-Siegel above 15, mpmath's zeta below."""
    if t < 15.0:
        return complex(mzeta(mpc(mpf('0.5'), mpf(t))))
    tm = mpf(t)
    return complex(mpf(siegelz(tm)) * mexp(mpc(0, 1) * siegeltheta(tm)))

ts = np.arange(0.0, T + H / 2, H)
print("=" * 100)
print("NB3: d_N^2 via the Fourier kernel, with the Mobius known-answer check")
print("=" * 100)
print("  grid: h=%.3f, T=%.0f -> %d points ; dps=%d" % (H, T, len(ts), mp.dps))
print("  Burnol constant C = 2 + gamma - log(4pi) = %.12f" % C_burnol)

# ---- one pass over the grid -------------------------------------------------------------------
CACHE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data',
                       'nb3_grid_H%.3f_T%.0f.npz' % (H, T))
zvals = np.zeros(len(ts), dtype=complex)   # zeta(1/2+it)/(1/4+t^2)
fvals = np.zeros(len(ts))                  # |zeta(1/2+it)|^2/(1/4+t^2)   (real, even)
if os.path.exists(CACHE):
    _c = np.load(CACHE)
    zvals, fvals = _c['zvals'], _c['fvals']
    print("    grid loaded from cache (%d points)" % len(ts), flush=True)
    ts = _c['ts']
for i, t in enumerate(ts):
    if os.path.exists(CACHE):
        break
    z = zeta_half(t)
    w = 1.0 / (0.25 + t * t)
    zvals[i] = z * w
    fvals[i] = (z.real * z.real + z.imag * z.imag) * w
    if i and i % 2000 == 0:
        print("    grid %d/%d" % (i, len(ts)), flush=True)
if not os.path.exists(CACHE):
    np.savez_compressed(CACHE, zvals=zvals, fvals=fvals, ts=ts)
    print("    grid done (%d points), cached to %s" % (len(ts), os.path.basename(CACHE)), flush=True)

def g(x):
    """Kernel entry: (1/pi) int_0^T f(t) cos(t x) dt  (integrand even -> half line)."""
    if x == 0.0:
        return float(np.trapz(fvals, ts)) / float(mpi)
    return float(np.trapz(fvals * np.cos(ts * x), ts)) / float(mpi)

print("  g(0) = %.10f    (= (1/pi) int_0^T |zeta|^2/(1/4+t^2) dt)" % g(0.0))

# ---- linear form at a few small n, against mu --------------------------------------------------
mus = {1: 1, 2: -1, 3: -1, 4: 0, 5: -1, 6: 1, 7: -1, 8: 0, 9: 0, 10: 1, 11: -1, 12: 0, 13: -1,
       15: 1, 16: 0, 18: 0, 20: 0, 24: 0, 30: -1, 35: 1, 40: 0}
print()
print("  %5s %6s %16s" % ("n", "mu(n)", "l_n"))
ell = {}
for n in sorted(mus):
    lg = float(mlog(n))
    ell[n] = float(np.trapz((zvals * np.exp(-1j * ts * lg)).real, ts)) / float(mpi) / np.sqrt(n)
    print("  %5d %6d %16.9f" % (n, mus[n], ell[n]))

# ---- solve K a = l for all n <= NMAX and compare a with mu -------------------------------------
N = NMAX
K = np.zeros((N, N))
lv = np.zeros(N)
for m in range(1, N + 1):
    lgm = float(mlog(m))
    for n in range(1, N + 1):
        # FIX 2026-09-12 (E26A): the defining integral carries the (mn)^{-1/2} weight.
        # Without it the kernel is inconsistent with the linear form below (which has n^{-1/2})
        # and the minimiser solves the wrong problem; convention A is the correct one.
        K[m - 1, n - 1] = g(float(mlog(n)) - lgm) / np.sqrt(float(m) * float(n))
    lv[m - 1] = float(np.trapz((zvals * np.exp(-1j * ts * lgm)).real, ts)) / float(mpi) / np.sqrt(m)

mu = np.zeros(N + 1, dtype=int)
mu[1] = 1
for i in range(1, N + 1):
    for j in range(2 * i, N + 1, i):
        mu[j] -= mu[i]

a = np.linalg.solve(K, lv)
d2 = 1.0 - float(lv @ a)

print()
print("  %5s %6s %14s %14s" % ("n", "mu(n)", "a_n", "a_n/mu(n) if mu!=0"))
for n in range(1, min(N, 26) + 1):
    ratio = (a[n - 1] / mu[n]) if mu[n] != 0 else float('nan')
    print("  %5d %6d %14.8f %14s" % (n, mu[n], a[n - 1],
          ("%.4f" % ratio) if mu[n] != 0 else "-"))

print()
print("  d_N^2 (N=%d)      = %+.10f" % (N, d2))
print("  C / log N         = %.10f" % (C_burnol / float(mlog(N))))
print("  d_N^2 * log N     = %+.10f" % (d2 * float(mlog(N))))

print()
print("=" * 100)
print("READ-OFF (conclusions generated from the numbers above)")
print("=" * 100)
idx = [n for n in range(1, min(N, 26) + 1) if mu[n] != 0]
agree = sum(1 for n in idx if np.sign(a[n - 1]) == mu[n] and abs(a[n - 1]) > 1e-9)
print("  * Mobius check: sign of a_n follows mu(n) for %d of the %d squarefree n <= 25." % (agree, len(idx)))
print("  * d_N^2 is a squared distance, so it must be positive; a negative value means the")
print("    quadrature or the kernel is wrong, not that a theorem has failed.")
print("  * Burnol's proved lower bound requires d_N^2 * log N >= C = %.6f." % C_burnol)
if d2 > 0:
    print("  * here d_N^2 = %.6e > 0 and d_N^2*log N = %.6f, so the Burnol inequality %s."
          % (d2, d2 * float(mlog(N)), "holds" if d2 * float(mlog(N)) >= C_burnol else "FAILS"))
else:
    print("  * here d_N^2 = %.6e <= 0: the implementation is wrong (see the Mobius check above)." % d2)
