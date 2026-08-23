#!/usr/bin/env python3
"""验证"完全刚性"推论：Σwδ = O(1)（对缓变 w）？
如果 δ 的累积从不增长（H=0）——缓变加权的和应该也 O(1)
测试：不同权重的 Σwδ 随 N 的标度
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

K = 2000000
z = load_zeros(K)

def N0p(t):
    t = np.asarray(t, dtype=float)
    return np.log(t/(2*pi))/(2*pi)

def th1(t):
    return np.arctan(1/(2*t))

dg = np.diff(z)
Np = N0p(z[:-1])
delta = dg - 1.0/Np

# 不同权重
def w_g(t):  # 缓变绝对可积
    return 2*pi/(t*np.log(t/(2*pi))**2)

def w_fn(t, n):  # f_n 核
    return 4*np.sin(n*th1(t))**2 * N0p(t)

def w_const(t):
    return np.ones_like(t)

print("不同权重的 Σwδ 随 N 的标度（H 拟合）：")
for name, wfun in [("g(可积)", w_g), ("f_100核", lambda t: w_fn(t, 100)), ("f_1000核", lambda t: w_fn(t, 1000)), ("常数", w_const)]:
    w = wfun(z[:-1])
    contrib = w * delta
    S = np.cumsum(contrib)
    Ns = np.array([10**4, 10**5, 5*10**5, 10**6, 2*10**6], dtype=float)
    mxs = np.array([np.max(np.abs(S[:int(N)])) for N in Ns], dtype=float)
    A = np.vstack([np.log(Ns), np.ones(len(Ns))]).T
    coef = np.linalg.lstsq(A, np.log(mxs), rcond=None)[0]
    print(f"  {name:12s}: max|Σwδ| = {mxs[-1]:8.3f}  H = {coef[0]:+.3f}  （最终值 {S[-1]:+.3f}）")

# 关键：f_n 核的 Σwδ 是否真的 O(1)（H≈0）？
print("\nf_n 核 Σwδ 的详细（n=100——不同 N）：")
w = w_fn(z[:-1], 100)
S = np.cumsum(w*delta)
for N in [10**4, 10**5, 5*10**5, 10**6, 2*10**6]:
    print(f"  N={N:8d}: max|Σwδ| = {np.max(np.abs(S[:int(N)])):8.3f}")
