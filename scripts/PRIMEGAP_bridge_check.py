#!/usr/bin/env python3
"""
PRIMEGAP_bridge_check.py -- checking the two proposed bridges between the finite-off-line premise and the
prime-gap conjectures (Oppermann / Andrica), after 唐先生's analysis of 2026-09-13.

WHAT IS CHECKED, IN THREE PARTS

(1) The modulus identity and, crucially, its TWO sides.  For a zero rho = beta + i gamma,
        |1 - 1/rho|^2 = 1 + (1 - 2 beta)/(beta^2 + gamma^2) ,
    so |1-1/rho| < 1 exactly when beta > 1/2.  The functional equation pairs rho with 1 - conj(rho), hence
    ANY off-line zero is accompanied by one with beta < 1/2, whose modulus EXCEEDS one.  This part verifies
    the identity and the pairing, and measures the reciprocal relation |q'| = 1/|q| between partners.

(2) The consequence for the Li tail, which is the part of the analysis that needs correcting: the partner with
    beta < 1/2 contributes Re[1 - q^n], whose magnitude GROWS like |q|^n.  So the Li sequence is not
    asymptotically blind to off-line zeros; it develops negative values at large n.  This part exhibits the
    growth on a model pair and locates the order of n at which the negative excursion first exceeds a
    smooth main term of the classical size.

(3) The vanishing question on prime Mellin points, which is where the proposed Andrica bridge would have to
    bite.  A nonzero exponential polynomial with finitely many modes has a zero set of bounded density, while
    the primes have density growing like e^u/u in the Mellin variable u = log x.  Hence a nonzero off-line
    profile can vanish at only finitely many primes, so "vanishes at all primes" forces it to vanish
    identically.  This part counts zeros of a model profile against the prime count to exhibit the density
    comparison.

INPUTS   none (mpmath / numpy); no data files
OUTPUT   scripts/PRIMEGAP_bridge_check.txt

PROVENANCE
  Written 2026-09-13 by 小灵 in response to 唐先生's analysis of the Oppermann/Andrica-to-RH bridges.
  Two corrections are recorded in the companion document: the finite-off-line premise is NOT established
  (what is established is a verified height), and the functional-equation pairing makes the Li tail
  sensitive rather than blind.  No RH assumption is used or claimed; NO LEAN IS RUN (compute directive).
"""

import os

from mpmath import mp, mpf, sqrt as msqrt, cos, sin, exp, log, pi, mpc
import numpy as np

mp.dps = 30


def part1():
    out = []
    out.append("PART 1 -- the modulus identity and the functional-equation pairing")
    out.append("   |1-1/rho|^2 = 1 + (1-2beta)/(beta^2+gamma^2) ; partner of rho is 1-conj(rho)")
    out.append("   beta     gamma        |q|^2 (formula)      |q|^2 (direct)      |q|      partner |q|    product")
    for (b, g) in ((mpf(1) / 2, mpf('14.134725')), (mpf('0.6'), mpf('100')),
                   (mpf('0.55'), mpf('1000')), (mpf('0.4'), mpf('100')), (mpf('0.45'), mpf('1000'))):
        rho = mpc(b, g)
        q = 1 - 1 / rho
        f = 1 + (1 - 2 * b) / (b ** 2 + g ** 2)
        rho2 = 1 - rho.conjugate()
        q2 = 1 - 1 / rho2
        out.append("   %-8s %-12s %-19s %-19s %-9s %-11s %s"
                   % (mp.nstr(b, 6), mp.nstr(g, 8), mp.nstr(f, 12), mp.nstr(abs(q) ** 2, 12),
                      mp.nstr(abs(q), 9), mp.nstr(abs(q2), 9), mp.nstr(abs(q) * abs(q2), 12)))
    out.append("   => the identity holds; beta > 1/2 gives |q| < 1 and beta < 1/2 gives |q| > 1; the partner has")
    out.append("      modulus exactly reciprocal, so an off-line zero always brings a growing mode with it.")
    return out


