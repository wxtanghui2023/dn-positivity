#!/usr/bin/env python3
"""追 dS_k 的 ρ 来源（P_N 存活的最后判定——）
dS_k = S_{k+1} - S_k = 1 - ΔN₀(k)——ΔN₀ = N₀(γ_{k+1}) - N₀(γ_k)
1+2Σρ(dS) ≈ 0（方差压缩——）——ρ 的来源：
(a) 无条件（从 ΔN₀ 的定义/零点计数的——）
(b) GUE/Montgomery 对关联（条件——退化——）
检验: ρ(lag) 的衰减结构 vs 理论预测——
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = min(len(z), 500000)
z = z[:K]

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
S_z = np.arange(1, K) - N0v
dS = np.diff(S_z)

print('=== dS 的来源分析 ===')
print(f'dS: mean={dS.mean():+.5f}——std={dS.std():.4f}')
# dS = 1 - ΔN0——ΔN0 = N0(γ_{k+1})-N0(γ_k)
dN0 = np.diff(N0v)
print(f'1-ΔN0: mean={(1-dN0).mean():+.5f}——与 dS 差: {(dS-(1-dN0)).std():.2e}')
# dS = 1 - ΔN0 精确?——ΔN0 用 N0 在零点的差——dS_k = S_{k+1}-S_k = (k+1-N0(γ_{k+1})) - (k-N0(γ_k)) = 1 - ΔN0
print(f'ΔN0: mean={dN0.mean():+.5f}——std={dN0.std():.4f}')

# ΔN0 的结构——ΔN0 ~ N0'Δγ——Δγ 的（间距——）
dg = np.diff(z)
print(f'Δγ: mean={dg.mean():.5f}——std={dg.std():.5f}')

# dS = 1 - ΔN0 = -(ΔN0 - 1)——ΔN0 偏离 1 的（= -dS——）
# 相关结构: dS 的 ρ(lag) vs Δγ 的 ρ(lag)（间距相关——）
print()
print('ρ(lag) 对比（dS vs Δγ vs ΔN0——）:')
for lag in [1, 2, 3, 5, 10, 20, 50, 100]:
    c_dS = np.corrcoef(dS[:-lag], dS[lag:])[0,1]
    c_dg = np.corrcoef(dg[:-lag], dg[lag:])[0,1]
    c_dN = np.corrcoef(dN0[:-lag], dN0[lag:])[0,1]
    print(f'  lag={lag:3d}: ρ_dS={c_dS:+.4f}——ρ_Δγ={c_dg:+.4f}——ρ_ΔN0={c_dN:+.4f}')

# 关键: dS 的 ρ 是否 = Δγ 的 ρ（dS = 1-ΔN0 ≈ -N0'Δγ + 1 的——）
# ΔN0 ≈ N0'(γ_k)·Δγ_k——(1-ΔN0) ≈ 1 - N0'Δγ = -(N0'Δγ - 1) = -N0'δ
# 所以 dS ≈ -N0'δ——ρ(dS) ≈ ρ(δ)?（δ = Δγ - 1/N0'——）
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0p
print()
print('ρ(lag) dS vs δ（dS ≈ -N0\'δ——）:')
for lag in [1, 2, 3, 5, 10]:
    c_dS = np.corrcoef(dS[:-lag], dS[lag:])[0,1]
    c_d = np.corrcoef(delta[:-lag], delta[lag:])[0,1]
    print(f'  lag={lag}: ρ_dS={c_dS:+.4f}——ρ_δ={c_d:+.4f}')

# 方差压缩的'来源'——1+2Σρ(dS) 的分解——用 δ 的（如果 dS ~ -N0'δ——）
# Var(P_N) 的解析: P_N = ΣdS 的前缀和——压缩 = Σδ 相关?
print()
print('Σρ 的收敛性（方差压缩需要 Σρ = -1/2——）:')
cum_rho = 0
for lag in range(1, 2000):
    c = np.corrcoef(dS[:-lag], dS[lag:])[0,1]
    cum_rho += c
    if lag in [10, 50, 100, 200, 500, 1000, 1999]:
        print(f'  lag≤{lag}: Σρ = {cum_rho:+.4f}——1+2Σρ = {1+2*cum_rho:+.4f}')
