"""
PAPERA_sigma_verify.py -- A1 route C: verify the candidate Sigma-form van der Corput lemma.

PROVENANCE
  Created 2026-09-12 by assistant (subagent) for the task
  "A1 verify Sigma-form lemma (sole gatekeeper of region B)".
  Reads data/zeros_odlyzko_2M.npy ; writes scripts/PAPERA_sigma_verify.txt.
  Not committed. No other file touched.

CANDIDATE LEMMA (as used in PAPERA-uniformity-attack.md s4.2, marked UNVERIFIED there):
    For real sequence phi_k (k <= M):
        |sum_{k<=M} e^{i phi_k}| <= sqrt(M * L) + sqrt(M / L),
        where L := sum_k |Delta^2 phi_k|  (TOTAL second-difference mass replacing sup).
  Second difference: Delta^2 phi_k = phi_{k+2} - 2 phi_{k+1} + phi_k  (k = 1..M-2).

This script:
  (V1) reproduces the region-B number L_B, sqrt(M_B L_B)+sqrt(M_B/L_B) = 3.622e5.
  (V2) COUNTEREXAMPLE: step-function phase  phi_k = 2*pi*m_k, m_k = 0 (k<=K), 1 (k>K).
       Then e^{i phi_k} = 1 for all k -> |sum| = M, but L = 4*pi (two second-diff spikes).
       The lemma would demand M <= sqrt(M*4pi)+sqrt(M/(4pi)) ~ 5.4e3 for M=2e6. FALSE.
  (V3) CONVEX phase: does the Sigma-form hold for convex (sign-fixed second difference)?
       Scan random convex phases; also near-linear integer-slope convex perturbation.
  (V4) SIGN-CHANGING phase (the realistic regime: phi_k = n theta(gamma_k) has
       second differences of mixed sign from gap jumps): does Sigma-form hold?
  (V5) empirical constant: maximize |sum e^{i phi}| / (sqrt(M L) + sqrt(M/L))
       over families, to find the correct form / constant.
"""
import numpy as np
from math import pi, log, atan, sqrt

def d2(phi):
    """second differences phi[k+2]-2phi[k+1]+phi[k], length len(phi)-2."""
    return phi[2:] - 2 * phi[1:-1] + phi[:-2]

def L_of(phi):
    return float(np.abs(d2(phi)).sum())

def sigma_bound(M, L):
    if L <= 0:
        return np.inf
    return sqrt(M * L) + sqrt(M / L)

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

out('=' * 80)
out('SIGMA-FORM LEMMA VERIFICATION  (candidate: |sum e^{i phi}| <= sqrt(ML)+sqrt(M/L))')
out('=' * 80)

# ---------- V1: reproduce region B number ----------
G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); N = int(G.size)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
n = int(T0 ** 2)
gres = sqrt(2 * pi * n / log(3e5))
for _ in range(300):
    gres = sqrt(2 * pi * n / log(gres / (2 * pi)))
gk = (G[2:] + G[1:-1] + G[:-2]) / 3.0
d2B = n * np.abs(TH[2:] - 2 * TH[1:-1] + TH[:-2])
regB = gk > gres
LB = float(d2B[regB].sum()); MB = int(regB.sum())
out('(V1) region B reproduction:')
out('    M_B = {}  L_B = {:.4e}'.format(MB, LB))
out('    sqrt(M_B L_B) + sqrt(M_B/L_B) = {:.4e} + {:.2e} = {:.4e}'.format(
    sqrt(MB*LB), sqrt(MB/LB), sigma_bound(MB, LB)))
out()

# ---------- V2: step-function counterexample (general real phase) ----------
out('(V2) COUNTEREXAMPLE (step function, general real phase):')
out('    phi_k = 2*pi*m_k, m_k = 0 for k<=K, m_k = 1 for k>K.')
out('    Then e^{i phi_k} = 1 for ALL k  =>  |sum| = M.  But Delta^2 phi has two spikes')
out('    (+2pi, -2pi) => L = 4*pi.  The lemma would require M <= ~sqrt(M*4pi)+sqrt(M/(4pi)).')
for M in [100, 1000, 10**6, 2*10**6]:
    K = M // 2
    phi = np.zeros(M); phi[K:] = 2 * pi
    lhs = abs(np.exp(1j * phi).sum())
    L = L_of(phi)
    rhs = sigma_bound(M, L)
    out('    M={:>8}: |sum| = {:.3e}   L = {:.4f}   sqrt(ML)+sqrt(M/L) = {:.3e}   '
        'RATIO lhs/rhs = {:.1f}  {}'.format(M, lhs, L, rhs, lhs/rhs,
        'LEMMA FAILS' if lhs > rhs else 'ok'))
out()

