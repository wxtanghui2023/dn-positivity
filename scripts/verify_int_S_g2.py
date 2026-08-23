#!/usr/bin/env python3
"""修正版：∫S·g = O(1) 验证——从 γ₁ 积分（避开 g 在 2π 的奇点）
g(t) = 2π/(t log²(t/2π))——t=2π 处发散——但 S 定义域 t ≥ γ₁ = 14.13
"""
import numpy as np
import math
from math import log, pi
from scipy.integrate import quad

def g(t):
    return 2*pi/(t*np.log(t/(2*pi))**2)

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

G1 = 14.134725142

# 1. ∫_{max(p,γ₁)}^∞ sin(t log p)g(t)dt——van der Corput 界
print("∫_{max(p,γ₁)}^∞ sin(t log p)g(t)dt（从 γ₁ 开始——避开奇点）：")
for p in [2, 3, 5, 11, 101, 1009]:
    lo = max(p, G1)
    val, err = quad(lambda t: np.sin(t*log(p))*g(t), lo, 2e6, limit=2000)
    # 尾部 t>2e6：g ~ 2π/(t log²t)——振荡积分 ~ O(1/(2e6·log²2e6·log p))
    tail = 2*pi/(2e6*log(2e6)**2)/log(p)
    # van der Corput 一阶：|∫| ≤ |g(lo)|/log p + ∫|g'|/log p
    g_lo = 2*pi/(lo*log(lo/(2*pi))**2)
    vdc = (g_lo + 2*pi/(lo*log(lo/(2*pi))**2))/log(p)  # 粗略
    print(f"  p={p:5d}: ∫ = {val:+.4f}  （vdc 界 ~ {vdc:.4f}——比值 {abs(val)/max(vdc,1e-20):.3f}）")

# 2. ∫S·g dt 数值（分段——从 γ₁）
print("\n∫S·g dt（分段——S(t) = k − N₀(t) on [γ_k, γ_{k+1})——从 γ₁ 到 γ_500k）：")
z = load_zeros(500000)
def N0(t):
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
total = 0.0
for k in range(len(z)-1):
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    total += 0.5*(b-a)*np.sum(wg*S_vals*g(ts))
print(f"  ∫S·g（到 γ_500k）≈ {total:+.4f}（8/23 声称 +0.1313）")

# 3. Σδ_k 与 ∫S·g 的关联
print("\nΣδ_k 验证：")
dg = np.diff(z)
Np = np.log(z[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np
Sd = np.cumsum(delta)
print(f"  max|Σδ_k| = {np.max(np.abs(Sd)):.3f}（若 ∫S·g = O(1) → Σδ = O(1)）")
