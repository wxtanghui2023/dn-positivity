#!/usr/bin/env python3
"""验证"长程刚性"：1+2Σρ(δ) 的全滞后累积——是否精确 = 0？
对应唐先生线索（Bourgade 刚性/Odlyzko 长程相关/Berry-Keating 谱刚性）
1+2Σ_{j≥1}ρ_j = 0 ⟺ 方差完全压缩 ⟺ 长程刚性
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

K = 2000000
z = load_zeros(K)

dg = np.diff(z)
Np = np.log(z[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np
d = delta - np.mean(delta)
s = np.std(d)
s2 = s*s

# 全滞后自相关（到 lag 1000——长程）
print("1 + 2Σρ_j 的全滞后累积（长程刚性检验）：")
cum = 1.0
for lag in range(1, 1001):
    rho = np.mean(d[:-lag]*d[lag:])/s2
    cum += 2*rho
    if lag in [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000]:
        print(f"  lag ≤ {lag:4d}: 1+2Σρ = {cum:+.4f}")

# 长程相关的衰减率——ρ_j 的尾部分布
print("\nρ_j 的衰减（长程相关结构）：")
for lag in [1, 2, 5, 10, 50, 100, 500, 1000, 5000]:
    rho = np.mean(d[:-lag]*d[lag:])/s2
    print(f"  lag={lag:5d}: ρ = {rho:+.5f}")

# 分块方差压缩（长程——大块）
print("\n分块 Σδ 的方差压缩（块大小 → 大）：")
for block in [1000, 10000, 100000]:
    nblocks = len(delta)//block
    blocks = delta[:nblocks*block].reshape(nblocks, block)
    sums = np.sum(blocks, axis=1)
    var_comp = np.var(sums)/(block*s2)  # = 1+2Σρ（块内）
    print(f"  block={block:6d}: Var(块和)/(block·Var(δ)) = {var_comp:.4f}（→0 = 完全压缩）")