def part2():
    out = []
    out.append("")
    out.append("PART 2 -- the Li tail is NOT asymptotically blind: growth of the partner's contribution")
    out.append("   contribution of one off-line pair to Re lambda_n : Re[1-q^n] + Re[1-q2^n]")
    out.append("   Self-correction: the first model used a near-line zero (beta = 0.6, gamma = 100), whose"
               " growth rate")
    out.append("   is only about 1e-5 per step, so the divergence is invisible below n = 1e5 even though it is"
               " certain;")
    out.append("   a second model with a distant zero makes the effect visible, and the running minimum is"
               " reported.")
    for (b, g) in ((mpf('0.2'), mpf(5)), (mpf('0.6'), mpf(100))):
        rho = mpc(b, g)
        q = 1 - 1 / rho
        q2 = 1 - 1 / (1 - rho.conjugate())
        rate = abs(q2)
        out.append("")
        out.append("   model pair: beta = %s, gamma = %s   =>  |q| = %s , |q2| = %s  (growth rate %s per step)"
                   % (mp.nstr(b, 4), mp.nstr(g, 6), mp.nstr(abs(q), 10), mp.nstr(abs(q2), 10),
                      mp.nstr(rate, 12)))
        out.append("      n          contribution            running min over n'<=n    n/2 log n (smooth size)")
        run_min = mpf(0)
        for n in (1, 5, 10, 50, 100, 500, 1000, 5000, 20000):
            v = (1 - q ** n).real + (1 - q2 ** n).real
            if v < run_min:
                run_min = v
            main = mpf(n) / 2 * log(n) if n > 1 else mpf(0)
            out.append("      %-10s %-23s %-25s %s"
                       % (n, mp.nstr(v, 10), mp.nstr(run_min, 10), mp.nstr(main, 8)))
    out.append("   => the running minimum decreases without bound, so the off-line modes cannot be absorbed into")
    out.append("      an o(1) correction: the Li sequence does see them.  What is large is the ONSET index, and it")
    out.append("      is enormous when the zero sits close to the line, which is the classical observation that a")
    out.append("      failure of the hypothesis would be hard -- not impossible -- to see numerically.")
    return out


def part3():
    out = []
    out.append("")
    out.append("PART 3 -- could an off-line profile vanish at all prime Mellin points?  (density comparison)")
    out.append("   model profile F(u) = sum_j a_j exp(delta_j u) cos(gamma_j u + phi_j), zeros counted by sign change")
    np.random.seed(20260913)
    modes = [(0.02, 3.7, 0.4), (0.01, 9.1, 2.2)]
    def F(u):
        s = 0.0
        for (d, gm, ph) in modes:
            s += np.exp(d * u) * np.cos(gm * u + ph)
        return s
    # primes up to e^U
    def primes_upto(n):
        sieve = np.ones(n + 1, dtype=bool); sieve[:2] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                sieve[i * i:: i] = False
        return np.nonzero(sieve)[0]
    out.append("      U        zeros of F in [0,U]     primes <= e^U      ratio primes/zeros")
    prev = 0
    for U in (5, 10, 15, 20):
        u = np.linspace(0, U, 200001)
        vals = F(u)
        zc = int(np.sum(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0))
        npr = len(primes_upto(int(np.exp(U))))
        out.append("   %-8d %-24d %-18d %s"
                   % (U, zc, npr, ("%.3f" % (npr / zc)) if zc else "inf"))
    out.append("   => the prime count overtakes the zero count and keeps accelerating: for a FIXED nonzero")
    out.append("      profile the number of primes at which it can vanish is finite.  So a bridge of the form")
    out.append("      'off-line profile vanishes on the primes' would indeed force the profile to vanish, and the")
    out.append("      entire content of the bridge therefore sits in the arithmetic statement that it vanishes.")
    return out


def main():
    out = []
    out.append("Prime-gap / finite-off-line bridge: numerical checks of the three decisive points")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 108)
    out += part1()
    out += part2()
    out += part3()
    out.append("")
    out.append("=" * 108)
    out.append("READING")
    out.append("  Part 1 confirms the modulus identity and shows the pairing is fatal to the 'eventually invisible'")
    out.append("  picture: every off-line zero drags in a mode of modulus exceeding one.  Part 2 exhibits the")
    out.append("  resulting unbounded negative excursion of the Li tail.  Part 3 shows the vanishing route is not")
    out.append("  blocked by anything analytic: a nonzero profile vanishes at only finitely many primes, so the")
    out.append("  bridge would work if the arithmetic side could produce that vanishing -- and that is exactly")
    out.append("  where no argument is currently available.")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "PRIMEGAP_bridge_check.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
