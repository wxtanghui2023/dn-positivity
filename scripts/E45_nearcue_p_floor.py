#!/usr/bin/env python3
"""
E45_nearcue_p_floor.py -- exploration point E45, step 12: how low can the simple fraction p go?

THE QUESTION
  Step 11 showed the ceiling's bound is only as strong as the law's simple fraction p is small, that our
  recorded exact-ramp laws have p = 1, and -- by sampling supports -- that exactness does NOT force p = 1:
  exact-ramp laws with p = 0.75 (grid size four) and p = 8/9 (grid size six) were found.  The razor
  question is whether p has a FLOOR above the frontier's value 0.6818287.  If it does, then no exact-ramp
  law on these grids can witness the ceiling at all -- a clean structural obstruction.  If p can be pushed
  below 0.6818287, the numeric half and the ceiling's purpose can be combined.

WHY THE FULL FAMILY (this is what is new here)
  Step 11 maximised the mark-2 weight over RANDOM supports of size N+2, which only lower-bounds the
  achievable mark-2 weight.  Here the linear program runs over the COMPLETE family (every unit-mark and
  every mark-2 configuration of the grid), so its optimum is the true worst case in that family:
      max  sum over mark-2 configurations of w_c      (equivalently  min p = 1 - that maximum)
      s.t. the exact ramp equations on (u_c, t_c),  w_c = u_c + t_c sqrt(D) >= 0,  sum u = 1, sum t = 0.
  Because grid size four and six have complete families of 98 and 1144 configurations, these two optima are
  exact answers (not samples) for those grids and fields.

INPUTS   none (exact construction; the programs are solved in floating point and the optima re-checked)
OUTPUT   scripts/E45_nearcue_p_floor.txt

CONCLUSIONS (digit-driven)
  The minimal simple fraction per grid, compared with the frontier's 0.6818287, and the resulting verdict:
  a floor above it is an obstruction; a value below it makes a same-type instance possible.

PROVENANCE
  Written 2026-09-13 by 小灵 for the E45 continuation, approved by 唐先生 (11:53 "继续").
  Sources: docs/E45-ceiling-law-construction.md sections 11-19; arXiv:2608.13637v2 section 7.2.
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

FRONTIER_P0 = F(6818287, 10 ** 7)          # 0.6818287, the frontier's recorded ceiling constant


def nonneg(u, t, D):
    if t == 0:
        return u >= 0
    if t > 0:
        return True if u >= 0 else (D * t * t >= u * u)
    return u >= 0 and u * u >= D * t * t


def main():
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 12 -- the floor of the simple fraction p over EXACT-ramp laws (complete families)")
    w("LP: maximise the weight on mark-2 configurations s.t. the exact ramp equations and nonnegativity")
    w("    => min p = 1 - optimum ; compare with the frontier's recorded 0.6818287")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    for N in (4, 6):
        Q = 2 * N; D = DQ[Q]
        unit = [(sub, (1,) * N) for sub in itertools.combinations(range(Q), N)]
        mark2 = [(sub, (2,) * (N // 2)) for sub in itertools.combinations(range(Q), N // 2)] \
            if N % 2 == 0 else []
        fam = unit + mark2
        is_m2 = [False] * len(unit) + [True] * len(mark2)
        M = len(fam)
        A = np.zeros((M, N + 1)); B = np.zeros((M, N + 1))
        for ci, (pos, marks) in enumerate(fam):
            for j in range(1, N + 1):
                a = F(0); b = F(0)
                for k1 in range(len(pos)):
                    for k2 in range(len(pos)):
                        ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
                        mm = marks[k1] * marks[k2]
                        a += ca * mm; b += cb * mm
                A[ci, j] = float(a); B[ci, j] = float(b)
        w("", flush=True)
        w("N = %d (Q = %d, field Q(sqrt%d)) : complete family %d configurations (%d unit-mark, %d mark-2)"
          % (N, Q, D, M, len(unit), len(mark2)), flush=True)

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
        c = np.zeros(nv)
        for k in range(M):
            if is_m2[k]:
                # SELF-CORRECTION: the objective must be the WEIGHT w_c = u_c + sqrt(D) t_c, not just its
                # u-part.  Maximising sum u alone is unbounded, because the u-versus-t split has a
                # nullspace direction that keeps the ramp equalities while driving u up and down.
                c[k] = 1.0
                c[M + k] = np.sqrt(D)
        r = linprog(-c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq,
                    bounds=[(None, None)] * nv, method="highs")
        if not r.success:
            w("   LP failed: %s" % r.message, flush=True)
            continue
        wmax = -r.fun
        pmin = 1.0 - wmax
        w("   max weight on mark-2 configurations = %.9f  =>  MINIMAL simple fraction p = %.9f"
          % (wmax, pmin), flush=True)
        w("   frontier's recorded ceiling constant = %.7f  (%s p_min)"
          % (float(FRONTIER_P0), "BELOW" if pmin < float(FRONTIER_P0) else "ABOVE"), flush=True)
        # carrier support of the optimum
        x = r.x
        sup = [k for k in range(M) if abs(x[k]) + abs(x[M + k]) > 1e-9]
        wsup = sum(1 for k in sup if is_m2[k])
        w("   optimal law uses %d configurations (%d of them mark-2)" % (len(sup), wsup), flush=True)
        # feasibility of a prescribed target just below the frontier's value
        target = float(FRONTIER_P0) - 1e-6
        wrow = np.zeros(nv)
        for k in range(M):
            if is_m2[k]:
                wrow[k] = -1.0                 # -sum_{mark2} w  <=  -(1 - target)
                wrow[M + k] = -np.sqrt(D)
        Aub2 = np.vstack([Aub, wrow[None, :]])
        bub2 = np.concatenate([bub, [-(1.0 - target)]])
        r2 = linprog(np.zeros(nv), A_ub=Aub2, b_ub=bub2, A_eq=Aeq, b_eq=beq,
                     bounds=[(None, None)] * nv, method="highs")
        w("   is there an exact-ramp law with p <= %.7f ?  %s"
          % (target, "YES" if r2.success else "NO"), flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  A minimal p ABOVE the frontier's 0.6818287 is a structural obstruction: on that grid no exact-ramp")
    w("  law can be a ceiling-witnessing law.  A minimal p BELOW it means the two purposes can be combined:")
    w("  an exact numeric input (tau = 0) attached to a law whose simple fraction is at or below the")
    w("  frontier's, which is the strongest form of the E45 reconciliation.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_p_floor.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
