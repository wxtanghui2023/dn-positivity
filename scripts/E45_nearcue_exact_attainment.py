#!/usr/bin/env python3
"""
E45_nearcue_exact_attainment.py -- exploration point E45, step 5: is tau = 0 attainable?

THE OPEN QUESTION (left open in docs/E45-ceiling-law-construction.md section 4)
  Can the ramp  sum_c w_c |F_c(j)|^2 = j,  j = 1..N-1,  be met EXACTLY by a law with algebraic weights?
  Step 2 decided only the RATIONAL-weight case; for weights in a quadratic field the same real equation
  can hold with both parts nonzero, so exactness stayed open.  This script decides it as far as it can.

WHY IT IS DECIDABLE, AND HOW
  On the grid m/Q with Q = 2N every |F_c(j)|^2 lies in a quadratic field (Q(sqrt2), Q(sqrt3), Q(sqrt5)
  for N = 4, 6, 5).  Write |F_c(j)|^2 = a_cj + b_cj sqrt(D) and allow weights w_c = u_c + t_c sqrt(D)
  with u,t RATIONAL.  Then
      w_c |F_c(j)|^2 = (u_c a_cj + D t_c b_cj) + (u_c b_cj + t_c a_cj) sqrt(D),
  so  sum_c w_c |F_c(j)|^2 = j  (rational right side) is EQUIVALENT to the two RATIONAL equations
      sum_c (u_c a_cj + D t_c b_cj) = j        sum_c (u_c b_cj + t_c a_cj) = 0 ,
  for every j, together with sum_c u_c = 1 and sum_c t_c = 0.  This is a RATIONAL LINEAR SYSTEM in the
  2m unknowns (u_c, t_c) for a support of size m -- decidable by exact elimination.
  Nonnegativity of the weights, u_c + t_c sqrt(D) >= 0, is then checked EXACTLY:
      t = 0 -> u >= 0 ;  u >= 0, t < 0 -> u^2 >= D t^2 ;  u < 0 -> t > 0 and D t^2 >= u^2 .
  Note w_c = 0 forces u_c = t_c = 0 (rationals), so zero weights are exactly the zero pair.

METHOD
  Random supports of increasing size; exact Gaussian elimination over Q; exact nonnegativity test; and a
  from-scratch re-verification of the ramp for any candidate.  A hit is an exact certificate.

INPUTS   none (exact rational arithmetic; fixed seed for reproducibility)
OUTPUT   scripts/E45_nearcue_exact_attainment.txt

CONCLUSIONS (digit-driven; printed as it goes)
  A hit  => tau = 0 IS attainable: the ceiling theorem's only numeric input becomes an exact identity in a
            quadratic field, and the theorem's constant loses its tau term, leaving 1/(6N^2).
  No hit => evidence (not proof) that these grids force tau > 0, pointing the construction at finer grids.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session), exploration point E45, approved by 唐先生.
  Sources: arXiv:2608.13637v2 section 7.2; github.com/anthropics/zeta-23-lean tag v1.0.  No RH claim.
"""

import itertools
import os
import random
import sys
from fractions import Fraction as F

DQ = {8: 2, 10: 5, 12: 3}
COS = {}
COS[8] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
          4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))}
COS[12] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(1, 2), F(0)), 3: (F(0), F(0)),
           4: (F(-1, 2), F(0)), 5: (F(0), F(-1, 2)), 6: (F(-1), F(0)), 7: (F(0), F(-1, 2)),
           8: (F(-1, 2), F(0)), 9: (F(0), F(0)), 10: (F(1, 2), F(0)), 11: (F(0), F(1, 2))}
COS[10] = {0: (F(1), F(0)), 1: (F(1, 4), F(1, 4)), 2: (F(-1, 4), F(1, 4)), 3: (F(-1, 4), F(-1, 4)),
           4: (F(1, 4), F(-1, 4)), 5: (F(-1), F(0)), 6: (F(1, 4), F(-1, 4)), 7: (F(-1, 4), F(-1, 4)),
           8: (F(-1, 4), F(1, 4)), 9: (F(1, 4), F(1, 4))}

SEED = 20260913
TRIALS = 4000
MAX_EXTRA = 4


def values(N, Q, pos, marks, j):
    a = F(0); b = F(0)
    for k1 in range(len(pos)):
        for k2 in range(len(pos)):
            ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
            m = marks[k1] * marks[k2]
            a += ca * m; b += cb * m
    return a, b


