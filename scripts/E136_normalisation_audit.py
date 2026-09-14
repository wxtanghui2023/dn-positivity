#!/usr/bin/env python3
"""E136 -- normalisation audit: cutoff/weight sweep with R(T) monitored, and the scale check.

唐先生's audit plan (2026-09-14), rows to be filled:
   (row1) zero weights  : E130's A_gamma  vs  the true explicit-formula B_gamma
   (row2) phase         : e^{i gamma log x}  vs  N^{i gamma} e^{i gamma log(x/N)}
   (row3) truncation    : gamma <= 3T  vs  smooth weight / tail
   (row4) overall scale : Q  vs  J/(hN)

This script does (row1) numerically for the cutoff/weight question (sec.1 of his plan):
keep EVERYTHING else fixed and change only the truncation, monitoring
        R(G) = Q(G) / sum_{gamma<=G} |A_gamma|^2 .
If R is stable as G grows, the observed decay of Q is just the 1/gamma weight, not a
missing explicit-formula tail.  If R drifts, a tail is being wrongly removed.

Q is evaluated WITHOUT forming the full Gram matrix (memory-safe): the quadratic form
        Q = sum_{g,g'} A_g conj(A_g') K_Y(g - g')
is accumulated in row chunks, with K_Y(d) = ((N+Y)^{1+i d} - N^{1+i d})/((1+i d)Y).

Two extra layers are appended for large G, where the dense matrix is impossible:
   - the diagonal tail  sum_{gamma>G} |A_gamma|^2   (off-diagonal is negligible there
     because |K_Y(d)| ~ T_Y/|d| -> 0 once |d| >> T_Y = N/Y),
   - and the smooth-weight variants  exp(-(g/T)^2)  and  (1-(g/T)^2)_+^2  applied to the
     weights, again monitoring R.

INPUT
  data/zeros_odlyzko_2M.npy

OUTPUT
  scripts/E136_normalisation_audit.txt

PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 "normalisation audit" directive; no RH used;
  no Lean run; numerics are evidence, not proof.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E136_normalisation_audit.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

T = 1000.0
N = T * T
Y = T
u = np.log1p(Y / N)
CH = 120                     # rows per chunk (memory + speed)

lines = []
def emit(s=""):
    lines.append(s); print(s)

def KY(d):
    return ((N + Y) ** (1.0 + 1j * d) - N ** (1.0 + 1j * d)) / ((1.0 + 1j * d) * Y)

def A_of(g, w=None):
    rho = 0.5 + 1j * g
    a = (np.exp(u * rho) - 1.0) / rho
    return a if w is None else a * w

def Qform(g, w=None):
    """Q = A^* G A, accumulated in chunks over rows (no full matrix)."""
    a = A_of(g, w)
    tot = 0.0 + 0.0j
    m = len(g)
    for s in range(0, m, CH):
        e = min(s + CH, m)
        blk = a[s:e][:, None] * np.conj(a)[None, :]
        tot += np.sum(blk * KY(g[s:e][:, None] - g[None, :]))
    return float(np.real(tot)), float(np.sum(np.abs(a) ** 2))

emit("E136 -- normalisation audit (row 3: truncation / weight), T = %.1f, N = %.3g, Y = %.1f" % (T, N, Y))
emit("zeros: %d, max ordinate %.6f" % (len(zeros), zeros[-1]))
emit("")
emit("Q is evaluated by chunked accumulation (no dense Gram) -> memory safe.")
emit("")
emit("%14s %8s %16s %16s %12s" % ("weight/truncation", "M", "Q", "sum|A|^2", "R = Q/sum"))
emit("-" * 74)

for G, tag in [(T, "cut gamma<=T"), (3 * T, "cut gamma<=3T"), (10 * T, "cut gamma<=10T")]:
    g = zeros[zeros <= G]
    Q, s2 = Qform(g)
    emit("%14s %8d %16.6e %16.6e %12.6f" % (tag, len(g), Q, s2, Q / s2))

emit("")
# smooth weights, cutoff at 10T to keep the cost bounded
G = 10 * T
g = zeros[zeros <= G]
for nm, w in [("flat (w=1)", None),
              ("exp(-(g/T)^2)", np.exp(-(g / T) ** 2)),
              ("(1-(g/T)^2)_+^2", np.clip(1.0 - (g / T) ** 2, 0.0, None) ** 2)]:
    Q, s2 = Qform(g, w)
    emit("%14s %8d %16.6e %16.6e %12.6f" % (nm, len(g), Q, s2, Q / s2))

emit("")
# diagonal tail beyond the cutoff (off-diagonal negligible there)
for G0, tag in [(3 * T, "tail beyond 3T"), (10 * T, "tail beyond 10T"), (300 * T, "tail beyond 300T")]:
    gt = zeros[zeros > G0]
    a = A_of(gt)
    emit("%14s %8d   diag tail = %16.6e" % (tag, len(gt), float(np.sum(np.abs(a) ** 2))))

emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  R stable as the cutoff grows  -> the decay of Q is just the 1/gamma weight;")
emit("                                   no explicit-formula tail is being lost.")
emit("  R drifting with the cutoff    -> a tail is being wrongly removed.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
