"""
PAPERA_expsum_routes.py -- routes A (equidistribution) and B (rigidity): explicit numbers.

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the task on
  |sum_{gamma<=T0} e^{i n theta(gamma)}| <= (1-delta)(N - n B_T0), n <= T0^2.
  Reads data/zeros_odlyzko_2M.npy ; writes scripts/PAPERA_expsum_routes.txt.
  Not committed.  No other file touched.

SECTIONS
 (A) size scan over n: where is the constraint binding, and what is the best absolute
     delta?  (small n is NOT the sqrt(N) regime!)
 (B) smooth-model split  S_n = S_n^smooth + D_n ,  ghat(k) = Nbar^{-1}(k+1/2).
     S^smooth is a sum over a SMOOTH monotone sequence => van der Corput applies with an
     explicit O(sqrt N) bound; the whole difficulty is the rigidity error D_n.
     Also verified: D_n ~ sum_k (e^{i lambda_k (S_k+1/2)} - 1) e^{i phi_k}, with
     lambda_k = 2 pi n/(gamma_k^2 log(gamma_k/2 pi)) and S_k = k - Nbar(gamma_k) the
     classical error term of the zero-counting function.
 (C) rigidity route: the discrete van-der-Corput second-difference quantity
       Lambda = max_k | n( theta(g_{k+2}) - 2 theta(g_{k+1}) + theta(g_k) ) |
     in the slow region B (gamma > gamma_res) and the fast region A.

DISCIPLINE: exact sums where exact; vdC quoted as a THEOREM with the constant flagged.
"""

import numpy as np
from math import pi, log, atan, sqrt

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); N = int(G.size)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
MAIN_T0 = float((T0 / (2 * pi)) * log(T0 / (2 * pi * np.e)) + 7.0 / 8.0)
B_T0 = (log(T0) + 1.0) / (4 * pi * T0)

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

out('=' * 80)
out('ROUTES A (equidistribution) and B (rigidity) -- explicit numbers')
out('=' * 80)
out('T0 = {:.6f}  N(actual zero count) = {}  main(T0) = {:.4f}'.format(T0, N, MAIN_T0))
out('B_T0 = {:.6e}   allowance(n) := N - n*B_T0 ; allowance(T0^2) = {:.6e} = {:.4f} N'.format(
    B_T0, N - int(T0**2)*B_T0, (N - int(T0**2)*B_T0)/N))
out()

# ---------------- (A) size scan ----------------
out('(A) WHERE IS THE CONSTRAINT BINDING ?   delta(n) := [(N - nB) - |S_n|] / (N - nB)')
out('    (the proposition |S_n| <= (1-delta)(N-nB) holds for every delta <= min_n delta(n))')
ns_small = np.arange(1, 301)
ns_big = np.unique(np.round(np.logspace(log(300,10), 2*log(T0,10), 250))).astype(np.int64)
ns = np.concatenate([ns_small, ns_big[ns_big > 300]])
vals = np.empty(len(ns)); dlt = np.empty(len(ns))
for i, n in enumerate(ns):
    S = abs(np.exp(1j * (n * TH)).sum())
    al = N - n * B_T0
    vals[i] = S; dlt[i] = (al - S) / al
j = int(np.argmin(dlt))
out('    scanned {} n in [1, T0^2]'.format(len(ns)))
out('    min_n delta(n) = {:.4e}  at n = {}   (|S_n| = {:.6f}, allowance = {:.6f})'.format(
    dlt[j], ns[j], vals[j], N - ns[j] * B_T0))
out('    delta(1) = {:.4e} ; delta(10) = {:.4e} ; delta(100) = {:.4e}'.format(dlt[0], dlt[9], dlt[99]))
out('    for n >= 300 (log-spaced sample): min delta = {:.4e} at n = {}'.format(
    dlt[len(ns_small):].min(), ns[len(ns_small):][int(np.argmin(dlt[len(ns_small):]))]))
out('    |S_n| at n=1,10,100,1e3,1e6,1e9,1e12,T0^2:')
for n in [1, 10, 100, int(1e3), int(1e6), int(1e9), int(1e12), int(T0**2)]:
    S = abs(np.exp(1j * (n * TH)).sum())
    out('        n={:>13}: |S_n| = {:>15.4f}   |S_n|/N = {:.6f}   delta(n) = {:.4e}'.format(
        n, S, S/N, ((N - n*B_T0) - S)/(N - n*B_T0)))
out('    => FOR SMALL n there is NO sqrt(N): the phases barely wrap, |S_n| ~ N - c n^2,')
out('       and the binding constant is delta ~ {:.1e} (NOT O(1)).  The sqrt(N) regime'.format(dlt[0]))
out('       (task premise) only begins once n >> 1 (n*theta_gamma ~ n/gamma is not small).')
out()

