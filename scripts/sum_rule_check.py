#!/usr/bin/env python3
"""物理 sum rule 验证：守恒律（Σδ=O(1)）⟹ 方差压缩（1+2Σρ=0）？
物理：守恒 ⟹ 零频响应 S_δ(0)=0——块和的"平均"行为
关键：块和 O(1)（有界）是否 → 0（平均）？——物理 sum rule 需要"趋于 0"
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

z = load_zeros(2000000)
gz = z[:-1]

dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del dg, Np
gc.collect()

# 1. 块和的行为：不同块大小的 Σδ 分布
print("块和 Σδ 的统计（守恒——物理 sum rule）：")
for block in [100, 1000, 10000, 100000]:
    nblocks = len(delta)//block
    blocks = delta[:nblocks*block].reshape(nblocks, block)
    sums = np.sum(blocks, axis=1)
    print(f"  块={block:7d}: mean={np.mean(sums):+.4f}  std={np.std(sums):.4f}  max|·|={np.max(np.abs(sums)):.3f}  std/√block={np.std(sums)/np.sqrt(block):.4f}")

# 2. 关键：块和的平方平均 → 0？（物理 sum rule：S_δ(0)=0）
print("\n块和平方平均（→0 = 方差完全压缩——sum rule）：")
for block in [100, 1000, 10000, 100000]:
    nblocks = len(delta)//block
    blocks = delta[:nblocks*block].reshape(nblocks, block)
    sums = np.sum(blocks, axis=1)
    ms = np.mean(sums**2)
    # 独立预测：block·Var(δ)
    var_ind = block * np.var(delta)
    print(f"  块={block:7d}: mean(Σδ)² = {ms:10.4f}  独立预测 = {var_ind:10.4f}  压缩比 = {ms/var_ind:.6f}")

# 3. 物理"零频响应"：S_δ(0) 的直接估计
# S_δ(0) = Σρ（全滞后）= (1+2Σρ−1)/2——1+2Σρ ≈ 0 已验
print("\n1+2Σρ（全滞后——零频响应——应 → 0）：")
d = delta - np.mean(delta)
s2 = np.var(delta)
cum = 1.0
for lag in range(1, 5001):
    rho = np.mean(d[:-lag]*d[lag:])/s2
    cum += 2*rho
    if lag in [1, 10, 100, 1000, 5000]:
        print(f"  lag≤{lag:5d}: 1+2Σρ = {cum:+.4f}")

del delta, d, gz
gc.collect()
print("\n内存已释放")
