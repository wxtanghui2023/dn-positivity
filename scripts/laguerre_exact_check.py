#!/usr/bin/env python3
"""修正 Laguerre 谱验证——含尾部——确认 S₂(n) = −n·c_n + 正规化
F 尾部（x > xmax）：F(x) = Σ_{m>e^x}Λ(m)/(m log m)——尾部小但 L_{n-1} ~ e^{x/2} 增长
用更大的 Nmax + 直接比较 S₂ 的完整形式
关键：验证 S₂(n)（Euler 积——Nmax 截断）与 −n·c_n(Nmax) + 正规化(Nmax) 的一致性
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

xmax = log(Nmax)

# 精确的交换关系：S₂(N) = Σ_{m≤N}Λ(m)/m·Q_n(log m)
# = −n·∫_0^{log N} L_{n-1}(x)·F_N(x)dx（F_N 是截断版本）
# 其中 F_N(x) = Σ_{e^x < m ≤ N} Λ(m)/(m log m)
# 验证：对每个 n，两个表达式应一致（差 = 离散化误差）
print("验证交换恒等式（离散 → 积分——精确）：")
for n in [2, 3, 5]:
    # 直接
    direct = sum(lam[m]/m * (-n*sum(comb(n-1,k)*(-1)**k*log(m)**k/factorial(k+1) for k in range(n))) for m in range(2, Nmax+1))
    # 积分形式——用更精确的梯形（4000 点）
    xs = np.linspace(0, xmax, 4000)
    Fx = np.array([F_fast(x) for x in xs])
    Lx = L_m(xs, n-1)
    integ = np.trapz(Lx*Fx, xs)
    print(f"  n={n}: 直接 Σ={direct:+10.4f} vs −n∫LF={-n*integ:+10.4f}（差 {abs(direct+n*integ):.4f}）")

# S₂ 完整值（正规化后）与"积分部分+正规化"的关系
print("\nS₂(n) 分解（N=2e6）：")
for n in [5, 10, 20]:
    xs = np.linspace(0, xmax, 6000)
    Fx = np.array([F_fast(x) for x in xs])
    Lx = L_m(xs, n-1)
    cn = np.trapz(Lx*Fx, xs)
    int_part = -n*cn
    reg = sum(comb(n,j)*(-1)**j*log(Nmax)**j/factorial(j) for j in range(1, n+1))
    # S₂ 直接
    direct = sum(lam[m]/m * (-n*sum(comb(n-1,k)*(-1)**k*log(m)**k/factorial(k+1) for k in range(n))) for m in range(2, Nmax+1))
    s2 = direct - reg
    print(f"  n={n:2d}: 积分={int_part:+10.4f} 正规化={reg:+10.4f} 积分+正规化={int_part+reg:+10.4f} S₂={s2:+8.4f} 差={abs(int_part+reg-s2):.4f}")
