#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""level-m subspace LP bound for binary covering codes K(n,1) (R=1).

## 仅用于回测研究，不包含实盘下单逻辑

Background (archive): MCOVER-2026-09-26 (exact reconstruction of the Östergård–Blass
style "M-covering system" for n=9, R=1) and ASSETS-REGISTRY C-429 (n=10 generalization
A_ii = n+1-m).

Setup (prefix-cell partition): fix the first m coordinates.  Cells are indexed by the
prefix x in F_2^m, so t = 2^m cells, each with s = 2^(n-m) words.
Let y_i = |C ∩ cell_i|.  A codeword c in cell i covers:
  - n+1-m words inside cell i  (c itself + b=c⊕e_j for j>m),
  - exactly 1 word in each cell j with d(prefix_i, prefix_j) = 1,
  - 0 words in cells at prefix-distance >= 2.
Hence the "level-m M-covering system":
    sum_j A_ji y_j >= s  for all i,   A_ii = n+1-m, A_ij = 1[d(i,j)=1], A_ij = 0 (d>=2)
    0 <= y_i <= s,      sum_i y_i = M
Any covering code of size M yields a feasible integral y, so
    L(m) := min { sum_i y_i : A^T y >= s*1, 0 <= y <= s }
is a valid lower bound on K(n,1)  (LP relaxation; no integrality used here).

Aggregated bound (always available): summing the t constraints gives
    (n+1) * sum_i y_i >= t*s = 2^n   =>   L(m) >= 2^n/(n+1)  (= volume/sphere bound).
So the interesting quantity is the *refinement gain*  L(m) - 2^n/(n+1).

Output: for n = 9 and n = 10, a table of L(m) vs m (the "capability test" curve).
"""
import numpy as np
from scipy.optimize import linprog


def build_A(n: int, m: int) -> np.ndarray:
    """A_ii = n+1-m ; A_ij = 1 iff prefixes differ in exactly one coordinate."""
    t = 1 << m
    A = np.zeros((t, t), dtype=float)
    for i in range(t):
        A[i, i] = float(n + 1 - m)
        for b in range(m):
            A[i, i ^ (1 << b)] = 1.0
    return A


def lp_bound(n: int, m: int):
    """Return (L(m), status, message).  Constraints: A^T y >= s, bounds [0,s]."""
    t = 1 << m
    s = float(1 << (n - m))
    A = build_A(n, m)
    res = linprog(
        c=np.ones(t),
        A_ub=-A.T,
        b_ub=-np.full(t, s),
        bounds=[(0.0, s)] * t,
        method="highs",
    )
    return res.fun, res.status, res.message


def main():
    for n in (9, 10):
        vol = (1 << n) / (n + 1)
        print("=" * 78)
        print(f"n = {n}   volume/sphere bound 2^n/(n+1) = {vol:.6f}")
        print(f"{'m':>3} {'t=2^m':>7} {'s=2^(n-m)':>10} {'L(m)':>14} "
              f"{'L(m)-vol':>12} {'status':>7}")
        for m in range(1, n + 1):
            if (1 << m) > 2048:
                break
            try:
                val, st, msg = lp_bound(n, m)
            except Exception as exc:  # pragma: no cover
                print(f"{m:>3} {'-':>7} {'-':>10} {'EXC':>14} {'-':>12} "
                      f"{type(exc).__name__:>7}")
                continue
            if st == 0:
                print(f"{m:>3} {1 << m:>7} {1 << (n - m):>10} {val:>14.6f} "
                      f"{val - vol:>12.6f} {st:>7}")
            else:
                print(f"{m:>3} {1 << m:>7} {1 << (n - m):>10} {'INFEAS/UNB':>14} "
                      f"{'-':>12} {st:>7}  ({msg[:40]})")
        print()


if __name__ == "__main__":
    main()
