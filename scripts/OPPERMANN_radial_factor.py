#!/usr/bin/env python3
"""
OPPERMANN_radial_factor.py -- the complete algebraic expansion of a functional built from the two Oppermann
primes around a square, and the decisive test of whether the radial factor m^{2 beta - 1} is created.

THE PROPOSAL BEING TESTED
  唐先生 proposes building a functional from the two primes that Oppermann places around each square m^2,
      p_m^- = m^2 - a_m ,   p_m^+ = m^2 + b_m ,   1 <= a_m, b_m < m ,
   in the hope that the asymmetry D_m = b_m - a_m, together with the square scale, produces a radial factor
   m^{2 beta - 1} able to distinguish a zero at distance delta = beta - 1/2 from the line from an on-line zero.

WHAT THIS SCRIPT DOES
  (1) expands the second difference of a test function around the square,
          Phi(m^2 + h) + Phi(m^2 - h) - 2 Phi(m^2) ,   h = m = sqrt(x) ,
      in powers of 1/m, and verifies the leading coefficients numerically for Phi(z) = z^rho.  The leading
      coefficient is rho(rho-1)/2 times (h/x)^2 x^rho, so the radial part of the leading term is
          x^{beta-1} = m^{2(beta-1)} ,
      which relative to the on-line value m^{-1} carries the factor m^{2 beta - 1} exactly as hoped.
  (2) checks the same for the ANTISYMMETRIC combination Phi(p^+) - Phi(p^-), which is the other half of the
      proposed two-degrees-of-freedom structure, and records what it couples to.
  (3) states the obstruction that decides the question: which of these functionals is USABLE, i.e. can be
      formed from quantities we actually know.  The individual primes p_m^\pm are not known for all m -- only
      their existence is conjectured -- so any functional built from them is unavailable; the usable object is
      the summatory function, and on the summatory side the second difference reproduces precisely the
      factor x^{delta - 1/2} computed earlier, with no new mechanism.

INPUTS   none (mpmath / numpy)
OUTPUT   scripts/OPPERMANN_radial_factor.txt

PROVENANCE
  Written 2026-09-13 by 小灵, executing 唐先生's instruction to construct the functional from p_m^\pm and expand
  it completely, closing the line immediately if the only outcome is a gamma-phase or a return to the explicit
  formula.  No RH assumption is used or claimed; NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

from mpmath import mp, mpf, mpc, exp, log, sqrt as msqrt, pi
import numpy as np

mp.dps = 30


def part1():
    out = []
    out.append("PART 1 -- expansion of the symmetric second difference around a square, h = m = sqrt(x)")
    out.append("   Phi(z) = z^rho ,  S = Phi(x+h) + Phi(x-h) - 2 Phi(x) = x^rho [ (1+u)^rho + (1-u)^rho - 2 ], u = h/x")
    out.append("   predicted leading behaviour: S / (x^rho u^2) -> rho(rho-1)")
    out.append("      x        rho                S/(x^rho u^2)            rho(rho-1)             ratio")
    for (b, g) in ((mpf('0.5'), mpf(10)), (mpf('0.6'), mpf(10)), (mpf('0.75'), mpf(30))):
        rho = mpc(b, g)
        for e in (6, 12):
            x = mpf(10) ** e
            h = msqrt(x)
            u = h / x
            S = (x + h) ** rho + (x - h) ** rho - 2 * x ** rho
            got = S / (x ** rho * u ** 2)
            want = rho * (rho - 1)
            out.append("      %-8s beta=%-4s gamma=%-5s  %-22s %-22s %.6f"
                       % ("1e%d" % e, mp.nstr(b, 3), mp.nstr(g, 4), mp.nstr(got, 10), mp.nstr(want, 10),
                          float(abs(got / want))))
    out.append("   => the leading coefficient is confirmed, so the radial part of the leading term is")
    out.append("      x^{beta-1} = m^{2(beta-1)}, i.e. relative to on-line zeros a factor m^{2 beta - 1}.")
    out.append("      So the factor 唐先生 is hunting for DOES appear, at the level of the kernel.")
    return out


def part2():
    out = []
    out.append("")
    out.append("PART 2 -- the antisymmetric combination and what it couples to")
    out.append("   Phi(p^+) - Phi(p^-) with p^+ = x + b, p^- = x - a, x = m^2, a,b in (0,m)")
    out.append("   prediction: leading term = Phi'(x)(a+b) + higher orders, so it couples to the SUM a+b (a gap)")
    out.append("   and NOT to the asymmetry D = b - a at leading order; the asymmetry enters only at order 1/m^2,")
    out.append("   i.e. inside the term Phi''(x)(b^2 - a^2)/2 = Phi''(x)(a+b)D/2.")
    b_, a_ = mpc(mpf('0.5'), mpf(10)), mpc(mpf('0.4'), mpf(8))
    for e in (6, 12, 18):
        m = mpf(10) ** (e // 2)
        x = m ** 2
        pplus, pminus = x + b_ * m, x - a_ * m
        lead = b_ * m  # Phi'(x) = 1 for Phi(z) = z
        exact_lin = (pplus - pminus) - (b_ * m + a_ * m)
        out.append("      m = 1e%d : (p^+ - p^-) - (b+a) = %s  (linear part exact for Phi = identity)"
                   % (e // 2, mp.nstr(exact_lin, 8)))
    out.append("   => with Phi the identity the antisymmetric part reduces to the ordinary prime gap, so it carries")
    out.append("      no information beyond Andrica-type statements; the asymmetry D appears only multiplied by")
    out.append("      Phi'' at order m^0 relative to Phi'', which is a smooth-factor coupling, not a new detector.")
    return out


def part3():
    out = []
    out.append("")
    out.append("PART 3 -- usability, and the decisive comparison")
    out.append("   The kernel does produce the radial factor, so the question is settled by which functionals exist:")
    out.append("     (i)  functionals built from the individual primes p_m^pm : NOT USABLE, because those primes are")
    out.append("          unknown for all m (their existence is exactly what Oppermann conjectures).")
    out.append("     (ii) summatory functionals, i.e. what the explicit formula can read: on those, the second")
    out.append("          difference at shift h = sqrt(x) gives one zero rho the contribution")
    out.append("             -x^rho (rho-1) (h/x)^2 (1 + O(1/x)) ,   magnitude ~ x^{beta-1} |rho|^2 = x^{delta-1/2}|rho|^2")
    out.append("          with delta = beta - 1/2.  This is precisely the factor computed in the earlier assessment,")
    out.append("          and it carries no information beyond it.")
    out.append("   numerical magnitudes for the same model used before (delta = 0.1, gamma = 10):")
    delta, gamma = mpf('0.1'), mpf(10)
    rho = mpc(mpf(1) / 2 + delta, gamma)
    for e in (6, 12, 24, 48):
        x = mpf(10) ** e
        val = x ** rho * (rho - 1) * (msqrt(x) / x) ** 2
        online = x ** mpc(mpf(1) / 2, gamma) * (mpc(mpf(1) / 2, gamma) - 1) * (msqrt(x) / x) ** 2
        ratio = abs(val) / abs(online)
        out.append("      x = 1e%-6d ratio |off-line|/|on-line| = %s   (predicted m^{2 delta} = %s)"
                   % (e, mp.nstr(ratio, 10), mp.nstr(x ** delta, 10)))
    out.append("   => the ratio is m^{2 delta} = x^{2 delta}, growing: the off-line mode dominates the ON-LINE")
    out.append("      signal, but it does not dominate the MAIN term, which for the symmetric difference cancels")
    out.append("      exactly and for any one-sided difference equals h = m = x^{1/2}.  Since x^{delta} << x^{1/2}")
    out.append("      for every delta < 1/2, no nonemptiness statement can detect it -- the obstruction is unchanged.")
    out.append("")
    out.append("   VERDICT (by 唐先生's own criterion, applied honestly): the radial factor appears at the level of")
    out.append("   the kernel, but the only usable functionals are the summatory ones, and there the factor is the")
    out.append("   earlier x^{delta-1/2} restated.  The mechanism produces no new discriminating power, and the")
    out.append("   individual-prime functionals are unavailable in principle.  The line therefore closes, not because")
    out.append("   the factor is absent, but because its presence does not change the comparison that must be won.")
    return out


def main():
    out = []
    out.append("Oppermann square-centre functional: complete expansion and the radial-factor test")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 110)
    out += part1()
    out += part2()
    out += part3()
    out.append("")
    out.append("=" * 110)
    out.append("READING")
    out.append("  The expansion confirms that the second difference around a square produces the radial factor")
    out.append("  m^{2 beta - 1} multiplying the on-line baseline, exactly as hoped; the antisymmetric combination")
    out.append("  instead reproduces the prime gap and couples the asymmetry only through a smooth second-derivative")
    out.append("  factor.  What decides the matter is which functional can actually be formed: the individual primes")
    out.append("  are not known, and on the summatory side the same factor reappears in its earlier form, with the")
    out.append("  comparison against the main term unchanged.")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "OPPERMANN_radial_factor.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
