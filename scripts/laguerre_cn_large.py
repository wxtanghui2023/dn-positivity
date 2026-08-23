#!/usr/bin/env python3
"""F 的 Laguerre 谱：c_n = ∫L_{n-1}F——精确渐近检查
关键：−n·c_n 是否有界？——c_n ~ O(1/n)？——与 F 光滑性/RH 的关系
用更高的积分精度 + 更大 n
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

Nmax = 5*10**6
print(f"计算 Λ 到 {Nmax}...", flush=True)
lam = Lambda_upto(Nmax)
ms = np.arange(2, Nmax+1)
pref = np.cumsum(lam[2:Nmax+1] / (ms * np.log(ms)))
pref = np.concatenate([[0.0], pref])
Ptotal = pref[-1]
print(f"Ptotal = {Ptotal:.6f}")

def F_fast(x):
    m0 = min(int(math.exp(x)), Nmax)
    if m0 < 2: return Ptotal
    return Ptotal - pref[m0-1]

# c_n = ∫_0^∞ L_{n-1}(x)F(x)dx——F 在 [0, log Nmax]——尾部 F→0 快
# 但 L_{n-1}(x) 在 x~n 处振荡大——梯形点数要够
xmax = log(Nmax)
print(f"xmax = {xmax:.2f}")

# 对每个 n 用自适应网格（L_{n-1} 的振荡频率 ~ √n 在 x~n）
print("\nn·|c_n| 与 |c_n| 检查（8000 点）：")
xs = np.linspace(0, xmax, 8000)
Fx = np.array([F_fast(x) for x in xs])
for n in [2, 3, 5, 10, 20, 40, 60, 100, 150, 200, 300]:
    Lx = L_m(xs, n-1)
    cn = np.trapz(Lx*Fx, xs)
    print(f"  n={n:4d}: c_n={cn:+10.4f}  |c_n|={abs(cn):8.4f}  n|c_n|={n*abs(cn):9.3f}  -n·c_n={-n*cn:+10.3f}")

# 检查截断误差：x > xmax 的部分——F(x) ~ ?（素数定理——F 尾部）
# F(x) = Σ_{m>e^x}Λ(m)/(m log m)——尾部小（m 大——Λ(m)/(m log m) ~ 1/(m log²m)·...）
print("\n尾部贡献估计：F(14.5) =", F_fast(14.5), " F(13) =", F_fast(13))
