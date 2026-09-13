#!/usr/bin/env python3
"""
E45_nearcue_p_low_search.py -- exploration point E45, step 18: verified small-simple-fraction exact-ramp
laws on the refined grid, by construction rather than by optimisation.

WHY NOT THE PROGRAM'S VALUE
  Step 17 fixed the field multiplication of step 14 and re-ran the program on the grouped model (133 groups,
  532 variables), and it still reported a minimal simple fraction of zero.  That cannot be right: step 16
  decided EXHAUSTIVELY, over all 255 supports of the eight difference classes of the all-two configurations,
  that no exact nonnegative law with a vanishing fraction exists.  The program's zero is therefore a boundary
  artifact again: minimising the fraction pushes against the nonnegativity constraints, and a tolerance of
  one part in a billion lets the returned point be slightly infeasible.  Optimisation values on the boundary
  are exactly what this project's discipline says not to trust, so this step abandons them.

WHAT THIS DID INSTEAD
  Searches by construction: sample supports among the groups, solve the exact rational system with the
  correct field multiplication, test every weight's sign rigorously with interval bounds, and record the
  simple fraction of every law that passes.  Each reported value therefore comes with a concrete law that has
  been verified, not with a program's claim.  Supports are biased towards groups with few mark-one points,
  since those are what lower the fraction.

INPUTS   none (exact rational arithmetic)
OUTPUT   scripts/E45_nearcue_p_low_search.txt

CONCLUSIONS (digit-driven)
  The smallest VERIFIED simple fraction found on the refined grid, and whether it lies below the frontier's
  0.6818287.

PROVENANCE
  Written 2026-09-13 by 小灵, approved by 唐先生 (12:01 "继续").  Arithmetic, families and the rigorous sign
  test are imported from the earlier E45 scripts so no formula is implemented twice.
  Sources: docs/E45-ceiling-law-construction.md sections 20-22; arXiv:2608.13637v2 section 7.2.
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os
import random
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from E45_nearcue_p_floor_fine import all_marked, cos_table, fadd, fmul  # noqa: E402
from E45_nearcue_p_zero_decide import sign_of, solve_exact, EMB_IV     # noqa: E402

N = 4
Q = 16
COARSE = 0.713388348
FRONTIER = 0.6818287
SEED = 20260913
SIZES = (6, 8, 10)
TRIALS = 3000


def value_interval(coords):
    lo = sum(min(coords[i] * EMB_IV[i][0], coords[i] * EMB_IV[i][1]) for i in range(4))
    hi = sum(max(coords[i] * EMB_IV[i][0], coords[i] * EMB_IV[i][1]) for i in range(4))
    return lo, hi


def main():
    COS = cos_table(Q)
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 18 -- VERIFIED small-p exact-ramp laws on the refined grid (N = 4, Q = 16)")
    w("by construction and exact sign tests, not by trusting a program's boundary optimum")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    # groups: (value vector, n1) -> list of (positions, marks); weights aggregate per group
    groups = {}
    for pos, marks in all_marked(N, Q):
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
        groups.setdefault(key, []).append((pos, marks))
    keys = list(groups.keys())
    G = len(keys)
    w("groups (value vector, mark-one count): %d   [configurations %d]"
      % (G, sum(len(v) for v in groups.values())), flush=True)
    n1arr = [k[1] for k in keys]
    w("mark-one counts present: %s" % sorted(set(n1arr)), flush=True)

    rng = random.Random(SEED)
    best = None
    found = 0
    for s in SIZES:
        for trial in range(TRIALS):
            # bias: prefer groups with few mark-one points (they are what lowers p)
            pool = sorted(range(G), key=lambda g: (n1arr[g], rng.random()))
            idx = pool[:max(s * 6, 40)]
            sup = rng.sample(idx, s)
            n = 4 * s
            rows = []; r2 = []
            for j in range(1, N):
                vv = [keys[g][0][j - 1] for g in sup]
                for m in range(4):
                    row = [F(0)] * n
                    for a in range(s):
                        e = None
                        M = [fmul(tuple(F(1) if k == i else F(0) for k in range(4)), vv[a]) for i in range(4)]
                        for i in range(4):
                            row[4 * a + i] = M[i][m]
                    rows.append(row)
                    r2.append(F(j) if m == 0 else F(0))
            for m in range(4):
                row = [F(0)] * n
                if m == 0:
                    for a in range(s):
                        row[4 * a] = F(1)
                rows.append(row)
                r2.append(F(1) if m == 0 else F(0))
            sol = solve_exact(rows, r2, n)
            if sol is None or any(x is None for x in sol):
                continue
            ok = True
            for a in range(s):
                sg = sign_of(tuple(sol[4 * a + k] for k in range(4)))
                if sg is None or sg < 0:
                    ok = False
                    break
            if not ok:
                continue
            found += 1
            lo = F(0); hi = F(0)
            for a, g in enumerate(sup):
                iv = value_interval(tuple(sol[4 * a + k] for k in range(4)))
                lo += F(n1arr[g], N) * iv[0]
                hi += F(n1arr[g], N) * iv[1]
            if best is None or hi < best[0]:
                best = (hi, lo, s, sup, sol)
        if best is not None and float(best[0]) < FRONTIER:
            break
    w("", flush=True)
    w("exact verified laws found: %d" % found, flush=True)
    if best is None:
        w("   none found within the sampled supports (evidence, not proof)", flush=True)
    else:
        hi, lo, s, sup, sol = best
        w("   smallest verified simple fraction: p in [%s, %s]  =  [%.9f, %.9f]"
          % (lo, hi, float(lo), float(hi)), flush=True)
        w("   support size %d groups; mark-one counts %s" % (s, sorted(n1arr[g] for g in sup)), flush=True)
        w("   coarse value = %.9f ; frontier = %.7f" % (COARSE, FRONTIER), flush=True)
        w("   verdict: %s" % ("BELOW the frontier -> a ceiling-comparable exact-ramp law exists on this grid"
                              if float(hi) < FRONTIER else
                              "still above the frontier in the sampled supports"), flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  Every number here comes from a concrete law whose ramp identity and weight signs were checked")
    w("  exactly, so unlike the program values of steps 14 and 17 it can be trusted as it stands.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_p_low_search.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
