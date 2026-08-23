#!/usr/bin/env python3
"""验证 f_n 核 Abel 项：Σ 4sin²(nθ₁(γ_k))·N₀'(γ_k)·δ_k 的数值行为
这是 r(n) = O(1) 的 Abel 项（未证——需要 δ 强抵消）
如果数值 O(1)——目标确认；如果增长——r(n) = O(1) 的数值基础需重新检查
"""
import numpy as np

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def N0p(t):
    return np.log(t/(2*np.pi))/(2*np.pi)

def th1(t):
    return np.arctan(1/(2*t))

def fn(t, n):
    return 4*np.sin(n*th1(t))**2

K = 2000000
z = load_zeros(K)

# δ_k = Δγ_k - 1/N₀'(γ_k)
dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np

print(f"{'n':>6} {'Sum fn*Np*delta':>14} {'max|partial|':>12} {'Sum|contrib|':>14}")
for n in [50, 100, 200, 500, 1000, 2000, 3000]:
    w = fn(z[:-1], n) * Np
    contrib = w * delta
    S = np.cumsum(contrib)
    print(f"{n:6d} {S[-1]:+14.4f} {np.max(np.abs(S)):12.4f} {np.sum(np.abs(contrib)):14.2f}")
