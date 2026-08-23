#!/usr/bin/env python3
"""验证 Abel 求和定理：Σ_k f̃(γ_k)ΔS_k = O(1)（无条件——加权 S 差分和）
w_k = f̃(γ_k)·N₀'(γ_k)——缓变权重
Σε_m = -Σ_k w_k·δ_k（δ_k = Δγ_k - 1/N₀'(γ_k)——间距偏差）

Abel 求和：Σ w_k δ_k = w_N·Σδ - Σ Δw_k·Σ_{k'≤k}δ_{k'}
需要验证：
1. w_k 缓变（|Δw_k| 小——|w'|Δγ）
2. Σ|Δw_k|·loglog γ_k 收敛
3. 直接计算 Σ_k w_k δ_k 是否 O(1)
"""
import numpy as np
import math

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 500000  # 用 500k 快速验证
z = load_zeros(K)

def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8

def N0p(t):
    return np.log(t/(2*np.pi))/(2*np.pi)

def theta(t):
    return np.pi - 2*np.arctan(2*t)

def ftilde(gamma, c):
    """f̃(γ) = 2sin(cθ(γ))sin(θ(γ)/2)——θ(γ) ≈ 1/γ 慢变"""
    th = theta(gamma)
    return 2*np.sin(c*th)*np.sin(th/2)

# 参数：c = n + 1/2（r(n) 的振荡核）——取 n=100（c=100.5）和 n=1000
for n in [100, 1000, 3000]:
    c = n + 0.5
    # 1. 直接计算 Σ_k w_k·δ_k
    g = z
    dg = np.diff(g)
    Np = N0p(g[:-1])
    # δ_k = Δγ_k - 1/N₀'(γ_k)
    delta = dg - 1.0/Np
    w = ftilde(g[:-1], c) * Np
    S_wdelta = np.sum(w * delta)
    
    # 2. Δw_k 的缓变性
    dw = np.diff(w)
    print(f"\nn={n} (c={c}):")
    print(f"  Σ w_k·δ_k = {S_wdelta:+10.4f}")
    print(f"  max|w| = {np.max(np.abs(w)):.4f}, max|Δw| = {np.max(np.abs(dw)):.6f}")
    print(f"  Σ|Δw| = {np.sum(np.abs(dw)):.4f}")
    
    # 3. Σ|Δw_k|·loglog(γ_k) 收敛检查
    gk = g[:-2]
    dw2 = dw
    loglog = np.log(np.log(gk))
    contrib = np.abs(dw2) * loglog
    print(f"  Σ|Δw|·loglog γ = {np.sum(contrib):.4f}")
    print(f"  尾部（后 1/3）Σ|Δw|·loglog = {np.sum(contrib[2*len(contrib)//3:]):.4f}")
    
    # 4. Abel 求和重建（比较）
    # Σ_{k'≤k}δ_{k'} 的部分和
    Sd = np.cumsum(delta)
    # Σ w_k δ_k = w_last·Sd_last - Σ Δw_k·Sd_k
    abel = w[-1]*Sd[-1] - np.sum(dw*Sd[:-1])
    print(f"  Abel 重建 = {abel:+10.4f}（应≈直接计算 {S_wdelta:+10.4f}）")
    print(f"  max|Σδ| = {np.max(np.abs(Sd)):.3f}（理论 O(loglog)~{np.log(np.log(z[-1])):.2f}）")
