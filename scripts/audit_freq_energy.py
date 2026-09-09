#!/usr/bin/env python3
"""Prime Frequency Energy Lemma 审计（NS 启发——能量 vs 点态——）
F(t) = Σ_p e^{it log p}/(√p log p)（S 的展开系数——）
E(H) = (1/H)∫_0^H |F(t)|²dt——对角（Σa_p²）vs 交叉（频率间隙——）
"""
import numpy as np
from math import log, pi

# 素数到 1e6
primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
ps = primes[primes < 1000000]
a_p = 1.0/(np.sqrt(ps)*np.log(ps))  # 系数

print('=== Prime Frequency Energy 审计 ===')
print(f'素数到 {ps[-1]}——{len(ps)} 个')

# 1. 对角项 Σa_p²
diag = np.sum(a_p**2)
print(f'\n对角 Σa_p² = {diag:.6f}（收敛？——Σ1/(p log²p)——）')

# 2. 交叉项（频率间隙——）Σ_{p≠q} a_p a_q / |log p - log q|
# 数值（分块——全对 ~5e10 太大——用采样/近似——）
# 先算"主要交叉"（邻近的 p,q——）——1/|log(p/q)| 大当 p~q——
# 分块估计：对每个 p——邻近的 q（|p-q| 小——）贡献大——
print('\n交叉项结构（邻近素数主导?——）:')
# 对几个 p——看 Σ_q a_p a_q/|log p - log q| 的（邻近 vs 远处——）
for p_test in [2, 100, 1000, 10000]:
    idx = np.searchsorted(ps, p_test)
    if idx >= len(ps): continue
    # 邻近 ±50
    lo, hi = max(0, idx-50), min(len(ps), idx+51)
    near_sum = 0
    for j in range(lo, hi):
        if j == idx: continue
        q = ps[j]
        near_sum += a_p[idx]*a_p[j]/abs(log(p_test)-log(q))
    # 远处（全部——采样——）
    far_sum = 0
    step = max(1, len(ps)//2000)
    for j in range(0, len(ps), step):
        if abs(j-idx) <= 50: continue
        q = ps[j]
        far_sum += a_p[idx]*a_p[j]/abs(log(p_test)-log(q)) * step  # 粗估计
    print(f'  p={p_test}: 邻近(±50)交叉={near_sum:.6f}——远处(采样)≈{far_sum:.6f}')

# 3. 能量积分的直接数值（F(t) 在 t 网格——）
print('\nE(H) = (1/H)∫|F(t)|²dt 数值:')
# F(t) 用素数到 1e5（截断——够——a_p 衰减——）
ps2 = ps[ps < 100000]
a2 = 1.0/(np.sqrt(ps2)*np.log(ps2))
t_grid = np.linspace(100, 20000, 20000)
# 分块算 F（省内存——）
F_vals = np.zeros(len(t_grid))
for i, t in enumerate(t_grid):
    F_vals[i] = np.sum(a2 * np.exp(1j*t*np.log(ps2))).real  # Re F——(1/H)∫|F|² = Σa_p² + 交叉——直接看 |F|² 平均
# |F|² 的平均（= E——）
E_est = np.mean(F_vals**2)
print(f'E ≈ (1/H)∫(Re F)² = {E_est:.6f}——对角 Σa_p²(截断) = {np.sum(a2**2):.6f}')
print(f'交叉贡献 ≈ {E_est - np.sum(a2**2):+.6f}（~0 = 对角主导——）')

# 4. 频率间隙的分布（非共振性——）
print('\n频率间隙 log(p/q) 分布（邻近素数——）:')
gaps = np.diff(np.log(ps2))
print(f'  log p 的最小相邻间隙: {gaps.min():.6f}（p 大——间隙 ~1/p——）')
print(f'  平均间隙: {gaps.mean():.6f}（~1/p 类——）')
# Σ_{q≠p} 1/|log p - log q| 的（对固定 p——）——收敛?
# 1/|log(p/q)| ~ p/|p-q|（p~q——）——Σ_q p/|p-q| ~ p·Σ 1/|p-q| ~ p·log（发散——）?
# 但加权 a_p a_q ~ 1/(√p√q log p log q)~1/(p log²p)——总 ~ Σ 1/(p log²p)·p/|p-q| 类——
# 用 p=10000 的实际和估计
p_ref = 10000
idx = np.searchsorted(ps2, p_ref)
s = 0
for j in range(len(ps2)):
    if j == idx: continue
    q = ps2[j]
    s += a2[idx]*a2[j]/abs(log(p_ref)-log(q))
print(f'  p={p_ref} 的全交叉和 ≈ {s:.6f}（>1 = 交叉主导?——）')
