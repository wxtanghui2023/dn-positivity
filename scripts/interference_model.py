#!/usr/bin/env python3
# Verify interference model: Re(A1)*eps = 1 + eps^2 * sum_{j!=0} 1/(eps^2 + (gamma_j-gamma_0)^2)
# If deviation is pure interference (all zeros on-line), prediction should match numerics.
import numpy as np
import mpmath as mp
mp.mp.dps = 30

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')

def logxi_deriv1(s):
    return (1/s + 1/(s-1) - 0.5*mp.log(mp.pi)
            + 0.5*mp.digamma(s/2) + mp.zeta(s, derivative=1)/mp.zeta(s))

# sample zeros
ks = [0, 9, 49, 99, 199, 349, 499]
eps = 0.01
print(f"{'k':>4} {'gamma0':>9} {'num ReA1*eps':>13} {'pred 1+S':>13} {'diff':>10} {'S':>10}")
for k in ks:
    g0 = zeros[k]
    # interference sum over all other zeros in our data (100k, gamma up to ~10^5)
    dg = np.abs(zeros - g0)
    dg = dg[dg > 1e-6]  # exclude self
    S = eps**2 * np.sum(1.0/(eps**2 + dg**2))
    pred = 1 + S
    s0 = 0.5 + 1j*g0 + eps
    A1 = logxi_deriv1(s0)
    num = float(mp.re(A1)*eps)
    print(f"{k+1:>4} {g0:>9.3f} {num:>13.6f} {pred:>13.6f} {num-pred:>10.2e} {S:>10.6f}")
