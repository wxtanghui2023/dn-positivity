#!/usr/bin/env python3
"""深挖：Σ1/(γ_k−γ_j) ≈ 常数（−2.5）——零点局部排斥场的普适常数
局部（对称窗口）vs 全范围——窗口大小依赖
与 GUE 的对应（能级排斥的局部结构）
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

z = load_zeros(500000)

# 局部窗口的 Σ1/(γ_k−γ_j)——窗口大小依赖
print("Σ1/(γ_k−γ_j) 的窗口大小依赖（k=5000——γ≈5449）：")
gk = z[5000]
for W in [10, 50, 100, 200, 500, 1000, 5000, 20000]:
    lo = max(0, 5000-W); hi = min(len(z), 5000+W)
    s = 0.0
    for j in range(lo, hi):
        if j != 5000:
            s += 1.0/(gk - z[j])
    print(f"  窗口 ±{W:6d}: Σ = {s:+.4f}")

# 多个 k 的局部值（窗口 ±2000）
print("\nΣ1/(γ_k−γ_j)（窗口 ±2000）随 k：")
for k in [1000, 5000, 10000, 50000, 100000, 200000, 400000]:
    gk = z[k]
    lo = max(0, k-2000); hi = min(len(z), k+2000)
    s = 0.0
    for j in range(lo, hi):
        if j != k:
            s += 1.0/(gk - z[j])
    # 归一化：局部密度 ~ log γ/(2π)——Σ1/(γ_k−γ_j) 是"局部排斥"
    Np = log(gk/(2*pi))/(2*pi)
    print(f"  γ_{k:6d} = {gk:10.3f}: Σ（±2000）= {s:+.4f}  N₀' = {Np:.4f}  Σ/N₀' = {s/Np:.4f}")

# 理论：如果零点"均匀"（平均密度 ρ）——Σ_{j≠k}1/(γ_k−γ_j) 的期望
# 局部均匀（密度 ρ）：Σ ~ ρ·∫(1/x)dx（对称——主值——0？）——但实际 −2.5
# 说明：不是均匀——有结构（排斥——间距分布）
print("\n与 GUE 的对应：GUE 特征值的局部排斥——Σ1/(λ_k−λ_j)（跳过自己）")
print("GUE（Sine 核——普适）：局部结构不依赖位置——ζ 的 −2.5 常数类似")
