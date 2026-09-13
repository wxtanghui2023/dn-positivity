#!/usr/bin/env python3
"""
E45_nearcue_p_floor_fine.py -- exploration point E45, step 14: does the p-floor survive a FINER grid?

WHY THIS IS THE DECISIVE EXPERIMENT
  Steps 12-13 established, over the complete space of marked configurations, that on the coarse grid
  Q = 2N the exact-ramp condition forces the simple fraction p above the frontier's 0.6818287:
  p >= (10+sqrt2)/16 = 0.713388348 at N = 4 and p >= (11+sqrt3)/18 = 0.707336156 at N = 6, both robust to
  enlarging the family to all mixed-mark configurations.  That is a structural obstruction -- on those
  grids exactness and ceiling-witnessing are mutually exclusive.  But the frontier's own law has
  p = 0.6818 < our floors, so it cannot live on the coarse grid: its positions must have larger
  denominators.  The question that decides whether our exact-ramp route can ever produce a
  ceiling-comparable law is therefore whether the floor drops below 0.6818 when the position grid is
  refined.  This script refines it for N = 4: positions on the 16-grid instead of the 8-grid.

THE FIELD (this is the technical step)
  With positions x = N*m/Q and Q = 16, every cos(2 pi r / 16) = cos(pi r / 8) lies in
      K = Q(zeta_16)^+ = Q(u),  u = sqrt(2 + sqrt(2)),  u^4 = 4 u^2 - 2,
  a totally real quartic field (minimal polynomial x^4 - 4x^2 + 2, Eisenstein at 2, hence irreducible).
  Basis {1, u, u^2, u^3}; powers reduce by u^4 = 4u^2 - 2, u^5 = 4u^3 - 2u, u^6 = 14u^2 - 8.
  Cosines: cos(pi/8) = u/2, cos(pi/4) = (u^2-2)/2, cos(3pi/8) = (u^3-3u)/2, and their sign variants,
  using sqrt(2) = u^2 - 2 and sqrt(2 - sqrt(2)) = u^3 - 3u.
  Weights live in the same field, so "sum_c w_c |F_c(j)|^2 = j" with rational right side is equivalent to
  FOUR rational equations per j (the coefficient of 1 must equal j; the others must vanish) -- the same
  exactness criterion as before, one dimension higher.

RELATION TO THE COARSE GRID
  The 8-grid configurations embed into the 16-grid (even indices), so the 16-grid family contains the coarse
  one and its floor can only be lower.  The coarse floor is 0.713388348; the frontier's value is 0.6818287.

INPUTS   none (exact rational arithmetic in the quartic field; one linear program per grid size)
OUTPUT   scripts/E45_nearcue_p_floor_fine.txt

CONCLUSIONS (digit-driven)
  The minimal simple fraction on the refined grid, compared with 0.6818287 and with the coarse floor.

PROVENANCE
  Written 2026-09-13 by 小灵, approved by 唐先生 (11:56 "继续细网格实验").
  Sources: docs/E45-ceiling-law-construction.md sections 20-21; arXiv:2608.13637v2 section 7.2.
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import itertools
import os
import sys
from fractions import Fraction as F

import numpy as np
from scipy.optimize import linprog

FRONTIER_P0 = 0.6818287
COARSE_FLOOR = 0.713388348

U0 = (2 + 2 ** 0.5) ** 0.5                 # the positive root u
EMB = (1.0, U0, U0 ** 2, U0 ** 3)          # real embedding of the basis {1, u, u^2, u^3}


# ---------------------------------------------------------------- quartic field arithmetic
def fadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def fsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def fmul(a, b):
    """multiply in Q[u]/(u^4 - 4u^2 + 2) using exact rationals:
    u^4 = 4u^2 - 2, u^5 = 4u^3 - 2u, u^6 = 14u^2 - 8"""
    c = [F(0)] * 7
    for i in range(4):
        if a[i] == 0:
            continue
        for k in range(4):
            c[i + k] += a[i] * b[k]
    out = [F(0)] * 4
    out[0] = c[0] - 2 * c[4] - 8 * c[6]
    out[1] = c[1] - 2 * c[5]
    out[2] = c[2] + 4 * c[4] + 14 * c[6]
    out[3] = c[3] + 4 * c[5]
    return tuple(out)


def fscale(a, s):
    return tuple(x * s for x in a)


def fvalue(a):
    return sum(x * e for x, e in zip(a, EMB))


ONE = (F(1), F(0), F(0), F(0))


def cos_table(Q):
    """cos(2 pi r / Q) as an element of K = Q(zeta_16)^+, for Q = 16"""
    assert Q == 16
    half_u = (F(0), F(1, 2), F(0), F(0))                  # cos(pi/8)
    root2h = (F(-1), F(0), F(1, 2), F(0))                  # cos(pi/4) = (u^2-2)/2
    v_half = (F(0), F(-3, 2), F(0), F(1, 2))               # cos(3pi/8) = (u^3-3u)/2
    zero = (F(0), F(0), F(0), F(0))
    neg = lambda a: fscale(a, F(-1))
    tbl = {
        0: ONE, 1: half_u, 2: root2h, 3: v_half, 4: zero,
        5: neg(v_half), 6: neg(root2h), 7: neg(half_u), 8: neg(ONE),
        9: neg(half_u), 10: neg(root2h), 11: neg(v_half), 12: zero,
        13: v_half, 14: root2h, 15: half_u,
    }
    return tbl


def all_marked(N, Q):
    """every multiset of marks in {1,2} at distinct grid positions with total N"""
    fam = []
    for two in range(0, N // 2 + 1):
        ones = N - 2 * two
        for pos2 in itertools.combinations(range(Q), two):
            rest = [p for p in range(Q) if p not in pos2]
            for pos1 in itertools.combinations(rest, ones):
                fam.append((pos1 + pos2, (1,) * ones + (2,) * two))
    return fam


def main():
    N = 4
    Q = 16
    COS = cos_table(Q)
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 14 -- the p-floor on a REFINED grid: N = 4, Q = 16 (coarse was Q = 8)")
    w("field K = Q(zeta_16)^+ = Q[u]/(u^4-4u^2+2) ; weights in K ; ramp becomes 4 rational equations per j")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    fam = all_marked(N, Q)
    M = len(fam)
    w("family: ALL marked configurations with marks in {1,2} summing to %d on the %d-grid = %d"
      % (N, Q, M), flush=True)
    n1 = np.zeros(M)
    VAL = np.zeros((M, N, 4))          # exact coefficients of |F_c(j)|^2 for j = 1..N-1
    for ci, (pos, marks) in enumerate(fam):
        n1[ci] = sum(1 for m in marks if m == 1)
        for j in range(1, N):
            acc = (F(0), F(0), F(0), F(0))
            for k1 in range(len(pos)):
                for k2 in range(len(pos)):
                    idx = (j * (pos[k1] - pos[k2])) % Q
                    acc = fadd(acc, fscale(COS[idx], F(marks[k1] * marks[k2])))
            VAL[ci, j] = acc
            if j == 1 and ci < 3:
                w("   spot check: config %s -> |F(1)|^2 = %s (embeds to %.12f)"
                  % (str(list(pos)), str(tuple(str(x) for x in acc)), fvalue(acc)), flush=True)

    # ---- linear program: minimise p = sum_c (n1_c/N) * value(w_c) over the field
    #      built SPARSE: a dense inequality matrix would be about 420 MB
    from scipy.sparse import coo_matrix, vstack as spvstack
    nv = 4 * M
    rows_i = []; cols_i = []; vals_i = []
    rhs = []
    ridx = 0
    for j in range(1, N):
        for comp in range(4):
            for ci in range(M):
                v = VAL[ci, j][comp]
                if v != 0:
                    rows_i.append(ridx); cols_i.append(4 * ci + comp); vals_i.append(float(v))
            rhs.append(F(j) if comp == 0 else F(0))
            ridx += 1
    for comp in range(4):
        for ci in range(M):
            if ONE[comp] != 0:
                rows_i.append(ridx); cols_i.append(4 * ci + comp); vals_i.append(float(ONE[comp]))
        rhs.append(F(1) if comp == 0 else F(0))
        ridx += 1
    Aeq = coo_matrix((vals_i, (rows_i, cols_i)), shape=(ridx, nv)).tocsr()
    beq = np.array([float(x) for x in rhs])
    # nonnegativity: the real value of each weight must be >= 0
    ii = []; jj = []; vv = []
    for ci in range(M):
        for comp in range(4):
            if EMB[comp] != 0.0:
                ii.append(ci); jj.append(4 * ci + comp); vv.append(-EMB[comp])
    Aub = coo_matrix((vv, (ii, jj)), shape=(M, nv)).tocsr()
    bub = np.zeros(M)
    c = np.zeros(4 * M)
    for ci in range(M):
        for comp in range(4):
            c[4 * ci + comp] = n1[ci] / N * EMB[comp]
    w("", flush=True)
    w("solving LP: %d variables, %d equations, %d nonnegativity rows" % (nv, Aeq.shape[0], M), flush=True)
    r = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq,
                bounds=[(None, None)] * nv, method="highs")
    if not r.success:
        w("   LP failed: %s" % r.message, flush=True)
    else:
        pmin = r.fun
        w("", flush=True)
        w("   MINIMAL simple fraction p on the refined grid (N=4, Q=16) = %.9f" % pmin, flush=True)
        w("   comparison: coarse grid floor = %.9f ; frontier's constant = %.7f" % (COARSE_FLOOR, FRONTIER_P0),
          flush=True)
        w("   verdict: %s" % ("BELOW the frontier -> the obstruction DISSOLVES on the refined grid"
                              if pmin < FRONTIER_P0 else
                              "still ABOVE the frontier -> the obstruction PERSISTS"), flush=True)
        x = r.x
        sup = [ci for ci in range(M) if max(abs(x[4 * ci + k]) for k in range(4)) > 1e-9]
        w("   optimal law uses %d configurations" % len(sup), flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  A floor below the frontier's 0.6818287 on the refined grid means the coarse-grid obstruction was a")
    w("  resolution effect: with enough position resolution an exact-ramp law can have a small simple")
    w("  fraction and hence be a ceiling-comparable law.  A floor that stays above it means the obstruction")
    w("  is not about resolution, and the exact-ramp route cannot produce such a law at this grid size.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_p_floor_fine.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
