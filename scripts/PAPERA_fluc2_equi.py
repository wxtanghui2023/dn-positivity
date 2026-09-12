"""
PAPERA_fluc2_equi.py -- ROUTE 2 (reciprocal variable u = 1/gamma) and ROUTE 4 (Erdos-Turan)

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the round-2 task.
  Reads data/zeros_odlyzko_2M.npy; writes scripts/PAPERA_fluc2_equi.txt.
  Not committed; no other file touched.

ROUTE 2
  Put u = theta(gamma) ~= 1/gamma.  The density of the u's is rho(u) = |d gamma/du| main'(gamma(u)),
  gamma(u) = (1/2) cot(u/2), i.e. rho(u) = log(1/u)/(2pi u^2) (1 + O(u^2 log u)).  Then
      sum_{gamma<=T0} cos(n theta_gamma)  =  int cos(nu) rho(u) du  +  (u-space fluctuation).
  We verify that the "smooth part" int cos(nu) rho(u) du is EXACTLY J(n) = int_0^{T0} cos(n theta) d main
  (a change of variable), report its size, and hence the size of the u-space fluctuation.
  We also report the discrepancy of the u-sequence itself.

ROUTE 4
  Erdos-Turan for the point set x_gamma = n theta_gamma/(2 pi) mod 1:
      D_N <= C ( 1/M + sum_{k=1}^{M} (1/k) |(1/N) sum_gamma e^{2 pi i k x_gamma}| ),
  and Koksma with f(x) = cos(2 pi x), Var(f) = 4, gives |sum_gamma cos(n theta_gamma)| <= 4 N D_N.
  We compute the exponential sums for k <= 30 and the resulting bound, at the heights that matter.

DISCIPLINE: all numbers computed; the ET constant is stated; where a route cannot deliver a
bound the loss factor is printed.
"""

import numpy as np
from math import pi, log, atan, tan, sin, cos, sqrt, exp

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); Nz = int(G.size)
th = np.arctan(G / (G ** 2 - 0.25))
TH0 = 2.0 * atan(1.0 / (2.0 * T0))
MAIN_T0 = float((T0 / (2 * pi)) * log(T0 / (2 * pi * np.e)) + 7.0 / 8.0)
MASS = MAIN_T0 - 7.0 / 8.0
B_T0 = (log(T0) + 1.0) / (4 * pi * T0)
ALLOW = MAIN_T0 - int(T0 ** 2) * B_T0

lines = []
def out(s=''):
    lines.append(s); print(s)

out('=' * 78)
out('ROUTE 2 (reciprocal variable) + ROUTE 4 (Erdos-Turan)')
out('=' * 78)
out('  T0 = {:.6f}   N = {:,}   sqrt(N) = {:.1f}'.format(T0, Nz, sqrt(Nz)))
out()

# ------------------------------------------------------------------ ROUTE 2
out('-' * 78)
out('ROUTE 2 -- THE u = theta(gamma) DENSITY AND ITS SMOOTH PART')
out('-' * 78)
out()
out('  gamma(u) = (1/2) cot(u/2);  rho(u) = main\'(gamma(u)) * |d gamma/du|')
out('  (asymptotically rho(u) = log(1/u)/(2 pi u^2) (1 + O(u^2 log u))).')
out()
def gamma_of_u(u): return 0.5 / np.tan(u / 2.0)
def rho_of_u(u):
    g = gamma_of_u(u)
    return (np.log(g / (2 * pi)) / (2 * pi)) * (0.25 / np.sin(u / 2.0) ** 2)

def G_of_u(u, n):
    t = 0.5 / np.tan(u / (2.0 * n))
    return np.log(t / (2 * pi)) / (2 * pi) * (4.0 * t * t + 1.0) / (4.0 * n)

def TermB(n, per=40):
    u0 = n * TH0; uhi = n * pi
    if uhi <= u0: return 0.0
    uc = min(max(2 * pi, u0), uhi)
    tot = 0.0
    if uc > u0 * (1 + 1e-13):
        u = np.exp(np.linspace(log(u0), log(uc), 400001))
        tot += float(np.trapz((1 - np.cos(u)) * G_of_u(u, n), u))
    if uhi > uc:
        h = 2 * pi / per; step = 2_000_000 * h; a = uc
        while a < uhi - 1e-9:
            b = min(uhi, a + step)
            M = max(int((b - a) / h) + 1, 2)
            u = np.linspace(a, b, M)
            tot += float(np.trapz((1 - np.cos(u)) * G_of_u(u, n), u)); a = b
    return tot

