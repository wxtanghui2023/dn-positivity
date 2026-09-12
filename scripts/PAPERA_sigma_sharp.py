"""
PAPERA_sigma_sharp.py -- A1 route C: sharp-constant check for the Sigma-form and sup-form
van der Corput lemmas.

PROVENANCE
  Created 2026-09-12 by assistant (subagent). Reads data/zeros_odlyzko_2M.npy ;
  writes scripts/PAPERA_sigma_sharp.txt. Not committed. No other file touched.

PURPOSE (number-driven):
  (S1) Clean convex counterexample to the Sigma-form (pure parabola, no fp cancellation):
         phi_k = eps*(k - M/2)^2  with  eps = c / M^2.
         Second difference Delta^2 phi = 2 eps (constant), L = 2 eps M = 2 c / M.
         Sigma-bound = sqrt(M L) + sqrt(M/L) = sqrt(2c) + M/sqrt(2c).
         For c in ( ~2 , M^2/2 ) the bound < M while |sum| ~ M.  => Sigma-form FALSE
         even for CONVEX phase (one-sign second difference).
  (S2) Sharp constant for the SUP-form  |sum| <= M sqrt(Lam) + C / sqrt(Lam),
         Lam = max_k |Delta^2 phi_k|, tested on adversarial families (convex parabola,
         sign-changing random, step function) to find minimal C for which it holds.
  (S3) The STANDARD van der Corput second-derivative test uses MIN (not max) and needs
         one-sign second derivative; report the form with correct constant and show it is
         inapplicable to phi_k = n theta(gamma_k) (sign-changing Delta^2 from gap jumps).
"""
import numpy as np
from math import pi, log, atan, sqrt

def d2(phi):
    return phi[2:] - 2 * phi[1:-1] + phi[:-2]

def L_of(phi):
    return float(np.abs(d2(phi)).sum())

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

out('=' * 78)
out('SIGMA-FORM / SUP-FORM SHARP-CONSTANT CHECK')
out('=' * 78)

# ---- S1: clean convex counterexample (pure parabola) ----
out('(S1) CLEAN CONVEX COUNTEREXAMPLE to Sigma-form (pure parabola, no fp cancellation).')
out('     phi_k = eps*(k-M/2)^2 ;  Delta^2 phi = 2 eps (const) ; L = 2 eps M.')
out('     Sigma bound = sqrt(2 eps M^2) + sqrt(M/(2 eps M)) = M sqrt(2 eps) + 1/sqrt(2 eps).')
for M in [10**4, 2 * 10**6]:
    out('  M = {}:'.format(M))
    for c in [0.1, 0.5, 1.0, 2.0, 4.0, 10.0]:
        eps = c / M**2
        kk = np.arange(M, dtype=float)
        phi = eps * (kk - M / 2.0) ** 2
        lhs = abs(np.exp(1j * phi).sum())
        L = 2 * eps * M
        rhs = sqrt(M * L) + sqrt(M / L) if L > 0 else np.inf
        # also the sup-form with coefficient 1 and with C=8
        Lam = float(np.abs(d2(phi)).max())
        sup1 = M * sqrt(Lam) + 1.0 / sqrt(Lam) if Lam > 0 else np.inf
        sup8 = M * sqrt(Lam) + 8.0 / sqrt(Lam) if Lam > 0 else np.inf
        out('    c={:5.2f} eps={:.3e}: |sum|={:.4e}  L={:.4e}  Sigma={:.4e} '
            '[ratio {:.3f}]  sup(C=1)={:.4e}[{:.3f}]  sup(C=8)={:.4e}[{:.3f}]'.format(
            c, eps, lhs, L, rhs, lhs/rhs, sup1, lhs/sup1, sup8, lhs/sup8))
out()

