#!/usr/bin/env python3
"""BKT 类比验证：ζ 零点 = 2D 超流的涡旋（无隙但准长程刚性——拓扑保护）
BKT：关联 ~ r^{-η}（代数——准长程序——涡旋束缚）
ζ：ρ_j ~ j^{-α}（α≈0.45）——S(t) 相位 = 涡旋密度？
验证：1. α 的精确值（η 类比）
      2. 零点的"涡旋结构"（S 的跳跃 = 相位涡旋）
      3. 涡旋束缚的迹象（零点配对？）
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

z = load_zeros(500000)
gz = z[:-1]

dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del dg, Np
gc.collect()

# 1. α 的精确值（多个拟合区间）
print("α（ρ_j ~ j^{-α}）的精确值：")
d = delta - np.mean(delta)
s2 = np.var(delta)
for lo, hi in [(10, 100), (10, 500), (10, 2000), (50, 5000)]:
    lags = np.arange(lo, hi)
    rhos = np.array([np.mean(d[:-l]*d[l:])/s2 for l in lags])
    A = np.vstack([np.log(lags), np.ones(len(lags))]).T
    coef = np.linalg.lstsq(A, np.log(np.abs(rhos)), rcond=None)[0]
    print(f"  lag {lo}-{hi}: α = {-coef[0]:.4f}")

# 2. 涡旋结构：S(t) 的跳跃（arg ζ 的 2π 跳跃——winding）
def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8
S_k = np.array([(k+1) - N0(z[k]) for k in range(500000)], dtype=float)
dS = np.diff(S_k)
print(f"\nS 的跳跃统计（涡旋——winding）：mean(ΔS) = {np.mean(dS):+.4f}")
print(f"  ΔS 的范围：[{np.min(dS):+.4f}, {np.max(dS):+.4f}]（ΔS = 1-N₀'Δγ ≈ -δN₀'）")

# 3. 涡旋"束缚"迹象：δ 的相邻配对（正负交替——涡旋-反涡旋）
print("\n涡旋束缚检验（δ 的符号交替——配对）：")
sign = np.sign(delta)
flips = np.sum(sign[:-1] != sign[1:]) / (len(sign)-1)
print(f"  符号翻转率 = {flips:.4f}（0.5 = 随机——>0.5 = 交替——配对）")
# 交替（正负配对——涡旋束缚）
alt = np.sum(sign[:-1] == -sign[1:]) / (len(sign)-1)
print(f"  交替率 = {alt:.4f}（>0.5 = 强交替——涡旋-反涡旋配对）")

# 4. BKT 的"束缚能量"类比：δ 的大偏差成本
print("\nBKT 类比：涡旋束缚 vs 自由涡旋——δ 的约束：")
print(f"  max|δ| = {np.max(np.abs(delta)):.3f}（束缚——小）")
print(f"  max|Σδ| = {np.max(np.abs(np.cumsum(delta))):.3f}（低频压制——准长程序）")

del delta, d, S_k, dS, sign
gc.collect()
print("\n内存已释放")
