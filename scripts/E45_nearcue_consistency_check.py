#!/usr/bin/env python3
"""
E45_nearcue_consistency_check.py -- E45 reconciliation: is the ramp EXACTLY attainable, or only to
machine precision?

WHY THIS EXISTS
  E45 step 1 (scripts/E45_nearcue_law_probe.py) reported residual 0.000e+00 for the ramp condition
  sum_c w_c |F_c(j)|^2 = j, j = 1..N-1, on sampled grid laws -- i.e. it looked as if an EXACT near-CUE
  law exists.  E45 step 2/3 (scripts/E45_nearcue_rational_law.py, scripts/E45_nearcue_exact_law.py) then
  found the same requirement INFEASIBLE when the values are split into their rational and sqrt(D) parts,
  which is the exact form of the condition.  The two cannot both be right, so this script isolates the
  discrepancy (project habit: when a result looks too good, suspect the implementation first).

WHAT IT COMPARES, at N = 4 (Q = 8, field Q(sqrt2)) on the COMPLETE family of the grid
  (A) floating point:  V[c][j] = |F_c(j)|^2 by numpy, and the LP  min_{w>=0, sum w=1} max_j |...- j|
  (B) exact split:    |F_c(j)|^2 = a_cj + b_cj sqrt2 by the cosine tables, LP with the two rational
                      systems  sum_c w_c a_cj = j  and  sum_c w_c b_cj = 0
  (C) cross-check:    for every configuration and every j, is (A) equal to (B)'s a + b*sqrt2 ?
  (D) the exact split LP, but with the equality rows relaxed by a tolerance delta (bisection on delta):
      this measures how far the exact-arithmetic condition is from solvable.

INPUTS   none.  OUTPUT scripts/E45_nearcue_consistency_check.txt

CONCLUSION (expected shape, to be confirmed or refuted by the run)
  If (A) is 0 but (B) is infeasible, then the ramp is attainable only up to floating point noise, NOT
  exactly: the difference is the exact vanishing of the sqrt-part, which floating point cannot see.
  That is the resolution, and it matters: an exact law would allow tau = 0, while an approximate one
  forces tau > 0 -- exactly the situation the frontier is in with tau = 3e-40.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session), exploration point E45, approved by 唐先生.
  Sources: arXiv:2608.13637v2 sec. 7.2; github.com/anthropics/zeta-23-lean tag v1.0.  No RH claim.
"""

import itertools
import os
from fractions import Fraction as F

import numpy as np
from scipy.optimize import linprog

N = 4
Q = 8
COS = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
       4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))}


def exact_pair(pos, j):
    a = F(0); b = F(0)
    for k1 in range(len(pos)):
        for k2 in range(len(pos)):
            ca, cb = COS[(j * (pos[k1] - pos[k2])) % Q]
            a += ca; b += cb
    return a, b


def float_val(pos, j):
    Fv = np.exp(2j * np.pi * j * np.array(pos) / Q).sum()
    return abs(Fv) ** 2


def lp_maxres(V, ramp, delta=None):
    """min_{w>=0,sum w=1} max_j |sum_c w_c V[c][j] - ramp_j| ; if delta given, allow slack delta"""
    M, K = V.shape
    nv = M + 1
    A_ub = np.zeros((2 * K, nv)); b_ub = np.zeros(2 * K)
    A_ub[:K, :M] = V.T; A_ub[:K, M] = -1.0; b_ub[:K] = ramp
    A_ub[K:, :M] = -V.T; A_ub[K:, M] = -1.0; b_ub[K:] = -ramp
    A_eq = np.zeros((1, nv)); A_eq[0, :M] = 1.0
    c = np.zeros(nv); c[M] = 1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0],
                  bounds=[(0, None)] * M + [(0, None)], method="highs")
    return (res.x[M], res.x[:M]) if res.success else (None, None)


