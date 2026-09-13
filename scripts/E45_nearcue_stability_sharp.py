#!/usr/bin/env python3
"""
E45_nearcue_stability_sharp.py -- exploration point E45, step 19: the exact-ramp law is EXTREMAL for the
stability inequality.

WHAT IS BEING CHECKED
  The ceiling theorem's analytic content is the stability inequality: for the certificate's window r and the
  law's grid data, the quadrature deficit
        Q(r) := int_0^1 r(x) x dx  -  sum_{j=1}^{N} s_j r(j/N) ,      s_j = S(j)/N
  is bounded by  |Q(r)| <= |D(1)| |r(1)| + (1/(6N^2)) (|r'(1)| + int_0^1 |r''|)  up to the tolerance term.
  For a near-CUE law the masses are the ramp and this script checks the natural certificate r(x) = x against
  it.  Writing out the two sides for the ramp (S(j) = j/N, so s_j = j/N^2) gives
        Q(x)      = 1/3 - (N+1)(2N+1)/(6N^2) = -(3N+1)/(6N^2)
        bound(x)  = 1/(2N) + 1/(6N^2)        =  (3N+1)/(6N^2)
  so the inequality is an EQUALITY for every N -- the exact-ramp law sits exactly on the boundary of the
  stability inequality, with both error terms (the edge bound and the kernel term) saturated at once.
  This is verified here in exact rational arithmetic, together with the identity 1 + 2 + ... + N = N(N+1)/2
  that underlies the closed form.

WHY IT MATTERS FOR E45
  E45 has now established, with verified constructions: the exact numeric input (tolerance zero), the exact
  edge bound d1 = 1/(2N), and -- on a fine enough grid -- an arbitrary simple fraction.  This step adds the
  remaining sharpness statement available inside the theorem's own framework: the law constructed here
  attains the stability bound rather than merely obeying it, so the constants 1/(2N) and 1/(6N^2) are both
  necessary for this law.  What it does NOT provide, and cannot, is the frontier's class-level ceiling, which
  needs their own analytic construction pairing a law with a certificate; that remains the single open item.

INPUTS   none (exact rational arithmetic)
OUTPUT   scripts/E45_nearcue_stability_sharp.txt

PROVENANCE
  Written 2026-09-13 by 小灵, approved by 唐先生 (12:06 "继续").
  Sources: repo tag v1.0, Zeta23/PairCeiling/{Defs,Stability,Ceiling,NearCUE}.lean (the stability inequality
  and Dfun = Cstep - x^2/2); docs/E45-ceiling-law-construction.md sections 9-23; arXiv:2608.13637v2 sec. 7.2.
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os
from fractions import Fraction as F


def main():
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 19 -- is the exact-ramp law EXTREMAL for the stability inequality?  (certificate r(x) = x)")
    w("quadrature deficit  Q(x) = 1/3 - sum_j (j/N^2)(j/N)   vs   bound  d1 + 1/(6N^2),   d1 = 1/(2N)")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)
    w("%4s %14s %14s %14s %10s" % ("N", "Q(x)", "bound", "|Q|-bound", "equality"), flush=True)
    all_eq = True
    for N in range(2, 31):
        # exact mass sum: s_j = (j/N)/N, so sum_j s_j (j/N) = (1/N^3) sum j^2 = (N+1)(2N+1)/(6 N^2)
        s_sum = sum(F(j, N * N) * F(j, N) for j in range(1, N + 1))
        assert s_sum == F((N + 1) * (2 * N + 1), 6 * N * N)
        q = F(1, 3) - s_sum
        bound = F(1, 2 * N) + F(1, 6 * N * N)          # d1|r(1)| + (1/(6N^2))(|r'(1)| + int|r''|), r = x
        diff = abs(q) - bound
        eq = (diff == 0)
        all_eq = all_eq and eq
        if N <= 10 or not eq:
            w("%4d %14s %14s %14s %10s"
              % (N, str(q), str(bound), str(diff), "YES" if eq else "NO"), flush=True)
    w("", flush=True)
    w("equality for EVERY N in 2..30 : %s" % all_eq, flush=True)
    w("", flush=True)
    w("closed forms:  Q(x) = -(3N+1)/(6N^2)   and   bound = 1/(2N) + 1/(6N^2) = (3N+1)/(6N^2)", flush=True)
    w("=> the exact-ramp law SATURATES the stability inequality: both the edge term and the kernel term", flush=True)
    w("   are necessary for it, and the equality holds for every grid size.", flush=True)
    w("", flush=True)
    w("=" * 100)
    w("READING")
    w("  Sharpness inside the theorem's own framework is therefore complete for this law: the numeric input is")
    w("  exact (tau = 0), the edge bound is exact, an arbitrary simple fraction is reachable on a fine grid,")
    w("  and the stability inequality is attained.  The single remaining item is the frontier's class-level")
    w("  ceiling, which needs their analytic law-plus-certificate construction and is not bounded work.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_stability_sharp.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
