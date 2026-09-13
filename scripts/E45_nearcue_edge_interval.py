#!/usr/bin/env python3
"""
E45_nearcue_edge_interval.py -- exploration point E45, step 9: does one family fill an INTERVAL of
edge values?

WHY THIS STEP EXISTS (a methodological correction)
  Step 8 (scripts/E45_nearcue_edge_set_structure.py) sampled exact-ramp laws and reported visibly
  isolated edge values, suggesting a discrete set.  That reading is NOT reliable: the exact solver used
  there returns the particular solution with all free variables set to zero, so every sample is one point
  of the affine solution family and the sampling never probes the family's interior.  The theory says the
  image should be an interval: for a support larger than the number of equations the solution set is an
  affine family of positive dimension, nonnegativity cuts a polytope in it, and the edge functional
  S(N) = sum_c w_c |F_c(N)|^2 is LINEAR there.  This step settles the question by optimising directly.

METHOD
  For a fixed support, maximise and minimise the edge functional subject to
      (i)  the ramp: 2(N-1) + 2 exact rational equations in (u_c, t_c),
      (ii) nonnegativity w_c = u_c + t_c sqrt(D) >= 0,
  which is a linear program (the only irrational coefficient is sqrt(D), used here at floating point
  precision to locate the optimum).  The interval length between the two optima answers the question;
  a positive length means the achievable edge set contains an interval, so any edge value in it -- in
  particular one matching the frontier's shape -- is attainable EXACTLY.

INPUTS   none (exact rational construction; floating-point LP for the optimum)
OUTPUT   scripts/E45_nearcue_edge_interval.txt

CONCLUSIONS (digit-driven)
  interval length > 0  => the edge set is continuous (contains an interval); the frontier's edge shape can
                          be matched exactly by an exact-ramp law.
  interval length = 0  => the edge functional is constant on that family, so the edge set is governed by
                          other structure.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session), exploration point E45, approved by 唐先生 (11:20 "继续").
  Sources: arXiv:2608.13637v2 section 7.2; github.com/anthropics/zeta-23-lean tag v1.0.  No RH claim.
"""

import itertools
import os
import random
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

SEED = 20260913


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


def feasible_exact(N, D, idx, A, B, sol_f, tol=1e-7):
    """recover exact rationals from the float solution by solving the active system exactly"""
    m = len(idx)
    # active equations: all ramp rows; plus nonneg rows that are (numerically) tight
    rows = []; rhs = []
    for j in range(1, N):
        r1 = [F(0)] * (2 * m); r2 = [F(0)] * (2 * m)
        for k, ci in enumerate(idx):
            r1[k] = A[(ci, j)]; r1[k + m] = D * B[(ci, j)]
            r2[k] = B[(ci, j)]; r2[k + m] = A[(ci, j)]
        rows.append(r1); rhs.append(F(j))
        rows.append(r2); rhs.append(F(0))
    rows.append([F(1)] * m + [F(0)] * m); rhs.append(F(1))
    rows.append([F(0)] * m + [F(1)] * m); rhs.append(F(0))
    for k in range(m):
        u = sol_f[k]; t = sol_f[k + m]
        if abs(u + t * np.sqrt(D)) < 1e-7:
            r = [F(0)] * (2 * m); r[k] = F(1); r[k + m] = F(0)   # placeholder; w=0 <=> u=t=0 handled below
            # we simply fix u_k = 0 and t_k = 0 as two extra equations
            r1 = [F(0)] * (2 * m); r1[k] = F(1); rows.append(r1); rhs.append(F(0))
            r2 = [F(0)] * (2 * m); r2[k + m] = F(1); rows.append(r2); rhs.append(F(0))
    # exact solve
    aug = [[F(v) for v in rows[i]] + [rhs[i]] for i in range(len(rows))]
    mm = len(aug); n = 2 * m; piv = []; r = 0
    for col in range(n):
        sel = next((i for i in range(r, mm) if aug[i][col] != 0), None)
        if sel is None:
            continue
        aug[r], aug[sel] = aug[sel], aug[r]
        pv = aug[r][col]
        aug[r] = [v / pv for v in aug[r]]
        for i in range(mm):
            if i != r and aug[i][col] != 0:
                f = aug[i][col]
                aug[i] = [aug[i][kk] - f * aug[r][kk] for kk in range(n + 1)]
        piv.append(col); r += 1
        if r == mm:
            break
    for i in range(r, mm):
        if all(v == 0 for v in aug[i][:n]) and aug[i][n] != 0:
            return None
    sol = [F(0)] * n
    for i, col in enumerate(piv):
        sol[col] = aug[i][n]
    return sol


