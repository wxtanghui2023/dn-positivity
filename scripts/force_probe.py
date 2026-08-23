#!/usr/bin/env python3
"""唐先生的外力探测实验：稳态看不出灾难抵消差额——加外力（变形）放大它
1. r(n) 对 n 的导数（dr/dn——响应）——量级？
2. 微扰零点位置（外力）——λ_n 的响应——χ(n)——找临界（峰）
3. 相变探测：哪个参数区域响应最大？
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

z = load_zeros(500000)

def th1(t):
    return np.arctan(1/(2*t))

def lam_n(n, z):
    return 4*np.sum(np.sin(n*th1(z))**2)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

gamma_E = 0.5772156649015329
c = 0.5*(gamma_E - 1 - log(2*pi))

def r_n(n, z):
    return lam_n(n, z) - (0.5*n*log(n) + c*n)

# 实验 1：dr/dn（响应——数值差分）
print("实验 1：r(n) 对 n 的导数（响应）：")
print(f"{'n':>6} {'r(n)':>10} {'r(n+1)':>10} {'Δr/Δn':>10} {'r(n)/n':>10}")
for n in [50, 100, 200, 500, 1000]:
    r1 = r_n(n, z)
    r2 = r_n(n+1, z)
    dr = r2 - r1
    print(f"{n:6d} {r1:+10.4f} {r2:+10.4f} {dr:+10.4f} {r1/n:+10.4f}")

# 实验 2：外力（微扰零点位置）——响应 χ
print("\n实验 2：外力微扰零点——λ_n 的响应：")
print("  微扰：γ_k → γ_k·(1+ε)——尺度变形")
for n in [100, 500]:
    base = lam_n(n, z)
    resp = []
    for eps in [1e-4, 3e-4, 1e-3, 3e-3]:
        z_pert = z*(1+eps)
        l_pert = lam_n(n, z_pert)
        chi = (l_pert - base)/eps
        resp.append(chi)
    print(f"  n={n}: χ(ε) = {[f'{c:.2f}' for c in resp]}")

# 实验 3：相变探测——微扰强度 vs 响应（找临界）
print("\n实验 3：微扰强度扫描（找响应峰值——相变）：")
for n in [100]:
    base = lam_n(n, z)
    print(f"  n={n}:")
    for eps in [1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2]:
        z_pert = z*(1+eps)
        l_pert = lam_n(n, z_pert)
        delta = l_pert - base
        chi = delta/eps
        print(f"    ε={eps:.0e}: Δλ = {delta:+.4f}  χ = {chi:+.2f}")

del z
gc.collect()
print("内存已释放")
