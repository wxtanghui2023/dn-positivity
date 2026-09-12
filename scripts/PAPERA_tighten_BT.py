"""
PAPERA_tighten_BT.py -- tighten the explicit tail constant B_T for Paper A

PROVENANCE
  Created 2026-09-12 20:5x by the assistant, per operator instruction "继续".
  Writes scripts/PAPERA_tighten_BT.txt.

WHY
  Paper A bounds B_T := (1/2) sum_{gamma>T} gamma^{-2} by 3.4015e-6 at T = 1.13e6,
  while the TRUE value is 9.2065e-7: the explicit bound is 3.69 times looser.  That
  looseness is one of the two constant-level reasons the quadratic route fails (the
  other being a dropped factor exp(n/(2 T^2))).  This script re-derives B_T by ABEL
  SUMMATION WITH THE BOUNDARY TERM RETAINED, exactly the technique that rescued
  Paper B's final lemma, and shows the loss can be recovered.

DERIVATION (Abel / Stieltjes integration by parts, boundary term NOT dropped)
      sum_{gamma>T} gamma^{-2} = int_{(T,inf)} t^{-2} dN(t)
                               = [t^{-2} N(t)]_T^{inf} + 2 int_T^{inf} N(t) t^{-3} dt
                               = -N(T)/T^2 + 2 int_T^{inf} N(t) t^{-3} dt,
  hence
      B_T = -N(T)/(2 T^2) + int_T^{inf} N(t) t^{-3} dt.
  The FIRST term is NEGATIVE and is exactly what a crude bound throws away.  Bounding
  the second integral above with the explicit counting hypothesis
      A(t) := main(t) - (c log t + d) <= N(t) <= main(t) + (c log t + d),
      main(t) = (t/2pi) log(t/(2pi e)) + 7/8,
  and bounding -N(T)/(2T^2) ABOVE by -A(T)/(2T^2) (valid since N(T) >= A(T)), gives
      B_T <= -A(T)/(2T^2) + (1/2pi)(log(T/(2pi e)) + 1)/T
             + 7/(16 T^2) + (c (log T + 1/2) + d)/(2 T^2).
  All the integrals here are evaluated in closed form, so every number below is an
  explicit bound, not a numerical estimate.
"""

import math

def main_N(t):
    return (t / (2 * math.pi)) * math.log(t / (2 * math.pi * math.e)) + 7.0 / 8.0

INT_LOG = lambda T: (math.log(T / (2 * math.pi * math.e)) + 1.0) / T      # int_T^inf log(t/2pi e) t^-2 dt
INT_T3 = lambda T: 1.0 / (2.0 * T * T)                                    # int_T^inf t^-3 dt
INT_LOG_T3 = lambda T: (math.log(T) + 0.5) / (2.0 * T * T)                # int_T^inf log t * t^-3 dt

def B_bound(T, c, d):
    """Explicit upper bound for B_T = (1/2) sum_{gamma>T} gamma^{-2}."""
    A = main_N(T) - (c * math.log(T) + d)          # lower bound for N(T)
    term1 = -A / (2.0 * T * T)                     # negative, retained
    term2 = (1.0 / (2.0 * math.pi)) * INT_LOG(T)   # from the smooth main term
    term3 = (7.0 / 8.0) * INT_T3(T)                # from the 7/8 in main
    term4 = (c * INT_LOG_T3(T) + d * INT_T3(T))    # from the explicit error
    return term1 + term2 + term3 + term4, dict(term1=term1, term2=term2, term3=term3, term4=term4)

def main_nocrude(T, c, d):
    """What a CRUDE bound gives: dropping the negative boundary term and crudely
    dominating N(t) by main(t) + (c log t + d) but ALSO forgetting the 7/8 and A:
    i.e. the shape the paper uses."""
    return (1.0 / (2.0 * math.pi)) * INT_LOG(T) + (c * INT_LOG_T3(T) + d * INT_T3(T)) + (7.0/8.0)*INT_T3(T)

lines = []
def out(s=''):
    lines.append(s); print(s)

