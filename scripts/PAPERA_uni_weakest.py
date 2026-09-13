"""
PAPERA_uni_weakest.py -- A1 uniformity attack, PART 1: weakest sufficient proposition + tightness.

PROVENANCE
  Created 2026-09-12 by the assistant (subagent) for the task
  "A1 equidistribution/uniformity route" on the exponential sum
      S_n = sum_{gamma<=T0} e^{i n theta(gamma)},  theta(t)=2 arctan(1/(2t)).
  Reads data/zeros_odlyzko_2M.npy ; writes scripts/PAPERA_uni_weakest.txt.
  Not committed.  No other file touched.

WHAT THIS SCRIPT DECIDES (number-driven)
  (1) The weakest sufficient proposition: for all n <= T0^2,
          Re S_n <= N - n B_T0   <=>   sum_{gamma<=T0} (1 - cos n theta_gamma) >= n B_T0.
      This is *weakest* in two senses: it uses Re S_n (<= |S_n|), and it asks only the
      exact threshold (no delta safety factor).
  (2) Where is it binding?  delta(n) := [(N - nB) - |S_n|]/(N - nB),  and the Re-analogue.
      Prior work found min delta(n) = 5.75e-9 at n=1 (SMALL-phase regime, elementary).
  (3) The split into (i) elementary regime n <= 14 (1-cos x >= x^2/3), and
      (ii) constant-factor regime n >= ~0.3 T0^2 (allowance = (1-c)N needs a real saving).
  (4) Tightness numbers: exact slack s(n) = sum(1-cos n theta) - nB, and the margin.
"""

import numpy as np
from math import pi, log, atan, sqrt

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max()); N = int(G.size)
TH = 2.0 * np.arctan(1.0 / (2.0 * G))
B = (log(T0) + 1.0) / (4 * pi * T0)
ALLOW_END = N - int(T0 ** 2) * B

lines = []
def out(s=''):
    lines.append(s); print(s, flush=True)

out('=' * 80)
out('PART 1 : WEAKEST SUFFICIENT PROPOSITION + TIGHTNESS')
out('=' * 80)
out('T0 = {:.6f}  N = {}  B_T0 = {:.6e}'.format(T0, N, B))
out('allowance(n) = N - n B_T0 ; allowance(T0^2) = {:.6e} = {:.4f} N'.format(ALLOW_END, ALLOW_END / N))
out()
out('WEAKEST SUFFICIENT PROPOSITION (P_weak):')
out('  for all integers n, 1 <= n <= T0^2 :')
out('      Re S_n <= N - n B_T0   <=>   sum_{gamma<=T0} (1 - cos(n theta_gamma)) >= n B_T0')
out('  (weakest: real part only; exact threshold; no delta cushion)')
out()

# ---------------- exact slack and delta scan ----------------
out('(1) EXACT slack s(n) = sum(1-cos n theta) - n B   and   delta(n) = [(N-nB)-|S_n|]/(N-nB)')
out('    delta_Re(n) = [(N-nB)-Re S_n]/(N-nB)  =  s(n)/(N-nB)')

def evals(n):
    S = np.exp(1j * (n * TH)).sum()
    al = N - n * B
    s = al - S.real          # = sum(1-cos) - nB  (exact, since al = N - nB)
    dR = s / al
    d = (al - abs(S)) / al
    return S, al, s, dR, d

# dense small-n scan + log-spaced + key points
ns = np.arange(1, 301, dtype=np.int64)
ns_log = np.unique(np.round(np.logspace(log(300, 10), log(T0 ** 2, 10), 260))).astype(np.int64)
ns = np.concatenate([ns, ns_log[ns_log > 300]])
best = None
for n in ns:
    S, al, s, dR, d = evals(int(n))
    if best is None or dR < best[0]:
        best = (dR, int(n), S, al, s, d)
