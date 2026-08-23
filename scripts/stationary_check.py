#!/usr/bin/env python3
"""n 大（stationary phase 活跃）验证：Σ|w·I_p^(截断)| 仍收敛？
stationary 只对有限 p（p²·log p < n——n≤3000 → p≤29 类）——有限和 O(n^{-1/4})
验证 n=500, 1000, 3000 的 Σ|w·I_p| + ∫f_n·S·g 直接
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
g1 = z[0]

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
xg, wg = leggauss(16)

def quad_from(a, f, nsub=12):
    total = 0.0
    for i in range(nsub):
        lo = a + (T-a)*i/nsub
        hi = a + (T-a)*(i+1)/nsub
        ts = 0.5*(hi-lo)*xg + 0.5*(hi+lo)
        total += 0.5*(hi-lo)*np.sum(wg*f(ts))
    return total

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

ps = primes_upto(50000)

# n 大验证
print("n 大（stationary 活跃）——Σ|w·I_p^(截断)|：")
for n in [500, 1000, 3000]:
    sum_abs = 0.0
    sum_sig = 0.0
    for p in ps:
        lo = max(p, g1)
        val = quad_from(lo, lambda t, p=p: f_n(t, n)*np.sin(t*log(p))*g(t), nsub=8)
        w = 1.0/(np.sqrt(p)*log(p))
        sum_abs += abs(val)*w
        sum_sig += val*w
    print(f"  n={n:4d}: Σ|w·I_p| = {sum_abs:.4f}  Σ w·I_p = {sum_sig:+.4f}  −(1/π)Σ = {-(1/pi)*sum_sig:+.4f}")

# 直接 ∫f_n·S·g（n 大——抽样检查）
print("\n直接 ∫f_n·S·g（n 大——12 点/区间）：")
for n in [500, 1000, 3000]:
    total = 0.0
    for k in range(len(z)-1):
        a, b = z[k], z[k+1]
        if b - a < 1e-12: continue
        ts = 0.5*(b-a)*xg + 0.5*(a+b)
        S_vals = (k+1) - N0(ts)
        total += 0.5*(b-a)*np.sum(wg*S_vals*f_n(ts, n)*g(ts))
    print(f"  n={n:4d}: ∫f_n·S·g = {total:+.6f}")

# stationary 的 p 范围（n 依赖）
print("\nstationary phase 的 p 范围（t* = √(n/log p) > max(p,γ₁)）：")
for n in [500, 1000, 3000]:
    ps_st = []
    for p in ps[:200]:
        t_star = np.sqrt(n/log(p) - 0.25)
        if t_star > max(p, g1):
            ps_st.append(p)
    print(f"  n={n}: stationary p = {ps_st[:10]}（{len(ps_st)} 个——有限）")

del z
gc.collect()
print("内存已释放")
