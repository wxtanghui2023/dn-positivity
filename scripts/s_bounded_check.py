#!/usr/bin/env python3
"""验证 S(t) 的数值范围——相位均匀性讨论的基础
S(γ_k⁺) = k − N₀(γ_k)（零点处右极限）
S 在区间 [γ_k, γ_{k+1}) 内 = k − N₀(t)——最小值在区间末（N₀ 增）
关键问题：S 是否有界？（Gram 定律——86.5% 在 (0,1)——但极端值？）
"""
import numpy as np

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8

K = 2000000
z = load_zeros(K)

# S(γ_k⁺) = k − N₀(γ_k)（k = 1..K）
S_k = np.arange(1, K+1) - N0(z)
print(f"S(γ_k⁺) 统计（K={K}）：")
print(f"  min = {np.min(S_k):+.4f}, max = {np.max(S_k):+.4f}")
print(f"  mean = {np.mean(S_k):+.6f}（理论 ½ + O(log²/N)）")
print(f"  <0 占比: {np.mean(S_k<0)*100:.2f}%   >1 占比: {np.mean(S_k>1)*100:.2f}%   (0,1) 占比: {np.mean((S_k>0)&(S_k<1))*100:.2f}%")

# S 在区间内的最小值：S(t) = k − N₀(t) on [γ_k, γ_{k+1})——最小值在 t→γ_{k+1}⁻
# = k − N₀(γ_{k+1}) = S(γ_{k+1}⁺) − 1
S_min_int = S_k[1:] - 1  # 区间 [γ_k, γ_{k+1}) 内最小值（左开右闭近似）
print(f"\n区间内 S 最小值（= S(γ_{'{k+1}'}⁺) − 1）：")
print(f"  min = {np.min(S_min_int):+.4f}")

# S 的全局范围（零点处 + 区间内）
all_S = np.concatenate([S_k, S_min_int])
print(f"  S 全局 min = {np.min(all_S):+.4f}")

# δ 与 S 的关系检查
dg = np.diff(z)
Np = np.log(z[:-1]/(2*np.pi))/(2*np.pi)
delta = dg - 1.0/Np
# 理论：δ_k ≈ −ΔS_k/N₀'(γ_k)——ΔS_k = S_{k+1} − S_k
dS = np.diff(S_k)
pred = -dS/Np
corr = np.corrcoef(delta, pred)[0,1]
print(f"\ncorr(δ, −ΔS/N') = {corr:.4f}（理论 0.9998——验证）")

# 关键：ρ(δ_k, δ_{k+1}) 与 S 有界的关系
rho_d = np.corrcoef(delta[:-1], delta[1:])[0,1]
rho_dS = np.corrcoef(dS[:-1], dS[1:])[0,1]
print(f"ρ(δ_k, δ_{'{k+1}'}) = {rho_d:.4f}")
print(f"ρ(ΔS_k, ΔS_{'{k+1}'}) = {rho_dS:.4f}")
