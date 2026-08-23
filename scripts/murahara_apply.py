#!/usr/bin/env python3
"""Murahara 界应用到我们的加权 Weyl 和（f(γ) = nθ₁(γ)/π）
D = O(1/H) + O(1/(T|f'(T)|)) + O(log H/T) + O(H|f(T)|/T)
验证各成分量级 + 实际 discrepancy——能否给加权 Weyl 和有界？
"""
import numpy as np
import gc
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)
T = z[-1]
print(f"T = γ_max = {T:.1f}")

# f(γ) = n·θ₁(γ)/π——θ₁ = arctan(1/2t)——f'(t) = n·θ₁'/π
# θ₁'(t) = d/dt arctan(1/2t) = −1/(2t²)·(1/(1+1/4t²)) = −2/(4t²+1)
def f_prime(t, n):
    return n * (-2/(4*t*t + 1)) / pi

# Murahara 界成分
print("\nMurahara 界成分（f = nθ₁/π）：")
for n in [100, 500, 1000, 3000]:
    fp = abs(f_prime(T, n))
    fT = n * np.arctan(1/(2*T)) / pi
    print(f"\n  n={n}: |f'(T)| = {fp:.6e}  f(T) = {fT:.6e}")
    for H in [1, 10, 100, 1000]:
        term1 = 1/H
        term2 = 1/(T*fp)
        term3 = log(H)/T
        term4 = H*abs(fT)/T
        D_bound = term1 + term2 + term3 + term4
        print(f"    H={H:5d}: 1/H={term1:.4f}  1/(T|f'|)={term2:.4f}  logH/T={term3:.6f}  H|f|/T={term4:.6e}  D_bound={D_bound:.4f}")

# 实际 discrepancy（我们的相位序列）
print("\n实际 discrepancy D_N（相位 {nθ₁(γ)/π}）：")
for n in [100, 500, 1000]:
    th1 = np.arctan(1/(2*z))
    phase = np.mod(n*th1/pi, 1.0)
    # D*（星偏差——排序）
    sorted_p = np.sort(phase)
    Dstar = np.max(np.abs(sorted_p - np.arange(len(sorted_p))/len(sorted_p)))
    print(f"  n={n}: D* = {Dstar:.4f}")

# 加权 Weyl 和（我们的目标）
print("\n加权 Weyl 和（Σe^{i·2nθ₁(γ)}——r(n) 的核）：")
for n in [100, 500, 1000]:
    th1 = np.arctan(1/(2*z))
    W = np.sum(np.exp(1j*2*n*th1))
    print(f"  n={n}: |Σe^{{i·2nθ₁}}| = {abs(W):.4f}（O(1) = 有界目标）")

del z
gc.collect()
print("内存已释放")
