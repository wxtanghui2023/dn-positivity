#!/usr/bin/env python3
"""决定性检查：f_n 核的 Σwδ 对所有 n 是否一致 O(1)？
r(n) = O(1) 的核心数值——如果所有 n 平台——数值基础稳固
逐点累积（避免 cumsum 精度问题）
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
def th1(t):
    return np.arctan(1/(2*t))

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np

print("f_n 核 Σwδ 对所有 n（N=2e6——逐点累积）：")
print(f"{'n':>6} {'Σwδ':>10} {'max|Σwδ|':>10}")
for n in [10, 50, 100, 200, 500, 1000, 2000, 3000, 5000]:
    w = 4*np.sin(n*th1(z[:-1]))**2 * Np
    S = 0.0; mx = 0.0
    for i in range(len(delta)):
        S += w[i]*delta[i]
        if abs(S) > mx: mx = abs(S)
    print(f"{n:6d} {S:+10.4f} {mx:10.4f}")
