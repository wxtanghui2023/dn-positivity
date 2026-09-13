#!/usr/bin/env python3
"""E120 -- locate the bookkeeping error: is the magnitude sum truncated at the natural height?

PURPOSE
  The E117-E119 magnitude estimates repeatedly came out far below the target h*N,
  which contradicts the known openness of Legendre.  Hypothesis to test: the
  relevant zero heights are NOT limited to the natural height T = N/h; the
  magnitude sum is instead dominated by the TAIL gamma > T, because a single
  term is |A_gamma| ~= u for gamma << T but ~= 1/gamma for gamma >> T, and the
  number of zeros grows like log t, so the tail sum ~= (1/4pi) log^2 x can
  exceed the head sum ~= (1/2pi) log T.

INPUT
  data/zeros_odlyzko_2M.npy  (2,001,052 zeros, max ordinate 1132490.658714)
  (provenance: Odlyzko zero tables, staged in-repo; see docs for source note)

OUTPUT
  scripts/E120_height_truncation.txt  (written beside this script)

CONCLUSION (expected)
  If |S_tail| >> |S_head| then the truncation at the natural height is the
  bookkeeping error, and the pair-correlation range must be re-derived with
  heights up to x rather than up to T.

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-13 "先修" instruction; no RH used;
  no Lean run; numerics are evidence, not proof.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E120_height_truncation.txt")

zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))
lines = []


def emit(s=""):
    lines.append(s)
    print(s)


emit("E120 -- height truncation diagnostic")
emit("zeros loaded: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")

# consistent scale: N = x0, h = sqrt(N), Y = sqrt(N)
x0 = 1.0e6
h = np.sqrt(x0)
N_cut = h                      # natural height T = N/h = sqrt(N)
u = np.log1p(h / x0)
emit("x0 = %.1f   h = sqrt(x0) = %.3f   natural height T = %.3f   u = %.3e" % (x0, h, N_cut, u))
emit("")

sel_head = zeros <= N_cut
sel_tail = (zeros > N_cut) & (zeros <= 1.05 * x0)
emit("zeros: head (gamma<=T) = %d ; tail (T<gamma<=1.05 x0) = %d" % (sel_head.sum(), sel_tail.sum()))

# magnitude sums (the objects the bookkeeping uses)
g_head, g_tail = zeros[sel_head], zeros[sel_tail]
A_head = u / np.sqrt(0.25 + g_head**2) * np.sqrt(np.maximum(1.0, np.minimum(g_head * u, np.pi) ** 2))
# cleaner: |A| = |e^{rho u}-1|/|rho|
def absA(g):
    rho = 0.5 + 1j * g
    return np.abs(np.exp(u * rho) - 1.0) / np.abs(rho)

sum_head = absA(g_head).sum()
sum_tail = absA(g_tail).sum()
emit("")
emit("SUM |A| over head  = %.6e" % sum_head)
emit("SUM |A| over tail  = %.6e" % sum_tail)
emit("ratio tail/head    = %.4f" % (sum_tail / max(sum_head, 1e-300)))
emit("predicted head ~ (1/2pi) log T          = %.6f" % (np.log(N_cut) / (2 * np.pi)))
emit("predicted tail ~ (1/4pi)(log^2(1.05x0)-log^2 T) = %.6f"
     % ((np.log(1.05 * x0)**2 - np.log(N_cut)**2) / (4 * np.pi)))
emit("")

# partial sums versus cut, to see where the magnitude actually comes from
emit("cumulative |A| versus cut (the diagnostic):")
for frac in [1, 2, 5, 10, 50, 100, 500, 1000]:
    cut = N_cut * frac
    g = zeros[zeros <= cut]
    emit("  cut = %8.1f T : n_zeros = %8d : sum|A| = %.6e" % (frac, len(g), absA(g).sum()))
emit("")
emit("READING: if the sum keeps GROWING well past cut = T, the natural-height")
emit("truncation is the bookkeeping error, and every E117-E119 estimate that")
emit("truncated at T is (systematically, not marginally) too small.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