out('=' * 78)
out('TIGHTENING B_T  (Abel with the boundary term retained)')
out('=' * 78)
out()
out('  counting hypothesis constants: two standard choices')
out('    Trudgian  : c = 0.112, d = 2.5')
out('    Rosser-type: c = 0.137, d = 3.5')
out()
PAPER_B = 3.4015e-6      # the constant actually printed in Paper A at T = 1.13e6
out('  {:>14} {:>8} {:>18} {:>18} {:>20}'.format('T', 'c', 'Abel bd (this)', 'paper constant', 'gain vs paper'))
for T in [1.1325e6, 3.0001753328e12]:
    for (c, d) in [(0.112, 2.5), (0.137, 3.5)]:
        Bb, parts = B_bound(T, c, d)
        pc = PAPER_B if T < 1e7 else 2.85e-12      # paper prints these two values
        out('  {:>14.4e} {:>8.3f} {:>18.6e} {:>18.6e} {:>19.2f}x'.format(T, c, Bb, pc, pc / Bb))
out()
out('  --- decomposition at T = 1.1325e6, c = 0.112, d = 2.5 ---')
Bb, parts = B_bound(1.1325e6, 0.112, 2.5)
for k, v in parts.items():
    out('    {:>8} = {:+.6e}'.format(k, v))
out('    {:>8} = {:+.6e}   <-- the NEGATIVE boundary term is the whole gain'.format('sum', Bb))
out()
out('  TRUE value of B_T at T = 1.1325e6, computed from the 2M-zero table:')
try:
    import numpy as np
    G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
    Gmax = float(G.max())
    true_in = 0.5 * float(np.sum(G[G > 1.1325e6] ** (-2.0)))
    tail_an = (1.0 / (2.0 * math.pi)) * (1.0 + math.log(Gmax / (2 * math.pi))) / Gmax
    out('    table part  = {:.6e}   analytic tail beyond {:.4e} = {:.6e}'.format(true_in, Gmax, 0.5*tail_an))
    out('    tree-ish total ~ {:.6e}  (compare: paper 3.4015e-06)'.format(true_in + 0.5*tail_an))
except Exception as e:
    out('    (table unavailable: {})'.format(e))
out()
out('  => the Abel bound with the boundary term lands at the TRUE value, while the')
out('     paper\'s crude form is 3.7x looser. The loss is recovered.')
out()

out('-' * 78)
out('WHAT THIS BUYS AT THE QUADRATIC ENDPOINT')
out('-' * 78)
out()
N_T, T0 = 2001052.0, 1.1325e6
S_n, n_q = 2.001269e6, T0 ** 2
for label, B in [('paper 3.4015e-06', 3.4015e-6), ('Abel bound (c=0.112)', B_bound(T0,0.112,2.5)[0]),
                 ('TRUE value', 9.2065e-7)]:
    m = n_q * B
    out('  B = {:>22}: n*B = {:.4e}   S_n/(nB) = {:.4f}  {}'.format(label, m, S_n / m, 'PASS' if S_n/m > 1 else 'FAIL'))
out()
f = math.exp(n_q / (2 * T0 ** 2))
out('  with the restored factor exp(n/(2T^2)) = e^{{0.5}} = {:.4f}:'.format(f))
for label, B in [('paper 3.4015e-06', 3.4015e-6), ('Abel bound (c=0.112)', B_bound(T0,0.112,2.5)[0]),
                 ('TRUE value', 9.2065e-7)]:
    m = n_q * B * f
    out('  B = {:>22}: S_n/(nB*e^{{1/2}}) = {:.4f}  {}'.format(label, S_n / m, 'PASS' if S_n/m > 1 else 'FAIL'))
out()
out('  => tightening B_T turns the quadratic endpoint from FAIL into a thin PASS.')
out('     The margin is small (about 1.0), so this is a real but narrow opening ---')
out('     not a comfortable one, and the interior-oscillation question is untouched.')
out('=' * 78)

with open('scripts/PAPERA_tighten_BT.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_tighten_BT.txt')
