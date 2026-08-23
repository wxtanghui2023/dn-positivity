#!/usr/bin/env python3
"""验证 ∫S·N₀'dt = O(1)？（mean(S)=½ 强形式——潜在无条件新定理）
N₀' = log(t/2π)/2π——缓变但增长——van der Corput 需要处理
Titchmarsh：∫S·N₀' = −(1/π)Σ_p (1/√p log p)∫sin(t log p)N₀'(t)dt + R
"""
import numpy as np
import math
from math import log, pi
from scipy.integrate import quad

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(500000)

def N0p(t):
    return np.log(t/(2*pi))/(2*pi)

def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

S_k = np.array([(k+1) - N0(z[k]) for k in range(len(z))], dtype=float)

# 1. Σ(S_j−½) 直接
PS = np.cumsum(S_k - 0.5)
print(f"Σ(S_j−½) 最终 = {PS[-1]:+.4f}（max|·| = {np.max(np.abs(PS)):.4f}）")

# 2. ∫S·N₀'（分段——S = k − N₀ on [γ_k, γ_{k+1})）
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
total = 0.0
for k in range(len(z)-1):
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    total += 0.5*(b-a)*np.sum(wg*S_vals*N0p(ts))
print(f"∫S·N₀'dt = {total:+.4f}（Σ(S_j−½) = {PS[-1]:+.4f}——差 {abs(PS[-1]-total):.4f}）")

# 3. Titchmarsh 分解：∫sin(t log p)·N₀'(t)dt——van der Corput
print("\n∫sin(t log p)N₀'(t)dt（van der Corput——N₀' 缓变增长）：")
def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

sum_p = 0.0
ps = primes_upto(200)
for p in ps:
    lo = max(p, z[0])
    val, err = quad(lambda t: np.sin(t*log(p))*N0p(t), lo, z[-1], limit=1000, epsabs=1e-9)
    # 尾部：∫_T^∞ sin(t log p)log t dt ~ O(log T/(T log p))——小
    sum_p += val/(np.sqrt(p)*log(p))
titch = -sum_p/pi
print(f"  Σ_p 项 = {titch:+.4f} vs ∫S·N₀' = {total:+.4f}（差 {abs(total-titch):.4f}）")

# 4. van der Corput 界：|∫sin(t log p)N₀'(t)dt| ~ O(log p 相关)
print("\n单个积分 |∫sin(t log p)N₀'(t)dt|：")
for p in [2, 3, 5, 11, 101]:
    lo = max(p, z[0])
    val, err = quad(lambda t: np.sin(t*log(p))*N0p(t), lo, z[-1], limit=1000, epsabs=1e-9)
    print(f"  p={p:4d}: |∫| = {abs(val):.4f}  （log p = {log(p):.3f}——比值 {abs(val)/log(p):.3f}）")
