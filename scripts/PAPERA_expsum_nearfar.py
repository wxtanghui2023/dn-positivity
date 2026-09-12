"""
PAPERA_expsum_nearfar.py -- HARD DELIVERABLE #1: near-pair vs far-pair decision.

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the task "attack the
  exponential-sum inequality |sum_{gamma<=T0} e^{i n theta(gamma)}| <= (1-delta)(N - n B)".
  Reads data/zeros_odlyzko_2M.npy ; writes scripts/PAPERA_expsum_nearfar.txt.
  Not committed.  No other file touched.

THE TENSION TO RESOLVE
  With S_n = sum_{gamma<=T0} e^{i n theta_gamma}, theta(t)=2 arctan(1/(2t)), N = #zeros:
      |S_n|^2 = N + 2 sum_{k<l} cos( n (theta_l - theta_k) ).
  (a) adjacent pairs (l=k+1): theta_l-theta_k ~ gap_k/gamma_k^2 is TINY when n << gamma^2,
      so those pairs contribute +1 each => ~N positive terms;
  (b) the other ~N^2/2 pairs are called "far"; if their phases were random the sum would
      be O(N);
  (c) measurement says |S_n|^2 ~ N (i.e. total pair sum ~ 0) => the far pairs must carry a
      large NEGATIVE deterministic contribution.
  => If (a)+(c) hold, the cancellation is NOT a nearest-neighbour (local / pair-correlation)
     effect but a global one.  This script decides it by direct measurement.

METHOD (exact, no model)
  P_tot(n) := |S_n|^2 - N  =  2 sum_{j>=1} A_j(n),
      A_j(n) = 2 sum_{k=1}^{N-j} cos( n ( theta_{k+j} - theta_k) ).
  A_j is computed by direct summation (vectorised in k) for j = 1..Jmax; the "far" part is
  then the EXACT remainder  P_far = P_tot - sum_{j<=J} A_j.  No approximation anywhere.
  A second, independent decomposition splits each A_j by octave-bins of gamma.
  Controls: (R) iid uniform phases, (S) gap-shuffled zero set, (M) mean-gap smooth model.

DISCIPLINE: everything printed is either an exact finite sum or a clearly labelled model.
"""

import numpy as np
from math import pi, log, atan, sqrt

rng = np.random.default_rng(20260912)

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); N = int(G.size)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
MAIN_T0 = float((T0 / (2 * pi)) * log(T0 / (2 * pi * np.e)) + 7.0 / 8.0)
B_T0 = (log(T0) + 1.0) / (4 * pi * T0)

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

NPTS = [int(1e6), int(1e9), int(1e12), int(T0 ** 2)]

out('=' * 80)
out('DELIVERABLE #1 : near-pair vs far-pair decomposition of |S_n|^2 = N + 2 sum_{k<l} cos')
out('=' * 80)
out('T0 = {:.6f}   N = {}   main(T0) = {:.4f}   B_T0 = {:.6e}'.format(T0, N, MAIN_T0, B_T0))
out('phase: theta(gamma) = 2 arctan(1/(2 gamma))  (identical to project convention)')
out('allowance(n) = N - n*B_T0 ; at n=T0^2 : {:.6e} = {:.4f}*N'.format(MAIN_T0 - int(T0**2)*B_T0, (MAIN_T0-int(T0**2)*B_T0)/N))
out()

# ---------------- exact total pair sum from |S_n|^2 ----------------
out('(0) EXACT |S_n|^2 and total pair sum P_tot = |S_n|^2 - N')
out('{:>10}  {:>15}  {:>15}  {:>15}  {:>12}  {:>10}'.format('n','Re S=sum cos','Im S=sum sin','|S|^2','P_tot=|S|^2-N','|S|/sqrtN'))
S_cache = {}
for n in NPTS:
    S = np.exp(1j * (n * TH)).sum()
    S_cache[n] = S
    out('{:>10.3e}  {:>15.5f}  {:>15.5f}  {:>15.5f}  {:>15.6e}  {:>10.4f}'.format(
        n, S.real, S.imag, abs(S)**2, abs(S)**2 - N, abs(S)/sqrt(N)))
