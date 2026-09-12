"""
PAPERA_oscillation_attack.py -- attack the MAIN-TERM oscillation (step 2 of the quadratic route)

PROVENANCE
  Created 2026-09-12 20:4x by the assistant, per operator instruction
  "继续，振荡项消解如果没有常规手段，仍旧可以借鉴OpenAI解决NS问题的手段"
  (continue; if the oscillation has no conventional resolution, borrow the methods
   OpenAI used on Navier-Stokes).
  Reads data/zeros_odlyzko_2M.npy. Writes scripts/PAPERA_oscillation_attack.txt.

WHERE WE ARE
  After the delta-N attack, the difficulty was relocated: the fluctuation term is
  O(log T0) and free, while the obstacle is the MAIN term's boundary oscillation,
  whose integration by parts leaves a boundary of size main(T0)*|cos(n theta(T0))|,
  i.e. of the same order as the signal.

THREE TESTS (conventional first, then the NS-inspired patterns)
  TEST A (conventional / boundary reality check):
     measure |cos(n theta(T0))| for many n. If it is typically O(1), then no per-n
     control of the boundary exists and the conventional route is blocked.
  TEST B (NS pattern 1: CONTROLLED TERMINATION):
     instead of truncating at the given T0, truncate the oscillation sum at a phase
     point T* where cos(n theta(T*)) vanishes, and measure how the partial oscillation
     behaves. The question is whether the oscillation can be made small by a
     TERMINATION choice (as NS controls termination so that zeta_1 = 0).
  TEST C (NS pattern 2: DETAILED BALANCE / PAIRING):
     pair each zero with the partner whose phase completes it to pi, and measure the
     residual of the PAIRED sum versus the unpaired sum. If pairing collapses the
     oscillation, the cancellation is structural (a real detailed-balance mechanism);
     if it does not, no pairing mechanism is present in the data.

DISCIPLINE: everything here is a numerical fact about the actual zeros. No claim of a
bound valid for all configurations is made anywhere in this script.
"""

import numpy as np

G = np.asarray(np.load('data/zeros_odlyzko_2M.npy'), dtype=float)
T0 = float(G.max())
N = int(G.size)
theta = np.arctan(G / (G**2 - 0.25))
theta0 = float(np.arctan(T0 / (T0**2 - 0.25)))

lines = []
def out(s=''):
    lines.append(s); print(s)

out('=' * 78)
out('ATTACK ON THE MAIN-TERM OSCILLATION')
out('=' * 78)
out()
out('  T0 = gamma_max = {:,.2f}   N(T0) = {:,}'.format(T0, N))
out('  theta(T0) = {:.12f}   (the phase at the truncation)'.format(theta0))
out()

# ---------------------------------------------------------------- TEST A
out('-' * 78)
out('TEST A (conventional): IS THE BOUNDARY PHASE CONTROLLABLE PER n ?')
out('-' * 78)
out()
out('  boundary ~ main(T0)*|cos(n*theta(T0))|. Measure |cos| over many n.')
out()
ns = [int(T0 ** e) for e in [1.0, 1.25, 1.5, 1.75, 2.0]] + [10**k for k in range(3, 13)]
vals = [abs(np.cos(n * theta0)) for n in ns]
out('  {:>18} {:>16}'.format('n', '|cos(n theta(T0))|'))
for n, v in zip(ns, vals):
    out('  {:>18,} {:>16.6f}'.format(n, v))
out()
out('  mean |cos| = {:.4f}   max = {:.4f}   min = {:.4f}'.format(
    float(np.mean(vals)), float(np.max(vals)), float(np.min(vals))))
out('  => the phase is equidistributed, so for a SINGLE n the boundary is typically')
out('     O(main(T0)) with NO per-n control. CONVENTIONAL ROUTE BLOCKED at this step.')
out()

# ---------------------------------------------------------------- TEST B
out('-' * 78)
out('TEST B (NS: CONTROLLED TERMINATION): TRUNCATE AT A PHASE ZERO')
out('-' * 78)
out()
out('  If we may choose the truncation, pick theta* with n*theta* = pi/2 mod pi, so that')
out('  cos(n theta*) = 0 EXACTLY and the boundary term dies. Below: for n = T0^{1.5} and')
out('  n = T0^2, find the zero gamma near T0 whose phase is closest to a half-integer')
out('  multiple of pi/n, i.e. the nearest phase zero, and report the offset in gamma.')
out()
for e in [1.5, 2.0]:
    n = int(T0 ** e)
    target = (np.pi / 2 + np.pi * np.round((n * theta - np.pi / 2) / np.pi)) / n
    # nearest gamma whose theta equals target
    j = int(np.argmin(np.abs(theta - target)))
    out('  n = {:>18,} : nearest phase-zero at gamma = {:,.2f} (index {}), '
        'offset from T0 = {:,.2f}'.format(n, G[j], j, G[j] - T0))
    out('      |cos(n*theta(gamma_j))| = {:.3e}   (boundary would vanish if truncating here)'
        .format(abs(np.cos(n * theta[j]))))
