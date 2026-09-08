#!/usr/bin/env python3
"""
验证 Banks 定理 3.1（修复版）：Σ₁(T) + Σ₂(T/2πξ) = O(T^{½}log²T)
Σ₁(T) = Σ_{0<γ≤T} ξ^{−ρ}𝒳(1−ρ)（ζ 零点——）
𝒳(1−ρ) 用 Banks (2.1)【直接以 s=ρ 代入】：≈ e^{−iπ/4}e^{+iγ log(γ/2πe)}（正相位——）
Σ₂(U) = Σ_{1<n≤U} Λ(n)e(−nξ)——e(u)=e^{2πiu}
"""
import numpy as np
from math import pi, log, sqrt

def chi_X(g):
    """𝒳(1−ρ)——Banks (2.1)：𝒳(1−s) ≈ e^{−iπ/4}(t/2π)^{σ−½}exp(it log(t/2πe))
    直接以 s=ρ=½+iγ 代入——σ=½——t=γ——= e^{−iπ/4}·e^{+iγ log(γ/2πe)}"""
    import cmath
    t = g
    if t < 1: return complex(0, 0)
    phase = 1j*t*cmath.log(t/(2*pi*cmath.e))
    return cmath.exp(complex(-1j*pi/4)) * cmath.exp(phase)

def main():
    print("="*70)
    print("验证定理 3.1（修复 𝒳 相位——）")
    print("="*70)
    
    z = np.load('/tmp/zeros_odlyzko_100k.npy')
    try:
        primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    except:
        print("无素数数据——退出"); return
    
    U_max = 200000
    lambdas = {}
    for p in primes:
        if p > U_max: break
        pk = p
        while pk <= U_max:
            lambdas[int(pk)] = float(log(p))
            pk *= p
    
    # 先精确验证 𝒳(1−ρ) 修复版 vs mpmath（对 ρ=½+iγ——𝒳(1−ρ)=2(2π)^{−ρ}Γ(ρ)cos(πρ/2)）
    import mpmath as mp
    mp.mp.dps = 15
    print("\n𝒳(1−ρ) 修复版验证（mpmath——）:")
    for g in z[:3]:
        rho = mp.mpc(0.5, float(g))
        chi_exact = 2*(2*mp.pi)**(-rho)*mp.gamma(rho)*mp.cos(mp.pi*rho/2)
        cs = chi_X(float(g))
        print(f"  γ={float(g):.3f}: 精确={mp.nstr(chi_exact,6)}——修复版=({cs.real:+.4f}{cs.imag:+.4f}i)——差={abs(complex(chi_exact)-cs):.4f}")
    
    for q, m in [(2,1), (3,1)]:
        xi = m/q
        print(f"\nξ={m}/{q}:")
        for T in [2000, 5000, 10000, 20000]:
            zsel = z[z <= T]
            S1 = sum(xi**(-(0.5+1j*g)) * chi_X(g) for g in zsel)
            U = T/(2*pi*xi)
            S2 = sum(lambdas[n]*np.exp(-2j*pi*n*xi) for n in lambdas if n <= U)
            total = S1 + S2
            print(f"  T={T:>6}: Σ₁={S1.real:+9.2f}{S1.imag:+6.2f}i——"
                  f"Σ₂={S2.real:+9.2f}{S2.imag:+6.2f}i——|总|={abs(total):7.2f}"
                  f"——T^½log²T={sqrt(T)*log(T)**2:7.1f}——比值={abs(total)/(sqrt(T)*log(T)**2):.3f}")

if __name__ == "__main__":
    main()