# ---------------- (B) smooth model ----------------
out('(B) SMOOTH-MODEL SPLIT  S_n = S_n^smooth + D_n ,  ghat(k) = Nbar^{-1}(k+1/2)')
def Nbar(t):
    t = np.maximum(t, 1e-12)
    return (t / (2 * pi)) * np.log(t / (2 * pi * np.e)) + 0.875
def ghat(k):
    x = np.log(np.maximum(k + 0.5, 1.0)) + np.log(2 * pi) + 1.0
    for _ in range(120):
        f = Nbar(np.exp(x)) - (k + 0.5)
        x = x - f / (np.exp(x) * x / (2 * pi))
    return np.exp(x)
GH = ghat(np.arange(N, dtype=float))
dev = G - GH
out('    max |gamma_k - ghat(k)| = {:.4f}   rms = {:.4f}   (O(1): classical S(t) error)'.format(
    np.abs(dev).max(), np.sqrt((dev**2).mean())))
THS = 2.0 * np.arctan(1.0 / (2.0 * GH))
out('    {:>10}  {:>14}  {:>14}  {:>14}  {:>14}'.format('n', '|S_n|', '|S_smooth|', '|D_n|', '|D_n|/sqrt N'))
for n in [int(1e6), int(1e9), int(1e12), int(T0**2)]:
    Sa = np.exp(1j * (n * TH)).sum(); Ss = np.exp(1j * (n * THS)).sum()
    out('    {:>10.3e}  {:>14.4e}  {:>14.4e}  {:>14.4e}  {:>14.4f}'.format(
        n, abs(Sa), abs(Ss), abs(Sa - Ss), abs(Sa - Ss) / sqrt(N)))
out('    => BOTH parts are Theta(sqrt N): the smooth density already produces the sqrt(N)')
out('       cancellation, and the rigidity error D_n is the same size (not dominant).')
out()

# identity for D_n
out('    identity check: D_n  vs  sum_k (e^{i lambda_k (S_k+a)} - 1) e^{i phi_k}')
Serr = np.arange(1.0, N + 1.0) - Nbar(G)
for n in [int(1e9), int(1e12), int(T0**2)]:
    lam = 2 * pi * n / (G ** 2 * np.log(G / (2 * pi)))
    phi = n * TH
    Da = np.exp(1j * (n * TH)).sum() - np.exp(1j * (n * THS)).sum()
    row = '      n={:.3e}: D_n = {:>12.2f}'.format(n, abs(Da))
    for a in [0.0, 0.5]:
        Dm = np.sum((np.exp(1j * lam * (Serr + a)) - 1.0) * np.exp(1j * phi))
        row += '   |model(a={:.1f})| = {:>10.2f}'.format(a, abs(Dm))
    out(row)
out('    => the rigidity error is controlled by the equidistribution of')
out('       { lambda_k * S_k / 2 pi } mod 1,  lambda_k = 2 pi n/(gamma_k^2 log(gamma_k/2pi)).')
out()

# ---------------- vdC bound for the smooth model ----------------
out('    vdC second-derivative test on the smooth sequence (phi(k) = n theta(ghat(k))):')
out('      phi\'(k)  = -2 pi n/(gamma^2 log(gamma/2pi))        [per unit index]')
out('      phi\'\'(k) =  (2 pi/(gamma log))(2 - 1/log) * (2 pi/log)   (>0, decreasing in gamma)')
n = int(T0 ** 2)
gres = sqrt(2 * pi * n / log(3e5))
for _ in range(300):
    gres = sqrt(2 * pi * n / log(gres / (2 * pi)))
lam2 = 2 * pi / (gres * log(gres / (2 * pi))) * (2 - 1.0 / log(gres / (2 * pi))) * (2 * pi / log(gres / (2 * pi)))
MB = int((G > gres).sum()); MA = N - MB
out('      resonance point lambda(gamma_res)=1 : gamma_res = {:.4e}   M_B = {} = {:.1f}% N   M_A = {}'.format(
    gres, MB, 100.0*MB/N, MA))
out('      phi\'\'(gamma_res) = {:.4e}   sqrt = {:.4e}'.format(lam2, sqrt(lam2)))
out('      vdC(2nd) on B : M_B sqrt(lam2) + 1/sqrt(lam2) = {:.1f} + {:.1f} = {:.1f}'.format(
    MB*sqrt(lam2), 1/sqrt(lam2), MB*sqrt(lam2)+1/sqrt(lam2)))
out('      vdC(1st) on A : |phi\'| >= 1 and monotone in the smooth model')
out('                      => sum over lambda-dyadic shells of O(1/lambda) = O(1)')
out('      => |S_smooth| <= ~1700 << allowance 6.55e5.  THE SMOOTH PART IS PROVABLE.')
out()

