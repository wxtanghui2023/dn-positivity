#!/usr/bin/env python3
# Push asymptotic matching to the data limit (gamma up to ~75000).
import numpy as np
import mpmath as mp
import time
mp.mp.dps = 30

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')

def logxi_deriv1(s):
    return (1/s + 1/(s-1) - 0.5*mp.log(mp.pi)
            + 0.5*mp.digamma(s/2) + mp.zeta(s, derivative=1)/mp.zeta(s))

def interference_S(g0, eps):
    dg = np.abs(zeros - g0)
    dg = dg[dg > 1e-6]
    return eps**2 * np.sum(1.0/(eps**2 + dg**2))

ks = [5000, 10000, 15000, 20000, 30000, 40000, 60000, 80000, 99000]
eps = 0.01
print(f"{'k':>6} {'gamma0':>10} {'ReA1*eps':>13} {'1+S':>13} {'diff':>10}  time")
for k in ks:
    if k >= len(zeros):
        continue
    g0 = zeros[k]
    t0 = time.time()
    s0 = 0.5 + 1j*g0 + eps
    A1 = logxi_deriv1(s0)
    num = float(mp.re(A1)*eps)
    S = interference_S(g0, eps)
    pred = 1 + S
    dt = time.time() - t0
    print(f"{k+1:>6} {g0:>10.2f} {num:>13.6f} {pred:>13.6f} {num-pred:>10.2e}  {dt:.1f}s")