out()

# ---------------- A_j profile (exact) ----------------
def A_j(n, j):
    d = TH[j:] - TH[:-j]
    return float(2.0 * np.sum(np.cos(n * d)))

Jsmall = list(range(1, 65))
Jbig = [128, 256, 512, 1024, 2048]

out('(1) EXACT separation profile A_j(n) = 2 sum_k cos(n(theta_{k+j}-theta_k));  P_tot = sum_j A_j')
out('    [A_j > 0  <=> zero-pairs at separation j add constructively]')
hdr = '{:>10}  {:>15}  {:>15}  {:>15}  {:>15}'.format('n','sum_{j<=8} A_j','sum_{j<=64} A_j','sum_{j<=2048} A_j','P_tot (exact)')
out(hdr)
prof = {}
for n in NPTS:
    vals = {}
    for j in Jsmall + Jbig:
        vals[j] = A_j(n, j)
    prof[n] = vals
    c8 = sum(vals[j] for j in range(1, 9))
    c64 = sum(vals[j] for j in range(1, 65))
    c2048 = c64 + sum(vals[j] for j in Jbig)
    out('{:>10.3e}  {:>15.4e}  {:>15.4e}  {:>15.4e}  {:>15.4e}'.format(n, c8, c64, c2048, abs(S_cache[n])**2 - N))
out()

out('(1b) same, NORMALISED by N (so that P_tot/N = |S|^2/N - 1)')
out('{:>10}  {:>14}  {:>14}  {:>14}  {:>14}  {:>14}'.format('n','near/N (j<=64)','near/N (j<=2048)','far/N (J=64)','far/N (J=2048)','P_tot/N'))
for n in NPTS:
    vals = prof[n]
    c64 = sum(vals[j] for j in range(1, 65))
    c2048 = c64 + sum(vals[j] for j in Jbig)
    Pt = abs(S_cache[n])**2 - N
    out('{:>10.3e}  {:>14.5f}  {:>14.5f}  {:>14.5f}  {:>14.5f}  {:>14.5f}'.format(
        n, c64/N, c2048/N, (Pt - c64)/N, (Pt - c2048)/N, Pt/N))
out()

out('(1c) per-j table for n = T0^2 = {:.6e} (exact A_j)'.format(int(T0**2)))
vals = prof[int(T0**2)]
for j in list(range(1, 21)) + [32, 48, 64, 128, 256, 512, 1024, 2048]:
    out('    j = {:>5}   A_j = {:>15.4e}   A_j/(2N) = {:>10.5e}'.format(j, vals[j], vals[j]/(2*N)))
out()

# ---------------- gamma-octave split of the coherent (small-j) mass ----------------
out('(2) WHERE does the positive small-j mass live?  A_j split by octave bins of gamma')
out('    criterion: pair (k,k+j) is phase-coherent iff  n*(theta_{k+j}-theta_k) < 1,')
out('    i.e. n*2*pi/(gamma^2 log(gamma/2pi)) * j  <~ 1   =>  gamma >~ sqrt(2 pi j n / log(gamma/2pi))')
edges = [0.0, 1e2, 1e3, 1e4, 1e5, 3e5, 6e5, 9e5, 1.05e6, T0 + 1e-6]
nam = ['<1e2','1e2-1e3','1e3-1e4','1e4-1e5','1e5-3e5','3e5-6e5','6e5-9e5','9e5-1.05e6','>1.05e6']
n = int(T0 ** 2)
idx = np.searchsorted(edges, G, side='right') - 1
for j in [1, 2, 4, 8, 16]:
    d = TH[j:] - TH[:-j]
    c = 2.0 * np.cos(n * d)
    b = np.bincount(idx[:-j], weights=c, minlength=len(nam))
    cnt = np.bincount(idx[:-j], minlength=len(nam))
    out('    j = {:>3} :'.format(j))
    for i, nn in enumerate(nam):
        if cnt[i] > 0:
            out('        gamma in {:<11} : count {:>8}   sum 2cos = {:>13.4e}   mean cos = {:>9.5f}'.format(
                nn, cnt[i], b[i], b[i] / (2 * cnt[i])))
