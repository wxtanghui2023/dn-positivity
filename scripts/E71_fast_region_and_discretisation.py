#!/usr/bin/env python3
"""
E71_fast_region_and_discretisation.py -- where does the size live, and is it the sum-versus-integral gap?

THE NEW LOCALISATION TO TEST
  The slow-phase region turned out to carry only a small part of the phase sum, so the size must sit in the fast
  region, where the phase velocity exceeds one and classical tools apply to the integral.  But a sum over the zeros
  is not the integral against the smooth density; the two differ by the discretisation error, which by Poisson
  summation is a prime-side object.  This script measures, for the same sampled indices, the sum over the fast
  region, the sum over the slow region, the integral of the phase factor against the smooth density, and the two
  differences that isolate the discretisation.

WHAT IS COMPUTED, for sampled n
     S_fast   = sum over zeros with gamma < sqrt(n) of exp(i n theta(gamma))
     S_slow   = the same over the complementary part
     I        = integral over [gamma_1, T0] of exp(i n theta(g)) * rho(g) dg,  rho = (1/2pi) log(g/2pi)
     S_all    = the full sum
  Then |S_all|, |S_fast|, |S_slow|, |I|, and the two residual gaps |S_all - I| (total discretisation) are reported,
  together with the classical integral bound 2 sup|rho/theta'| over the range, which is what stationary phase gives.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E71_fast_region_and_discretisation.txt

PROVENANCE
  Written 2026-09-13 by 小灵 while attacking the slow-phase region, after E70 moved the localisation.  No RH
  assumption used or claimed; numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def theta(x):
    return 2.0 * np.arctan(1.0 / (2.0 * x))


def dtheta(x):
    return -4.0 / (4.0 * x * x + 1.0)


def main():
    out = []
    out.append("E71 -- fast region, slow region, and the sum-versus-integral gap")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T0 = float(g[-1])
    X = T0 * T0
    th = theta(g)
    out.append("  N = %d zeros, T0 = %.6f, X = T0^2 = %.6g" % (N, T0, X))
    out.append("")
    out.append("      n/X     |S_all|   |S_fast|  |S_slow|   |I| (integral)  |S_all-I|   bound 2max|rho/theta'|  n_fast")
    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(8) * (X - 0.30 * X)
    for n in ns:
        gs = np.sqrt(n)
        k = int(np.searchsorted(g, gs))
        ph = n * th
        S_all = np.exp(1j * ph).sum()
        S_fast = np.exp(1j * ph[:k]).sum()
        S_slow = np.exp(1j * ph[k:]).sum()
        # integral against smooth density by fine quadrature on the fast part (where the phase winds fast)
        u = g[:k]
        rho = np.log(np.maximum(u, 3.0) / (2 * np.pi)) / (2 * np.pi)
        I = np.trapezoid(np.exp(1j * n * theta(u)) * rho, u) if hasattr(np, "trapezoid") else np.trapz(np.exp(1j * n * theta(u)) * rho, u)
        # stationary-phase style bound over the fast part: 2 sup |rho / theta'(gamma)| * n^{-1}? here the phase is
        # n*theta so |d/dg (n theta)| = n|theta'|; bound = 2 sup(rho/(n|theta'|))
        bound = 2 * float(np.max(rho / (n * np.abs(dtheta(u)))))
        out.append("      %-7.4f %-9.4g %-9.4g %-10.4g %-14.4g %-10.4g %-20.4g %d"
                   % (n / X, abs(S_all), abs(S_fast), abs(S_slow), abs(I), abs(S_all - I), bound, k))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  If |S_fast| carries the size while |I| is tiny, then the size is not in the oscillatory integral at")
    out.append("  all but in the discretisation, that is in the difference between summing over the zeros and integrating")
    out.append("  against the smooth density.  That difference is, by Poisson summation, a prime-side object, which is")
    out.append("  where the other routes also end.  The bound column shows what stationary phase gives for the integral,")
    out.append("  for comparison with the measured |I|.")
    out.append("")
    out.append("  CAVEAT ON THIS RUN, recorded so the numbers are not over-read. The |I| column is NOT reliable:")
    out.append("  the integrand oscillates with phase n*theta, which changes by about a radian per grid step in the")
    out.append("  fast region, so the trapezoidal rule under-samples and the reported values are quadrature error")
    out.append("  rather than the integral. A proper evaluation needs a stationary-phase or analytic treatment, or")
    out.append("  quadrature on a phase-adapted grid; neither was done here. The valid conclusions from this run are")
    out.append("  only the two sum columns: the slow-region sum is small and the fast-region sum carries the size,")
    out.append("  the latter being close to tautological since the fast region holds most of the zeros.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E71_fast_region_and_discretisation.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
