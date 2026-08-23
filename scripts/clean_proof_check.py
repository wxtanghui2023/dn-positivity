#!/usr/bin/env python3
"""验证干净证明：∫S·g = Σ S_k·g·Δγ + ΣE_k——三项都 O(1) 无条件
关键：g 绝对可积——不需要振荡抵消
"""
import numpy as np
import math
from math import log, pi

def g(t):
    t = np.asarray(t, dtype=float)
    return 2*pi/(t*np.log(t/(2*pi))**2)

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 500000
z = load_zeros(K)

def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

# S_k = k - N₀(γ_k)（零点处右极限）
S_k = np.array([(k+1) - N0(z[k]) for k in range(K)], dtype=float)

# 1. Σ S_k·g(γ_k)·Δγ_k
dg = np.diff(z)
g_k = g(z[:-1])
term1 = np.sum(S_k[:-1] * g_k * dg)
print(f"1. Σ S_k·g·Δγ = {term1:+.4f}")

# 1b. 用 mean(S)=½ + Abel 验证：(1/2)Σg·Δγ 的预测
half_sum = 0.5*np.sum(g_k*dg)
print(f"   (1/2)Σg·Δγ = {half_sum:+.4f}（mean(S)=½ 预测——差 {term1-half_sum:+.4f} 应 O(1)）")

# 2. 直接 ∫S·g（分段 Gauss——精确）
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
total = 0.0
for k in range(K-1):
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    total += 0.5*(b-a)*np.sum(wg*S_vals*g(ts))
print(f"2. 直接 ∫S·g = {total:+.4f}")

# 3. E_k = 每区间误差（∫(k−N₀)g − S_k·g(γ_k)·Δγ）
print(f"3. ΣE_k = ∫S·g − ΣS_k·g·Δγ = {total - term1:+.4f}（应 O(1)）")

# 4. ∫g dt（绝对可积）
from scipy.integrate import quad
val, err = quad(g, z[0], 1e7, limit=500)
print(f"4. ∫g dt = {val:.4f}（绝对可积——O(1)）")

# 5. Σ|E_k| 的界验证（|E_k| 的绝对值——是否收敛）
# E_k ≈ (1/2)∫(k−N₀)''g + ... —— 用数值差分
E_abs = 0.0
for k in range(0, K-1, 50):  # 采样
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    exact = 0.5*(b-a)*np.sum(wg*S_vals*g(ts))
    approx = S_k[k]*g(z[k])*(b-a)
    E_abs += abs(exact - approx)*50  # 补偿采样
print(f"5. Σ|E_k|（采样估计）≈ {E_abs:.4f}（绝对值收敛——O(1)）")