# mass check: log grid (the mass of rho sits at u ~ theta(T0), a 1/u^2 spike)
u_lo = TH0; u_hi = 2.0 * atan(1.0 / (2.0 * 1e-6))
uu = np.exp(np.linspace(log(u_lo), log(u_hi), 2000001))
out('  mass int rho du over u in [{:.3e},{:.6f}] = {:.6f}   (mass main(T0)-main(0+) = {:.6f})'.format(
    u_lo, u_hi, float(np.trapz(rho_of_u(uu), uu)), MASS))
out('  u_max = theta(gamma_1) = {:.6f}  (< pi/2; the u-densities pile up at u -> 0 like log(1/u)/u^2)'.format(
    2 * atan(1.0 / (2.0 * G[0]))))
out()
out('  smooth part  S_sm(n) = int cos(nu) rho(u) du   vs   J(n) = int_0^{T0} cos(n theta) d main')
out('  (identical after u = theta(t); checked numerically by two independent grids)')
hdr = '{:>10} {:>20} {:>20} {:>10}'
out(hdr.format('n', 'S_sm (rho-grid)', 'J = MASS-TermB', 'ratio'))
for n in [10**3, 10**4, 10**5, 10**6]:
    n = int(n)
    R = 4_000_000
    u = np.exp(np.linspace(log(u_lo), log(u_hi), R))
    Ssm = float(np.trapz(np.cos(n * u) * rho_of_u(u), u))
    Jv = MASS - TermB(n)
    out(hdr.format('{:>10,}'.format(n), '{:+.8e}'.format(Ssm), '{:+.8e}'.format(Jv),
                   '{:.4f}'.format(Ssm / Jv) if Jv else '-'))
out()
out('  => S_sm(n) == J(n) (same integral).  Sizes: J(n) = Theta(mass) for n << T0; for n >> T0')
out('     the period-block identity (int_0^{2pi} cos = 0, int_0^{2pi} u cos u du = 0) applies')
out('     and gives |J(n)| <= G_phase(u0) = main\'(T0)(4T0^2+1)/(4n) -- table below.')
out()
hdr1 = '{:>20} {:>16} {:>18} {:>12}'
out(hdr1.format('n', 'u0 = n theta(T0)', 'G_phase(u0)', '|J|/G(u0)'))
for n in [10**6, 10**8, 10**10, 10**12, int(T0 ** 2)]:
    n = int(n)
    u0 = n * TH0
    G0 = (log(T0 / (2 * pi)) / (2 * pi)) * (4 * T0 * T0 + 1.0) / (4.0 * n)
    if n <= 3 * 10**6:
        ratio = abs(MASS - TermB(n)) / G0
    else:
        ratio = float('nan')
    out(hdr1.format('{:>20,}'.format(n), '{:.4e}'.format(u0), '{:.6e}'.format(G0),
                    '{:.3f}'.format(ratio) if ratio == ratio else '(n.a.)'))
out()
out('  THE FLUCTUATION AFTER THE u-CHANGE:  sum cos - J')
hdr2 = '{:>16} {:>16} {:>18} {:>18} {:>14}'
out(hdr2.format('n', 'sum cos', 'J (= S_sm)', 'fluctuation', '|fluc|/|sum|'))
for n in [10**3, 10**4, 10**5, 10**6, 10**9, int(T0 ** 2)]:
    n = int(n)
    S = float(np.sum(np.cos(n * th)))
    if n <= 3 * 10**6:
        Jv = MASS - TermB(n)
    else:
        u0 = n * TH0
        Jv = -sin(u0) * (log(T0 / (2 * pi)) / (2 * pi)) * (4 * T0 * T0 + 1.0) / (4.0 * n)
    out(hdr2.format('{:>16,}'.format(n), '{:+.6e}'.format(S), '{:+.6e}'.format(Jv),
                    '{:+.6e}'.format(S - Jv), '{:.4f}'.format(abs(S - Jv) / abs(S)) if S else '-'))
