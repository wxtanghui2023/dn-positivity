#!/usr/bin/env python3
"""K_p 的非乘性全局化测试：素数态重叠矩阵
M_{pq}(s) = ⟨ψ_{p,s}, ψ_{q,1-s̄}⟩
  = √((1-p^{-2σ})(1-q^{-2+2σ})) / (1 - p^{-σ}q^{-(1-σ)}(p/q)^{it})
对角 = κ_p（纯 σ——）非对角含跨素数相位 (p/q)^{it}
问题：det M_N(s) 是否有非平凡（离散——）零点结构？
——非乘性全局化（矩阵 det ≠ ∏ 或 Σ——）——
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

def M_pq(p, q, sigma, t):
    """M_{pq}(s)——复——"""
    # 对角: κ_p（纯 σ——）
    if p == q:
        a = p**(-2*sigma)
        b = p**(-2+2*sigma)
        return sqrt((1-a)*(1-b))/(1-1.0/p)
    # 非对角: 交叉（含 (p/q)^{it}——）
    lp = log(p); lq = log(q)
    phase = np.exp(1j*t*(lp - lq))  # (p/q)^{it}
    denom = 1 - p**(-sigma)*q**(-(1-sigma))*phase
    num = sqrt((1-p**(-2*sigma))*(1-q**(-2+2*sigma)))
    return num/denom

def det_MN(primes, sigma, t):
    N = len(primes)
    M = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            M[i,j] = M_pq(primes[i], primes[j], sigma, t)
    return np.linalg.det(M)

pr = primes_below(200)  # 前 46 个素数
print(f'素数数: {len(pr)}——前 10: {pr[:10]}')

# 1. |det| 的 σ-t 行为（找零点结构——）
print()
print('=== |det M_N(s)| 扫描（N=30——）===')
pr30 = pr[:30]
for sigma in [0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]:
    row = []
    for t in [0, 5, 10, 14.13, 20, 25, 30]:
        d = det_MN(pr30, sigma, t)
        row.append(f'{abs(d):.2e}')
    print(f'  σ={sigma}: ' + ' | '.join(row))

# 2. σ=0.5 全线是否 det=0？（像 κ 的区域——还是非零——）
print()
print('=== σ=½ 的 det（t 扫描——）= 0 吗？===')
for t in [0, 3, 7, 14.13, 21.02, 30]:
    d = det_MN(pr30, 0.5, t)
    print(f'  t={t}: |det| = {abs(d):.3e}——arg = {np.angle(d):.4f}')

# 3. det 的零点搜索（σ-t 平面——）
print()
print('=== |det| 极小搜索（找离散零点——）===')
# 粗扫 σ∈[0.1,0.9], t∈[5,40]
mins = []
for sigma in np.linspace(0.1, 0.9, 17):
    for t in np.linspace(5, 40, 36):
        d = abs(det_MN(pr20 if False else pr30, sigma, t))
        mins.append((d, sigma, t))
mins.sort()
print('  最小的 10 个 |det|:')
for d, s, t in mins[:10]:
    print(f'    |det|={d:.3e} at σ={s:.3f}, t={t:.2f}')

# 4. 与 ζ 零点的关系（t=14.13, 21.02, 25.01——零点高度——）
print()
print('=== |det| 在 ζ 零点高度 vs 非零点高度 ===')
for t in [10.0, 14.13, 15.0, 20.0, 21.02, 25.0, 25.01, 30.0]:
    d = det_MN(pr30, 0.5, t)
    print(f'  t={t}: |det(σ=0.5)| = {abs(d):.3e}')