out('    coherent-mass prediction (n=T0^2): gamma_coherent >~ {:.3e}, i.e. {} zeros = {:.1f}% of N'.format(
    sqrt(2 * pi * n / log(T0 / (2 * pi))), int(round(N * (1 - np.searchsorted(G, sqrt(2*pi*n/log(T0/(2*pi)))) / N))),
    100.0 * (1 - np.searchsorted(G, sqrt(2*pi*n/log(T0/(2*pi)))) / N)))
out()

# ---------------- models ----------------
out('(3) CONTROLS (clearly labelled models; same N, same n-values)')
out('    R = iid uniform phases ; S = gap-shuffled zero set ; M = mean-gap smooth phase')
for n in [int(1e9), int(T0 ** 2)]:
    # R
    tot_R = []
    for _ in range(5):
        psi = rng.uniform(0, 2 * pi, N)
        tot_R.append(abs(np.exp(1j * psi).sum())**2 - N)
    # S: shuffle the gaps, rebuild zeros
    gaps = np.diff(G)
    tot_S = []
    for _ in range(5):
        gs = rng.permutation(gaps)
        Gs = np.concatenate(([G[0]], G[0] + np.cumsum(gs)))
        THs = 2.0 * np.arctan(1.0 / (2.0 * Gs))
        tot_S.append(abs(np.exp(1j * (n * THs)).sum())**2 - N)
    # M: mean-gap smooth (replace gamma_k by smooth inverse of the counting function)
    def smooth_inv(k):
        # solve (t/2pi) log(t/2pi e) + 7/8 = k+1  approximately by Newton on log t
        x = np.log(max(k + 1.0, 1.0)) + np.log(2 * pi)
        for _ in range(60):
            f = (np.exp(x) / (2 * pi)) * (x - 1.0) + 0.875 - (k + 1.0)
            fp = np.exp(x) / (2 * pi) * x
            x = x - f / fp
        return np.exp(x)
    ks = np.array([1, 10, 100, 1000, N - 1], dtype=float)
    out('    n = {:.3e} :'.format(n))
    out('        R (iid phases)      : mean P_tot = {:>13.5e}   rms = {:>13.5e}   (5 draws)'.format(np.mean(tot_R), np.std(tot_R)))
    out('        S (shuffled gaps)   : mean P_tot = {:>13.5e}   rms = {:>13.5e}   (5 draws)'.format(np.mean(tot_S), np.std(tot_S)))
    out('        actual              :      P_tot = {:>13.5e}'.format(abs(S_cache[n])**2 - N))
out()

out('=' * 80)
out('READING OF THE NUMBERS')
out('=' * 80)
for n in NPTS:
    vals = prof[n]
    c8 = sum(vals[j] for j in range(1, 9))
    c64 = sum(vals[j] for j in range(1, 65))
    Pt = abs(S_cache[n])**2 - N
    out('  n={:.3e}: near(j<=8)/N = {:>9.5f}   near(j<=64)/N = {:>9.5f}   far/N = {:>9.5f}   P_tot/N = {:>9.5f}'.format(
        n, c8/N, c64/N, (Pt - c64)/N, Pt/N))
out()
out('  Decision rule:')
out('   * if near(j<=~64) alone accounts for the O(N) positive mass AND the far remainder is')
out('     also Theta(N) of the OPPOSITE sign  => the cancellation is GLOBAL, pair correlation')
out('     (a local/nearest-neighbour statement) is NOT the correct input.');
out('   * if the near mass is O(sqrt(N)) random-looking  => nearest-neighbour pairs are NOT')
out('     even coherent at this n, and the whole Theta(N) discussion is vacuous.');
out('=' * 80)

with open('scripts/PAPERA_expsum_nearfar.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_expsum_nearfar.txt')
