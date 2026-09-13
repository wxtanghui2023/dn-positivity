#!/usr/bin/env python3
"""
E70_slow_region_modulated_geometric.py -- attack the slow-phase region as a modulated geometric series.

THE ATTACK
  In the slow-phase region the phase velocity n*theta'(gamma) is at most one in absolute value, so stationary
  phase and van der Corput give nothing.  Writing the phases in turns and subtracting the mean increment turns the
  sum into a geometric series modulated by the accumulated deviation E_j of the phase increments from their mean.
  The claim to test is that E_j is controlled by the classical, unconditional, POINTWISE bound on the error in the
  zero counting function, S(gamma) << log gamma: since E_j is the phase deviation created by the positional
  discrepancy, E_j is approximately minus the index times the phase derivative times the discrepancy, which at the
  scales of the problem is a times two pi times S over log gamma, hence bounded by a constant.  If that is true, the
  slow-region sum is a geometric series modulated by a bounded, slowly varying factor, and the distance of the mean
  increment from an integer gives a uniform bound.

WHAT IS MEASURED, for sampled indices n
  the slow region gamma >= sqrt(n); the phases in turns; the increments; the mean increment delta;
  the accumulated deviation E_j; its maximum and its total variation; the exact sum over the slow region;
  the pure geometric-series size 1/|delta|; and the classical prediction for the size of E_j.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E70_slow_region_modulated_geometric.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction to attack the slow-phase region.  No RH assumption used or
  claimed; the classical pointwise bound on the counting error is used only as a target of comparison, not assumed;
  numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def main():
    out = []
    out.append("E70 -- the slow-phase region as a modulated geometric series")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T0 = float(g[-1])
    X = T0 * T0
    th = 2.0 * np.arctan(1.0 / (2.0 * g))
    out.append("  N = %d zeros, T0 = %.6f, X = T0^2 = %.6g" % (N, T0, X))
    out.append("")

    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(12) * (X - 0.30 * X)
    out.append("  slow region = zeros with gamma >= sqrt(n); 12 sampled indices")
    out.append("")
    out.append("      n/X      sqrt(n)     #slow      mean delta    1/|delta|    max|E_j|     TV(E)      |sum slow|   |sum|/N")
    for n in ns:
        gs = np.sqrt(n)
        idx = np.searchsorted(g, gs)
        gj = g[idx:]
        ph = n * th[idx:]                      # radians, decreasing in gamma
        d = np.diff(ph) / (2 * np.pi)          # increments in turns (negative)
        delta = float(np.mean(d))
        eps = d - delta
        E = np.concatenate(([0.0], np.cumsum(eps)))
        TV = float(np.sum(np.abs(np.diff(np.exp(2j * np.pi * E))))) / (2 * np.pi)
        s = np.exp(1j * ph).sum()
        out.append("      %-8.4f %-11.6g %-10d %-14.6f %-12.4g %-11.4g %-11.4g %-12.4g %.3e"
                   % (n / X, gs, len(gj), delta, 1.0 / abs(delta), float(np.max(np.abs(E))), TV, abs(s), abs(s) / N))
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  If max|E_j| stays of order one, the classical pointwise bound on the counting error does control the")
    out.append("  accumulated phase deviation, and the slow-region sum is a geometric series modulated by a bounded")
    out.append("  factor; the column 1/|delta| then is the natural uniform bound.  If max|E_j| grows with the region")
    out.append("  length, the modulation is not bounded and the route needs the total variation instead.  The measured")
    out.append("  sum over the slow region is the quantity the whole trigger is about.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E70_slow_region_modulated_geometric.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
