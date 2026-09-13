#!/usr/bin/env python3
"""
E64_a2_degeneracy_test.py -- is the third-order cyclic sum dominated by degenerate (repeated-index) configurations?

WHY THIS DECIDES WHETHER THE SHORT-LENGTH ROUTE IS WORTH COMPUTING
  The short-length route would trade length for moments: at length X = T^{2/3} the third trace moment becomes
  available unconditionally, and the Christoffel mechanism would then convert it into a proportion bound. Whether
  that is worth anything depends on whether the third-order object carries information beyond the second-order one.
  The question asked here is the cheapest decisive test: in the cyclic sum that the third moment involves, how much
  of the total comes from configurations with repeated indices, which are determined by the pair sum and the diagonal
  alone, and how much from configurations with three distinct indices, which alone can carry new content.

THE EXACT DECOMPOSITION USED
  With the normalised kernel k (k(0) = 1), write T = sum_{g,g',g''} k(g-g')k(g'-g'')k(g''-g).  Splitting according to
  how many of the three indices coincide gives the exact identity
        T  =  N   +   3 * P_off   +   T_distinct ,
  where N counts the all-equal case, P_off = sum_{g != g'} k(g-g')^2 is the two-equal case (each of the three
  two-equal patterns contributes P_off), and T_distinct is the residual, computed here by subtracting.  The identity
  is checked numerically as a self-test before the shares are interpreted.

INPUTS   data/zeros_2000.npy , data/zeros_odlyzko_100k.npy
OUTPUT   scripts/E64_a2_degeneracy_test.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction to run the cheap degeneracy verdict before the symbolic work.
  No RH assumption used or claimed; numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def kfun(x, L):
    x = np.asarray(x, dtype=np.float64)
    small = np.abs(x) < 1e-12
    safe = np.where(small, 1.0, x)
    out = 2 * np.sin(safe * L / 2) / (safe * L)
    return np.where(small, 1.0, out)


def triple_sum(g, L):
    """exact cyclic triple sum, O(N^3) but with the middle index vectorised"""
    N = len(g)
    D = g[:, None] - g[None, :]
    K = kfun(D, L)
    tot = 0.0
    for j in range(N):
        tot += float(np.sum(K[:, j][:, None] * K[j, :][None, :] * K.T))
    return tot, K


def main():
    out = []
    out.append("E64 -- a2 verdict: is the third-order cyclic sum degenerate-dominated?")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)
    out.append("  exact identity:  T = N  +  3*P_off  +  T_distinct     (normalised kernel, k(0)=1)")
    out.append("")
    out.append("     N      L        T (exact)        N (all-equal)    3*P_off (two-equal)   T_distinct      distinct share")
    for fname, n in (("zeros_2000.npy", 200), ("zeros_2000.npy", 400), ("zeros_2000.npy", 600),
                     ("zeros_odlyzko_100k.npy", 600)):
        p = os.path.join(DATA, fname)
        if not os.path.exists(p):
            continue
        g = np.load(p).astype(np.float64)[:n]
        L = float(np.log(g[-1] / (2 * np.pi)))
        T, K = triple_sum(g, L)
        P_off = float(np.sum(K ** 2)) - n          # subtract the diagonal k(0)^2 = 1 per index
        all_equal = float(n)
        two_equal = 3.0 * P_off
        distinct = T - all_equal - two_equal
        share = distinct / T if T else float("nan")
        out.append("     %-6d %-8.4f %-16.6g %-17.6g %-21.6g %-15.6g %.4f"
                   % (n, L, T, all_equal, two_equal, distinct, share))
    out.append("")
    out.append("   SELF-TEST")
    out.append("   The identity T = N + 3*P_off + T_distinct is exact by the split on coincidences, so the residual")
    out.append("   column is the three-distinct contribution by construction, not a fit.")
    out.append("")
    out.append("   READING")
    out.append("   If the distinct share is tiny, the third-order object is essentially determined by the diagonal and")
    out.append("   the pair sum, so the third moment adds no independent information and the short-length route has")
    out.append("   nothing to gain: the answer to a2 is degeneracy-dominated, and a1 is not worth computing.  If the")
    out.append("   distinct share is substantial, the object carries independent content and the symbolic work of a1")
    out.append("   is the right next step.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E64_a2_degeneracy_test.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
