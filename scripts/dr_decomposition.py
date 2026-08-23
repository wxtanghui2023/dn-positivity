#!/usr/bin/env python3
"""Δr = r(n+1) − r(n) 的分解——灾难抵消的"导数版"
Δr = 4Σθ₁·sin((2n+1)θ₁) − 主项差（~½log n）
验证：各部分量级——抵消结构——van der Corput 可行性
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

z = load_zeros(300000)

def th1(t):
    return np.arctan(1/(2*t))

def lam_n(n, z):
    return 4*np.sum(np.sin(n*th1(z))**2)

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

gamma_E = 0.5772156649015329
c = 0.5*(gamma_E - 1 - log(2*pi))

def main_n(n):
    return 0.5*n*log(n) + c*n

# Δr 分解
print("Δr 分解（n=100, 500——各分量）：")
for n in [100, 500]:
    # λ 增量
    dl = lam_n(n+1, z) - lam_n(n, z)
    # 主项差
    dm = main_n(n+1) - main_n(n)
    # Δr
    dr = dl - dm
    # sin² 差分解：4Σ[sin²((n+1)θ₁)−sin²(nθ₁)] = 4Σsin((2n+1)θ₁)sin(θ₁)
    th = th1(z)
    sin_diff = 4*np.sum(np.sin((2*n+1)*th)*np.sin(th))
    # 近似：4Σθ₁·sin((2n+1)θ₁)
    approx = 4*np.sum(th*np.sin((2*n+1)*th))
    print(f"\n  n={n}: Δλ = {dl:+.4f}  主项差 = {dm:+.4f}  Δr = {dr:+.4f}")
    print(f"    sin²差（精确）= {sin_diff:+.4f}（vs Δλ {dl:+.4f}——差 {abs(sin_diff-dl):.2e}）")
    print(f"    θ₁近似 = {approx:+.4f}")

# 主项部分：∫θ₁·sin((2n+1)θ₁)N₀'——van der Corput 可行性
print("\n∫θ₁·sin((2n+1)θ₁)N₀'（主项——van der Corput）：")
from scipy.integrate import quad
for n in [100, 500]:
    integ, err = quad(lambda t: np.arctan(1/(2*t))*np.sin((2*n+1)*np.arctan(1/(2*t)))*N0p(t),
                      z[0], z[-1], limit=2000)
    print(f"  n={n}: ∫θ₁sinN₀' = {integ:+.4f}")

# 关键：θ₁·N₀' 的可积性（van der Corput 权重）
print("\nθ₁·N₀' 的可积性（尾部）：")
for t in [100, 1000, 10000, 100000]:
    val = np.arctan(1/(2*t))*N0p(t)
    print(f"  t={t:7d}: θ₁N₀' = {val:.6e}（θ₁~1/2t——N₀'~logt——乘积~logt/t——可积）")

del z
gc.collect()
print("内存已释放")
