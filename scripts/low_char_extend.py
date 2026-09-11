#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# Extend characteristic-quantity A1 analysis to higher zeros.
# Question: does Re(A1)*eps stay ~1.0000 (on-line signature) as gamma grows?
# Deviation |1 - Re(A1)*eps| measures interference from neighboring zeros.
import numpy as np
import mpmath as mp
mp.mp.dps = 30

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')

def logxi_deriv1(s):
    return (1/s + 1/(s-1) - 0.5*mp.log(mp.pi)
            + 0.5*mp.digamma(s/2) + mp.zeta(s, derivative=1)/mp.zeta(s))

# Sample zeros at increasing heights: k = 1,2,..., every 10th up to 600
ks = list(range(0, 60)) + list(range(60, 600, 10))
eps = 0.01
print(f"{'k':>4} {'gamma_k':>10} {'Re(A1)*eps':>12} {'dev|1-..|':>10} {'Im(A1)*eps':>11}")
devs = []
for k in ks:
    gamma = zeros[k]
    s0 = 0.5 + 1j*gamma + eps
    A1 = logxi_deriv1(s0)
    a1e = float(mp.re(A1)*eps)
    a1i = float(mp.im(A1)*eps)
    dev = abs(1 - a1e)
    devs.append((gamma, dev, a1e))
    if k < 60 or dev > 1e-3:
        print(f"{k+1:>4} {gamma:>10.4f} {a1e:>12.6f} {dev:>10.2e} {a1i:>11.4f}")

print(f"\n=== Deviation summary ===")
devs = np.array(devs)
print(f"samples: {len(devs)}, gamma range: {devs[0,0]:.1f} .. {devs[-1,0]:.1f}")
print(f"max dev |1-ReA1*eps|: {devs[:,1].max():.3e} at gamma={devs[devs[:,1].argmax(),0]:.1f}")
print(f"mean dev: {devs[:,1].mean():.3e}")
# does dev grow with gamma?
g = devs[:,0]; d = devs[:,1]
# correlation of log dev vs log gamma
mask = d > 0
if mask.sum() > 10:
    slope = np.polyfit(np.log(g[mask]), np.log(d[mask]), 1)[0]
    print(f"log dev vs log gamma slope: {slope:.2f} (0=constant, >0=grows with height)")
