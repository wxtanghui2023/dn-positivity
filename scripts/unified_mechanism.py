#!/usr/bin/env python3
"""统一视角验证：Σδ = O(1) 的机制 = S 的素数项低频压制（Guinand 无条件版）
Σδ_k = -S/N' - ∫S·g + O(1)——∫S·g = -(1/π)Σ_p(1/√p log p)∫sin(t log p)g dt
验证：Σ_p 项（van der Corput）确实是 ∫S·g 的主项——统一 Guinand 与 Σδ=O(1)
"""
import numpy as np
import math
from math import log, pi
from scipy.integrate import quad

def g(t):
    t = np.asarray(t, dtype=float)
    return 2*pi/(t*np.log(t/(2*pi))**2)

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 300000
z = load_zeros(K)

# Σδ_k
dg = np.diff(z)
Np = np.log(z[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np
Sd = np.cumsum(delta)
print(f"Σδ_k（到 γ_{K}）= {Sd[-1]:+.4f}（max|·| = {np.max(np.abs(Sd)):.3f}）")

# ∫S·g（直接——分段）
def N0(t):
    t = np.asarray(t, dtype=float)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(8)
total = 0.0
for k in range(K-1):
    a, b = z[k], z[k+1]
    ts = 0.5*(b-a)*xg + 0.5*(a+b)
    S_vals = (k+1) - N0(ts)
    total += 0.5*(b-a)*np.sum(wg*S_vals*g(ts))
print(f"∫S·g（到 γ_{K}）= {total:+.4f}")

# S/N' 端点
S_K = K - N0(z[K-1])
endpoint = S_K/Np[-1]
print(f"-S/N'（端点）= {-endpoint:+.4f}")

# 恒等式检查：Σδ = -S/N' - ∫S·g + C？
print(f"Σδ + S/N' + ∫S·g = {Sd[-1] + endpoint + total:+.4f}（应 = 常数——积分下限）")

# Titchmarsh Σ_p 项（主项——验证统一）
def primes_upto(n):
    sieve = np.ones(n+1, dtype=bool); sieve[:2]=False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    return np.nonzero(sieve)[0]

ps = primes_upto(500)
sum_p = 0.0
for p in ps:
    lo = max(p, z[0])
    val, err = quad(lambda t: np.sin(t*log(p))*g(t), lo, z[K-1], limit=500)
    sum_p += val/(np.sqrt(p)*log(p))
titch = -sum_p/pi
print(f"\nTitchmarsh Σ_p 项（p≤500）= {titch:+.4f}")
print(f"∫S·g ≈ Σ_p 项 + R：{total:+.4f} vs {titch:+.4f}——差 {total-titch:+.4f}（R + 高 p）")
print(f"\n统一：Σδ = O(1) ⟸ ∫S·g = O(1) ⟸ Titchmarsh Σ_p（van der Corput——Guinand 无条件版）")
