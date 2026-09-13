#!/usr/bin/env python3
"""
E45_nearcue_density.py -- exploration point E45, step 10: is the achievable edge set DENSE?

WHY
  Step 9 established that on a fixed support the edge value S(N) is FORCED (the edge functional is constant
  over the whole feasible family), so the achievable edge set is a set of per-support values, not an
  interval.  Whether that set becomes dense as supports grow decides something practical: if it does, then
  any prescribed edge value -- in particular one matching the frontier's shape -- can be approximated
  arbitrarily well by an exact-ramp law; if it stays sparse, exact matching is a search problem with no
  guarantee.

METHOD
  For grid size four, sample supports of growing size m and, for each support that admits a nonnegative
  exact-ramp solution, record the forced edge value S(N) exactly (an element of the quadratic field).  For
  each m report the number of feasible supports, the number of DISTINCT edge values, the smallest and
  largest gap between consecutive distinct values, and the range covered.  Densification shows up as
  growing distinct counts with shrinking smallest gaps.

INPUTS   none (exact rational arithmetic; fixed seed)
OUTPUT   scripts/E45_nearcue_density.txt

CONCLUSIONS (digit-driven)
  Number of distinct values and the smallest gap, per support size, with the trend between sizes.

PROVENANCE
  Written 2026-09-13 by 小灵 for the E45 continuation, approved by 唐先生 (11:36 "4，1，6都要深入分析").
  Sources: docs/E45-ceiling-law-construction.md sections 16-17; arXiv:2608.13637v2 section 7.2.
  No RH assumption used or claimed.  NOTE: no Lean is run here (compute directive of 2026-09-13 11:47).
"""

import itertools
import os
import random
from fractions import Fraction as F

DQ = {8: 2}
COS = {8: {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
           4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))}}

SEED = 20260913
M_LIST = (6, 8, 10, 12)
TRIALS = 4000


def values(N, Q, pos, marks, j):
    a = F(0); b = F(0)
    for k1 in range(len(pos)):
        for k2 in range(len(pos)):
            ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
            m = marks[k1] * marks[k2]
            a += ca * m; b += cb * m
    return a, b


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
    N = 4
    Q = 2 * N
    D = DQ[Q]
    fam = [(sub, (1,) * N) for sub in itertools.combinations(range(Q), N)]
    fam += [(sub, (2,) * (N // 2)) for sub in itertools.combinations(range(Q), N // 2)]
    A = {}; B = {}
    for ci, (pos, marks) in enumerate(fam):
        for j in range(1, N + 1):
            a, b = values(N, Q, pos, marks, j)
            A[(ci, j)] = a; B[(ci, j)] = b
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 10 -- does the achievable edge set become DENSE as support grows?  (N = 4, field Q(sqrt2))")
    w("step 9 showed the edge value is forced per support; here we sample supports of growing size and")
    w("measure how many distinct forced values occur and how small the gaps between them get.")
    w("NOTE: no Lean is run in this script (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)
    rng = random.Random(SEED)
    summary = []
    for m in M_LIST:
        vals = set()
        feas = 0
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
                if not nonneg(sol[k], sol[k + m], D):
                    ok = False; break
            if not ok:
                continue
            feas += 1
            aN = F(0); bN = F(0)
            for k, ci in enumerate(idx):
                u, t = sol[k], sol[k + m]
                aN += u * A[(ci, N)] + D * t * B[(ci, N)]
                bN += u * B[(ci, N)] + t * A[(ci, N)]
            vals.add((aN / N, bN / N))
        dec = sorted(float(a) + float(b) * float(D) ** 0.5 for a, b in vals)
        if len(dec) >= 2:
            gaps = [dec[i + 1] - dec[i] for i in range(len(dec) - 1)]
            ming, maxg = min(gaps), max(gaps)
        else:
            ming = maxg = float("nan")
        summary.append((m, feas, len(dec), dec[0] if dec else float("nan"),
                        dec[-1] if dec else float("nan"), ming, maxg))
        w("   m = %2d : feasible supports %5d / %d ; DISTINCT edge values %4d ; range [%.6f, %.6f]"
          % (m, feas, TRIALS, len(dec), dec[0] if dec else 0.0, dec[-1] if dec else 0.0), flush=True)
        w("            smallest gap %.9f ; largest gap %.9f ; median gap %.9f"
          % (ming, maxg, sorted(gaps)[len(gaps) // 2] if len(dec) >= 2 else float("nan")), flush=True)
    w("")
    w("=" * 100)
    w("TREND (support size m -> distinct values, smallest gap)")
    for m, feas, nd, lo, hi, ming, maxg in summary:
        w("   m = %2d : distinct %4d   smallest gap %.9f" % (m, nd, ming))
    w("")
    w("READING")
    w("  If the distinct count grows and the smallest gap shrinks as m grows, the achievable set densifies,")
    w("  so any prescribed edge value can be approximated arbitrarily well by an exact-ramp law.  If the")
    w("  smallest gap stalls, densification is not happening at these sizes and exact matching stays a search")
    w("  problem -- both answers are useful, and this script reports which one the data shows.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_density.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
