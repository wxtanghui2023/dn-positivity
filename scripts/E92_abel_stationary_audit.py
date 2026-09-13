"""E92 - the explicit-formula / stationary-phase audit of the Abel term D_I.

PURPOSE
  To execute Tang's section-10 proposal: expand S(t) by the explicit formula,
  split the kernel K_n(t) = phi'(t) exp(i phi(t)) against each prime-side
  frequency, and bound every resulting integral by stationary/non-stationary
  phase.  Two quantities are computed:

    (A) the NON-stationary (integration-by-parts) bound for the '-' branch,
        phase Phi_m(t) = phi(t) - t log m, derivative -(4n/(4t^2+1)) - log m,
        which is strictly negative on the band (so no stationary point);

    (B) the STATIONARY contribution of the '+' branch, phase
        Phi_m(t) = phi(t) + t log m, derivative phi'(t) + log m, which DOES
        vanish inside the band whenever log m lies in [1, 11].

  (B) is the correction to Tang's claim: the sin(k t log p) expansion produces
  both branches, and only the '-' branch is stationary-free.

INPUT
  none (pure closed-form arithmetic); constants taken from the project's
  verified-height data record: T0 = 1132490.658714411, n = T0^2, band
  I = [sqrt(n/11), sqrt(n)].

OUTPUT
  scripts/E92_abel_stationary_audit.txt (written beside this script).

CONCLUSION
  see the .txt and docs/E92-*.md; no RH used, no Lean run.
PROVENANCE
  written by 小灵 on 唐先生's instruction, 2026-09-13; theorem input is
  Karatsuba 1996 Theorem C restated in docs/E90.
"""
import math

T0 = 1132490.658714411
n = T0 * T0
lam = math.sqrt(n)                 # = T0
lo = math.sqrt(n / 11.0)
hi = lam

def phi(t):   return n * 2.0 * math.atan(1.0 / (2.0 * t))
def dphi(t):  return -4.0 * n / (4.0 * t * t + 1.0)
def ddphi(t): return 32.0 * n * t / (4.0 * t * t + 1.0) ** 2

# sieve primes up to X (explicit-formula truncation); take X = T0
X = int(T0)
sieve = bytearray([1]) * (X + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(X ** 0.5) + 1):
    if sieve[i]:
        sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [i for i in range(2, X + 1) if sieve[i]]

# mu bar: c_m = Lambda(m)/(sqrt(m) log m); primes first, then prime powers
def cm(p, k):
    m = p ** k
    return math.log(p) / (math.sqrt(m) * math.log(m))

allowance = 1.063e6     # E82 ledger, fast+middle budget after the deep region
H = hi - lo

print("E92 - Abel term split against prime-side frequencies")
print(f"T0={T0:.6f}  n={n:.6e}  sqrt(n)={lam:.6f}")
print(f"band I=[{lo:.6f},{hi:.6f}]  |I|=H={H:.6e}")
print(f"|phi'| on band: [{abs(dphi(hi)):.6f}, {abs(dphi(lo)):.6f}]")
print(f"truncation X={X}, #primes={len(primes)}")
print()
print("(A) NON-STATIONARY bound, '-' branch: |int| <= 2 c_p / min|Phi'|, min|Phi'| = |phi'|_min + log p")
A = 0.0
for p in primes:
    A += 2.0 * cm(p, 1) / (abs(dphi(hi)) + math.log(p))
print(f"    total (A) = {A:.6e}")
print()
print("(B) STATIONARY contribution, '+' branch: phi'(t) + log p = 0 at t_p = sqrt(n/log p)")
print("    inside the band iff log p in [1, 11] i.e. p in [e, e^11]")
B = 0.0
detail = []
for p in primes:
    lp = math.log(p)
    if not (abs(dphi(lo)) >= lp >= abs(dphi(hi))):
        continue
    tp = math.sqrt(max((4.0 * n / lp - 1.0) / 4.0, 0.0))
    if not (lo <= tp <= hi):
        continue
    w = math.sqrt(2.0 * math.pi / abs(ddphi(tp)))
    contrib = cm(p, 1) * w
    B += contrib
    detail.append((p, tp, w, contrib))
print(f"    #stationary primes = {len(detail)} (largest few):")
for p, tp, w, c in detail[-6:]:
    print(f"      p={p:>7}  t_p={tp:.6e}  width={w:.4e}  contrib={c:.4e}")
print(f"    total (B) = {B:.6e}")
print()
print(f"    allowance (E82 fast+middle budget) = {allowance:.6e}")
print(f"    (A)+(B) = {A+B:.6e}   ratio to allowance = {(A+B)/allowance:.3e}")
print()
print("(C) CONSISTENCY: Cauchy-Schwarz route without the spurious 1/sqrt(2pi)")
S2_main = H * math.log(math.log(T0)) / (2.0 * math.pi ** 2)
Ephi = (11.0 ** 1.5 - 1.0) / 3.0 * lam + 0.0
Dcs = math.sqrt(S2_main) * math.sqrt(Ephi)
print(f"    int S^2 (main) = {S2_main:.6e}   E_phi = {Ephi:.6e}")
print(f"    D_CS = sqrt(S^2)*sqrt(E_phi) = {Dcs:.6e}")
print(f"    ratio to allowance = {Dcs/allowance:.4f}  (>1 means dead)")
Lambda_inf = (11.0 ** 1.5 - 1.0) / (3.0 * (1.0 - 11.0 ** -0.5))
print(f"    Lambda_inf = E_phi/H -> {Lambda_inf:.6f}")
print(f"    |D_I|/H  <=  sqrt(Lambda_inf/(2 pi^2)) * sqrt(loglog T)"
      f" = {math.sqrt(Lambda_inf/(2*math.pi**2)):.6f} * sqrt(loglog T)")
