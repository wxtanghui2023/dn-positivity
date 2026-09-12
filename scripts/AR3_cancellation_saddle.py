#!/usr/bin/env python3
"""
AR3: Error structure of the binomial route -- location of the saddle

For  lambda_n = sum_{j=1}^{n} (-1)^{j+1} C(n,j) Z_j   define  T_j := (-1)^{j+1} C(n,j) Z_j.
The sum is massively cancelling.  We tabulate T_j, the partial sums, and locate
  * j_peak = argmax_j |T_j|           (the saddle of the summand)
  * j_bar  = sum j|T_j| / sum |T_j|   (mean index)
  * the "dominant range"  { j : |T_j| >= (1/10) max |T_j| }
  * cancellation = sum|T_j| / |lambda_n|  (decimal digits lost by cancellation)
and compare the observed saddle with the model prediction j ~ n/(1+r), r = |rho_1| = 14.1347...

Z_j are taken from the zero table (equivalently from the arithmetic formula; see AR1),
so that Z_j itself is known to ~18 digits for every j used.

Inputs : data/zeros_odlyzko_2M.npy
Outputs: scripts/AR3_cancellation_saddle.txt
"""
import os, time
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ZP = os.path.join(ROOT, 'data', 'zeros_odlyzko_2M.npy')
OUT = []


def emit(s=''):
    print(s)
    OUT.append(str(s))


T0 = time.time()
gam = np.sort(np.load(ZP).astype(np.float64).ravel())
gam = gam[gam > 0.5]
JMAX = 320
z = (np.longdouble(0.5) + 1j * gam.astype(np.longdouble))
Z = {}
for j in range(1, JMAX + 1):
    Z[j] = 2 * np.real(np.sum(z ** (-j)))
emit("Z_j computed from %d zeros, j=1..%d" % (gam.size, JMAX))

R1 = float(gam[0])
emit("first zero gamma_1 = %.10f  ->  model saddle j ~ n/(1+gamma_1) = n/%.4f" % (R1, 1 + R1))

NS = [20, 40, 60, 80, 100, 150, 200, 300]
mp.mp.dps = 60
summary = []
for n in NS:
    T = [mp.mpf(0)] * (n + 1)
    for j in range(1, n + 1):
        T[j] = (-1) ** (j + 1) * mp.binomial(n, j) * mp.mpf(repr(float(Z[j])))
    absT = [abs(T[j]) for j in range(1, n + 1)]
    jpk = 1 + int(np.argmax([float(a) for a in absT]))
    S = mp.fsum(absT)
    lam = mp.fsum(T[1:])
    jbar = mp.fsum([j * absT[j - 1] for j in range(1, n + 1)]) / S
    cancel = S / abs(lam)
    summary.append((n, jpk, float(jbar), cancel, lam, S))
    if n in (60, 200, 300):
        emit()
        emit("-" * 92)
        emit("n = %d :  full summand table   T_j = (-1)^{j+1} C(n,j) Z_j" % n)
        emit("-" * 92)
        emit("%5s %-26s %-26s" % ("j", "T_j", "partial sum"))
        run = mp.mpf(0)
        for j in range(1, n + 1):
            run += T[j]
            if j <= 12 or j % 5 == 0 or abs(T[j]) > abs(T[jpk]) / 2000:
                emit("%5d %-26s %-26s" % (j, mp.nstr(T[j], 16), mp.nstr(run, 16)))
        emit("   lambda_n = %s    sum|T_j| = %s    cancellation = %s (= %s digits)"
             % (mp.nstr(lam, 16), mp.nstr(S, 12), mp.nstr(cancel, 8), mp.nstr(mp.log10(cancel), 6)))

emit()
emit("=" * 118)
emit("TASK 3   saddle location and cancellation, by n")
emit("=" * 118)
emit("%5s %7s %8s %10s %14s %14s %10s %10s" %
     ("n", "j_peak", "j_bar", "j_peak/n", "|T_jpeak|", "sum|T_j|", "cancel", "digits"))
for (n, jpk, jbar, cancel, lam, S) in summary:
    emit("%5d %7d %8.2f %10.4f %14s %14s %10s %10.2f" %
         (n, jpk, jbar, jpk / n, mp.nstr(abs(mp.mpf(repr(float(Z[jpk])))) * mp.binomial(n, jpk), 6),
          mp.nstr(S, 6), mp.nstr(cancel, 6), float(mp.log10(cancel))))
emit()
emit("observed peak index vs n/(1+gamma_1):")
for (n, jpk, jbar, cancel, lam, S) in summary:
    emit("   n=%-4d  j_peak=%-4d   n/(1+gamma_1)=%8.3f   n/j_peak=%7.4f  (1+gamma_1=%7.4f)"
         % (n, jpk, n / (1 + R1), n / jpk, 1 + R1))
emit()
emit("precision budget of the arithmetic route (decimal digits):")
emit("   part 1: Z_j from 1-(1-2^-j)z(j)+(-1)^j eta_{j-1} loses  D1(j)=log10(14/3)*j = 0.6690*j digits")
emit("   part 2: the transform itself loses         D2(n)=log10(sum|T_j|/|lambda_n|)")
emit("%5s %8s %10s %10s %10s" % ("n", "j_peak", "D1(jpk)", "D2(n)", "total"))
for (n, jpk, jbar, cancel, lam, S) in summary:
    d1 = 0.6690 * jpk
    d2 = float(mp.log10(cancel))
    emit("%5d %8d %10.1f %10.2f %10.1f" % (n, jpk, d1, d2, d1 + d2))
emit()
emit("(D1 uses the AR1-verified cancellation ratio  |Z_j| / |pieces| ~ (3/14)^j ;")
emit(" cf. AR1 table: j=25 gives 16.6 digits, i.e. 0.664*j.)")

with open(os.path.join(HERE, 'AR3_cancellation_saddle.txt'), 'w') as f:
    f.write("\n".join(OUT) + "\n")
print("\n[AR3 done, %.1fs]" % (time.time() - T0))
