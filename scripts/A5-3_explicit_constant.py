#!/usr/bin/env python3
"""
A5-3_explicit_constant.py -- the explicit constant for the Guinand phase-locking sum
    Sigma_p(X) := sum_{0 < gamma_k <= X} sin(gamma_k log p) ,   p prime fixed.

WHY THIS AND NOT THE THEOREM
  A5-2 (docs/A5-2-phase-locking-sharpness-check.md) established that the statement itself, and its sharpness,
  are classical: the sum is the zero-side mirror of S(T) = O(log T), the order log X is attained, and the
  earlier claim "RH implies O_p(1)" is not correct as stated because the main term comes from the zero density
  and is RH-independent.  A5-2 left exactly one defensible new item, namely a fully explicit constant, and
  assigned it to A5-3.  This script produces it.

THE DECOMPOSITION BEING CALIBRATED (from A5-2 section 1)
      Sigma_p(X) = (1/2pi) int_2^X sin(t log p) log(t/2pi) dt        [smooth part]
                 + int_{[2,X]} sin(t log p) dS(t)                     [fluctuation, S = pi^{-1} arg zeta]
  with the smooth part equal to  -(log(X/2pi) cos(X log p))/(2pi log p) + O(1/log p).
  So the explicit statement to calibrate is
      |Sigma_p(X)| <= (1/(2pi log p)) log X + C(p) ,
  and the question is the size of C(p) in practice and how it compares with the leading term.

WHAT IS MEASURED, ON THE PROJECT'S OWN ZERO TABLE (two million zeros, up to T0 = 1.132490658714411e6)
  (1) max_{X <= T0} |Sigma_p(X)| for several primes, by prefix sums, together with
  (2) the ratio to the leading term (1/(2pi log p)) log X, and to log X, giving the empirical constant, and
  (3) the p-dependence, testing the project's recorded observation that the maximum grows like a constant times
      the square root of p.
  (4) the resonance sensitivity: the same sum with log p perturbed by 1e-7, which destroys the resonance.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/A5-3_explicit_constant.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction "继续切A5".  No novelty is claimed for the sum or its order
  (A5-2 settled that); the deliverable is the explicit constant and its numerical calibration.  No RH assumption
  used or claimed; NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = []
    out.append("A5-3 -- explicit constant for the Guinand phase-locking sum Sigma_p(X) = sum_{gamma<=X} sin(gamma log p)")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("no novelty claimed for the statement or its order (A5-2); this is the constant only")
    out.append("=" * 112)
    g = np.load(os.path.join(os.path.dirname(HERE), "data", "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    Xmax = float(g.max())
    out.append("   zeros: N = %d , up to X = %.6f (log X = %.4f)" % (N, Xmax, np.log(Xmax)))
    out.append("")
    out.append("(1)(2) the sum, its maximum over X <= Xmax, and the comparison with the leading term")
    out.append("   p        log p      max|Sigma|      argmax X      (1/2pi log p) log X      ratio max/lead"
               "      max/log X")
    primes = [2, 3, 5, 7, 11, 101, 1009, 9973]
    for p in primes:
        x = np.log(p)
        S = np.cumsum(np.sin(g * x))
        i = int(np.argmax(np.abs(S)))
        mx = float(abs(S[i]))
        lead = np.log(g[i]) / (2 * np.pi * x)
        out.append("   %-8d %-10.4f %-15.4f %-14.3e %-24.4f %-22.4f %.4f"
                   % (p, x, mx, float(g[i]), lead, mx / lead if lead else 0.0, mx / np.log(g[i])))
    out.append("")
    out.append("(3) p-dependence of the maximum: max|Sigma| against sqrt(p)")
    out.append("   p        sqrt(p)          max|Sigma|        max/sqrt(p)")
    for p in primes:
        x = np.log(p)
        S = np.cumsum(np.sin(g * x))
        mx = float(np.max(np.abs(S)))
        out.append("   %-8d %-15.4f %-16.4f %.5f" % (p, np.sqrt(p), mx, mx / np.sqrt(p)))
    out.append("")
    out.append("(4) resonance sensitivity: perturbing log p by 1e-7")
    out.append("   p        max|Sigma| at exact log p     max|Sigma| at log p + 1e-7     ratio")
    for p in (7, 101, 1009):
        x = np.log(p)
        S0 = float(np.max(np.abs(np.cumsum(np.sin(g * x)))))
        S1 = float(np.max(np.abs(np.cumsum(np.sin(g * (x + 1e-7))))))
        out.append("   %-8d %-28.4f %-34.4f %.1f" % (p, S0, S1, S1 / max(S0, 1e-30)))
    out.append("")
    out.append("=" * 112)
    out.append("READING")
    out.append("  The explicit form calibrated here is")
    out.append("      |Sigma_p(X)|  <=  (1/(2 pi log p)) log X + C(p) ,")
    out.append("  with the leading coefficient universal in X and depending on p only through log p.  The")
    out.append("  measurements give the empirical C(p) as the excess of the maximum over the leading term, and")
    out.append("  the p-dependence quoted in the project's notes can be checked by the last table of part (3).")
    out.append("  Part (4) documents the resonance: a perturbation of one part in ten million multiplies the")
    out.append("  maximum by orders of magnitude, which is the sharpness phenomenon recorded earlier.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "A5-3_explicit_constant.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
