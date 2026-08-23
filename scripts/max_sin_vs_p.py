#!/usr/bin/env python3
"""max|Σ_{k≤K} sin(γ_k log p)| 随 p 的增长模式——决定 A_p 加权收敛性
如果 max ~ O(1)：Σ_p A_p·max 发散（Σ 1/(√p log p) 发散）——需抵消
如果 max ~ O(p^α)：加权 Σ 1/(p^{1/2-α} log p) 收敛当 α < 1/2
如果 max ~ O(log p)：加权 Σ 1/(√p log p)·log p = Σ 1/√p 发散
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

z = load_zeros(2000000)
K = len(z)

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i] = False
    return np.nonzero(sieve)[0]

ps = primes_upto(5000)
print(f"{'p':>6} {'x=log p':>9} {'max|Σsin|':>10} {'max/√p':>10} {'max/log p':>10} {'max·log p/√p':>12}")
logK = math.log(K)
# 每 20 个素数采样输出 + 几个特殊值
step = 20
for i, p in enumerate(ps):
    if i % step != 0 and p not in [2, 3, 5, 7, 11, 47, 97, 997, 4999]:
        continue
    x = math.log(p)
    S = np.cumsum(np.sin(z*x))
    mx = np.max(np.abs(S))
    print(f"{p:6d} {x:9.4f} {mx:10.2f} {mx/math.sqrt(p):10.4f} {mx/x:10.3f} {mx*math.log(p)/math.sqrt(p):12.4f}")
