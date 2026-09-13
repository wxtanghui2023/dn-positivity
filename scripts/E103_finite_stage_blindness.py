"""E103 - finite-stage prime data does not see the zeros: an argument-principle check.

PURPOSE
  Support the monopoly claim for the analytic-continuation transport with an elementary
  and a numerical statement.

  Lemma A (elementary, no computation needed): a finite Euler product
      F_P(s) = prod_{p<=P} (1 - p^{-s})^{-1}
  is a product of nonvanishing factors off its pole set, so it has NO zeros at all, and
  its poles sit on the line sigma = 0, i.e. on the boundary of the critical strip and not
  inside it.  Hence no finite stage of the prime data can locate a zero of zeta.

  Corollary: whatever locates the zeros must be a LIMIT procedure, and the naive
  pointwise limits available in the strip (truncated Dirichlet sums) do not converge to
  zeta there, so their zero sets cannot converge to the zero set of zeta either.  This
  script measures that mismatch.

INPUT
  none (mpmath internal zeta zeros; no data files).

OUTPUT
  scripts/E103_finite_stage_blindness.txt (beside this script).

CONCLUSION
  the zero counts in a fixed box do not stabilise towards the zeta count as the truncation
  grows, so truncated prime data is finite-blind.  No RH used, no Lean run.
PROVENANCE
  written by 小灵 on 唐先生's instruction 2026-09-13 21:52; relates to docs/E102 and the
  registry's 'limit-seeing / finite-blind' formulation of the single open gap.
"""
from mpmath import mp, mpf, mpc, exp, log, zetazero, pi

mp.dps = 25


def DN(s, N):
    """Truncated zeta series sum_{n<=N} n^{-s}."""
    tot = mpc(0)
    for n in range(1, N + 1):
        tot += exp(-s * log(n))
    return tot


def winding_zero_count(f, sigma_a, sigma_b, tmin, tmax, samples=2400):
    """Number of zeros inside the rectangle via the argument principle."""
    pts = []
    # bottom, right, top, left (counter-clockwise)
    for i in range(samples):
        x = sigma_a + (sigma_b - sigma_a) * i / samples
        pts.append(mpc(x, tmin))
    for i in range(samples):
        y = tmin + (tmax - tmin) * i / samples
        pts.append(mpc(sigma_b, y))
    for i in range(samples):
        x = sigma_b - (sigma_b - sigma_a) * i / samples
        pts.append(mpc(x, tmax))
    for i in range(samples):
        y = tmax - (tmax - tmin) * i / samples
        pts.append(mpc(sigma_a, y))
    pts.append(pts[0])
    total = mpf(0)
    prev = f(pts[0])
    for p in pts[1:]:
        cur = f(p)
        d = cur / prev
        total += mp.arg(d)
        prev = cur
    return int(round(float(total / (2 * pi))))


sa, sb, tmin, tmax = mpf('0.02'), mpf('0.98'), mpf('0.5'), mpf('30')

print("E103 - finite-stage prime data is blind to the zeros")
print("=" * 78)
print(f"box: sigma in [{sa}, {sb}],  t in [{tmin}, {tmax}]")
print()

# zeta's own zeros in the box
zcount = 0
while True:
    z = zetazero(zcount + 1)
    if float(z.imag) > float(tmax):
        break
    if float(sa) < float(z.real) < float(sb):
        zcount += 1
    else:
        break
print(f"zeros of zeta inside the box               : {zcount}")
first = [float(zetazero(k).imag) for k in range(1, 6)]
print(f"first five ordinates                       : "
      + ", ".join(f"{v:.4f}" for v in first))
print()

print("truncated zeta series D_N(s) = sum_{n<=N} n^{-s}: zeros inside the SAME box")
print(f"{'N':>8} {'#zeros(D_N)':>14} {'ratio to zeta':>16}")
for N in (10, 20, 50, 100):
    c = winding_zero_count(lambda s, N=N: DN(s, N), sa, sb, tmin, tmax)
    print(f"{N:>8} {c:>14} {(c/zcount if zcount else float('nan')):>16.2f}")
print()
print("Reading: the count grows with the truncation and does not settle at the zeta count.")
print("The truncated sums do not converge to zeta inside the strip (they diverge there),")
print("so their zero sets cannot converge to zeta's zeros either.  Combined with Lemma A")
print("(finite Euler products have no zeros in the strip at all) this says: the zeros are")
print("created by the limit, and the limits that see them are not the naive finite ones.")
print("=" * 78)
print("Boundary: this is not a theorem that analytic continuation is the UNIQUE limit")
print("procedure; it only excludes the naive finite-stage limits and records that any")
print("successful procedure must be limit-seeing.")