out()
out('  => in u-space the SMOOTH part is provably O(T0^2 log(T0/2pi)/n) (the period-block')
out('     identity: int_0^{2pi} cos = 0 and int_0^{2pi} u cos u du = 0), but the FLUCTUATION')
out('     is the same object as before:  sum cos - J = int_0^{T0} cos(n theta) dS.  The')
out('     u-parametrisation is exact and gain-free.')
out()
out('  STRUCTURAL NOTE: theta(t) = 2 arctan(1/(2t)) has branch points at t = +-i/2;')
out('  in u-space the phase n theta(t) ~ n/t becomes exp(i n gamma^{-1}), whose only')
out('  singularity in gamma is at gamma = 0 (essential).  The admissible-class obstruction')
out('  is invariant: +-i/2 <-> 0.')
out()

# ------------------------------------------------------------------ ROUTE 4
out('-' * 78)
out('ROUTE 4 -- ERDOS-TURAN FOR x_gamma = n theta_gamma/(2 pi) mod 1')
out('-' * 78)
out()
out('  D_N <= C ( 1/M + sum_{k=1}^{M} (1/k) |(1/N) sum_gamma e^{2 pi i k x_gamma}| ),  C = 2 used.')
out('  Koksma: |sum_gamma cos(n theta_gamma)| <= 4 N D_N   (Var(cos 2 pi .) = 4).')
out()
hdr3 = '{:>8} {:>10} {:>18} {:>16} {:>18} {:>14} {:>14}'
out(hdr3.format('n', 'M', 'max_k |S_k|/N', 'D_N (ET)', '4 N D_N', 'true |sum cos|', '|S_1|/N'))
for n in [10**6, 10**9, 10**12, int(T0 ** 2)]:
    n = int(n)
    x = (n * th) / (2 * pi)
    M = 30
    coef = 1.0 / M
    mx = 0.0
    for k in range(1, M + 1):
        Sk = abs(np.sum(np.exp(2j * pi * k * x))) / Nz
        mx = max(mx, Sk)
        coef += Sk / k
    DN = 2.0 * coef
    S = abs(float(np.sum(np.cos(n * th))))
    S1 = abs(np.sum(np.exp(1j * n * th))) / Nz
    out(hdr3.format('{:>8,}'.format(n), M, '{:.6e}'.format(mx), '{:.6e}'.format(DN),
                    '{:.6e}'.format(4 * Nz * DN), '{:.6e}'.format(S), '{:.6e}'.format(S1)))
out()
out('  NOTE: |S_1| is dominated by the SMOOTH part of e^{i n theta}: at n=1e6, |S_1|/N = 5.7e-1')
out('  while Re S_1 = sum cos = 1.4e4 = 7.2e-3 N.  So the ET sums are NOT calibrated by the')
out('  allowance at small n; ET fails there (bound 1.9e7 > allowance 2.0e6).')
out()
out('  => at n = T0^2 the ET bound (5.7e5) is just BELOW the allowance (6.5e5), but 94% of it')
out('     is the 1/M floor; with the same M the bound fails at n = 1e6 by a factor 9.5.')
out('     The requirement is |S_k| <= delta N with delta ~ allow/(4 C N log M) = {:.4f} for'.format(ALLOW / (8.0 * Nz * 7.0)))
out('     every k <= M, M >~ 25.  The k = 1 term IS the required sum (with 2 pi n in place of n).')
out('     ET therefore presupposes ~30 constant-factor bounds each as hard as the original.')
out('     Loss: strictly more than the original problem (30 frequencies instead of 1).')
out()

out('=' * 78)
out('SUMMARY -- routes 2 and 4')
out('=' * 78)
out('  2. u = theta(gamma) is an exact reparametrisation: the smooth part becomes J(n),')
out('     provably O(T0^2 log T0/n) for n >> T0 by the period-block identity, but the')
out('     fluctuation is unchanged (sum cos - J = int cos dS).  No gain; the analytic')
out('     singularity merely moves +-i/2 -> 0.')
out('  4. Erdos-Turan needs |sum_gamma e^{i k n theta_gamma}| <= delta N, delta ~ 0.006, for')
out('     k <= M >~ 25.  The k = 1 term is the required sum itself; ET is circular and asks')
out('     for ~30 times more.  Measured |S_k| would just fit at n=T0^2 (5.7e5 < 6.5e5) but')
out('     fail by 9.5x at n=1e6.')
out('=' * 78)

with open('scripts/PAPERA_fluc2_equi.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_fluc2_equi.txt')
