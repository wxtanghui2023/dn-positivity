#!/usr/bin/env python3
"""新攻击框架：Σw_kδ_k = ∫w dS = [wS] − ∫S·w' dt（部分积分——Stieltjes）
对 w → 0 且 w' 绝对可积的权重——Titchmarsh + van der Corput → O(1)？
f_n 核：w(t) = 4sin²(nθ₁(t))——w' ~ n·sin(2nθ₁)·θ₁'——变差 O(n)——需要振荡抵消
"""
import numpy as np
import math
from math import log, pi
from scipy.integrate import quad

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
def th1(t):
    return np.arctan(1/(2*t))

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np

# 1. 恒等式检查：Σwδ = ∫w dS（数值）
for n in [100, 500]:
    w_k = 4*np.sin(n*th1(z[:-1]))**2
    S_wd = np.sum(w_k * delta)
    
    # ∫w dS = Σ w(γ_k) - ∫w N₀' dt（黎曼和差）
    # = Σw(γ_k) - ∫w N₀' dt
    def w_func(t):
        return 4*np.sin(n*np.arctan(1/(2*t)))**2
    from numpy.polynomial.legendre import leggauss
    xg, wg = leggauss(8)
    total = 0.0
    for k in range(len(z)-1):
        a, b = z[k], z[k+1]
        ts = 0.5*(b-a)*xg + 0.5*(a+b)
        total += 0.5*(b-a)*np.sum(wg*w_func(ts)*N0p(ts))
    # 尾部
    tail = n**2*(np.log(z[-1]/(2*pi))/z[-1] + 1/z[-1])/(2*pi)
    int_wNp = total + tail
    S_w = np.sum(w_func(z))
    int_wdS = S_w - int_wNp  # ∫w dS = Σw - ∫w N₀' dt
    print(f"n={n}: Σwδ = {S_wd:+.4f}  vs  ∫w dS = {int_wdS:+.4f}（差 {abs(S_wd-int_wdS):.4f}）")

# 2. ∫S w' dt（部分积分形式——数值）
print("\n∫S·w' dt 检查（部分积分——[wS] − ∫S w'）：")
for n in [100, 500]:
    def w_func(t):
        return 4*np.sin(n*np.arctan(1/(2*t)))**2
    def wp_func(t):
        # w' = 4·2sin(nθ₁)cos(nθ₁)·nθ₁' = 4n·sin(2nθ₁)·θ₁'
        th = np.arctan(1/(2*t))
        thp = -2/(4*t*t+1)
        return 4*n*math.sin(2*n*th)*thp
    # ∫S w' dt——分段（S = k - N₀）
    def N0(t):
        return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8
    from numpy.polynomial.legendre import leggauss
    xg, wg = leggauss(8)
    total = 0.0
    for k in range(len(z)-1):
        a, b = z[k], z[k+1]
        ts = 0.5*(b-a)*xg + 0.5*(a+b)
        S_vals = (k+1) - N0(ts)
        total += 0.5*(b-a)*np.sum(wg*S_vals*wp_func(ts))
    print(f"  n={n}: ∫S w' dt = {total:+.4f}")
