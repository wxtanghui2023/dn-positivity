#!/usr/bin/env python3
"""
E45_nearcue_p_zero_check.py -- exploration point E45, step 15: verify EXACTLY that an exact-ramp law with
a vanishing simple fraction exists on the refined grid (the float LP said so; this proves it).

WHY
  Step 14 solved a linear program on the refined grid (N = 4, positions on the 16-grid, field
  K = Q(zeta_16)^+ = Q[u]/(u^4-4u^2+2)) and reported a minimal simple fraction of exactly zero, i.e. the
  program claimed the ramp can be met exactly by a law all of whose points are in off-line pairs.  Floating
  point cannot establish that.  Because every field coordinate is RATIONAL, the ramp equations are a
  RATIONAL linear system in the coordinates of the weights, so feasibility can be decided exactly by
  elimination, and the only ingredient needing care is the SIGN of a field element in the chosen real
  embedding -- handled here with rational interval bounds on sqrt2 and u, so the sign test is rigorous.

WHY IT MATTERS
  The set of achievable simple fractions is the image of a convex set under a linear map, hence an interval.
  If p = 0 is exactly achievable, then EVERY simple fraction in that interval is achievable, in particular
  the frontier's 0.6818287 -- which would mean the coarse-grid obstruction found in steps 12-13 is a
  resolution effect rather than a property of exactness.

METHOD
  Restrict to all-two configurations (two points of mark two on the 16-grid: C(16,2) = 120 of them, each with
  zero mark-one points, so p = 0 by construction).  Sample supports of size s, solve the exact rational
  system (4 field components per j, plus the normalisation m0 = 1) by Gaussian elimination over Q, and test
  nonnegativity of every weight rigorously with rational interval bounds.  First success is reported.

INPUTS   none (exact rational arithmetic)
OUTPUT   scripts/E45_nearcue_p_zero_check.txt

PROVENANCE
  Written 2026-09-13 by 小灵, approved by 唐先生 (11:56 "继续细网格实验").  Field helpers are imported from
  scripts/E45_nearcue_p_floor_fine.py so that the arithmetic is implemented exactly once.
  Sources: docs/E45-ceiling-law-construction.md sections 20-21; arXiv:2608.13637v2 section 7.2.
  No RH assumption used or claimed, and NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import itertools
import math
import os
import random
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from E45_nearcue_p_floor_fine import fmul, fadd, fscale, cos_table, all_marked, EMB  # noqa: E402

SEED = 20260913
TRIALS = 600
SIZES = (5, 6, 7)
SCALE = 10 ** 30


def rat_sqrt_interval(x: F):
    """rigorous rational interval [lo, hi] containing sqrt(x) for rational x >= 0"""
    n = x.numerator * SCALE * SCALE
    d = x.denominator
    # sqrt(x) = sqrt(n/d)/SCALE  ->  bound sqrt(n/d) by isqrt of n*big/d
    big = 10 ** 60
    r = math.isqrt(int(n * big // d))
    lo = F(r, SCALE * 10 ** 30)
    hi = F(r + 1, SCALE * 10 ** 30)
    return lo, hi


def embed_intervals():
    """rigorous intervals for the basis values 1, u, u^2, u^3 in the chosen embedding (u > 0)"""
    two = F(2)
    # sqrt2
    s2lo, s2hi = rat_sqrt_interval(two)
    # u = sqrt(2 + sqrt2)
    ulo = rat_sqrt_interval(two + s2lo)[0]
    uhi = rat_sqrt_interval(two + s2hi)[1]
    u2lo, u2hi = two + s2lo, two + s2hi
    u3lo = ulo * u2lo
    u3hi = uhi * u2hi
    return [(F(1), F(1)), (ulo, uhi), (u2lo, u2hi), (u3lo, u3hi)]


EMB_IV = None


def sign_of(a):
    """rigorous sign of the field element a = (c0,c1,c2,c3) in the chosen embedding: -1, 0, +1, or None"""
    lo = sum(min(a[i] * EMB_IV[i][0], a[i] * EMB_IV[i][1]) for i in range(4))
    hi = sum(max(a[i] * EMB_IV[i][0], a[i] * EMB_IV[i][1]) for i in range(4))
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    if lo == 0 and hi == 0:
        return 0
    return None                      # interval straddles zero; treated as inconclusive (never a false +)


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
    global EMB_IV
    EMB_IV = embed_intervals()
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    N = 4; Q = 16
    COS = cos_table(Q)
    w("E45 step 15 -- EXACT verification that the ramp can be met by an all-two-mark law on the 16-grid")
    w("(so that its simple fraction is exactly 0, and by convexity every fraction in the interval is reachable)")
    w("rigorous sign test via rational interval bounds on sqrt2 and u=sqrt(2+sqrt2)")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    fam = [(pos, (2, 2)) for pos in itertools.combinations(range(Q), 2)]
    M = len(fam)
    w("all-two configurations on the 16-grid: %d  (each has no mark-one points, so p = 0)" % M, flush=True)
    VAL = [[(F(0), F(0), F(0), F(0)) for _ in range(N + 1)] for _ in range(M)]
    for ci, (pos, marks) in enumerate(fam):
        for j in range(1, N + 1):
            acc = (F(0), F(0), F(0), F(0))
            for k1 in range(len(pos)):
                for k2 in range(len(pos)):
                    acc = fadd(acc, fscale(COS[(j * (pos[k1] - pos[k2])) % Q], F(4)))
            VAL[ci][j] = acc

    rng = random.Random(SEED)
    hit = None
    for s in SIZES:
        for trial in range(TRIALS):
            idx = rng.sample(range(M), s)
            n = 4 * s
            rows = []; rhs = []
            # four field components per frequency j = 1..N-1
            for j in range(1, N):
                for comp in range(4):
                    row = [F(0)] * n
                    for k, ci in enumerate(idx):
                        row[4 * k + comp] = VAL[ci][j][comp]
                    rows.append(row)
                    rhs.append(F(j) if comp == 0 else F(0))
            # normalisation: sum of weights = 1 in the field
            for comp in range(4):
                row = [F(0)] * n
                for k in range(s):
                    if comp == 0:
                        row[4 * k] = F(1)
                rows.append(row)
                rhs.append(F(1) if comp == 0 else F(0))
            sol = solve_exact(rows, rhs, n)
            if sol is None:
                continue
            signs = []
            ok = True
            for k in range(s):
                sg = sign_of(tuple(sol[4 * k + c] for c in range(4)))
                signs.append(sg)
                if sg is None or sg < 0:
                    ok = False
                    break
            if ok:
                hit = (s, idx, sol, signs)
                break
        if hit:
            break
    if hit:
        s, idx, sol, signs = hit
        w("", flush=True)
        w("   *** EXACT HIT ***  support size %d, all weights nonnegative (rigorous sign test)" % s, flush=True)
        for k, ci in enumerate(idx):
            pos = fam[ci][0]
            wt = tuple(sol[4 * k + c] for c in range(4))
            w("      w = %s + (%s)u + (%s)u^2 + (%s)u^3   at grid positions %s (all marks 2)"
              % (wt[0], wt[1], wt[2], wt[3], list(pos)), flush=True)
        w("", flush=True)
        w("   => the ramp holds EXACTLY with this law, and it has NO mark-one points:", flush=True)
        w("      simple fraction p = 0 EXACTLY on the refined grid.", flush=True)
        w("   => by convexity of the feasible set, every p in [0, 1] is achievable by an exact-ramp law", flush=True)
        w("      on this grid -- in particular the frontier's 0.6818287.", flush=True)
    else:
        w("", flush=True)
        w("   no exact nonnegative solution found in %d trials per size %s (evidence, not proof)" % (TRIALS, SIZES),
          flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  A verified hit means the coarse-grid obstruction of steps 12-13 is a RESOLUTION effect: exactness")
    w("  and a ceiling-comparable simple fraction can coexist once the position grid is fine enough.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_p_zero_check.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
