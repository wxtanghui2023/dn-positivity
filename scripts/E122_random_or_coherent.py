#!/usr/bin/env python3
"""E122 -- is the window-averaged zero sum random-like or coherent?

PURPOSE
  E121 argued (mechanistically) that the phase excursion gamma*Y/N = gamma/T
  means the window averages out heights gamma >> T while leaving gamma <~ T
  intact, hence the effective range is gamma <~ T and a cancellation of order
  log^2 T/(4pi^2) is required.  That argument must be tested, and the decisive
  question is whether the window-averaged zero sum
      S(x) = sum_{gamma <= G} e^{i gamma log x}
  behaves like a RANDOM sum (so |S|^2 ~ N(G)) or like a COHERENT sum
  (so |S|^2 ~ N(G)^2).  Everything about the required cancellation depends
  on which.

INPUT
  data/zeros_odlyzko_2M.npy   (2,001,052 zeros, max ordinate 1132490.658714)

OUTPUT
  scripts/E122_random_or_coherent.txt

CONCLUSION (expected)
  Gives the growth exponent of int_window |S|^2 versus the number of zeros, and
  hence decides whether the required cancellation is present or absent.

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-13 continuing instruction; no RH used;
  no Lean run; numerics are evidence, not proof.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E122_random_or_coherent.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

N = 1.0e6
Y = 1.0e3
xs = N + Y * np.linspace(0.0, 1.0, 64)      # window sample
logx = np.log(xs)

lines = []
def emit(s=""):
    lines.append(s); print(s)

emit("E122 -- window-averaged zero sum: random-like or coherent?")
emit("N = %.1f   Y = %.1f   window samples = %d" % (N, Y, len(xs)))
emit("zeros: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")
emit("%12s %10s %14s %14s %14s %10s" %
     ("G", "N(G)", "mean|S|^2", "diag=Y*N(G)", "coh=Y*N(G)^2", "ratio/diag"))
emit("-" * 82)

rows = []
for G in [1.0e3, 3.162e3, 1.0e4, 3.162e4, 1.0e5, 3.162e5, 1.0e6, 1.1325e6]:
    g = zeros[zeros <= G]
    m = len(g)
    if m == 0:
        continue
    # S(x_j) = sum_gamma e^{i gamma log x_j}  -- vectorised
    S = np.exp(1j * np.outer(logx, g)).sum(axis=1)
    intS2 = Y * float(np.mean(np.abs(S) ** 2))     # window integral approx
    diag = Y * m
    coh = Y * float(m) ** 2
    rows.append((G, m, intS2, diag, coh))
    emit("%12.4g %10d %14.6e %14.6e %14.6e %10.3f"
         % (G, m, intS2, diag, coh, intS2 / diag))

emit("")
emit("READING")
emit("  intS2/diag ~ 1        -> RANDOM-like: no coherence, cancellation present.")
emit("  intS2/diag ~ N(G)     -> FULLY COHERENT: no cancellation.")
emit("  growth of intS2 versus N(G): fit the exponent from the table above.")
if len(rows) >= 3:
    ns = np.array([r[1] for r in rows], float)
    vs = np.array([r[2] for r in rows], float)
    ok = (ns > 0) & (vs > 0)
    slope = np.polyfit(np.log(ns[ok]), np.log(vs[ok]), 1)[0]
    emit("  fitted exponent d(log intS2)/d(log N(G)) = %.4f" % slope)
    emit("  (0.5 = random-like, 1.0 = coherent-with-fixed-|S|, 2.0 = fully coherent)")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
