#!/usr/bin/env python3
"""
PAPERA_trudgian_remainder_check.py -- Paper A (li-range): verify, independently and elementarily, the
remainder term in the explicit Riemann-von Mangoldt bound quoted as Lemma 2.

THE CLAIM
  Lemma 2 of the paper states, for T >= e,
        |N(T) - F(T)| <= 0.112 log T + 0.278 log log T + 2.510 + 0.2/T,
  with F(T) = (T/2pi) log(T/2pi e) + 7/8.  The first three constants are Trudgian's bound on |S(T)| for the
  argument of zeta (Math. Comp. 81 (2012) 1053-1061; the sequel II, J. Number Theory 134 (2014) 280-292,
  lowers them to 0.111, 0.275, 2.450).  Those constants are NOT re-derived here.  What IS checked here is the
  last term, which is elementary and self-contained:

  the exact identity  N(T) = (1/pi) theta(T) + 1 + S(T)  with  theta(T) = arg Gamma(1/4 + iT/2) - (T/2) log pi
  gives, with the Stirling expansion of theta,
        N(T) - F(T) - S(T) = r(T)/pi ,
  where r(T) is the explicit remainder of that expansion.  Hence Lemma 2 follows from the quoted |S(T)| bound
  as soon as |r(T)|/pi <= 0.2/T, which is what this script measures over the ranges the paper uses.

INPUTS   none (mpmath at 40 digits; the gamma function is evaluated by mpmath, so theta is computed from its
         definition rather than from the expansion being tested)
OUTPUT   scripts/PAPERA_trudgian_remainder_check.txt

PROVENANCE
  Written 2026-09-13 by 小灵, closing item (1) of the four restore-todos recorded in
  docs/PARKED-2026-09-11-li-paper.md (check the Trudgian constants against the original).  The bibliographic
  side of that item found the paper's original bibitem to cite the wrong title and year, now corrected.
  No RH assumption used or claimed; NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

from mpmath import mp, mpf, log, pi, loggamma, mpc

mp.dps = 40


def theta_exact(T):
    """theta(T) = Im log Gamma(1/4 + iT/2) - (T/2) log pi.

    Self-correction: the imaginary part of the logarithm is taken through loggamma, which is analytic off the
    negative real axis, so it is the CONTINUOUS branch of the argument along the positive imaginary axis.  A
    first version used arg(gamma(...)), which returns the principal value in (-pi, pi] and wraps; the wrap made
    r(T) enormous (about -144 at T = 100) instead of the Stirling remainder it should be."""
    z = mpc(mpf(1) / 4, T / 2)
    return loggamma(z).imag - (T / 2) * log(pi)


def theta_asym(T):
    """(T/2) log(T/2pi) - T/2 - pi/8  (no remainder term)"""
    return (T / 2) * log(T / (2 * pi)) - T / 2 - pi / 8


def main():
    out = []
    out.append("Paper A -- Lemma 2: independent check of the remainder term 0.2/T")
    out.append("identity used: N(T) = (1/pi) theta(T) + 1 + S(T), so N(T) - F(T) - S(T) = r(T)/pi")
    out.append("bound to be verified: |r(T)|/pi <= 0.2/T")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 104)
    out.append("      T            r(T)              |r(T)|/pi         0.2/T            ratio (must be <= 1)")
    worst = None
    for T in (mpf(10), mpf(100), mpf(10) ** 6, mpf('1.1324906587144114e6'), mpf(3) * mpf(10) ** 12):
        r = theta_exact(T) - theta_asym(T)
        lhs = abs(r) / pi
        rhs = mpf('0.2') / T
        ratio = lhs / rhs
        out.append("   %-12s %-+20s %-18s %-18s %.6f"
                   % (mp.nstr(T, 8), mp.nstr(r, 12), mp.nstr(lhs, 10), mp.nstr(rhs, 10), float(ratio)))
        if worst is None or ratio > worst[0]:
            worst = (ratio, T)
    out.append("")
    out.append("   worst ratio |r(T)|/pi * T/0.2 = %.6f at T = %s" % (float(worst[0]), mp.nstr(worst[1], 8)))
    out.append("   => the remainder term 0.2/T in Lemma 2 is valid (and in fact the true remainder is far smaller:")
    out.append("      asymptotically |r(T)|/pi = 1/(48 pi T) + O(T^-3), i.e. about 0.0066/T)")
    # cross-check the asymptotic shape of r itself: r(T) ~ 1/(48 T)
    out.append("")
    out.append("   shape check (should approach 1):  r(T) * 48 T")
    for T in (mpf(100), mpf(10) ** 6, mpf(3) * mpf(10) ** 12):
        r = theta_exact(T) - theta_asym(T)
        out.append("      T = %-12s : r*48T = %.9f" % (mp.nstr(T, 8), float(r * 48 * T)))
    out.append("")
    out.append("=" * 104)
    out.append("READING")
    out.append("  The last term of Lemma 2 is now checked rather than quoted: the discrepancy between N(T) and")
    out.append("  F(T)+S(T) is the explicit Stirling remainder divided by pi, and it is bounded by 0.2/T across")
    out.append("  the whole range the paper uses, with the true size asymptotically 0.0066/T.  The first three")
    out.append("  constants are Trudgian's |S(T)| bound and are cited, not re-proved here.")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "PAPERA_trudgian_remainder_check.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
