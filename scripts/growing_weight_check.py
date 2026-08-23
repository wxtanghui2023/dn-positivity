#!/usr/bin/env python3
"""真正检验"完全刚性"：不衰减权重的 Σwδ
w = log γ（增长——不衰减）——如果 Σwδ 仍 O(1)——完全刚性极强
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

# 不同增长权重——逐点累积
tests = {
    "log γ": np.log(z[:-1]),
    "sqrt log γ": np.sqrt(np.log(z[:-1])),
    "1/log γ": 1.0/np.log(z[:-1]),
    "N₀' (log γ/2π)": Np,
}

for name, w in tests.items():
    S = 0.0; mx = 0.0
    pts = []
    for i in range(len(delta)):
        S += w[i]*delta[i]
        if abs(S) > mx: mx = abs(S)
        if i in [999, 9999, 99999, 499999, 999999, 1999998]:
            pts.append((i+1, S, mx))
    print(f"\n{name}:")
    for N, Sv, m in pts:
        print(f"  N={N:8d}: Σwδ = {Sv:+10.3f}  max = {m:10.3f}")