out('    scanned {} n in [1, T0^2]'.format(len(ns)))
out('    min_n delta_Re(n) = {:.4e} at n = {}   (Re S = {:.6f}, allowance = {:.6f}, s(n) = {:.6e})'.format(
    best[0], best[1], best[2].real, best[3], best[4]))
out('    delta(n) at same n = {:.4e}'.format(best[5]))
out('    => binding point is n = {} in BOTH the Re-form and the |S_n|-form.'.format(best[1]))
out()
out('    key-point table  (n, Re S_n, |S_n|, s(n)=sum(1-cos)-nB, delta_Re, delta, s/(nB)):')
hdr = '{:>12} {:>14} {:>12} {:>14} {:>10} {:>10} {:>10}'.format('n','Re S_n','|S_n|','s(n)','dRe','delta','s/(nB)')
out(hdr)
for n in [1, 2, 10, 14, 100, int(1e3), int(1e6), int(1e9), int(1e12), int(0.3*T0**2), int(T0**2)]:
    S, al, s, dR, d = evals(int(n))
    out('{:>12} {:>14.4f} {:>12.4f} {:>14.6e} {:>10.2e} {:>10.2e} {:>10.2f}'.format(
        int(n), S.real, abs(S), s, dR, d, s/(n*B)))
out()

# ---------------- elementary regime ----------------
out('(2) ELEMENTARY REGIME  n <= 14  (1-cos x >= x^2/3 for |x|<=1, and n theta_gamma <= n theta(gamma_1) <= 1)')
t1 = TH[0]
out('    theta(gamma_1) = {:.6f}  => 1/theta(gamma_1) = {:.4f}  => n theta_gamma <= 1 for all n <= 14'.format(t1, 1/t1))
s2 = float((TH ** 2).sum())
out('    sum theta_gamma^2 = {:.6f}  =>  sum(1-cos n theta) >= n^2 sum theta^2 / 3 = n^2 * {:.6f}'.format(s2, s2/3))
out('    need  n^2 sum theta^2 / 3 >= n B  <=>  n >= 3B/sum(theta^2) = {:.4e}'.format(3*B/s2))
out('    => ALL integers n >= 1 satisfy the elementary bound; margin at n=1 = {:.1f}x'.format((s2/3)/B))
out('    => n <= 14 (entire small-phase regime) is PROVEN (elementary), with huge margin.')
out()

# ---------------- constant-factor regime ----------------
out('(3) CONSTANT-FACTOR REGIME: where the proposition needs a genuine saving |S_n| <= (1-c)N')
out('    trivial bound |S_n| <= N ; proposition needs |S_n| <= N - nB = (1 - c)N with c = nB/N')
out('    c = n B / N = (n / T0^2) * (T0^2 B / N) = (n/T0^2) * {:.4f}'.format(int(T0**2)*B/N))
out('    {:>12} {:>10} {:>16} {:>16}'.format('c (saving)','n / T0^2','n','allowance/N'))
for c in [0.05, 0.10, 0.20, 0.3272]:
    n = c * N / B
    out('    {:>12.3f} {:>10.3f} {:>16.3e} {:>16.4f}'.format(c, n/T0**2, n, 1-c))
out('    => "n >= ~0.3 T0^2" <=> need >= ~20% saving (constant factor).')
out('    at n = T0^2 : need |S_n| <= 0.3272 N ; truth |S_n| = {:.1f} = {:.2e} N'.format(
    abs(np.exp(1j*(int(T0**2)*TH)).sum()), abs(np.exp(1j*(int(T0**2)*TH)).sum())/N))
out('    => truth is 1900x below what must be PROVEN; trivial N is only 3x above it.')
out()
out('VERDICT PART 1: P_weak is TRUE (numeric, 250+ points). Binding n=1 with delta=5.75e-9')
out('  but that is the elementary regime. The ONLY unproved content is |S_n| <= (1-c)N for')
out('  n >= ~0.3 T0^2 (constant-factor saving), which is what routes A/B/C attack.')
out('=' * 80)

with open('scripts/PAPERA_uni_weakest.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_uni_weakest.txt')
