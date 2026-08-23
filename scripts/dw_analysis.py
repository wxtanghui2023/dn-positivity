#!/usr/bin/env python3
"""验证 Δw_k 分析：Σ|Δw_k| 对 n 的依赖 + 带符号抵消
w_k = 1 − cos(nθ_k)，θ_k = 2arctan(2γ_k) − π ≈ −1/γ_k
预测：Σ|Δw_k| = O(n)——但带符号 ΣΔw_k·A_k（A_k = Σδ = O(1)）可能更好
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
Sd = np.cumsum(delta)  # A_k = Σ_{j≤k}δ_j = O(1)（新定理）

print("w_k = 1 − cos(nθ_k) 的 Δw_k 分析：")
print(f"{'n':>6} {'Σ|Δw|':>10} {'ΣΔw·A_k':>12} {'|r(n)|≈|ΣΔw·A|':>14}")
for n in [10, 50, 100, 200, 500, 1000, 2000]:
    th = 2*np.arctan(2*z[:-1]) - pi  # θ_k ≈ −1/γ
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    s_abs = np.sum(np.abs(dw))
    # ΣΔw_k·A_k（A_k = Σδ——部分和——Abel 的核心项）
    S_wa = np.sum(dw * Sd[:-1]) if len(dw) == len(Sd[:-1]) else np.sum(dw * Sd[:len(dw)])
    print(f"{n:6d} {s_abs:10.4f} {S_wa:+12.4f} {abs(S_wa):14.4f}")

# 关键：Δw_k 的符号结构——振荡？
print("\nΔw_k 的符号变化（n=100——前 50 个）：")
th = 2*np.arctan(2*z[:-1]) - pi
w = 1 - np.cos(100*th)
dw = np.diff(w)
sign_changes = np.sum(np.sign(dw[1:]) != np.sign(dw[:-1]))
print(f"  符号变化次数（前 500k）：{sign_changes}（振荡——抵消来源）")
