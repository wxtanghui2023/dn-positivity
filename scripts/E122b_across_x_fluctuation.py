#!/usr/bin/env python3
"""E122b -- across-x fluctuation of the zero sum: is there a heavy tail?

PURPOSE
  E122 showed that WITHIN one window the averaged zero sum behaves randomly,
  |S|^2 ~ N(G), so square-root cancellation is present on average.  But the
  requirement is per-window (equivalently pointwise at each x), not on average,
  so what matters is the FLUCTUATION of |S| across x.  This script measures the
  distribution of |S(x)| over many x and reports the sup versus the typical
  value, which is the quantity the per-window requirement actually needs.

INPUT
  data/zeros_odlyzko_2M.npy

OUTPUT
  scripts/E122b_across_x_fluctuation.txt

CONCLUSION (expected)
  Gives sup|S| / rms|S|; a value near sqrt(2 log M) with M the number of
  samples indicates a light (Gaussian-like) tail, a much larger value a heavy
  tail.  This decides whether the per-window requirement is close to the
  averaged one or far above it.

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-13 continuing instruction; no RH used;
  no Lean run; numerics are evidence, not proof.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E122b_across_x_fluctuation.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

N = 1.0e6
h = np.sqrt(N)
T = h
u = np.log1p(h / N)
rho = 0.5 + 1j * zeros
A = (np.exp(u * rho) - 1.0) / rho          # the true amplitudes
lines = []
def emit(s=""):
    lines.append(s); print(s)

emit("E122b -- across-x fluctuation of the weighted zero sum")
emit("N = %.1f   h = %.1f   natural height T = %.1f   u = %.4e" % (N, h, T, u))
emit("")

rng = np.random.default_rng(20260913)
xs = N * (1.0 + 0.5 * rng.random(300))       # x spread over [N, 1.5N]
logx = np.log(xs)

for G, tag in [(T, "gamma<=T (natural height)"),
               (10 * T, "gamma<=10T"),
               (1.1325e6, "all available zeros")]:
    g = zeros[zeros <= G]
    cut = A[zeros <= G]
    S = np.exp(1j * np.outer(logx, g)) @ cut
    a = np.abs(S)
    emit("%s : n_zeros(G) = %d" % (tag, len(g)))
    emit("   rms|S| = %.6e   mean|S| = %.6e   max|S| = %.6e   max/rms = %.4f"
         % (np.sqrt(np.mean(a**2)), a.mean(), a.max(), a.max() / np.sqrt(np.mean(a**2))))
    emit("   pure-random prediction: rms ~ sqrt(sum |A|^2) = %.6e"
         % (np.sqrt(np.sum(np.abs(cut) ** 2))))
    emit("   coherent (worst) case: sum |A|      = %.6e" % (np.abs(cut).sum()))
    emit("")

emit("READING")
emit("  max/rms near sqrt(2 log M) with M=300 samples (~3.4) -> Gaussian tail:")
emit("     the per-window requirement is close to the averaged one.")
emit("  max/rms well above that -> heavy tail, individual windows are much")
emit("     larger than the average, and the per-window requirement is far")
emit("     above the averaged estimate.")
emit("  Also compare rms|S| with the pure-random sqrt(sum|A|^2): agreement")
emit("  means the sum's SIZE is randomised, disagreement means structure.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
