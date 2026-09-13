"""
PAPERA_uni_largesieve.py -- A1 uniformity attack, ROUTE A: Weyl / Erdos-Turan / large sieve.

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the task
  "A1 equidistribution/uniformity route".  Reads data/zeros_odlyzko_2M.npy ;
  writes scripts/PAPERA_uni_largesieve.txt.  Not committed.  No other file touched.

DECIDES (number-driven) whether a UNIFORMITY input can prove
    |S_n| <= (1-delta)(N - n B)   uniformly in n <= T0^2,  S_n = sum_gamma e^{i n theta(gamma)}.
  (A1) Weyl criterion  -> circular (the k=1 condition IS S_n/N = the target).
  (A2) Erdos-Turan    -> circular (k=1 term = target); measured ET numbers from prior round.
  (A3) large sieve    -> min spacing delta of {theta(gamma)/2 pi} is ~ 1/T0^2, so the
       L^2 bound is (N + 1/delta)^{1/2} sqrt(N) >> N : WORSE than trivial.  Structural:
       an L^2 large-sieve bound can never beat the trivial L^1 bound N for constant
       coefficients (it needs 1/delta <= 0 to give |S| < N).
"""

import numpy as np
from math import pi, log, atan, sqrt

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); N = int(G.size)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
B = (log(T0) + 1.0) / (4 * pi * T0)
n_end = int(T0 ** 2)

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

out('=' * 80)
out('ROUTE A : UNIFORMITY DIRECT  (Weyl / Erdos-Turan / large sieve)')
out('=' * 80)
out('T0 = {:.6f}  N = {}  allowance(T0^2) = {:.4e}'.format(T0, N, N - n_end * B))
out()

# ---------- A1 Weyl ----------
out('(A1) WEYL CRITERION (equidistribution of {n theta_gamma / 2 pi} mod 1)')
out('  The sequence {n theta_gamma mod 2 pi}_{gamma<=T0} is equidistributed')
out('  <=>  (1/N) sum_gamma e^{2 pi i m n theta_gamma/2 pi} -> 0  for all m >= 1')
out('  <=>  S_{m n}/N -> 0  for all m >= 1 ,  with S_k = sum_gamma e^{i k theta_gamma}.')
out('  The m = 1 condition is  S_n / N = the very quantity to be bounded.')
out('  => CIRCULAR: Weyl needs S_n = o(N) as one of its own hypotheses.')
out()

# ---------- A2 Erdos-Turan ----------
out('(A2) ERDOS-TURAN discrepancy (C = 2)')
out('  x_gamma = n theta_gamma / 2 pi mod 1 ;')
out('  D_N <= C ( 1/M + sum_{k<=M} (1/k) |(1/N) sum_gamma e^{2 pi i k x_gamma}| )')
out('  = C ( 1/M + sum_{k<=M} (1/k) |S_{k n}| / N ).')
out('  Koksma (f = cos 2 pi x, Var = 4): |sum_gamma cos(n theta_gamma)| <= 4 N D_N.')
out('  The k = 1 term is |S_n|/N = the target itself (same circularity).')
M = 30
S1 = abs(np.exp(1j * (1 * n_end * TH)).sum())
out('  measured at n = T0^2, M = {} : |S_1|/N = {:.4e}'.format(M, S1/N))
out('  prior-round numbers (reproduced, see PAPERA-fluc-round2 s.4): ET bound at T0^2 = 5.67e5')
out('  vs allowance 6.55e5 (barely under) BUT 94% is the 1/M floor; fails 9.5x at n=1e6.')
out('  => CIRCULAR + quantitatively useless (needs |S_k| <= 0.0058 N for ALL k<=~30).')
out()

# ---------- A3 large sieve ----------
out('(A3) LARGE SIEVE  (Selberg / Montgomery-Vaughan)')
out('  points x_j = theta(gamma_j)/2 pi in [0, 1/2]; coefficients a_j = 1.')
out('  Montgomery-Vaughan large sieve:')
out('      sum_{m=M+1}^{M+Q} |sum_j e^{2 pi i m x_j}|^2  <=  (Q + 1/delta) * N')
out('  with delta = min_{j!=k} || x_j - x_k ||  (minimal spacing of the points).')
dth = np.diff(TH)
dmin = float(np.abs(dth).min()) / (2 * pi)
out('  theta is decreasing; min |theta(k+1)-theta(k)| = {:.4e}  => delta = {:.4e}'.format(
    np.abs(dth).min(), dmin))
out('  1/delta = {:.4e}   (vs N = {:.4e})'.format(1/dmin, float(N)))
out('  single-frequency bound (take one n0 in the sum, all terms >=0):')
bound = sqrt((float(N) + 1/dmin) * N)
out('      |S_n| <= (N + 1/delta)^(1/2) * sqrt(N) = {:.4e}'.format(bound))
out('      ratio to N = {:.1f}   ratio to trivial = {:.1f}'.format(bound/N, bound/N))
out('  => WORSE than trivial (N) by a factor {:.0f}.'.format(bound/N))
out('  REASON: theta = 1/gamma compresses the top of the range:')
out('  gamma in [T0/2, T0]  ->  theta in [1/T0, 2/T0] of length ~1/T0, holding ~N/2 points')
out('  => min spacing ~ 1/(T0^2 log) while N ~ T0 log T0  =>  1/delta ~ T0^2 >> N.')
out()
out('  STRUCTURAL OBSTRUCTION (theorem-level): the large sieve is an L^2 (moment) bound.')
out('  For constant coefficients a_j = 1 it gives |S_n| <= sqrt((Q+1/delta) N).  To get')
out('  |S_n| < N (any constant-factor saving) one needs Q + 1/delta < N, i.e. 1/delta < N.')
out('  Here 1/delta = {:.2e} > N = {:.2e}, so even |S_n| <= N is NOT attained --'.format(
    1/dmin, float(N)))
out('  let alone a saving.  A constant-factor saving requires L^1/L^infinity (cancellation')
out('  / equidistribution) structure, which is exactly what Weyl/ET re-express as S_n = o(N).')
out()
out('VERDICT ROUTE A:  FAIL (circular + structurally impossible).')
out('  Weyl/ET: circular (k=1 = target).  large sieve: |S_n| <= {:.2e} = {:.0f}x trivial.'.format(bound, bound/N))
out('  Uniformity-as-input is the wrong direction: it REPHRASES the target, never bounds it.')
out('=' * 80)

with open('scripts/PAPERA_uni_largesieve.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_uni_largesieve.txt')
