#!/usr/bin/env python3
"""素数的 Laguerre 指数和——c_n = O(1/n) 的直接机制
c_n = Σ_m Λ(m)/(m log m)·∫_0^{log m} L_{n-1}(x)dx
   = −(1/n)·Σ_m Λ(m)/m·Q_n(log m)（Q_n 定义——平凡）
但更有启发性：c_n ≈ Σ_m [Λ(m)/(m log m)]·[L 的积分]——跳跃 × Laguerre 振荡

关键：跳跃的"相位"——L_{n-1}(log m) 作为 m 的函数振荡（频率 ~ √(n log m)）
素数的稀疏性（Λ 只在素数幂非零）+ Laguerre 振荡 → 抵消
对比：无跳跃模型（光滑）不抵消
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

# 直接：c_n = −(1/n)·Σ_m Λ(m)/m·Q_n(log m)
def Qn(t, n):
    s = sum(comb(n-1,k)*(-1)**k*t**k/factorial(k+1) for k in range(n))
    return -n*s

print("素数的 Laguerre 指数和——部分和结构（n=20）：")
n = 20
# S(M) = Σ_{m≤M} Λ(m)/(m log m)·∫_0^{log m}L_{n-1}(x)dx 的部分和
# 用积分近似 ∫L = 数值（每 m 太慢）——用 Q_n 关系：∫_0^{log m}L = −(log m/n)Q_n(log m)
# c_n(M) = Σ_{m≤M} Λ(m)/(m log m)·(−log m/n)·Q_n(log m) = −(1/n)Σ_{m≤M}Λ(m)/m·Q_n(log m)
partial = []
cum = 0.0
for m in range(2, Nmax+1):
    if lam[m] > 0:
        t = log(m)
        Q = Qn(t, n)
        cum += lam[m]/m * Q
        partial.append((m, cum))
# 采样显示部分和
print(f"  n={n}: 部分和 ΣΛ/m·Q_n 的演化（应收敛到 −n·c_n）：")
for idx in [0, 9, 99, 999, 9999, len(partial)-1]:
    m, cum = partial[idx]
    print(f"    m≤{m:8d}: Σ = {cum:+12.4f}")

# 完整 c_n vs 积分
print(f"\n  c_n(直接) = {-(cum/n):+.6f} vs c_n(积分) 之前算的")

# 关键：L_{n-1}(log m) 的振荡——跳跃的相位
print("\nL_{n-1}(log m) 的振荡（n=20——m 变化）：")
for m in [2, 3, 5, 10, 50, 100, 500, 1000]:
    Lv = L_m(np.array([log(m)]), n-1)[0]
    print(f"    m={m:5d}: L_19(log m) = {Lv:+.6f}")
