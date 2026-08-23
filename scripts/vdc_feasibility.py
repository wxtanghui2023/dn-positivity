#!/usr/bin/env python3
"""验证 ΣΔw·A_k 的 van der Corput 可行性——目标 r(n) = O(n^{1/2−ε})
ΣΔw·A_k = Σ sin(2nθ₁(γ_k))·g_k·A_k——φ_k = 2nθ₁ 单调——van der Corput 二阶
数值：|ΣΔw·A_k| 随 n 的增长——是否 ~ O(√n) 或更小？
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
def th1(t):
    return np.arctan(1/(2*t))

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np
Sd = np.cumsum(delta)
A_inf = Sd[-1]

print("ΣΔw·A_k 的增长（r(n) Abel 项——目标 O(n^{1/2−ε})）：")
print(f"{'n':>6} {'ΣΔw·A':>12} {'log|·|':>8} {'0.5log n':>8} {'log n':>8}")
res = []
for n in [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    Ak = Sd[:len(dw)]
    S_wa = np.sum(dw * Ak)
    res.append((n, abs(S_wa)))
    print(f"{n:6d} {S_wa:+12.4f} {log(abs(S_wa)):8.3f} {0.5*log(n):8.3f} {log(n):8.3f}")

# 拟合
ns = np.array([r[0] for r in res], dtype=float)
vals = np.array([max(r[1], 1e-10) for r in res], dtype=float)
A = np.vstack([np.log(ns), np.ones(len(ns))]).T
coef = np.linalg.lstsq(A, np.log(vals), rcond=None)[0]
print(f"\nlog|ΣΔw·A| ≈ {coef[0]:.3f}·log n——α = {coef[0]:.3f}")
print(f"目标：α < 0.5（O(n^{{1/2−ε}}) 就够 ℓ² ⟹ RH）")
