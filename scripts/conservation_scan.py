#!/usr/bin/env python3
"""物理方向：系统扫描"守恒量族"——Σwδ 对权重族 w ~ t^{-α}、t^{α} 的边界
守恒律（可积系统）的定量结构——哪些权重有界（守恒）——物理"相关长度"
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

# 分块加载（内存管理）
z = load_zeros(1000000)
gz = z[:-1]

dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del dg, Np
gc.collect()

print("守恒量族扫描：Σwδ for w ~ t^α（α 扫描——守恒边界）：")
print(f"{'α':>6} {'Σ t^α·δ':>12} {'max|累积|':>10}")
for alpha in [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0]:
    w = gz**alpha
    contrib = w * delta
    S = np.sum(contrib)
    cum = np.cumsum(contrib)
    print(f"{alpha:6.1f} {S:+12.4f} {np.max(np.abs(cum)):10.3f}")

print("\n权重扫描：w ~ (log t)^β / t^γ：")
for gamma, beta in [(2, 0), (2, 1), (1.5, 0), (1.5, 1), (1, 0), (1, 1)]:
    w = np.log(gz)**beta / (gz**gamma)
    contrib = w * delta
    S = np.sum(contrib)
    cum = np.cumsum(contrib)
    print(f"  (log t)^{beta}/t^{gamma}: Σ = {S:+10.4f}  max|累积| = {np.max(np.abs(cum)):8.3f}")

print("\n振荡权重（物理：声子模——频率 ω）：")
for freq in [0.01, 0.05, 0.1, 0.5, 1.0]:
    w = np.cos(freq * gz)
    contrib = w * delta
    S = np.sum(contrib)
    print(f"  cos({freq}·t): Σ = {S:+10.4f}")

del delta, gz
gc.collect()
print("\n内存已释放")
