#!/usr/bin/env python3
"""高精度确认 ∫f_n·S·g = O(1)——更多 n + 验证 Titchmarsh 分解
直接（S_k 分段——高精度）vs Titchmarsh（Σ_p 项 + R 项）
"""
import numpy as np
import gc
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(300000)
T = z[-1]

def th1(t):
    return np.arctan(1/(2*t))
def g(t):
    return 2*pi/(t*np.log(t/(2*pi))**2)
def f_n(t, n):
    return 4*np.sin(n*np.arctan(1/(2*t)))**2
def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(12)

# 直接 ∫f_n·S·g（高精度——每零点区间 12 点高斯）
print("∫f_n·S·g 直接（高精度——12 点/区间）：")
for n in [50, 100, 200, 300, 500, 800]:
    total = 0.0
    for k in range(len(z)-1):
        a, b = z[k], z[k+1]
        if b - a < 1e-12: continue
        ts = 0.5*(b-a)*xg + 0.5*(a+b)
        S_vals = (k+1) - N0(ts)
        total += 0.5*(b-a)*np.sum(wg*S_vals*f_n(ts, n)*g(ts))
    print(f"  n={n:4d}: ∫f_n·S·g = {total:+.6f}")

# Titchmarsh 分解验证（n=100——Σ_p 项）
print("\nTitchmarsh 分解（n=100）：")
def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

n = 100
ps = primes_upto(30000)
sum_t = 0.0
for p in ps:
    # I_p（分块高斯 16×12）
    val = 0.0
    nsub = 12
    for i in range(nsub):
        lo = z[0] + (T-z[0])*i/nsub
        hi = z[0] + (T-z[0])*(i+1)/nsub
        ts = 0.5*(hi-lo)*xg + 0.5*(hi+lo)
        val += 0.5*(hi-lo)*np.sum(wg*f_n(ts, n)*np.sin(ts*log(p))*g(ts))
    sum_t += val/(np.sqrt(p)*log(p))
# Titchmarsh：S(t) = −(1/π)Σ_p sin(t log p)/(√p log p) + R
# ∫f_n·S·g = −(1/π)Σ_p w_p·I_p + ∫f_n·R·g
print(f"  −(1/π)Σ_p w·I_p = {-(1/pi)*sum_t:+.6f}")
print(f"  直接 ∫f_n·S·g（n=100）= +0.0337")
print(f"  差（R 项 + 截断误差）= {0.0337 + sum_t/pi:+.6f}")

del z
gc.collect()
print("内存已释放")
