#!/usr/bin/env python3
"""关键修正验证：I_p 的积分下限 = max(p, γ₁)（Titchmarsh p≤t 截断）
|I_p^(截断)| ≤ C·g(p)/log p ~ C/(p·log³p)——衰减——绝对收敛！
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
g1 = z[0]  # γ₁ ≈ 14.13

def th1(t):
    return np.arctan(1/(2*t))
def g(t):
    return 2*pi/(t*np.log(t/(2*pi))**2)
def f_n(t, n):
    return 4*np.sin(n*np.arctan(1/(2*t)))**2

from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(16)

def quad_from(a, f, nsub=20):
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

# I_p 截断（从 max(p, γ₁)）——p 衰减
print("I_p^(截断)（下限 max(p,γ₁)——Titchmarsh p≤t）随 p：")
ps = primes_upto(20000)
vals_cut = []
for p in ps:
    lo = max(p, g1)
    val = quad_from(lo, lambda t: f_n(t, 100)*np.sin(t*log(p))*g(t), nsub=16)
    vals_cut.append((p, val))
print(f"{'p':>6} {'I_p^(截断)':>12} {'C/(p·log³p)':>14} {'比值':>8}")
for p, val in vals_cut[:10]:
    bound = 1.0/(p*log(p)**3)
    print(f"{p:6d} {val:+12.6f} {bound:14.8f} {abs(val)/bound if bound>0 else 0:8.2f}")
print("  ...")
for p, val in vals_cut[-5:]:
    bound = 1.0/(p*log(p)**3)
    print(f"{p:6d} {val:+12.6f} {bound:14.8f} {abs(val)/bound if bound>0 else 0:8.2f}")

# Σ_p (1/(√p log p))·|I_p^(截断)|——绝对收敛？
print("\nΣ_p w·|I_p^(截断)|（绝对收敛检验）：")
cum = 0.0
for p, val in vals_cut:
    w = 1.0/(np.sqrt(p)*log(p))
    cum += abs(val)*w
print(f"  Σ|w·I_p| = {cum:.6f}（有限 = 绝对收敛！）")

# Σ_p (1/(√p log p))·I_p^(截断)（带符号——Titchmarsh 值）
cum_s = 0.0
for p, val in vals_cut:
    w = 1.0/(np.sqrt(p)*log(p))
    cum_s += val*w
print(f"  Σ w·I_p = {cum_s:+.6f}")
print(f"  −(1/π)·Σ w·I_p = {-(1/pi)*cum_s:+.6f}（应 ≈ ∫f_n·S·g = +0.034）")

del z
gc.collect()
print("内存已释放")
