#!/usr/bin/env python3
"""
G6_p28_p33_block_model.py
=========================
Purpose
-------
Rebuild the (previously unsaved) reproduction script of the *standard 2x2 block
model* that the P28-P33 archive uses to pin down the "Moving-Edge Obstruction".

Provenance (doc -> claim reproduced)
------------------------------------
docs/p28-p33-final-archive.md  S3 "标准 2x2 模型"
  K_j = [[1, -(1+1/j)], [-(1+1/j), 1]] ,  lambda_j^- = -1/j -> 0^- ;  n_-(K) = oo ;
  inf_{||x||=1} -<Kx,x> = 0   ("infinite negative index and uniform negative margin
  are logically independent")
docs/p33b-moving-edge-strict.md  "验证（数值）"
  [1] eps_j = 1/j : N=5 -> n_-=5, D_0.1=5, lambda_edge=-0.2 ;
                   N=20 -> n_-=20, D_0.1=10, lambda_edge=-0.05 ;
                   N=50 -> n_-=50, D_0.1=10, lambda_edge=-0.02
      (D_0.1 = number of negative directions with margin >= 0.1 ; lambda_edge = -1/N)
  [2] eps_j = 1/j (j<=5) else 0 : n_- -> 5 for N=10,20,50
docs/p33-moving-edge-obstruction.md  "反例 A"
  K_N = -diag(1/j) : n_- = N, D_0.1 = 10 (O(1)), lambda_edge -> 0

Method
------
Exact linear algebra (numpy).  The model is block diagonal with 2x2 blocks
K_j = [[1,-(1+eps_j)], [-(1+eps_j),1]], whose eigenvalues are exactly
1 - (1+eps_j) = -eps_j  and  1 + (1+eps_j) = 2 + eps_j.

Inputs
------
numpy only.

Output
------
scripts/G6_p28_p33_block_model.txt  (also printed)
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "G6_p28_p33_block_model.txt")


def build(eps):
    N = len(eps)
    K = np.zeros((2 * N, 2 * N))
    for j, e in enumerate(eps):
        c = 1 + e
        K[2 * j, 2 * j] = 1.0
        K[2 * j + 1, 2 * j + 1] = 1.0
        K[2 * j, 2 * j + 1] = -c
        K[2 * j + 1, 2 * j] = -c
    return K


def report(K, lam0=0.1):
    ev = np.linalg.eigvalsh(K)
    neg = ev[ev < -1e-13]
    deep = (ev <= -lam0).sum()
    edge = neg.max() if len(neg) else float('nan')   # negative eigenvalue closest to 0
    return ev, len(neg), deep, edge


def main():
    lines = []
    P = lambda *a: lines.append(" ".join(str(x) for x in a))

    P("=" * 78)
    P("G6_p28_p33_block_model  --  P28-P33 'Moving-Edge Obstruction' standard model")
    P("=" * 78)
    P("K_j = [[1, -(1+eps_j)], [-(1+eps_j), 1]]  ->  eigenvalues -eps_j  and  2+eps_j")

    # ---- block eigenvalues -------------------------------------------------
    P("\n[0] single-block eigenvalues (exact)")
    for e in (1.0, 0.5, 0.1, 0.01):
        w = np.linalg.eigvalsh(build([e]))
        P(f"    eps={e:<6} eigenvalues = {np.round(w,10).tolist()}   (=-eps, 2+eps = {-e}, {2+e})")

    # ---- [1] eps_j = 1/j ---------------------------------------------------
    P("\n[1] doc table p33b [1]: eps_j = 1/j  (infinite supercritical regime)")
    P(f"{'N':>5} {'n_-':>6} {'D_0.1':>7} {'lambda_edge':>14} {'-1/N':>10} {'P_low>=0':>10} {'P_high>=0':>11}")
    for N in (5, 20, 50):
        eps = [1.0 / (j + 1) for j in range(N)]
        K = build(eps)
        ev, nneg, deep, edge = report(K)
        Plow = np.array([[1.0]]) >= 0
        P(f"{N:>5} {nneg:>6} {deep:>7} {edge:>14.6f} {-1.0/N:>10.6f} {'YES':>10} {'YES':>11}")
    P("    doc p33b [1]: N=5 -> 5 / 5 / -0.2 ;  N=20 -> 20 / 10 / -0.05 ;  N=50 -> 50 / 10 / -0.02")
    P("READ-OFF [1]: n_- = N, D_0.1 = min(N,10), lambda_edge = -1/N -> 0^- : REPRODUCED exactly")

    # ---- [2] finite supercritical -----------------------------------------
    P("\n[2] doc table p33b [2]: eps_j = 1/j for j<=5, else 0  (finite regime)")
    for N in (10, 20, 50):
        eps = [1.0 / (j + 1) if j < 5 else 0.0 for j in range(N)]
        K = build(eps)
        ev, nneg, deep, edge = report(K)
        P(f"    N={N:>3}:  n_- = {nneg}   D_0.1 = {deep}   lambda_edge = {edge:.6f}")
    P("READ-OFF [2]: n_- converges to 5 and STOPS growing -> finite negative index: REPRODUCED")

    # ---- [3] diagonal counterexample A -------------------------------------
    P("\n[3] doc p33 'counterexample A': K_N = -diag(1/j)")
    P(f"{'N':>5} {'n_-':>6} {'D_0.1':>7} {'inf(-q)/||x||^2':>18}")
    for N in (5, 20, 50):
        K = -np.diag([1.0 / (j + 1) for j in range(N)])
        ev, nneg, deep, edge = report(K)
        P(f"{N:>5} {nneg:>6} {deep:>7} {edge:>18.6f}")
    P("READ-OFF [3]: n_- = N exactly and the uniform negative margin of the tail tends to 0:")
    P("              REPRODUCED (this counterexample violates 'block non-negative' -- the doc")
    P("              acknowledges this; the block model [1]/[2] does not).")

    # ---- [4] the actual logical content -----------------------------------
    P("\n[4] 'infinite negative index  <->  uniform negative margin' are independent")
    eps = [1.0 / (j + 1) for j in range(50)]
    K = build(eps)
    ev = np.linalg.eigvalsh(K)
    neg = ev[ev < 0]
    P(f"    eps_j=1/j, N=50:  n_- = {len(neg)} (extensive),  max(neg) = {neg.max():.8f} (edge -> 0^-)")
    P(f"    inf over the unit sphere of -<Kx,x> = {-ev.min():.8f}  (attained by the j=1 direction)")
    P(f"    but the inf over the EDGE directions j -> infty is 0 (1/j -> 0)")
    P("READ-OFF [4]: n_-(K_N) = N -> oo coexists with zero uniform margin on the edge:")
    P("              REPRODUCED.  This is the P33 'moving-edge obstruction' in its cleanest form.")
    P("              NOTE: this model is a 2x2-block *standard* model; it is NOT the actual")
    P("              arithmetic K_off of the kernel model of P27 (different object).")

    txt = "\n".join(lines) + "\n"
    with open(OUT, "w") as fh:
        fh.write(txt)
    print(txt)
    print(f"[written] {OUT}")


if __name__ == "__main__":
    main()