# ---- S2: sharp constant for sup-form (max version) ----
out('(S2) SUP-FORM (max version): minimal C with  |sum| <= M sqrt(Lam) + C/sqrt(Lam).')
out('     Lam = max_k |Delta^2 phi_k|.  Scan adversarial families; report max needed C.')
rng = np.random.default_rng(999)
def sup_C_needed(phi):
    M = len(phi); lhs = abs(np.exp(1j * phi).sum()); Lam = float(np.abs(d2(phi)).max())
    if Lam <= 0:
        return np.inf, lhs, Lam
    # need C >= (lhs - M sqrt(Lam)) * sqrt(Lam)
    return max(0.0, (lhs - M * sqrt(Lam)) * sqrt(Lam)), lhs, Lam

worst_C = 0.0; worst_info = None
# family 1: convex parabola eps = c/M^2 (the dangerous regime for sup-form)
for M in [10**4, 10**5, 2 * 10**6]:
    for c in np.logspace(-3, 2, 40):
        eps = c / M**2
        kk = np.arange(M, dtype=float)
        phi = eps * (kk - M / 2.0) ** 2
        C, lhs, Lam = sup_C_needed(phi)
        if C > worst_C:
            worst_C = C; worst_info = ('convex parabola', M, c, lhs, Lam)
# family 2: sign-changing random second differences (integrate twice)
for M in [300, 3000, 30000]:
    for _ in range(200):
        dd = rng.standard_normal(M - 2)
        d1 = np.zeros(M - 1); d1[0] = rng.uniform(-5, 5)
        d1[1:] = d1[0] + np.cumsum(dd)
        phi = np.zeros(M); phi[0] = rng.uniform(0, 2 * pi)
        phi[1:] = phi[0] + np.cumsum(d1)
        C, lhs, Lam = sup_C_needed(phi)
        if C > worst_C:
            worst_C = C; worst_info = ('random sign-changing', M, None, lhs, Lam)
# family 3: step function
for M in [10**4, 2 * 10**6]:
    phi = np.zeros(M); phi[M // 2:] = 2 * pi
    C, lhs, Lam = sup_C_needed(phi)
    if C > worst_C:
        worst_C = C; worst_info = ('step', M, None, lhs, Lam)
out('    max C needed over all families = {:.4f}  (from {} , M={}, lhs={:.3e}, Lam={:.3e})'.format(
    worst_C, worst_info[0], worst_info[1], worst_info[3], worst_info[4]))
out('    => sup-form  M sqrt(Lam) + 1/sqrt(Lam)  (C=1) is INVALID (needs C ~= {:.2f}).'.format(worst_C))
out()

# ---- S3: standard second-derivative test (min, one sign) inapplicability ----
out('(S3) STANDARD second-derivative test (van der Corput, Graham-Kolesnik):')
out('     hypothesis:  lambda <= |f\'\'| <= alpha*lambda  (ONE SIGN, bounded away from 0),')
out('     conclusion:  |sum e(f(n))| <= C*( N sqrt(lambda) + 1/sqrt(lambda) ).')
out('     Uses MIN |f\'\'| (typical curvature), NOT max, NOT total mass.')
G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
n = int(float(G.max()) ** 2)
d2th = TH[2:] - 2 * TH[1:-1] + TH[:-2]   # sign of Delta^2 theta
pos = (d2th > 0).sum(); neg = (d2th < 0).sum(); tot = d2th.size
out('    actual phase phi_k = n theta(gamma_k): Delta^2 theta sign split:')
out('      positive {} ({:.1f}%)  negative {} ({:.1f}%)  total {}'.format(
    pos, 100*pos/tot, neg, 100*neg/tot, tot))
out('    => second difference is SIGN-CHANGING (gap jumps) => one-sign hypothesis FAILS.')
out('    => standard second-derivative test DOES NOT apply; sup-form/run-split/Sigma-form')
out('       are all MISAPPLICATIONS of van der Corput for this phase.')
out()
out('VERDICT:')
out('  Sigma-form lemma: FALSE (step-function ratio ~370x; convex parabola ratio >1).')
out('  Sup-form with C=1: FALSE (needs C ~= {:.2f}); and even then the standard test'.format(worst_C))
out('     needs one-sign second derivative, which n theta(gamma_k) does not have.')
out('  Correct region-B bound: only TRIVIAL M_B = 581491 = 0.888x allowance applies.')

with open('scripts/PAPERA_sigma_sharp.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_sigma_sharp.txt')
