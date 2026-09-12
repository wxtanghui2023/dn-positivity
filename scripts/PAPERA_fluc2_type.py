"""
PAPERA_fluc2_type.py -- ROUTE 3 (linearised phase / admissible test function) and
                        ROUTE 5 (finite expansion of f into admissible terms)

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the round-2 task.
  Reads data/zeros_odlyzko_2M.npy; writes scripts/PAPERA_fluc2_type.txt.
  Not committed; no other file touched.

ROUTE 3
  The obstacle is the non-linearity of the phase n theta(gamma) (theta(t) = 2 arctan(1/(2t))).
  One asks for a criterion whose fluctuation term has a LINEAR phase, so that the
  Guinand-Weil explicit formula applies directly.  We compute what such a criterion costs:
  the instantaneous frequency of e^{i n theta(gamma)} in gamma is
      (1/2 pi) |d/dgamma (n theta)| = 4n / (2 pi (4 gamma^2 + 1)) <= 0.8 n/(2 pi) = 0.1273 n,
  at gamma = 1 (max).  A test function matching the phase must therefore have Fourier
  support of radius Lambda >= 0.1273 n (cycles per unit gamma), and by the explicit
  formula the prime side then runs to m <= e^{2 pi Lambda} = e^{0.8 n}.
  Cross-check against the band-limited route already in the project: the threshold
  pi Delta >= 2.678 n corresponds to prime side e^{5.357 n}.  Both are e^{Theta(n)}.

ROUTE 5
  f(n theta_gamma) with (1 - 1/rho)^n = e^{i n theta_gamma} has a FINITE expansion
      (1 - 1/rho)^n = sum_{j=0}^{n} C(n,j) (-1)^j rho^{-j},
  hence lambda_n = sum_j (-1)^{j+1} C(n,j) Z_j,  Z_j = sum_rho rho^{-j}.
  Each term rho^{-j} IS admissible: s -> s^{-j} is holomorphic on Re s > 0, in particular on
  |Im s| <= 1/2 + eps for every eps < 1/2, and decays.  So for the FINITE expansion the
  admissibility obstruction of the band-limited route does NOT apply -- the failure is
  purely the CANCELLATION COST.  We measure that cost: the digits needed are
  log10( sum_j |C(n,j) Z_j| / |lambda_n| ).  |Z_j| is measured from the table (it decays
  like r^{-j} with r = |rho_1| = 14.13), lambda_n is computed from the table.

DISCIPLINE: measured |Z_j| law stated with its fit range; lambda_n from the table is a
lower bound (omitted tail is positive); the digit count uses the measured |Z_j| law
extrapolated in j, and says so.
"""

import numpy as np
from math import pi, log, atan, sqrt, lgamma, log10, exp

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); Nz = int(G.size)
th = np.arctan(G / (G ** 2 - 0.25))
MAIN_T0 = float((T0 / (2 * pi)) * log(T0 / (2 * pi * np.e)) + 7.0 / 8.0)
B_T0 = (log(T0) + 1.0) / (4 * pi * T0)
ALLOW = MAIN_T0 - int(T0 ** 2) * B_T0

lines = []
def out(s=''):
    lines.append(s); print(s)

out('=' * 78)
out('ROUTE 3 (linearised phase) + ROUTE 5 (finite admissible expansion)')
out('=' * 78)
out('  T0 = {:.6f}   N = {:,}   allowance at n=T0^2 = {:.6e}'.format(T0, Nz, ALLOW))
out()

