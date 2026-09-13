#!/usr/bin/env python3
"""
E45_nearcue_p_floor_mixed.py -- exploration point E45, step 13: does the p-floor survive a FULLER family?

WHY THIS STEP EXISTS (a correction of the family, not of the computation)
  Step 12 reported a floor on the simple fraction of exact-ramp laws: p >= 0.7134 at grid size four and
  p >= 0.7073 at grid size six, both above the frontier's 0.6818287, and drew the structural conclusion
  that exactness and ceiling-witnessing are incompatible on these grids.  But step 12's family contained
  only two shapes of configuration: all marks one, or all marks two.  Configurations MIXING the two mark
  kinds -- some points simple and on-line, some in off-line pairs -- are equally admissible and are far more
  numerous, and they are exactly what lowers the simple fraction.  The floor found in step 12 may therefore
  be an artifact of the restricted family rather than a property of exactness.  This step re-runs the same
  complete-family optimisation over ALL marked configurations with the marks summing to the grid size.

THE FAMILY (all partitions of N into parts 1 and 2, placed at distinct grid positions)
  * N ones              : C(Q, N)
  * one 2 and N-2 ones  : Q * C(Q-1, N-2)
  * two 2s and N-4 ones : C(Q,2) * C(Q-2, N-4)
  * ... etc.  Every such configuration has sum of marks N, so the theorem's normalisation is respected.

THE PROGRAM
  minimise  p = sum_c w_c * (number of mark-1 points in c) / N
  subject to the exact ramp equations on (u_c, t_c), w_c = u_c + t_c sqrt(D) >= 0, sum u = 1, sum t = 0.
  The objective is the weight itself (not its rational part alone), which step 12 learned the hard way.

INPUTS   none (exact construction; programs solved in floating point and reported with the frontier value)
OUTPUT   scripts/E45_nearcue_p_floor_mixed.txt

PROVENANCE
  Written 2026-09-13 by 小灵 for the E45 continuation, approved by 唐先生 (11:53 "继续").
  Sources: docs/E45-ceiling-law-construction.md section 20; arXiv:2608.13637v2 section 7.2.
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import itertools
import os
from fractions import Fraction as F

import numpy as np
from scipy.optimize import linprog

DQ = {8: 2, 12: 3}
COS = {}
COS[8] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
          4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))}
COS[12] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(1, 2), F(0)), 3: (F(0), F(0)),
           4: (F(-1, 2), F(0)), 5: (F(0), F(-1, 2)), 6: (F(-1), F(0)), 7: (F(0), F(-1, 2)),
           8: (F(-1, 2), F(0)), 9: (F(0), F(0)), 10: (F(1, 2), F(0)), 11: (F(0), F(1, 2))}

FRONTIER_P0 = 0.6818287


def all_marked(N, Q):
    """every multiset of marks in {1,2} on distinct grid positions with total N"""
    fam = []
    for two in range(0, N // 2 + 1):
        ones = N - 2 * two
        for pos2 in itertools.combinations(range(Q), two):
            for pos1 in itertools.combinations([p for p in range(Q) if p not in pos2], ones):
                pos = pos1 + pos2
                marks = (1,) * ones + (2,) * two
                fam.append((pos, marks))
    return fam


def main():
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 13 -- the p-floor re-examined on the FULL family of MIXED-mark configurations")
    w("step 12 used only all-ones and all-twos configurations; mixed ones are admissible and more numerous")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    for N in (4, 6):
        Q = 2 * N; D = DQ[Q]
        fam = all_marked(N, Q)
        M = len(fam)
        w("", flush=True)
        w("N = %d (Q = %d, field Q(sqrt%d)) : family of ALL marked configurations = %d"
          % (N, Q, D, M), flush=True)
        n1 = np.zeros(M)                      # number of mark-1 points per configuration
        A = np.zeros((M, N + 1)); B = np.zeros((M, N + 1))
        for ci, (pos, marks) in enumerate(fam):
            n1[ci] = sum(1 for m in marks if m == 1)
            for j in range(1, N + 1):
                a = F(0); b = F(0)
                for k1 in range(len(pos)):
                    for k2 in range(len(pos)):
                        ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
                        mm = marks[k1] * marks[k2]
                        a += ca * mm; b += cb * mm
                A[ci, j] = float(a); B[ci, j] = float(b)
        nv = 2 * M
        nrow = 2 * (N - 1) + 2
        Aeq = np.zeros((nrow, nv)); beq = np.zeros(nrow)
        for j in range(1, N):
            Aeq[2 * (j - 1), :M] = A[:, j]
            Aeq[2 * (j - 1), M:] = D * B[:, j]
            Aeq[2 * (j - 1) + 1, :M] = B[:, j]
            Aeq[2 * (j - 1) + 1, M:] = A[:, j]
            beq[2 * (j - 1)] = j
            beq[2 * (j - 1) + 1] = 0.0
        Aeq[2 * (N - 1), :M] = 1.0
        Aeq[2 * (N - 1) + 1, M:] = 1.0
        beq[2 * (N - 1)] = 1.0
        beq[2 * (N - 1) + 1] = 0.0
        Aub = np.zeros((M, nv)); bub = np.zeros(M)
        for k in range(M):
            Aub[k, k] = -1.0
            Aub[k, M + k] = -np.sqrt(D)
        # objective: p = sum_c w_c * n1_c / N  (the WEIGHT, including its sqrt part)
        c = np.zeros(nv)
        for k in range(M):
            c[k] += n1[k] / N
            c[M + k] += n1[k] / N * np.sqrt(D)
        r = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq,
                    bounds=[(None, None)] * nv, method="highs")
        if not r.success:
            w("   LP failed: %s" % r.message, flush=True)
            continue
        pmin = r.fun
        w("   MINIMAL simple fraction p over the full mixed family = %.9f" % pmin, flush=True)
        w("   frontier's recorded constant = %.7f   =>  %s"
          % (FRONTIER_P0, "BELOW (compatible!)" if pmin < FRONTIER_P0 else "ABOVE (obstruction stands)"),
          flush=True)
        x = r.x
        sup = [k for k in range(M) if abs(x[k]) + abs(x[M + k]) > 1e-9]
        kinds = {}
        for k in sup:
            pos, marks = fam[k]
            kinds[len(marks) - sum(1 for m in marks if m == 2)] = \
                kinds.get(len(marks) - sum(1 for m in marks if m == 2), 0) + 1
        w("   optimal law: %d configurations (mark-1 counts: %s)"
          % (len(sup), sorted(kinds.items())), flush=True)
        w("   step 12 comparison: its floor was 0.713388 (N=4) / 0.707336 (N=6) on the restricted family",
          flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  If the mixed family lowers the minimal fraction below the frontier's 0.6818287, then step 12's")
    w("  floor was a family artifact, the obstruction dissolves, and an exact-ramp law with a")
    w("  ceiling-comparable simple fraction exists on the SAME coarse grid -- the strongest possible")
    w("  reconciliation of the numeric half with the ceiling's purpose.  If the floor persists, the")
    w("  obstruction is real for these grids.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_p_floor_mixed.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
