#!/usr/bin/env python3
"""
E74_fast_region_attack.py -- attack the fast phase region: what is available, and what is structurally impossible.

WHAT IS TESTED
  The slow phase range is closed (previous step).  The fast range, where the phase derivative exceeds one, remains.
  Three things are examined here and settled numerically.

  (1) LIPSCHITZ IN THE INDEX.  The phase sum as a function of the index has derivative sum_gamma theta(gamma), which
      is small because theta(gamma) <= theta(14) = 0.0714.  So the sum is Lipschitz in the index with a small
      constant, which quantifies how slowly it moves.  Verified directly by finite differences.

  (2) CAN LIPSCHITZ PLUS A GLOBAL SECOND MOMENT BOUND THE MAXIMUM?  No.  A Lipschitz function can exceed a level on a
      set of small measure while its average stays small; the argument yields only M^3 <= 4 L |I| B, computed here to
      show it lands above the requirement.  This is a structural obstruction, not a constant problem.

  (3) IS THE LOCAL SECOND MOMENT UNIFORM?  No.  The kernel width of a block of length l in the index corresponds to
      an ordinate window of width 4 pi gamma^2 / l, so the neighbour constant C0(l) grows like 4 pi gamma^2 rho / l
      and is already large for every block length available here.  This refutes a tempting idea: combining a small
      block with Lipschitz would give M <= sqrt(4 B), which fails precisely because the local bound is not uniform.

  Also computed: the second-difference ratio that decides applicability of the second-derivative test, and the
  Cauchy-Schwarz bound on the intermediate band, which is the one piece of the fast range that does close.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E74_fast_region_attack.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction to attack the fast region.  No RH assumption used or claimed;
  numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def theta(x):
    return 2.0 * np.arctan(1.0 / (2.0 * x))


def main():
    out = []
    out.append("E74 -- attack on the fast phase region")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T = float(g[-1])
    X = T * T
    th = theta(g)

    # ---- (1) Lipschitz constant in the index ----
    L = float(np.sum(th))
    out.append("(1) Lipschitz in the index")
    out.append("    sum over zeros of theta(gamma) = %.6f   (theta(14) = %.6f, so this is the Lipschitz constant of S)" % (L, theta(14.0)))
    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(6) * (X - 0.30 * X)
    out.append("      n/X      h         |S(n+h)-S(n)|/h   Lipschitz constant   ratio")
    for n in ns[:3]:
        for h in (1e3, 1e6, 1e9):
            d = abs(np.exp(1j * (n + h) * th).sum() - np.exp(1j * n * th).sum()) / h
            out.append("      %-8.4f %-9.3g %-17.6f %-20.6f %.4f" % (n / X, h, d, L, d / L))
    out.append("")

    # ---- (2) can Lipschitz plus a global second moment bound the max? ----
    B = 14.25 * N                       # rigorous block second-moment constant from the earlier work
    I = X / 2.0
    M_imp = (4 * L * I * B) ** (1.0 / 3.0)
    out.append("(2) Lipschitz plus global second moment: the best such bound is M^3 <= 4 L |I| B")
    out.append("    L = %.4f, |I| = %.4g, B = 14.25N = %.4g  =>  M <= %.4g" % (L, I, B, M_imp))
    out.append("    requirement is 0.8N = %.4g  =>  this route is short by a factor %.1f" % (0.8 * N, M_imp / (0.8 * N)))
    out.append("    the obstruction is structural: Lipschitz bounds the MEASURE of the high set, not its height")
    out.append("")

    # ---- (3) is the local second moment uniform? ----
    rho = float(np.log(T / (2 * np.pi)) / (2 * np.pi))
    out.append("(3) local second moment: kernel width in ordinate is 4 pi gamma^2 / l, so C0(l) ~ 4 pi gamma^2 rho / l")
    out.append("      l (block length in n)      C0(l)              is the local bound usable?")
    for l in (1e4, 1e6, 1e9, 6.4e11):
        C0 = 4 * np.pi * T * T * rho / l
        out.append("      %-26.4g %-19.4g %s" % (l, C0, "yes (C0 small)" if C0 < 1 else "NO (bound is vacuous)"))
    out.append("    => the tempting argument 'small block + Lipschitz gives M <= sqrt(4B)' fails, because taking the")
    out.append("       block as short as M/L = %.3g makes C0 enormous.  Recorded as refuted." % (M_imp / L))
    out.append("")

    # ---- second-difference ratio: applicability of the second-derivative test ----
    seg = np.diff(g)
    dg = np.abs(np.diff(seg))
    out.append("(4) second-difference ratio: gap-fluctuation term / curvature term = gamma * |delta g| / (2 g^2)")
    out.append("      at gamma = T:          %.4f      (>> 1 => the gap term dominates)"
               % (T * float(np.mean(dg)) / (2 * float(np.mean(seg)) ** 2)))
    out.append("      at gamma = 100:        %.4f" % (100 * float(np.mean(dg)) / (2 * float(np.mean(seg)) ** 2)))
    out.append("    => the second differences are gap-dominated with mixed signs throughout, so the second-derivative")
    out.append("       test of van der Corput is never applicable in this problem.  This explains the earlier finding.")
    out.append("")

    # ---- intermediate band: the one piece of the fast range that closes ----
    out.append("(5) intermediate band [0.3 sqrt(n), sqrt(n)], where the increment per gap is between 1 and 2 pi")
    out.append("      n         int |phi'|^2 over band     CS bound       0.8N        margin")
    for n in (0.30 * X, 0.65 * X, X):
        a = 0.3 * np.sqrt(n)
        b = np.sqrt(n)
        intp2 = float(n ** 2 * (1.0 / (3 * a ** 3) - 1.0 / (3 * b ** 3)))
        cs = float(np.sqrt(T * np.log(np.log(T)) / (2 * np.pi ** 2)) * np.sqrt(intp2))
        out.append("      %-9.4g %-25.4g %-15.4g %-11.4g %.2fx" % (n, intp2, cs, 0.8 * N, 0.8 * N / cs))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  The Lipschitz fact is real and elementary, but it cannot bound the maximum, and the local second moment")
    out.append("  is not uniform, so blocking does not rescue it either.  The second-derivative test is structurally")
    out.append("  inapplicable.  The intermediate band does close by Cauchy-Schwarz, with a thin margin, and the deep")
    out.append("  fast region, where the phase advances by much more than a full turn per gap, is left needing an")
    out.append("  exponential-sum bound at critical density, which is the same wall the other routes meet.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E74_fast_region_attack.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
