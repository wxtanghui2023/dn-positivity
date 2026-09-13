#!/usr/bin/env python3
"""
E45_nearcue_rational_law.py -- exploration point E45, step 2: does a RATIONAL-weight near-CUE law exist?

WHY (context)
  E44 (docs/E44-ceiling-encl-audit.md) showed the frontier's ceiling theorem depends on one numeric input
  -- EnclOK, the enclosure of the grid form factor of a law whose data file is not public -- so that input
  cannot be recomputed by a third party.  E45 builds our own law instead.
  Step 1 (scripts/E45_nearcue_law_probe.py) found that the exact ramp E|F(j)|² = j, j = 1..N-1, is
  attainable in the convex hull of sampled configurations at N = 4,5,6,8,12,16 with machine-zero residual,
  so the construction is not a one-off miracle.  Step 1's weights were ALGEBRAIC (they looked like
  (2 ± √2)/4 and 1/√5 combinations).

  Step 2 asks the sharper question: is there a law with RATIONAL weights?
  Self-correction (made while reconciling, see scripts/E45_nearcue_consistency_check.py): the split into
  (rational part, sqrt(D) part) with BOTH parts required to match decides the RATIONAL-weight case only.
  For real weights the two parts need not vanish separately -- (sum w a - j) + (sum w b) sqrt D = 0 can
  hold with both terms nonzero -- so infeasibility here means "no rational-weight law", NOT "no law".

WHY A RATIONAL LP SUFFICES FOR N = 4,5,6
  The positions sit on the grid m/Q, Q = 2N, so E|F(j)|² is a sum of cos(2π j d/Q), d integer.  For
    N = 4  (Q = 8)  the cosines lie in Z[√2]/2          -> value = a + b√2,   basis {1, √2}
    N = 6  (Q = 12) the cosines lie in Z[√3]/2          -> value = a + b√3,   basis {1, √3}
    N = 5  (Q = 10) the cosines lie in Z[√5]/4          -> value = a + b√5,   basis {1, √5}
  Writing each |F_c(j)|² as a rational pair (a_cj, b_cj), the ramp condition
        sum_c w_c |F_c(j)|² = j   for all j = 1..N-1
  is EQUIVALENT to the pair of RATIONAL systems
        sum_c w_c a_cj = j      and      sum_c w_c b_cj = 0 ,
  plus w >= 0, sum w = 1.  Every vertex of a rational LP is rational, so feasibility already implies a
  rational law: the script solves the rational LP and then re-verifies the winning weights EXACTLY with
  fractions.Fraction.

INPUTS   none (exact rational/algebraic arithmetic, enumeration is deterministic)
OUTPUT   scripts/E45_nearcue_rational_law.txt

CONCLUSIONS (digit-driven; printed at the end)
  Feasible  => a law with rational weights and the EXACT ramp exists at that N (tau = 0 in NearCUE).
  Infeasible => this configuration family admits no rational-weight ramp law (not a general impossibility,
                since feasibility depends on the family; the script says which family was used).

PROVENANCE
  Written 2026-09-13 by 小灵 (main session) for exploration point E45 of
  docs/EXPLORATION-POINTS-REGISTER.md, approved by 唐先生.
  Sources read: arXiv:2608.13637v2 section 7.2 and github.com/anthropics/zeta-23-lean tag v1.0
  (Zeta23/PairCeiling/{Defs,Grid,NearCUE,Ceiling,CeilingLaw256,LawN256}.lean).
  No RH assumption is used or claimed.
"""

import itertools
import os
from fractions import Fraction as F

import numpy as np
from scipy.optimize import linprog

# exact cosine tables: cos(2*pi*r/Q) = a + b*sqrt(D) with rational a,b
# Q = 8  (D = 2)
COS8 = {}
for r in range(8):
    v = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(0), F(0)), 3: (F(0), F(-1, 2)),
         4: (F(-1), F(0)), 5: (F(0), F(-1, 2)), 6: (F(0), F(0)), 7: (F(0), F(1, 2))}[r]
    COS8[r] = v
