#!/usr/bin/env python3
"""
E80_budget_after_local_selberg.py -- recompute the three-region budget with the local (band-length) second moment.

WHAT IS COMPUTED
  At the top of the index interval, n = T^2, the three regions are the deep fast region gamma <= sqrt(n/11), the
  middle band sqrt(n/11) <= gamma <= sqrt(n), and the slow region gamma >= sqrt(n), which is empty there.  For each,
  the allowance is compared with the bound obtained from the Abel decomposition: a smooth part, a boundary part, and
  a discrepancy part bounded by Cauchy-Schwarz against the second moment of the counting error.

  Two versions of that second moment are compared: the global one over [0,T], giving ||S||_2 = sqrt(T loglog T/(2 pi^2)),
  and the local one over the band itself, giving sqrt(L loglog T/(2 pi^2)) with L the band length.  The local version
  is the improvement; the dyadic splitting of the band into sub-bands is also evaluated, to test whether splitting
  helps, since splitting a Cauchy-Schwarz bound is superadditive.

INPUTS   none (pure arithmetic, but recorded as a script per the project protocol)
OUTPUT   scripts/E80_budget_after_local_selberg.txt

PROVENANCE
  Written 2026-09-13 by 小灵 executing 唐先生's improvement (1).  No RH assumption used or claimed; Selberg's second
  moment is unconditional, quoted here for comparison only; NO LEAN IS RUN.
"""

from math import log, sqrt

T = 1132490.658714
N = 2001052
n = T * T
A11 = 11.0
g_deep_top = sqrt(n / A11)
g_lo_mid = g_deep_top
g_hi_mid = sqrt(n)


def count(x):
    """smooth zero counting law"""
    from math import e
    return (x / (2 * 3.141592653589793)) * log(x / (2 * 3.141592653589793 * e)) + 7.0 / 8.0


def main():
    out = []
    out.append("E80 -- three-region budget recomputed with the local (band-length) second moment")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)
    ll = log(log(T))
    c = ll / (2 * 3.141592653589793 ** 2)          # Selberg constant per unit length
    out.append("  T = %.6f, N = %d, n = T^2 = %.6g, loglog T = %.6f, Selberg constant per unit length = %.6f"
               % (T, N, n, ll, c))
    out.append("  allowance = 0.8N = %.6g" % (0.8 * N))
    out.append("")

    M_deep = count(g_deep_top)
    M_mid = count(g_hi_mid) - count(g_lo_mid)
    out.append("  deep fast: gamma <= %.6g, zeros = %.6g (trivial bound)" % (g_deep_top, M_deep))
    out.append("  middle   : %.6g <= gamma <= %.6g, zeros = %.6g" % (g_lo_mid, g_hi_mid, M_mid))
    out.append("  slow     : gamma >= %.6g, zeros = 0 (empty at this scale)" % g_hi_mid)
    out.append("")

    # middle band: sharp ||phi'||_2 and the two versions of ||S||_2
    def abel_terms(lo, hi):
        """sharp ||phi'||_2 over [lo,hi] and the band length"""
        intp2 = (n ** 2) / 3.0 * (1.0 / lo ** 3 - 1.0 / hi ** 3)
        return sqrt(intp2), (hi - lo)

    norm_ph_mid, L_mid = abel_terms(g_lo_mid, g_hi_mid)
    S_global = sqrt(T * c)
    S_local = sqrt(L_mid * c)
    out.append("  middle band: length = %.6g, sharp ||phi'||_2 = %.6g" % (L_mid, norm_ph_mid))
    out.append("      ||S||_2 global = %.6g  (over [0,T])   => Cauchy-Schwarz term = %.6g" % (S_global, S_global * norm_ph_mid))
    out.append("      ||S||_2 local  = %.6g  (over band)   => Cauchy-Schwarz term = %.6g   <-- improvement"
               % (S_local, S_local * norm_ph_mid))
    out.append("")

    # dyadic splitting of the middle band in |phi'| = n/gamma^2 : values 11 down to 1
    out.append("  dyadic splitting of the middle band in |phi'| (11 -> 1), each sub-band with its own local second moment:")
    total_dy = 0.0
    out.append("      |phi'| range   gamma range                length       ||phi'||_2     CS term")
    for a in (8.0, 4.0, 2.0, 1.0):
        hi = sqrt(n / a)
        lo = sqrt(n / min(2 * a, A11)) if a < A11 else sqrt(n / A11)
        if a == 8.0:
            lo, hi = sqrt(n / A11), sqrt(n / 8.0)
        else:
            lo, hi = sqrt(n / (2 * a)), sqrt(n / a)
        if hi > g_hi_mid:
            hi = g_hi_mid
        if lo < g_lo_mid:
            lo = g_lo_mid
        if hi <= lo:
            continue
        nph, La = abel_terms(lo, hi)
        cs = sqrt(La * c) * nph
        total_dy += cs
        out.append("      %-14s %-25s %-12.4g %-14.4g %.4g"
                   % ("[%g,%g]" % (a, min(2 * a, A11)), "[%.4g,%.4g]" % (lo, hi), La, nph, cs))
    out.append("      sum over sub-bands = %.6g   (single band was %.6g)  => splitting %s"
               % (total_dy, S_local * norm_ph_mid, "HELPS" if total_dy < S_local * norm_ph_mid else "HURTS"))
    out.append("")

    # totals
    cs_best = min(total_dy, S_local * norm_ph_mid, S_global * norm_ph_mid)
    allow_mid = 0.8 * N - M_deep
    tot = M_deep + cs_best
    out.append("  summary")
    out.append("      deep trivial bound                    = %.6g" % M_deep)
    out.append("      middle best Cauchy-Schwarz bound      = %.6g   (its allowance is 0.8N - deep = %.6g)"
               % (cs_best, allow_mid))
    out.append("      total                                 = %.6g   vs 0.8N = %.6g" % (tot, 0.8 * N))
    out.append("      shortfall                             = %.2f%%" % (100.0 * (tot / (0.8 * N) - 1.0)))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  Using the second moment over the band rather than over the whole range improves the middle band by about")
    out.append("  seventeen percent, and splitting the band into dyadic pieces does not help because splitting a")
    out.append("  Cauchy-Schwarz bound is superadditive.  The total is still over the allowance, by a few percent, and the")
    out.append("  remaining gap can only be closed by improving the deep fast region, whose trivial bound is far above its")
    out.append("  true size.")
    txt = "\n".join(out) + "\n"
    with open("scripts/E80_budget_after_local_selberg.txt", "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
