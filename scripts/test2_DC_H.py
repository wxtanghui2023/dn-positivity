#!/usr/bin/env python3
"""Test 2: DC(H) 随 H 的变化——M_H(T) 的常数项 vs Σ ŵ_H(log p)/(√p log²p)
M_H(T) = ∫S̄_H——DC(H) = 徘徊中心——随 H 变?
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

t0, t1 = 200.0, 60000.0
ds = 0.2
t_grid = np.arange(t0, t1, ds)
S_grid = np.array([S_at(t) for t in t_grid])

def Sbar_H(H):
    nH = max(1, int(round(H/ds)))
    kernel = np.ones(nH)/nH
    sb = np.convolve(S_grid, kernel, mode='valid')
    tb = t_grid[nH//2 : nH//2 + len(sb)]
    return tb, sb

# 对每个 H——算 M_H(T) = ∫Sbar_H dt（累积——）——找 DC（徘徊中心——末段平均——）
print('=== Test 2: DC(H) 随 H ===')
for H in [0.5, 1.0, 2.0, 4.0, 8.0, 16.0]:
    tb, sb = Sbar_H(H)
    # M_H = ∫Sbar dt（累积——）
    M_H = np.cumsum(sb) * ds  # 均匀网格——∫ ≈ Σ sb·ds
    # DC（末 20% 的平均——徘徊中心——）
    n_last = int(len(M_H)*0.2)
    dc = np.mean(M_H[-n_last:])
    # 范围
    print(f'H={H:5.1f}: S̄ std={sb.std():.4f}——M_H DC={dc:+.4f}——max|M_H|={np.max(np.abs(M_H)):.3f}')

# 理论预测: DC(H) = Σ_p ŵ_H(log p)·c_p——c_p 从 H 小的拟合（a_p ~ -0.155/√p·ŵ——）
# DC(H) = Σ a_p(H)/log p——如果 a_p(H) = a_p(0)·ŵ_H(log p)——a_p(0) ~ -0.155/√p
# 但需要全 p——先看 DC(H)/DC(0.5) 的比值（相对变化——）
print()
print('相对 DC:')
dc_vals = {}
for H in [0.5, 1.0, 2.0, 4.0, 8.0, 16.0]:
    tb, sb = Sbar_H(H)
    M_H = np.cumsum(sb) * ds
    n_last = int(len(M_H)*0.2)
    dc_vals[H] = np.mean(M_H[-n_last:])
dc0 = dc_vals[0.5]
for H in [1.0, 2.0, 4.0, 8.0, 16.0]:
    print(f'  DC({H})/DC(0.5) = {dc_vals[H]/dc0:.4f}')