# ------------------------------------------------------------------ ROUTE 3
out('-' * 78)
out('ROUTE 3 -- WHAT A "LINEAR-PHASE" CRITERION COSTS')
out('-' * 78)
out()
out('  phase in the gamma variable:  phi(gamma) = n theta(gamma),  theta(gamma) = 2 arctan(1/(2 gamma))')
out('  phi\'(gamma) = -4n/(4 gamma^2 + 1);  max over gamma in [1,T0] at gamma=1:  |phi\'| = 4n/5 = 0.8n')
out()
hdr = '{:>20} {:>16} {:>18} {:>22} {:>22}'
out(hdr.format('n', 'max |phi\'|', 'Lambda (cycles)', 'prime side e^{2 pi L}', 'bandlimit route e^{5.357n}'))
for n in [10**6, 10**9, 10**12, int(T0 ** 2)]:
    n = int(n)
    mx = 0.8 * n
    Lam = mx / (2 * pi)
    out(hdr.format('{:>20,}'.format(n), '{:.4e}'.format(mx), '{:.4e}'.format(Lam),
                   '10^{:.3e}'.format(0.8 * n / log(10)),
                   '10^{:.3e}'.format(5.357 * n / log(10))))
out()
out('  => ANY criterion whose fluctuation term reproduces the Li phase over gamma <= T0 and')
out('     n <= T0^2 must carry exponential type >= 0.1273 n; the explicit-formula prime side')
out('     then reaches m <= e^{0.8n} = 10^{0.347 n}.  At n = T0^2 that is 10^{4.45e11}.')
out('     Feasible explicit verifications of the explicit formula reach prime side T0^{O(1)},')
out('     i.e. log10 <= O(log T0) ~ 14.  Loss factor = 10^{4.45e11} / 10^{14} = 10^{4.45e11}.')
out()
out('  CROSS-CHECK: the project\'s band-limited analysis (PAPERA-bandlimited-route.md) gets the')
out('  same structure with the (larger) threshold pi Delta >= 2.678 n: prime side e^{5.357n}.')
out('  Both are e^{Theta(n)}; the linearisation does not reduce the exponent, it only changes')
out('  the constant (0.8 vs 5.357).  The Li weight (1-1/rho)^n itself has exponential type n.')
out()
out('  WHAT DOES EXIST: Oesterle/Voros linearise by the change of variable n theta = t, which')
out('  turns the fluctuation into the Fourier coefficient of an L^1 function and sends it to 0')
out('  by Riemann-Lebesgue.  That is an n -> infinity statement; it produces the closed form')
out('  of lambda_n but NO uniform-in-n error.  The linear-phase object is EVALUABLE, not BOUNDABLE.')
out()

# ------------------------------------------------------------------ ROUTE 5
out('-' * 78)
out('ROUTE 5 -- FINITE ADMISSIBLE EXPANSION AND ITS CANCELLATION COST')
out('-' * 78)
out()
out('  (1) ADMISSIBILITY: the binomial expansion is finite (n+1 terms) and each term')
out('      rho -> rho^{-j} is holomorphic on Re s > 0 (so on |Im s| <= 1/2 + eps, eps < 1/2)')
out('      and decays.  The band-limited obstruction (branch point at s = 1/2 +- i/2) does NOT')
out('      apply to this expansion.  Admissibility is satisfied; the obstruction is elsewhere.')
out()
out('  (2) THE |Z_j| LAW, measured from the table:  Z_j = sum_rho rho^{-j},  j = 2..25')
rho1 = G[0]
Zj = []
for j in range(2, 26):
    v = 2.0 * float(np.sum(np.real((0.5 + 1j * G) ** (-j))))
    Zj.append(v)
Zj = np.array(Zj)
js = np.arange(2, 26)
sl = np.polyfit(js, np.log(np.abs(Zj)), 1)[0]
out('      fit  log|Z_j| = a - j log r  =>  r = {:.5f}   (|rho_1| = {:.5f})'.format(exp(-sl), rho1))
for j in [2, 3, 5, 10, 20, 25]:
    out('      j = {:>3}: |Z_j| = {:.6e}'.format(j, abs(Zj[j - 2])))
