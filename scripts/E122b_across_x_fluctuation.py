#!/usr/bin/env python3
"""E122b (memory-safe) -- across-x fluctuation of the zero sum.

WHY RERUN
  The previous version of this script allocated np.outer(logx, g) with
  300 x-samples times up to 2,001,052 zeros as complex128: 300*2e6*16 bytes
  = 9.6 GB.  That is what killed it (no output file was produced).  This
  version never materialises more than a CHUNK x n_zeros array, and reports
  its own peak memory so the budget is visible.

PURPOSE
  E122 showed that WITHIN a window the averaged zero sum behaves randomly,
  |S|^2 ~ N(G), so square-root cancellation is present on average.  But the
  requirement is per-window (pointwise in x), not on average, so what matters
  is the fluctuation of |S| ACROSS x: max|S| / rms|S|.  This is the headline
  quantity: it measures how far the worst window sits above the typical one.

INPUT
  data/zeros_odlyzko_2M.npy   (2,001,052 zeros, max ordinate 1132490.658714)

OUTPUT
  scripts/E122b_across_x_fluctuation.txt

METHOD
  For each x, accumulate S = sum_gamma w_gamma e^{i gamma log x} in chunks of
  200,000 zeros.  Peak allocation ~ chunk size only.

CONCLUSION (expected)
  Gives rms and max of |S| across x, the ratio max/rms, and the comparison of
  rms with the pure-random prediction sqrt(sum |w|^2).

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 instruction ("result?" + "do not blow
  memory again"); no RH used; no Lean run; numerics are evidence, not proof.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E122b_across_x_fluctuation.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

N = 1.0e6
h = np.sqrt(N)
T = h
u = np.log1p(h / N)
CH = 200_000                      # chunk over zeros -> tiny peak allocation
NSAMP = 120                       # x samples

lines = []
def emit(s=""):
    lines.append(s); print(s)

def wsum(logx, w, arr):
    """sum_j w_j e^{i arr_j logx} in chunks; returns complex."""
    tot = 0.0 + 0.0j
    n = len(arr)
    for s in range(0, n, CH):
        e = min(s + CH, n)
        tot += np.dot(w[s:e], np.exp(1j * arr[s:e] * logx))
    return tot

rho = 0.5 + 1j * zeros
A = (np.exp(u * rho) - 1.0) / rho

emit("E122b -- across-x fluctuation of the zero sum (memory-safe rerun)")
emit("N = %.1f   h = %.1f   T = %.1f   u = %.4e" % (N, h, T, u))
emit("chunk = %d zeros   x-samples = %d   peak-so-far = %.1f MB"
     % (CH, NSAMP, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")

rng = np.random.default_rng(20260913)
xs = N * (1.0 + 0.5 * rng.random(NSAMP))
logx = np.log(xs)

for G, tag in [(T, "gamma<=T  (natural height)"),
               (10 * T, "gamma<=10T"),
               (1.1325e6, "all available zeros")]:
    m = int(np.searchsorted(zeros, G, side="right"))
    g = zeros[:m]
    emit("--- %s : n_zeros = %d ---" % (tag, m))

    # unweighted and weighted accumulations, one x at a time
    un = np.empty(NSAMP, dtype=complex)
    wt = np.empty(NSAMP, dtype=complex)
    for i, lx in enumerate(logx):
        un[i] = wsum(lx, np.ones(m, dtype=complex), g)
        wt[i] = wsum(lx, A[:m], g)

    for nm, v in (("unweighted", un), ("A-weighted", wt)):
        a = np.abs(v)
        rms = float(np.sqrt(np.mean(a ** 2)))
        emit("   %-10s rms=%.6e  mean=%.6e  max=%.6e  max/rms=%.4f"
             % (nm, rms, a.mean(), a.max(), a.max() / rms))
    emit("   pure-random prediction rms_unw ~ sqrt(n) = %.6e" % np.sqrt(m))
    emit("   pure-random prediction rms_wt  ~ sqrt(sum|A|^2) = %.6e"
         % float(np.sqrt(np.sum(np.abs(A[:m]) ** 2))))
    emit("   coherent worst case sum|A| = %.6e" % float(np.abs(A[:m]).sum()))
    emit("")

emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  max/rms near sqrt(2 log M) with M samples (~3.1 for M=120): light tail.")
emit("  much larger: heavy tail, worst windows far above the average.")
emit("  rms vs the pure-random prediction: agreement means the SIZE of the")
emit("  sum is randomised; disagreement means residual structure.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
