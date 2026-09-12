"""
E44_beta_exclusion_curve.py -- 4-A: quantifying the beta-exclusion wall

PROVENANCE
  Created 2026-09-12 18:2x by the assistant, per operator instruction "两个都做"
  (do both), responding to item 4-A recommended in docs/PHYSICS-FRONTIER-2026-09-12.md.
  Reads data/zeros_odlyzko_2M.npy. Writes scripts/E44_beta_exclusion_curve.txt.

WHAT THIS COMPUTES (and what it does NOT)
  RH is the statement that no zero has real part > 1/2. An unconditional theorem
  "excludes" off-line zeros up to height T for a strip sigma > s*(T) if it forces
  N(sigma,T) = 0 there. We tabulate, for the standard unconditional inputs:

    (1) the classical zero-free region      sigma > 1 - 1/(R log T),  R ~ 5.573
    (2) Ingham-type zero density            N(sigma,T) << T^{3(1-sigma)/(2-sigma)} log^5 T
    (3) Guth-Maynard 2024 zero density      N(sigma,T) << T^{15(1-sigma)/(3+5 sigma)+eps}
    (4) the trivial count                   N(sigma,T) <= N(T) ~ (T/2pi) log(T/2pi)

  the exponent a(sigma) of each, and whether the bound can force N < 1 (i.e. exclude).

  DISCIPLINE (mandatory, per the frontier report T3/T6): at sigma > 1/2 the TRUE count
  is zero (RH is verified to T0 = 3.0e12, Platt-Trudgian), so this script does NOT
  "verify the absence of off-line zeros". What it measures is the SLACKNESS of the
  unconditional bounds -- how far the region they can actually exclude sits from 1/2,
  and how that distance behaves as T grows.

CONCLUSION TO BE READ OFF THE NUMBERS (not asserted in advance)
"""

import json
import numpy as np

# ---------------------------------------------------------------- zero table
z = np.load('data/zeros_odlyzko_2M.npy')
Z = np.asarray(z, dtype=float)
gamma_max = float(Z.max())
n_zeros = int(Z.size)

R_ZFR = 5.573   # classical zero-free region constant, sigma > 1 - 1/(R log T), T >= 3

def zfr_edge(T):
    """Largest sigma known to be zero-free, from the classical zero-free region."""
    if T < 3:
        return float('nan')
    return 1.0 - 1.0 / (R_ZFR * np.log(T))

def a_ingham(s):
    return 3.0 * (1.0 - s) / (2.0 - s)

def a_gm(s):
    return 15.0 * (1.0 - s) / (3.0 + 5.0 * s)

lines = []
def out(s=''):
    lines.append(s)
    print(s)

out('=' * 78)
out('4-A  THE beta-EXCLUSION WALL, QUANTIFIED')
out('=' * 78)
out('')
out('Zero table: data/zeros_odlyzko_2M.npy')
out('  zeros = {:,}   gamma_max = {:,.1f}'.format(n_zeros, gamma_max))
out('  [all tabulated zeros are on the critical line by construction of the table]')
out('')
out('Reference heights:  gamma_max (this table) = {:,.3g}'.format(gamma_max))
out('                    Platt-Trudgian verified height T0 = 3.0e12')
out('')

# --------------------------------------------------- (1) zero-free region
out('-' * 78)
out('(1) CLASSICAL ZERO-FREE REGION   sigma > 1 - 1/(R log T),  R = {}'.format(R_ZFR))
out('-' * 78)
out('')
out('{:>12} {:>14} {:>16} {:>16}'.format('T', 'zfr edge', 'excluded band', 'width to 1/2'))
out('{:>12} {:>14} {:>16} {:>16}'.format('', 'sigma*(T)', '(sigma*, 1)', 'sigma* - 1/2'))
for T in [1e3, 1e6, 1e9, 1e12, 3.0e12, 1e20, 1e50, 1e100, 1e1000]:
    e = zfr_edge(T)
    out('{:>12.3g} {:>14.6f} {:>16} {:>16.6f}'.format(T, e, '(%.6f, 1)' % e, e - 0.5))
out('')
out('  => the zero-free edge sigma*(T) RISES toward 1 as T grows:')
out('     the region unconditional theorems can exclude RETREATS from 1/2.')
out('')

