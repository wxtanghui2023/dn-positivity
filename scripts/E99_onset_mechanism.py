"""E99 - mechanism of the quadratic law: onset of an off-line zero's exponential growth.

PURPOSE
  The project's unified framework records a quadratic conversion law, verified height T
  giving reachable index about T squared, without an explanation of where the square
  comes from.  This script derives and checks the elementary mechanism on the Li side.

  For a zero rho = 1/2 + i*gamma its partner under the functional equation is
  1 - conj(rho) = 1/2 + i*gamma, which is the zero itself, so on-line zeros are
  self-paired.  For an off-line zero at beta = 1/2 + eps the partner is 1/2 - eps + i*gamma,
  and with q = 1 - 1/rho one has |q| = r < 1 for the way-in zero and |q'| = 1/r > 1 for the
  partner, so the partner's contribution to the Li coefficient lambda_n grows like r^{-n}.

  Claim: 1 - r ~ eps/gamma^2 (the numeric check in part 1 corrected an initial factor-two
  error of mine), hence the contribution grows like exp(eps*n/gamma^2) and becomes visible
  at onset n0 ~ gamma^2*log(M)/eps.  Worst case eps of order one gives n0 ~ gamma^2, which
  is the quadratic law.

INPUT
  none (closed-form arithmetic; mpmath for the high-precision checks).

OUTPUT
  scripts/E99_onset_mechanism.txt (beside this script).

CONCLUSION
  see the .txt; the derivation is heuristic (an onset estimate), not a proof that no
  criterion can do better.  No RH used, no Lean run.
PROVENANCE
  written by 小灵 on 唐先生's instruction 2026-09-13 21:18; framework reference
  docs/E30-UNIFIED-CONVERSION-LAW.md and docs/MASTER-NOGO-AND-LIVE-PATHS.md.
"""
import math

try:
    from mpmath import mp, mpf, mpc, fabs
    mp.dps = 40
    HAVE = True
except Exception:
    HAVE = False


def r_of(eps, gamma):
    """|q| = |(rho-1)/rho| for rho = 1/2 + eps + i*gamma (the way-in zero)."""
    b = 0.5 + eps
    num = (b - 1.0) ** 2 + gamma ** 2
    den = b ** 2 + gamma ** 2
    return math.sqrt(num / den)


print("E99 - onset mechanism of the quadratic law")
print("=" * 78)
print("(1) 1 - r versus the predicted eps/gamma^2")
print(f"{'eps':>8} {'gamma':>10} {'1-r':>18} {'2*eps/g^2':>18} {'ratio':>10}")
rows = []
for eps in (0.5, 0.1, 0.01, 0.001):
    for gamma in (1e2, 1e3, 1e4, 1e6):
        r = r_of(eps, gamma)
        pred = eps / gamma ** 2
        rows.append((eps, gamma, 1.0 - r, pred, (1.0 - r) / pred))
        print(f"{eps:>8} {gamma:>10.0e} {1.0-r:>18.12e} {pred:>18.12e} {(1.0-r)/pred:>10.5f}")
print()
print("  -> the identity is exact to leading order; ratio tends to 1 as gamma grows")
print()

print("(2) onset index n0 where the partner's growth matches a main term of size M")
print("    r^{-n} = exp(eps*n/gamma^2) >= M   =>   n0 = gamma^2*log(M)/eps")
print(f"{'eps':>8} {'gamma':>10} {'n0 for M=1e2':>18} {'n0 for M=1e6':>18}")
for eps in (0.5, 0.1, 0.01):
    for gamma in (1e3, 1e6):
        n_a = gamma ** 2 * math.log(1e2) / eps
        n_b = gamma ** 2 * math.log(1e6) / eps
        print(f"{eps:>8} {gamma:>10.0e} {n_a:>18.4e} {n_b:>18.4e}")
print()
print("  -> worst case eps of order one: n0 ~ gamma^2 (up to a log) = the quadratic law")
print("  -> a nearly-on-line zero (eps -> 0) has onset FAR LARGER: it is invisible")
print()

if HAVE:
    print("(3) high-precision check of |q'| = 1/r and of the partner's growth")
    for eps, gamma in ((mpf('0.1'), mpf('1000')), (mpf('0.01'), mpf('1000'))):
        rho_in = mpc('0.5') + eps + mpc(0, 1) * gamma
        rho_out = mpc('0.5') - eps + mpc(0, 1) * gamma
        q_in = 1 - 1 / rho_in
        q_out = 1 - 1 / rho_out
        prod = fabs(q_in) * fabs(q_out)
        print("    eps=%s gamma=%s: |q_in|*|q_out|-1 = %.3e   |q_out|-1 = %.12e"
              "   predicted eps/g^2 = %.12e"
              % (eps, gamma, float(prod - 1), float(fabs(q_out) - 1), float(eps / gamma ** 2)))
    print()
print("=" * 78)
print("Boundary: the onset estimate is heuristic. It explains the quadratic law as the")
print("worst case over admissible configurations, but it is NOT a proof that no criterion")
print("consuming only 'no off-line zeros up to height T' can beat T squared.")