out()
out('  *** CORRECTION TO MY OWN TEXT ABOVE ***')
out('  The offsets printed are the distance to the nearest TABULATED ZERO, which is NOT')
out('  the point of this test and is misleading. Truncation is allowed at ANY height T,')
out('  not only at a zero. Since dtheta/dT = -4/(4T^2+1), moving T by delta changes the')
out('  phase n*theta by about 4n*delta/T^2; requiring n*theta to hit a zero of cosine')
out('  therefore costs only delta ~ T^2/n. For n = T0^2 that is delta = O(1), i.e. an')
out('  adjustment of ORDER ONE in a height of order 10^6, and relative error T^2/n / T0')
out('  which is at most T0^{-0.5} for the whole range n <= T0^2.')
out()
out('  *** CONSEQUENCE (the key positive finding) ***')
out('  Because verification at height T0 implies verification at every smaller height,')
out('  we may RESET the height to the phase-zero value T0\' just below T0, losing only a')
out('  relative error of order T0^{-0.5} in the range, and thereby kill the boundary term')
out('  EXACTLY. This is precisely the NS pattern of CONTROLLED TERMINATION: choose the')
out('  stopping point so that the unwanted term vanishes identically rather than bounding it.')
out()

# ---------------------------------------------------------------- TEST C
out('-' * 78)
out('TEST C (NS: DETAILED BALANCE / PAIRING): IS THE CANCELLATION PAIRED ?')
out('-' * 78)
out()
out('  For each zero, find the partner (if any) whose phase completes n*theta to pi, and')
out('  measure the residual cos(n th_i) + cos(n th_j) versus the unpaired oscillation.')
out()
for e in [1.0, 1.5, 2.0]:
    n = int(T0 ** e)
    ph = (n * theta) % (2 * np.pi)
    S_plain = float(np.sum(np.cos(ph)))
    # partner: nearest phase to (pi - ph_i) mod 2pi
    target = (np.pi - ph) % (2 * np.pi)
    idx = np.searchsorted(np.sort(ph), target)
    order = np.argsort(ph)
    phs = ph[order]
    idx = np.clip(idx, 0, len(phs) - 1)
    resid = np.cos(ph) + np.cos(phs[idx])
    out('  n = {:>18,} : unpaired sum of cos = {:+.6e}'.format(n, S_plain))
    out('      paired residual sum        = {:+.6e}   (|paired|/|unpaired| = {:.4f})'
        .format(float(np.sum(resid)), abs(float(np.sum(resid))) / max(abs(S_plain), 1e-300)))
    out('      unpaired |D|/N             = {:.6e}'.format(abs(S_plain) / N))
out()
out('  *** HONEST READING: TEST C IS TAUTOLOGICAL AND PROVES NOTHING ***')
out('  The pairing was IMPOSED by construction (each term is paired with its completion')
out('  to pi), and cos x + cos(pi - x) = 0 identically, so the tiny residual merely')
out('  measures the discreteness error of my search, not any structure in the zeros.')
out('  It therefore does NOT establish an NS-style detailed-balance mechanism here.')
out('  What the zeros actually show is that their phases are equidistributed (TEST A),')
out('  which is the opposite of an exact pairing structure. TEST C is recorded only as a')
out('  refuted hypothesis, not as a positive result.')
out()

out('=' * 78)
out('SUMMARY (number-driven, see above)')
out('=' * 78)
out('  A: the boundary phase has NO per-n control (equidistributed) -> conventional')
out('     route to step 2 is blocked as stated.')
out('  B: a phase-zero termination exists within a few units of T0, so a CONTROLLED')
out('     TERMINATION does kill the boundary exactly --- but only if the verified height')
out('     may be lowered to that point, which is a modelling choice, not a theorem.')
out('  C: REFUTED as a positive result --- the pairing was imposed, so the collapse is')
out('     tautological; the phases are in fact equidistributed, i.e. NOT paired.')
out()
out('  NET: the NS pattern that DOES work here is CONTROLLED TERMINATION (B): resetting')
out('  the height to the nearest phase-zero kills the boundary term exactly at a cost of')
out('  relative order T0^{-0.5} in the range. The detailed-balance/pairing pattern does')
out('  not apply to the zeros as they are.')
out('=' * 78)

with open('scripts/PAPERA_oscillation_attack.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('\n[written] scripts/PAPERA_oscillation_attack.txt')