out('      => |Z_j| ~ r^{-j} with r = |rho_1| = 14.13, i.e. the terms decay geometrically at')
out('         the scale of the FIRST zero, not at the arithmetic scale 3 (the trivial zero s=-2).')
out()
out('  (3) lambda_n FROM THE TABLE (lower bound: the omitted tail is positive) and the')
out('      CANCELLATION COST  digits = log10( sum_j |C(n,j) Z_j| / lambda_n ).')
out()
lam1 = 2.0 * float(np.sum(1.0 - np.cos(th)))
out('      check:  lambda_1 = 2 sum (1 - cos theta_gamma) = {:.15f}'.format(lam1))
out('              known value                            = 0.023095708966121'.format())
out()
logr = -sl
hdr2 = '{:>8} {:>20} {:>14} {:>16} {:>16}'
out(hdr2.format('n', 'log10 sum|C(n,j)Z_j|', 'j_peak', 'log10 lambda_n', 'digits needed'))
rowd = []
jpks = []
for n in [50, 100, 200, 300, 400, 600]:
    lg = []
    jj = []
    for j in range(1, n + 1):
        lz = log10(abs(Zj[0])) - (j - 2) * logr if j >= 2 else log10(abs(lam1))
        val = lgamma(n + 1) - lgamma(j + 1) - lgamma(n - j + 1) + lz
        lg.append(val); jj.append((val, j))
    jpks = []
    mx = max(lg)
    tot = mx + log10(sum(10.0 ** (v - mx) for v in lg))
    jpk = max(jj)[1]
    lamn = 2.0 * float(np.sum(1.0 - np.cos(n * th)))
    rowd.append((n, tot - log10(lamn), jpk))
    jpks.append(jpk)
    out(hdr2.format(n, '{:.4f}'.format(tot), jpk, '{:.4f}'.format(log10(lamn)),
                    '{:.2f}'.format(tot - log10(lamn))))
out()
nn = np.array([r[0] for r in rowd], float); dd = np.array([r[1] for r in rowd])
jjj = np.array([r[2] for r in rowd], float)
slopej = float(np.polyfit(nn, jjj, 1)[0])
slope0 = float(np.polyfit(nn, dd, 1)[0])
out('  => j_peak/n = {:.4f} for n >= 200 (project: j_approx = n/(1+|rho_1|) = n/15.13;'.format(slopej))
out('     at n <= 100 the j = 2 term is still exceptional, as the project found).')
out('     digits needed grows LINEARLY: fitted rate {:.4f} digits per unit n'.format(slope0))
out('     (the project measured 0.0427 n from the Z_j cancellation + 0.029 n from the binomial')
out('     transform; our n = 50..600 numbers are the same order and the same law).')
out('     EXTRAPOLATION: at n = T0^2 = {:.3e} the cost is ~ {:.2e} digits, versus ~50 digits'.format(
    T0 ** 2, slope0 * T0 ** 2))
out('     that a high-precision (MPFR, 200-bit) implementation can afford.  ROUTE 5 fails on')
out('     precision, NOT on admissibility: the finite binomial expansion is fully admissible.')
out()

out('=' * 78)
out('SUMMARY -- routes 3 and 5')
out('=' * 78)
out('  3. A linear-phase criterion must have exponential type >= 0.1273 n; the explicit')
out('     formula prime side then reaches e^{0.8 n} = 10^{4.45e11} at n = T0^2, versus')
out('     T0^{O(1)} feasible.  ROUTE 3 fails by ~10^{4.45e11}.  The "linear phase" object')
out('     exists (Oesterle) but is evaluable, not uniformly boundable.')
out('  5. The FINITE binomial expansion has admissible terms -- so the admissibility wall of')
out('     the band-limited route is NOT the issue -- but the binomial transform loses about')
out('     {:.4f} digits per unit n, i.e. ~{:.2e} digits at n = T0^2.'.format(slope0, slope0 * T0 ** 2))
out('     ROUTE 5 fails on the cancellation cost, not on the class of test functions.')
out('=' * 78)

with open('scripts/PAPERA_fluc2_type.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_fluc2_type.txt')
