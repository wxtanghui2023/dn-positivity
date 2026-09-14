#!/usr/bin/env python3
"""E135 -- (a) does the continuous density model already give Q = o(1)?  and does Q(T) decrease?

WHAT
  唐先生's (a): replace the zeros by their smooth density and see whether the window
  quadratic form is then small.  His prediction: NO -- the density model gives a GROWING
  main term, Q_dens ~ c0 (log T)^2, so E130's tiny Q must come from DISCRETE cancellation.
  His sec.11 adds a logical check: with Q ~ 4.7e-4 at T = 10^3, one must NOT extrapolate
  Q(T) -> 0 without measuring the T-dependence.

SETUP (exactly E130's convention so numbers are comparable)
  N = T^2,  h = Y = T,  u = log(1 + h/N),
  rho = 1/2 + i gamma,  A_gamma = (exp(u rho) - 1)/rho,
  G_{jj'} = ((N+Y)^(1+i d) - N^(1+i d)) / ((1+i d) Y),  d = gamma_j - gamma_j',
  Q = A^* G A.

TWO FAMILIES OF POSITIONS
  actual : the real zeros up to G = 3T.
  density: the same NUMBER of points, placed by inverting the smooth count
           N(t) = (t/2pi) log(t/2pi e) + 7/8   (the "rigid"/smooth surrogate).

ALSO
  the diagonal/off-diagonal split of Q:  diag = sum |A_gamma|^2 (since K_Y(0)=1),
  and the ratio Q/(A^*A) = Q / sum|A_gamma|^2 (the "low-energy vector" ratio of E130 sec.9).

INPUT
  data/zeros_odlyzko_2M.npy

OUTPUT
  scripts/E135_density_model_vs_discrete.txt

MEMORY
  Gram matrices are M x M complex128, M capped at 3000.

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 "(a) -> (b)" directive; no RH used; no Lean run;
  numerics are evidence, not proof.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E135_density_model_vs_discrete.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))
MCAP = 3000

lines = []
def emit(s=""):
    lines.append(s); print(s)

def smooth_count(t):
    return (t / (2 * np.pi)) * np.log(t / (2 * np.pi * np.e)) + 7.0 / 8.0

def smooth_inverse(j):
    """gamma with smooth_count(gamma) = j, by bisection."""
    lo, hi = 1.0, 1e9
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if smooth_count(mid) < j:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def Qform(g, N, Y, u):
    rho = 0.5 + 1j * g
    A = (np.exp(u * rho) - 1.0) / rho
    d = g[:, None] - g[None, :]
    G = ((N + Y) ** (1.0 + 1j * d) - N ** (1.0 + 1j * d)) / ((1.0 + 1j * d) * Y)
    Q = float(np.real(np.conj(A) @ (G @ A)))
    diag = float(np.sum(np.abs(A) ** 2))
    return Q, diag, A

emit("E135 -- (a) density-model Q vs actual Q;  and the T-dependence of Q(T)")
emit("zeros: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")
emit("%8s %9s %8s %14s %14s %12s %12s %10s" %
     ("T", "N=T^2", "M", "Q_actual", "Q_density", "Qact/sum|A|^2", "log^2 T", "ratio dens/act"))
emit("-" * 108)

rows = []
for T in [100.0, 316.0, 1000.0]:
    N = T * T
    Y = T
    u = np.log1p(Y / N)
    Gcut = 3.0 * T
    g = zeros[zeros <= Gcut]
    if len(g) > MCAP:
        g = g[:MCAP]
    M = len(g)
    Qa, diaga, _ = Qform(g, N, Y, u)
    gs = np.array([smooth_inverse(j + 1.0) for j in range(M)])
    Qd, diagd, _ = Qform(gs, N, Y, u)
    rows.append((T, N, M, Qa, Qd, Qa / diaga, Qd / diagd))
    emit("%8.1f %9.3g %8d %14.6e %14.6e %12.6f %12.4f %10.3g"
         % (T, N, M, Qa, Qd, Qa / diaga, np.log(T) ** 2, Qd / Qa if Qa > 0 else float("nan")))

emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  Q_density >> Q_actual  -> the density model does NOT give o(1); the smallness")
emit("                            of the actual Q comes from DISCRETE cancellation.")
emit("  Q_density ~ c0 log^2 T -> confirms 唐先生's predicted main term.")
emit("  Q_actual vs T          -> decides whether Q(T) -> 0 (the line lives) or")
emit("                            Q(T) stays O(1) (the small value was a small-T accident).")
if len(rows) >= 2:
    Ts = np.array([r[0] for r in rows]); Qs = np.array([r[3] for r in rows])
    sl = np.polyfit(np.log(Ts), np.log(Qs), 1)[0]
    emit("  fitted exponent d(log Q_actual)/d(log T) = %.4f" % sl)
    Qd = np.array([r[4] for r in rows])
    sl2 = np.polyfit(np.log(Ts), np.log(Qd), 1)[0]
    emit("  fitted exponent d(log Q_density)/d(log T) = %.4f" % sl2)

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
