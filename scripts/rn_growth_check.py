#!/usr/bin/env python3
"""检查 r(n) 的数值增长——O(1)？O(log n)？O(n^{1/2})？
Arias ℓ² 判据只需要 r(n) = O(n^{1/2−ε})——弱化目标！
r(n) = λ_n − ½nlogn − cn——用 sin² 公式（β=½）——8/22 权威方法
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
Tmax = z[-1]

def th1(t):
    return np.arctan(1/(2*t))

# λ_n = 4Σsin²(nθ₁(γ_k))——到 γ_max + 尾部修正
# 尾部：∫_{γ_max}^∞ 4sin²(nθ₁)N₀' dt——f_n ~ n²/t²——尾部 = n²(log(T/2π)/T + 1/T)/(2π)
c = -1.13033070075  # ½(γ−1−log2π)

print("r(n) 的数值增长（sin² 公式——到 γ_1e6 + 尾部）：")
print(f"{'n':>6} {'λ_n':>14} {'主项':>14} {'r(n)':>10} {'log n':>8} {'√n':>8}")
for n in [50, 100, 200, 500, 1000, 2000, 5000]:
    lam = 4*np.sum(np.sin(n*th1(z))**2)
    # 尾部修正
    tail = n**2*(log(Tmax/(2*pi))/Tmax + 1/Tmax)/(2*pi)
    lam += tail
    main = 0.5*n*log(n) + c*n
    r = lam - main
    print(f"{n:6d} {lam:14.4f} {main:14.4f} {r:+10.4f} {log(n):8.3f} {n**0.5:8.1f}")

# 关键：r(n) 的增长拟合——O(1)？O(log n)？O(n^α)？
print("\nr(n) 增长拟合：")
ns = np.array([50, 100, 200, 500, 1000, 2000, 5000], dtype=float)
# 重算 r
rs = []
for n in ns:
    n = int(n)
    lam = 4*np.sum(np.sin(n*th1(z))**2) + n**2*(log(Tmax/(2*pi))/Tmax + 1/Tmax)/(2*pi)
    rs.append(lam - (0.5*n*log(n) + c*n))
rs = np.array(rs)
A = np.vstack([np.log(ns), np.ones(len(ns))]).T
coef = np.linalg.lstsq(A, np.log(np.abs(rs)), rcond=None)[0]
print(f"  log|r(n)| ≈ {coef[0]:.3f}·log n + {coef[1]:.3f}——r(n) ~ n^{coef[0]:.3f}")
print(f"  α = {coef[0]:.3f}（0 = O(1)——0.5 = O(√n)——需要 < 0.5 就够 ℓ²）")
