#!/usr/bin/env python3
"""E129 -- compute the Bessel constant C exactly, and test whether it can be large.

PURPOSE
  (b) of 唐先生's instruction.  The constant in the Bessel-type bound
      || sum_gamma A_gamma phi_gamma ||^2  <=  C * sum_gamma |A_gamma|^2 ||phi_gamma||^2
  with phi_gamma(x) = e^{i gamma log x} on [N, N+Y] is, by definition, the
  largest eigenvalue of the NORMALISED GRAM MATRIX
      G_{jj'} = (1/Y) * int_N^{N+Y} e^{i (gamma_j - gamma_j') log x} dx .
  That integral is elementary:
      int_N^{N+Y} x^{i d} dx = ((N+Y)^{1+i d} - N^{1+i d}) / (1 + i d),
  so G can be built EXACTLY, with no quadrature.

  Three things are computed:
    (1) C_actual  -- lambda_max of G for the REAL zeros (several cutoffs).
    (2) C_rigid   -- lambda_max of G for a RIGID surrogate: an arithmetic
        progression with the same local density (equally spaced zeros), which
        is the configuration that would make the phases align.
    (3) C_random  -- lambda_max of G for a RANDOM surrogate (spacings drawn
        from the same local density but randomised).  This separates the two
        conceivable behaviours.

INPUT
  data/zeros_odlyzko_2M.npy

OUTPUT
  scripts/E129_bessel_constant.txt

CONCLUSION (expected)
  C_actual close to 1 confirms near-orthogonality for the real zeros, while
  C_rigid near the number of frequencies would show the constant is NOT
  universally bounded, i.e. the bound is a genuine arithmetic input.

MEMORY
  Gram matrix is M x M complex128; M is capped at 3000 (~144 MB).

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 "continue a, b" instruction; no RH
  used; no Lean run; numerics are evidence, not proof.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E129_bessel_constant.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

N = 1.0e6
Y = np.sqrt(N)                 # window = sqrt(N)
MCAP = 3000

lines = []
def emit(s=""):
    lines.append(s); print(s)

def gram_lambda_max(g):
    """lambda_max of the normalised Gram matrix for frequencies g."""
    d = g[:, None] - g[None, :]                 # M x M separations
    denom = 1.0 + 1j * d
    top = (N + Y) ** (1.0 + 1j * d) - N ** (1.0 + 1j * d)
    G = (top / denom) / Y
    w = np.linalg.eigvalsh(G)
    return float(w[-1]), float(w[0]), float(w.sum().real)

emit("E129 -- the Bessel constant C = lambda_max of the normalised Gram")
emit("N = %.1f   Y = sqrt(N) = %.3f   M capped at %d" % (N, Y, MCAP))
emit("zeros: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")
emit("%22s %8s %14s %14s %14s" % ("frequency set", "M", "lambda_max", "lambda_min", "trace/M"))
emit("-" * 78)

for G, tag in [(1.0e3, "real zeros, gamma<=T"),
               (1.5e3, "real zeros, gamma<=1.5T"),
               (2.0e3, "real zeros, gamma<=2T"),
               (3.0e3, "real zeros, gamma<=3T")]:
    g = zeros[zeros <= G]
    m = len(g)
    if m > MCAP:
        g = g[:MCAP]; m = MCAP
    lmax, lmin, tr = gram_lambda_max(g)
    emit("%22s %8d %14.6f %14.6e %14.6f" % (tag, m, lmax, lmin, tr / m))

emit("")

# rigid surrogate: arithmetic progression with the local mean spacing
for m in [649, 1500, 2629]:
    t_lo, t_hi = 1.0, 3000.0
    rigid = np.linspace(t_lo, t_hi, m)          # equally spaced = rigid
    # local density must match roughly; equally spaced is the extreme rigid case
    lmax, lmin, tr = gram_lambda_max(rigid)
    emit("RIGID (equally spaced), M=%5d : lambda_max = %14.6f  (M = %d) ratio=%.4f"
         % (m, lmax, m, lmax / m))
emit("")

# random surrogate: spacings from the local mean spacing, randomised
rng = np.random.default_rng(20260914)
for m in [649, 1500, 2629]:
    sp = rng.exponential(3000.0 / m, m)         # random spacings, matching density
    rnd = np.cumsum(sp)
    rnd -= rnd[0]
    lmax, lmin, tr = gram_lambda_max(rnd)
    emit("RANDOM (random spacings), M=%5d : lambda_max = %14.6f  (M = %d) ratio=%.4f"
         % (m, lmax, m, lmax / m))
emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  C >= 1 always (diagonal is 1, so trace/M = 1 and lambda_max >= 1).")
emit("  If RIGID gives lambda_max ~ M while REAL gives ~1, then C is NOT")
emit("  universally bounded: the bound is a genuine arithmetic input, and the")
emit("  real zeros behave like the RANDOM surrogate rather than the rigid one.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
