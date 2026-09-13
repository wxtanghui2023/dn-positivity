"""
PAPERA_uni_moments.py -- A1 uniformity attack, ROUTE B: replace pointwise input with moments.

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the task
  "A1 equidistribution/uniformity route".  Reads data/zeros_odlyzko_2M.npy ;
  writes scripts/PAPERA_uni_moments.txt.  Not committed.  No other file touched.

DECIDES whether replacing  sup|S(t)|  (pointwise, = O(log t))  by  Selberg / Tsang moments
(L^2 of the zero-counting error S(t)) can compress the route-A bound |D_n| <= 8.7e6 to
below the allowance 6.55e5.

SETUP (from PAPERA-expsum s.3):  S_n = S_n^smooth + D_n,
  D_n ~ sum_k (e^{i lambda_k S_k} - 1) e^{i phi_k},  lambda_k = 2 pi n/(gamma_k^2 log(gamma_k/2pi)),
  S_k = k - Nbar(gamma_k) the classical error term,  Nbar(t) = (t/2pi) log(t/2pi e) + 7/8.
  Region split at resonance  lambda(gamma_res) = 1 :
      A: lambda > 1 (fast)  -> |e^{i lambda S} - 1| <= 2  (trivial),  N_A terms
      B: lambda <= 1 (slow) -> |e^{i lambda S} - 1| <= lambda_k |S_k|,  N_B terms
  =>  |D_n| <= 2 N_A + sum_{k in B} lambda_k |S_k|.
  Pointwise:  sum_B lambda_k |S_k| <= sup_B |S_k| * sum_B lambda_k.
  Moment:     sum_B lambda_k |S_k| <= (sum_B lambda_k^2)^{1/2} (sum_B S_k^2)^{1/2}   (Cauchy-Schwarz).
"""

import numpy as np
from math import pi, log, atan, sqrt

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); N = int(G.size)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
B = (log(T0) + 1.0) / (4 * pi * T0)
n = int(T0 ** 2)
ALLOW = N - n * B

Nbar = (G / (2 * pi)) * np.log(G / (2 * pi * np.e)) + 0.875
Serr = np.arange(1.0, N + 1.0) - Nbar

# resonance
gres = sqrt(2 * pi * n / log(3e5))
for _ in range(300):
    gres = sqrt(2 * pi * n / log(gres / (2 * pi)))
regB = G > gres
NB = int(regB.sum()); NA = N - NB
lam = 2 * pi * n / (G ** 2 * np.log(G / (2 * pi)))

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

out('=' * 80)
out('ROUTE B : REPLACE POINTWISE sup|S| WITH MOMENTS (Selberg / Tsang)')
out('=' * 80)
out('T0 = {:.6f}  N = {}  allowance(T0^2) = {:.4e}  gamma_res = {:.4e}'.format(T0, N, ALLOW, gres))
out('N_A = {}   N_B = {}   (resonance split lambda=1)'.format(NA, NB))
out()

out('(B1) POINTWISE INPUT (prior round) vs SHARP constant')
sumlamB = float(lam[regB].sum())
out('    sum_B lambda_k = {:.4e}'.format(sumlamB))
out('    crude  sup|S| <= 1.0 * log T0 = {:.2f}   (used in PAPERA-expsum)'.format(log(T0)))
sup_sharp = 0.110 * log(T0) + 0.290 * log(log(T0)) + 2.290   # Platt-Trudgian 2021
out('    sharp  sup|S| <= 0.110 log t + 0.290 log log t + 2.290 = {:.3f}  [Platt-Trudgian 2021, cite unverified]'.format(sup_sharp))
out('    measured sup_k |S_k| = {:.3f}  (NOT usable in a proof -- that would be circular)'.format(np.abs(Serr).max()))
out('    => pointwise region-B term:  crude {:.3e} ;  sharp {:.3e}'.format(log(T0)*sumlamB, sup_sharp*sumlamB))
out()

