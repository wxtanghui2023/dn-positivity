#!/usr/bin/env python3
"""逐项检查 Σ_p A_p·Σ_k sin(γ_k log p) 的每素数贡献——为什么收敛
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

ps = primes_upto(300)
print(f"{'p':>5} {'Ssin(K)':>10} {'A_p':>10} {'贡献':>12} {'累积':>12}")
cum = 0.0
for p in ps:
    x = math.log(p)
    Ssin = np.sum(np.sin(z*x))
    Ap = 1.0/(np.sqrt(p)*math.log(p))
    contrib = Ap*Ssin
    cum += contrib
    if p <= 100 or p % 20 == 0:
        print(f"{p:5d} {Ssin:+10.3f} {Ap:10.5f} {contrib:+12.5f} {cum:+12.5f}")

print(f"\n总累积 (p≤300) = {cum:+.4f}")
print(f"K = {K}")

# 检查：Σ_k sin(γ_k log p) 最终值 vs max 的行为差异
print("\n部分和最终值 vs max（几个 p）：")
for p in [2, 47, 97, 179, 283]:
    x = math.log(p)
    S = np.cumsum(np.sin(z*x))
    print(f"  p={p:4d}: 最终值={S[-1]:+8.3f}  max|·|={np.max(np.abs(S)):8.2f}  比值={S[-1]/np.max(np.abs(S)):+.4f}")
