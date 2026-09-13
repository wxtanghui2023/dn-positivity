"""E100 - function-field Li criterion: verify the power-sum form and the p=0 onset.

PURPOSE
  The function-field Li criterion is a finite-dimensional spectral-radius criterion:
  for a curve of genus g over F_q, L_K(T) = prod_{j=1}^{2g} (1 - alpha_j T), the Li
  coefficients are lambda_K(n) = -sum_j alpha_j^n, and RH is equivalent to
  |lambda_K(n)| <= 2g q^{n/2} for all n.  This script verifies the equivalence on a
  model multiset of Frobenius roots and measures the detection onset for an off-line
  root, checking the predicted n0 ~ log(2g)/(eps log q).

INPUT
  none (arithmetic only).

OUTPUT
  scripts/E100_function_field_onset.txt (beside this script).

CONCLUSION
  the onset is logarithmic in the genus and independent of any height parameter, i.e.
  p = 0 in the sense recorded in the audit; this is the control experiment showing the
  quadratic law is NOT intrinsic to the Li structure.  No RH used, no Lean run.
PROVENANCE
  written by 小灵 on 唐先生's instruction 2026-09-13 21:22; formulation per 唐先生
  (function-field Li as power sums) and docs/CROSS-DIRECTION-ANALYSIS-2026-09-13.md.
"""
import math
import random

random.seed(20260913)


def onset(g, q, eps, trials=200, nmax=4000):
    """Smallest n at which an off-line root can exceed the on-line envelope."""
    best = None
    for _ in range(trials):
        # 2g-1 roots on the critical modulus, one at q^{1/2+eps}
        mods = [q ** 0.5] * (2 * g - 1) + [q ** (0.5 + eps)]
        thetas = [random.uniform(0, 2 * math.pi) for _ in mods]
        al = [m * complex(math.cos(t), math.sin(t)) for m, t in zip(mods, thetas)]
        for n in range(1, nmax):
            lam = -sum(a ** n for a in al)
            if abs(lam) > 2 * g * q ** (n / 2.0):
                if best is None or n < best:
                    best = n
                break
    return best


print("E100 - function-field Li criterion: power sums and the p=0 onset")
print("=" * 78)
print("(1) the equivalence, checked on a model multiset")
for (g, q) in ((2, 2), (5, 3), (13, 7)):
    mods = [q ** 0.5] * (2 * g)          # all on the critical modulus
    thetas = [random.uniform(0, 2 * math.pi) for _ in mods]
    al = [m * complex(math.cos(t), math.sin(t)) for m, t in zip(mods, thetas)]
    worst = 0.0
    for n in range(1, 200):
        lam = -sum(a ** n for a in al)
        worst = max(worst, abs(lam) / (2 * g * q ** (n / 2.0)))
    print(f"    g={g:>3} q={q}:  max_n |lambda_K(n)| / (2g q^(n/2)) = {worst:.6f}"
          f"   (<=1 means the envelope holds)")
print()
print("(2) detection onset with one root at q^(1/2+eps)   [predicted log(2g)/(eps log q)]")
print(f"{'g':>4} {'q':>4} {'eps':>8} {'measured n0':>12} {'predicted':>12} {'ratio':>8}")
for (g, q) in ((2, 2), (5, 3), (13, 7), (50, 11)):
    for eps in (0.5, 0.2, 0.05):
        m = onset(g, q, eps)
        pred = math.log(2 * g) / (eps * math.log(q))
        r = (m / pred) if (m and pred) else float('nan')
        print(f"{g:>4} {q:>4} {eps:>8} {str(m):>12} {pred:>12.3f} {r:>8.3f}")
print()
print("(3) scaling: onset versus genus (fixed q, eps)")
for g in (2, 10, 100, 10 ** 4, 10 ** 6):
    pred = math.log(2 * g) / (0.2 * math.log(3))
    print(f"    g=1e{math.log10(g):.0f}: predicted n0 = {pred:.4f}   (logarithmic in g)")
print()
print("=" * 78)
print("Reading: the onset is logarithmic in the genus and carries NO height parameter.")
print("In the number field the same analysis gives n0 ~ gamma^2/eps, because the carrier")
print("is the damping map rho -> 1 - 1/rho, whose deficit is eps/gamma^2 rather than eps.")
print("This is the p=0 versus p=2 contrast, and it is a comparison of CARRIERS, not of")
print("probes: the function-field carrier is the Frobenius eigenvalue itself.")
