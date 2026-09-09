#!/usr/bin/env python3
"""Ŝ 元素零点结构测试：F_N(s) = Σ_{p≤N}(c_p(s) − 1)
c_p = √((1-p^{-2σ})(1-p^{-2+2σ}))/(1-p^{-1}e^{-2it·log p})
——测零点结构（σ-t 平面——）+ N 依赖（极限警告——）
"""
import numpy as np
from math import log, sqrt

def primes_below(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]

def c_p(p, sigma, t):
    lp = log(p)
    a = p**(-2*sigma)
    b = p**(-2+2*sigma)
    R = sqrt((1-a)*(1-b))
    denom = 1 - p**(-1)*np.exp(-2j*t*lp)
    return R/denom

def F_N(primes, sigma, t):
    return sum(c_p(p, sigma, t) - 1 for p in primes)

pr_all = primes_below(3000)

print('=== |F_N(s)| 的 σ-t 扫描（找零点结构——）===')
for N in [50, 100, 200]:
    pr = pr_all[:N]
    print(f'N={N}:')
    # 粗扫 |F| 极小
    mins = []
    for sigma in np.linspace(0.1, 0.9, 17):
        for t in np.linspace(2, 40, 39):
            v = abs(F_N(pr, sigma, t))
            mins.append((v, sigma, t))
    mins.sort()
    print(f'  最小 |F|: {mins[0][0]:.4f} at σ={mins[0][1]:.2f}, t={mins[0][2]:.1f}')
    # σ=0.5 扫描（零点在线上？）
    vals_half = [abs(F_N(pr, 0.5, t)) for t in np.linspace(2, 40, 39)]
    print(f'  σ=0.5 的 |F| 范围: [{min(vals_half):.4f}, {max(vals_half):.4f}]')

# N 依赖（零点是否漂移——极限现象——）
print()
print('=== F_N 在固定点的 N 依赖（收敛？）===')
for (sigma, t) in [(0.5, 14.13), (0.5, 21.02), (0.4, 14.13), (0.6, 14.13), (0.5, 10.0)]:
    vals = []
    for N in [10, 20, 50, 100, 200, 400]:
        v = F_N(pr_all[:N], sigma, t)
        vals.append(v)
    print(f'  (σ={sigma}, t={t}): F_N = {[f"{v:.4f}" for v in vals]}')

# 与 Euler 的关系（Σ(c_p−1) ~ log ζ(1+2it) 类？——）
print()
print('=== F 的 t 结构（Euler 频率检查——2t——）===')
# F_N(σ=0.5, t) vs t 的 FFT 主频（应 ~ log 2 的倍数（Euler——）还是别的——）
N = 200
pr = pr_all[:N]
ts = np.linspace(2, 60, 581)
vals = np.array([F_N(pr, 0.5, t) for t in ts])
# 与 e^{2it log2} 的相关（Euler p=2 频率——）
c2 = np.corrcoef(vals.real, np.cos(2*ts*log(2)))[0,1]
c1 = np.corrcoef(vals.real, np.cos(ts*log(2)))[0,1]
print(f'  F ~ cos(2t·log2)? corr={c2:+.3f}——~cos(t·log2)? corr={c1:+.3f}')
