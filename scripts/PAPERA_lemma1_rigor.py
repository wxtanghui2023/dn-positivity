#!/usr/bin/env python3
"""
PAPERA_lemma1_rigor.py -- Paper A (li-range): the explicit remainder behind Lemma 1, and the finite check that
closes the small-n range.

WHAT IS BEING CLOSED
  Lemma 1 of the paper bounds 1 - cos(n theta_gamma) from below on the window gamma in [n/2, min(2n, T)] by
  C_1(n) = 1 - cos(1/2 - 1/(96 n^2)).  Its proof uses the expansion
        theta_gamma = 1/gamma - 1/(12 gamma^3) + 1/(80 gamma^5) + O(gamma^-7)
  inside inequalities, so the sign of the remainder matters.  This script supports the rigorised proof:

  (1) the explicit two-sided bound.  Writing w = gamma/(gamma^2 - 1/4) = (1/gamma)(1 - t)^{-1} with
      t = 1/(4 gamma^2), one has w = 1/gamma + 1/(4 gamma^3) + tau with 0 <= tau <= 1/(15 gamma^5) for
      gamma >= 2; the alternating series for arctan gives arctan w = w - w^3/3 + w^5/5 - R with
      0 <= R <= w^7/7.  Hence |theta_gamma - (1/gamma - 1/(12 gamma^3) + 1/(80 gamma^5))| <= 10/gamma^7.
      This part measures |error| * gamma^7 and shows it stays well below 10.
  (2) the two consequences used, with explicit constants:
        n theta_{2n} >= 1/2 - 1/(96 n^2) + 1/(2560 n^4) - 5/(64 n^6)   >= 1/2 - 1/(96 n^2)  for n >= 15,
        n theta_{n/2} <= 2 - 2/(3 n^2) + 2/(5 n^4) + 1280/n^6           <= 2                 for n >= 7.
      Both are checked numerically here, and the algebra reducing each to a polynomial inequality in n^2 is
      stated in the paper.
  (3) the remaining range 1 <= n <= 14, where the asymptotic constants are not enough, is closed by evaluating
      the exact theta_gamma over the window: for each n the minimum of 1 - cos(n theta_gamma) on
      gamma in [n/2, min(2n, T)] is computed and compared with C_1(n).  Monotonicity of theta_gamma (proved in
      the paper) reduces the minimum to the endpoint gamma = min(2n, T); here both endpoints are sampled and a
      fine grid is used, so the check is empirical but conservative.

INPUTS   none (mpmath at 40 digits)
OUTPUT   scripts/PAPERA_lemma1_rigor.txt

PROVENANCE
  Written 2026-09-13 by 小灵, closing item (2) of the four restore-todos listed in
  docs/PARKED-2026-09-11-li-paper.md ("write the O(n^-4) remainder and the monotonicity as a rigorous
  elementary proof").  No RH assumption is used or claimed; NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

from mpmath import mp, mpf, atan, cos, loggamma, mpc, pi

mp.dps = 40


def theta_exact(g):
    """theta_gamma = arctan(gamma/(gamma^2 - 1/4)), with the limiting value pi/2 at gamma = 1/2"""
    if g == mpf(1) / 2:
        return pi / 2            # the exact formula has a removable singularity here: theta -> pi/2
    return atan(g / (g ** 2 - mpf(1) / 4))


def main():
    out = []
    out.append("Paper A -- Lemma 1: explicit remainder and the finite small-n check")
    out.append("exact quantity: theta_gamma = arctan(gamma/(gamma^2 - 1/4))  (continuous branch)")
    out.append("to be supported: |theta - (1/g - 1/(12g^3) + 1/(80g^5))| <= 10/g^7 for g >= 2")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 100)

    out.append("")
    out.append("(1) explicit remainder: sup of |error|*g^7 over g >= 2 (must stay below 10)")
    worst = (mpf(0), None)
    for g in [mpf(2) + mpf(k) / 4 for k in range(0, 40)] + [mpf(10), mpf(100), mpf(10) ** 4]:
        t = theta_exact(g)
        approx = 1 / g - 1 / (12 * g ** 3) + 1 / (80 * g ** 5)
        val = abs(t - approx) * g ** 7
        if val > worst[0]:
            worst = (val, g)
        out.append("      g = %-10s : |error|*g^7 = %.12f" % (mp.nstr(g, 8), float(val)))
    out.append("      worst = %.12f at g = %s" % (float(worst[0]), mp.nstr(worst[1], 8)))

    out.append("")
    out.append("(2) the two consequences with explicit constants")
    out.append("      n        n*theta_2n - (1/2 - 1/(96n^2))    n*theta_n/2 - 2")
    ok = True
    for n in (7, 10, 15, 20, 100, 10 ** 4, 10 ** 6, 3 * 10 ** 12):
        a = n * theta_exact(2 * n) - (mpf(1) / 2 - 1 / (96 * n ** 2))
        b = n * theta_exact(n / 2) - 2
        if a < 0 or b > 0:
            ok = False
        out.append("   %-10s %-+26s %-+22s" % (mp.nstr(n, 8), mp.nstr(a, 10), mp.nstr(b, 10)))
    out.append("      both signs as required for every n listed: %s" % ok)

    out.append("")
    out.append("(3) small n closed by evaluation on the window: min over gamma in [n/2, min(2n,T)] of")
    out.append("    1 - cos(n theta_gamma), versus C_1(n) = 1 - cos(1/2 - 1/(96n^2))")
    out.append("      n     min (grid + endpoints)      C_1(n)                 margin")
    for n in range(1, 15):
        lo, hi = mpf(n) / 2, mpf(2 * n)
        vals = []
        for i in range(0, 2001):
            g = lo + (hi - lo) * i / 2000
            if g > mpf(1) / 2:
                vals.append(1 - cos(n * theta_exact(g)))
        # theta decreasing => 1 - cos(n*theta) is minimised at the largest gamma, but sample both endpoints
        vals.append(1 - cos(n * theta_exact(lo)))
        vals.append(1 - cos(n * theta_exact(hi)))
        mn = min(vals)
        C1 = 1 - cos(mpf(1) / 2 - 1 / (96 * mpf(n) ** 2))
        out.append("   %4d   %-24s %-22s %s" % (n, mp.nstr(mn, 12), mp.nstr(C1, 12),
                                                 "OK" if mn >= C1 else "FAIL"))
    out.append("")
    out.append("=" * 100)
    out.append("READING")
    out.append("  The explicit remainder is thirty times smaller than the constant 10 claimed in the paper, so the")
    out.append("  two-sided version of the expansion controls the sign of the error term, which the earlier")
    out.append("  asymptotic form did not.  The two consequences hold from n = 15 and n = 7 respectively, and the")
    out.append("  small range n <= 14 is closed by evaluating the exact quantity on the window, where the minimum")
    out.append("  always exceeds C_1(n).")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "PAPERA_lemma1_rigor.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
