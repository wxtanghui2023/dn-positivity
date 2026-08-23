#!/usr/bin/env python3
"""关键实验：c_n = O(1/n) 的来源——F 的光滑主项 vs 阶梯跳跃？
构造模型 F 对比真实 F：
1. F_smooth：光滑近似（模拟素数定理主项——缓变递减）
2. F_real：真实 F（阶梯——跳跃在 log m）
如果 F_smooth 的 Laguerre 系数也 O(1/n)——衰减来自缓变（可严格化）
如果不同——来自跳跃结构
"""
import numpy as np
import math
from math import comb, factorial, log

def L_m(x, m):
    if m == 0: return np.ones_like(x)
    L0 = np.ones_like(x); L1 = 1 - x
    if m == 1: return L1
    for k in range(2, m+1):
        L2 = ((2*k-1-x)*L1 - (k-1)*L0)/k
        L0, L1 = L1, L2
    return L1

def Lambda_upto(N):
    lam = np.zeros(N+1)
    sieve = np.ones(N+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(N**0.5)+1):
        if sieve[i]: sieve[i*i::i] = False
    primes = np.nonzero(sieve)[0]
    for p in primes:
        pk = p
        while pk <= N:
            lam[pk] += log(p)
            pk *= p
    return lam

Nmax = 10**6
lam = Lambda_upto(Nmax)
ms = np.arange(2, Nmax+1)
pref = np.cumsum(lam[2:Nmax+1] / (ms * np.log(ms)))
pref = np.concatenate([[0.0], pref])
Ptotal = pref[-1]

def F_fast(x):
    m0 = min(int(math.exp(x)), Nmax)
    if m0 < 2: return Ptotal
    return Ptotal - pref[m0-1]

xmax = log(Nmax)

# 模型 1：F_smooth(x) = C − log(1+x)（缓变——模拟素数定理主项）
# F(x) 从 3.2 到 0（x=0 到 14.5）——log(1+x) 从 0 到 2.74——C = 3.2
C = 3.2
def F_smooth(x):
    return C - log(1+x)  # 单调递减——类似 F 的缓变

# 模型 2：F_exp(x) = C·e^{-x/5}（指数衰减——另一种缓变）
def F_exp(x):
    return C*math.exp(-x/5)

# 模型 3：F_power(x) = C/(1+x)^0.5（幂衰减）
def F_power(x):
    return C/(1+x)**0.5

print("Laguerre 系数对比（6000 点梯形——[0, xmax]）：")
xs = np.linspace(0, xmax, 6000)
F_real = np.array([F_fast(x) for x in xs])
F_sm = np.array([F_smooth(x) for x in xs])
F_ex = np.array([F_exp(x) for x in xs])
F_pw = np.array([F_power(x) for x in xs])

print(f"{'n':>5} | {'真实F c_n':>12} {'n|c_n|':>8} | {'光滑 c_n':>10} {'n|c_n|':>8} | {'指数 c_n':>10} {'n|c_n|':>8} | {'幂 c_n':>10} {'n|c_n|':>8}")
for n in [2, 5, 10, 20, 40, 80, 150, 300]:
    Lx = L_m(xs, n-1)
    cr = np.trapz(Lx*F_real, xs)
    cs = np.trapz(Lx*F_sm, xs)
    ce = np.trapz(Lx*F_ex, xs)
    cp = np.trapz(Lx*F_pw, xs)
    print(f"{n:5d} | {cr:+12.4f} {n*abs(cr):8.2f} | {cs:+10.4f} {n*abs(cs):8.2f} | {ce:+10.4f} {n*abs(ce):8.2f} | {cp:+10.4f} {n*abs(cp):8.2f}")
