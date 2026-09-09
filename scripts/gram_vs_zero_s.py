#!/usr/bin/env python3
"""Arithmetic generator 弱形式测试第一步:
S(t) 在三种采样下的分布——零点 γ_k / Gram 点 g_k（纯 N₀——）/ 随机 t
如果 S(γ_k) 与 S(g_k) 同分布（弱——）——"弱增长"是 N₀/Gram 的（非零点特有——）
如果 S(γ_k) 特殊（更弱——）——零点采样有独立压制——
"""
import numpy as np
from math import log, pi, sqrt
z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = 400000
z = z[:K]

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi))-1)+7.0/8
def N0_inv(n):
    """N0(t) = n 的 t（牛顿——）"""
    t = 2*pi*n/log(max(n, 10))  # 初值
    for _ in range(20):
        t = t - (N0(t) - n)/(log(t/(2*pi))/(2*pi))
    return t

# 1. S(γ_k)（零点采样——）
N0v_g = np.array([N0(t) for t in z[:K-1]])
S_gamma = np.arange(1, K) - N0v_g  # S(γ_k+)（mean ~0.5——）
# 去 mean（用已知的 +0.5 偏置——右极限——）
S_gamma_c = S_gamma - 0.5

# 2. S(g_k)（Gram 点采样——纯 N₀——）g_k = N0^{-1}(k)
from bisect import bisect_right
ks = np.arange(1000, K, 7)  # 采样 Gram 点（每 7 个——）
S_gram = []
for k in ks:
    gk = N0_inv(k)
    Nk = bisect_right(z, gk)
    S_gram.append(Nk - k)
S_gram = np.array(S_gram)

# 3. S(t) 随机（同范围——）
rng = np.random.default_rng(1)
t_rand = np.exp(rng.uniform(log(100), log(z[K-1]), len(ks)))
S_rand = np.array([bisect_right(z, t) - N0(t) for t in t_rand])

print('=== S 的三种采样分布 ===')
# 分段（按 k/t 范围——看增长——）
def seg_stats(vals, labels, nbins=3):
    n = len(vals)
    for i in range(nbins):
        sl = slice(i*n//nbins, (i+1)*n//nbins)
        print(f'  {labels} 段{i}: std={vals[sl].std():.4f}')

print('S(γ_k)−½（零点——）:')
seg_stats(S_gamma_c, '零点')
print('S(g_k)（Gram 点——）:')
seg_stats(S_gram, 'Gram')
print('S(t)（随机——）:')
seg_stats(S_rand, '随机')

print()
print(f'总 std: 零点 {S_gamma_c.std():.4f}——Gram {S_gram.std():.4f}——随机 {S_rand.std():.4f}')
# Gram 定律检查（S(g_k) 的符号 vs Z 的——不直接——跳过——）
# 关键: Gram 点 S 是否也弱（~0.3-0.4——）vs 随机（~0.43 增长——）
