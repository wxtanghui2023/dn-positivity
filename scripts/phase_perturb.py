#!/usr/bin/env python3
"""相位扰动实验（唐先生外力探测的正确设计）
只扰动相位（不改变密度）：γ_k → γ_k + ε·sin(γ_k)——振荡位移
响应：Δλ_n = λ_n(扰动) − λ_n(未扰动)——如果 = O(1）——相位刚性（差额可读？）
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

# 相位扰动：γ_k → γ_k + ε·sin(γ_k)
print("相位扰动实验（γ → γ + ε·sin(γ)——只动相位）：")
print(f"{'n':>6} {'Δλ(ε=0.1)':>12} {'Δλ(ε=0.3)':>12} {'Δλ(ε=1.0)':>12} {'r(n)':>10}")
for n in [50, 100, 200, 500, 1000]:
    base = lam_n(n, z)
    rn = r_n(n, z)
    deltas = []
    for eps in [0.1, 0.3, 1.0]:
        z_p = z + eps*np.sin(z)
        deltas.append(lam_n(n, z_p) - base)
    print(f"{n:6d} {deltas[0]:+12.4f} {deltas[1]:+12.4f} {deltas[2]:+12.4f} {rn:+10.4f}")

# 关键：响应 vs 扰动大小（找非线性/相变）
print("\n响应 vs 扰动强度（n=100——找相变）：")
base = lam_n(100, z)
for eps in [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0]:
    z_p = z + eps*np.sin(z)
    dl = lam_n(100, z_p) - base
    print(f"  ε={eps:6.2f}: Δλ = {dl:+10.4f}  相对 = {dl/base*100:+.3f}%")

# 对比：随机扰动（噪声——非相位结构）
print("\n随机扰动（对照——噪声 vs 相位结构）：")
rng = np.random.default_rng(42)
base = lam_n(100, z)
for trial in range(3):
    z_p = z + 0.3*rng.standard_normal(len(z))
    dl = lam_n(100, z_p) - base
    print(f"  随机扰动 {trial+1}: Δλ = {dl:+10.4f}")

del z
gc.collect()
print("内存已释放")
