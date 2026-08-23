#!/usr/bin/env python3
"""验证 S₂(n) = −n∫_0^∞ L_{n-1}(x)F(x)dx 的 Laguerre 积分形式
F(x) = Σ_{m>e^x} Λ(m)/(m log m)——素数和的缓变函数
S₂(n) = Σ_m Λ(m)/m·Q_n(log m) − 正规化
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

# 计算 F(x) = Σ_{m>e^x} Λ(m)/(m log m)——对给定 x
Nmax = 10**6
lam = Lambda_upto(Nmax)
# 预计算 F 在 x 网格上的值
# F(x) = Σ_{m > e^x, m≤Nmax} Λ(m)/(m log m) + 尾部（忽略——Nmax 截断）
def F(x, Nmax=Nmax):
    m0 = max(int(math.exp(x))+1, 2)
    if m0 > Nmax: return 0.0
    ms = np.arange(m0, Nmax+1)
    return np.sum(lam[m0:Nmax+1] / (ms * np.log(ms)))

# 验证 S₂(n) = Σ_m Λ(m)/m·Q_n(log m) vs −n∫L_{n-1}F dx（截断）
print("验证 Laguerre 积分形式（截断 Nmax=1e6）：")
for n in [2, 3, 5]:
    # 直接：Σ_{m≤Nmax} Λ(m)/m·Q_n(log m)
    ms = np.arange(2, Nmax+1)
    direct = np.sum(lam[2:Nmax+1]/ms * np.array([Qn(log(m), n) for m in ms]))
    # 积分形式：−n∫_0^{log Nmax} L_{n-1}(x)F(x)dx
    xs = np.linspace(0, log(Nmax), 500)
    Fx = np.array([F(x) for x in xs])
    Lx = np.array([L_m(x, n-1) for x in xs])
    integ = np.trapz(Lx*Fx, xs)
    print(f"  n={n}: 直接 Σ={direct:+.4f} vs −n∫LF={-n*integ:+.4f}（差 {abs(direct+n*integ):.4f}）")

# F(x) 的行为
print("\nF(x) 的行为（Nmax=1e6）：")
for x in [0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 10.0]:
    print(f"  F({x:.1f}) = {F(x):+.6f}")

# F 的 Laguerre 系数：∫L_{n-1}F——看衰减
print("\nF 的 Laguerre 系数 c_n = ∫L_{n-1}(x)F(x)dx：")
xs = np.linspace(0, log(Nmax), 2000)
Fx = np.array([F(x) for x in xs])
for n in [1, 2, 3, 5, 8, 12, 20]:
    Lx = np.array([L_m(x, n-1) for x in xs])
    cn = np.trapz(Lx*Fx, xs)
    print(f"  n={n}: c_n = {cn:+.6f}  （−n·c_n 应 ≈ S₂ 的积分部分）")
