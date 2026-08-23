#!/usr/bin/env python3
"""分解 ΣΔw·A_k = 常数部分（望远镜）+ 振荡剩余
A_k = Σδ_j → 4.37（平台——O(1)）
ΣΔw·A_k ≈ A_∞·ΣΔw + ΣΔw·(A_k − A_∞)
第一项 = A_∞·(w_N − w_1) = O(1)（望远镜——无条件）
第二项——振荡剩余——数值检查
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

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np
Sd = np.cumsum(delta)
A_inf = Sd[-1]  # A_∞ ≈ 4.37（平台值）

print(f"A_∞ = Σδ（最终）= {A_inf:+.4f}")

for n in [10, 50, 100, 200, 500, 1000, 2000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    # 常数部分：A_∞·ΣΔw = A_∞·(w_N − w_1)
    const_part = A_inf * (w[-1] - w[0])
    # 完整：ΣΔw·A_k
    Ak = Sd[:len(dw)]
    full = np.sum(dw * Ak)
    # 振荡剩余：ΣΔw·(A_k − A_∞)
    resid = np.sum(dw * (Ak - A_inf))
    print(f"n={n:5d}: 常数部分 = {const_part:+8.3f}  完整 = {full:+8.3f}  振荡剩余 = {resid:+8.3f}")

# 关键：振荡剩余是否 O(1)？（如果 A_k 快速收敛到 A_∞——剩余小）
print(f"\nA_k 收敛到 A_∞ 的速度：")
for k in [1000, 5000, 10000, 50000, 100000, 400000]:
    print(f"  k={k:7d}: |A_k − A_∞| = {abs(Sd[k-1]-A_inf):.4f}")
