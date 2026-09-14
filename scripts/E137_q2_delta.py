#!/usr/bin/env python3
"""E137 (final) -- psi -> vartheta at the CORRECT arithmetic scale N = q^2 - delta.

唐先生's arithmetic correction (2026-09-14): with h = 2 sqrt(N), Y = sqrt(N) and N = p^2,

    sqrt(N + Y + h) = sqrt(p^2 + 3p) = p + 3/2 + O(1/p),

so the square-root range is (p, p + 1.5], which contains NO prime because p + 1 is even for
odd p and the next prime is at least p + 2.  Hence N = p^2 NEVER yields P_2 != 0.

Correct choice:  N = q^2 - delta,  q prime,  0 < delta < 3q,  which places q^2 inside
(N, N + Y + h].  With one square prime inside, P_2 is a single jump:

    P_2(y) = log q * 1_{y >= y0},     y0 = q^2 - N - h = delta - h,
    Q_2    = (Y - max(y0,0))/(hN) * (log q)^2,
    C_psi2 = (log q)/(h sqrt N) * Re int_{max(y0,0)}^Y F(y) dy,
    Q_theta = Q_psi - 2 C_psi2 + Q_2.

Reported for several delta/q (so q^2 sits at different positions in the window) and two primes q.
Verdict criteria (唐先生): Q_theta ~ Q_psi -> P_2 is lower order, paradox persists;
2 C_psi2 of the order of Q_psi -> the missing same-scale cancellation is found;
Q_theta not -> 0 while Q_psi -> 0 -> explains why E130's small Q cannot give Legendre.

INPUT  data/zeros_odlyzko_2M.npy
OUTPUT scripts/E137_q2_delta.txt
PROVENANCE  written by 小灵 on 唐先生's 2026-09-14 directive; no RH; no Lean; numerics are evidence.
"""
import os
import resource
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "E137_q2_delta.txt")
zeros = np.load(os.path.join(HERE, "..", "data", "zeros_odlyzko_2M.npy"))
CH = 120
NG = 600

lines = []
def emit(s=""):
    lines.append(s); print(s)

def F_all(N, h, Gcut, ys):
    Y = np.sqrt(N)
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

emit("E137 (final) -- psi->vartheta at N = q^2 - delta  (lambda = h/Y = 2, Legendre)")
emit("zeros: %d" % len(zeros))
emit("")
emit("%6s %8s %10s %10s %10s %12s %10s %12s" %
     ("q", "delta/q", "N", "Y", "y0/Y", "Q_psi", "Q_2", "C_psi2"))
emit("-" * 96)

rows = []
for q in [997, 1009]:
    lq = np.log(q)
    for frac in [0.25, 1.0, 2.0, 2.4, 2.7]:
        delta = frac * q
        N = q * q - delta
        Y = np.sqrt(N)
        h = 2.0 * Y
        y0 = delta - h
        Gcut = 10.0 / np.log1p(h / N)
        ys = np.linspace(0.0, Y, NG)
        Fv = F_all(N, h, Gcut, ys)
        Q_psi = float(np.mean(np.abs(Fv) ** 2))
        ya = max(y0, 0.0)
        fracwin = max(0.0, (Y - ya) / Y)
        Q2 = fracwin * lq ** 2 / (h * N) * Y / Y  # = (Y-ya)*lq^2/(hN)
        Q2 = (Y - ya) * lq ** 2 / (h * N) if ya < Y else 0.0
        # C_psi2 = (log q)/(h sqrtN) * Re int_{ya}^{Y} F dy
        m = ys >= ya
        integ = float(np.trapz(np.real(Fv[m]), ys[m])) if m.sum() > 1 else 0.0
        C2 = lq * integ / (h * np.sqrt(N))
        rows.append((q, frac, N, Y, y0 / Y, Q_psi, Q2, C2))
        emit("%6d %8.2f %10.6g %10.3f %10.3f %12.6e %10.3e %12.6e"
             % (q, frac, N, Y, y0 / Y, Q_psi, Q2, C2))

emit("")
emit("Q_theta = Q_psi - 2 C_psi2 + Q_2")
emit("%6s %8s %14s %14s %14s %14s %12s" %
     ("q", "delta/q", "Q_psi", "Q_theta", "2C_psi2", "Q_theta/Q_psi", "2C2/Q_psi"))
emit("-" * 96)
for (q, frac, N, Y, y0r, Qp, Q2, C2) in rows:
    Qt = Qp - 2 * C2 + Q2
    emit("%6d %8.2f %14.6e %14.6e %14.6e %14.6f %12.4f"
         % (q, frac, Qp, Qt, 2 * C2, Qt / Qp if Qp else float("nan"), (2 * C2) / Qp if Qp else float("nan")))

emit("")
emit("peak RSS = %.1f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
emit("")
emit("READING")
emit("  Q_theta ~ Q_psi      -> P_2 is a lower-order correction; the paradox persists.")
emit("  2 C_psi2 ~ Q_psi     -> the missing same-scale cancellation term is FOUND.")
emit("  Q_theta not -> 0 while Q_psi -> 0 -> E130's small Q cannot give Legendre.")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")
print("\nwrote %s" % OUT)
