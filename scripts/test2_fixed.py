#!/usr/bin/env python3
"""Test 2 修正: 用 Bohr 系数算模型 DC(H) = Σa_p(H)/log p
验证: a_p(H) ~ ŵ_H(log p) 的系数——DC_model(H) 随 H 的变化——
对比 M 的真实 DC（0.6——）——残差 DC 补差——
"""
import numpy as np
from math import log, pi
from bisect import bisect_right

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

def N0(t):
    if t <= 1: return 0.0
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

def S_at(u):
    k = bisect_right(z, u)
    return k - N0(u)

# 均匀网格 S
t0, t1 = 500.0, 60000.0
ds = 0.5  # 粗一点（省时间——Test 1 的细网格已验——）
t_grid = np.arange(t0, t1, ds)
S_grid = np.array([S_at(t) for t in t_grid])

def Sbar_H(H):
    nH = max(1, int(round(H/ds)))
    kernel = np.ones(nH)/nH
    sb = np.convolve(S_grid, kernel, mode='valid')
    tb = t_grid[nH//2 : nH//2 + len(sb)]
    return tb, sb

primes_t = []
for n in range(2, 200):
    if all(n % p for p in primes_t if p*p <= n):
        primes_t.append(n)

print('=== Test 2 修正: DC_model(H) = Σa_p(H)/log p ===')
print('M 的真实 DC ≈ 0.6（已知——）')
for H in [0.5, 1.0, 2.0, 4.0]:
    tb, sb = Sbar_H(H)
    T = tb[-1]
    dc_model = 0.0
    # Bohr 系数（多 p——到 100——）
    n_p = 0
    for p in primes_t:
        if p > 100: break
        a = np.trapz(sb * np.sin(tb*log(p)), tb)/T
        dc_model += a/log(p)
        n_p += 1
    # 尾估计（p>100——a_p ~ -0.155/√p·ŵ——粗略——）
    print(f'H={H:.1f}: DC_model(p≤100) = {dc_model:+.4f}——（p 数 {n_p}——）')

# M 的真实 DC（用零点公式——精确——）
def IntN0(t):
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
def M_zero(T):
    idx = bisect_right(z, T)
    return sum(T - g for g in z[:idx]) - IntN0(T)
# 在几个 T 的 M——DC 的估计（末段平均——）
Ts = np.linspace(30000, 60000, 50)
M_vals = [M_zero(t) for t in Ts]
print(f'\nM(零点公式) 末段: mean={np.mean(M_vals):+.3f}——范围 [{min(M_vals):+.2f}, {max(M_vals):+.2f}]')