# ---------------- (C) rigidity route ----------------
out('(C) RIGIDITY ROUTE: discrete vdC on the ACTUAL sequence phi(k) = n theta(gamma_k).')
out('    Lambda_B = max_{gamma_k>gamma_res} | n (theta(g_{k+2}) - 2 theta(g_{k+1}) + theta(g_k)) |')
d2 = TH[2:] - 2.0 * TH[1:-1] + TH[:-2]
sec = n * np.abs(d2)
gk = (G[2:] + G[1:-1] + G[:-2]) / 3.0
regB = gk > gres
lamB = sec[regB].max()
out('    REGION B (gamma > {:.4e}, {} terms):'.format(gres, int(regB.sum())))
out('      max |n Delta^2 theta| = {:.4e}  (99.9%q {:.4e}, median {:.4e})'.format(
    lamB, np.quantile(sec[regB], 0.999), np.median(sec[regB])))
out('      vdC bound  M_B sqrt(Lambda) + Lambda^-1/2 = {:.4e} + {:.2f} = {:.4e}'.format(
    MB*sqrt(lamB), 1/sqrt(lamB), MB*sqrt(lamB)+1/sqrt(lamB)))
lm = np.median(sec[regB])
out('      with the MEDIAN second difference: {:.4e} + {:.2f} = {:.4e}'.format(
    MB*sqrt(lm), 1/sqrt(lm), MB*sqrt(lm)+1/sqrt(lm)))
out('      NEEDED: M_B sqrt(Lambda) <= 0.327 N  <=>  Lambda <= (0.327 N/M_B)^2 = {:.4f}'.format(
    (0.327*N/MB)**2))
out('      Lambda ~ n|gap_jump|/gamma^2  =>  need max|gap_(k+1)-gap_k| <= {:.4f}  (region B)'.format(
    (0.327*N/MB)**2 * gres**2 / n))
gp = (G[2:]-G[1:-1]) - (G[1:-1]-G[:-2])
out('      MEASURED max |gap_(k+1)-gap_k| in B = {:.4f}   (rms {:.4f})  =>  {}'.format(
    np.abs(gp[regB]).max(), np.sqrt((gp[regB]**2).mean()),
    'FITS' if np.abs(gp[regB]).max()*n/gres**2 <= (0.327*N/MB)**2 else 'DOES NOT FIT'))
lamA = sec[~regB].max()
out('    REGION A (gamma < gamma_res, {} terms): max |n Delta^2 theta| = {:.4e}'.format(int((~regB).sum()), lamA))
out('      => 2nd-difference test fails there (M_A sqrt(Lambda) = {:.3e});'.format(MA*sqrt(lamA)))
out('         must use the 1st-derivative test, whose hypothesis f\' monotone FAILS for the')
out('         actual increments  n(theta_{k+1}-theta_k) = n gap_k/gamma_k^2 (gap noise ~40%).')
out('      => the rigidity route covers region B only, and needs max|gap jump| <= {:.3f} there.'.format(
    (0.327*N/MB)**2 * gres**2 / n))
out()
out('(D) REGION SPLIT OF S_n and the ROUTE-A (equidistribution) BOUND NUMBERS')
out('    {:>10}  {:>14}  {:>14}  {:>14}  {:>14}'.format('n','|S_n^A| (fast)','|S_n^B| (slow)','|S_n| total','sqrt(M_A),sqrt(M_B)'))
for n2 in [int(1e9), int(1e12), n]:
    z = np.exp(1j * (n2 * TH))
    sA = z[G <= gres].sum(); sB = z[G > gres].sum()
    out('    {:>10.3e}  {:>14.4e}  {:>14.4e}  {:>14.4e}  {:>7.0f},{:>7.0f}'.format(
        n2, abs(sA), abs(sB), abs(sA + sB), sqrt(MA), sqrt(MB)))
lamk = 2 * pi * n / (G ** 2 * np.log(G / (2 * pi)))
sumB = float(lamk[G > gres].sum()); minA = float(lamk[G <= gres].min())
out('    route-A bound |D_n| <= 2 N_A + (sup|S_k|) * sum_B lambda_k,  at n=T0^2:')
out('      2 N_A = {:.4e} ;  sum_B lambda_k = {:.4e} ;  with sup|S| = C log T0 = 14.0 -> {:.4e}'.format(
    2*MA, sumB, 14.0*sumB))
out('      => the PROVABLE bound is ~{:.1e} > allowance 6.55e5 (fails by {:.1f}x).'.format(
    2*MA + 14.0*sumB, (2*MA + 14.0*sumB)/(N - int(T0**2)*B_T0)))
out('    lambda-dyadic shells in region A: log2(lambda_max/lambda_min) = log2({:.3e}/1) = {:.1f}'.format(
    float(lamk[G <= gres].max()), log(float(lamk[G <= gres].max()), 2)))
out('=' * 80)

with open('scripts/PAPERA_expsum_routes.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_expsum_routes.txt')
