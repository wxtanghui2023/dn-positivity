#!/usr/bin/env python3
"""ρ₁ 的解析路径：从 S 的自协方差（γ(0), γ(1), γ(2)）
ρ₁ = (2γ(1)−γ(0)−γ(2))/(2γ(0)−2γ(1))——AR(1): ρ₁ = (2φ−1−φ²)/(2−2φ)
验证 + 从 Selberg/Tsang 矩推导 φ 的解析值
"""
import numpy as np
import gc
from math import log, pi, asin, sqrt

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)

def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

S_k = np.array([(k+1) - N0(z[k]) for k in range(1000000)], dtype=float)
del z
gc.collect()

# 1. S 的自协方差（数值）
s = S_k - np.mean(S_k)
g0 = np.var(s)
g1 = np.mean(s[:-1]*s[1:])
g2 = np.mean(s[:-2]*s[2:])
print(f"S 的自协方差：γ(0) = {g0:.6f}  γ(1) = {g1:.6f}  γ(2) = {g2:.6f}")
print(f"φ = γ(1)/γ(0) = {g1/g0:.6f}")

# 2. ρ₁ 公式验证
rho1_formula = (2*g1 - g0 - g2)/(2*g0 - 2*g1)
print(f"\nρ₁（公式）= {rho1_formula:.6f}")

# 直接测量 ρ₁（δ 的）
gz = None
# 重新加载 δ
z2 = load_zeros(1000000)
dg = np.diff(z2)
Np = np.log(z2[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del dg, Np, z2
gc.collect()
d = delta - np.mean(delta)
s2d = np.var(d)
rho1_direct = np.mean(d[:-1]*d[1:])/s2d
print(f"ρ₁（δ 直接）= {rho1_direct:.6f}（差 {abs(rho1_formula-rho1_direct):.5f}）")

# AR(1) 预测：ρ₁ = (2φ−1−φ²)/(2−2φ)
phi = g1/g0
rho1_ar1 = (2*phi - 1 - phi**2)/(2 - 2*phi)
print(f"AR(1) 预测 ρ₁ = {rho1_ar1:.6f}（φ = {phi:.4f}）")
print(f"arcsin p（AR1 ρ₁）= {0.5 - asin(rho1_ar1)/pi:.6f}")
print(f"arcsin p（实测 ρ₁）= {0.5 - asin(rho1_direct)/pi:.6f}")
print(f"实际 p = {np.mean(np.sign(delta[:-1]) != np.sign(delta[1:])):.6f}")

# 3. 从 Selberg 矩推导 γ(0)（无条件）
# Var(S) ~ (1/2π²)·log log T（Selberg）
T = 1000000
gamma0_selberg = (1/(2*pi*pi))*log(log(T))
print(f"\nSelberg 预测 γ(0) = {gamma0_selberg:.6f} vs 实测 {g0:.6f}")

# 4. φ 的解析值？——黄金比例测试
# 如果 p = 1/φ（黄金比例）——ρ₁ = −sin(π(1/φ − 1/2)) = −sin(π·0.11803) = ?
target_p = (sqrt(5)-1)/2
rho1_target = -np.sin(pi*(target_p - 0.5))
print(f"\n黄金比例 p = {target_p:.6f} → ρ₁_target = {rho1_target:.6f}（实测 {rho1_direct:.6f}）")

del delta, d, s, S_k
gc.collect()
print("内存已释放")
