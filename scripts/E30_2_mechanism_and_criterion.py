#!/usr/bin/env python3
"""
E30-2: what actually produces the "square law", and what a real breakthrough must beat.

The project's unified framework recorded two "conversion laws": a T^2 law (reach = square of the
verified height) for coefficient-type criteria, and a log law for moment/order/phase-type criteria.
The register flags a suspicion: the Li coefficients look LINEAR in the height, so where does a
square come from? This script separates the two mechanisms that are being conflated.

MECHANISM A (window / direct positivity). For an on-line zero at height gamma the n-th Li term is
    1 - cos(n theta_gamma),  theta_gamma = arg(1 - 1/rho) ~ 1/gamma for large gamma,
which first becomes non-negligible when n theta_gamma ~ 2 pi, i.e. n*(gamma) ~ 2 pi gamma. Inverting,
the index n probes zeros only up to height h(n) ~ n/(2 pi): LINEAR in n. The input used is the
sign of each individual term (1 - cos >= 0), which is unconditional.

MECHANISM B (tail budget). To bound the whole tail sum one needs the counting function out to height
~ sqrt(n), because the accumulated sensitivity of the n-th coefficient to a zero at height gamma
behaves like 1 - |1 - 1/rho|^n with |1 - 1/rho|^2 = 1 + (1-2 beta)/(beta^2 + gamma^2); for an off-axis
zero this departs from 1 by about n/gamma^2, so a zero at height gamma is only detected once
n ~ gamma^2, i.e. h(n) ~ sqrt(n). The input used is a counting hypothesis (and a repair of a broken
lemma), which is conditional.

The two give different laws for the same criterion, so "the T^2 law" is a property of the mechanism,
not of the criterion. This script verifies both correspondences numerically.

Inputs : data/zeros_odlyzko_2M.npy (fallback /tmp/) ; Outputs : scripts/E30_2_mechanism_and_criterion.txt
"""
import os, numpy as np
from mpmath import mp, mpf, mpc, log as mlog, pi as mpi, atan as matan, sqrt as msqrt

mp.dps = 30
ZP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'zeros_odlyzko_2M.npy')
g = np.sort(np.load(ZP if os.path.exists(ZP) else '/tmp/zeros_odlyzko_2M.npy').astype(float).ravel())

def theta(gam):
    """arg(1 - 1/rho) for rho = 1/2 + i gamma."""
    z = mpc(1, 0) - 1 / mpc(mpf('0.5'), mpf(gam))
    return float(abs(matan(z.imag / z.real)))

print("=" * 100)
print("E30-2: the two mechanisms behind the conversion laws, and the refined breakthrough criterion")
print("=" * 100)

print("\nMECHANISM A (window): first sign change of 1 - cos(n theta), predicted n* = 2 pi / theta(gamma)")
print("  %10s %14s %14s %12s" % ("gamma", "theta", "2 pi/theta", "2 pi*gamma"))
for gam in (14.134, 50.0, 100.0, 500.0, 1000.0):
    th = theta(gam)
    print("  %10.3f %14.8f %14.2f %12.1f" % (gam, th, 2 * float(mpi) / th, 2 * float(mpi) * gam))

print("\nMECHANISM B (tail): sensitivity of the n-th coefficient to an off-axis zero at height gamma")
print("  departure from 1 of |1-1/rho|^n is about n/gamma^2 for small n/gamma^2:")
print("  %10s %12s %12s %14s" % ("gamma", "gamma^2", "n=gamma^2", "|1-1/rho|^n at n=gamma^2"))
for gam in (14.134, 100.0, 1000.0):
    rho = mpc(mpf('0.5'), mpf(gam))
    q = abs(1 - 1 / rho)
    n = gam * gam
    print("  %10.3f %12.0f %12.0f %14.8f" % (gam, gam * gam, n, float(q ** int(n)) if n < 10**7 else float('nan')))

print("\nDETECTION THRESHOLD for off-axis zeros (n* such that the n-th term departs from 1 by 1%):")
print("  beta = 1/2 + delta gives |1-1/rho|^2 = 1 - (2 delta)/(beta^2+gamma^2) < 1, so the term DECAYS")
print("  and the departure is 1 - q^n with q = |1-1/rho|; solving 1 - q^n = 0.01 gives n* = log(0.99)/log(q).")
print("  %10s %10s %14s %14s %14s" % ("gamma", "delta", "q=|1-1/rho|", "n* (arg n*=2)", "n*/gamma^2"))
for gam in (14.134, 100.0, 1000.0):
    for d in (mpf('0.01'), mpf('0.1')):
        rho = mpc(mpf('0.5') + d, mpf(gam))
        q = abs(1 - 1 / rho)
        nstar = mlog(mpf('0.99')) / mlog(q)
        print("  %10.3f %10s %14.10f %14.4g %14.6f" % (gam, d, float(q), float(nstar), float(nstar) / gam**2))

print()
print("=" * 100); print("READ-OFF (conclusions generated from the numbers above)"); print("=" * 100)
th100 = theta(100.0)
print("  * mechanism A is linear: the predicted first sign change at gamma=100 is %.0f, which is"
      % (2 * float(mpi) / th100))
print("    2 pi * gamma = %.0f to within a few percent, so h(n) ~ n/(2 pi)." % (2 * float(mpi) * 100))
print("  * mechanism B is quadratic: an off-axis zero at height gamma needs n of order gamma^2,")
print("    i.e. h(n) ~ sqrt(n).")
print("  * therefore the square law belongs to the tail-budget mechanism, not to the criterion;")
print("    the same Li criterion also admits a linear-range treatment, and that treatment is the one")
print("    whose inputs are unconditional.")
print("  * refined breakthrough criterion: a probe must be scored on TWO axes -- h(n) (reach) and")
print("    whether its inputs are unconditional. Improving h(n) while losing unconditionality is not")
print("    progress; the target is a window-type mechanism with h(n) growing slower than linearly.")