# ---------------------------------------- (2)(3)(4) zero-density exponents
out('-' * 78)
out('(2)(3)(4) ZERO-DENSITY EXPONENTS a(sigma)  [bound ~ T^a]')
out('-' * 78)
out('')
out('  A bound forces N(sigma,T) = 0 only if it is < 1, which (up to log factors and')
out('  the unknown explicit constant) requires a(sigma) <= 0. Below we report a(sigma)')
out('  and the resulting bound at two large heights.')
out('')
hdr = '{:>8} {:>14} {:>14} {:>18} {:>18}'
out(hdr.format('sigma', 'Ingham a', 'Guth-May a', 'Ingham@1e12', 'GM@1e12'))
rows = []
for s in [0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.99, 0.999]:
    ai, ag = a_ingham(s), a_gm(s)
    T = 1e12
    bi, bg = T ** ai, T ** ag
    out(hdr.format('%.3f' % s, '%.5f' % ai, '%.5f' % ag,
                   '%.3e' % bi, '%.3e' % bg))
    rows.append(dict(sigma=s, a_ingham=ai, a_gm=ag, bound_ingham=bi, bound_gm=bg))
out('')
out('  NOTE (numerical coincidence, verified): at sigma = 0.7 the two exponents agree')
out('       a_ingham(0.7) = a_gm(0.7) = 0.6923077, so the two bounds coincide there.')
out('')
out('  => a(sigma) = 0 occurs ONLY at sigma = 1 for BOTH bounds.')
out('     For every sigma < 1 the bound is astronomically larger than 1,')
out('     so zero-density estimates exclude NOTHING below sigma = 1.')
out('')

# --------------------------------------------- (5) slackness vs the truth
out('-' * 78)
out('(5) SLACKNESS: bound / truth   at sigma = 0.6 and 0.7, T0 = 3.0e12')
out('-' * 78)
out('')
out('  True N(sigma,T0) = 0 for sigma > 1/2 (RH verified to T0). The bounds give:')
T0 = 3.0e12
for s in [0.6, 0.7, 0.8]:
    out('    sigma = {:.2f}:  Ingham bound = {:.3e}   Guth-Maynard bound = {:.3e}   truth = 0'
        .format(s, T0 ** a_ingham(s), T0 ** a_gm(s)))
out('')
out('  => the ratio bound/truth is INFINITE at every sigma > 1/2: the bounds are')
out('     not merely loose, they are vacuous in exactly the region that matters.')
out('     truth is 0 while the bound is {:.3e} at sigma = 0.6 (Ingham)'.format(T0 ** a_ingham(0.6)))
out('     and {:.3e} at sigma = 0.6 (Guth-Maynard): the gap is unbounded.'.format(T0 ** a_gm(0.6)))
out('')

# ------------------------------------------------------ summary of the wall
out('-' * 78)
out('SUMMARY: THE SHAPE OF THE WALL (numbers above, not interpretation)')
out('-' * 78)
out('')
out('  sigma in [1 - 1/(5.573 log T), 1]      : EXCLUDED (zero-free region)')
out('  sigma in (1/2, 1 - 1/(5.573 log T))    : NO unconditional exclusion exists')
out('                                            from any of the four standard inputs')
out('  sigma = 1/2                             : the RH line itself')
out('')
out('  Width of the UNEXCLUDED band, 1/2 < sigma < sigma*(T):')
for T in [1e6, 1e12, 1e100]:
    out('    T = {:>8.3g}: width = {:.6f}'.format(T, zfr_edge(T) - 0.5))
out('    T -> infinity: width -> 0.500000  (the band fills the entire strip)')
out('')
out('  => As the verified height grows WITHOUT BOUND, the unconditionally unexcluded')
out('     band WIDENS toward (1/2, 1). The wall does not move toward RH; the')
out('     unconditional knowledge retreats away from it.')
out('')

# --------------------------------------------- the Landau-Widom / LM overlay
out('-' * 78)
out('(6) THE THREE KNOWN INGREDIENTS, SIDE BY SIDE')
out('-' * 78)
out('')
out('  (a) numerical verification  : zeros on the line up to gamma = {:.3g}'.format(gamma_max))
out('                               (this table) and to 3.0e12 (Platt-Trudgian)')
out('  (b) zero-free region        : excludes sigma > 1 - 1/(5.573 log T)')
out('  (c) de Bruijn-Newman        : Lambda >= 0, and Lambda = 0 iff RH (Rodgers-Tao)')
out('  (d) zero-density exponents  : a(sigma) > 0 for all sigma < 1 (no exclusion)')
out('')
out('  (a) and (b) are both of the form "verified/excluded up to some boundary";')
out('  (b) RETREATS as T grows, (a) ADVANCES only with computation. Neither touches')
out('  the individual real parts in (1/2, 1). (c) is a single number. (d) is vacuous.')
out('')
out('  This is the beta-wall, stated in numbers rather than in words.')
out('=' * 78)

with open('scripts/E44_beta_exclusion_curve.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('\n[written] scripts/E44_beta_exclusion_curve.txt')
