#!/usr/bin/env python3
"""
验证 Banks (1.1)：ζ 零点的 ξ=m/q 扭曲和
Σ_{ρ=½+iγ} ξ^{−ρ} 𝒳(1−ρ) ℬ(γ/2πX) + (μ(q)/φ(q))C_ℬ X ≪ X^{½+ε}

机制：ζ 零点经有理扭曲 ξ 编码模 q 信息——这是"RH 零点 → GRH"的通道
验证：和的主项（−(μ/φ)C_ℬ X——）和误差（≪X^{½+ε}——）
"""
import numpy as np
from math import log, pi, sqrt

def mu_phi(q):
    """μ(q) 和 φ(q)"""
    # μ(q)
    n = q
    mu = 1
    p = 2
    facs = []
    while p*p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0, None  # 有平方因子——μ=0
            facs.append(p)
        p += 1
    if n > 1:
        facs.append(n)
    mu = (-1)**len(facs)
    # φ(q)
    phi = q
    for p in set(facs):
        phi = phi * (p-1) // p
    return mu, phi

def chi_func(g):
    """𝒳(1−ρ)——ρ=½+iγ——1−ρ=½−iγ——
    用 Stirling 渐近（Banks (2.1)——稳定无溢出——）：
    𝒳(1−s) ≈ e^{−iπ/4}(t/2π)^{σ−½}exp(it·log(t/2πe))——对 s=1−ρ=½−iγ——
    先用 (2.1) 对 t=γ>0 得 𝒳(½+iγ)——再共轭：𝒳(½−iγ) = conj(𝒳(½+iγ))"""
    import cmath
    # 𝒳(½+iγ) ≈ e^{−iπ/4}·(γ/2π)^{0}·exp(iγ·log(γ/(2πe)))（σ=½——t=γ——）
    t = g
    if t < 1:
        return complex(0, 0)
    phase = 1j*t*cmath.log(t/(2*cmath.e))
    chi_pos = cmath.exp(complex(-1j*pi/4)) * cmath.exp(phase)  # 𝒳(½+iγ)
    return chi_pos.conjugate()  # 𝒳(½−iγ) = conj(𝒳(½+iγ))

def B_test(u):
    """测试函数 ℬ(u)——紧支撑（|u|<1——）平滑——"""
    if abs(u) >= 1:
        return 0.0
    return (1-u*u)**3

def C_B():
    """C_ℬ = ∫ℬ(u)du——ℬ 支撑 (−1,1)——"""
    us = np.linspace(-1, 1, 10001)
    return np.trapz([B_test(u) for u in us], us)

def main():
    print("="*70)
    print("验证 Banks (1.1)：ζ 零点的 ξ 扭曲和")
    print("="*70)
    
    z = np.load('/tmp/zeros_odlyzko_100k.npy')
    print(f"零点可用: {len(z)}——γ到 {z[-1]:.0f}")
    
    Cb = C_B()
    print(f"C_ℬ = ∫ℬ = {Cb:.4f}")
    
    for q in [2, 3, 4, 5]:
        m = 1
        if q == 4: continue  # μ(4)=0——跳过
        mu, phi = mu_phi(q)
        if mu == 0:
            print(f"\nq={q}: μ(q)=0——跳过")
            continue
        xi = m/q
        print(f"\nξ = {m}/{q}——μ(q)/φ(q) = {mu}/{phi} = {mu/phi:.3f}")
        
        for X in [200, 500, 1000, 2000]:
            T_max = 2*pi*X  # γ 上限
            # 取零点 γ ≤ T_max
            zsel = z[z <= T_max]
            if len(zsel) < 10:
                continue
            gamma_vals = zsel
            
            # Σ ξ^{−ρ} 𝒳(1−ρ) ℬ(γ/2πX)——ρ=½+iγ
            S = 0
            for g in gamma_vals:
                rho = 0.5 + 1j*g
                # ξ^{−ρ} = ξ^{−½−iγ}
                xi_pow = xi**(-rho)
                # 𝒳(1−ρ)
                chi_val = chi_func(g)  # 传入 γ——内部算 𝒳(½−iγ)
                Bv = B_test(g/(2*pi*X))
                S += xi_pow * chi_val * Bv
            
            main_term = (mu/phi) * Cb * X
            total = S + main_term
            bound = X**0.5 * (log(X))**0.5  # 参考尺度
            print(f"  X={X:>5}: γ≤{T_max:>6.0f}（{len(gamma_vals):>5}零点——）"
                  f"Σ={S.real:+.2f}{S.imag:+.2f}i——主项={main_term:+.2f}——"
                  f"|总|={abs(total):.2f}——X^½(logX)^½={bound:.1f}——比值={abs(total)/X**0.5:.3f}")

if __name__ == "__main__":
    main()
