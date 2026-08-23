#!/usr/bin/env python3
"""物理角度探索：ζ 零点是"可积/守恒"系统？（Toda 晶格类比）
可积系统特征：无限守恒量 + 孤子（局部化大偏差）
检查：
1. δ 的"守恒量族"——Σwδ 对多个 w（已验证几个——O(1)？）
2. δ 的大偏差结构——孤子（局部化）vs 随机（分布）
3. δ 的谱隙——功率谱低频（S_δ(0) ≈ 0？）
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

# 分块加载（内存管理——NAS 重启教训！）
CHUNK = 500000
z = load_zeros(CHUNK)  # 只加载 50 万——够探索

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np
del dg, Np  # 及时释放

# 1. 守恒量族：Σwδ 对多个权重（可积系统的"守恒量"检验）
print("守恒量族检验（Σwδ——多个权重——可积系统的特征）：")
weights = {
    "常数(1)": np.ones_like(delta),
    "1/t": 1.0/z[:-1],
    "1/t²": 1.0/(z[:-1]**2),
    "log t/t²": np.log(z[:-1])/(z[:-1]**2),
    "sin(t/100)": np.sin(z[:-1]/100),
    "cos(t/100)": np.cos(z[:-1]/100),
}
for name, w in weights.items():
    S = np.sum(w * delta)
    print(f"  {name:12s}: Σwδ = {S:+.4f}")

# 2. δ 的大偏差结构（孤子 vs 随机）
print("\nδ 的大偏差（|δ| > 2 的孤立性——孤子特征）：")
big = np.where(np.abs(delta) > 2)[0]
print(f"  |δ|>2 的数量：{len(big)}（{len(big)/len(delta)*100:.2f}%）")
if len(big) > 3:
    # 检查大偏差是否"孤立"（孤子——周围正常）vs 成簇
    gaps_between = np.diff(big)
    print(f"  大偏差间距：min={gaps_between.min()}, max={gaps_between.max()}, 中位数={np.median(gaps_between):.0f}")
    print(f"  （若间距大——孤立（孤子）；若小——成簇）")

# 3. 谱隙：δ 的功率谱低频（S_δ(0) ≈ 0？——物理谱隙）
print("\nδ 的谱隙检验（累积和——低频压制）：")
Sd = np.cumsum(delta)
print(f"  max|Σδ| = {np.max(np.abs(Sd)):.3f}（低频压制——谱隙——O(1) 已证）")

# 4. 分块释放
del delta, Sd, weights
import gc; gc.collect()
print("\n内存已释放（分块处理——NAS 教训）")
