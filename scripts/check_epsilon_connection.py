#!/usr/bin/env python3
"""检查 Σε 与 Σ_p A_p·Σ_k sin(γ_k log p) 的关系（8/23 日志：p≤100 和 = +1.42 与 Σε ±1.7 同量级）
A_p = 1/(√p log p)（Titchmarsh S 的素数项系数）
S(γ_k) ≈ -(1/π)Σ_p sin(γ_k log p)/(√p log p)——S 的素数表示
问题：Σ_p A_p·Σ_k sin(γ_k log p)（交换序）是否 O(1)？——决定 r(n) 路径
"""
import numpy as np
import math

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 2000000
z = load_zeros(K)

# 素数列表
def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i] = False
    return np.nonzero(sieve)[0]

# 计算 Σ_p A_p·Σ_k sin(γ_k log p) for p ≤ Pmax
print("p 累积贡献 Σ_p A_p·Σ_k sin(γ_k log p)：")
for Pmax in [20, 50, 100, 200, 500, 1000, 2000]:
    ps = primes_upto(Pmax)
    total = 0.0
    for p in ps:
        x = math.log(p)
        Ssin = np.sum(np.sin(z*x))  # Σ_k sin(γ_k log p)
        total += Ssin/(np.sqrt(p)*math.log(p))
    print(f"  p≤{Pmax:5d}: {total:+10.4f}")

# 也检查中间的部分和（K 截断）——看是否随 K 增长
print("\nΣ_p≤100 A_p·Σ_{k≤K} sin(γ_k log p) 随 K 变化：")
ps = primes_upto(100)
for Kk in [10000, 100000, 500000, 1000000, 2000000]:
    total = 0.0
    for p in ps:
        x = math.log(p)
        Ssin = np.sum(np.sin(z[:Kk]*x))
        total += Ssin/(np.sqrt(p)*math.log(p))
    print(f"  K={Kk:7d}: {total:+10.4f}")

# 检查交换序：先 k 后 p（S 的 Titchmarsh）
print("\n对比：-(1/π)Σ_k S(γ_k)（S 的和——通过 N-N₀）")
# S(γ_k) = k - N₀(γ_k)
def N0(t):
    return (t/(2*np.pi))*np.log(t/(2*np.pi)) - t/(2*np.pi) + 7/8
S_at_zeros = np.arange(1, K+1) - N0(z)
print(f"  Σ_k S(γ_k) = {np.sum(S_at_zeros):+10.3f}（N/2 + O(log²N) 理论）")
print(f"  K/2 = {K/2:+.3f}")