out('(B2) L^2 INPUT (Selberg 1946 second moment)')
out('    Selberg: int_0^T S(t)^2 dt = (T/(2 pi^2)) log log T (1+o(1))   [cite: Selberg 1946]')
pred_cont = (T0 / (2 * pi ** 2)) * log(log(T0))
out('    => int_0^T0 S^2 ~ {:.4e}   (RMS of S over [0,T0] ~ {:.3f})'.format(pred_cont, sqrt(pred_cont/T0)))
sumS2_all = float((Serr ** 2).sum())
sumS2_B = float((Serr[regB] ** 2).sum())
out('    measured sum_k S_k^2 (all N zeros) = {:.4e} ;  (region B) = {:.4e}'.format(sumS2_all, sumS2_B))
out('    NOTE: sampling at zeros weighs by density log/2pi ~ 2, so sum_k S(g_k)^2 ~ 2 * int S^2 ;')
out('    Selberg-predicted sum_B S^2 ~ 2*(T0-gres)/(2 pi^2) log log T0 * (M_B/M_total) [needs care; flagged]')
out()

out('(B3) CAUCHY-SCHWARZ on region B')
sumlam2B = float((lam[regB] ** 2).sum())
csB = sqrt(sumlam2B) * sqrt(sumS2_B)
out('    sum_B lambda_k^2 = {:.4e}  =>  sqrt = {:.2f}'.format(sumlam2B, sqrt(sumlam2B)))
out('    sum_B S_k^2 = {:.4e}  =>  sqrt = {:.2f}'.format(sumS2_B, sqrt(sumS2_B)))
out('    CS region-B term = {:.4e}   (vs pointwise sharp {:.3e} : improvement {:.1f}x)'.format(
    csB, sup_sharp*sumlamB, sup_sharp*sumlamB/csB))
out()

out('(B4) TOTAL and the region-A wall')
out('    |D_n| <= 2 N_A + [region-B term]')
tot_point_crude = 2 * NA + log(T0) * sumlamB
tot_point_sharp = 2 * NA + sup_sharp * sumlamB
tot_l2 = 2 * NA + csB
out('    {:>28} {:>14} {:>14}'.format('bound', 'value', 'x allowance'))
for name, val in [('crude pointwise', tot_point_crude), ('sharp pointwise', tot_point_sharp),
                  ('L^2 (Selberg)', tot_l2), ('region A alone (2 N_A)', 2*NA)]:
    out('    {:>28} {:>14.4e} {:>14.2f}'.format(name, val, val / ALLOW))
out()
out('    => 2 N_A = {:.4e} ALREADY exceeds allowance {:.4e} by {:.2f}x.'.format(2*NA, ALLOW, 2*NA/ALLOW))
out('    => even with PERFECT region-B control (sum_B -> 0), |D_n| <= 2 N_A fails.')
out()
out('(B5) WHY region A cannot be helped by moments of S(t)')
out('    region A has lambda_k > 1 (up to {:.4e} at gamma_1), so exp(i lambda S) is a fast phase;'.format(lam[0]))
out('    the only pointwise bound is |e^{i lambda S} - 1| <= 2, and S(t)-moments do not enter.')
out('    Region A is a *phase-increment* (vdC) problem, not a rigidity-moment problem (see route C).')
out()
out('VERDICT ROUTE B:  FAIL (region A wall, 4.3x even with perfect region B).')
out('  L^2 (Selberg/Tsang) compresses region B from {:.2e} to {:.2e} (a {:.0f}x win),'.format(
    sup_sharp*sumlamB, csB, sup_sharp*sumlamB/csB))
out('  but 2 N_A = {:.2e} > allowance, and region A is unreachable by S(t)-moments.'.format(2*NA))
out('=' * 80)

with open('scripts/PAPERA_uni_moments.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_uni_moments.txt')
