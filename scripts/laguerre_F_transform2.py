#!/usr/bin/env python3
"""验证 S₂(n) = -n∫L_{n-1}(x)F(x)dx——前缀和优化版
F(x) = Σ_{m>e^x} Λ(m)/(m log m) = F(0) - Σ_{m≤e^x} Λ(m)/(m log m)
"""
import numpy as np
import math
from math import comb, factorial, log

def Qn(t, n):
    s = sum(comb(n-1,k)*(-1)**k*t**k/factorial(k+1) for k in range(n))
    return -n*s

def L_m(x, m):
    return sum(comb(m,k)*(-x)**k/factorial(k) for k in range(m+1))

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
# 前缀和 P(m) = Σ_{j≤m} Λ(j)/(j log j)
pref = np.cumsum(lam[2:Nmax+1] / (ms * np.log(ms)))
pref = np.concatenate([[0.0], pref])  # pref[i] = Σ_{j≤i+1}... 对齐
# F(x) = Σ_{m>e^x} = P(Nmax) - P(e^x)
Ptotal = pref[-1]

def F_fast(x):
    m0 = min(int(math.exp(x)), Nmax)
    if m0 < 2: return Ptotal
    return Ptotal - pref[m0-1]  # pref[m0-1] = Σ_{j≤m0}

print(f"Ptotal = Σ_{'{m≤1e6}'} Λ(m)/(m log m) = {Ptotal:.6f}")
print("\n验证 Laguerre 积分形式：")
for n in [2, 3, 5]:
    direct = np.sum(lam[2:Nmax+1]/ms * np.array([Qn(log(m), n) for m in ms]))
    xs = np.linspace(0, log(Nmax), 2000)
    Fx = np.array([F_fast(x) for x in xs])
    Lx = np.array([L_m(x, n-1) for x in xs])
    integ = np.trapz(Lx*Fx, xs)
    print(f"  n={n}: 直接 Σ={direct:+.4f} vs -n∫LF={-n*integ:+.4f}（差 {abs(direct+n*integ):.4f}）")

print("\nF(x) 行为：")
for x in [0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 10.0, 12.0]:
    print(f"  F({x:5.1f}) = {F_fast(x):+.6f}")

print("\nF 的 Laguerre 系数 c_n = ∫L_{n-1}(x)F(x)dx（2000 点）：")
xs = np.linspace(0, log(Nmax), 2000)
Fx = np.array([F_fast(x) for x in xs])
for n in [1, 2, 3, 5, 8, 12, 20]:
    Lx = np.array([L_m(x, n-1) for x in xs])
    cn = np.trapz(Lx*Fx, xs)
    print(f"  n={n}: c_n = {cn:+.6f}  （-n·c_n = {-n*cn:+.4f}）")
