#!/usr/bin/env python3
"""验证 Titchmarsh 分解：∫S·g = −(1/π)Σ_p (1/(√p log p))∫sin(t log p)g dt + R
关键：Σ_p 项之和（数值）vs ∫S·g（直接）——确认分解成立（交换合法）
"""
import numpy as np
import math
from math import log, pi
from scipy.integrate import quad

def g(t):
    return 2*pi/(t*np.log(t/(2*pi))**2)

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

G1 = 14.134725142
K = 200000
z = load_zeros(K)

# 直接：∫S·g（分段——从 γ₁ 到 γ_K）
def N0(t):
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
total = 0.0
for k in range(K-1):
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    total += 0.5*(b-a)*np.sum(wg*S_vals*g(ts))
print(f"直接 ∫S·g（γ₁→γ_{K}）≈ {total:+.4f}")

# Titchmarsh 分解：−(1/π)Σ_p (1/(√p log p))∫_{max(p,γ₁)}^{γ_K} sin(t log p)g dt
# 素数
def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

ps = primes_upto(2000)
sum_p = 0.0
for p in ps:
    lo = max(p, G1)
    val, err = quad(lambda t: np.sin(t*log(p))*g(t), lo, z[K-1], limit=500)
    sum_p += val/(np.sqrt(p)*log(p))
titch = -sum_p/pi
print(f"Titchmarsh Σ_p 项 ≈ {titch:+.4f}（截断 p≤2000, t≤γ_{K}）")
print(f"差 = {total - titch:+.4f}（R 余项 + 高 p 项 + 尾部——应小）")

# 高 p 贡献估计：p > 2000——Σ 1/(p^{3/2}log⁴p) 尾部
ps_all = primes_upto(100000)
tail = np.sum(1.0/(ps_all[ps_all>2000]**1.5 * np.log(ps_all[ps_all>2000])**4))
print(f"高 p 尾部（p>2000）Σ 1/(p^{{3/2}}log⁴p) ≈ {tail:.6f}——小 ✓")
