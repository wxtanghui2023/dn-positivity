"""
PAPERA_block_method_test.py -- does the PERIOD-BLOCK method kill the interior oscillation?

PROVENANCE
  Created 2026-09-12 21:0x by the assistant, per operator instruction "先选乙"
  (attack the endpoint on the phase route).
  Writes scripts/PAPERA_block_method_test.txt.

THE IDEA BEING TESTED
  The interior term is  I(n) = int_0^{T0} cos(n theta(t)) d main(t),  with
  theta(t) = 2 arctan(1/(2t)),  main'(t) = (log(t/2 pi e) + 1)/(2 pi).
  The by-parts route leaves an O(main(T0)) boundary.  The BLOCK route instead
  partitions the range where the phase phi = n theta(t) advances by 2 pi, and on each
  FULL block substitutes u = phi(t):

      I(n) = int cos(u) G(u) du,   G(u) := main'(t(u)) / |phi'(t(u))|.

  Now cos(u) against a slowly varying G over a full period gives ZERO for the constant
  AND for the linear term, because
      int_0^{2pi} cos u du = 0   and   int_0^{2pi} u cos u du = [u sin u + cos u] = 0.
  Hence each full block contributes only the CURVATURE term G'' * O(1), and the total is
      I(n) ~ G''(u) * (number of blocks).
  Since phi advances by about n*pi in total, the number of blocks is about n/2, and since
  G ~ n/(2 pi u^2) * log(n/u) the curvature behaves like n/u^4, so the sum over blocks from
  u_min ~ n/T0 upward behaves like  T0^3 / (3 n^2).
  At the quadratic endpoint n = T0^2 this is about 1/(3 T0) --- utterly negligible against
  the signal 2 N(T0) ~ (T0/pi) log T0.

  THIS SCRIPT TESTS THE SCALING DIRECTLY, at small n where I(n) can be computed with a
  fine trapezoid in the u variable (a few hundred blocks at most).

DISCIPLINE: this is a numerical check of a heuristic scaling law, not a proof; the scaling
is what is being tested, and a failure would kill the block route.
"""

import numpy as np
from math import pi, log, atan

T0 = 1.0e6                      # a clean height; the scaling law should be T0-independent in form
def theta(t):  return 2.0*atan(1.0/(2.0*t))
def dthetadt(t): return -4.0/(4.0*t*t + 1.0)
def mainp(t): return (log(t/(2*pi*np.e)) + 1.0)/(2*pi)      # main'(t)

def t_of_phi(phi, n):
    """Invert phi = n*theta(t) for t, by bisection on t in [tiny, huge]."""
    lo, hi = 1e-8, 1e9
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if n*theta(mid) > phi: lo = mid          # theta decreasing -> larger t means smaller phi
        else: hi = mid
    return 0.5*(lo+hi)

def G(u, n):
    t = t_of_phi(u, n)
    return mainp(t)/abs(n*dthetadt(t))

lines = []
def out(s=''):
    lines.append(s); print(s)

out('=' * 78)
out('PERIOD-BLOCK TEST OF THE INTERIOR OSCILLATION')
out('=' * 78)
out()
out('  T0 = {:.2e}   predicted scaling  |I(n)| ~ T0^3/(3 n^2)'.format(T0))
out('  signal 2 N(T0) ~ (T0/pi) log T0 = {:.4e}'.format((T0/pi)*log(T0)))
out()
out('  computing I(n) by fine trapezoid in the u = phi variable (points per block = 400).')
out()
hdr = '{:>10} {:>10} {:>16} {:>16} {:>14} {:>12}'
out(hdr.format('n', 'blocks', 'I(n) numeric', 'predicted', 'num/pred', 'I/2N'))
rows = []
for n in [1e3, 3e3, 1e4, 3e4, 1e5]:
    n = int(n)
    u_hi = n*theta(1e-8)          # phase at t -> 0
    u_lo = n*theta(T0)            # phase at t = T0
    nb = int((u_hi - u_lo)/(2*pi))
    if nb < 1: continue
    per = 400
    M = max(int(nb*per), 2000)
    u = np.linspace(u_lo, u_hi, M)
    t = np.array([t_of_phi(x, n) for x in u])
    Gu = (np.log(t/(2*pi*np.e)) + 1.0)/(2*pi) / np.abs(n*(-4.0/(4.0*t*t+1.0)))
    I = np.trapz(np.cos(u)*Gu, u)
    pred = T0**3/(3.0*n**2)
    rows.append((n, I, pred))
    out(hdr.format(n, nb, '{:+.6e}'.format(I), '{:.6e}'.format(pred),
                   '{:.3f}'.format(abs(I)/pred), '{:.3e}'.format(abs(I)/((T0/pi)*np.log(T0)))))
out()
if len(rows) >= 3:
    ns = np.array([r[0] for r in rows], dtype=float)
    Is = np.array([abs(r[1]) for r in rows])
    sl = np.polyfit(np.log(ns), np.log(Is), 1)[0]
    out('  fitted exponent  |I| ~ n^s  with  s = {:.3f}      (prediction: s = -2)'.format(sl))
    out('  => the prediction s = -2 is {}'.format('CONFIRMED' if abs(sl+2) < 0.4 else 'NOT confirmed'))
out()
out('  ⚠️ CAVEATS: (a) small T0 and small n are used because the integral must be computed')
out('     exhaustively; (b) the block count grows like n/2 so n is limited; (c) the')
out('     comparison to the prediction is a SCALING test, not an absolute bound.')
out('=' * 78)

with open('scripts/PAPERA_block_method_test.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_block_method_test.txt')
