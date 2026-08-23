#!/usr/bin/env python3
"""更大 n 确认：ΣΔw·A_k 是否真的 < O(n^{1/2})？——van der Corput 可行性
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

z = load_zeros(2000000)

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np
Sd = np.cumsum(delta)

print("ΣΔw·A_k 更大 n（N=2e6）：")
print(f"{'n':>7} {'ΣΔw·A':>12} {'|·|/√n':>10} {'|·|/log n':>10}")
res = []
for n in [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]:
    th = 2*np.arctan(2*z[:-1]) - pi
    w = 1 - np.cos(n*th)
    dw = np.diff(w)
    Ak = Sd[:len(dw)]
    S_wa = np.sum(dw * Ak)
    res.append((n, abs(S_wa)))
    print(f"{n:7d} {S_wa:+12.4f} {abs(S_wa)/n**0.5:10.4f} {abs(S_wa)/log(n):10.3f}")

ns = np.array([r[0] for r in res], dtype=float)
vals = np.array([max(r[1], 1e-10) for r in res], dtype=float)
A = np.vstack([np.log(ns), np.ones(len(ns))]).T
coef = np.linalg.lstsq(A, np.log(vals), rcond=None)[0]
print(f"\nlog|ΣΔw·A| ≈ {coef[0]:.3f}·log n——α = {coef[0]:.3f}")
print(f"目标：α < 0.5（严格）——van der Corput 二阶典型界 O(√n·log)（α=0.5+ε）")