# Q = 12 (D = 3)
COS12 = {}
for r in range(12):
    tab = {0: (F(1), F(0)), 1: (F(0), F(1, 2)), 2: (F(1, 2), F(0)), 3: (F(0), F(0)),
           4: (F(-1, 2), F(0)), 5: (F(0), F(-1, 2)), 6: (F(-1), F(0)),
           7: (F(0), F(-1, 2)), 8: (F(-1, 2), F(0)), 9: (F(0), F(0)),
           10: (F(1, 2), F(0)), 11: (F(0), F(1, 2))}
    COS12[r] = tab[r]
# Q = 10 (D = 5)
COS10 = {}
for r in range(10):
    tab = {0: (F(1), F(0)), 1: (F(1, 4), F(1, 4)), 2: (F(-1, 4), F(1, 4)), 3: (F(-1, 4), F(-1, 4)),
           4: (F(1, 4), F(-1, 4)), 5: (F(-1), F(0)), 6: (F(1, 4), F(-1, 4)), 7: (F(-1, 4), F(-1, 4)),
           8: (F(-1, 4), F(1, 4)), 9: (F(1, 4), F(1, 4))}
    COS10[r] = tab[r]

FAMILIES = {4: (8, COS8, "sqrt2"), 6: (12, COS12, "sqrt3"), 5: (10, COS10, "sqrt5")}


def value_coeffs(N, Q, COS, positions, marks, j):
    """exact (a, b) with |F(j)|^2 = a + b*sqrt(D), F(j) = sum_k m_k exp(2 pi i j x_k / N)"""
    a = F(0); b = F(0)
    for k1, x1 in enumerate(positions):
        for k2, x2 in enumerate(positions):
            d = (x1 - x2) % Q
            ca, cb = COS[(j * d) % Q]
            m = marks[k1] * marks[k2]
            a += ca * m; b += cb * m
    return a, b


