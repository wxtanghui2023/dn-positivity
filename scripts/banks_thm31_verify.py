#!/usr/bin/env python3
"""
验证 Banks 定理 3.1：Σ₁(T) + Σ₂(T/2πξ) = O(T^{½}log²T)
Σ₁(T) = Σ_{0<γ≤T} ξ^{−ρ}𝒳(1−ρ)（ζ 零点——）
Σ₂(U) = Σ_{1<n≤U} Λ(n)e(−nξ)（素数幂——直接从素数数据算——）
——检验我的 Σ₁ 实现与 Σ₂ 理解——确定符号/主项结构——
"""
import numpy as np
from math import pi, log, sqrt

def chi_X(g):
    import cmath
    t = g
    if t < 1: return complex(0, 0)
    phase = 1j*t*cmath.log(t/(2*pi*cmath.e))
    chi_pos = cmath.exp(complex(-1j*pi/4)) * cmath.exp(phase)
    return chi_pos.conjugate()

def main():
    print("="*70)
    print("验证定理 3.1：Σ₁(T) + Σ₂(T/2πξ) = O(T^{½}log²T)")
    print("="*70)
    
    z = np.load('data/zeros_odlyzko_100k.npy')
    # 素数数据（到 10^7——够 U ~ 几千到几万——）
    try:
        primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
        print(f"素数可用: {len(primes)}——最大 {primes[-1]}")
    except:
        print("无 primes_1e8——用简单筛到 2e6")
        N = 2000000
        sieve = np.ones(N+1, dtype=bool); sieve[:2] = False
        for i in range(2, int(N**0.5)+1):
            if sieve[i]: sieve[i*i::i] = False
        primes = np.nonzero(sieve)[0].astype(np.int64)
        print(f"筛出素数: {len(primes)}")
    
    # 素数幂的 Λ(n) 列表（n ≤ U_max——）
    U_max = 200000
    # Λ(n) 稀疏表：n → Λ(n)（素数幂——）
    # 用字典存（U_max 不大——）
    lambdas = {}  # n → Λ(n)
    for p in primes:
        if p > U_max: break
        pk = p
        while pk <= U_max:
            lambdas[int(pk)] = float(log(p))
            pk *= p
    print(f"素数幂到 {U_max}: {len(lambdas)} 个")
    
    for q, m in [(2,1), (3,1)]:
        xi = m/q
        print(f"\nξ={m}/{q}:")
        for T in [2000, 5000, 10000, 20000]:
            # Σ₁(T)
            zsel = z[z <= T]
            S1 = sum(xi**(-(0.5+1j*g)) * chi_X(g) for g in zsel)
            # Σ₂(U)——U = T/2πξ
            U = T/(2*pi*xi)
            S2 = sum(lambdas[n]*np.exp(-2j*pi*n*xi) for n in lambdas if n <= U)
            total = S1 + S2
            # 各自的主项系数（每 T——）
            print(f"  T={T:>6}: Σ₁={S1.real:+9.2f}{S1.imag:+6.2f}i——"
                  f"Σ₂={S2.real:+9.2f}{S2.imag:+6.2f}i——|总|={abs(total):7.2f}"
                  f"——T^½log²T={sqrt(T)*log(T)**2:7.1f}——比值={abs(total)/(sqrt(T)*log(T)**2):.3f}")

if __name__ == "__main__":
    main()