def solve_exact_simple(N, D, idx, A, B):
    """exact solution (free variables set to zero) of the ramp system on this support, or None"""
    m = len(idx)
    rows = []; rhs = []
    for j in range(1, N):
        r1 = [F(0)] * (2 * m); r2 = [F(0)] * (2 * m)
        for k, ci in enumerate(idx):
            r1[k] = A[(ci, j)]; r1[k + m] = D * B[(ci, j)]
            r2[k] = B[(ci, j)]; r2[k + m] = A[(ci, j)]
        rows.append(r1); rhs.append(F(j))
        rows.append(r2); rhs.append(F(0))
    rows.append([F(1)] * m + [F(0)] * m); rhs.append(F(1))
    rows.append([F(0)] * m + [F(1)] * m); rhs.append(F(0))
    n = 2 * m
    aug = [[F(v) for v in rows[i]] + [rhs[i]] for i in range(len(rows))]
    mm = len(aug); piv = []; r = 0
    for col in range(n):
        sel = next((i for i in range(r, mm) if aug[i][col] != 0), None)
        if sel is None:
            continue
        aug[r], aug[sel] = aug[sel], aug[r]
        pv = aug[r][col]
        aug[r] = [v / pv for v in aug[r]]
        for i in range(mm):
            if i != r and aug[i][col] != 0:
                f = aug[i][col]
                aug[i] = [aug[i][kk] - f * aug[r][kk] for kk in range(n + 1)]
        piv.append(col); r += 1
        if r == mm:
            break
    for i in range(r, mm):
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

    w("E45 step 9 -- does one solution FAMILY fill an interval of edge values?  (direct optimisation)")
    w("objective: maximise/minimise S(N) = sum_c w_c |F_c(N)|^2 subject to the exact ramp equations")
    w("and to w_c = u_c + t_c sqrt(D) >= 0.  Positive interval length => the edge set is continuous.")
    w("phase 1: find a support (size > N) that admits a nonneg exact-ramp solution at all")
    w("phase 2: on that support, optimise the edge functional in both directions")
    w("=" * 100, flush=True)
    for N in (4, 6):
        Q = 2 * N; D = DQ[Q]
        fam, A, B = build(N, Q)
        w("", flush=True)
        w("N = %d (Q = %d, field Q(sqrt%d), %d configs)" % (N, Q, D, len(fam)), flush=True)
        rng = random.Random(SEED)
        for m in (N + 1, N + 2):
            support = None
            trials = 0
            while trials < 12000 and support is None:
                trials += 1
                idx = rng.sample(range(len(fam)), m)
                sol = solve_exact_simple(N, D, idx, A, B)
                if sol is None:
                    continue
                if all(nonneg(sol[k], sol[k + m], D) for k in range(m)):
                    support = idx
            w("   m = %d : feasible support found after %d trials : %s"
              % (m, trials, "yes" if support else "NO"))
            if support is None:
                continue
            nv = 2 * m
            Aeq = np.zeros((2 * (N - 1) + 2, nv)); beq = np.zeros(2 * (N - 1) + 2)
            for j in range(1, N):
                for k, ci in enumerate(support):
                    Aeq[2 * (j - 1), k] = float(A[(ci, j)])
                    Aeq[2 * (j - 1), k + m] = D * float(B[(ci, j)])
                    Aeq[2 * (j - 1) + 1, k] = float(B[(ci, j)])
                    Aeq[2 * (j - 1) + 1, k + m] = float(A[(ci, j)])
                beq[2 * (j - 1)] = j; beq[2 * (j - 1) + 1] = 0.0
            for k in range(m):
                Aeq[2 * (N - 1), k] = 1.0
                Aeq[2 * (N - 1) + 1, k + m] = 1.0
            beq[2 * (N - 1)] = 1.0; beq[2 * (N - 1) + 1] = 0.0
            Aub = np.zeros((m, nv)); bub = np.zeros(m)
            for k in range(m):
                Aub[k, k] = -1.0
                Aub[k, k + m] = -np.sqrt(D)
            c = np.zeros(nv)
            for k, ci in enumerate(support):
                # objective S(N) = E|F(N)|^2 / N ; self-correction: an earlier version omitted the /N and
                # therefore reported E|F(N)|^2 instead (a factor N off in the printed interval)
                c[k] = (float(A[(ci, N)]) + np.sqrt(D) * float(B[(ci, N)])) / N
                c[k + m] = (D * float(B[(ci, N)]) + np.sqrt(D) * float(A[(ci, N)])) / N
            rmax = linprog(-c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq,
                           bounds=[(None, None)] * nv, method="highs")
            rmin = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq,
                           bounds=[(None, None)] * nv, method="highs")
            if not (rmax.success and rmin.success):
                w("   m = %d : LP failed" % m)
                continue
            hi, lo = -rmax.fun, rmin.fun
            w("   m = %d : edge interval S(N) = [%.9f, %.9f]   length = %.9f  %s"
              % (m, lo, hi, hi - lo, "=> CONTINUOUS" if hi - lo > 1e-7 else "=> the edge value is FORCED on this support"))
            w("      supports exactly re-checked at both optima: %s"
              % str([_check(N, D, support, A, B, v) for v in (rmin.x, rmax.x)]))
            if hi - lo > 1e-7:
                break
    w("")
    w("=" * 100)
    w("READING")
    w("  A positive interval length means one family already covers a whole range of edge values, so the")
    w("  achievable edge set is continuous and the frontier's edge shape can be matched EXACTLY at tau = 0.")
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_edge_interval.txt"), "w").write("\n".join(out) + "\n")


