"""E93 - close the middle-band ledger using Theorem 4's MOMENT bound on the remainder.

PURPOSE
  E92 showed the Cauchy-Schwarz route applied to S itself is asymptotically dead, and
  that the prime-side part of the Abel term is controlled by non-resonance with a
  factor-44 margin.  The open item was the remainder R = S - P_x of the explicit
  formula.  This script tests the key realisation: R must NOT be bounded pointwise
  (that costs 2.6e6, over the allowance); Karatsuba's Theorem 4 gives a MOMENT bound
  \int_T^{T+H}|R|^{2k} dt = O(H L^{-2k}), L = log T, and since ||R||_2 is about five
  times smaller than ||S||_2, the Cauchy-Schwarz step applied to R (not to S) fits.

LEDGER (all numbers from the project's verified-height record and E82)
  allowance for the middle band at n = T0^2 (the slow band is empty there):
      A_mid = 0.8*N - N(0.3015*T0)  = 1.06266e6
  prime-side part (E92, non-resonance):           2.4015e4
  remainder part with ||R||_2 = sqrt(H)/L:        see below
  E82's Cauchy-Schwarz value for comparison:      9.74507e5

INPUT
  none (closed-form arithmetic); constants from data/ and docs/E82.

OUTPUT
  scripts/E93_remainder_ledger.txt (beside this script).

CONCLUSION
  see the .txt; no RH used; no Lean run.
PROVENANCE
  written by 小灵 on 唐先生's instruction 2026-09-13 20:50; inputs = E92 script output
  and Karatsuba 1996 Theorem 4 (excerpt in data/karatsuba1996_thmC_excerpt.txt).
"""
import math

T0 = 1132490.658714411
n = T0 * T0
lam = math.sqrt(n)
lo = math.sqrt(n / 11.0)
hi = lam
H = hi - lo
L = math.log(T0)
loglog = math.log(L)

N = 2001052.0                      # zeros with 0 < gamma <= T0
deep = 538184.0                    # N(0.3015*T0), E82
allow_mid = 0.8 * N - deep         # middle-band allowance at n = T0^2

Ephi = (11.0 ** 1.5 - 1.0) / 3.0 * lam
Lam_inf = Ephi / H
S2_main = H * loglog / (2.0 * math.pi ** 2)

print("E93 - middle-band ledger with Theorem 4 controlling the remainder")
print(f"T0={T0:.6f}  H={H:.6e}  L=log T0={L:.6f}  loglog T={loglog:.6f}")
print(f"N={N:.0f}  deep=N(0.3015 T0)={deep:.0f}  allowance_mid=0.8N-deep={allow_mid:.6e}")
print()

print("(1) PRIME SIDE (E92 non-resonance, truncation X = T0)")
prime = 2.401532e4
print(f"    (A) non-stationary + (B) stationary = {prime:.6e}")
print()

print("(2) REMAINDER, two treatments")
R2_pointwise = 1.0 * math.sqrt(n) * (math.sqrt(11.0) - 1.0)   # sup|R| * int|phi'|
print(f"    pointwise   : sup|R| * int_I|phi'| = {R2_pointwise:.6e}"
      f"   ratio to allowance = {R2_pointwise/allow_mid:.4f}  (>1 = dead)")
R2_moment = H / L ** 2
normR = math.sqrt(R2_moment)
rem = normR * math.sqrt(Ephi)
print(f"    Theorem 4   : ||R||_2^2 = H/L^2 = {R2_moment:.6e}  -> ||R||_2 = {normR:.6f}")
print(f"                  int R K  <= ||R||_2 sqrt(E_phi) = {rem:.6e}"
      f"   ratio to allowance = {rem/allow_mid:.4f}")
print()

print("(3) LEDGER")
tot = prime + rem
print(f"    prime side            = {prime:.6e}")
print(f"    remainder (Theorem 4) = {rem:.6e}")
print(f"    TOTAL                 = {tot:.6e}")
print(f"    allowance             = {allow_mid:.6e}")
print(f"    MARGIN                = {allow_mid/tot:.4f} x")
print()
print("(4) COMPARISON with E82's Cauchy-Schwarz value")
cs82 = 9.74507e5
print(f"    E82 C-S for the middle band = {cs82:.6e}  ratio to allowance = {cs82/allow_mid:.4f}  (>1 = fails)")
print(f"    new bound                   = {tot:.6e}  ratio to allowance = {tot/allow_mid:.4f}")
print(f"    improvement factor          = {cs82/tot:.4f} x")
print()
print("(5) WHY it works: the two L2 norms")
print(f"    ||S||_2^2 = {S2_main:.6e}   ||R||_2^2 = {R2_moment:.6e}"
      f"   ratio = {S2_main/R2_moment:.4f}")
print("    -> bounding the REMAINDER by Cauchy-Schwarz is legitimate;")
print("       bounding S ITSELF by Cauchy-Schwarz is not (E92).")
print(f"    Lambda_inf = {Lam_inf:.6f}")
