#!/usr/bin/env python3
"""修复版：Σδ_k = O(1) 确认——避免 numpy 精度崩溃
用纯 Python 循环（float64 安全）计算 δ_k
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

K = 500000  # 500k 足够确认
z = load_zeros(K)

# 逐点计算 δ_k（float64 安全）
deltas = []
for k in range(K-1):
    gk = z[k]
    Np = log(gk/(2*pi))/(2*pi)
    dg = z[k+1] - gk
    deltas.append(dg - 1.0/Np)
deltas = np.array(deltas)

# 检查异常值
bad = np.where(np.abs(deltas) > 100)[0]
print(f"异常 δ 数量：{len(bad)}")
if len(bad) > 0:
    for i in bad[:5]:
        print(f"  k={i}: γ={z[i]:.4f}, δ={deltas[i]:.3e}")
    # 移除异常
    mask = np.abs(deltas) < 100
    deltas_clean = deltas[mask]
    print(f"移除后：{len(deltas_clean)} 个正常 δ")
else:
    deltas_clean = deltas

print(f"\nδ 统计：mean={np.mean(deltas_clean):+.6f} std={np.std(deltas_clean):.4f}")
print(f"  min={np.min(deltas_clean):+.4f} max={np.max(deltas_clean):+.4f}")

# Σδ 部分和
Sd = np.cumsum(deltas_clean)
print(f"\nΣδ_k 部分和：")
print(f"  最终 = {Sd[-1]:+.4f}")
print(f"  max|Σδ| = {np.max(np.abs(Sd)):.4f}")
print(f"  分块（每 100k）：")
for i in range(0, len(deltas_clean), 100000):
    j = min(i+100000, len(deltas_clean))-1
    print(f"    k={i+1:6d}-{j+1:6d}: Σδ = {Sd[j]:+.4f}")
print(f"\n  loglog(γ_500k) = {log(log(z[-1])):.4f}（8/22 理论界 O(loglog)）")
print(f"  max|Σδ| = {np.max(np.abs(Sd)):.4f}（若 O(1)——改进！）")
