#!/usr/bin/env python3
"""
E45_nearcue_law_probe.py -- exploration point E45, step 1: feasibility probe for a near-CUE law

OBJECT (why this exists)
  The frontier's bandwidth-one ceiling (arXiv:2608.13637v2 section 7.2) rests on the hypothesis EnclOK,
  which certifies that the GRID FORM FACTOR of a specific 256-periodic marked law lies in a recorded
  table of enclosures.  E44 showed that table is public but the LAW is not, so that single input cannot
  be recomputed by a third party (docs/E44-ceiling-encl-audit.md).

  E45 attacks the gap from our side: build our OWN law, with data we can certify exactly.
  The key structural fact, read from the public Lean source this session, is that the ceiling theorem is
  PARAMETRIC in N:

    Zeta23.PairCeiling.ceiling_nearCUE (hN : 0 < N) (S : N -> R) {tau d1 : R}
        (hτ : 0 ≤ tau) (hS : NearCUE S N tau) (hD1 : |Dfun (massOf S N) N 1| ≤ d1) ... :
        c₀ + ∫₀¹ r·x ≤ p + d₁|r(1)| + (1/(6N²) + tau/(2N))(|r'(1)| + ∫|r''|)

  and NearCUE is exactly the ramp condition  |N·S(j) − j| ≤ tau  for 0 < j < N.  So if we exhibit a law
  whose grid form factor is EXACTLY S(j) = j/N on j = 1..N−1, then tau = 0 and the single numeric input
  becomes pure rational arithmetic — the interval arithmetic disappears entirely.

PROBLEM, MADE FINITE
  A law = finite mixture of "marked 256-periodic configurations": positions x ∈ [0,N) rational, marks
  m ∈ {1,2}, with sum of marks = N per configuration; the grid form factor is
      S(j) = (1/N) * E|F(j)|²,     F(j) = sum_k m_k exp(2πi j x_k / N) .
  Requirement:  E|F(j)|² = j  exactly,  for j = 1..N−1.
  This is a linear feasibility problem for the weights w:  sum_c w_c |F_c(j)|² = j, w ≥ 0, sum w = 1.
  This script probes whether the ramp vector lies in the convex hull of sampled configurations for small
  N, by minimising the worst residual with an LP.  A residual at machine level means: a law exists in the
  sampled hull (sufficient, since sampling only shrinks the hull).  A large residual means this sampling
  did not find one (necessary conditions are NOT violated by that alone).

INPUTS   none (self-contained arithmetic).  Sampling is seeded for reproducibility.
OUTPUT   scripts/E45_nearcue_law_probe.txt

CONCLUSIONS (see the printed report; digit-driven)
  Reported per N: best worst-residual, whether it is at machine level, and the corresponding structure.
  Interpretation of a machine-level residual: the exact ramp is attainable in the sampled hull, so an
  exactly-certifiable law exists at that scale, and the residual is limited by floating point only.

PROVENANCE
  Written 2026-09-13 by 小灵 (main session) for exploration point E45 of
  docs/EXPLORATION-POINTS-REGISTER.md, approved by 唐先生 (2026-09-13).
  Sources read: arXiv:2608.13637v2 section 7.2 and github.com/anthropics/zeta-23-lean tag v1.0
  (Zeta23/PairCeiling/{Defs,Grid,NearCUE,Ceiling,CeilingLaw256,LawN256}.lean).
  No RH assumption is used or claimed.
"""

import numpy as np
from scipy.optimize import linprog

N_LIST = [4, 5, 6, 8, 12, 16]
M_SAMPLE = 4000                    # configurations sampled per N
SEED = 20260913


def configs_unit_marks(N, Q, M, rng):
    """M configurations: N distinct positions on the grid m/Q (x/N = m/Q), all marks 1 (sum = N)."""
    V = np.empty((M, N - 1))
    P = np.empty((M, N), dtype=int)
    for c in range(M):
        pos = rng.choice(Q, size=N, replace=False)
        P[c] = pos
        F = np.exp(2j * np.pi * np.outer(np.arange(1, N), pos) / Q).sum(axis=1)   # F(j), j=1..N-1
        # keep |F|² only (marks all 1)
        V[c] = np.abs(F) ** 2
    return V, P


