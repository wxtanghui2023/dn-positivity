#!/usr/bin/env python3
"""验证振荡剩余的正交性假设：A_k（低频）vs Δw（高频）
A_k − A_∞：δ 部分和残差——波动周期（低频？）
Δw_k ~ n·sin(nθ_k)·Δθ_k：振荡——频率 ~ n/(γ²log γ)
如果频谱分离——ΣΔw·(A_k−A_∞) = O(1)（Riemann-Lebesgue 型）
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

z = load_zeros(500000)

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np
Sd = np.cumsum(delta)
A_inf = Sd[-1]
resid = Sd[:len(Sd)] - A_inf  # A_k − A_∞

# A_k 残差的"波动周期"——过零次数
sign_changes_A = np.sum(np.sign(resid[1:]) != np.sign(resid[:-1]))
print(f"A_k − A_∞：过零次数 = {sign_changes_A}（{len(resid)} 点——周期 ~ {len(resid)/max(sign_changes_A,1):.0f}）")

# Δw 的振荡（n=100, 1000）
for n in [100, 1000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    sign_changes_w = np.sum(np.sign(dw[1:]) != np.sign(dw[:-1]))
    print(f"\nn={n}: Δw 过零次数 = {sign_changes_w}（周期 ~ {len(dw)/max(sign_changes_w,1):.0f}）")
    
    # 相关性：corr(resid[:-1], dw)
    r = np.corrcoef(resid[:len(dw)], dw)[0,1]
    print(f"  corr(A_k−A_∞, Δw) = {r:+.4f}（≈0 = 正交）")
    
    # 块相关（分块看）
    block = 5000
    corrs = []
    for i in range(0, len(dw)-block, block):
        c = np.corrcoef(resid[i:i+block], dw[i:i+block])[0,1]
        if not np.isnan(c):
            corrs.append(c)
    print(f"  分块 corr：mean = {np.mean(corrs):+.4f}  max|·| = {np.max(np.abs(corrs)):.4f}")

# 关键检验：振荡剩余的累积——看是否有系统增长
print(f"\n振荡剩余 ΣΔw·(A_k−A_∞) 的累积结构：")
for n in [100, 1000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    Ak = resid[:len(dw)]
    contrib = dw * Ak
    cum = np.cumsum(contrib)
    print(f"  n={n}: 最终 = {cum[-1]:+.4f}  max|累积| = {np.max(np.abs(cum)):.4f}")
