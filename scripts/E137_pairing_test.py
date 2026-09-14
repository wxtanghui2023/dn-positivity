#!/usr/bin/env python3
"""E137 (7 three-way test) -- A: algebraic pairing, B: cutoff comparison, C: tail scale.

唐先生's design (2026-09-14).  Goal is NOT to find support for (7) but to decide whether
conditional convergence / pairing can possibly be the break point.

  A) F_G^pm(y)  (explicit sum over +-gamma)  vs  F_G^pair(y) = 2 Re sum_{0<gamma<=G}(...)
     must agree to machine precision; D_G = ||F^pm - F^pair||_2 / ||F^pm||_2 ~ 1e-16.
     If so, "pairing" adds nothing and (7) is a tautology for a symmetric cutoff.
  B) Q_pair(G) vs Q_sharp(G) at G = T_eff, 3 T_eff, 10 T_eff; compare with E136.
  C) E_pair(G, dG) = (1/Y) int |F_{G+dG}^pair - F_G^sharp|^2 dy  versus Q_G.

Also recorded: the E130 object is the COMPLEX positive-gamma sum, whereas the physical
object is the symmetrised REAL field 2Re(...).  The two differ by a factor of order 2 in
the mean square, not in order.  And per 唐先生 sec.6, the full explicit formula also carries
the main term (which cancels after the short-interval difference), the constant
-zeta'/zeta(0) (cancels) and the trivial-zero correction (tiny), so Q_E130 = J_psi/(hN) only
after those are shown to be o(1).

INPUT  data/zeros_odlyzko_2M.npy
OUTPUT scripts/E137_pairing_test.txt
PROVENANCE  written by 小灵 on 唐先生's 2026-09-14 directive; no RH; no Lean; numerics evidence.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E137_pairing_test.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))
CH = 200
NG = 400

N = 1.0e6
Y = np.sqrt(N)
T = Y
h = Y                     # lambda = 1  (E130 convention)
u = np.log1p(h / N)
Teff = 1.0 / u

lines = []
def emit(s=""):
    lines.append(s); print(s)

ys = np.linspace(0.0, Y, NG)

def field(Gcut, y, sym):
    """sym=False: complex sum over gamma>0 (E130 object).
       sym=True : 2 Re of the same sum (the physical symmetrised field)."""
    g = zeros[zeros <= Gcut]
    rho = 0.5 + 1j * g
    A = (np.exp(u * rho) - 1.0) / rho
    ph = A * np.exp(1j * g * np.log(N)) * np.exp(rho * np.log1p(y / N))
    tot = 0.0 + 0.0j
    for a0 in range(0, len(g), CH):
        b0 = min(a0 + CH, len(g))
        tot += np.sum(ph[a0:b0])
    return 2.0 * tot.real if sym else tot

def field_pm(Gcut, y):
    """explicit +- gamma sum: B_rho + B_rhobar = 2 Re B_rho, done term by term."""
    g = zeros[zeros <= Gcut]
    rho = 0.5 + 1j * g
    A = (np.exp(u * rho) - 1.0) / rho
    base = A * np.exp(1j * g * np.log(N)) * np.exp(rho * np.log1p(y / N))
    rho2 = 0.5 - 1j * g
    A2 = (np.exp(u * rho2) - 1.0) / rho2
    base2 = A2 * np.exp(-1j * g * np.log(N)) * np.exp(rho2 * np.log1p(y / N))
    tot = 0.0 + 0.0j
    for a0 in range(0, len(g), CH):
        b0 = min(a0 + CH, len(g))
        tot += np.sum(base[a0:b0] + base2[a0:b0])
    return tot

emit("E137-(7) three-way test   N=%.1f Y=%.1f h=%.1f  T_eff=%.3f" % (N, Y, h, Teff))
emit("")

# ---- A: algebraic pairing ----
Gcut = 3 * Teff
Fpm = np.array([field_pm(Gcut, y) for y in ys])
Fpair = np.array([field(Gcut, y, True) for y in ys])
n1 = np.linalg.norm(Fpm); n2 = np.linalg.norm(Fpm - Fpair)
emit("(A) algebraic pairing at G = 3 T_eff = %.1f" % Gcut)
emit("    |F^pm| = %.6e   |F^pm - F^pair| = %.6e   D_G = %.3e"
     % (n1, n2, n2 / n1 if n1 else float("nan")))
emit("    (D_G at machine level  ->  pairing adds nothing; (7) is a tautology here)")
emit("")

# ---- B: cutoff comparison, sharp vs paired, and vs the complex object ----
emit("(B) Q at three cutoffs:  sharp(+-) | paired(2Re) | complex(E130 object)")
emit("%12s %16s %16s %16s" % ("G", "Q_sharp", "Q_pair", "Q_complex"))
for c in [1.0, 3.0, 10.0]:
    G = c * Teff
    Qs = float(np.mean([abs(field_pm(G, y)) ** 2 for y in ys]))
    Qp = float(np.mean([field(G, y, True) ** 2 for y in ys]))
    Qc = float(np.mean([abs(field(G, y, False)) ** 2 for y in ys]))
    emit("%12.1f %16.6e %16.6e %16.6e" % (G, Qs, Qp, Qc))
emit("")

# ---- C: tail increment scale ----
emit("(C) tail increment  E_pair(G,dG)/(Q_G)   with dG = G")
emit("%12s %12s %16s %16s %10s" % ("G", "dG", "E_pair", "Q_G(pair)", "ratio"))
for c in [1.0, 3.0, 10.0]:
    G = c * Teff
    dG = G
    R = np.array([field(G + dG, y, True) - field_pm(G, y) for y in ys])
    Ep = float(np.mean(np.abs(R) ** 2))
    Qp = float(np.mean([field(G, y, True) ** 2 for y in ys]))
    emit("%12.1f %12.1f %16.6e %16.6e %10.4f" % (G, dG, Ep, Qp, Ep / Qp if Qp else float("nan")))
emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  A: D_G machine-level        -> conditional convergence / pairing is NOT the break.")
emit("  B: sharp == paired          -> the cutoff question is not a summation-convention artefact.")
emit("  C: E_pair/Q_G -> 0          -> no same-scale tail correction; (7) dead.")
emit("     E_pair/Q_G -> O(1)       -> (7) could be a real break point.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
