#!/usr/bin/env python3
"""
子问题 B——k(u) = E(h)(u) 验证——Mellin 变换零点 vs Ξ 零点
h(u) = π/2·u²(2πu²−3)e^{−πu²}——（Letter (13)——）
E(f)(u) = u^{1/2}Σ_{n≥1}f(nu)——（求和映射——）
k(u) = E(h)(u)——k̂(t) = ∫k(u)u^{it}d*u = Ξ(t)（Fact 6.2——）
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def h(u):
    """h(u) = π/2·u²(2πu²−3)e^{−πu²}"""
    return mp.pi/2 * u**2 * (2*mp.pi*u**2 - 3) * mp.e**(-mp.pi*u**2)

def k_Eh(u, N=200):
    """k(u) = E(h)(u) = u^{1/2}Σ_{n≤N}h(nu)"""
    total = mp.mpf('0')
    for n in range(1, N+1):
        nu = n*u
        if nu > 5:  # h 指数衰减——截断
            break
        total += h(nu)
    return u**0.5 * total

def khat(t, umax=5.0, Nsum=200):
    """k̂(t) = ∫₀^∞ k(u)u^{it} d*u = ∫ k(u)u^{it−1}du"""
    def integrand(u):
        return k_Eh(u, Nsum) * u**(1j*t) / u
    return mp.quad(integrand, [0, umax])

def xi_xi(t):
    """Ξ(t) = ξ(½+it)——用 mpmath"""
    return mp.zeta(0.5+1j*t) * 0.5*(0.5+1j*t)*(0.5+1j*t-1) * mp.pi**(-(0.5+1j*t)/2) * mp.gamma((0.5+1j*t)/2)

def main():
    print("="*70)
    print("子问题 B——k(u)=E(h)(u) 验证——k̂(t) vs Ξ(t)")
    print("="*70)
    
    # 1. k(u) 与 Riemann 的 theta 关系验证
    print("\n1. k(u) 基本验证:")
    for u in [0.5, 1.0, 1.5, 2.0]:
        print(f"   k({u}) = {float(k_Eh(u)):.6f}")
    
    # 2. k̂(t) vs Ξ(t)（几个 t——）
    print("\n2. k̂(t) vs Ξ(t)（归一化——）:")
    # Ξ 用标准定义——ξ(½+it)——注意常数
    for t in [0.0, 5.0, 10.0, 14.0]:
        kh = khat(t)
        xi = xi_xi(t)
        ratio = kh/xi if abs(xi) > 1e-10 else float('inf')
        print(f"   t={t}: k̂={complex(kh):.4e}——Ξ={complex(xi):.4e}——比 {ratio:.4f}")
    
    # 3. k̂(t) 的零点 vs Ξ 零点（关键——）
    print("\n3. k̂(t) 零点（|k̂| 扫描——找极小——）:")
    # Ξ 的零点在 t = γ_n（虚部——）
    from mpmath import zetazero
    gammas = [float(zetazero(k).imag) for k in range(1, 6)]
    print(f"   Ξ 零点（预期——）: {gammas}")
    # k̂ 在 γ_n 附近
    for g in gammas:
        kh = khat(g)
        print(f"   k̂(γ={g:.2f}) = {complex(kh):.4e}（应≈0——）")

if __name__ == "__main__":
    main()
