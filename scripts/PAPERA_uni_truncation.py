"""
PAPERA_uni_truncation.py -- A1 uniformity attack, ROUTE C: rigidity -> phase increment,
                            quantile/truncation/moment versions (region B) + region A coverage.

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the task
  "A1 equidistribution/uniformity route".  Reads data/zeros_odlyzko_2M.npy ;
  writes scripts/PAPERA_uni_truncation.txt.  Not committed.  No other file touched.

DECIDES (number-driven) whether the rigidity (van der Corput second-difference) route can be
rescued by replacing the sup-form  max_k |Delta^2 phi_k|  by a quantile / truncation / moment
form, and whether region A (fast phase) can be covered at all.

SETUP (from PAPERA-expsum s.4):
  phi_k = n theta(gamma_k).  Discrete vdC 2nd-difference test (Graham-Kolesnik, sup form):
      |sum e^{i phi_k}| <= M sqrt(Lambda) + Lambda^{-1/2},   Lambda = max_k |n Delta^2 theta_k|.
  Region B (gamma > gamma_res, slow): Lambda = n max|gap_jump|/gamma^2 ; prior round found
      Lambda = 2.844 -> M_B sqrt(Lambda) = 9.81e5 > allowance 6.55e5  (fails 1.5x);
      needed max|gap_jump| <= 0.675, measured 1.663.
  Region A (gamma < gamma_res, fast): max n Delta^2 theta = 2e10 -> 2nd-difference test dead;
      1st-derivative test needs monotone increments (fails, ~40% gap noise).
"""

import numpy as np
from math import pi, log, atan, sqrt

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); N = int(G.size)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
B = (log(T0) + 1.0) / (4 * pi * T0)
n = int(T0 ** 2)
ALLOW = N - n * B

gres = sqrt(2 * pi * n / log(3e5))
for _ in range(300):
    gres = sqrt(2 * pi * n / log(gres / (2 * pi)))
regB = G > gres
NB = int(regB.sum()); NA = N - NB

# gap jumps: Delta g_k = (g_{k+2}-g_{k+1}) - (g_{k+1}-g_k), index 0..N-3 <-> zero k+1
gp = (G[2:] - G[1:-1]) - (G[1:-1] - G[:-2])
# second difference n*|theta_{k+2}-2theta_{k+1}+theta_k|, index 0..N-3
d2 = n * np.abs(TH[2:] - 2 * TH[1:-1] + TH[:-2])
gk = (G[2:] + G[1:-1] + G[:-2]) / 3.0   # gamma location of the second difference
regB_d2 = gk > gres                       # region-B mask on the length-(N-2) grid
gjB = np.abs(gp)[regB_d2]                 # gap jumps inside region B (consistent grid)
d2B = d2[regB_d2]                         # second differences inside region B

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

out('=' * 80)
out('ROUTE C : RIGIDITY -> PHASE INCREMENT  (quantile / truncation / moment versions)')
out('=' * 80)
out('T0 = {:.6f}  N = {}  allowance(T0^2) = {:.4e}  gamma_res = {:.4e}'.format(T0, N, ALLOW, gres))
out('N_A = {}   N_B = {}'.format(NA, NB))
out()

# ---------------- region B sup form (reproduce prior) ----------------
out('(C1) REGION B, SUP FORM (reproduce prior round)')
lamB = float(d2[gk > gres].max())
vdB = NB * sqrt(lamB) + 1 / sqrt(lamB)
out('    Lambda_B = max n Delta^2 theta = {:.4e}   vdC bound = {:.2e} + {:.2f} = {:.2e}'.format(
    lamB, NB*sqrt(lamB), 1/sqrt(lamB), vdB))
out('    gap-jump max = {:.4f} (rms {:.4f}) ;  needed max|gap_jump| <= 0.675'.format(gjB.max(), sqrt((gjB**2).mean())))
out('    => FAILS by {:.2f}x'.format(vdB / ALLOW))
out()

# ---------------- region B truncation ----------------
out('(C2) REGION B, TRUNCATION (split good / bad gap-jumps)')
out('    gap-jump tail (region B):')
for q in [0.5, 0.9, 0.99, 0.999, 0.9999]:
    out('        quantile {:.4f} = {:.4f}'.format(q, np.quantile(gjB, q)))
out('    {:>8} {:>12} {:>12} {:>16} {:>16}'.format('tau', 'frac>tau', 'count>tau', 'Lambda_good', 'M_good sqrt(L)'))
for tau in [0.4, 0.5, 0.675, 0.8, 1.0, 1.2, 1.4, 1.6]:
    good = gjB <= tau
    cnt = int((~good).sum())
    lamg = float(d2B[good].max()) if good.any() else 0.0
    Mgood = int(good.sum())
    bound_good = Mgood * sqrt(lamg) + (1/sqrt(lamg) if lamg > 0 else 0.0)
    out('    {:>8.3f} {:>12.4f} {:>12} {:>16.4e} {:>16.4e}'.format(tau, (~good).mean(), cnt, lamg, bound_good))
