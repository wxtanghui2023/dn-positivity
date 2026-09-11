#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Verify Lehmer pairs (nearly-degenerate zero pairs) with A1 detector.
# These are the theoretical candidate locations for off-axis zeros ("low-near").
import numpy as np
import mpmath as mp
mp.mp.dps = 30

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gaps = np.diff(zeros)

def logxi_deriv1(s):
    return (1/s + 1/(s-1) - 0.5*mp.log(mp.pi)
            + 0.5*mp.digamma(s/2) + mp.zeta(s, derivative=1)/mp.zeta(s))

def interference_S(g0, eps):
    dg = np.abs(zeros - g0)
    dg = dg[dg > 1e-6]
    return eps**2 * np.sum(1.0/(eps**2 + dg**2))

# Test the tightest pairs AND both members
tightest = np.argsort(gaps)[:8]
eps = 0.005  # smaller eps for tighter resolution (pairs ~0.015-0.04 apart)
print(f"=== Lehmer pair verification (eps={eps}) ===")
print(f"{'pair':>6} {'gamma_a':>10} {'gamma_b':>10} {'gap':>8} | {'A_a*eps':>9} {'A_b*eps':>9} {'pred':>9}")
for i in sorted(tightest):
    ga, gb = zeros[i], zeros[i+1]
    gap = gaps[i]
    res = []
    for g0 in [ga, gb]:
        s0 = 0.5 + 1j*g0 + eps
        A1 = logxi_deriv1(s0)
        num = float(mp.re(A1)*eps)
        S = interference_S(g0, eps)
        pred = 1 + S
        res.append((num, pred))
    # note: for tight pairs, the OTHER member is very close -> its pole at distance ~gap
    # A1 at ga: target pole at eps, partner pole at gap-eps (if on-line both at 1/2)
    print(f"{i+1:>6} {ga:>10.4f} {gb:>10.4f} {gap:>8.5f} | {res[0][0]:>9.5f} {res[1][0]:>9.5f} pred_a={res[0][1]:>9.5f} pred_b={res[1][1]:>9.5f}")
