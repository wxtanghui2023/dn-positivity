#!/usr/bin/env python3
"""严格化验证：ΣΔu·(S−½) = O(1) 的 Abel 证明
ΣΔu_k·(S_{k+1}−½) = Δu_N·Σ(S−½) − ΣΔ²u_k·Σ_{j≤k}(S_j−½)
需要：Σ(S_j−½) = O(log²γ)（mean(S)=½ 定理）——Σ|Δ²u|·log² 收敛？
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

def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

S_k = np.array([(k+1) - N0(z[k]) for k in range(len(z))], dtype=float)

# Σ(S_j − ½) 的界（mean(S)=½ 的误差）
PS = np.cumsum(S_k - 0.5)
print("Σ(S_j−½) 的界（mean(S)=½ 误差）：")
for k in [100, 1000, 10000, 100000, 500000, 999999]:
    print(f"  k={k:7d}: |Σ(S_j−½)| = {abs(PS[k-1]):8.3f}  log²γ = {np.log(z[k-1])**2:8.2f}")

# Σ|Δ²u|·log²γ 的收敛（u = w/N₀'——f_n 核）
print("\nΣ|Δ²u|·log²γ 收敛性：")
for n in [100, 500, 1000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    u = w / N0p(z[:-1])
    du = np.diff(u)
    d2u = np.diff(du)
    gk = z[1:-2]
    contrib = np.abs(d2u) * np.log(gk)**2
    total = np.sum(contrib)
    tail = np.sum(contrib[4*len(contrib)//5:])
    print(f"  n={n:5d}: Σ|Δ²u|·log²γ = {total:10.4f}（尾部后1/5 = {tail:.4f}）")

# 验证 Abel：ΣΔu·(S−½) = Δu_N·Σ(S−½) − ΣΔ²u·Σ(S−½)（精确）
print("\nAbel 恒等式验证：")
for n in [100, 1000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    u = w / N0p(z[:-1])
    du = np.diff(u)
    d2u = np.diff(du)
    # ΣΔu_k·(S_{k+1}−½)——注意索引
    S_resid = S_k[1:len(u)] - 0.5
    direct = np.sum(du * S_resid)
    # Abel：Σ du_k·B_k = du_{N}·ΣB − Σ d2u_k·Σ_{j≤k}B_j
    SB = np.cumsum(S_resid)
    abel = du[-1]*SB[-1] - np.sum(d2u * SB[:-1])
    print(f"  n={n}: 直接 = {direct:+.4f} vs Abel = {abel:+.4f}（差 {abs(direct-abel):.2e}）")
