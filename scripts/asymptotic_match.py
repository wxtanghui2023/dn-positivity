#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Asymptotic matching: does Re(A1)*eps match on-line prediction 1+S at HIGHER zeros?
# S = eps^2 * sum_{j!=0} 1/(eps^2 + (gamma_j-gamma_0)^2) over all data zeros.
# If matching persists to high gamma -> on-line holds there (asymptotic evidence).
import numpy as np
import mpmath as mp
import time
mp.mp.dps = 30

zeros = np.load('data/zeros_odlyzko_100k.npy')
print(f"data zeros: {len(zeros)}, last gamma = {zeros[-1]:.1f}")

def logxi_deriv1(s):
    return (1/s + 1/(s-1) - 0.5*mp.log(mp.pi)
            + 0.5*mp.digamma(s/2) + mp.zeta(s, derivative=1)/mp.zeta(s))

def interference_S(g0, eps):
    dg = np.abs(zeros - g0)
    dg = dg[dg > 1e-6]
    return eps**2 * np.sum(1.0/(eps**2 + dg**2))

# sample zeros at increasing heights
ks = [700, 1000, 1400, 1800, 2200, 2700, 3200]  # gamma roughly 1000..4500
eps = 0.01
print(f"\n{'k':>5} {'gamma0':>10} {'ReA1*eps(num)':>15} {'1+S(pred)':>13} {'diff':>10}")
for k in ks:
    g0 = zeros[k]
    t0 = time.time()
    s0 = 0.5 + 1j*g0 + eps
    A1 = logxi_deriv1(s0)
    num = float(mp.re(A1)*eps)
    S = interference_S(g0, eps)
    pred = 1 + S
    dt = time.time() - t0
    print(f"{k+1:>5} {g0:>10.2f} {num:>15.6f} {pred:>13.6f} {num-pred:>10.2e}  ({dt:.1f}s)")
