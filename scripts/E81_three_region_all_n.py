#!/usr/bin/env python3
"""
E81_three_region_all_n.py -- the three-region accounting over the whole index interval, with all terms included.

WHY
  The previous step closed the accounting at the single index n = T^2.  The requirement is uniform over the whole
  interval, and the slow region is empty only at the top, so the accounting must be recomputed for every n, with the
  smooth and boundary terms of the Abel decomposition included rather than omitted.

WHAT IS COMPUTED, for each n in [0.3 T^2, T^2]
  deep fast region gamma <= sqrt(n/11): bound = number of zeros (triangle inequality);
  middle band sqrt(n/11) <= gamma <= sqrt(n): dyadic split in |phi'|, each sub-band bounded by the Abel decomposition
      with the local (sub-band length) second moment of the counting error;
  slow region sqrt(n) <= gamma <= T: the Abel decomposition with the local second moment over that region;
  and the total compared with the allowance 0.8N, with the shortfall printed.

  Selberg's constant per unit length is loglog T / (2 pi^2), used unconditionally.

INPUTS   none (arithmetic, recorded as a script per protocol)
OUTPUT   scripts/E81_three_region_all_n.txt

PROVENANCE
  Written 2026-09-13 by 小灵 executing 唐先生's improvement (1) with the uniform check.  No RH assumption; Selberg's
  second moment is unconditional; NO LEAN IS RUN.
"""

from math import e, log, pi, sqrt

T = 1132490.658714
N = 2001052
X = T * T
C = log(log(T)) / (2 * pi ** 2)        # Selberg constant per unit length
SUPS = 0.110 * log(T) + 0.290 * log(log(T)) + 2.290   # explicit pointwise bound on the counting error


def count(x):
    return (x / (2 * pi)) * log(x / (2 * pi * e)) + 7.0 / 8.0


def norms(lo, hi, n):
    """sharp ||phi'||_2 over [lo,hi] with phi = n*theta, theta = 1/gamma"""
    if hi <= lo:
        return 0.0, 0.0
    intp2 = (n * n) / 3.0 * (1.0 / lo ** 3 - 1.0 / hi ** 3)
    return sqrt(intp2), (hi - lo)


def rho(u):
    return log(u / (2 * pi)) / (2 * pi)


def abel(lo, hi, n):
    """smooth + boundary + Cauchy-Schwarz with the local second moment, for the region [lo,hi]"""
    if hi <= lo:
        return 0.0
    # smooth part: |INT rho e^{i phi}| <= 2 sup |rho/phi'| + INT |(rho/phi')'| ; both estimated by the endpoint
    phip_lo = n * 1.0 / lo ** 2          # |phi'| = n*theta' ~ n/gamma^2
    phip_hi = n * 1.0 / hi ** 2
    ratio_hi = rho(hi) / max(phip_hi, 1e-300)
    smooth = 3.0 * ratio_hi
    bound = 2.0 * SUPS                   # boundary terms, one pair per region (the split boundary is shared)
    nph, L = norms(lo, hi, n)
    cs = sqrt(L * C) * nph               # Cauchy-Schwarz with the local second moment
    return smooth + bound + cs


def region_bounds(n):
    g_deep = sqrt(n / 11.0)
    g_mid = sqrt(n)
    deep = count(g_deep)                 # triangle inequality
    # middle: dyadic in |phi'| from 11 down to 1
    mid = 0.0
    edges = [11.0, 8.0, 4.0, 2.0, 1.0]
    for i in range(len(edges) - 1):
        a, b = edges[i], edges[i + 1]
        lo, hi = sqrt(n / a), sqrt(n / b)
        mid += abel(lo, hi, n)
    # slow: gamma from sqrt(n) to T
    slow = abel(g_mid, T, n) if g_mid < T else 0.0
    return deep, mid, slow


def main():
    out = []
    out.append("E81 -- three-region accounting over the whole index interval, all terms included")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)
    out.append("  T = %.6f, N = %d, allowance 0.8N = %.6g, Selberg constant per length = %.6f, sup|S| bound = %.4f"
               % (T, N, 0.8 * N, C, SUPS))
    out.append("")
    out.append("      n/X        deep        middle      slow        total       0.8N         shortfall")
    worst = (-1e9, None)
    for frac in (0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00):
        n = frac * X
        d, m, s = region_bounds(n)
        tot = d + m + s
        sh = 100.0 * (tot / (0.8 * N) - 1.0)
        if sh > worst[0]:
            worst = (sh, frac)
        out.append("      %-10.4f %-11.6g %-11.6g %-11.6g %-12.6g %-12.6g %+.2f%%"
                   % (frac, d, m, s, tot, 0.8 * N, sh))
    out.append("")
    out.append("      worst case: n/X = %.2f with shortfall %+.2f%%" % (worst[1], worst[0]))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  If every row is negative, the accounting closes uniformly over the interval with explicit terms, under")
    out.append("  the single assumption that the counting error has, over a sub-interval, a second moment proportional to")
    out.append("  its length with Selberg's constant.  If some row is positive, the worst index is identified and that is")
    out.append("  where the remaining work is.")
    txt = "\n".join(out) + "\n"
    with open("scripts/E81_three_region_all_n.txt", "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
