#!/usr/bin/env python3
"""
诊断 Banks 定理 3.1 的 Σ₁(T) = Σ_{γ≤T} ξ^{−ρ} 𝒳(1−ρ)（截断——无 ℬ——）
定理 3.1：Σ₁(T) + Σ₂(T/2πξ) = O(T^{½}log²T)
Σ₂(U) ~ μ(q)/φ(q)·U（Λ 扭曲主项——Ramanujan——）
⟹ 若定理 3.1 对——Σ₁(T) ~ −μ(q)/φ(q)·T/(2πξ) + O(T^{½}log²T)（T 线性主项——）
诊断：Σ₁(T) 是否有 T 线性主项？——验证 𝒳 相位/实现的正确性——
"""
import numpy as np
from math import pi, log

def chi_X(g):
    """𝒳(1−ρ)——ρ=½+iγ——𝒳(½−iγ) = conj(𝒳(½+iγ))——Stirling（Banks 2.1）"""
    import cmath
    t = g
    if t < 1:
        return complex(0, 0)
    # 𝒳(½+iγ) ≈ e^{−iπ/4}·exp(iγ log(γ/2πe))（σ=½——t=γ——(t/2π)^0=1）
    phase = 1j*t*cmath.log(t/(2*pi*cmath.e))
    chi_pos = cmath.exp(complex(-1j*pi/4)) * cmath.exp(phase)
    return chi_pos.conjugate()

def mu_phi(q):
    n = q; mu = 1; p = 2; facs = []
    while p*p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0: return 0, None
            facs.append(p)
        p += 1
    if n > 1: facs.append(n)
    mu = (-1)**len(facs)
    phi = q
    for p in set(facs): phi = phi * (p-1) // p
    return mu, phi

def main():
    print("="*70)
    print("诊断：Σ₁(T) = Σ_{γ≤T} ξ^{−ρ}𝒳(1−ρ)——截断和——主项？")
    print("="*70)
    
    z = np.load('/tmp/zeros_odlyzko_100k.npy')
    print(f"零点: {len(z)}——γ到{z[-1]:.0f}")
    
    for q, m in [(2,1), (3,1), (5,1), (3,2)]:
        mu, phi = mu_phi(q)
        if mu == 0: continue
        xi = m/q
        print(f"\nξ={m}/{q}——μ/φ = {mu}/{phi}——预测主项系数 {-(mu/phi)/(2*pi*xi):.4f}")
        for T in [1000, 2000, 5000, 10000, 20000]:
            zsel = z[z <= T]
            S1 = 0j
            for g in zsel:
                rho = 0.5 + 1j*g
                S1 += xi**(-rho) * chi_X(g)
            # 预测：−μ/φ·T/(2πξ)
            pred = -(mu/phi) * T / (2*pi*xi)
            # 实际每零点平均
            print(f"  T={T:>6}: 零点{len(zsel):>6}——Σ₁ = {S1.real:+9.2f}{S1.imag:+9.2f}i"
                  f"——预测主项 = {pred:+9.2f}——|Σ₁|/T = {abs(S1)/T:.4f}")

if __name__ == "__main__":
    main()
