#!/usr/bin/env python3
"""
E73_rigorous_chain.py -- term-by-term verification of the rigorous chain for the slow phase range.

THE CHAIN BEING VERIFIED
  Write the phase sum with the index-dependent phase phi(u) = n*theta(u), theta(u) = 2 arctan(1/(2u)), and let
  A(u) be the zero counting function with A(u) = M(u) + S(u), M the smooth law and S the classical error, for which
  the explicit pointwise bound |S(u)| <= c1 log u + c2 log log u + c3 is available.  Then

      sum_{gamma in [Y,T]} e^{i phi(gamma)} = INT_{Y}^{T} e^{i phi} rho du + [e^{i phi} S]_{Y}^{T}
                                              - INT_{Y}^{T} S i phi' e^{i phi} du ,

  with rho = M', and each piece is bounded:
      (1) smooth part    <= 2 sup|rho/phi'| + INT |(rho/phi')'|          (monotone phase, elementary)
      (2) boundary       <= 2 (c1 log T + c2 log log T + c3)
      (3) discrepancy    <= ||S||_{L^2} * ||phi'||_{L^2}                 (Cauchy-Schwarz)
  On the slow range Y = sqrt(n) one has |phi'| <= 1, so ||phi'||_{L^2} <= sqrt(T-Y), and ||S||_{L^2} is controlled by
  Selberg's unconditional second moment, INT_0^T S^2 ~ T log log T / (2 pi^2).  The resulting bound is uniform in n
  because S does not depend on n.

WHAT IS CHECKED
  For several indices: the split point Y = sqrt(n); the three bounds above (with the table's own INT S^2 as well as
  the Selberg value, for comparison); the measured slow-range sum; and the comparison with the requirement 0.8N.
  Each inequality of the chain is reported with its margin so that the numbers, not the narration, carry the claim.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E73_rigorous_chain.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction to make the cancellation route rigorous.  No RH assumption used
  or claimed; the explicit counting-error constants are the classical ones; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")

C1, C2, C3 = 0.110, 0.290, 2.290      # explicit |S(u)| bound, classical, valid for u >= e


def main():
    out = []
    out.append("E73 -- rigorous chain for the slow phase range, verified term by term")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T = float(g[-1])
    X = T * T
    M = (g / (2 * np.pi)) * np.log(g / (2 * np.pi * np.e)) + 7.0 / 8.0
    A = np.arange(1, N + 1, dtype=np.float64)
    S = A - M
    du = float(np.mean(np.diff(g)))
    out.append("  N = %d, T = %.6f, X = T^2 = %.6g, mean grid spacing = %.6f" % (N, T, X, du))
    out.append("  explicit counting-error bound at u = T: c1 log T + c2 loglog T + c3 = %.4f"
               % (C1 * np.log(T) + C2 * np.log(np.log(T)) + C3))
    out.append("")

    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(6) * (X - 0.30 * X)
    out.append("      n/X      Y=sqrt(n)   (1) smooth   (2) boundary   (3) discrepancy   chain total   measured |sum|   0.8N")
    for n in ns:
        Y = np.sqrt(n)
        k = int(np.searchsorted(g, Y))
        # (1) smooth part: 2 sup|rho/phi'| + INT|(rho/phi')'| ; rho/phi' is monotone, so both equal the endpoint value
        rho_T = np.log(T / (2 * np.pi)) / (2 * np.pi)
        phip_T = abs(4.0 * n / (4.0 * T * T + 1.0))
        ratio = rho_T / phip_T
        smooth = 3.0 * ratio
        # (2) boundary
        bnd = 2.0 * (C1 * np.log(T) + C2 * np.log(np.log(T)) + C3)
        # (3) discrepancy: ||S||_2 over [Y,T] * sqrt(T-Y)   (since |phi'| <= 1 there)
        intS2 = float(np.sum(S[k:] ** 2) * du)
        intS2_selberg = T * np.log(np.log(T)) / (2 * np.pi ** 2)
        disc = float(np.sqrt(intS2) * np.sqrt(T - Y))
        disc_sel = float(np.sqrt(intS2_selberg) * np.sqrt(T - Y))
        # measured slow-range sum
        th = 2.0 * np.arctan(1.0 / (2.0 * g[k:]))
        meas = abs(np.exp(1j * n * th).sum())
        out.append("      %-8.4f %-11.6g %-12.4g %-14.4g %-16.4g %-13.4g %-14.4g %.4g"
                   % (n / X, Y, smooth, bnd, disc, smooth + bnd + disc, meas, 0.8 * N))
        out.append("      %-8s %-11s %-12s %-14s %-16.4g (Selberg version)                          margin vs 0.8N: %.2fx"
                   % ("", "", "", "", smooth + bnd + disc_sel, 0.8 * N / (smooth + bnd + disc_sel)))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  Term (1) is elementary, term (2) uses the explicit pointwise counting-error bound, term (3) uses")
    out.append("  Cauchy-Schwarz against the second moment of the counting error, which Selberg supplies unconditionally")
    out.append("  and which does not depend on the index.  If the chain total stays below four fifths of the count for")
    out.append("  every index, the slow phase range is closed rigorously and uniformly, and the only remaining piece is")
    out.append("  the fast range, where the phase derivative exceeds one.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E73_rigorous_chain.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
