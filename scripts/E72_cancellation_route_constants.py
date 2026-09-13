#!/usr/bin/env python3
"""
E72_cancellation_route_constants.py -- check the constants of a cancellation route that needs no pointwise input.

THE ROUTE
  The phase sum is split against the smooth counting law.  The smooth-density part is bounded by integration by
  parts against a monotone phase, giving a constant.  The discrepancy part is bounded by Cauchy-Schwarz against the
  second moment of the counting error, which Selberg's central limit theorem supplies unconditionally, and whose
  bound does NOT depend on the index n because the counting error is a fixed function of the ordinate while n only
  enters the weight.  That is what would make the bound uniform in the index without any pointwise rigidity input,
  which is the opposite of what an earlier note in this project concluded.

WHAT IS CHECKED
  For the two-million-zero table: the counting error S(u) = A(u) - M(u) with M the smooth counting law; its second
  moment over the whole range and over the slow ranges for several indices; the Cauchy-Schwarz bound for the
  discrepancy part on each slow range; the closed-form bound for the smooth-density part; and the requirement,
  which is four fifths of the count.  The measured slow-region sums from the earlier step are repeated for
  comparison.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E72_cancellation_route_constants.txt

PROVENANCE
  Written 2026-09-13 by 小灵 immediately after 唐先生 observed that cancellation should be treatable.  No RH
  assumption used or claimed; Selberg's second moment is used only as a target of numerical comparison; NO LEAN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def main():
    out = []
    out.append("E72 -- constants of the cancellation route that would need no pointwise input")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T0 = float(g[-1])
    X = T0 * T0
    # smooth counting law and the counting error on the zero grid
    M = (g / (2 * np.pi)) * np.log(g / (2 * np.pi * np.e)) + 7.0 / 8.0
    A = np.arange(1, N + 1, dtype=np.float64)
    S = A - M
    out.append("  N = %d, T0 = %.6f, X = T0^2 = %.6g" % (N, T0, X))
    out.append("  counting error S: sup = %.4f, rms over the table = %.4f, classical scale log T0 = %.4f"
               % (float(np.max(np.abs(S))), float(np.sqrt(np.mean(S ** 2))), float(np.log(T0))))
    seg = np.diff(g)
    out.append("  mean gap = %.6f, min gap = %.6f, max gap = %.6f" % (float(np.mean(seg)), float(np.min(seg)), float(np.max(seg))))
    out.append("")

    out.append("      n/X     range length    int S^2 (table)   CS bound      smooth-part bound   total bound    0.8N")
    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(6) * (X - 0.30 * X)
    for n in ns:
        gs = np.sqrt(n)
        k = int(np.searchsorted(g, gs))
        S_slow = S[k:]
        intS2 = float(np.sum(S_slow ** 2) * np.mean(seg))
        L_slow = float(T0 - gs)
        cs = float(np.sqrt(intS2) * np.sqrt(L_slow))       # (int S^2)^{1/2} (int |phi'|^2)^{1/2}, |phi'|<=1
        a = n / X
        smooth = 2 * float(np.log(T0 / (2 * np.pi)) / (2 * np.pi)) / (4 * n / (4 * T0 ** 2 + 1))
        total = cs + smooth + 4 * float(np.log(T0))        # + boundary terms at the classical scale
        out.append("      %-7.4f %-15.6g %-17.4g %-13.4g %-19.4g %-15.4g %.4g"
                   % (n / X, L_slow, intS2, cs, smooth, total, 0.8 * N))
    out.append("")
    out.append("  reference: measured slow-region sums earlier were between 0.77 and 181")
    out.append("  Selberg target for the whole range: T0*log(log T0)/(2 pi^2) = %.4g, table value = %.4g"
               % (T0 * np.log(np.log(T0)) / (2 * np.pi ** 2), float(np.sum(S ** 2) * float(np.mean(seg)))))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  The route is viable if the total bound stays below four fifths of the count for every index, with")
    out.append("  the Cauchy-Schwarz term carrying the discrepancy and the smooth part carried by monotone-phase")
    out.append("  integration by parts.  The margin, not the truth, decides: even a crude bound suffices if it is")
    out.append("  uniform in the index.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E72_cancellation_route_constants.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
