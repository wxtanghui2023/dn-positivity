#!/usr/bin/env python3
"""
E45_nearcue_edge_set_structure.py -- exploration point E45, step 8: is the achievable edge set
continuous or discrete?

CONTEXT
  Step 7 (scripts/E45_nearcue_edge_control.py) showed the edge row is NOT pinned by the ramp: 40 exact-ramp
  laws gave 3 distinct edge values at N = 4 and 28 at N = 6.  Whether that set is finite (a discrete set,
  because small supports force a unique solution) or an interval (supports with more configurations than
  the equations allow leave a family, and the edge functional is linear on it) is the natural next question,
  and it decides whether the frontier's specific edge value can be matched EXACTLY rather than approximated.

WHY EXPECT CONTINUITY
  The ramp imposes 2(N-1) + 2 = 2N rational equations on 2m unknowns (u_c, t_c) for a support of size m.
  For m = N the system is square and generically determines a unique solution, so its edge value is one
  point.  For m > N the solution set is an affine family of positive dimension, the feasibility condition
  w_c = u_c + t_c sqrt(D) >= 0 cuts a polytope in it, and the edge functional S(N) = sum_c w_c |F_c(N)|^2
  is LINEAR on that affine set -- so its image is an interval (a single point only if the functional is
  constant on the family).  Hence for larger supports the achievable set should fill intervals.

METHOD
  Reuse the exact machinery of step 5/7, but sample only supports of size N+1 .. N+3 (where a family
  exists) and collect many exact-ramp laws.  Report the number of distinct edge values, the minimum, the
  maximum, and the largest gaps between consecutive sorted values: many small gaps => the set is dense
  (intervals); a few large gaps with isolated values => discrete points.

INPUTS   none (exact rational arithmetic; fixed seed)
OUTPUT   scripts/E45_nearcue_edge_set_structure.txt

CONCLUSIONS (digit-driven)
  Density of the collected values, with the largest observed gaps, decides between "interval" and
  "isolated points" for the achievable edge set at these grid sizes.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session), exploration point E45, approved by 唐先生 (11:20 "继续").
  Sources: arXiv:2608.13637v2 section 7.2; github.com/anthropics/zeta-23-lean tag v1.0.  No RH claim.
"""

import itertools
import os
import random
from fractions import Fraction as F

DQ = {8: 2, 12: 3}
COS = {}
COS[8] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
          4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))}
COS[12] = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(1, 2), F(0)), 3: (F(0), F(0)),
           4: (F(-1, 2), F(0)), 5: (F(0), F(-1, 2)), 6: (F(-1), F(0)), 7: (F(0), F(-1, 2)),
           8: (F(-1, 2), F(0)), 9: (F(0), F(0)), 10: (F(1, 2), F(0)), 11: (F(0), F(1, 2))}

SEED = 20260913
TRIALS = 9000
CAP = 500


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
        for j in range(1, N + 1):
            a, b = values(N, Q, pos, marks, j)
            A[(ci, j)] = a; B[(ci, j)] = b
    return fam, A, B


def nonneg(u, t, D):
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


def main():
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    rng = random.Random(SEED)
    w("E45 step 8 -- structure of the achievable EDGE set (continuous interval vs isolated points)")
    w("theory: for support m > N the solution set is an affine family of positive dimension, the edge")
    w("functional is linear on it, and the nonnegativity cuts a polytope => the image should be an interval")
    w("=" * 100, flush=True)
    for N in (4, 6):
        Q = 2 * N; D = DQ[Q]
        fam, A, B = build(N, Q)
        w("", flush=True)
        w("N = %d (Q = %d, field Q(sqrt%d)) : %d equations per law; sampling supports of size %d..%d"
          % (N, Q, D, 2 * N, N + 1, N + 3), flush=True)
        found = set()
        for m in (N + 1, N + 2, N + 3):
            for _ in range(TRIALS):
                idx = rng.sample(range(len(fam)), m)
                rows = []; rhs = []
                for j in range(1, N):
                    r1 = [F(0)] * (2 * m); r2 = [F(0)] * (2 * m)
                    for k, ci in enumerate(idx):
                        r1[k] = A[(ci, j)]; r1[m + k] = D * B[(ci, j)]
                        r2[k] = B[(ci, j)]; r2[m + k] = A[(ci, j)]
                    rows.append(r1); rhs.append(F(j))
                    rows.append(r2); rhs.append(F(0))
                rows.append([F(1)] * m + [F(0)] * m); rhs.append(F(1))
                rows.append([F(0)] * m + [F(1)] * m); rhs.append(F(0))
                sol = solve_exact(rows, rhs, 2 * m)
                if sol is None:
                    continue
                ok = True
                for k in range(m):
                    if not nonneg(sol[k], sol[m + k], D):
                        ok = False; break
                if not ok:
                    continue
                aN = F(0); bN = F(0)
                for k, ci in enumerate(idx):
                    u, t = sol[k], sol[m + k]
                    aN += u * A[(ci, N)] + D * t * B[(ci, N)]
                    bN += u * B[(ci, N)] + t * A[(ci, N)]
                found.add((aN / N, bN / N))
                if len(found) >= CAP:
                    break
            if len(found) >= CAP:
                break
        vals = sorted(float(a) + float(b) * float(D) ** 0.5 for a, b in found)
        w("   distinct edge values S(N) collected: %d" % len(vals), flush=True)
        if vals:
            w("   min = %.9f   max = %.9f   (theoretical ceiling (sum m)^2/N = %.1f)"
              % (vals[0], vals[-1], (N * N) / N))
            gaps = sorted((vals[i + 1] - vals[i], i) for i in range(len(vals) - 1))
            big = gaps[-5:] if gaps else []
            w("   largest gaps between consecutive values: %s"
              % ", ".join("%.6f" % g for g, _ in reversed(big)))
            w("   median gap = %.9f" % (gaps[len(gaps) // 2][0] if gaps else 0.0))
            w("   => %s"
              % ("many small gaps: the set behaves like an INTERVAL (achievable values are dense)"
                 if gaps and gaps[len(gaps) // 2][0] < 1e-3 else
                 "large gaps: the collected values look ISOLATED (a discrete set at this sampling)"))
        # print a few values for the record
        w("   sample of collected values: %s" % ", ".join("%.6f" % v for v in vals[:12]))
    w("")
    w("=" * 100)
    w("READING")
    w("  Density with small median gaps at supports larger than N means the frontier's specific edge value")
    w("  (211.43 at N = 256, or anything comparable at these sizes) can be matched EXACTLY by an exact-ramp")
    w("  law, not merely approximated -- the strongest form of the E45 conclusion.")
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_edge_set_structure.txt"), "w").write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
