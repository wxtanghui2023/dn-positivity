#!/usr/bin/env python3
"""相位均匀性 P_N = Σ[S(γ_k)-½] 与 Σδ_k 的关系
δ_k = Δγ_k - 1/N0'(γ_k)——Σδ = O(1)（8/23 无条件——）
S(γ_k) 与 δ 的关系：S(γ_k) = N(γ_k) - N0(γ_k)——δ = Δγ - 1/N0'
——如果 P_N 能从 δ（或 N0' 的——）表达——可能无条件——
"""
import numpy as np
from math import log, pi

# 2M 零点（长——确认 P_N 的 O(1)——）
z = np.load('data/zeros_odlyzko_2M.npy')
K = min(len(z), 500000)
z = z[:K]
print(f'零点: {K}——γ到 {z[-1]:.0f}')

dg = np.diff(z)
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

# S(γ_k) 右极限 = k - N0(γ_k)——（k = 第 k 个零点——z[k-1]——）
N0v = np.array([N0(t) for t in z[:-1]])
kk = np.arange(1, K)
S_right = kk - N0v  # S(γ_k+)——但需要仔细（N(γ_k+) = k——）

# 相位均匀性 P_N = Σ_{k<=N}[S(γ_k) - 1/2]
P_cum = np.cumsum(S_right - 0.5)

# δ_k = Δγ_k - 1/N0'(γ_k)——N0'(t) = (1/2π)log(t/2π)
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0p
D_cum = np.cumsum(delta)

print('\n=== 相位均匀性 P_N vs Σδ ===')
print(f'P_N（Σ[S-½]——）: 末值={P_cum[-1]:+.3f}——max|={np.max(np.abs(P_cum)):.3f}')
print(f'Σδ: 末值={D_cum[-1]:+.3f}——max|={np.max(np.abs(D_cum)):.3f}')

# 分段——看两者的行为
print('\n分段（每 5 万零点——）:')
for i in range(0, K-1, 50000):
    print(f'  到零点{i+50000 if i+50000<K else K-1}: P_N={P_cum[min(i+49999,K-2)]:+.3f}——Σδ={D_cum[min(i+49999,K-2)]:+.3f}')

# 相关（增量——）
dP = np.diff(P_cum[::10])  # 每 10 个采样
dD = np.diff(D_cum[::10])
c = np.corrcoef(dP, dD)[0,1]
print(f'\n增量相关（ΔP vs Δδ——）: {c:+.4f}')

# S(γ_k) 与 δ 的关系——S 的差分 vs δ
# S(γ_{k+1}) - S(γ_k) = 1 - [N0(γ_{k+1}) - N0(γ_k)] ≈ 1 - N0'(γ_k)·Δγ_k = -N0'(γ_k)·δ_k?? 
# 1 - N0'Δγ = -(N0'Δγ - 1) = -N0'·δ?  δ = Δγ - 1/N0'——N0'δ = N0'Δγ - 1——1 - N0'Δγ = -N0'δ
# 所以 ΔS_k = 1 - N0'(γ_k)Δγ_k = -N0'(γ_k)·δ_k（精确到二阶——）
dS = np.diff(S_right)
pred = -N0p[:-1] * delta[:-1]
print('\nΔS vs -N0\'·δ 检验（S 的差分 = 间距偏差的——）:')
c2 = np.corrcoef(dS, pred)[0,1]
print(f'  相关: {c2:.6f}（~1 = 精确关系——）')
print(f'  残差 std: {(dS - pred).std():.6f}（vs ΔS std {dS.std():.6f}——）')
