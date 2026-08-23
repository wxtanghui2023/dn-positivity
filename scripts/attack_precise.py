#!/usr/bin/env python3
"""高精度验证攻击点：
1. I_p(n=500) 的真实量级（高精度积分——消除伪影）
2. ∫f_n·S·g 直接数值（用 S_k 实际值——分段——目标 O(1)）
"""
import numpy as np
import gc
from math import log, pi
from scipy.integrate import quad

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(300000)
T = z[-1]

def th1(t):
    return np.arctan(1/(2*t))
def g(t):
    return 2*pi/(t*np.log(t/(2*pi))**2)
def f_n(t, n):
    return 4*np.sin(n*np.arctan(1/(2*t)))**2

# 1. 高精度 I_p(n=500)——分块积分（f_n 振荡快——分小区间）
def quad_precise(f, a, b, nsub=50):
    """分块积分——每块高斯——提高精度"""
    from numpy.polynomial.legendre import leggauss
    xg, wg = leggauss(16)
    total = 0.0
    for i in range(nsub):
        lo = a + (b-a)*i/nsub
        hi = a + (b-a)*(i+1)/nsub
        ts = 0.5*(hi-lo)*xg + 0.5*(hi+lo)
        total += 0.5*(hi-lo)*np.sum(wg*f(ts))
    return total

print("高精度 I_p(n)——分块高斯（16 点 × 50 块）：")
for p in [2, 3, 5]:
    for n in [10, 100, 500]:
        val = quad_precise(lambda t: f_n(t, n)*np.sin(t*log(p))*g(t), z[0], T)
        print(f"  p={p:3d} n={n:4d}: I_p = {val:+.6f}")

# 2. ∫f_n·S·g 直接（S_k 分段——S(t) = k − N₀(t) 在 [γ_k, γ_{k+1})）
def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

print("\n∫f_n·S·g 直接数值（S_k 分段——目标 O(1)）：")
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
for n in [10, 50, 100, 200, 500]:
    total = 0.0
    step = 10000  # 每 1 万零点一块（S 分段）
    for k0 in range(0, len(z)-1, step):
        k1 = min(k0+step, len(z)-1)
        for k in range(k0, k1):
            a, b = z[k], z[k+1]
            if b - a < 1e-10: continue
            ts = 0.5*(b-a)*xg + 0.5*(a+b)
            S_vals = (k+1) - N0(ts)
            fg = f_n(ts, n)*g(ts)
            total += 0.5*(b-a)*np.sum(wg*S_vals*fg)
    print(f"  n={n:4d}: ∫f_n·S·g = {total:+.6f}")

del z
gc.collect()
print("内存已释放")
