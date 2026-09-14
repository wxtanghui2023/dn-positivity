#!/usr/bin/env python3
"""E137 (upgrade) -- Q_lambda with the CORRECT T_eff and its truncation dependence, plus C_{psi,2}.

唐先生's revised directive (2026-09-14): E136 shows ① FAILS -- R is not stable
(0.512 / 0.769 / 0.620) and Q jumps 4.51x from T to 3T while sum|A|^2 jumps only 3x,
so the band T <~ gamma <~ 3T contributes nearly as-is and cannot be dropped.
Therefore:
  (A) run the lambda scan PROPERLY: lambda = 1, 1.5, 2, 2.5, with
      u_lambda = log(1 + h/N), h = lambda*sqrt(N), so the effective frequency scale is
          T_eff = 1/u_lambda ~ T/lambda,
      and report Q_lambda AND R_lambda = Q_lambda / sum|A_gamma^(lambda)|^2,
      at cutoffs gamma <= c*T_eff for c = 1, 3, 10 (so the truncation question is asked
      at each lambda, not once).
  (B) compute the psi->vartheta CROSS term, which is the dangerous one:
          C_{psi,2} = (1/(h sqrt N)) Re int_0^Y F(y) conj(P_2(y)) dy,
          Q_2       = (1/(hN)) int_0^Y P_2(y)^2 dy,
      with P_2(y) = sum_{k>=2} [ vartheta((N+y+h)^{1/k}) - vartheta((N+y)^{1/k}) ]
                  = sum of log p over p^k in (N+y, N+y+h], k >= 2.

Criterion: each normalised quantity must be o(1).

INPUT  data/zeros_odlyzko_2M.npy
OUTPUT scripts/E137_lambda_and_cross.txt
PROVENANCE  written by 小灵 on 唐先生's 2026-09-14 directive; no RH; no Lean; numerics are evidence.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E137_lambda_and_cross.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))

N = 1.0e6
T = np.sqrt(N)
Y = T
CH = 120
NG = 400

lines = []
def emit(s=""):
    lines.append(s); print(s)

def Q_of(h, Gcut, ygrid):
    """(1/Y) int |F|^2 over the window, F(y) = sum_{g<=Gcut} e^{i g log N} e^{rho log(1+y/N)} A_g."""
    u = np.log1p(h / N)
    g = zeros[zeros <= Gcut]
    rho = 0.5 + 1j * g
    A = (np.exp(u * rho) - 1.0) / rho
    base = A * np.exp(1j * g * np.log(N))
    tot = 0.0
    for y in ygrid:
        ph = np.exp(rho * np.log1p(y / N))
        v = 0.0 + 0.0j
        for a0 in range(0, len(g), CH):
            b0 = min(a0 + CH, len(g))
            v += np.dot(base[a0:b0] * ph[a0:b0], np.ones(b0 - a0))
        tot += abs(v) ** 2
    return tot / len(ygrid), float(np.sum(np.abs(A) ** 2))

emit("E137 (upgrade) -- lambda scan with T_eff and its truncation dependence")
emit("N = %.1f  T = %.1f  window Y = %.1f" % (N, T, Y))
emit("zeros: %d" % len(zeros))
emit("")
emit("(A) lambda scan:  h = lambda*T,  T_eff = 1/log(1+h/N),  R = Q / sum|A|^2")
emit("%8s %10s %10s %8s %16s %16s %10s" %
     ("lambda", "h", "T_eff", "cutoff", "Q", "sum|A|^2", "R"))
emit("-" * 92)
yg = np.linspace(0.0, Y, 60)
for lam in [1.0, 1.5, 2.0, 2.5]:
    h = lam * T
    u = np.log1p(h / N)
    Teff = 1.0 / u
    for c in [1.0, 3.0, 10.0]:
        Gcut = c * Teff
        Q, s2 = Q_of(h, Gcut, yg)
        emit("%8.2f %10.3f %10.3f %8.1f %16.6e %16.6e %10.6f"
             % (lam, h, Teff, Gcut, Q, s2, Q / s2))
    emit("")

# (B) the psi->vartheta cross term at lambda = 2
pmax = int(np.sqrt(N + Y + 3 * T + 2)) + 2
sv = np.ones(pmax + 1, dtype=bool)
sv[:2] = False
for p in range(2, int(pmax ** 0.5) + 1):
    if sv[p]:
        sv[p * p:: p] = False
primes = np.nonzero(sv)[0]
logs = np.log(primes)

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

def F_vec(h, Gcut, ys):
    u = np.log1p(h / N)
    g = zeros[zeros <= Gcut]
    rho = 0.5 + 1j * g
    A = (np.exp(u * rho) - 1.0) / rho
    base = A * np.exp(1j * g * np.log(N))
    out = np.empty(len(ys), dtype=complex)
    for i, y in enumerate(ys):
        ph = np.exp(rho * np.log1p(y / N))
        v = 0.0 + 0.0j
        for a0 in range(0, len(g), CH):
            b0 = min(a0 + CH, len(g))
            v += np.dot(base[a0:b0] * ph[a0:b0], np.ones(b0 - a0))
        out[i] = v
    return out

emit("(B) psi->vartheta cross term at lambda = 2 (and lambda = 1 for contrast)")
for lam in [1.0, 2.0]:
    h = lam * T
    u = np.log1p(h / N)
    Gcut = 3.0 / u
    ys = np.linspace(0.0, Y, NG)
    Fv = F_vec(h, Gcut, ys)
    P2v = np.array([P2(y, h) for y in ys])
    frac = float(np.mean(P2v != 0))
    quad = float(np.trapz(P2v ** 2, ys)) / (h * N)
    cross = 2.0 * float(np.trapz(np.real(Fv * np.conj(P2v)), ys)) / (h * np.sqrt(N))
    emit("    lambda=%.1f: P2 max=%.4f nonzero frac=%.5f | Q2=(1/hN)int P2^2=%.6e"
         % (lam, P2v.max(), frac, quad))
    emit("              Q=(1/Y)int|F|^2=%.6e | C_psi2=(2/h sqrtN)Re int F conj(P2)=%.6e"
         % (float(np.mean(np.abs(Fv) ** 2)), cross))
emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  Q_lambda must be o(1) at lambda = 2, at every cutoff c = 1, 3, 10, for Legendre.")
emit("  C_{psi,2} is the dangerous cross term; Q_2 is the safer quadratic one.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