def build(N, Q):
    fam = [(sub, (1,) * N) for sub in itertools.combinations(range(Q), N)]
    if N % 2 == 0:
        fam += [(sub, (2,) * (N // 2)) for sub in itertools.combinations(range(Q), N // 2)]
    A = {}; B = {}
    for ci, (pos, marks) in enumerate(fam):
        for j in range(1, N):
            a, b = values(N, Q, pos, marks, j)
            A[(ci, j)] = a; B[(ci, j)] = b
    return fam, A, B


def nonneg(u, t, D):
    """EXACT and COMPLETE test of u + t*sqrt(D) >= 0.
    Self-correction: the first version required u^2 >= D t^2 whenever u >= 0, which wrongly rejects the
    valid case t > 0 (where u >= 0 alone already suffices) -- a conservative test that can LOSE hits."""
    if t == 0:
        return u >= 0
    if t > 0:
        return True if u >= 0 else (D * t * t >= u * u)
    return u >= 0 and u * u >= D * t * t


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


def system(N, D, fam_idx, A, B):
    m = len(fam_idx)
    rows = []; rhs = []
    for j in range(1, N):
        r1 = [F(0)] * (2 * m); r2 = [F(0)] * (2 * m)
        for k, ci in enumerate(fam_idx):
            r1[k] = A[(ci, j)]; r1[m + k] = D * B[(ci, j)]
            r2[k] = B[(ci, j)]; r2[m + k] = A[(ci, j)]
        rows.append(r1); rhs.append(F(j))
        rows.append(r2); rhs.append(F(0))
    rows.append([F(1)] * m + [F(0)] * m); rhs.append(F(1))
    rows.append([F(0)] * m + [F(1)] * m); rhs.append(F(0))
    return rows, rhs


def main():
    log = []
    def w(s, flush=False):
        log.append(s)
        if flush:
            print(s, flush=True)

    rng = random.Random(SEED)
    w("E45 step 5 -- is tau = 0 attainable?  exact-attainment search (weights in a quadratic field)")
    w("system: 2N rational equations in (u_c,t_c); nonneg checked exactly; hits re-verified from scratch")
    w("=" * 100, flush=True)
    for N in (4, 6, 5):
        Q = 2 * N; D = DQ[Q]
        fam, A, B = build(N, Q)
        w("", flush=True)
        w("N = %d (Q = %d, field Q(sqrt%d), family %d configs, %d equations)"
          % (N, Q, D, len(fam), 2 * N), flush=True)
        hit = None
        for extra in range(0, MAX_EXTRA + 1):
            m = N + extra
            best = None
            for _ in range(TRIALS):
                idx = rng.sample(range(len(fam)), m)
                rows, rhs = system(N, D, idx, A, B)
                sol = solve_exact(rows, rhs, 2 * m)
                if sol is None:
                    continue
                ws = []; ok = True
                for k in range(m):
                    u, t = sol[k], sol[m + k]
                    if not nonneg(u, t, D):
                        ok = False; break
                    ws.append((idx[k], u, t))
                if ok:
                    hit = (m, ws); break
            if hit:
                break
            w("   support m = %d : no exact nonneg solution in %d supports"
              % (m, TRIALS), flush=True)
        if hit:
            m, ws = hit
            w("   *** HIT *** support m = %d" % m, flush=True)
            for ci, u, t in ws:
                pos, marks = fam[ci]
                w("     w = %s + (%s)sqrt%d   positions %s  marks %s"
                  % (u, t, D, list(pos), list(marks)))
            w("   re-verification: ramp recomputed from scratch with these weights ...")
            allok = True
            for j in range(1, N):
                s1 = F(0); s2 = F(0)
                for ci, u, t in ws:
                    pos, marks = fam[ci]
                    a, b = values(N, Q, pos, marks, j)
                    s1 += u * a + D * t * b
                    s2 += u * b + t * a
                if s1 != j or s2 != 0:
                    allok = False
            w("   EXACT ramp sum_c w_c|F_c(j)|^2 = j for all j : %s" % allok)
            if allok:
                w("   => tau = 0 IS ATTAINABLE at N = %d.  S(j) = j/N exactly;" % N)
                w("      the ceiling theorem's constant becomes 1/(6N^2) = %s (no tau term)."
                  % F(1, 6 * N * N))
        else:
            w("   NO HIT for supports N..N+%d  => evidence (not proof) that tau > 0 is forced here"
              % MAX_EXTRA, flush=True)
    w("")
    w("=" * 100)
    w("READING")
    w("  A hit proves tau = 0 attainable and turns the only numeric input of the ceiling theorem into an")
    w("  exact identity in a quadratic field.  No hit over small supports is evidence that these grids")
    w("  force tau > 0, pointing the construction at finer grids (larger position height).")
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_exact_attainment.txt"), "w").write("\n".join(log) + "\n")


if __name__ == "__main__":
    main()