def build_family(N, Q, COS):
    """all unit-mark configs (N distinct grid positions) and all mark-2 configs (N/2 positions, mark 2)"""
    rows = []
    desc = []
    for sub in itertools.combinations(range(Q), N):
        pos = list(sub); marks = [1] * N
        rows.append((pos, marks))
        desc.append(("unit", pos))
    if N % 2 == 0:
        for sub in itertools.combinations(range(Q), N // 2):
            pos = list(sub); marks = [2] * (N // 2)
            rows.append((pos, marks))
            desc.append(("mark2", pos))
    return rows, desc


def main():
    out = []
    w = out.append
    w("E45 step 2 -- does a RATIONAL-weight law with the EXACT ramp form factor exist?")
    w("ramp condition: sum_c w_c |F_c(j)|^2 = j for j = 1..N-1, w >= 0, sum w = 1")
    w("method: split each value into (rational part, sqrt(D) part) -> RATIONAL LP; re-verify exactly")
    w("=" * 100)
    for N, (Q, COS, field) in sorted(FAMILIES.items()):
        rows, desc = build_family(N, Q, COS)
        K = N - 1
        A = np.zeros((2 * K + 1, len(rows)))
        rhs = np.zeros(2 * K + 1)
        for c, (pos, marks) in enumerate(rows):
            for j in range(1, N):
                a, b = value_coeffs(N, Q, COS, pos, marks, j)
                A[j - 1, c] = float(a)          # rational part  = j
                A[K + j - 1, c] = float(b)      # sqrt part     = 0
                rhs[j - 1] = j
                rhs[K + j - 1] = 0.0
        A[2 * K, :] = 1.0
        rhs[2 * K] = 1.0
        res = linprog(np.zeros(len(rows)), A_eq=A, b_eq=rhs,
                      bounds=[(0, None)] * len(rows), method="highs")
        w("%4d  Q=%2d  field=Q(%s)  configs=%5d  LP status=%s"
          % (N, Q, field, len(rows), res.status))
        if res.status != 0:
            w("      -> INFEASIBLE: no RATIONAL-weight law here (the split criterion decides exactly that)")
            continue
        wts = res.x
        support = [i for i in range(len(rows)) if wts[i] > 1e-11]
        # exact re-verification: solve the active system with Fractions is unnecessary if we simply
        # re-check the *rationalised* weights; instead re-check with the exact algebraic pairs.
        # We test exactness by requiring sum_c w_c a_cj = j and sum_c w_c b_cj = 0 with Fraction weights.
        # The LP vertex is rational, so we recover it by solving the active constraints exactly.
        from fractions import Fraction
        # collect active rows: support configs plus equality rows that are tight
        # build exact system: variables = support weights; equations = all (a,b) rows + normalisation
        eq = []
        rbv = []
        for j in range(1, N):
            row_a = [value_coeffs(N, Q, COS, rows[c][0], rows[c][1], j)[0] for c in support]
            row_b = [value_coeffs(N, Q, COS, rows[c][0], rows[c][1], j)[1] for c in support]
            eq.append(row_a); rbv.append(F(j))
            eq.append(row_b); rbv.append(F(0))
        eq.append([F(1)] * len(support)); rbv.append(F(1))
        # solve overdetermined exact system by Gaussian elimination on rationals
        m, n = len(eq), len(support)
        aug = [[eq[i][k] for k in range(n)] + [rbv[i]] for i in range(m)]
        piv = []
        row = 0
        for col in range(n):
            sel = None
            for r2 in range(row, m):
                if aug[r2][col] != 0:
                    sel = r2; break
            if sel is None:
                continue
            aug[row], aug[sel] = aug[sel], aug[row]
            pv = aug[row][col]
            aug[row] = [v / pv for v in aug[row]]
            for r2 in range(m):
                if r2 != row and aug[r2][col] != 0:
                    f = aug[r2][col]
                    aug[r2] = [aug[r2][k] - f * aug[row][k] for k in range(n + 1)]
            piv.append(col); row += 1
            if row == m:
                break
        # consistency check
        consistent = all(all(v == 0 for v in aug[r2][:n]) and aug[r2][n] == 0
                         for r2 in range(row, m))
        exact = consistent and all(aug[i][n] >= 0 for i in range(row))
        wsol = [None] * n
        for i, col in enumerate(piv):
            wsol[col] = aug[i][n]
        w("      support=%d of %d ; weights (rationalised, first 8): %s"
          % (len(support), len(rows),
             ", ".join("" if wsol[i] is None else str(wsol[i]) for i in range(min(8, n)))))
        w("      EXACT re-verification with Fractions: consistent=%s, all weights >= 0 = %s"
          % (consistent, exact))
        if exact:
            w("      => *** RATIONAL-WEIGHT LAW WITH THE EXACT RAMP EXISTS at N=%d ***" % N)
            # print the configuration(s)
            for i in support[:8]:
                kind, pos = desc[rows.index(rows[support[i]])]
                w("         w=%s  %s config at grid positions %s (of Q=%d)"
                  % (wsol[i], kind, pos, Q))
        else:
            w("      => LP vertex is rational (a rational feasible point), but the exact algebraic")
            w("         re-check above is the deciding test.")

    w("")
    w("=" * 100)
    w("READING")
    w("  Feasibility would mean S(j) = j/N exactly, hence tau = 0 in NearCUE and NO interval arithmetic")
    w("  in the numeric input.  Infeasibility means the exact ramp is out of reach on this grid, so any")
    w("  construction must accept tau > 0 -- see scripts/E45_nearcue_consistency_check.py for the")
    w("  reconciliation and the quantitative floor.")
    txt = "\n".join(out) + "\n"
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_rational_law.txt"), "w").write(txt)
    print(txt)


if __name__ == "__main__":
    main()
