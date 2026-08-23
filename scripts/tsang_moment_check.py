#!/usr/bin/env python3
"""验证 Tsang/Selberg 矩与我们的 A_j 二阶结构连接
Tsang: ∫(S(t+h)−S(t))²dt ~ H·(1/π²)·log(2+h·log T)（k=1——无条件）
ΔS_k = −δ_k·N₀'——所以 δ 的二阶矩 = (1/N₀'²)·(1/π²)·log(2+h log T)
连接：Σ_{j≤k}A_j（δ 的二阶加权）能否用这个矩控制？
"""
import numpy as np
import math
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np

# 1. 验证 ΔS 的二阶矩（Tsang 预测）
# ΔS_k ≈ −δ_k·N₀'(γ_k)——S 的增量
# 但 ΔS_k = S(γ_{k+1})−S(γ_k) = 1 − N₀'(ξ)Δγ ≈ −δ_k·N₀'(γ_k)
dS = np.diff(np.arange(1, len(z)+1) - np.array([(t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8 for t in z]))
# 更直接：ΔS_k = 1 − N₀'(γ_k)·Δγ_k·(1+o)
dS2 = 1.0 - Np*dg  # ≈ ΔS_k（一阶）
pred = -delta * Np  # 理论：−δ·N₀'
corr = np.corrcoef(dS2, pred)[0,1]
print(f"corr(ΔS, −δ·N₀') = {corr:.4f}")

# 2. 分块二阶矩：∫(S(t+h)−S(t))² vs Tsang 预测
# h = 块内零点数对应的 t 间隔
for block in [100, 1000]:
    nblocks = len(dS2)//block
    # 每块的 ΔS 平方和（对应 ∫(ΔS)²dt 的离散版）
    sq = dS2[:nblocks*block].reshape(nblocks, block)
    block_sq = np.sum(sq**2, axis=1)  # 每块 ΣΔS²
    # Tsang: H·(1/π²)·log(2+h·log T)——H = block·(平均间距) = block/N₀'
    # 离散版：ΣΔS² ~ block·(1/π²)·log(2+h·log γ)——γ 是块中心
    mean_sq = np.mean(block_sq)
    print(f"\nblock={block}: 平均 ΣΔS² = {mean_sq:.4f}")
    # 对比 Tsang：block·(1/π²)·log(2+block·log γ/(2π)·(1/N₀'))... 简化
    # h·log T ~ block（因为 h ~ block·间距——h·log γ ~ block·2π）
    tsang_pred = block/(pi*pi)*log(2 + block)
    print(f"  Tsang 预测（粗略）：block·(1/π²)·log(2+block) = {tsang_pred:.4f}")

# 3. 关键：δ 的平方和（对应 ΔS 矩）
print("\nδ 的分块平方和（二阶矩）：")
for block in [100, 1000, 10000]:
    nblocks = len(delta)//block
    sq = delta[:nblocks*block].reshape(nblocks, block)
    block_sq = np.sum(sq**2, axis=1)
    print(f"  block={block}: mean Σδ² = {np.mean(block_sq):.4f}（Tsang 类 ~ block·log(2+block)/π²·(1/N₀'²)...）")