out()
tau = 0.675
good = gjB <= tau
cnt = int((~good).sum()); Mgood = int(good.sum())
lamg = float(d2B[good].max())
bgood = Mgood * sqrt(lamg) + 1/sqrt(lamg)
out('    at tau=0.675: good points = {} ; bad points = {} ({}%);'.format(Mgood, cnt, 100.0*cnt/NB))
out('        vdC(good) = {:.3e}  +  #bad = {:.3e}  =>  {:.3e}'.format(bgood, cnt, bgood + cnt))
out('    allowance = {:.3e}   =>   truncated bound / allowance = {:.3f}'.format(ALLOW, (bgood+cnt)/ALLOW))
out('    => truncation ALONE reaches {:.3f}x allowance (NUMERICAL ONLY: the good set is'.format((bgood+cnt)/ALLOW))
out('        non-contiguous, so the vdC sup-form theorem on the re-indexed good subsequence')
out('        is NOT literally valid; needs a sparse/non-contiguous vdC lemma. See C4.)')
out()
# rigorous version: split good set into maximal contiguous runs (in gamma order), apply
# sup-form vdC to each run; bad points bounded by 1 each.  This IS a legitimate argument.
good2 = gjB <= tau
runs = int((good2 & ~np.roll(good2, 1)).sum())
rig = Mgood * sqrt(lamg) + runs / sqrt(lamg) + cnt
out('    RIGOROUS run-split (contiguous good-runs + trivial bad points):')
out('        #good-runs = {}  (<= #bad+1 = {}) ; charge per run 1/sqrt(L) = {:.3f}'.format(runs, cnt+1, 1/sqrt(lamg)))
out('        bound = M_good sqrt(L) + runs/sqrt(L) + #bad')
out('              = {:.3e} + {:.2e} + {:.2e} = {:.3e}'.format(Mgood*sqrt(lamg), runs/sqrt(lamg), float(cnt), rig))
out('        vs allowance {:.3e}  =>  {:.3f}x  ({})'.format(ALLOW, rig/ALLOW, 'UNDER' if rig<ALLOW else 'OVER'))
out()

# ---------------- region B moment (Sigma) form ----------------
out('(C3) REGION B, SIGMA-FORM (moment van der Corput; HEURISTIC, lemma unverified)')
out('    Candidate lemma (needs verification vs Graham-Kolesnik):')
out('        |sum e^{i phi_k}| <= sqrt(M * L) + sqrt(M / L),  L = sum_k |Delta^2 phi_k|')
out('    (replaces sup Lambda by the TOTAL second-difference mass L).')
L_B = float(d2[gk > gres].sum())
out('    L_B = sum over k in B of n |Delta^2 theta_k| = {:.4e}'.format(L_B))
sigB = sqrt(NB * L_B) + sqrt(NB / L_B)
out('    sqrt(M_B * L_B) + sqrt(M_B/L_B) = {:.4e} + {:.2e} = {:.4e}'.format(sqrt(NB*L_B), sqrt(NB/L_B), sigB))
out('    => {:.2f}x UNDER allowance (vs sup-form {:.2f}x OVER).'.format(ALLOW/sigB, vdB/ALLOW))
out()

# ---------------- region A coverage ----------------
out('(C4) REGION A (fast phase): can ANY rigidity input cover it?')
out('    second-difference sup-form, octave-wise (use min(M sqrt L, M) since trivial M is better for big L):')
edges = [14.0, 100.0, 1e3, 1e4, 1e5, 3e5, gres]
tot_sup = 0.0
for a, b in zip(edges[:-1], edges[1:]):
    m = (gk > a) & (gk <= b)
    if m.sum() == 0:
        continue
    Lm = d2[m].max(); Mm = int(m.sum())
    term = min(Mm * sqrt(Lm) + (1/sqrt(Lm) if Lm>0 else 0), float(Mm))
    tot_sup += term
    out('        octave [{:>6.0e},{:>6.0e}]: M={:>8}, max n D2 = {:.3e}, term(min)= {:.3e}'.format(a, b, Mm, Lm, term))
out('    sum over octaves (sup-form) = {:.3e}  vs trivial N_A = {:.3e}  vs allowance {:.3e}'.format(tot_sup, float(NA), ALLOW))
L_A = float(d2[gk <= gres].sum())
sigA = sqrt(NA * L_A) + sqrt(NA / L_A)
out('    sigma-form region A: L_A = {:.4e} -> sqrt(M L)+sqrt(M/L) = {:.3e}'.format(L_A, sigA))
out('    => BOTH forms fail in region A (the 1/gamma^2 divergence of n theta\'\' near gamma_1 = 14 is fatal).')
out('    1st-derivative test needs monotone increments n theta\'(gamma); actual increments')
out('        n (theta_{k+1}-theta_k) = -n gap_k/gamma_k^2 have ~40% gap noise -> hypothesis FAILS.')
out()
out('VERDICT ROUTE C:')
out('  region B sup-form: FAIL 1.5x.  truncation: within ~1x but NUMERICAL (non-contiguous good set).')
out('  region B sigma-form: {:.2e} < allowance (HEURISTIC, lemma unverified).'.format(sigB))
out('  region A: NO rigidity input covers it (sup ~{:.1e}, sigma ~{:.1e}, both >> allowance).'.format(tot_sup, sigA))
out('=' * 80)

with open('scripts/PAPERA_uni_truncation.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_uni_truncation.txt')
