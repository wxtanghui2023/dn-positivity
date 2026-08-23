#!/usr/bin/env python3
"""物理"天然推导"检验：无穷守恒（短程族 Σt^{-γ}δ=O(1)）⟹ 完全刚性（方差压缩）
可积系统：无穷守恒 ⟹ 关联精确——ζ 的短程守恒族能否推出 1+2Σρ=0？
检验：加权块和（t^{-γ} 权重）的行为——平均 → 0？（⟹ 压缩）
"""
import numpy as np
import gc
from math import log, pi

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

# 加权块和：Σ_{k in block} t_k^{-γ}·δ_k——块的行为
print("加权块和的行为（无穷守恒检验——可积系统）：")
for gamma in [0.5, 1.0, 2.0]:
    w = gz**(-gamma)
    wd = w * delta
    print(f"\nγ = {gamma}：")
    for block in [1000, 10000]:
        nblocks = len(wd)//block
        blocks = wd[:nblocks*block].reshape(nblocks, block)
        sums = np.sum(blocks, axis=1)
        print(f"  块={block:6d}: mean(块和) = {np.mean(sums):+.6f}  std = {np.std(sums):.6f}  max|·| = {np.max(np.abs(sums)):.6f}  std/√block = {np.std(sums)/np.sqrt(block):.6f}")

# 关键：加权块和的平方平均 → 0？（⟹ 压缩——相位均匀性的一步）
print("\n加权块和平方平均（→0 = 完全压缩）：")
for gamma in [0.5, 1.0, 2.0]:
    w = gz**(-gamma)
    wd = w * delta
    for block in [1000, 10000, 100000]:
        nblocks = len(wd)//block
        blocks = wd[:nblocks*block].reshape(nblocks, block)
        sums = np.sum(blocks, axis=1)
        ms = np.mean(sums**2)
        var_ind = block * np.var(wd)
        print(f"  γ={gamma}: 块={block:7d}: mean(Σ)² = {ms:.3e}  独立 = {var_ind:.3e}  压缩比 = {ms/var_ind:.6f}")

# 理论：1+2Σρ 与加权块和的关系——如果 γ→0（无权重）——1+2Σρ
print("\n1+2Σρ（无权重——γ→0 极限——之前的验证）：")
d = delta - np.mean(delta)
s2 = np.var(d)
cum = 1.0
for lag in [1, 10, 100, 1000]:
    rho = np.mean(d[:-lag]*d[lag:])/s2
    cum += 2*rho
    print(f"  lag≤{lag:5d}: 1+2Σρ = {cum:+.4f}")

del z, gz, delta, d
gc.collect()
print("\n内存已释放")
