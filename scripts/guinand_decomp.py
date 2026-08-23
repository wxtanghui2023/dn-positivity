#!/usr/bin/env python3
"""Guinand 公式分解验证：Σ_{γ≤X} sin(γ log p) 的主项 vs 素数项
Guinand (1947): N(T) = T/2π·log(T/2π) - T/2π - (1/π)·Σ_n Λ(n) sin(T log n)/(√n log n) + 修正
（对 T 微分得到零点脉冲 = 主项导数 + 素数项导数）

对测试函数 sin(T log p)·1_{T≤X} 积分：
Σ_{γ_k≤X} sin(γ_k log p) ≈ (1/2π)∫_2^X sin(Tx)log(T/2π)dT   [主项]
                  + (1/π)Σ_n Λ(n)/√n·∫_2^X sin(Tx)cos(T log n)dT   [素数项]
                  + 边界
"""
import numpy as np
from scipy.special import expi
import math

def Ci(u):
    return 0.5*(expi(1j*u) + expi(-1j*u)).real

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def main_term(X, x):
    """(1/2π)∫_2^X sin(Tx)log(T/2π)dT —— 解析"""
    A = -np.log(X/(2*np.pi))*np.cos(X*x)/x + np.log(1/np.pi)*np.cos(2*x)/x
    B = (Ci(X*x) - Ci(2*x))/x
    return (A + B)/(2*np.pi)

def prime_term(X, x, nmax=100000):
    """(1/π)Σ_{n≤nmax} Λ(n)/√n·∫_2^X sin(Tx)cos(T log n)dT
    ∫sin(Tx)cos(T log n)dT = ½∫[sin(T(x+ln)) + sin(T(x-ln))]dT
    = ½[-cos(T(x+ln))/(x+ln) - cos(T(x-ln))/(x-ln)]_2^X  (x≠ln)
    x=ln 时：∫sin(Tx)cos(Tx)dT = ½∫sin(2Tx)dT = -cos(2Tx)/(4x)
    """
    def vdm(a):
        return (np.cos(a) - np.cos(X*a))/a  # ∫_2^X sin(Ta)dT = (cos 2a - cos Xa)/a
    # 素数幂 von Mangoldt
    total = 0.0
    # 素数
    primes = []
    sieve = np.ones(nmax+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(nmax**0.5)+1):
        if sieve[i]: sieve[i*i::i] = False
    primes = np.nonzero(sieve)[0]
    lp = np.log(primes)
    ln = np.log(nmax)
    # ∫ sin(Tx)cos(T ln) dT = ½·[vdm(x+ln) + vdm(x-ln)]  (x≠ln)
    # 注意 vdm(a) = ∫_2^X sin(Ta)dT = (cos(2a)-cos(Xa))/a
    I = 0.5*(vdm(x+lp) + vdm(x-lp))
    # x - lp 接近 0 的项（n≈p）——精确处理
    eps = 1e-8
    close = np.abs(x - lp) < eps
    if np.any(close):
        for p in primes[close]:
            a = x - np.log(p)
            # ∫sin(Tx)cos(T(x+a))dT ≈ ∫sin(Tx)cos(Tx)dT (a≈0)
            I_close = -np.cos(2*X*x)/(4*x) + np.cos(4*x)/(4*x)
            total += math.log(p)/np.sqrt(p) * I_close
    # 非共振项
    mask = ~close
    total += np.sum(np.log(primes[mask])/np.sqrt(primes[mask]) * I[mask])
    # 素数幂 n=p^m, m≥2（Λ = log p）
    for p in primes:
        if p*p > nmax: break
        for m in range(2, 30):
            n = p**m
            if n > nmax: break
            a = x - m*np.log(p)
            if abs(a) < eps:
                I_n = -np.cos(2*X*x)/(4*x) + np.cos(4*x)/(4*x)
            else:
                I_n = 0.5*(vdm(x+m*np.log(p)) + vdm(a))
            total += np.log(p)/np.sqrt(n) * I_n
    return total/np.pi

K = 2000000
z = load_zeros(K)
X = z[-1]

print(f"X = γ_2M = {X:.1f}")
for p0 in [2, 3, 5, 7, 11, 47]:
    x = math.log(p0)
    Ssum = np.sum(np.sin(z*x))
    MT = main_term(X, x)
    PT = prime_term(X, x, nmax=100000)
    print(f"\np={p0:2d} x={x:.6f}:")
    print(f"  Σsin(γ≤X)     = {Ssum:+10.4f}")
    print(f"  主项 (1/2π)∫  = {MT:+10.4f}")
    print(f"  素数项 (1/π)Σ = {PT:+10.4f}")
    print(f"  主项+素数项   = {MT+PT:+10.4f}  （vs Σsin 差 = {Ssum-MT-PT:+10.4f}）")