# ---------- V3: convex phase (sign-fixed second difference) ----------
out('(V3) CONVEX phase (Delta^2 phi >= 0): random convex + near-linear integer-slope perturb.')
rng = np.random.default_rng(12345)
def test_ratio(phi):
    lhs = abs(np.exp(1j * phi).sum()); L = L_of(phi); rhs = sigma_bound(len(phi), L)
    return lhs, L, rhs, (lhs / rhs if rhs > 0 else np.inf)

maxratio_conv = 0.0; maxratio_conv_info = None
# random convex: random positive second differences, integrate twice
for M in [300, 3000]:
    for trial in range(400):
        dd = rng.uniform(0, 3.0, M - 2)          # positive second differences
        # integrate: build phi with Delta^2 phi = dd
        d1 = np.zeros(M - 1); d1[0] = rng.uniform(-10, 10)
        for k in range(M - 2):
            d1[k + 1] = d1[k] + dd[k]
        phi = np.zeros(M); phi[0] = rng.uniform(0, 2 * pi)
        for k in range(M - 1):
            phi[k + 1] = phi[k] + d1[k]
        lhs, L, rhs, r = test_ratio(phi)
        if r > maxratio_conv:
            maxratio_conv = r; maxratio_conv_info = (M, lhs, L, rhs)
# near-linear integer-slope convex perturbation (the dangerous regime for Sigma-form)
for M in [10**4, 2 * 10**6]:
    for q in [1, 7]:
        for eps in [1.0/M, 1.0/M**1.5, 1.0/M**2]:
            # phi_k = 2*pi*q*k + eps*(k - M/2)^2  (convex, small, near in-phase)
            kk = np.arange(M, dtype=float)
            phi = 2 * pi * q * kk + eps * (kk - M / 2.0) ** 2
            lhs, L, rhs, r = test_ratio(phi)
            if r > maxratio_conv:
                maxratio_conv = r; maxratio_conv_info = (M, lhs, L, rhs, 'parabola q=%d eps=%.2e' % (q, eps))
            out('    M={:>9} q={} eps={:.2e}: |sum|={:.3e} L={:.3e} rhs={:.3e} ratio={:.3f}'.format(
                M, q, eps, lhs, L, rhs, r))
out('    CONVEX max ratio lhs/rhs over all trials = {:.3f}  (from {})'.format(
    maxratio_conv, maxratio_conv_info))
out('    => if max ratio <= 1 for all convex phases, Sigma-form holds (convex); else fails.')
out()

# ---------- V4: sign-changing phase (realistic gap-jump noise) ----------
out('(V4) SIGN-CHANGING phase (realistic regime: mixed-sign second differences).')
maxratio_mixed = 0.0; worst_mixed = None
for M in [300, 3000, 30000]:
    for trial in range(300):
        dd = rng.standard_normal(M - 2)          # mixed-sign second differences
        d1 = np.zeros(M - 1); d1[0] = rng.uniform(-5, 5)
        d1[1:] = d1[0] + np.cumsum(dd)
        phi = np.zeros(M); phi[0] = rng.uniform(0, 2 * pi)
        phi[1:] = phi[0] + np.cumsum(d1)
        lhs, L, rhs, r = test_ratio(phi)
        if r > maxratio_mixed:
            maxratio_mixed = r; worst_mixed = (M, lhs, L, rhs)
out('    mixed-sign random phase max ratio = {:.3f}  (from {})'.format(maxratio_mixed, worst_mixed))
# near-linear + single gap jump (the realistic "bad point" the Sigma-form was meant for)
out('    near-linear + single jump (the exact "bad point" scenario Sigma-form targets):')
for M in [10**4, 2 * 10**6]:
    for q in [1, 5]:
        kk = np.arange(M, dtype=float)
        phi = 2 * pi * q * kk                      # linear, in-phase -> sum = M
        # add a single jump in the SECOND difference of size J at position M/2
        J = 4 * pi
        phi = phi.copy(); K = M // 2
        phi[K:] += J * (kk[K:] - K)                 # kink: Delta^2 = J at one point
        lhs, L, rhs, r = test_ratio(phi)
        if r > maxratio_mixed:
            maxratio_mixed = r; worst_mixed = (M, lhs, L, rhs)
        out('    M={:>9} q={} J={:.2f}: |sum|={:.3e} L={:.3e} rhs={:.3e} ratio={:.3f} {}'.format(
            M, q, J, lhs, L, rhs, r, 'FAILS' if r > 1 else 'ok'))
out()

# ---------- V5: empirical correct form ----------
out('(V5) empirical: find the correct form / constant for the Sigma-type bound.')
out('    Compare |sum| against candidates A=sqrt(ML), B=sqrt(M/L), C=M/L, D=1/sqrt(L), E=const.')
out('    For convex phase, report |sum| / each candidate on the adversarial family.')

with open('scripts/PAPERA_sigma_verify.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_sigma_verify.txt')
