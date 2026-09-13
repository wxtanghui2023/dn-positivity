#!/usr/bin/env python3
"""
E45_nearcue_edge_control.py -- exploration point E45, step 7: is the EDGE ROW forced by the ramp?

QUESTION
  Steps 5-6 found exact-ramp laws (tau = 0) at N = 4 and N = 6, and in BOTH cases the free edge row came
  out S(N) = 1, i.e. the edge value E|F(N)|^2 was exactly N.  That is suspiciously rigid, so this script
  asks whether the ramp condition FORCES it.

WHY IT MATTERS (and why this is the sharp question)
  The theorem leaves the last row free: NearCUE constrains only 1 <= j < N, while the atom masses use
  j = 1..N.  So the edge row is exactly the remaining degree of freedom, and with tau = 0 the theorem's
  only other input is the edge bound
        d1 = |D(1)| = |C(1) - 1/2| = |S(N)/N - 1/(2N)| ,
  using C(1) = (N-1)/(2N) + S(N)/N from the ramp on the first N-1 rows.
  The frontier's own law has S(256) = 211.432..., hence D(1) = 0.82395317 -- precisely the recorded edge
  bound, so their instance is completely described by its edge row.
  Therefore:
    * if the ramp FORCES S(N) = N, then no exact-ramp law can have the frontier's large edge value, so
      their tau = 3e-40 is forced to be positive -- an explanation of why they need a tolerance at all;
    * if S(N) is FREE, then the frontier's shape is compatible with tau = 0, and their tolerance is a
      choice rather than a necessity.

METHOD
  Same exact machinery as step 5 (weights w = u + t*sqrt(D), ramp condition equivalent to two rational
  systems, exact nonnegativity test).  Here the search does NOT stop at the first hit: it collects many
  exact-ramp laws and reports the SET of achievable edge values S(N) = E|F(N)|^2 / N, exactly as an
  element of the quadratic field plus a decimal, together with the implied d1 = |S(N)/N - 1/(2N)|.

INPUTS   none (exact rational arithmetic; fixed seed)
OUTPUT   scripts/E45_nearcue_edge_control.txt

CONCLUSIONS (digit-driven; printed as it goes)
  Distinct edge values observed, their exact forms, and whether they are all equal to the grid size.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session), exploration point E45, approved by 唐先生 (11:13 "继续深化E45").
  Sources: arXiv:2608.13637v2 section 7.2; github.com/anthropics/zeta-23-lean tag v1.0; our own E44/E45
  records.  No RH assumption used or claimed.
"""

import itertools
import os
import random
import sys
from fractions import Fraction as F

DQ = {8: 2, 12: 3, 10: 5}
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
TRIALS = 6000
HIT_CAP = 40


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
    w("E45 step 7 -- is the EDGE ROW forced by the ramp condition?  (exact-ramp laws, tau = 0)")
    w("edge row S(N) = E|F(N)|^2 / N is the one row NearCUE leaves free; with tau = 0 the theorem's")
    w("only other input is d1 = |S(N)/N - 1/(2N)|.  Question: is S(N) pinned to the grid size N?")
    w("=" * 100, flush=True)
    for N in (4, 6):
        Q = 2 * N; D = DQ[Q]
        fam, A, B = build(N, Q)
        w("", flush=True)
        w("N = %d (Q = %d, field Q(sqrt%d), family %d configs)" % (N, Q, D, len(fam)), flush=True)
        edge_vals = {}      # (a,b) -> count
        hits = 0
        for m in (N, N + 1, N + 2):
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
                # exact edge row: E|F(N)|^2 = sum_c w_c |F_c(N)|^2 = (aN, bN)
                aN = F(0); bN = F(0)
                for k, ci in enumerate(idx):
                    u, t = sol[k], sol[m + k]
                    aN += u * A[(ci, N)] + D * t * B[(ci, N)]
                    bN += u * B[(ci, N)] + t * A[(ci, N)]
                key = (aN / N, bN / N)          # S(N) = E|F(N)|^2 / N
                edge_vals[key] = edge_vals.get(key, 0) + 1
                hits += 1
                if hits >= HIT_CAP:
                    break
            if hits >= HIT_CAP:
                break
        w("   exact-ramp laws collected: %d ; distinct edge values S(N): %d"
          % (hits, len(edge_vals)), flush=True)
        # report the distinct edge values, sorted, with the implied d1
        rowsrep = []
        for (a, b), cnt in edge_vals.items():
            dec = float(a) + float(b) * float(D) ** 0.5
            d1 = abs(a / N + b * float(D) ** 0.5 / N - 1.0 / (2 * N))     # |S(N)/N - 1/(2N)|
            rowsrep.append((dec, a, b, cnt, d1))
        rowsrep.sort()
        for dec, a, b, cnt, d1 in rowsrep:
            w("     S(N) = %s + (%s)sqrt%d = %.9f   (appears %d times)  =>  d1 = |S(N)/N - 1/(2N)| = %.9f"
              % (a, b, D, dec, cnt, d1))
        w("   NOTE: for the frontier at N = 256 the edge row is S(256) = 211.432009... , giving")
        w("         d1 = 0.82395317 exactly as recorded -- their instance is fixed by this one number.")
    w("")
    w("=" * 100)
    w("READING")
    w("  If every exact-ramp law shows S(N) = 1 (edge value = grid size N), the ramp PINS the edge row,")
    w("  and the frontier's large edge value is incompatible with an exact ramp -- which would explain")
    w("  why their construction needs tau = 3e-40 > 0.  If several distinct edge values occur, the edge")
    w("  row is controllable in exact-ramp laws, and the frontier's tolerance is a choice, not a necessity.")
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_edge_control.txt"), "w").write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
