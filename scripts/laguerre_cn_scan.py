#!/usr/bin/env python3
"""验证 F(x) 的 Laguerre 系数 c_n 是否有界（大 n）——S₂(n) = −n·c_n + 正规化
c_n = ∫_0^∞ L_{n-1}(x)F(x)dx——F(x) = Σ_{m>e^x}Λ(m)/(m log m)
如果 c_n = O(1)——S₂(n) 的积分部分 ~ O(n)——正规化抵消——大数相消
"""
import numpy as np
import math
from math import comb, factorial, log

def L_m(x, m):
    # Laguerre 多项式——对大 m 用递推（避免组合爆炸）
    if m == 0: return np.ones_like(x)
    L0 = np.ones_like(x)
    L1 = 1 - x
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

Nmax = 2*10**6
lam = Lambda_upto(Nmax)
ms = np.arange(2, Nmax+1)
pref = np.cumsum(lam[2:Nmax+1] / (ms * np.log(ms)))
pref = np.concatenate([[0.0], pref])
Ptotal = pref[-1]

def F_fast(x):
    m0 = min(int(math.exp(x)), Nmax)
    if m0 < 2: return Ptotal
    return Ptotal - pref[m0-1]

# 用 Gauss-Laguerre 正交算 c_n 更准——但 F 在 [0, log Nmax] 有界——用梯形
# c_n = ∫_0^log(Nmax) L_{n-1}(x)F(x)dx（截断）
xmax = log(Nmax)
xs = np.linspace(0, xmax, 4000)
Fx = np.array([F_fast(x) for x in xs])

print(f"xmax = log({Nmax}) = {xmax:.2f}")
print("c_n = ∫L_{n-1}F——梯形积分（4000 点）：")
cvals = {}
for n in [1, 2, 3, 5, 8, 12, 20, 30, 50, 80, 120]:
    Lx = L_m(xs, n-1)
    cn = np.trapz(Lx*Fx, xs)
    cvals[n] = cn
    print(f"  n={n:3d}: c_n = {cn:+10.4f}  -n·c_n = {-n*cn:+12.4f}")

# 检查 c_n 的界（|c_n| 随 n）
print("\n|c_n| 随 n：")
for n in [1, 2, 3, 5, 8, 12, 20, 30, 50, 80, 120]:
    print(f"  n={n:3d}: |c_n| = {abs(cvals[n]):8.4f}")
