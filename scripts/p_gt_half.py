#!/usr/bin/env python3
"""尝试证明 p > 0.5（无条件）：为什么 δ 强交替（配对）？
p = P(δ_{k+1}δ_k < 0)——δ_k ≈ −ΔS_k/N₀'——S 增量的符号翻转
从 S 的结构：mean(S)=½（已证）——S 的"锯齿"（Gram 区间）
检验：p 的条件结构——大 |δ| 翻转（已知 0.949）——小 |δ| 呢？
以及：p 能否从 S 的回归（φ）推导？
"""
import numpy as np
import gc
from math import log, pi, asin

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)
gz = z[:-1]
dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del z, gz, dg, Np
gc.collect()

# 1. 条件 p：给定 δ_k 的大小——p(翻转) 的完整结构
print("条件翻转概率 p(|δ_k|)——完整结构：")
sign = np.sign(delta)
flip = sign[:-1] != sign[1:]
for lo, hi in [(0, 0.1), (0.1, 0.3), (0.3, 0.6), (0.6, 1.0), (1.0, 2.0)]:
    mask = (np.abs(delta[:-1]) >= lo) & (np.abs(delta[:-1]) < hi)
    if np.sum(mask) > 100:
        p_cond = np.mean(flip[mask])
        print(f"  |δ|∈[{lo},{hi}): p = {p_cond:.4f}（{np.sum(mask)} 样本）")

# 2. 关键：p > 0.5 的"整体"——但更重要的：δ 的期望符号（E[sign(δ)]）
print(f"\nE[sign(δ)] = {np.mean(sign):+.6f}（0 = 对称——无偏向）")

# 3. S 的锯齿结构：ΔS_k = S_{k+1}−S_k 与 δ 的关系
def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8
# S 在零点处（右极限）
S_k = np.array([(k+1) - N0(z2) for k, z2 in enumerate(load_zeros(1000000)[:1000000])], dtype=float)
del S_k
gc.collect()

# 4. 尝试：p 与 ρ₁ 的 arcsin 关系——但 ρ₁ 未推导——换：p 的直接结构
# p = P(ΔS_k·ΔS_{k+1} < 0)——ΔS 的符号
# 如果 ΔS 是"锯齿"（回归——φ）——ΔS 的符号交替？
print("\nΔS（S 增量）的符号结构：")
# 重算 S
z = load_zeros(1000000)
S = np.array([(k+1) - N0(z[k]) for k in range(1000000)], dtype=float)
dS = np.diff(S)
dSsign = np.sign(dS)
p_dS = np.mean(dSsign[:-1] != dSsign[1:])
print(f"  ΔS 的符号翻转概率 = {p_dS:.6f}（δ 的 p = 0.618——对比）")
print(f"  corr(δ, −ΔS·N₀') 应 = 1（恒等式）")

# 5. 关键检验：p > 0.5 的来源——ΔS 的"锯齿"（N₀'Δγ 围绕 1）
print("\nN₀'Δγ（Gram 约束）的分布：")
g = Np * (np.diff(z[:1000000]))
# delta = Δγ·N₀' − 1
print(f"  mean(N₀'Δγ) = {np.mean(g):.6f}（应 ≈ 1）")
print(f"  std = {np.std(g):.4f}  [min, max] = [{np.min(g):.3f}, {np.max(g):.3f}]")

del z, delta, sign, flip, dS, dSsign, g
gc.collect()
print("内存已释放")
