#!/usr/bin/env python3
"""攻击振荡剩余：ΣΔw·(A_k−A_∞) = O(1) 的证明框架验证
单调区（γ_k > n/π）：Δw < 0 缓变——部分求和：
Σ Δw_k·(A_k−A_∞) = 端点 + Σ Δ(Δw)_k·Σ_{j≤k}(A_j−A_∞)
需要：|Σ_{j≤k}(A_j−A_∞)| = O(k^α)（α<1——从 δ 反持久）
验证：Σ_{j≤k}(A_j−A_∞) 的增长 + Σ|Δ(Δw)|·k^α 的收敛
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
Sd = np.cumsum(delta)
A_inf = Sd[-1]
resid = Sd - A_inf  # A_k − A_∞

# 1. Σ_{j≤k}(A_j − A_∞) 的部分和（A 的部分和——二阶矩）
print("1. |Σ_{j≤k}(A_j−A_∞)| 的增长（反持久检验）：")
S2 = np.cumsum(resid)
for k in [100, 1000, 10000, 100000, 500000, 999999]:
    print(f"  k={k:7d}: |ΣA_j残差| = {abs(S2[k-1]):.3f}  （k^0.16 = {k**0.16:.2f}——k^0.5 = {k**0.5:.1f}）")

# 拟合 α
ks = np.array([100, 1000, 10000, 100000, 500000, 999999], dtype=float)
vals = np.array([abs(S2[int(k)-1]) for k in ks], dtype=float)
A = np.vstack([np.log(ks), np.ones(len(ks))]).T
coef = np.linalg.lstsq(A, np.log(vals), rcond=None)[0]
print(f"  α = {coef[0]:.3f}（|ΣA_j残差| ~ k^α——目标 α < 1）")

# 2. Σ|Δ(Δw)_k|·k^α 的收敛（Δ²w = Δw_{k+1}−Δw_k）
print("\n2. Σ|Δ(Δw)_k|·k^α 收敛性（α = 0.16）：")
for n in [100, 1000, 5000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    d2w = np.diff(dw)
    ks_arr = np.arange(1, len(d2w)+1)
    contrib = np.abs(d2w) * ks_arr**0.16
    total = np.sum(contrib)
    print(f"  n={n}: Σ|Δ²w|·k^0.16 = {total:.4f}（尾部后1/3 = {np.sum(contrib[2*len(contrib)//3:]):.4f}）")

# 3. 完整部分求和重建（单调区 k > n/π）
print("\n3. 单调区部分求和重建 vs 直接：")
for n in [100, 1000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    # 单调区起点：|n·θ_k| < π——θ ≈ -1/γ——γ > n/π
    k0 = int(n/pi * 2*np.pi/np.log(max(n/pi, 2)))  # 粗略：γ ~ n/π 处的 k
    k0 = max(k0, 1)
    Ak = resid[:len(dw)]
    # 直接（单调区）
    direct = np.sum(dw[k0:] * Ak[k0:])
    # 部分求和：Δw_k·A_k = Δw_N·ΣA - Σ Δ(Δw)·ΣA
    # 用 A_k（残差）的部分和
    S_A = np.cumsum(Ak[k0:])
    d2w = np.diff(dw[k0:])
    ps = d2w[-1]*S_A[-1] - np.sum(d2w[:-1] * S_A[:-1]) + dw[k0]*Ak[k0]
    # 更标准的：Σ_{k≥k0}Δw_k·B_k = Δw_N·ΣB − ΣΔ(Δw)·Σ_{j≤k}B_j（Δw_N→0）
    B = Ak[k0:]
    dw2 = dw[k0:]
    SB = np.cumsum(B)
    ddw = np.diff(dw2)
    ps2 = -np.sum(ddw * SB[:-1])  # 端点项 0（dw_N→0）
    print(f"  n={n}: 单调区直接 = {direct:+.4f} vs 部分求和 = {ps2:+.4f}")
