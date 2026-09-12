#!/usr/bin/env python3
"""
AR2: Validation of the binomial transform

    lambda_n = sum_{j=1}^{n} (-1)^{j+1} C(n,j) Z_j ,     Z_j = sum_rho rho^{-j}

Three independent evaluations of lambda_n:
  (A) ZEROS-DIRECT (project's stable form):
        lambda_n = 4 sum_{gamma>0} sin^2(n theta_gamma),  theta_gamma = arctan(1/(2 gamma))
        (= sum_rho [1-(1-1/rho)^n] on the critical line), from data/zeros_odlyzko_2M.npy,
        plus the analytic tail n^2 * coef, coef = (1/2pi)(log(T/2pi)+1)/T.
  (B) BINOMIAL with ARITHMETIC Z_j:
        Z_1 = 1+gamma/2-(1/2)log(4pi);  Z_j = 1-(1-2^{-j})zeta(j)+(-1)^j eta_{j-1}  (j>=2).
  (C) STIELTJES/EXACT (classical, no zeros):
        lambda_n = n sum_{m=1}^{n} b_m C(n-1,m-1),  b_m = [u^m] log xi(1+u),
        b_1 = gamma/2 + 1 - log2 - (1/2)log pi,
        b_m = [u^m] log(u zeta(1+u)) + (-1)^m zeta(m,3/2)/(m 2^m)   (m>=2).
        (beta_m built from Stieltjes constants and Hurwitz zeta; independent of Z_j.)

Checks lambda_1 = 0.0230957089661210338.

Inputs : data/zeros_odlyzko_2M.npy
Outputs: scripts/AR2_binomial_route.txt
"""
import os, time
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ZP = os.path.join(ROOT, 'data', 'zeros_odlyzko_2M.npy')
OUT = []
NS = [1, 2, 3, 5, 10, 20, 40, 60, 80, 100]
NMAX = max(NS)


def emit(s=''):
    print(s)
    OUT.append(str(s))


T0 = time.time()
gam = np.sort(np.load(ZP).astype(np.float64).ravel())
gam = gam[gam > 0.5]
GMAX = float(gam[-1])
emit("zeros loaded: n=%d  gamma_max=%.6g" % (gam.size, GMAX))

# ---------------------------------------------------------------- (A) zeros direct
th = np.arctan(1.0 / (2.0 * gam))
lam_zeros, lam_zerostail = {}, {}
coef_tail = (1 / (2 * np.pi)) * (np.log(GMAX / (2 * np.pi)) + 1) / GMAX
for n in NS:
    s = 4.0 * np.sum(np.sin(n * th) ** 2)
    lam_zeros[n] = s
    lam_zerostail[n] = s + n * n * coef_tail
emit("tail coef = %.6e  (tail = n^2 * coef)" % coef_tail)

# ---------------------------------------------------------------- eta, Z_j arithmetic
mp.mp.dps = 130
KG = NMAX + 4
gam_k = [mp.stieltjes(k) for k in range(KG)]
gc = [mp.mpf(0)] * (KG + 1)
gc[0] = mp.mpf(1)
for k in range(KG):
    gc[k + 1] = (-1) ** k * gam_k[k] / mp.factorial(k)
gl = [mp.mpf(0)] * (KG + 1)
for m in range(1, KG + 1):
    acc = mp.mpf(m) * gc[m]
    for k in range(1, m):
        acc -= k * gl[k] * gc[m - k]
    gl[m] = acc / mp.mpf(m)
eta = [-mp.mpf(k + 1) * gl[k + 1] for k in range(KG)]


def Z_arith(j):
    if j == 1:
        return 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    return 1 - (1 - mp.mpf(2) ** (-j)) * mp.zeta(j) + (-1) ** j * eta[j - 1]


# ---------------------------------------------------------------- (C) b_m (log xi at 1)
# b_m = d_m + (-1)^m zeta(m,3/2)/(m 2^m) for m>=2 ; b_1 = gamma/2+1-log2-(1/2)log pi
# d_m = [u^m] log(1+g(u)),  g(u) = u zeta(1+u)-1 = sum_{m>=1} (-1)^{m-1} gamma_{m-1} u^m/(m-1)!
gm_ = [mp.mpf(0)] * (NMAX + 1)
for m in range(1, NMAX + 1):
    gm_[m] = (-1) ** (m - 1) * gam_k[m - 1] / mp.factorial(m - 1)
d = [mp.mpf(0)] * (NMAX + 1)
for m in range(1, NMAX + 1):
    acc = mp.mpf(m) * gm_[m]
    for k in range(1, m):
        acc -= gm_[k] * mp.mpf(m - k) * d[m - k]
    d[m] = acc / mp.mpf(m)
b = [mp.mpf(0)] * (NMAX + 1)
b[1] = mp.euler / 2 + 1 - mp.log(2) - mp.log(mp.pi) / 2
for m in range(2, NMAX + 1):
    b[m] = d[m] + (-1) ** m * mp.zeta(m, mp.mpf(3) / 2) / (mp.mpf(m) * mp.mpf(2) ** m)
lam_exact = {}
for n in NS:
    lam_exact[n] = n * mp.fsum([b[m] * mp.binomial(n - 1, m - 1) for m in range(1, n + 1)])

# ---------------------------------------------------------------- (B) binomial + arith Z
lam_binom = {}
for n in NS:
    lam_binom[n] = mp.fsum([(-1) ** (j + 1) * mp.binomial(n, j) * Z_arith(j)
                            for j in range(1, n + 1)])

LAM1 = mp.mpf('0.0230957089661210338')
emit()
emit("=" * 118)
emit("TASK 2   lambda_n three ways")
emit("=" * 118)
emit("(A) zeros direct + tail      (B) binomial with ARITHMETIC Z_j     (C) Stieltjes/exact")
emit("%5s  %-24s %-24s %-24s" % ("n", "(A) zeros+tail", "(B) binomial(Z_arith)", "(C) Stieltjes exact"))
for n in NS:
    emit("%5d  %-24s %-24s %-24s" %
         (n, mp.nstr(mp.mpf(repr(lam_zerostail[n])), 16),
          mp.nstr(lam_binom[n], 16), mp.nstr(lam_exact[n], 16)))
emit()
emit("differences")
emit("%5s  %-26s %-26s %-26s" % ("n", "(A)-(C)", "(B)-(C)", "(A)-(B)"))
for n in NS:
    a = mp.mpf(repr(lam_zerostail[n]))
    emit("%5d  %-26s %-26s %-26s" %
         (n, mp.nstr(a - lam_exact[n], 8), mp.nstr(lam_binom[n] - lam_exact[n], 8),
          mp.nstr(a - lam_binom[n], 8)))
emit()
emit("lambda_1 check:  (C) = %s" % mp.nstr(lam_exact[1], 22))
emit("                 known = %s   diff = %s" % (mp.nstr(LAM1, 22), mp.nstr(lam_exact[1] - LAM1, 3)))
emit("b_1 = %s   (must equal lambda_1)" % mp.nstr(b[1], 20))
emit("lambda_n / (n log n) for orientation:")
for n in (10, 20, 60, 100):
    emit("   n=%-4d lambda_n = %-18s   lambda_n/(n log n) = %s"
         % (n, mp.nstr(lam_exact[n], 12), mp.nstr(lam_exact[n] / (n * mp.log(n)), 8)))

with open(os.path.join(HERE, 'AR2_binomial_route.txt'), 'w') as f:
    f.write("\n".join(OUT) + "\n")
print("\n[AR2 done, %.1fs]" % (time.time() - T0))
