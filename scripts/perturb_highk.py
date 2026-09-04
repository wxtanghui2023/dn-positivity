#!/usr/bin/env python3
# Perturbation test: high-order A_k expansion coefficients at gamma1, epsilon-scan.
# On-line prediction: A_k * eps^k = (-1)^(k+1)/k  (no flip for any eps>0)
# If off-axis delta>0: flip at eps=delta for ALL k consistently.
# Multi-k consistency probes the delta < eps_min blind region.
import numpy as np
import mpmath as mp
mp.mp.dps = 40

zeros = np.load('/tmp/zeros_odlyzko_100k.npy')
gamma1 = zeros[0]

def log_xi(s):
    """log xi(s) = log(1/2) + log s + log(s-1) - (s/2) log pi + log Gamma(s/2) + log zeta(s)"""
    return (mp.log(mp.mpf('0.5')) + mp.log(s) + mp.log(s-1)
            - (s/2)*mp.log(mp.pi) + mp.loggamma(s/2) + mp.log(mp.zeta(s)))

def A_k_num(k, s0):
    """A_k = (1/k!) d^k/dw^k log xi(s0+w)|_{w=0} via numerical differentiation"""
    f = lambda w: log_xi(s0 + w)
    return mp.diff(f, 0, k) / mp.factorial(k)

# scan eps for k=1,2,3,5; check A_k*eps^k vs (-1)^(k+1)/k
print(f"=== High-order A_k at gamma1={gamma1:.6f}, eps-scan ===")
print(f"on-line prediction: A_k*eps^k = (-1)^(k+1)/k")
eps_list = [0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001]
for k in [1, 2, 3, 5]:
    pred = (-1)**(k+1)/k
    print(f"\n  k={k}: predicted A_k*eps^k = {pred:+.4f}")
    flip = None
    for eps in eps_list:
        s0 = 0.5 + 1j*gamma1 + eps
        try:
            Ak = A_k_num(k, s0)
            val = float(mp.re(Ak) * eps**k)
            # on-line: value should approach pred as eps->0; off-axis delta: deviates & flips
            dev = abs(val - pred)
            flag = ""
            if k % 2 == 1 and val < 0 and flip is None:  # odd k: on-line positive
                flip = eps
                flag = "  <-- FLIP?"
            if eps <= 0.01:
                print(f"    eps={eps:.5f}: Re(A_k)*eps^k = {val:+.6f}  (dev={dev:.1e}){flag}")
        except Exception as e:
            print(f"    eps={eps}: error {e}")
            break
    if flip:
        print(f"  !! flip detected at eps={flip}")
    else:
        print(f"  no flip down to eps={eps_list[-1]}")
