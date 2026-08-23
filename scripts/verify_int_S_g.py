#!/usr/bin/env python3
"""验证 ∫S·g = O(1) 的无条件论证——关键检查
∫S·g dt = −(1/π)Σ_p (1/(√p log p))∫_p^∞ sin(t log p)g(t)dt + R 余项
g(t) = 2π/(t log²(t/2π))

检查：
1. ∫_p^∞ sin(t log p)g(t)dt 的 van der Corput 界（数值）
2. Σ_p 收敛
3. ∫S·g 的数值（8/23: +0.1313）
4. 与 Σδ_k = O(1) 的关联
"""
import numpy as np
import math
from math import log, pi

def g(t):
    return 2*pi/(t*log(t/(2*pi))**2)

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

# 1. van der Corput 界验证：∫_p^∞ sin(t log p)g(t)dt
print("∫_p^∞ sin(t log p)g(t)dt 的数值（高精度）vs van der Corput 界：")
from scipy.integrate import quad
for p in [2, 3, 5, 11, 101, 1009]:
    val, err = quad(lambda t: np.sin(t*log(p))*g(t), p, 1e7, limit=1000)
    # 尾部估计（t > 1e7——g ~ 1/(t log²t)——振荡——~O(1/(1e7·log²)))
    tail_est = 2*pi/(1e7*log(1e7)**2)/log(p)  # 粗略
    vdc_bound = 2*pi/(p*log(p/(2*pi))**2)/log(p)  # g(p)/u——一阶 van der Corput
    print(f"  p={p:5d}: ∫ = {val:+.2e}  （van der Corput 界 ~ {vdc_bound:.2e}——比值 {abs(val)/max(vdc_bound,1e-30):.3f}）")

# 2. Σ_p 1/(p^{3/2}log⁴p) 收敛
print("\nΣ_p 1/(p^{3/2}log⁴p) 的部分和：")
def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]
for Pmax in [10**3, 10**4, 10**5, 10**6]:
    ps = primes_upto(Pmax)
    s = np.sum(1.0/(ps**1.5 * np.log(ps)**4))
    print(f"  p≤{Pmax:7d}: Σ = {s:.6f}")

# 3. ∫S·g 的数值（8/23 声称 +0.1313）
print("\n∫S·g dt 数值（分段——S(t) = k − N₀(t) on [γ_k, γ_{k+1})）：")
z = load_zeros(500000)
def N0(t):
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8
# ∫S·g = Σ_k ∫_{γ_k}^{γ_{k+1}} (k − N₀(t))·g(t)dt
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
total = 0.0
for k in range(len(z)-1):
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    total += 0.5*(b-a)*np.sum(wg*S_vals*g(ts))
print(f"  ∫S·g（到 γ_500k）≈ {total:+.4f}（8/23 声称 +0.1313）")

# 4. Σδ_k = −S/N' − ∫S·g + O(1) 验证
print("\nΣδ_k 分解验证：")
dg = np.diff(z)
Np = np.log(z[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np
Sd = np.cumsum(delta)
print(f"  max|Σδ_k| = {np.max(np.abs(Sd)):.3f}（应 ~ O(1) 如果 ∫S·g = O(1)）")
