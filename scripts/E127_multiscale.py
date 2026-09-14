#!/usr/bin/env python3
"""E127 (ii) -- multi-scale test of the asymptotic law for the zero sum.

PURPOSE
  E122b measured, at a single scale, that the weighted zero sum is fully
  randomised: rms|S| matches sqrt(sum|A|^2) to within 5 percent, with a light
  tail.  This script repeats the measurement at several scales to test the
  ASYMPTOTIC LAW that the ratio
      R := int_window |Delta|^2 / (h*N)
  equals |S|^2 (since the window and the short interval are both sqrt(N)), and
  that |S|^2 tracks sum_gamma |A_gamma|^2, predicted to behave like
  log(T)/(2*pi*T) with T = sqrt(N) the natural height.

  So the decisive number per scale is |S|^2 itself, and the prediction is
  that it DECREASES like log(T)/T, i.e. the requirement holds with a margin
  that grows.

INPUT
  data/zeros_odlyzko_2M.npy   (2,001,052 zeros, max ordinate 1132490.658714)

OUTPUT
  scripts/E127_multiscale.txt

MEMORY
  chunked accumulation over zeros (200k per chunk); hard virtual-memory limit
  is applied by the caller (ulimit -v).  Peak allocation stays small.

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 "i, ii" instruction; no RH used;
  no Lean run; numerics are evidence, not proof.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E127_multiscale.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))
CH = 200_000
NSAMP = 60

lines = []
def emit(s=""):
    lines.append(s); print(s)

def wsum(logx, w, arr):
    tot = 0.0 + 0.0j
    n = len(arr)
    for s in range(0, n, CH):
        e = min(s + CH, n)
        tot += np.dot(w[s:e], np.exp(1j * arr[s:e] * logx))
    return tot

emit("E127 (ii) -- multi-scale test: is |S|^2 the correct requirement ratio,")
emit("and does it decrease like log(T)/T with T = sqrt(N)?")
emit("zeros: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")
emit("%10s %10s %12s %14s %14s %14s %10s %10s" %
     ("N", "T=sqrt N", "n_zeros", "rms|S|", "sqrt(sum|A|^2)", "max/rms",
      "rms|S|^2", "log T/2piT"))
emit("-" * 104)

rows = []
rng = np.random.default_rng(20260914)

for N in [1.0e4, 1.0e5, 1.0e6]:
    T = np.sqrt(N)
    u = np.log1p(T / N)
    xs = N * (1.0 + 0.5 * rng.random(NSAMP))
    logx = np.log(xs)
    rho = 0.5 + 1j * zeros
    A = (np.exp(u * rho) - 1.0) / rho

    # only zeros that can contribute: up to a generous multiple of the data max
    m = len(zeros)
    S = np.empty(NSAMP, dtype=complex)
    for i, lx in enumerate(logx):
        S[i] = wsum(lx, A, zeros)
    a = np.abs(S)
    rms = float(np.sqrt(np.mean(a ** 2)))
    pred = float(np.sqrt(np.sum(np.abs(A) ** 2)))
    rms2 = rms ** 2
    asym = np.log(T) / (2 * np.pi * T)
    rows.append((N, T, m, rms, pred, a.max() / rms, rms2, asym))
    emit("%10.3g %10.4f %12d %14.6e %14.6e %14.4f %10.3e %10.3e"
         % (N, T, m, rms, pred, a.max() / rms, rms2, asym))

emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  column 'rms|S|^2' IS the requirement ratio R = int|Delta|^2/(h*N),")
emit("  because the window and the short interval both equal sqrt(N).")
emit("  R << 1 means the requirement o(hN) holds with margin 1/R.")
emit("  If rms|S|^2 decreases roughly like log T/T while rms|S| tracks")
emit("  sqrt(sum|A|^2), the randomised law is scale-stable and the margin grows.")
if len(rows) >= 2:
    T = np.array([r[1] for r in rows]); R = np.array([r[6] for r in rows])
    sl = np.polyfit(np.log(T), np.log(R), 1)[0]
    emit("  fitted exponent d(log R)/d(log T) = %.4f   (predicted ~ -1)" % sl)

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
