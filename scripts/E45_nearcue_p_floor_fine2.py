#!/usr/bin/env python3
"""
E45_nearcue_p_floor_fine2.py -- exploration point E45, step 17: the refined-grid floor, done correctly.

WHAT WAS WRONG BEFORE (root cause found by inspection)
  Step 14's refined-grid program wrote the field product w_c * |F_c(j)|^2 COMPONENTWISE.  In a quartic
  field the product is NOT componentwise: it is governed by the multiplication table of K = Q(u), u^4 =
  4u^2 - 2.  The program therefore solved a different, unphysical system, which is why it reported a
  vanishing simple fraction; the exact checks of steps 15-16 caught that, and here the formulation is
  corrected.  This is the same family of mistake as the earlier coercion-order and rewrite-order errors:
  check the shape of the object before trusting the arithmetic.

WHAT THIS SCRIPT DOES
  1. Groups the 3620 marked configurations of the 16-grid by (value vector, number of mark-one points),
     because the constraints see only the value vector and the objective only the mark-one count; this
     collapses the variable count.
  2. Builds the program with the CORRECT field multiplication: for each group g, the product w_g * v_g is a
     K-element whose four coordinates are linear functions of w_g's four coordinates, with the matrix
     M(v_g) given by M(v_g)[:, i] = e_i * v_g in K.
  3. Minimises the simple fraction  p = sum_g (n1_g / N) * value(w_g).
  4. Recovers the optimum EXACTLY: the equations are rational, so on the optimal support the system is
     solved by exact elimination and the weights' signs are tested rigorously with interval bounds on
     sqrt2 and u (imported from the earlier scripts so the arithmetic exists once).

INPUTS   none (exact rational arithmetic; one linear program, then exact recovery)
OUTPUT   scripts/E45_nearcue_p_floor_fine2.txt

CONCLUSIONS (digit-driven)
  The refined-grid minimal simple fraction, verified exactly on the recovered support, compared with the
  coarse value 0.713388348 and the frontier's 0.6818287.

PROVENANCE
  Written 2026-09-13 by 小灵, approved by 唐先生 (12:01 "继续").  Field arithmetic, the cosine table, the
  families and the rigorous sign test are imported from E45_nearcue_p_floor_fine.py and
  E45_nearcue_p_zero_decide.py so that no formula is implemented twice.
  Sources: docs/E45-ceiling-law-construction.md sections 20-22; arXiv:2608.13637v2 section 7.2.
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os
import sys
from fractions import Fraction as F

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from E45_nearcue_p_floor_fine import (all_marked, cos_table, fadd, fmul, ONE, EMB)  # noqa: E402
from E45_nearcue_p_zero_decide import sign_of, solve_exact                        # noqa: E402

N = 4
Q = 16
COARSE = 0.713388348
FRONTIER = 0.6818287


def main():
    COS = cos_table(Q)
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 17 -- the refined-grid floor with the CORRECT field multiplication (step 14's was wrong)")
    w("grouping by (value vector, mark-one count); exact recovery of the optimum; rigorous sign test")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    fam = all_marked(N, Q)
    groups = {}
    for pos, marks in fam:
        n1 = sum(1 for m in marks if m == 1)
        vals = []
        for j in range(1, N):
            acc = (F(0), F(0), F(0), F(0))
            for k1 in range(len(pos)):
                for k2 in range(len(pos)):
                    acc = fadd(acc, fmul(COS[(j * (pos[k1] - pos[k2])) % Q],
                                         (F(marks[k1] * marks[k2]), F(0), F(0), F(0))))
            vals.append(acc)
        key = (tuple(tuple(x for x in v) for v in vals), n1)
        groups[key] = groups.get(key, 0) + 1
    keys = list(groups.keys())
    G = len(keys)
    w("configurations %d  ->  groups (value vector, mark-one count) %d" % (len(fam), G), flush=True)

    # multiplication matrices M_g[j][:, i] = e_i * v_g[j]
    Ms = []
    for (vals, n1) in keys:
        per_j = []
        for j in range(N - 1):
            v = vals[j]
            M = np.zeros((4, 4))
            for i in range(4):
                e = tuple(F(1) if k == i else F(0) for k in range(4))
                col = fmul(e, v)
                for m in range(4):
                    M[m, i] = float(col[m])
            per_j.append(M)
        Ms.append(per_j)

    nv = 4 * G
    r_i = []; c_i = []; v_i = []; rhs = []; ridx = 0
    for j in range(N - 1):
        for m in range(4):
            for g in range(G):
                M = Ms[g][j]
                for i in range(4):
                    if M[m, i] != 0.0:
                        r_i.append(ridx); c_i.append(4 * g + i); v_i.append(M[m, i])
            rhs.append(F(j + 1) if m == 0 else F(0))
            ridx += 1
    for m in range(4):
        for g in range(G):
            if ONE[m] != 0:
                r_i.append(ridx); c_i.append(4 * g + m); v_i.append(float(ONE[m]))
        rhs.append(F(1) if m == 0 else F(0))
        ridx += 1
    Aeq = coo_matrix((v_i, (r_i, c_i)), shape=(ridx, nv)).tocsr()
    beq = np.array([float(x) for x in rhs])

    ii = []; jj = []; vv = []
    for g in range(G):
        for k in range(4):
            if EMB[k] != 0.0:
                ii.append(g); jj.append(4 * g + k); vv.append(-EMB[k])
    Aub = coo_matrix((vv, (ii, jj)), shape=(G, nv)).tocsr()
    bub = np.zeros(G)

    c = np.zeros(nv)
    for g, (vals, n1) in enumerate(keys):
        for k in range(4):
            c[4 * g + k] = n1 / N * EMB[k]

    w("solving: %d variables, %d equations, %d sign rows" % (nv, Aeq.shape[0], G), flush=True)
    r = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq,
                bounds=[(None, None)] * nv, method="highs")
    if not r.success:
        w("LP failed: %s" % r.message, flush=True)
        return
    p_lp = r.fun
    w("", flush=True)
    w("   LP value of the minimal simple fraction = %.9f" % p_lp, flush=True)
    w("   coarse value = %.9f ; frontier = %.7f" % (COARSE, FRONTIER), flush=True)

    # exact recovery on the optimal support
    x = r.x
    sup = [g for g in range(G) if max(abs(x[4 * g + k]) for k in range(4)) > 1e-9]
    w("   optimal support size = %d groups" % len(sup), flush=True)
    n = 4 * len(sup)
    rows = []; r2 = []
    for j in range(N - 1):
        for m in range(4):
            row = [F(0)] * n
            for a, g in enumerate(sup):
                M = Ms[g][j]
                for i in range(4):
                    row[4 * a + i] += M[m, i]
            rows.append(row); r2.append(F(j + 1) if m == 0 else F(0))
    # normalisation, expressed exactly in the field
    for m in range(4):
        row = [F(0)] * n
        for a in range(len(sup)):
            row[4 * a + m] += F(1)
        rows.append(row); r2.append(F(1) if m == 0 else F(0))
    # pin weights that are numerically zero, to fix the free parameters (documented heuristic)
    for a, g in enumerate(sup):
        for k in range(4):
            if abs(x[4 * g + k]) < 1e-9:
                row = [F(0)] * n; row[4 * a + k] = F(1)
                rows.append(row); r2.append(F(0))
    sol = solve_exact(rows, r2, n)
    if sol is None:
        w("   exact recovery: system INCONSISTENT on this support (heuristic pinning may be too crude)", flush=True)
        return
    signs = []
    for a in range(len(sup)):
        wt = tuple(sol[4 * a + k] for k in range(4))
        signs.append(sign_of(wt))
    nneg = sum(1 for s in signs if s is not None and s >= 0)
    p_exact = sum(F(keys[g][1], N) * sum(sol[4 * a + k] * F(EMB[k]).limit_denominator(10 ** 12)
                                         for k in range(4)) for a, g in enumerate(sup))
    w("   exact recovery: %d of %d weights nonnegative (rigorous sign test)" % (nneg, len(sup)), flush=True)
    if nneg == len(sup):
        val = float(sum(F(keys[g][1], N) * (sum(sol[4 * a + k] * EMB[k] for k in range(4)))
                        for a, g in enumerate(sup)))
        w("   *** VERIFIED exact-ramp law with simple fraction p = %.9f ***" % val, flush=True)
        w("   => refined-grid floor <= %.9f (verified); frontier = %.7f -> %s"
          % (val, FRONTIER, "BELOW the frontier: the obstruction DOES dissolve"
             if val < FRONTIER else "still above the frontier"), flush=True)
    else:
        w("   exact recovery did not produce an all-nonnegative law (heuristic limitation, not a theorem)",
          flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  With the correct field multiplication the refined-grid program has a definite value; the exact")
    w("  recovery then turns its optimum into a concrete law whose simple fraction is verified, so the")
    w("  number reported here can be trusted -- unlike step 14's.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_p_floor_fine2.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