def configs_mark2(N, Q, M, rng):
    """M configurations: N/2 distinct positions with mark 2 (sum of marks = N)."""
    V = np.empty((M, N - 1))
    P = np.empty((M, N // 2), dtype=int)
    for c in range(M):
        pos = rng.choice(Q, size=N // 2, replace=False)
        P[c] = pos
        F = 2.0 * np.exp(2j * np.pi * np.outer(np.arange(1, N), pos) / Q).sum(axis=1)
        V[c] = np.abs(F) ** 2
    return V, P


def best_residual(V, ramp):
    """min over w>=0, sum w =1 of max_j |(V^T w)_j - ramp_j|  (LP)"""
    M, K = V.shape
    # variables: w (M), t ; minimise t
    A_ub = np.zeros((2 * K + 0, M + 1))
    b_ub = np.zeros(2 * K)
    A_ub[:K, :M] = V.T
    A_ub[:K, M] = -1.0
    b_ub[:K] = ramp
    A_ub[K:, :M] = -V.T
    A_ub[K:, M] = -1.0
    b_ub[K:] = -ramp
    A_eq = np.zeros((1, M + 1))
    A_eq[0, :M] = 1.0
    b_eq = np.array([1.0])
    bounds = [(0, None)] * M + [(0, None)]
    c = np.zeros(M + 1)
    c[M] = 1.0
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
    if not res.success:
        return None, None, res.message
    return res.x[M], res.x[:M], "ok"


def main():
    out = []
    w = out.append
    rng = np.random.default_rng(SEED)
    w("E45 step 1 -- feasibility probe: does a law with EXACTLY the ramp form factor exist?")
    w("target: E|F(j)|² = j for j = 1..N-1  (this is exactly what NearCUE with tau = 0 demands)")
    w("criterion: LP min over w>=0, sum w=1 of max_j |sum_c w_c|F_c(j)|² - j|")
    w("positions live on the grid m/Q with Q = 2N, i.e. x = N*m/Q; unit-mark configs have N points,")
    w("mark-2 configs have N/2 points (both have sum of marks = N).")
    w("=" * 100)
    w("%5s %6s %8s %14s %14s %10s  %s" % ("N", "Q", "configs", "residual(A)", "residual(B)", "ramp avg", "verdict"))
    for N in N_LIST:
        Q = 2 * N                                  # positions on the grid m/Q, m = 0..Q-1
        ramp = np.arange(1, N, dtype=float)
        V1, P1 = configs_unit_marks(N, Q, M_SAMPLE, rng)
        r1, w1, msg1 = best_residual(V1, ramp)
        V2 = None
        P2 = None
        r2 = None
        if N % 2 == 0:
            V2, P2 = configs_mark2(N, Q, M_SAMPLE, rng)
            r2, w2, msg2 = best_residual(V2, ramp)
        # combine both families in one hull as well
        fam = [V1] + ([V2] if V2 is not None else [])
        Vc = np.vstack(fam)
        rc, wc, msgc = best_residual(Vc, ramp)
        tag = ""
        if rc is not None:
            tag = "EXACT-at-machine-level" if rc < 1e-9 else ("close" if rc < 1e-3 else "far")
        w("%5d %6d %8d %14s %14s %10.2f  %s"
          % (N, Q, 2 * M_SAMPLE if r2 is not None else M_SAMPLE,
             ("%.3e" % r1) if r1 is not None else "LP-fail",
             ("%.3e" % r2) if r2 is not None else "-",
             ramp.mean(),
             ("combined: %.3e  -> %s" % (rc, tag)) if rc is not None else "combined LP fail"))
        if rc is not None and rc < 1e-9:
            support = np.where(wc > 1e-12)[0]
            w("          combined hull attains the ramp; support size = %d of %d configurations"
              % (len(support), Vc.shape[0]))
            w("          weights (first 6 non-zeros): %s"
              % ", ".join("%.12f" % wc[i] for i in support[:6]))
            # print the WINNING configurations (positions on the grid m/Q, x = N*m/Q)
            rows = [("unit", P1[i], [1] * N) for i in range(len(P1))]
            if P2 is not None:
                rows += [("mark2", P2[i], [2] * (N // 2)) for i in range(len(P2))]
            for i in support[:6]:
                kind, pos, mk = rows[i]
                w("            w=%.12f  %s: grid positions %s of Q=%d (x = N*m/Q)"
                  % (wc[i], kind, list(map(int, pos)), Q))
    w("")
    w("=" * 100)
    w("READING OF THE TABLE")
    w("  residual at 1e-15 level => the ramp is attainable in the sampled hull (sufficient for existence)")
    w("  residual O(1)            => this sampling did not find a law (NOT a proof of non-existence:")
    w("                              the sampled hull is only a subset of the true one)")
    w("  A machine-level hit makes the numeric input of the ceiling theorem exact rational data with")
    w("  tau = 0, i.e. NO interval arithmetic anywhere -- which is the whole point of E45.")
    txt = "\n".join(out) + "\n"
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    open(os.path.join(here, "E45_nearcue_law_probe.txt"), "w").write(txt)
    print(txt)


if __name__ == "__main__":
    main()
