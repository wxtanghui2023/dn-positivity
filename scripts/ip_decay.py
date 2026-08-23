#!/usr/bin/env python3
"""关键验证：I_p(n) 随 p 的衰减 + Σ_p 部分和收敛
如果 I_p(n) = O(1) 一致（不随 p 增长）——绝对收敛——无条件！
如果增长——需带符号抵消（相位均匀性）
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

from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(16)

def quad_precise(f, a, b, nsub=30):
    total = 0.0
    for i in range(nsub):
        lo = a + (b-a)*i/nsub
        hi = a + (b-a)*(i+1)/nsub
        ts = 0.5*(hi-lo)*xg + 0.5*(hi+lo)
        total += 0.5*(hi-lo)*np.sum(wg*f(ts))
    return total

def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

# I_p(n) 随 p 的衰减（n=100 固定）
print("I_p(n=100) 随 p 的衰减（p → 大）：")
ps = primes_upto(5000)
vals = []
for p in ps:
    val = quad_precise(lambda t: f_n(t, 100)*np.sin(t*log(p))*g(t), z[0], T, nsub=20)
    vals.append((p, val))
print(f"{'p':>6} {'I_p':>12} {'1/(√p·logp)':>12} {'|I_p|·w':>12}")
for p, val in vals[:10]:
    w = 1.0/(np.sqrt(p)*log(p))
    print(f"{p:6d} {val:+12.4f} {w:12.6f} {abs(val)*w:12.6f}")
# 大 p
print("  ...")
for p, val in vals[-5:]:
    w = 1.0/(np.sqrt(p)*log(p))
    print(f"{p:6d} {val:+12.4f} {w:12.6f} {abs(val)*w:12.6f}")

# Σ_p 部分和（绝对 vs 条件）
print("\nΣ_p (1/(√p·logp))·I_p 的部分和（n=100）：")
sum_abs = 0.0
sum_signed = 0.0
for p, val in vals:
    w = 1.0/(np.sqrt(p)*log(p))
    sum_abs += abs(val)*w
    sum_signed += val*w
print(f"  Σ|I_p|·w = {sum_abs:.4f}（绝对——发散则无界）")
print(f"  Σ I_p·w = {sum_signed:+.4f}（带符号——收敛目标）")
print(f"  ∫f_n·S·g 直接 = +0.034（n=100——对比）")
print(f"  （Titchmarsh: ∫f_n·S·g ≈ −(1/π)Σ_p w·I_p——检查符号）")

# 收敛性判定：Σ|I_p|·w 随 pmax
print("\nΣ|I_p|·w 随 pmax（绝对收敛检验）：")
cum = 0.0
for i, (p, val) in enumerate(vals):
    w = 1.0/(np.sqrt(p)*log(p))
    cum += abs(val)*w
    if p in [100, 500, 1000, 2000, 5000]:
        print(f"  p≤{p:5d}: Σ|I_p|·w = {cum:.4f}")

del z
gc.collect()
print("内存已释放")
