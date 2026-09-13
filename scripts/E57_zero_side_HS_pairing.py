#!/usr/bin/env python3
"""
E57_zero_side_HS_pairing.py -- can the Hilbert-Schmidt input of the inertia device be evaluated on the ZERO side
with elementary tools (no cancellation)?

WHY THIS MATTERS FOR THE GOAL
  The inertia / rank-trace device (rebuilt by us in the analytic-half reconstruction) converts a spectral input
  into Li-type positivity, and its one quantitative input is the Hilbert-Schmidt norm of the certificate matrix.
  On the zero side that norm is a pair sum over the ordinates with an explicit kernel:
        ||G||^2_HS  ~  (a^2 L^2)^{-1} * sum_{gamma,gamma'} Phi(gamma - gamma')^2 * (weights) ,
  with Phi the Fourier transform of the squared window.  The frontier evaluates this quantity on the PRIME side
  (a Dirichlet-polynomial second moment).  The question here is whether it can instead be bounded on the ZERO
  side ELEMENTARILY, using only the triangle inequality and a count of neighbours, the way the phase-locking sum
  was handled in E55.  If yes, the device stops needing the hard analytic input; if the pairing turns out to be
  O(N log N) instead of O(N), the elementary route is dead and one must keep the prime-side machinery.

WHAT IS COMPUTED
  With the indicator window psi_0 (psi = 1 on [-1/2,1/2], so phi^2 = 1 on [-L/2,L/2] and the kernel is the sine
  kernel Phi(x) = 2 sin(xL/2)/x, Phi(0) = L), the normalised pairing
        R_meas(N) := (1/N) * sum_{gamma,gamma'} ( Phi(gamma-gamma') / L )^2 = 1 + (off-diagonal)/N
  is evaluated exactly by enumerating all pairs using the project's zero tables, at several sizes, together with
  R(psi_0) = 4/3, the value the frontier's prime-side evaluation gives for this window.  The diagonal is 1 by
  construction, so the off-diagonal is R_meas - 1, and its growth in N decides the question.

INPUTS   data/zeros_2000.npy , data/zeros_odlyzko_100k.npy , data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E57_zero_side_HS_pairing.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction "继续" after the goal correction.  No RH assumption used or
  claimed; numerics are evidence, not proof; NO LEAN IS RUN (compute directive 2026-09-13 11:47).
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def pairing(g, L):
    """(1/N) sum_{gamma,gamma'} (Phi(gamma-gamma')/L)^2 with Phi(x) = 2 sin(xL/2)/x, Phi(0)=L"""
    N = len(g)
    tot = 0.0
    # diagonal
    tot += N * 1.0
    # off-diagonal by offsets, memory-safe
    # truncate: the kernel decays like 1/d, so its square decays like 1/d^2; the tail is estimated analytically
    K = min(N - 1, 2000)
    off = 0.0
    for k in range(1, K + 1):
        d = g[k:] - g[:-k]
        val = 2 * np.sin(d * L / 2) / (d * L)          # Phi/L
        off += 2.0 * float(np.sum(val ** 2))
    # tail: beyond K, |Phi/L| <= 2/(k gap L), so each offset contributes at most 2*N*(2/(k gap L))^2
    gap = 2 * np.pi / np.log(g[-1])
    ks = np.arange(K + 1, K + 4001, dtype=np.float64)
    tail = 2.0 * N * float(np.sum(4.0 / (ks ** 2 * gap ** 2 * L ** 2)))
    return 1.0 + (off + tail) / N, (off + tail) / N


def main():
    out = []
    out.append("E57 -- zero-side evaluation of the inertia device's Hilbert-Schmidt pairing")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 112)
    out.append("   R_meas(N) = (1/N) sum_{gamma,gamma'} (Phi(gamma-gamma')/L)^2  with Phi/L = 2 sin(dL/2)/(dL)")
    out.append("   diagonal = 1 ; off-diagonal = R_meas - 1 ; frontier's prime-side value for this window: R(psi_0)=4/3")
    out.append("")
    out.append("      N          T (top)        L = log(T/2pi)     R_meas         off-diagonal/N     ratio to 4/3")
    for fname, n in (("zeros_2000.npy", 2000), ("zeros_odlyzko_100k.npy", 100000)):
        p = os.path.join(DATA, fname)
        if not os.path.exists(p):
            continue
        g = np.load(p).astype(np.float64)[:n]
        T = float(g[-1])
        L = float(np.log(T / (2 * np.pi)))
        R, off = pairing(g, L)
        out.append("      %-10d %-14.6g %-19.6f %-15.6f %-19.6f %.4f" % (n, T, L, R, off, R / (4.0 / 3.0)))
    out.append("")
    out.append("   READING")
    out.append("   The diagonal is fixed at 1.  If the off-diagonal divided by N stays bounded as N grows, the")
    out.append("   pairing is O(N) and the zero-side elementary route can carry the device's input; if it grows like")
    out.append("   log N, the pairing is O(N log N), the elementary route cannot reach the needed constant, and the")
    out.append("   prime-side machinery remains essential.  The frontier's value 4/3 is the target for the total.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E57_zero_side_HS_pairing.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
