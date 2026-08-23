#!/usr/bin/env python3
"""验证部分求和框架：Σ|Δ²w_k|·k^α（α = 0.495——实际 ΣA_j残差 的增长）
如果收敛——振荡剩余 O(1) 的证明框架成立
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

print("Σ|Δ²w_k|·k^α（α=0.495）收敛性：")
for n in [100, 500, 1000, 2000, 5000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    d2w = np.diff(dw)
    ks = np.arange(1, len(d2w)+1)
    contrib = np.abs(d2w) * ks**0.495
    total = np.sum(contrib)
    tail = np.sum(contrib[4*len(contrib)//5:])
    print(f"  n={n:5d}: Σ|Δ²w|·k^0.495 = {total:8.4f}（尾部后1/5 = {tail:.4f}）")

# 用单调区（k > n/π 附近）——Δw 缓变的区域
print("\n单调区（|n·θ| < π——γ > n/π）的部分求和：")
for n in [100, 1000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    d2w = np.diff(dw)
    # 单调区起点：找 γ_k > n/π 的第一个 k
    gam = z[:-1]
    k0 = np.searchsorted(gam, n/pi)
    if k0 < len(d2w):
        ks = np.arange(1, len(d2w)+1)
        contrib = np.abs(d2w[k0:]) * ks[k0:]**0.495
        print(f"  n={n}: k0={k0}（γ={gam[k0]:.1f}）Σ|Δ²w|·k^0.495（单调区）= {np.sum(contrib):.4f}")
