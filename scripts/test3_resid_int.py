#!/usr/bin/env python3
"""Test 3: 残差积分 R_M(T) = ∫(S̄_H - S_model)dt 的增长行为
O(1) / log / 随机游走（√N）——决定展开命题的可行性——
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

t0, t1 = 500.0, 60000.0
ds = 0.5
t_grid = np.arange(t0, t1, ds)
S_grid = np.array([S_at(t) for t in t_grid])

def Sbar_H(H):
    nH = max(1, int(round(H/ds)))
    kernel = np.ones(nH)/nH
    sb = np.convolve(S_grid, kernel, mode='valid')
    tb = t_grid[nH//2 : nH//2 + len(sb)]
    return tb, sb

primes_t = []
for n in range(2, 100):
    if all(n % p for p in primes_t if p*p <= n):
        primes_t.append(n)

print('=== Test 3: 残差积分增长 ===')
for H in [1.0, 2.0]:
    tb, sb = Sbar_H(H)
    T = tb[-1]
    # 模型（Bohr 系数——p≤97——）
    model = np.zeros(len(tb))
    for p in primes_t:
        a = np.trapz(sb * np.sin(tb*log(p)), tb)/T
        model += a * np.sin(tb*log(p))
    resid = sb - model
    # 残差积分（累积——）
    cumR = np.cumsum(resid) * ds
    # 增长分析——分段 max|cumR|
    print(f'\nH={H}: S̄ std={sb.std():.4f}——残差 std={resid.std():.4f}（占比 {resid.std()/max(sb.std(),1e-9):.2f}——）')
    print('  残差积分分段 max|∫R|（每 5000 点——）:')
    seg_max = []
    for i in range(0, len(cumR), 5000):
        seg = cumR[i:i+5000]
        seg_max.append(np.max(np.abs(seg)))
        if len(seg_max) <= 12:
            print(f'    到 t={tb[min(i+4999,len(tb)-1)]:.0f}: max|∫R|={np.max(np.abs(seg)):.3f}（当前 {cumR[min(i+4999,len(cumR)-1)]:+.3f}——）')
    print(f'  总 max|∫R| = {np.max(np.abs(cumR)):.3f}——末值 = {cumR[-1]:+.3f}')
    # 对比: 随机游走基线（残差 std × √N × ds 类——）
    rw = resid.std() * np.sqrt(len(resid)) * ds
    print(f'  随机游走基线 ≈ {rw:.1f}——比值 = {np.max(np.abs(cumR))/max(rw,1e-9):.4f}')
