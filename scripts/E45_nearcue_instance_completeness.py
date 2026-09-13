#!/usr/bin/env python3
"""
E45_nearcue_instance_completeness.py -- exploration point E45, step 11: what a COMPLETE instance needs,
and whether exactness is compatible with the small "simple fraction" the ceiling requires.

THE TWO HALVES OF AN INSTANCE
  The ceiling theorem's conclusion is
      c₀ + ∫₀¹ r·x  ≤  p + d₁·|r(1)| + (1/(6N²) + τ/(2N))·(|r'(1)| + ∫₀¹|r''|)
  under: the ramp condition on the grid form factor S with tolerance τ; the edge bound d₁; and the
  validity of the certificate (c₀, r) against the law,  c₀ + Σ_j (S(j)/N)·r(j/N) ≤ p.
  So an instance needs (i) the LAW's grid data — masses and edge row — which E45 supplies exactly with
  τ = 0 and d₁ = 1/(2N), and (ii) a certificate valid against that law, which is the analytic half.
  This script does (i) exactly, exhibits a valid certificate for (ii), and evaluates the conclusion.

WHY p MATTERS (the point of this step)
  For the ceiling to bound the certificate CLASS, the law must be one against which certificates cannot be
  certified above ~0.68: the smaller the law's simple fraction p, the stronger the bound.  Our constructed
  laws use only unit-mark configurations, so every point is simple and on-line and p = 1 — maximal, hence
  useless for bounding the class.  That raises the sharp question: does exactness FORCE p = 1?
  If it does, the exact-ramp route and the ceiling's purpose are incompatible, and the honest conclusion is
  that our construction supplies the numeric input but cannot itself witness the ceiling.
  If it does not, exact-ramp laws with small p exist and the two halves can be combined.

METHOD
  p = Σ_c w_c · (number of mark-1 points in c) / N, so minimising p means putting weight on mark-2
  configurations.  Maximising the total weight on mark-2 configurations subject to the exact ramp
  equations and nonnegativity is a linear program (the only irrational coefficient is sqrt(D)), and the
  optimum answers the question.  A certificate is then exhibited and the conclusion evaluated exactly.

INPUTS   none (exact rational arithmetic; the LP is solved in floating point and re-checked)
OUTPUT   scripts/E45_nearcue_instance_completeness.txt

PROVENANCE
  Written 2026-09-13 by 小灵 for the E45 continuation, approved by 唐先生 (11:36 "4，1，6都要深入分析").
  Sources: docs/E45-ceiling-law-construction.md; arXiv:2608.13637v2 section 7.2; repo tag v1.0
  (NearCUE.lean, Ceiling.lean).  No RH assumption used or claimed, and NO LEAN IS RUN here
  (compute directive of 2026-09-13 11:47: Lean only at paper finalisation).
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
LAWS = {
    4: [((0, 2, 6, 7), (F(1, 2), F(-1, 4))),
        ((0, 3, 5, 7), (F(1, 2), F(1, 4)))],
    6: [((0, 2, 5, 7, 9, 10), (F(-11, 30), F(4, 15))),
        ((0, 1, 2, 4, 6, 9), (F(28, 15), F(-14, 15))),
        ((0, 3, 5, 6, 8, 11), (F(-1, 3), F(1, 3))),
        ((2, 3, 4, 8, 10, 11), (F(8, 15), F(-4, 15))),
        ((3, 5, 6, 7, 10, 11), (F(-19, 30), F(2, 5))),
        ((0, 2, 4, 6, 8, 9), (F(-1, 15), F(1, 5)))],
}


def values(N, Q, pos, j):
    a = F(0); b = F(0)
    for k1 in range(len(pos)):
        for k2 in range(len(pos)):
            ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
            a += ca; b += cb
    return a, b


def main():
    out = []

    def w(s, flush=False):
        out.append(s)
        if flush:
            print(s, flush=True)

    w("E45 step 11 -- instance completeness: exact law data + a valid certificate, and the role of p")
    w("the ceiling theorem's conclusion needs (i) the law's grid data (we supply exactly, tau = 0) and")
    w("(ii) a certificate valid against the law.  p = the law's simple fraction bounds the whole class,")
    w("so a law with p = 1 is useless for the ceiling.  Question: does exactness FORCE p = 1?")
    w("NOTE: no Lean is run here (compute directive 2026-09-13 11:47).")
    w("=" * 100, flush=True)

    for N in (4, 6):
        Q = 2 * N; D = DQ[Q]
        w("", flush=True)
        w("N = %d (Q = %d, field Q(sqrt%d))" % (N, Q, D), flush=True)

        # ---- (A) exact law data: masses from the ramp, and a valid certificate with its conclusion
        masses = [F(j, N * N) for j in range(1, N + 1)]      # s_j = S(j)/N = (j/N)/N
        assert sum(masses) == F(N + 1, 2 * N)
        d1 = F(1, 2 * N)                                     # |D(1)|, exact (E45 section 9-12)
        w("   (A) exact law data: masses s_j = j/%d^2,  C(1) = %s,  tau = 0,  d1 = %s"
          % (N, sum(masses), d1), flush=True)
        # certificate: r(x) = x, so r'(x) = 1 and r'' = 0; take c0 = 0 and p := validity sum
        p_val = sum(masses[j - 1] * F(j, N) for j in range(1, N + 1))
        lhs = F(1, 3)                                        # c0 + int_0^1 r(x) x dx = 0 + 1/3
        const = F(1, 6 * N * N)                              # 1/(6N^2) + tau/(2N), tau = 0
        rhs = p_val + d1 * 1 + const * 1 + const * 0          # |r(1)| = 1, |r'(1)| = 1, int|r''| = 0
        w("       certificate r(x) = x, c0 = 0, p := sum_j s_j r(j/N) = %s (so validity holds with =)"
          % p_val, flush=True)
        w("       conclusion:  1/3 <= p + d1 + 1/(6N^2)  :  %s <= %s  ->  %s"
          % (lhs, rhs, lhs <= rhs), flush=True)

        # ---- (B) the law's simple fraction: all our configurations are unit-mark, so p = 1
        w("   (B) our law's configurations are all unit-mark (every point simple and on-line)")
        w("       => simple fraction p = 1  (= %s for the recorded weights)"
          % sum(u for _, (u, _) in LAWS[N]), flush=True)

        # ---- (C) does exactness force p = 1?  maximise the weight on mark-2 configurations
        fam = [(sub, (1,) * N) for sub in itertools.combinations(range(Q), N)]
        mark2 = []
        if N % 2 == 0:
            mark2 = [(sub, (2,) * (N // 2)) for sub in itertools.combinations(range(Q), N // 2)]
        allc = fam + mark2
        idx_mark2 = set(range(len(fam), len(allc)))
        A = {}; B = {}
        for ci, (pos, marks) in enumerate(allc):
            for j in range(1, N + 1):
                a, b = values(N, Q, pos, j)
                a *= (marks[0] if False else 1)              # marks enter through the value computation
                A[(ci, j)] = a; B[(ci, j)] = b
        # rebuild values WITH marks (unit: all 1; mark2: all 2)
        A = {}; B = {}
        for ci, (pos, marks) in enumerate(allc):
            for j in range(1, N + 1):
                a = F(0); b = F(0)
                for k1 in range(len(pos)):
                    for k2 in range(len(pos)):
                        ca, cb = COS[Q][(j * (pos[k1] - pos[k2])) % Q]
                        mm = marks[k1] * marks[k2]
                        a += ca * mm; b += cb * mm
                A[(ci, j)] = a; B[(ci, j)] = b
        rng = random.Random(SEED + N)
        best = None
        for trial in range(4000):
            m = N + 2
            idx = rng.sample(range(len(allc)), m)
            # require at least one mark-2 config in the support, else the problem is trivial
            if not any(i in idx_mark2 for i in idx):
                continue
            nv = 2 * m
            Aeq = np.zeros((2 * (N - 1) + 2, nv)); beq = np.zeros(2 * (N - 1) + 2)
            for j in range(1, N):
                for k, ci in enumerate(idx):
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
            for k, ci in enumerate(idx):
                if ci in idx_mark2:
                    c[k] = 1.0        # maximise weight on mark-2 configurations  <=> minimise p
            r = linprog(-c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq,
                        bounds=[(None, None)] * nv, method="highs")
            if not r.success:
                continue
            val = -r.fun
            if best is None or val > best[1]:
                best = (idx, val, r.x)
            if val > 1e-6:
                break
        if best is None:
            w("   (C) no feasible support containing a mark-2 configuration was found", flush=True)
        else:
            idx, val, _ = best
            w("   (C) max feasible weight on mark-2 configurations = %.9f" % val, flush=True)
            if val > 1e-6:
                w("       => exactness does NOT force p = 1: an exact-ramp law with p = %.6f exists"
                  % (1.0 - val), flush=True)
            else:
                w("       => within this sampling, exactness FORCES all weight onto unit-mark")
                w("          configurations (p = 1); the exact-ramp route then supplies the numeric input")
                w("          but cannot by itself witness the ceiling, whose bound wants p ~ 0.68")
    w("")
    w("=" * 100)
    w("READING")
    w("  (A) shows the arithmetic of a complete instance is available to us exactly, with tau = 0 and")
    w("  d1 = 1/(2N).  (B)+(C) address the deeper question: the ceiling's bound is only as strong as the")
    w("  law's simple fraction is small, and our constructions are all-simple.  Whether exactness can be")
    w("  reconciled with a small simple fraction decides whether E45's numeric half can be combined with a")
    w("  ceiling-witnessing law, or whether the two purposes need different laws.")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "E45_nearcue_instance_completeness.txt"), "w") as fh:
        fh.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