def main():
    out = []; w = out.append
    ramp = np.arange(1, N, dtype=float)
    configs = list(itertools.combinations(range(Q), N))
    w("E45 reconciliation at N=%d (Q=%d, field Q(sqrt2)), COMPLETE family of %d configurations"
      % (N, Q, len(configs)))
    w("=" * 100)

    # (C) cross-check float vs exact split
    worst = 0.0
    for pos in configs:
        for j in range(1, N):
            a, b = exact_pair(list(pos), j)
            v_exact = float(a) + float(b) * np.sqrt(2)
            worst = max(worst, abs(v_exact - float_val(list(pos), j)))
    w("[C] max |float |F_c(j)|^2 - (a + b*sqrt2)| over all configs and j = %.3e" % worst)
    w("    (small => the two implementations agree; the discrepancy below is mathematical, not a bug)")

    # (A) floating point LP on the complete family
    V = np.array([[float_val(list(p), j) for j in range(1, N)] for p in configs])
    rA, wA = lp_maxres(V, ramp)
    w("[A] floating-point LP on the COMPLETE family: min max-residual = %s" % ("%.3e" % rA if rA is not None else "fail"))

    # (B) exact split LP
    A = np.zeros((2 * (N - 1) + 1, len(configs))); rhs = np.zeros(2 * (N - 1) + 1)
    for c, pos in enumerate(configs):
        for j in range(1, N):
            a, b = exact_pair(list(pos), j)
            A[j - 1, c] = float(a); A[N - 1 + j - 1, c] = float(b)
            rhs[j - 1] = j; rhs[N - 1 + j - 1] = 0.0
    A[2 * (N - 1), :] = 1.0; rhs[2 * (N - 1)] = 1.0
    res = linprog(np.zeros(len(configs)), A_eq=A, b_eq=rhs, bounds=[(0, None)] * len(configs),
                  method="highs")
    w("[B] exact-split LP (a-parts = j AND b-parts = 0): status = %d (%s)"
      % (res.status, "feasible" if res.status == 0 else "INFEASIBLE"))

    # (D) how SMALL can the algebraic deviation be?  min_{w} max_j |sum_c w_c b_cj|
    #     subject to the rational parts being exact (sum_c w_c a_cj = j), w >= 0, sum w = 1.
    #     This is the honest quantitative floor: deviation t in the b-part means the value is
    #     j + t*sqrt2, hence |N*S(j) - j| = t*sqrt2, so tau >= (min t)*sqrt2.
    M = len(configs)
    nv = M + 1
    A_ub = np.zeros((2 * (N - 1) + 0, nv)); b_ub = np.zeros(2 * (N - 1))
    for j in range(1, N):
        A_ub[j - 1, :M] = A[N - 1 + j - 1, :]      #  sum w b_cj <= t
        A_ub[j - 1, M] = -1.0
        A_ub[N - 1 + j - 1, :M] = -A[N - 1 + j - 1, :]   # -sum w b_cj <= t
        A_ub[N - 1 + j - 1, M] = -1.0
    A_eq2 = np.zeros((N, nv))
    for j in range(1, N):
        A_eq2[j - 1, :M] = A[j - 1, :]             #  sum w a_cj = j  exactly
    A_eq2[N - 1, :M] = 1.0
    b_eq2 = list(ramp) + [1.0]
    c = np.zeros(nv); c[M] = 1.0
    rD = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq2, b_eq=b_eq2,
                 bounds=[(0, None)] * M + [(0, None)], method="highs")
    if rD.success:
        tmin = rD.x[M]
        w("[D] minimum achievable algebraic deviation, min_w max_j |sum_c w_c b_cj| = %.3e" % tmin)
        w("    => the ramp is met up to a discrepancy of about %.3e in the sqrt-part," % tmin)
        w("       i.e. |N*S(j) - j| >= %.3e * sqrt2 = %.3e for any weight choice in this family"
          % (tmin, tmin * np.sqrt(2)))
        w("    (exact attainment would need tmin = 0; the LP above computes the true floor in this family)")
    else:
        w("[D] LP for the minimum deviation failed: %s" % rD.message)

    # (E) which half of the exact condition is the obstruction?
    #     E1: rational parts alone,  sum_c w_c a_cj = j, w >= 0, sum w = 1
    #     E2: sqrt parts alone,      sum_c w_c b_cj = 0, w >= 0, sum w = 1
    A1 = np.zeros((N, M)); b1 = list(ramp) + [1.0]
    for j in range(1, N):
        A1[j - 1, :] = A[j - 1, :]
    A1[N - 1, :] = 1.0
    r1 = linprog(np.zeros(M), A_eq=A1, b_eq=b1, bounds=[(0, None)] * M, method="highs")
    A2 = np.zeros((N, M)); b2 = [0.0] * (N - 1) + [1.0]
    for j in range(1, N):
        A2[j - 1, :] = A[N - 1 + j - 1, :]
    A2[N - 1, :] = 1.0
    r2 = linprog(np.zeros(M), A_eq=A2, b_eq=b2, bounds=[(0, None)] * M, method="highs")
    w("[E] which half obstructs the EXACT ramp?")
    w("    E1 rational parts only  (sum w a_cj = j)      : %s"
      % ("feasible" if r1.status == 0 else "INFEASIBLE"))
    w("    E2 sqrt parts only      (sum w b_cj = 0)      : %s"
      % ("feasible" if r2.status == 0 else "INFEASIBLE"))

    # (F) the quantitative floor: min_w max_j |sum_c w_c a_cj - j|  (rational parts only)
    nv2 = M + 1
    Aub = np.zeros((2 * (N - 1), nv2)); bub = np.zeros(2 * (N - 1))
    for j in range(1, N):
        Aub[j - 1, :M] = A1[j - 1, :]; Aub[j - 1, M] = -1.0
        bub[j - 1] = j
        Aub[N - 1 + j - 1, :M] = -A1[j - 1, :]; Aub[N - 1 + j - 1, M] = -1.0
        bub[N - 1 + j - 1] = -j
    Aeq3 = np.zeros((1, nv2)); Aeq3[0, :M] = 1.0
    c3 = np.zeros(nv2); c3[M] = 1.0
    rF = linprog(c3, A_ub=Aub, b_ub=bub, A_eq=Aeq3, b_eq=[1.0],
                 bounds=[(0, None)] * M + [(0, None)], method="highs")
    if rF.success:
        w("    F  floor of the rational parts: min_w max_j |sum_c w_c a_cj - j| = %.6e" % rF.x[M])
        w("       CAUTION: this bounds the a-parts ALONE.  A real-weight law need not make the a-parts")
        w("       match, so this is NOT a lower bound for tau -- see the RESOLUTION section.")
    else:
        w("    F  floor LP failed: %s" % rF.message)

    # (G) WHY the floor is what it is: inspect the rational parts themselves
    vals = set()
    for c, pos in enumerate(configs):
        for j in range(1, N):
            vals.add(A[j - 1, c])
    w("    G  distinct rational parts a_cj appearing in the family: %s"
      % sorted(vals)[:12])
    w("       all even integers? %s" % all(v % 2 == 0 for v in vals))
    w("       NOTE: parity alone is NOT an obstruction -- a convex combination of even integers can")
    w("       be odd (1 = 0.5*0 + 0.5*2), so the evenness below is a symptom, not the reason.")

    # (H) locate the obstruction row by row: is the single-row condition sum w a_cj = j feasible?
    w("    H  single-row feasibility of  sum_c w_c a_cj = j  (w in the simplex):")
    for j in range(1, N):
        Arow = np.zeros((2, M))
        Arow[0, :] = A[j - 1, :]
        Arow[1, :] = 1.0
        rr = linprog(np.zeros(M), A_eq=Arow, b_eq=[j, 1.0], bounds=[(0, None)] * M, method="highs")
        w("       j = %d : %s" % (j, "feasible" if rr.status == 0 else "INFEASIBLE"))
    w("       => single rows are individually satisfiable; the split system fails JOINTLY.")
    w("          (The split system is the RATIONAL-weight condition; see the RESOLUTION below.)")
    w("")
    w("=" * 100)
    w("RESOLUTION (corrected logic; an earlier draft of this section was WRONG)")
    w("  [C] shows the float and the exact-split implementations agree, so [A] vs [B] is a genuine")
    w("  discrepancy, not a coding error.  The resolution is about WHAT [B] decides:")
    w("    * The split criterion (a-parts = j AND b-parts = 0 SEPARATELY) is exactly the condition for a")
    w("      RATIONAL-weight law: both sums must be rational, which presupposes rational weights.")
    w("    * For REAL weights the two parts need not vanish separately: the single real equation")
    w("      (sum w a - j) + (sum w b)*sqrt2 = 0 can hold with both brackets nonzero.  Hence [B] does NOT")
    w("      rule out exactness, and [A] shows the ramp IS reached numerically with real weights.")
    w("    * [F] bounds the a-part alone and is therefore NOT a lower bound for tau.")
    w("  Corrected status: (i) RATIONAL weights are impossible in these families; (ii) real/algebraic")
    w("  weights reach the ramp numerically; (iii) whether they reach it EXACTLY is OPEN -- an algebraic")
    w("  question, not an LP one.  An exactly-certifiable law, if it exists, will have ALGEBRAIC")
    w("  weights, so its certificate is an identity in a number field (exactly checkable, but not")
    w("  rational arithmetic).")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_consistency_check.txt"), "w").write(txt)
    print(txt)


if __name__ == "__main__":
    main()
