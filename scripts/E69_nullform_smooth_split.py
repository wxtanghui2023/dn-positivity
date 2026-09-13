#!/usr/bin/env python3
"""
E69_nullform_smooth_split.py -- is the whole size of the phase sum carried by the singular (discrepancy) part?

THE NULL-FORM ATTEMPT
  The phase sum is a sum of exponentials whose phases are differences of a monotone function of the ordinate, so the
  natural cancellation structure is that of a null form: the oscillatory factor depends on combinations of ordinates
  that vanish on the degenerate set.  Working that structure out leads to a reformulation rather than a proof: since
  theta maps the ordinates into the tiny interval [0, theta(14)] with theta(14) about 0.0714, the phase sum is the
  Fourier transform at frequency n of the push-forward of the zero measure, a singular measure on that tiny interval.
  The classical theory of such transforms gives averaged (L2, Salem-Zygmund type) information, which is exactly the
  input this project already has, and no pointwise version.

  The attempt therefore turns on whether the size sits in the absolutely continuous (smooth) part, which stationary
  phase and van der Corput can handle, or in the singular (discrepancy) part, which they cannot.  That is what this
  script measures: the phase sum over the actual zeros, the phase sum over a smooth surrogate zero set of the same
  length, and the difference.

WHAT IS COMPUTED
  For sampled indices n in [0.30 X, X] with X = T0^2:
     S_n        = sum over the actual ordinates of exp(i n theta(gamma))
     S_n^sm     = the same sum over the smooth surrogate ordinates obtained by inverting the smooth counting law
                  F(v) = (v/2pi) log(v/2pi e) + 7/8, at the same count
     D_n        = S_n - S_n^sm
  and the root-mean-square and maximum of each, normalised by the count.

INPUTS   data/zeros_odlyzko_2M.npy
OUTPUT   scripts/E69_nullform_smooth_split.txt

PROVENANCE
  Written 2026-09-13 by 小灵 on 唐先生's instruction to keep trying.  No RH assumption used or claimed; the surrogate is
  the smooth density model already used in this project; numerics are evidence, not proof; NO LEAN IS RUN.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")


def smooth_surrogate(N, v0=10.0):
    """invert F(v) = (v/2pi) log(v/2pi e) + 7/8 for k = 1..N by Newton iteration"""
    out = np.empty(N)
    v = np.full(N, v0)
    k = np.arange(1, N + 1, dtype=np.float64)
    for _ in range(60):
        lv = np.log(v / (2 * np.pi))
        F = v * lv / (2 * np.pi) + 7.0 / 8.0 - k
        Fp = lv / (2 * np.pi) + 1.0 / (2 * np.pi)
        v = v - F / Fp
    out[:] = v
    return out


def main():
    out = []
    out.append("E69 -- does the singular (discrepancy) part carry the entire size of the phase sum?")
    out.append("NO LEAN IS RUN (compute directive 2026-09-13 11:47)")
    out.append("=" * 118)

    g = np.load(os.path.join(DATA, "zeros_odlyzko_2M.npy")).astype(np.float64)
    N = len(g)
    T0 = float(g[-1])
    X = T0 * T0
    out.append("  N = %d zeros, T0 = %.6f, X = T0^2 = %.6g" % (N, T0, X))
    sm = smooth_surrogate(N)
    out.append("  smooth surrogate built by inverting the counting law; top surrogate ordinate %.6f (actual %.6f)"
               % (float(sm[-1]), T0))
    th_g = 2.0 * np.arctan(1.0 / (2.0 * g))
    th_s = 2.0 * np.arctan(1.0 / (2.0 * sm))
    out.append("  Theta(14) = %.6f so the whole phase range lies in [0, %.4f]" % (2 * np.arctan(1 / 28.0), 2 * np.arctan(1 / 28.0)))
    out.append("")

    rng = np.random.default_rng(20260913)
    ns = 0.30 * X + rng.random(200) * (X - 0.30 * X)
    A = np.empty(len(ns))
    B = np.empty(len(ns))
    for i, n in enumerate(ns):
        A[i] = abs(np.exp(1j * n * th_g).sum())
        B[i] = abs(np.exp(1j * n * th_s).sum())
    D = A - B
    out.append("      quantity                rms              max            rms/N        max/N")
    for name, arr in (("S_n  (actual zeros)", A), ("S_n^smooth (surrogate)", B), ("D_n  (singular part)", np.abs(D))):
        out.append("      %-23s %-16.6g %-15.6g %-12.3e %.3e"
                   % (name, float(np.sqrt(np.mean(arr ** 2))), float(np.max(arr)),
                      float(np.sqrt(np.mean(arr ** 2))) / N, float(np.max(arr)) / N))
    out.append("")
    out.append("      ratio  max|D_n| / max|S_n|         : %.4f" % (float(np.max(np.abs(D))) / float(np.max(A))))
    out.append("      trivial bound for comparison        : |S_n| <= N, so needed is 0.8*N, i.e. a uniform 20%% gain")
    out.append("")
    out.append("=" * 118)
    out.append("READING")
    out.append("  If the smooth surrogate already reproduces the size, then the size is carried by the part that")
    out.append("  stationary phase can handle and the route would be open.  If the difference carries it, then the size")
    out.append("  sits in the singular part, which stationary phase cannot touch, and the route is blocked at the same")
    out.append("  place as the others.  The last line records the equivalent formulation of the requirement: a uniform")
    out.append("  gain of twenty percent over the trivial triangle-inequality bound.")
    txt = "\n".join(out) + "\n"
    with open(os.path.join(HERE, "E69_nullform_smooth_split.txt"), "w") as fh:
        fh.write(txt)
    print(txt)


if __name__ == "__main__":
    main()
