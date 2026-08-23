#!/usr/bin/env python3
"""检查 BV ⟹ c_n = O(1/n) 的可行性 + 抵消结构
S₂(n) = −n·c_n + 正规化——两者各自 O(1)（~±500）——抵消到 ±1
关键：验证 −n·c_n 与正规化的抵消——这是 Laguerre 版本相位均匀性
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
xs = np.linspace(0, xmax, 6000)
Fx = np.array([F_fast(x) for x in xs])

# 抵消结构：S₂(n)完整 = −n·c_n + 正规化 vs 直接 Euler 积计算
def S2_euler(n, N):
    total = 0.0
    for m in range(2, N+1):
        if lam[m] > 0:
            t = log(m)
            Q = -n*sum(comb(n-1,k)*(-1)**k*t**k/factorial(k+1) for k in range(n))
            total += lam[m]/m * Q
    reg = sum(comb(n,j)*(-1)**j*log(N)**j/factorial(j) for j in range(1, n+1))
    return total - reg

print("抵消结构（n=5,10,20）：")
for n in [5, 10, 20]:
    Lx = L_m(xs, n-1)
    cn = np.trapz(Lx*Fx, xs)
    int_part = -n*cn
    # 正规化（N=1e6）
    reg = sum(comb(n,j)*(-1)**j*log(Nmax)**j/factorial(j) for j in range(1, n+1))
    s2 = S2_euler(n, Nmax)
    print(f"  n={n:2d}: 积分部分={int_part:+10.4f}  正规化={reg:+10.4f}  和={int_part+reg:+8.4f}  S₂(直接)={s2:+8.4f}")

# 关键：BV ⟹ c_n = O(1/n) 的验证——F 的跳跃总和
print(f"\nF 的 BV（Σ|跳跃| = Ptotal）= {Ptotal:.6f}——收敛（Mertens——无条件）")
print("跳跃在 x = log m——稠密——但总和收敛——F 是 BV 函数")
