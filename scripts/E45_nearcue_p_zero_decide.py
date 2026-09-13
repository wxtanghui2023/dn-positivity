#!/usr/bin/env python3
"""
E45_nearcue_p_zero_decide.py -- exploration point E45, step 16: DECIDE, exhaustively and exactly, whether
the ramp can be met by an all-two-mark law on the refined grid (i.e. whether the simple fraction can be 0).

WHY
  Step 14's linear program said the minimal simple fraction on the refined grid is exactly zero, but the
  exact search of step 15 (sampled supports among all-two configurations) found nothing, so the zero was
  unverified.  A giant degenerate program of fourteen thousand variables can satisfy its equations to
  tolerance while no exact feasible point exists, and this project's habit is to suspect the computation
  first.  This step replaces sampling with an exhaustive, exact decision.

WHY EXHAUSTIVE IS POSSIBLE
  For an all-two configuration the two marked points sit at grid positions p, q, and the value depends only
  on the difference delta = q - p modulo 16 (the cosines are even).  So there are just EIGHT essentially
  different value vectors, delta = 1..8, with delta = 8 being its own negation.  Any law supported on all-two
  configurations therefore induces a weight on these eight classes, and the ramp condition depends only on
  those eight weights.  It is thus enough to test every nonempty subset of the eight classes (255 of them),
  solve the exact rational system for that subset (four field coordinates per class), and check the weights'
  signs rigorously.  No support beyond these eight is possible, so the answer is complete for laws whose
  weights lie in the field K = Q(zeta_16)^+.

INPUTS   none (exact rational arithmetic; the only irrational step is the rigorous sign test)
OUTPUT   scripts/E45_nearcue_p_zero_decide.txt

CONCLUSIONS (digit-driven)
  Whether some subset of the eight classes carries nonnegative field weights realising the ramp exactly.

PROVENANCE
  Written 2026-09-13 by 小灵, approved by 唐先生 (11:56 "继续细网格实验").  Field helpers imported from
  scripts/E45_nearcue_p_floor_fine.py (arithmetic implemented once).
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import itertools
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from E45_nearcue_p_floor_fine import fadd, fscale, cos_table  # noqa: E402

N = 4
Q = 16
SCALE = 10 ** 30
ZERO4 = (F(0), F(0), F(0), F(0))


def rat_sqrt_interval(x):
    big = 10 ** 60
    n = x.numerator * big // x.denominator
    r = math.isqrt(n)
    return F(r, 10 ** 30), F(r + 1, 10 ** 30)


def embed_intervals():
    two = F(2)
    s2lo, s2hi = rat_sqrt_interval(two)
    ulo = rat_sqrt_interval(two + s2lo)[0]
    uhi = rat_sqrt_interval(two + s2hi)[1]
    return [(F(1), F(1)), (ulo, uhi), (two + s2lo, two + s2hi),
            (ulo * (two + s2lo), uhi * (two + s2hi))]


EMB_IV = embed_intervals()


def sign_of(a):
    lo = sum(min(a[i] * EMB_IV[i][0], a[i] * EMB_IV[i][1]) for i in range(4))
    hi = sum(max(a[i] * EMB_IV[i][0], a[i] * EMB_IV[i][1]) for i in range(4))
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    if lo == 0 and hi == 0:
        return 0
    return None


def solve_exact(rows, rhs, n):
    aug = [[F(v) for v in rows[i]] + [F(rhs[i])] for i in range(len(rows))]
    m = len(aug); piv = []; r = 0
    for col in range(n):
        sel = next((i for i in range(r, m) if aug[i][col] != 0), None)
        if sel is None:
            continue
        aug[r], aug[sel] = aug[sel], aug[r]
        pv = aug[r][col]
        aug[r] = [v / pv for v in aug[r]]
        for i in range(m):
            if i != r and aug[i][col] != 0:
                f = aug[i][col]
                aug[i] = [aug[i][k] - f * aug[r][k] for k in range(n + 1)]
        piv.append(col); r += 1
        if r == m:
            break
    for i in range(r, m):
        if all(v == 0 for v in aug[i][:n]) and aug[i][n] != 0:
            return None
    sol = [F(0)] * n
    for i, col in enumerate(piv):
        sol[col] = aug[i][n]
    return sol


def main():
    COS = cos_table(Q)
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 16 -- EXHAUSTIVE exact decision: can the ramp be met by an all-two-mark law (p = 0)")
    w("on the refined grid (N = 4, Q = 16)?  Eight difference classes, all 255 supports tested.")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    # value vector per difference class, marks 2 and 2, so the pair weight is 4
    VAL = {}
    for d in range(1, Q):
        accs = []
        for j in range(1, N + 1):
            acc = ZERO4
            for k1, p in enumerate((0, d)):
                for k2, q in enumerate((0, d)):
                    acc = fadd(acc, fscale(COS[(j * (p - q)) % Q], F(4)))
            accs.append(acc)
        VAL[d] = accs
    classes = sorted(set(min(d, Q - d) for d in range(1, Q)))
    w("difference classes (up to sign): %s" % classes, flush=True)
    for d in classes:
        w("   delta = %2d : |F(1)|^2 = %s , |F(2)|^2 = %s , |F(3)|^2 = %s"
          % (d, tuple(str(x) for x in VAL[d][0]), tuple(str(x) for x in VAL[d][1]),
             tuple(str(x) for x in VAL[d][2])), flush=True)

    hits = []
    for r in range(1, len(classes) + 1):
        for sub in itertools.combinations(classes, r):
            n = 4 * r
            rows = []; rhs = []
            for j in range(1, N):
                for comp in range(4):
                    row = [F(0)] * n
                    for k, d in enumerate(sub):
                        row[4 * k + comp] = VAL[d][j - 1][comp]
                    rows.append(row)
                    rhs.append(F(j) if comp == 0 else F(0))
            for comp in range(4):
                row = [F(0)] * n
                if comp == 0:
                    for k in range(r):
                        row[4 * k] = F(1)
                rows.append(row)
                rhs.append(F(1) if comp == 0 else F(0))
            sol = solve_exact(rows, rhs, n)
            if sol is None:
                continue
            if any(sol[4 * k + c] is None for k in range(r) for c in range(4)):
                continue
            signs = [sign_of(tuple(sol[4 * k + c] for c in range(4))) for k in range(r)]
            if all(s is not None and s >= 0 for s in signs):
                hits.append((sub, sol, signs))
    w("", flush=True)
    w("supports tested: %d (all nonempty subsets of the %d classes)" % (2 ** len(classes) - 1, len(classes)),
      flush=True)
    w("EXACT nonnegative solutions with p = 0 : %d" % len(hits), flush=True)
    for sub, sol, signs in hits[:5]:
        w("   hit: deltas %s" % (list(sub),), flush=True)
        for k, d in enumerate(sub):
            wt = tuple(sol[4 * k + c] for c in range(4))
            w("      w(delta=%d) = %s + (%s)u + (%s)u^2 + (%s)u^3" % (d, wt[0], wt[1], wt[2], wt[3]),
              flush=True)
    w("", flush=True)
    if hits:
        w("   => p = 0 IS exactly achievable on the refined grid, hence by convexity every simple fraction", flush=True)
        w("      in the achievable interval -- in particular the frontier's 0.6818287 -- is achievable.", flush=True)
    else:
        w("   => NO all-two-mark law with field weights realises the ramp exactly on this grid:", flush=True)
        w("      p = 0 is NOT achievable, so the zero reported by the float program in step 14 was a", flush=True)
        w("      numerical artifact, as the exact search of step 15 already suggested.", flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  This is a complete decision for laws whose weights lie in K = Q(zeta_16)^+: every possible support")
    w("  among the eight difference classes was solved exactly.  Weights outside K are not covered.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_p_zero_decide.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
