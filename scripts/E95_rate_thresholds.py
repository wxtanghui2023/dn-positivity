"""E95 - the hard criterion for the S-level remainder: rate thresholds.

PURPOSE
  E94 established that Karatsuba's Theorem 4 controls the FIRST INTEGRAL of the
  counting error, not the counting error itself, so E93's remainder term is only a
  candidate until an S-level remainder bound is found inside the proof of Theorem C.
  This script computes, for each candidate rate of that remainder's squared norm,
  the largest admissible implicit constant, i.e. the threshold that decides LIVE
  versus DEAD for the E93 ledger.

  Model: ||R_S||_2^2 = C * H * M(T), so the Abel remainder term is
        int R K  <= ||R||_2 sqrt(E_phi) = sqrt(C) * H * sqrt(Lambda_inf * M(T)),
  and it must fit in allowance - prime_side.

INPUT
  none (closed-form arithmetic); constants from E93/E94 scripts and docs/E82.

OUTPUT
  scripts/E95_rate_thresholds.txt (beside this script).

CONCLUSION
  see the .txt.  No RH used, no Lean run.
PROVENANCE
  written by 小灵 on 唐先生's instruction 2026-09-13 20:58; proof structure read from
  data/karatsuba1996_thmC_excerpt.txt and PDF pages 927-931 (mathnet.ru, im86_eng.pdf).
"""
import math

T0 = 1132490.658714411
n = T0 * T0
lam = math.sqrt(n)
lo = math.sqrt(n / 11.0)
H = lam - lo
L = math.log(T0)
loglog = math.log(L)

Ephi = (11.0 ** 1.5 - 1.0) / 3.0 * lam
Lam_inf = Ephi / H
allow = 0.8 * 2001052.0 - 538184.0
prime = 2.401189e4                      # E94, with x = H
budget = allow - prime

print("E95 - rate thresholds for the S-level remainder")
print(f"H={H:.6e}  L={L:.6f}  loglog T={loglog:.6f}")
print(f"Lambda_inf={Lam_inf:.6f}  allowance={allow:.6e}  prime side={prime:.6e}")
print(f"budget for the remainder = {budget:.6e}")
print()

rates = [
    ("L^-2      (Theorem 4 rate, but for S1)", 1.0 / L ** 2),
    ("L^-1      (the intermediate candidate)", 1.0 / L),
    ("L^-1/2    (weaker than needed?)", 1.0 / math.sqrt(L)),
    ("(loglog)^-1/2  (the visible (51) rate)", 1.0 / math.sqrt(loglog)),
    ("(loglog)^-1    (weaker still)", 1.0 / loglog),
    ("1         (no decay at all)", 1.0),
]
for name, M in rates:
    width = math.sqrt(Lam_inf * M)          # sqrt(Lambda_inf * M)
    unit = H * width                        # remainder term with C = 1
    Cmax = (budget / unit) ** 2
    verdict = "LIVE" if Cmax >= 1.0 else "DEAD unless C<=%.3f" % Cmax
    print(f"  {name:42s} M={M:.6e}  sqrt(Lam*M)={width:8.4f}  term(C=1)={unit:.4e}  C_max={Cmax:9.4f}  {verdict}")

print()
print("Reference points")
print(f"  E93's choice (M = L^-2) gave term = 2.335084e5 and margin {allow/(prime+2.335084e5):.4f}x")
print(f"  M = L^-1 would still pass with C <= {((budget/(H*math.sqrt(Lam_inf/L)))**2):.4f}")
print(f"  M = (loglog)^-1/2 needs C <= {((budget/(H*math.sqrt(Lam_inf/math.sqrt(loglog))))**2):.4f}  -> essentially DEAD")
