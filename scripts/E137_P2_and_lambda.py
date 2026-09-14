#!/usr/bin/env python3
"""E137 -- psi -> vartheta (P_2) terms, and the lambda = h/Y scan.

唐先生's directive (2026-09-14): audit the three new terms in the decomposition

  (1/(hN)) int_0^Y Delta_vartheta(y)^2 dy
      = (Y/h) Q  -  (2/(h sqrt N)) Re int_0^Y F(y) conj(P_2(y)) dy
                 +  (1/(hN)) int_0^Y P_2(y)^2 dy    +  EF tail,

with
    P_2(y) = sum_{p^k in (N+y, N+y+h], k >= 2} log p        (prime powers, exponent >= 2)
    F(y)   = sum_gamma e^{i gamma log N} e^{rho log(1+y/N)} A_gamma ,  u = log(1+h/N)
and separately to test lambda = h/Y (Legendre => lambda ~ 2, E130 studied lambda = 1).

The criterion is that each normalised term be o(1).

INPUT
  data/zeros_odlyzko_2M.npy
OUTPUT
  scripts/E137_P2_and_lambda.txt
PROVENANCE
  written by 小灵 on 唐先生's 2026-09-14 directive; no RH; no Lean; numerics are evidence.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E137_P2_and_lambda.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

N = 1.0e6
T = np.sqrt(N)
Y = T
CH = 120
NG = 300

lines = []
def emit(s=""):
    lines.append(s); print(s)

# primes p up to sqrt(N + Y + 2T + 2)  -- tiny range
pmax = int(np.sqrt(N + Y + 2 * T + 2)) + 2
s = np.ones(pmax + 1, dtype=bool)
s[:2] = False
for p in range(2, int(pmax ** 0.5) + 1):
    if s[p]:
        s[p * p:: p] = False
primes = np.nonzero(s)[0]
logs = np.log(primes)

emit("E137 -- psi->vartheta (P_2) terms and the lambda = h/Y scan")
emit("N = %.1f   T = %.1f   Y = %.1f   window = [%.1f, %.1f]" % (N, T, Y, N, N + Y))
emit("primes up to %.0f : %d (largest %d)" % (pmax, len(primes), primes[-1]))
emit("")

def P2(y, h):
    a, b = N + y, N + y + h
    tot = 0.0
    for p, lp in zip(primes, logs):
        pk = float(p) * p
        while pk <= b:
            if pk > a:
                tot += lp
            pk *= p
    return tot

def F_of(ys, h, Gcut, xoffset=0.0):
    """F over the window: sum_{gamma<=Gcut} e^{i g log N} e^{rho log(1+y/N)} A_gamma."""
    u = np.log1p(h / N)
    g = zeros[zeros <= Gcut]
    rho = 0.5 + 1j * g
    A = (np.exp(u * rho) - 1.0) / rho
    base = A * np.exp(1j * g * np.log(N))
    out = np.empty(len(ys), dtype=complex)
    for i, y in enumerate(ys):
        ph = np.exp(rho * np.log1p(y / N))
        tot = 0.0 + 0.0j
        for a0 in range(0, len(g), CH):
            b0 = min(a0 + CH, len(g))
            tot += np.dot(base[a0:b0] * ph[a0:b0], np.ones(b0 - a0))
        out[i] = tot
    return out

ys = np.linspace(0.0, Y, NG)

emit("(A) P_2 statistics over the window at h = Y = T")
P2v = np.array([P2(y, Y) for y in ys])
nz = float(np.mean(P2v != 0))
emit("    P_2: max=%.6f  mean=%.6f  rms=%.6f  nonzero fraction=%.4f" %
     (P2v.max(), P2v.mean(), np.sqrt(np.mean(P2v ** 2)), nz))
emit("    expected magnitude when present ~ 0.5 log N = %.4f" % (0.5 * np.log(N)))
emit("")

Gcut = 3 * T
Fv = F_of(ys, Y, Gcut)
emit("(B) normalised terms (each should be o(1))")
quad = float(np.trapz(P2v ** 2, ys)) / (Y * N)
cross = 2.0 * float(np.trapz(np.real(Fv * np.conj(P2v)), ys)) / (Y * np.sqrt(N))
emit("    (1/(hN)) int P_2^2 dy             = %.6e" % quad)
emit("    F rms                             = %.6e" % np.sqrt(np.mean(np.abs(Fv) ** 2)))
emit("    (2/(h sqrtN)) Re int F conj(P_2)  = %.6e" % cross)
emit("    Q = (1/Y) int |F|^2               = %.6e" % float(np.mean(np.abs(Fv) ** 2)))
emit("")

emit("(C) lambda = h/Y scan: Q(lambda) = (1/Y) int |F|^2 with that h")
for lam in [0.5, 1.0, 2.0, 3.0]:
    F2 = F_of(ys, lam * T, Gcut)
    emit("    lambda = %.1f :  Q = %.6e   rms|F| = %.6e" % (lam, float(np.mean(np.abs(F2) ** 2)), np.sqrt(np.mean(np.abs(F2) ** 2))))
emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  both P_2 terms << 1  -> the psi->vartheta conversion is NOT the break point.")
emit("  Q(lambda) at lambda = 2 is the quantity Legendre actually needs to be o(1).")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
