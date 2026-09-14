#!/usr/bin/env python3
"""E130 -- make the window-integral identity EXACT and evaluate it exactly.

WHAT IS RIGORISED
  E122b/E127 estimated
      int_N^{N+Y} | sum_gamma A_gamma e^{i gamma log x} |^2 dx
  by SAMPLING x in the window.  But the integral is elementary:
      int_N^{N+Y} x^{i d} dx = ((N+Y)^{1+i d} - N^{1+i d}) / (1 + i d),
  so the whole quantity equals the exact quadratic form
      Y * A^* G A ,     G_{jj'} = ((N+Y)^{1+i d} - N^{1+i d}) / ((1+i d) Y),
      d = gamma_j - gamma_j' ,
  with G POSITIVE SEMIDEFINITE (it is a Gram matrix).  No quadrature, no
  sampling, no error term.  Everything measured before can now be computed
  exactly.

WHAT IS COMPUTED
  (1) rho := A^*G A / sum_gamma |A_gamma|^2   -- the exact replacement for the
      sampled "random-like" ratio (sampling gave ~1).
  (2) the eigen-decomposition: which eigenvalues and which projections carry
      the quadratic form, i.e. where the smallness (or not) comes from.
  (3) the exact requirement check: the criterion is
          int |Delta|^2 = o(h N)   <=>   N * A^*G A = o(h N)
                                   <=>   A^*G A = o(N)
      since h = Y = sqrt(N); so compare A^*G A with N.

INPUT
  data/zeros_odlyzko_2M.npy

OUTPUT
  scripts/E130_exact_quadratic.txt

MEMORY
  G is M x M complex128, M capped at 3000 (~150 MB).

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 "can the identity be made rigorous?"
  instruction; no RH used; no Lean run; numerics are evidence, not proof.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E130_exact_quadratic.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

N = 1.0e6
Y = np.sqrt(N)
MCAP = 3000

lines = []
def emit(s=""):
    lines.append(s); print(s)

def gram(g):
    d = g[:, None] - g[None, :]
    return ((N + Y) ** (1.0 + 1j * d) - N ** (1.0 + 1j * d)) / ((1.0 + 1j * d) * Y)

emit("E130 -- exact quadratic form for the window integral")
emit("N = %.1f   Y = sqrt(N) = %.3f   h = Y   (Legendre scale)" % (N, Y))
emit("zeros: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")
emit("identity: int_N^{N+Y} |sum_gamma A_gamma e^{i gamma log x}|^2 dx = Y * A^* G A")
emit("")

for Gcut in [1.0e3, 1.5e3, 2.0e3, 3.0e3]:
    g = zeros[zeros <= Gcut]
    if len(g) > MCAP:
        g = g[:MCAP]
    M = len(g)
    u = np.log1p(Y / N)
    rho = 0.5 + 1j * g
    A = (np.exp(u * rho) - 1.0) / rho

    Gm = gram(g)
    w, V = np.linalg.eigh(Gm)
    quad = float(np.real(np.conj(A) @ (Gm @ A)))      # A^* G A  (exact)
    diag = float(np.sum(np.abs(A) ** 2))               # sum |A|^2
    rho_ratio = quad / diag
    proj = np.abs(V.conj().T @ A) ** 2                 # |<A, v_k>|^2

    emit("--- gamma <= %.4g  (M = %d) ---" % (Gcut, M))
    emit("   A^*G A (exact)          = %.6e" % quad)
    emit("   sum |A_gamma|^2          = %.6e" % diag)
    emit("   rho = A^*G A / sum|A|^2  = %.6f      (sampling gave ~1)" % rho_ratio)
    emit("   requirement: int|Delta|^2 ~ N*Y*A^*GA, target h*N = Y*N, so the")
    emit("                criterion is A^*G A = o(1); here A^*G A = %.6e  (margin %.1fx)"
         % (quad, 1.0 / quad if quad > 0 else float("inf")))
    emit("   lambda_max = %.6f   (M = %d, ratio %.6f)" % (w[-1], M, w[-1] / M))
    top = np.argsort(np.abs(w * proj))[::-1][:3]
    for k in top:
        emit("   lambda=%12.6f  |<A,v>|^2=%14.6e  contributes %14.6e"
             % (w[k], proj[k], w[k] * proj[k]))
    # how much of the form comes from the top eigenvector
    tot = float(np.sum(w * proj))
    emit("   share of top eigenvector in the form = %.6f" % (w[top[0]] * proj[top[0]] / tot))
    emit("")

emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  The identity is now EXACT: no sampling, no quadrature error.")
emit("  rho = A^*GA / sum|A|^2 compares the form with the diagonal: rho near 1")
emit("  means no cancellation beyond the diagonal, rho below 1 means some.")
emit("  The criterion for the requirement o(hN) is A^*G A = o(1).")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
