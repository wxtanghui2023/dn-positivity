#!/usr/bin/env python3
"""验证 δ 的短块和 ≈ 0（局部密度守恒）——A_k 高频振荡的机制
A_k = Σδ——过零周期 3——因为 δ 的 3 项块和 ≈ 0？
如果 δ 的 m 项块和 ≈ 0（无条件——密度守恒）——A_k 振荡可控
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

print("δ 的 m 项块和（局部密度守恒检验）：")
for m in [2, 3, 5, 10, 20, 50]:
    nblocks = len(delta)//m
    blocks = delta[:nblocks*m].reshape(nblocks, m)
    sums = np.sum(blocks, axis=1)
    print(f"  m={m:3d}: 块和 mean = {np.mean(sums):+.5f}  std = {np.std(sums):.4f}  max|·| = {np.max(np.abs(sums)):.4f}")

# 关键：A_k 的块均值（m 项）——是否 ≈ 常数
print("\nA_k 的 m 项块均值（应 ≈ A_∞ 如果 δ 块和 ≈ 0）：")
Sd = np.cumsum(delta)
A_inf = Sd[-1]
for m in [3, 5, 10]:
    nblocks = len(Sd)//m
    blocks = Sd[:nblocks*m].reshape(nblocks, m)
    means = np.mean(blocks, axis=1)
    print(f"  m={m:3d}: 块均值 mean = {np.mean(means):+.4f}  std = {np.std(means):.4f}  （A_∞ = {A_inf:+.4f}）")

# 最关键的检验：ΣΔw·A_k 的"块化"——每 m 项一块——Δw 缓变
print("\n块化验证：ΣΔw·A_k ≈ Σ (Δw 块均值)·(A_k 块均值)——缓变×振荡：")
for n in [100, 1000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    Ak = Sd[:len(dw)]
    m = 10
    nblocks = len(dw)//m
    dw_blocks = dw[:nblocks*m].reshape(nblocks, m)
    Ak_blocks = Ak[:nblocks*m].reshape(nblocks, m)
    dw_mean = np.mean(dw_blocks, axis=1)
    Ak_mean = np.mean(Ak_blocks, axis=1)
    block_sum = np.sum(dw_mean * Ak_mean) * m
    full = np.sum(dw * Ak)
    print(f"  n={n}: 块化 = {block_sum:+.4f} vs 完整 = {full:+.4f}")
