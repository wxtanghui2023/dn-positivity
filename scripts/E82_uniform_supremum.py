#!/usr/bin/env python3
"""
E82_uniform_supremum.py -- write the dyadic + local-Selberg bound as an explicit function of n and take the
supremum over the whole index interval.

THE STRUCTURE
  Substituting gamma = sqrt(n) * u makes everything scale: a sub-band u in [u1,u2] has length sqrt(n)(u2-u1) in
  gamma, the phase derivative is 1/u^2 so its L2 norm is n^{1/4} sqrt(INT u^{-4} du), and the Cauchy-Schwarz term is
  therefore sqrt(n) times a coefficient that depends only on the partition of u and on Selberg's constant per unit
  length.  The middle band's bound is thus A * sqrt(n) with A a pure number, the deep fast region is bounded by the
  zero count N(sqrt(n/11)) which increases with n, and the slow region decreases and is small.  Hence the total bound
  is increasing in n and its supremum over the interval is attained at the top, n = T^2.  This script verifies the
  coefficients and prints the monotonicity table, all analytically, with no simulation.

INPUTS   none (arithmetic, recorded as a script per protocol)
OUTPUT   scripts/E82_uniform_supremum.txt

PROVENANCE
  Written 2026-09-13 by 小灵 executing 唐先生's E82 specification.  No RH assumption; Selberg's second moment is
  unconditional and is used only through its constant per unit length; NO LEAN IS RUN.
"""

from math import e, log, pi, sqrt

T = 1132490.658714
N = 2001052
X = T * T
C = log(log(T)) / (2 * pi ** 2)
SUPS = 0.110 * log(T) + 0.290 * log(log(T)) + 2.290
A11 = 11.0


def count(x):
    return (x / (2 * pi)) * log(x / (2 * pi * e)) + 7.0 / 8.0


def cos_coeff(u1, u2):
    """n-independent coefficient of the Cauchy-Schwarz term for a sub-band [u1,u2] in the u variable"""
    du = u2 - u1
    intp2 = (1.0 / 3.0) * (1.0 / u1 ** 3 - 1.0 / u2 ** 3)
    return sqrt(du * C) * sqrt(intp2)


def main():
    out = []
    out.append("E82 -- the dyadic + local-Selberg bound as an explicit function of n, and its supremum")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)
    out.append("  T = %.6f, N = %d, C = Selberg per unit length = %.6f, sup|S| bound = %.4f" % (T, N, C, SUPS))

    # the u-partition: |phi'| = 1/u^2 runs from 11 down to 1, so u from 1/sqrt(11) to 1
    edges_u = [1.0 / sqrt(A11), 1.0 / sqrt(8.0), 1.0 / sqrt(4.0), 1.0 / sqrt(2.0), 1.0]
    out.append("  u-partition (|phi'| = 1/u^2 from 11 to 1, dyadic):")
    tot_coef = 0.0
    out.append("      u-range                 |phi'| range    length coeff    ||phi'|| coeff   CS coeff")
    for i in range(len(edges_u) - 1):
        u1, u2 = edges_u[i], edges_u[i + 1]
        cc = cos_coeff(u1, u2)
        tot_coef += cc
        out.append("      [%.5f,%.5f]   [%.2f,%.2f]     %-15.5f %-15.5f %.5f"
                   % (u1, u2, 1.0 / u2 ** 2, 1.0 / u1 ** 2, u2 - u1, sqrt((1.0 / 3.0) * (1 / u1 ** 3 - 1 / u2 ** 3)), cc))
    out.append("      TOTAL coefficient A = %.5f      (check: bound at n=T^2 = A sqrt(n) = %.6g, vs E80 value 974554)"
               % (tot_coef, tot_coef * sqrt(X)))
    out.append("      number of dyadic bands = %d (a constant, since |phi'| spans only 11 to 1)"
               % (len(edges_u) - 1))
    out.append("")

    # monotonicity table
    out.append("      n/X        deep          middle        slow          total        0.8N          shortfall")
    prev = None
    mono = True
    for frac in (0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00):
        n = frac * X
        lam = sqrt(n)
        deep = count(sqrt(n / A11))
        mid = tot_coef * lam + 5 * 2 * SUPS         # five regions each with a pair of boundary terms
        # slow region [lambda, T]: Abel terms
        if lam < T:
            L = T - lam
            intp2 = (n * n / 3.0) * (1.0 / lam ** 3 - 1.0 / T ** 3)
            cs = sqrt(L * C) * sqrt(intp2)
            rho_T = log(T / (2 * pi)) / (2 * pi)
            slow = 3.0 * rho_T * T * T / n + 2 * SUPS + cs
        else:
            slow = 0.0
        tot = deep + mid + slow
        if prev is not None and tot < prev - 1e-6:
            mono = False
        prev = tot
        out.append("      %-10.4f %-13.6g %-13.6g %-13.6g %-13.6g %-13.6g %+.2f%%"
                   % (frac, deep, mid, slow, tot, 0.8 * N, 100.0 * (tot / (0.8 * N) - 1.0)))
    out.append("")
    out.append("      monotone increasing in n? %s   => supremum at n = T^2" % ("YES" if mono else "NO"))
    out.append("      margin at the top = 0.8N - total(T^2) = %.6g" % (0.8 * N - prev))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  The middle band's bound is A sqrt(n) with A a pure number, so it grows like the square root, while the")
    out.append("  deep region's trivial bound grows like the zero count, which is faster.  The total therefore increases,")
    out.append("  and the supremum is at the top of the interval, which is where the margin is the smallest.  The margin")
    out.append("  printed at the top is the hard budget within which the local-Selberg constant may be worse than")
    out.append("  Selberg's.")
    txt = "\n".join(out) + "\n"
    with open("scripts/E82_uniform_supremum.txt", "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