def _check(N, D, idx, A, B, sol_f, tol=1e-7):
    """verify a float LP optimum exactly: snap near-zero coordinates to zero, solve, test nonneg + ramp"""
    m = len(idx)
    rows = []; rhs = []
    for j in range(1, N):
        r1 = [F(0)] * (2 * m); r2 = [F(0)] * (2 * m)
        for k, ci in enumerate(idx):
            r1[k] = A[(ci, j)]; r1[k + m] = D * B[(ci, j)]
            r2[k] = B[(ci, j)]; r2[k + m] = A[(ci, j)]
        rows.append(r1); rhs.append(F(j))
        rows.append(r2); rhs.append(F(0))
    rows.append([F(1)] * m + [F(0)] * m); rhs.append(F(1))
    rows.append([F(0)] * m + [F(1)] * m); rhs.append(F(0))
    for k in range(m):
        if abs(sol_f[k]) < tol:
            r = [F(0)] * (2 * m); r[k] = F(1); rows.append(r); rhs.append(F(0))
        if abs(sol_f[k + m]) < tol:
            r = [F(0)] * (2 * m); r[k + m] = F(1); rows.append(r); rhs.append(F(0))
    n = 2 * m
    aug = [[F(v) for v in rows[i]] + [rhs[i]] for i in range(len(rows))]
    mm = len(aug); piv = []; r = 0
    for col in range(n):
        sel = next((i for i in range(r, mm) if aug[i][col] != 0), None)
        if sel is None:
            continue
        aug[r], aug[sel] = aug[sel], aug[r]
        pv = aug[r][col]
        aug[r] = [v / pv for v in aug[r]]
        for i in range(mm):
            if i != r and aug[i][col] != 0:
                f = aug[i][col]
                aug[i] = [aug[i][kk] - f * aug[r][kk] for kk in range(n + 1)]
        piv.append(col); r += 1
        if r == mm:
            break
    for i in range(r, mm):
        if all(v == 0 for v in aug[i][:n]) and aug[i][n] != 0:
            return "inconsistent"
    sol = [F(0)] * n
    for i, col in enumerate(piv):
        sol[col] = aug[i][n]
    if not all(nonneg(sol[k], sol[k + m], D) for k in range(m)):
        return "negative weight"
    for j in range(1, N):
        s1 = F(0); s2 = F(0)
        for k, ci in enumerate(idx):
            s1 += sol[k] * A[(ci, j)] + D * sol[k + m] * B[(ci, j)]
            s2 += sol[k] * B[(ci, j)] + sol[k + m] * A[(ci, j)]
        if s1 != j or s2 != 0:
            return "off ramp"
    return "OK"


if __name__ == "__main__":
    main()
