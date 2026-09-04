#!/usr/bin/env python3
# Extend high-order A_k perturbation test to first several low zeros.
# Multi-k consistency + multi-zero consistency: on-line signature at low region.
import numpy as np
import mpmath as mp
mp.mp.dps = 40

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')

def log_xi(s):
    return (mp.log(mp.mpf('0.5')) + mp.log(s) + mp.log(s-1)
            - (s/2)*mp.log(mp.pi) + mp.loggamma(s/2) + mp.log(mp.zeta(s)))

def A_k_num(k, s0):
    f = lambda w: log_xi(s0 + w)
    return mp.diff(f, 0, k) / mp.factorial(k)

eps_list = [0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001, 0.00005, 0.00002]
ks = [3, 5]
print(f"{'k':>2} {'zero':>3} {'gamma':>9} | " + "  ".join([f"eps={e:.0e}" for e in eps_list]))
for k in ks:
    pred = (-1)**(k+1)/k
    for zi in range(5):
        g0 = zeros[zi]
        row = []
        flip = None
        for eps in eps_list:
            s0 = 0.5 + 1j*g0 + eps
            try:
                Ak = A_k_num(k, s0)
                val = float(mp.re(Ak) * eps**k)
                dev = abs(val - pred)
                row.append(f"{dev:.0e}")
                if k % 2 == 1 and val < 0 and flip is None:
                    flip = eps
            except Exception as e:
                row.append("ERR")
        flag = f"  FLIP@{flip}" if flip else ""
        print(f"{k:>2} {zi+1:>3} {g0:>9.3f} | " + "  ".join(row) + flag)
