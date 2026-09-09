#!/usr/bin/env python3
"""Weighted δ 测试第 4 步: 对照已知 S(T) 界（Selberg——）
S(T)（时间——）~ 正态(0, √(½ log log T))（Selberg 1946——）
S(γ_k)（零点采样——）的统计（mean 0.5——std ?——）
——P_N = Σ(S(γ_k)−½) 的 O(1)——是否 = 已知 S(T) 理论的离散版（退化——）
   还是零点采样的新效应（存活——）
"""
import numpy as np
from math import log, pi, sqrt

z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = min(len(z), 500000)
z = z[:K]

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
S_z = np.arange(1, K) - N0v  # S(γ_k+) 零点采样

print('=== S(γ_k)（零点采样）的统计 ===')
print(f'S(γ_k): mean={S_z.mean():+.4f}——std={S_z.std():.4f}')
# Selberg: S(T)（时间——）std ~ √(½ log log T)
g = z[-1]
selberg_std = sqrt(0.5*log(log(g)))
print(f'Selberg（时间——T={g:.0f}）: std ~ √(½log log T) = {selberg_std:.3f}')
print(f'比值 采样std/Selberg std = {S_z.std()/selberg_std:.3f}')

# S(γ_k) 的自相关（相消结构——）
print()
print('S(γ_k)−½ 的自相关（相消——）:')
dS = S_z - 0.5
for lag in [1, 2, 3, 5, 10]:
    c = np.corrcoef(dS[:-lag], dS[lag:])[0,1]
    print(f'  ρ({lag}) = {c:+.4f}')

# P_N 的累积（Σ dS——）——O(1)?
P_N = np.cumsum(dS)
print(f'\nP_N: 末值={P_N[-1]:+.3f}——max|={np.max(np.abs(P_N)):.3f}')
# 对比随机游走（dS 独立——√N·std——）
rw = np.sqrt(len(dS))*dS.std()
print(f'随机游走基线（√N·std）= {rw:.1f}——P_N/基线 = {np.max(np.abs(P_N))/rw:.5f}')
# 对比 Σρ（方差压缩——）: Var(P_N) ~ N·std²·(1+2Σρ)
rho_sum = sum(np.corrcoef(dS[:-lag], dS[lag:])[0,1] for lag in range(1, 200))
print(f'1+2Σρ(lag<200) = {1+2*rho_sum:.3f}（~0 = 强相消——方差压缩——）')

# S(T)（时间——）的采样对照（随机 T——）
print()
print('S(T)（随机时间采样——）的统计（对照——）:')
rng = np.random.default_rng(42)
t_rand = rng.uniform(1000, z[-1], 100000)
from bisect import bisect_right
S_rand = np.array([bisect_right(z, t) - N0(t) for t in t_rand])
print(f'S(T)（随机 T——）: mean={S_rand.mean():+.4f}——std={S_rand.std():.4f}')
print(f'  （Selberg 预期 std ~{selberg_std:.3f}——）')
