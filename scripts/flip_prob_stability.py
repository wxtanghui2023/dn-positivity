#!/usr/bin/env python3
"""符号翻转概率 p 的稳定性检验（BKT 局部配对的系统性）
p = P(δ_{k+1} 符号 ≠ δ_k)——p > 0.5 = 交替倾向（束缚）
如果 p 稳定 > 0.5（各高度）——局部配对是系统性的——可证性关键
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

sign = np.sign(delta)
flip = sign[:-1] != sign[1:]

# p 随高度的稳定性（分块）
print("符号翻转概率 p 随高度（块 = 100k 零点）：")
print(f"{'块':>4} {'γ 范围':>14} {'p':>8} {'mean|δ|':>8}")
for b in range(10):
    lo = b*100000
    hi = min((b+1)*100000, len(flip))
    if hi - lo < 1000: break
    p = np.mean(flip[lo:hi])
    md = np.mean(np.abs(delta[lo:hi]))
    print(f"{b+1:4d} [{z[lo]:8.1f}, {z[hi]:8.1f}] {p:8.4f} {md:8.4f}")

# p 与 |δ| 的关系（大 |δ| 是否更倾向翻转？）
print("\np 与 |δ_k| 的关系（大偏差的翻转倾向）：")
for thresh in [0, 0.3, 0.6, 1.0, 1.3]:
    mask = np.abs(delta[:-1]) > thresh
    if np.sum(mask) > 100:
        p_cond = np.mean(flip[mask])
        print(f"  |δ| > {thresh}: p = {p_cond:.4f}（{np.sum(mask)} 样本）")

# 理论：p 的"理想值"——如果 δ 是独立的——p = 0.5
# 实际 0.619——超额 0.119——"排斥"的量化
print(f"\n理论：独立 δ → p = 0.5（无配对）")
print(f"实际：p = {np.mean(flip):.4f}——超额 = {np.mean(flip)-0.5:.4f}（排斥的量化）")

del delta, sign, flip
gc.collect()
print("内存已释放")
