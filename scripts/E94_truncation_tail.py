"""E94 - truncation tail: does requiring x <= H change the prime-side numbers?

PURPOSE
  Karatsuba's Theorem 4 asks for the truncation to satisfy T^{a/k} < x < H^{1/k}.
  For k = 1 this forces x < H, whereas the E92 stationary/non-stationary split was
  computed with x = T0.  This script redoes the prime-side sums at x = H and
  isolates the newly dropped tail e^11 < p <= H, so that the change can be measured
  rather than asserted.

  The stationary branch needs |phi'| = log p on the band, i.e. log p in [1, 11],
  i.e. p <= e^11 = 59874; since H = 7.91e5 > e^11, no stationary prime is lost.

INPUT
  none (closed-form arithmetic); constants from the project's verified-height
  record: T0 = 1132490.658714411, band I = [sqrt(n/11), sqrt(n)], n = T0^2.

OUTPUT
  scripts/E94_truncation_tail.txt (beside this script).

CONCLUSION
  the tail contributes about 15 out of a total (A) near 30, and the prime side
  changes by about 0.014 per cent; the ledger and the 4.13x margin are unchanged.
  No RH used, no Lean run.
PROVENANCE
  written by 小灵 on 唐先生's instruction 2026-09-13 20:56; inputs = E92/E93 scripts.
"""
import math

T0 = 1132490.658714411
n = T0 * T0
lam = math.sqrt(n)
lo = math.sqrt(n / 11.0)
hi = lam
H = hi - lo
X = int(T0)
Xh = int(H)


def sieve(N):
    s = bytearray([1]) * (N + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(2, N + 1) if s[i]]


pr = sieve(X)
mind = abs(-4.0 * n / (4.0 * hi * hi + 1.0))      # |phi'|_min = 1 on the band


def c(p):
    return 1.0 / math.sqrt(p)                      # Lambda(p)/(sqrt(p) log p)


def nonstat(p):
    return 2.0 * c(p) / (mind + math.log(p))


print("E94 - truncation tail: does x<=H change the prime-side numbers?")
print(f"H={H:.6e}  X=T0={X}  H_as_int={Xh}  e^11={math.exp(11):.6e}  H>e^11={H > math.exp(11)}")
A_T0 = sum(nonstat(p) for p in pr)
A_H = sum(nonstat(p) for p in pr if p <= Xh)
tail = sum(nonstat(p) for p in pr if math.exp(11) < p <= Xh)
print(f"(A) with X=T0      = {A_T0:.6e}")
print(f"(A) with x=H       = {A_H:.6e}")
print(f"    tail e^11<p<=H = {tail:.6e}   ({(A_T0 - A_H) / A_T0 * 100:.3f}% of (A))")

B = 0.0
cnt = 0
for p in pr:
    lp = math.log(p)
    if not (mind <= lp <= abs(-4.0 * n / (4.0 * lo * lo + 1.0))):
        continue
    tp = math.sqrt(max((4.0 * n / lp - 1.0) / 4.0, 0.0))
    if not (lo <= tp <= hi):
        continue
    B += c(p) * math.sqrt(2.0 * math.pi / abs(32.0 * n * tp / (4.0 * tp * tp + 1.0) ** 2))
    cnt += 1
print(f"(B) stationary (x>=e^11 keeps all) = {B:.6e}  (#{cnt})")

prime = A_H + B
rem = math.sqrt(H / math.log(T0) ** 2) * math.sqrt((11.0 ** 1.5 - 1.0) / 3.0 * lam)
allow = 0.8 * 2001052.0 - 538184.0
print(f"\nLEDGER with x=H : prime side = {prime:.6e}")
print(f"                 remainder(Thm4 form) = {rem:.6e}")
print(f"                 TOTAL = {prime + rem:.6e}  vs allowance {allow:.6e}"
      f"  -> margin {allow / (prime + rem):.4f}x")

print("\nCONSTANT THRESHOLD (constant enters under the square root):")
Cmax = ((allow - prime) / rem) ** 2
print(f"  need sqrt(C)*rem_unit + prime <= allow, rem_unit={rem:.6e}")
print(f"  C_Th4 <= ((allow-prime)/rem)^2 = {Cmax:.3f}")
print("  (the earlier figure 4.45 omitted the square root)")
