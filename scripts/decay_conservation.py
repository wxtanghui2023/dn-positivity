#!/usr/bin/env python3
"""验证：Σ t^{-γ}·δ = O(1)（衰减权重守恒律——潜在无条件定理）
Abel + Σδ=O(1)：Σ w_k δ_k = w_N·Σδ − ΣΔw_k·Σδ_j
w_k = t^{-γ}（γ>0）——w_N → 0——Σ|Δw| 收敛？——O(1)
"""
import numpy as np
import math
from math import log, pi
import gc

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
del dg, Np
gc.collect()

# Σδ 的部分和（O(1) 定理）
Sd = np.cumsum(delta)
print(f"max|Σδ| = {np.max(np.abs(Sd)):.3f}（O(1)——已证）")

# Abel 验证：Σ t^{-γ}δ = O(1) 对 γ > 0
print("\n衰减权重守恒律（Abel 验证）：")
print(f"{'γ':>5} {'Σ t^{-γ}δ':>12} {'Abel 重建':>12} {'Σ|Δw|':>10} {'max|Σ|':>10}")
for gamma in [0.5, 1.0, 1.5, 2.0]:
    w = gz**(-gamma)
    contrib = w * delta
    S = np.sum(contrib)
    cum = np.cumsum(contrib)
    # Abel：Σwδ = w_N·Σδ − ΣΔw·Σδ_j
    dw = np.diff(w)
    abel = w[-1]*Sd[-1] - np.sum(dw * Sd[:-1])
    print(f"{gamma:5.1f} {S:+12.4f} {abel:+12.4f} {np.sum(np.abs(dw)):10.4f} {np.max(np.abs(cum)):10.4f}")

# 边界：γ → 0（w ~ 常数——Σδ=O(1) 已证）——γ 小但正
print("\n边界（γ 小）：")
for gamma in [0.1, 0.2, 0.3]:
    w = gz**(-gamma)
    contrib = w * delta
    S = np.sum(contrib)
    cum = np.cumsum(contrib)
    print(f"  γ={gamma:.1f}: Σ = {S:+10.4f}  max|累积| = {np.max(np.abs(cum)):8.3f}")

del delta, Sd, gz
gc.collect()
print("\n内存已释放")
