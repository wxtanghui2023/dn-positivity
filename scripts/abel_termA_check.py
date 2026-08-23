#!/usr/bin/env python3
"""验证项 A 的 Abel 求和：Σ S_k·w_k = O(1)——w_k = g·Δγ 缓变
mean(S)=½：|Σ_{j≤k}S_j − k/2| = O(log²γ_k)（8/22 定理）
Abel：ΣS_k w_k = w_N·ΣS_k − ΣΔw_k·ΣS_j
需要：Σ|Δw_k|·log²γ_k < ∞
"""
import numpy as np
import math
from math import log, pi

def g(t):
    t = np.asarray(t, dtype=float)
    return 2*pi/(t*np.log(t/(2*pi))**2)

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 500000
z = load_zeros(K)

def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

S_k = np.array([(k+1) - N0(z[k]) for k in range(K)], dtype=float)
dg = np.diff(z)
w = g(z[:-1]) * dg  # w_k = g(γ_k)·Δγ_k

# 验证 mean(S)=½ 的偏差界
PS = np.cumsum(S_k)
dev = np.abs(PS - np.arange(1, K+1)/2)
print(f"max|ΣS_j − k/2| = {np.max(dev):.2f}（理论 O(log²γ)~{np.log(z[-1])**2:.1f}）")

# Δw_k 与 log²γ_k 的收敛
dw = np.diff(w)
gk = z[1:-1]
contrib = np.abs(dw) * np.log(gk)**2
print(f"\nΣ|Δw|·log²γ = {np.sum(contrib):.4f}（应收敛）")
print(f"尾部（后 1/3）Σ|Δw|·log²γ = {np.sum(contrib[2*len(contrib)//3:]):.4f}")

# Abel 求和验证
Sd_w = np.cumsum(S_k[:-1])  # Σ_{j≤k}S_j（k 从 0）
# Σ S_k·w_k = w_last·ΣS - Σ Δw_k·Σ_{j≤k}S_j
abel = w[-1]*Sd_w[-1] - np.sum(dw * Sd_w[:-1])
direct = np.sum(S_k[:-1] * w)
print(f"\nAbel 重建 = {abel:+.4f} vs 直接 = {direct:+.4f}（差 {abs(abel-direct):.2e}）")
print(f"ΣS_k·w_k = {direct:+.4f}（O(1)——因为 Σw_k ~ ∫g = 7.3——(1/2)Σw ~ 3.7）")
print(f"(1/2)Σw = {0.5*np.sum(w):+.4f}")
print(f"差 = {direct - 0.5*np.sum(w):+.4f}（应 O(1)——Abel 误差）")
