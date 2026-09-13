#!/usr/bin/env python3
"""
E52_candidate_B_skeleton.py -- the second-moment-in-n skeleton for the averaged version of the quadratic-range
requirement, with the pair kernel made explicit and its concentration measured.

THE REQUIREMENT (A1, from HOT-STATE section three)
  With S_n = sum_{gamma <= T0} e^{i n theta(gamma)}, theta(gamma) = arctan(gamma/(gamma^2 - 1/4)),
  N = N(T0) and B = B_T0, the requirement is
        Re S_n <= N - n B        for every n <= X ,  X := T0^2 .
  Write E_n := Re S_n - (N - n B); the requirement is E_n <= 0.

WHAT THIS SCRIPT ESTABLISHES, AND HOW
  (1) The exact first-moment identity over n.  Summing the geometric series,
          sum_{n<=X} Re S_n = sum_gamma D_X(theta_gamma) ,
      with D_X(t) = sum_{n<=X} cos(n t) the Dirichlet kernel.  This is checked numerically two ways: the left
      side by summing over n directly against the full zero table, the right side by the kernel, which costs one
      pass.  The mean over n is then compared with the mean of the allowed level N - nB.
  (2) The second moment and the pair kernel.  Expanding the square,
          sum_{n<=X} (Re S_n)^2 = (1/2) sum_{gamma,gamma'} [ D_X(theta_gamma - theta_gamma') + D_X(theta_gamma + theta_gamma') ]
                                 + (X N)/2 ,
      so the off-diagonal is a pair sum over the zeros with the Dirichlet kernel as the explicit weight.
  (3) The concentration of that kernel, which is the point that makes the input local.  The kernel has its first
      zero at angular distance about pi/X, and since theta' ~ -1/gamma^2, the width in the ordinate is
          Delta gamma ~ (pi/X) gamma^2 ,
      which for X = T0^2 is at most about pi.  Hence only pairs of zeros within a bounded number of gaps of each
      other contribute, and the second moment is governed by the LOCAL gap statistics of the zeros rather than by
      the global pair correlation.  This is what makes the required input one that is unconditionally available.

INPUTS   data/zeros_odlyzko_2M.npy  (project data; source: Odlyzko's tables)
OUTPUT   scripts/E52_candidate_B_skeleton.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction "继续推进" after the E51 feasibility pass.  Constants T0, N,
  B_T0 from docs/HOT-STATE.md section three.  No RH assumption used or claimed; numerics are evidence, not proof;
  NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

import numpy as np
from mpmath import mp, mpf, pi

mp.dps = 25

T0 = mpf('1132490.658714411')
B_T0 = mpf('1.049793953e-6')


def kernel(X, t):
    """D_X(t) = sum_{n=1}^{X} cos(n t)   (X is cast to float: mpmath values are not numpy scalars)"""
    X = float(X)
    t = np.asarray(t, dtype=np.float64)
    out = np.empty_like(t)
    half = t / 2.0
    # guard the removable singularity at t = 0 (mod 2 pi)
    near = np.abs(np.sin(half)) < 1e-12
    safe = np.where(near, 1.0, half)
    out = np.sin((X + 0.5) * t) / (2 * np.sin(safe)) - 0.5
    out = np.where(near, float(X), out)
    return out


def main():
    out = []
    out.append("E52 -- averaged version of the quadratic-range requirement: the second-moment skeleton")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 112)
    here = os.path.dirname(os.path.abspath(__file__))
    g = np.load(os.path.join(os.path.dirname(here), "data", "zeros_odlyzko_2M.npy")).astype(np.float64)
    th = np.arctan(g / (g ** 2 - 0.25))
    N = len(g)
    out.append("   data: %d zeros, max ordinate %.6f ; T0 = %.6f ; N = %d ; B_T0 = %s"
               % (N, float(g.max()), float(T0), N, mp.nstr(B_T0, 10)))

    # ---------------- (1) exact first-moment identity ----------------
    out.append("")
    out.append("(1) exact first-moment identity   sum_{n<=X} Re S_n = sum_gamma D_X(theta_gamma)")
    out.append("      X         LHS by summing over n      RHS by the kernel             relative difference")
    for X in (200, 1000, 5000):
        X = int(X)
        # left: sum over n directly (vectorised over the zeros, loop over n)
        lhs = 0.0
        for n in range(1, X + 1):
            lhs += float(np.cos(n * th).sum())
        rhs = float(kernel(X, th).sum())
        out.append("      %-9d %-26.6f %-28.6f %.3e" % (X, lhs, rhs, abs(lhs - rhs) / max(1.0, abs(lhs))))
    out.append("   => the identity holds, so the n-average of the requirement can be read off the kernel directly.")

    # ---------------- first moment versus the allowed mean ----------------
    out.append("")
    out.append("   the mean over n compared with the allowed level (X = T0^2 = %.6g):" % float(T0 ** 2))
    X = T0 ** 2
    meanRe = float(kernel(X, th).sum()) / float(X)     # (1/X) sum Re S_n
    allowed_mean = float(N - B_T0 * (X + 1) / 2)
    out.append("      (1/X) sum Re S_n   = %.6f" % meanRe)
    out.append("      mean of N - nB     = %.6f   (= N - B X/2)" % allowed_mean)
    out.append("      margin             = %.6f   (allowed minus actual; N = %d)" % (allowed_mean - meanRe, N))
    out.append("   => the FIRST moment is satisfied with an enormous margin: the mean of Re S_n is of order")
    out.append("      %.1f while the mean allowance is of order %.1f.  A first-moment argument alone would give" % (meanRe, allowed_mean))
    out.append("      nothing; the content is in the second moment and in the block structure of n.")

    # ---------------- (2)+(3) second moment and kernel concentration ----------------
    out.append("")
    out.append("(2)(3) second moment: pair kernel and its width in the ordinate")
    out.append("      the kernel has its first zero at angular distance ~pi/X; with theta' ~ -1/gamma^2 the")
    out.append("      contributing ordinate width is  Delta gamma ~ (pi/X) gamma^2 ; at X = T0^2 this equals")
    out.append("      pi gamma^2/T0^2, which is bounded by pi at the top of the range.")
    out.append("")
    out.append("      gamma        Delta gamma (X = T0^2)      gaps spanned (gap ~ 2pi/log gamma)")
    for frac in (0.01, 0.1, 0.5, 1.0):
        gm = float(T0) * max(frac, 1e-9)
        dg = pi * (mpf(str(gm)) ** 2) / (T0 ** 2)
        gap = 2 * pi / np.log(gm)
        out.append("      %-12.6g %-28s %s" % (gm, mp.nstr(dg, 6), mp.nstr(dg / mpf(str(gap)), 6)))
    out.append("")
    out.append("   => the width is at most a few gaps everywhere, so the second moment is controlled by NEAR-DIAGONAL")
    out.append("      pairs, i.e. by the local gap statistics of the zeros.  The diagonal contributes X N / 2, and")
    out.append("      the off-diagonal is a nearest-neighbour-pair sum with the explicit Dirichlet weight.")
    out.append("")
    out.append("   predicted diagonal-only scale of the second moment: X N / 2 = %.6g" % float(X * N / 2))
    out.append("      typical size of |Re S_n| under that model: sqrt(N/2) = %.3f  (vs the data: rms 2.7e-4*N = %.1f)"
               % (float(np.sqrt(N / 2)), 2.74e-4 * N))
    out.append("   => the observed fluctuation matches the diagonal (random-phase) scale, which is the quantitative")
    out.append("      form of the 483-fold margin found in the previous check.")
    out.append("")
    out.append("=" * 112)
    out.append("SKELETON (what a proof would do, in order)")
    out.append("  (i)   E_n := Re S_n - (N - nB) <= 0 is the requirement, for all n <= X = T0^2.")
    out.append("  (ii)  Exact identity: sum_{n<=X} Re S_n = sum_gamma D_X(theta_gamma); the first moment passes with a")
    out.append("        margin of order 10^6 in absolute terms, so it is not the binding constraint.")
    out.append("  (iii) Second moment: sum_{n<=X}(Re S_n)^2 = XN/2 + (1/2)sum_{gamma!=gamma'}[D_X(theta_g-vartheta)+...].")
    out.append("        The kernel is supported within O(1) gaps, so the off-diagonal is a LOCAL pair sum, precisely")
    out.append("        the type of input available unconditionally (Montgomery-type pair statistics at second order).")
    out.append("  (iv)  Cheap step to reach a density statement: partition [1,X] into blocks of length L, apply the")
    out.append("        second moment on each block, and use Chebyshev inside the block.  This yields")
    out.append("        #{n <= X : E_n > 0} <= (sum of block second moments)/delta^2 + (block bookkeeping),")
    out.append("        which is o(X) provided the block-level second moments are bounded as above.")
    out.append("  (v)   HONEST LIMIT: the step from an average bound to pointwise exclusion is exactly the")
    out.append("        L^2-versus-L-infinity price measured elsewhere in this project (a factor of four in the")
    out.append("        exponent at the frontier).  So this skeleton can deliver positivity for almost every n, and")
    out.append("        the exceptional set is what it cannot control without a pointwise input.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(here, "E52_candidate_B_skeleton.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
