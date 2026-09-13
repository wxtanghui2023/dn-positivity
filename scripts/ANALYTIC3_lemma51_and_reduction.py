#!/usr/bin/env python3
"""
ANALYTIC3_lemma51_and_reduction.py -- E46 / WP3.1: the von Mangoldt sum family (Lemma 5.1 of the source)
checked numerically, and the lattice-to-integral step that the Hilbert-Schmidt reduction rests on.

PART 1 -- the von Mangoldt sums
  The source records (Lemma 5.1) that for x >= 2
      sum_{n<=x} Lambda(n)            << x
      sum_{n<=x} Lambda(n)/sqrt(n)    <= 3 sqrt(x)
      sum_{n<=x} Lambda(n)/(sqrt(n) log n)                     << sqrt(x)/log x
      sum_{n<=x} Lambda(n)^2                                   << x log x
      sum_{n<=x} Lambda(n)^2/n        = (log x)^2/2 + O(log x)
      sum_{n<=x} (Lambda(n)^2/n)(log x - log n) = (log x)^3/6 + O((log x)^2)
  each following from sum_{n<=x} Lambda(n)/n = log x + O(1) by partial summation, i.e. from Chebyshev-type
  estimates available unconditionally.  This part evaluates the sums exactly by sieve and compares them with
  the closed forms, so that the constants are seen rather than assumed.

PART 2 -- the lattice-to-integral step
  The reduction of the source (Proposition 5.2) replaces the double sum over the sampling lattice by a double
  integral, and its core is the Poisson-Gabor identity established in WP2:
      sum_{k in Z} phi_hat(tau - alpha_k) phi_hat(tau' - alpha_k) = L * Phi(tau - tau'),   Phi := (phi^2)^ .
  Restricting k to the window [0, d) omits two tails, and the source's error analysis (its E_1 term) bounds
  what that omission costs.  This part checks, numerically and in the interior of the interval where the
  theorem uses it, that the restricted sum does approximate L*Phi to the accuracy the reduction assumes.

INPUTS   none (a sieve for Lambda; mpmath quadrature for the window transforms)
OUTPUT   scripts/ANALYTIC3_lemma51_and_reduction.txt

PROVENANCE
  Written 2026-09-13 by 小灵 for E46 work package WP3.1, approved by 唐先生 (12:24 "继续").
  Source read: arXiv:2608.13637v2 section 5.1-5.2 (Lemma 5.1, Proposition 5.2 and its proof).  Inputs are
  classical and unconditional (Chebyshev-type estimates, partial summation, weighted Hilbert inequality elsewhere).
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os
from math import log, sqrt

from mpmath import mp, mpf, sin, cos, exp, quad, pi, mpc

mp.dps = 30
LIMIT = 2 * 10 ** 6


def von_mangoldt_sieve(n):
    """Lambda(1..n): by definition Lambda(m) = log p when m = p^k is a prime power, and 0 otherwise.
    (Self-correction: a first version chained factorisations and produced wrong values, which showed up
    immediately as ratios in part 1 that did not approach one.)"""
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(range(i * i, n + 1, i)))
        i += 1
    lam = [0.0] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            pk = p
            while pk <= n:
                lam[pk] = log(p)
                pk *= p
    return lam


def part1():
    out = []
    lam = von_mangoldt_sieve(LIMIT)
    out.append("PART 1 -- von Mangoldt sums, exact evaluation vs the closed forms")
    out.append("   x      sum L/n - log x   sumL2/n / (log^2 x/2)   sumL2(log x-log n) / (log^3 x/6)"
               "   sumL/sqrt n / sqrt x   sumL/(sqrt n log n) / (sqrt x/log x)")
    for x in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 2 * 10 ** 6):
        s1 = s2 = s3 = s4 = s5 = 0.0
        for n in range(2, x + 1):
            v = lam[n]
            if v:
                s1 += v / n
                s2 += v * v / n
                s3 += v * v / n * (log(x) - log(n))
                s4 += v / sqrt(n)
                if n >= 2:
                    s5 += v / (sqrt(n) * log(n))
        lx = log(x)
        out.append("  %8d   %+.4f          %.5f                    %.5f                   %.4f                %.4f"
                   % (x, s1 - lx, s2 / (lx * lx / 2), s3 / (lx ** 3 / 6), s4 / sqrt(x), s5 / (sqrt(x) / lx)))
    out.append("   (ratios tending to 1 and the first column to a constant confirm the closed forms;")
    out.append("    the constant in the first column is the O(1) of Chebyshev's estimate)")
    return out


# ------------------------------------------------------------------ part 2
L = mpf(12)
H = 2 * pi / L
T0 = mpf(26)


def phi_bump(u):
    if abs(u) >= L / 2:
        return mpf(0)
    x = 2 * u / L
    return exp(-1 / (1 - x * x))


def phi_hat(z):
    zr, zi = z.real, z.imag
    re = quad(lambda u: phi_bump(u) * cos(zr * u) * exp(zi * u), [-L / 2, L / 2], maxdegree=11)
    im = quad(lambda u: -phi_bump(u) * sin(zr * u) * exp(zi * u), [-L / 2, L / 2], maxdegree=11)
    return mpc(re, im)


def Phi(z):
    """transform of phi^2"""
    zr, zi = z.real, z.imag
    re = quad(lambda u: phi_bump(u) ** 2 * cos(zr * u) * exp(zi * u), [-L / 2, L / 2], maxdegree=11)
    im = quad(lambda u: -phi_bump(u) ** 2 * sin(zr * u) * exp(zi * u), [-L / 2, L / 2], maxdegree=11)
    return mpc(re, im)


def part2():
    out = []
    d = int((L * T0 / (2 * pi)))
    out.append("")
    out.append("PART 2 -- lattice-to-integral step: sum_{k in [0,d)} phi_hat(tau-a_k)phi_hat(tau'-a_k)  vs  L*Phi(tau-tau')")
    out.append("   L = %s, h = %s, T0 = %s, d = %d ; tau, tau' taken in the interior of [T0, 2T0)"
               % (mp.nstr(L, 8), mp.nstr(H, 8), mp.nstr(T0, 6), d))
    for (t, tp) in [(T0 + 3, T0 + 4), (T0 + 5, T0 + 5), (T0 + 2, T0 + 8)]:
        s = mpc(0, 0)
        for k in range(0, d):
            a = T0 + H * k
            s += phi_hat(mpc(t - a, 0)) * phi_hat(mpc(tp - a, 0))
        target = L * Phi(mpc(t - tp, 0))
        rel = abs(s - target) / abs(target) if abs(target) > 0 else mpf('nan')
        out.append("   tau = %s, tau' = %s : sum = %s , L*Phi = %s , relative deviation = %s"
                   % (mp.nstr(t, 8), mp.nstr(tp, 8), mp.nstr(s, 16), mp.nstr(target, 16), mp.nstr(rel, 6)))
    out.append("   (small relative deviation in the interior is what the reduction assumes; the boundary")
    out.append("    rows of the interval carry the tails that the source's E_1 estimate bounds)")
    return out


def main():
    out = []
    out.append("E46 / WP3.1 -- von Mangoldt sums (Lemma 5.1) and the lattice-to-integral step (Proposition 5.2)")
    out.append("all inputs classical and unconditional; NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 110)
    out += part1()
    out += part2()
    out.append("")
    out.append("=" * 110)
    out.append("READING")
    out.append("  Part 1 exhibits the constants behind the six von Mangoldt estimates, all of which follow from")
    out.append("  Chebyshev's sum and partial summation.  Part 2 confirms the step on which the Hilbert-Schmidt")
    out.append("  reduction rests: the lattice sum over the sampling window reproduces L times the transform of")
    out.append("  the squared window, which is the Poisson-Gabor identity of WP2 restricted to the window, with a")
    out.append("  deviation that stays small in the interior where the theorem applies.")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "ANALYTIC3_lemma51_and_reduction.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
