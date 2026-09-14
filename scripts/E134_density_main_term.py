#!/usr/bin/env python3
"""E134 -- the decisive scalar: is there an uncentred density main term in S(T)=sum A_gamma?

WHY
  唐先生's critique of E130 sec.4 (accepted): the claim "|S| ~ sqrt(M) u" silently ASSUMED
  random phases, i.e. exactly the square-root cancellation that has to be PROVED.  The two
  extremes differ by sqrt(T log T):
        fully coherent        : |S| ~ log T / (2 pi)
        square-root cancelling: |S| ~ sqrt(log T / (2 pi T))
  So the question is which regime the ACTUAL A_gamma of E130 sits in.  His prescription:
  compute the continuous DENSITY main term S_dens(T) and align it term by term with the
  actual definition, then decide among three outcomes:
     A. density main term is o(1)          -> only the fluctuation remains
     B. density main term is a constant    -> extra cancellation needed
     C. density main term is C log T       -> E130's A_gamma is NOT correctly centred,
                                              and the test function must be redefined.

WHAT IS COMPUTED
  (1) S_direct(G) = sum_{gamma<=G} A_gamma  with the ACTUAL E130 weights
      A_gamma = (exp(u*rho)-1)/rho,  rho = 1/2 + i gamma,  u = log(1+h/N),  h = sqrt(N).
  (2) |S_direct|^2 compared with the exact quadratic form Q = A^* G A from E130
      (they should agree, since the Gram is nearly rank one).
  (3) the density model
      S_dens(T) = (1/2pi) int_1^T ((e^{i u gamma}-1)/(i gamma)) log(gamma/2pi) dgamma
      and the constant C = (1/2pi) int_0^1 (e^{iv}-1)/(iv) dv, to see whether the density
      route predicts C log T rather than o(1).
  (4) the random-phase prediction sqrt(M)*u for comparison.

INPUT
  data/zeros_odlyzko_2M.npy

OUTPUT
  scripts/E134_density_main_term.txt

MEMORY
  direct sums are cheap; the Gram matrix is M x M with M capped at 3000.

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 critique/directive; no RH used; no Lean run;
  numerics are evidence, not proof.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E134_density_main_term.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))
MCAP = 3000

N = 1.0e6
h = np.sqrt(N)
Y = h
T = h                      # natural height = 1/u
u = np.log1p(h / N)

lines = []
def emit(s=""):
    lines.append(s); print(s)

emit("E134 -- is there an uncentred density main term in S(T) = sum A_gamma ?")
emit("N = %.1f   h = Y = T = %.3f   u = %.6e   (natural height 1/u = %.3f)" % (N, h, u, 1.0 / u))
emit("zeros: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")

rho_all = 0.5 + 1j * zeros
A_all = (np.exp(u * rho_all) - 1.0) / rho_all

emit("%10s %10s %16s %16s %16s %16s" %
     ("G", "n_zeros", "|S_direct|", "|S|^2", "sqrt(M)*u", "log T/(2pi)"))
emit("-" * 96)
Svals = {}
for G in [T, 2 * T, 5 * T, 10 * T, 100 * T, float(zeros[-1])]:
    m = int(np.searchsorted(zeros, G, side="right"))
    S = complex(np.sum(A_all[:m]))
    Svals[G] = (m, S)
    emit("%10.4g %10d %16.6e %16.6e %16.6e %16.6f"
         % (G, m, abs(S), abs(S) ** 2, np.sqrt(m) * u, np.log(T) / (2 * np.pi)))

emit("")

# consistency with the exact quadratic form
Gcut = T
g = zeros[zeros <= Gcut][:MCAP]
m = len(g)
d = g[:, None] - g[None, :]
Gm = ((N + Y) ** (1.0 + 1j * d) - N ** (1.0 + 1j * d)) / ((1.0 + 1j * d) * Y)
rho = 0.5 + 1j * g
A = (np.exp(u * rho) - 1.0) / rho
Q = float(np.real(np.conj(A) @ (Gm @ A)))
S_head = complex(np.sum(A))
emit("consistency check at G = T (M = %d):" % m)
emit("   Q = A^*G A (exact, E130 method) = %.6e" % Q)
emit("   |S_direct|^2 (plain sum)        = %.6e" % (abs(S_head) ** 2))
emit("   ratio |S|^2 / Q                 = %.6f   (should be ~1 if rank one)" %
     (abs(S_head) ** 2 / Q if Q > 0 else float("nan")))
emit("")

# density model and its constant
from math import pi
def sdensity(Tv, uu, npts=200000):
    v = np.linspace(uu * 1.0, 1.0, npts)
    gam = v / uu
    f = (np.exp(1j * v) - 1.0) / (1j * v)
    integ = f * np.log(np.maximum(gam, 1.0) / (2 * pi))
    return float(np.trapz(integ, v)) / (2 * pi)

C0 = sdensity(T, u)               # scaled to the v-integral of length 1/u..1
vv = np.linspace(1e-6, 1.0, 400000)
fs = (np.exp(1j * vv) - 1.0) / (1j * vv)
Cv = float(np.trapz(fs, vv)) / (2 * pi)
emit("density model:")
emit("   C = (1/2pi) int_0^1 (e^{iv}-1)/(iv) dv = (%.6f %+.6fi)  |C| = %.6f"
     % (Cv.real, Cv.imag, abs(Cv)))
emit("   S_dens(T) with log(gamma/2pi) weight  = (%.6f %+.6fi)  |.| = %.6f"
     % (C0.real, C0.imag, abs(C0)))
emit("   naive 'C log T' (using C*log T)       = (%.6f %+.6fi)  |.| = %.6f"
     % ((Cv * np.log(T)).real, (Cv * np.log(T)).imag, abs(Cv * np.log(T))))
emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING / three outcomes")
emit("  A: density main term o(1)      -> only fluctuation remains")
emit("  B: density main term = constant-> extra cancellation needed")
emit("  C: density main term ~ C log T -> E130's A_gamma is NOT correctly centred")
emit("  Compare the |S_direct| column with the last two columns to decide.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
