#!/usr/bin/env python3
"""M 能量交叉项收敛性（死亡测试——）
∫|M(T)|² dT 展开——交叉项 ~ Σ_{p≠q} a_pa_q/(log p log q · |log p−log q|)
——邻近素数（|log p−log q| 小——）主导——收敛 or 发散?
"""
import numpy as np
from math import log, pi

primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')

print('=== M 能量交叉项收敛性（死亡测试——）===')
print('交叉项 C = Σ_{p≠q} a_p a_q / (log p log q · |log p - log q|)')
print('a_p = 1/(√p log p)——理论——')

# 分块计算（全对太大——）——用"每 p 的邻近贡献"（主导——）
# 邻近：1/|log(p/q)| ~ p/|p-q|（p~q——）——贡献 ~ 1/(p log³p)·p/|p-q| = 1/(log³p·|p-q|)
# Σ_q 1/|p-q|（q 素数邻近——）~ 2·(1/gap_1 + 1/gap_2 + ...)——素数 gap 平均 log p——
# 粗估计: Σ_{q≠p} 1/|p-q| ~ 2·Σ_{gaps} 1/gap ~ 发散（Σ 1/(k log p) ~ log log——）
# 精确数值（分块——）

def cross_for_p(p_idx, ps, a_p, window=2000):
    """p 与所有 q 的交叉（用窗口 + 远处粗估——）"""
    p = ps[p_idx]
    total = 0.0
    # 邻近（窗口——精确——）
    lo, hi = max(0, p_idx-window), min(len(ps), p_idx+window+1)
    for j in range(lo, hi):
        if j == p_idx: continue
        q = ps[j]
        total += a_p[p_idx]*a_p[j]/(log(p)*log(q)*abs(log(p)-log(q)))
    # 远处（|log p - log q| 大——贡献 ~ a_p a_q/(log p log q · log(p/q))——小——粗估——）
    # 远处总和 ~ Σ_q 1/(√p√q log³p · log(p/q))——q 积分 ~ 收敛（log(p/q) 分母——）
    return total

# 数值：分块算总交叉（到 p ≤ 1e5——窗口全——）——邻近主导——
ps_use = primes[primes <= 100000]
a_p = 1.0/(np.sqrt(ps_use)*np.log(ps_use))
N = len(ps_use)
print(f'素数到 1e5——{N} 个')

# 每 p 的交叉（全对——N²~2.5e7——可行但慢——用邻近精确 + 远处采样）
total_cross = 0.0
for i in range(N):
    # 邻近 ±500 精确
    lo, hi = max(0, i-500), min(N, i+501)
    for j in range(lo, hi):
        if j == i: continue
        total_cross += a_p[i]*a_p[j]/(log(ps_use[i])*log(ps_use[j])*abs(log(ps_use[i])-log(ps_use[j])))
    # 远处（采样估计——每 100 个——）
    if i % 100 == 0:
        for j in range(0, N, 100):
            if abs(j-i) <= 500: continue
            total_cross += a_p[i]*a_p[j]/(log(ps_use[i])*log(ps_use[j])*abs(log(ps_use[i])-log(ps_use[j]))) * 100
    if i % 5000 == 0:
        print(f'  i={i} (p={ps_use[i]}): 累计交叉 ≈ {total_cross:.4f}')

print(f'\n总交叉（到 p≤1e5——邻近精确+远处采样——）≈ {total_cross:.4f}')

# 收敛性诊断——分块看增长
print('\n分块交叉（每 5000 个 p——增长?——）:')
for i0 in range(0, N, 5000):
    block = 0.0
    for i in range(i0, min(i0+5000, N)):
        lo, hi = max(0, i-500), min(N, i+501)
        for j in range(lo, hi):
            if j == i: continue
            block += a_p[i]*a_p[j]/(log(ps_use[i])*log(ps_use[j])*abs(log(ps_use[i])-log(ps_use[j])))
    print(f'  p∈[{ps_use[i0]},{ps_use[min(i0+4999,N-1)]}]: 块交叉 ≈ {block:.4f}')
