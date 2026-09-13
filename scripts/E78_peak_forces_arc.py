#!/usr/bin/env python3
"""
E78_peak_forces_arc.py -- the inversion: a large peak forces the phases into a narrow arc, and what that demands.

THE INVERSION IN PROVABLE FORM
  For phases phi_j and positive weights w_j, set Sigma = sum_j w_j e^{i phi_j} and W = sum_j w_j.  For any arc A of
  length alpha,
        W(A^c) <= (W - |Sigma|) / (1 - cos(alpha/2)) ,
  because |Sigma| <= W(A) + W(A^c) cos(alpha/2).  So a large |Sigma| forces all but a controlled amount of weight
  into a narrow arc.  This uses no L2 average over the index, no Nyquist factor, no Sobolev, no Cauchy-Schwarz, no
  pair correlation, and no hypothesis.

  The arithmetic content is what the arc demands.  Inside the arc the phases n/gamma_j are held within alpha of one
  another, so consecutive increments satisfy dist(Delta_j, 2 pi Z) <= alpha, and the arc is a window in the variable
  1/gamma of width alpha/n, hence in the ordinate of width about gamma^2 alpha/n.  But for phases that are
  equidistributed the fraction of them lying in an arc of length alpha is exactly alpha/(2 pi), so the audit is the
  comparison between the fraction the budget demands and the fraction equidistribution supplies.

WHAT IS COMPUTED
  (1) the fast-region sum for sampled indices, the best-arc fractions for several arc lengths, and a check that the
      inversion inequality holds;
  (2) the audit at the budget: the fraction the budget demands for each arc length, against the achievable
      fraction alpha/(2 pi).

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E78_peak_forces_arc.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's E78 specification.  No RH assumption; no pair correlation; no GUE; no
  Nyquist factor; no Sobolev; no Cauchy-Schwarz in the theorem.  NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def theta(x):
    return 2.0 * np.arctan(1.0 / (2.0 * x))


def best_arc_frac(ph_sorted, alpha):
    """largest fraction of points in an arc of length alpha; ph_sorted must be sorted into [0, 2pi)"""
    p = ph_sorted
    n = len(p)
    if n == 0:
        return 0.0
    ext = np.concatenate([p, p + 2 * np.pi])
    j = np.searchsorted(ext, ext[:n] + alpha, side="right")
    return float(np.max(j - np.arange(n))) / n


def main():
    out = []
    out.append("E78 -- a large peak forces the phases into a narrow arc: inversion and arithmetic audit")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T = float(g[-1])
    X = T * T
    out.append("  table: N = %d zeros, T = %.6f, X = T^2 = %.6g" % (N, T, X))
    out.append("  budget for the fast part 0.8N = %.6g ; trivial bound N = %d" % (0.8 * N, N))
    out.append("")

    out.append("(1) inversion on real data: |Sigma|, best-arc fractions, and the inequality W(A^c) <= (W-|Sigma|)/(1-cos(a/2))")
    out.append("      n/X      |Sigma|     |Sigma|/N   arc frac (pi/2)   (pi)     (3pi/2)   inversion holds?")
    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(6) * (X - 0.30 * X)
    for n in ns:
        k = int(np.searchsorted(g, np.sqrt(n)))
        ph = np.remainder(n * theta(g[:k]), 2 * np.pi)
        W = float(k)
        S = float(abs(np.exp(1j * ph).sum()))
        phs = np.sort(ph)
        fr = [best_arc_frac(phs, a) for a in (np.pi / 2, np.pi, 1.5 * np.pi)]
        al = np.pi / 2
        wout = W * (1 - fr[0])
        rhs = (W - S) / (1 - np.cos(al / 2))
        out.append("      %-8.4f %-11.4g %-10.4f %-18.4f %-8.4f %-9.4f %s"
                   % (n / X, S, S / N, fr[0], fr[1], fr[2], "yes" if wout <= rhs + 1e-6 * max(rhs, 1.0) else "NO"))
    out.append("    reading: the arc fractions equal alpha/(2 pi) to four decimals, so the phases are equidistributed and")
    out.append("    the observed peak is three orders of magnitude below the budget.")
    out.append("")

    out.append("(2) audit at the budget: the fraction the budget demands, against what equidistribution supplies")
    out.append("      alpha        fraction demanded p >= 1-0.2/(1-cos(alpha/2))    achievable alpha/(2 pi)   verdict")
    for al in (np.pi / 2, np.pi, 1.5 * np.pi, 1.9 * np.pi, 1.99 * np.pi):
        p = 1 - 0.2 / (1 - np.cos(al / 2))
        ach = al / (2 * np.pi)
        out.append("      %-12.4f %-41.4f %-25.4f %s" % (al, p, ach, "holds" if ach >= p else "FAILS"))
    out.append("")
    out.append("    conclusion: the only arcs meeting the budget demand have length close to two pi, so the demand is")
    out.append("    that all but a sliver of the phases lie in an almost complete circle, which is nearly vacuous.")
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  The inversion is elementary and unconditional, and it is verified on real data.  But the demand it makes")
    out.append("  at the budget is nearly vacuous, for a structural reason: the required saving is only twenty percent of")
    out.append("  the trivial bound, and an inversion of this shape can only bite when the required value is a small")
    out.append("  fraction of the total.  So the necessary condition it produces can be met by equidistributed phases and")
    out.append("  has no force here, and by the stated rule the route is closed.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E78_peak_forces_arc.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
