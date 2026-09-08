#!/usr/bin/env python3
"""
跨越路径验证：D_F 从 ξ_F 整体算（不经零点枚举——）
D_F = Q_F − Q'_RH,F
Q_F = −Σm_ρw_H(γ_ρ,δ_ρ)——w_H = ⟨K^nat_ρ, H₀⟩（配对——）
用整体配对：⟨S_F, H₀⟩ 其中 S_F = ∂²log|ξ_F(½+it)|——从 ξ_F 数值算——
验证对 ζ（RH 数值成立——零点在线——）：D_ζ 应该 = 0
如果整体配对工作——D_F 可算（不经零点——）——跨越的基础
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

# H₀(t) = −(1/4π)log(1+t²) + 1/(2π(1+t²))——判据测试函数
def H0(t):
    return -(1.0/(4*np.pi))*np.log(1+t*t) + 1.0/(2*np.pi*(1+t*t))

# w_H(γ,δ) = ⟨K^nat_δ(·−γ), H₀⟩——闭式（判据——）
def wH(gamma, delta):
    a = 1 + delta
    return (a*a*(a+1) + delta*gamma*gamma) / (2*(a*a + gamma*gamma)**2)

def main():
    print("="*70)
    print("跨越路径：D_F 从 ξ_F 整体算（基础验证——）")
    print("="*70)
    
    # 对 ζ——用零点直接算 Q_ζ 和 Q'_RH,ζ（判据定义——）
    z = np.load('/tmp/zeros_odlyzko_100k.npy')
    z = z[:500]  # 前 500（δ=0——在线——RH 数值——）
    m = np.ones(len(z))  # 重数 1（简单零点——数值——）
    
    # Q_ζ = −Σw_H(γ,0)（δ=0——RH 数值——）
    Q_zeta = -np.sum(wH(z, 0.0))
    Qp_zeta = -np.sum(wH(z, 0.0))  # 投影 = 相同（δ=0——）
    D_zeta = Q_zeta - Qp_zeta
    print(f"零点 {len(z)}（在线——RH 数值——）:")
    print(f"  Q_ζ = −Σw_H(γ,0) = {Q_zeta:.8f}")
    print(f"  D_ζ = Q_ζ − Q'_RH,ζ = {D_zeta:.2e}（应 0——δ=0——）✓")
    
    # 现在验证整体配对：Q_F = −Σw_H 能否从 ξ_F 算？
    # 整体配对：−Σm_ρ⟨K^nat_ρ, H₀⟩ = −⟨Σm_ρK^nat_ρ, H₀⟩（逐项——）
    # Σm_ρK^nat_ρ(t) = S_F(t) − S_reg(t)——S_reg = Gamma/平凡项——
    # S_F(t) = ∂²log|ξ(½+it)|——ξ 是完成函数——需要 ξ 的数值——
    # ξ(½+it) = ½(½+it)(it−½)π^{-(½+it)/2}Γ((½+it)/2)ζ(½+it)——嗯——
    # 简化：S_F 的零点项部分 = ΣK^nat_ρ——直接数值算 K 和——
    
    # 数值验证：Σ_ρ w_H(γ_ρ, δ_ρ)（逐项——）vs ∫S_F(t)H₀(t)dt − ∫S_reg H₀（整体——）
    # 先算逐项的：−Σw_H（上面——）Q_zeta
    
    # 整体：⟨S_F, H₀⟩ = ∫S_F(t)H₀(t)dt——S_F = ∂²log|ξ(½+it)|——
    # 用 mpmath 数值算 S_F（对少量 t——）
    print("\n——整体配对验证（∫S_F·H₀ vs Σw_H——）——")
    print("——S_F = ∂²log|ξ(½+it)|——ξ 用 mpmath——")
    
    # S_F(t) = ∂²log|ξ| = Re[∂²log ξ]（ξ 实系数——|ξ| = ξ 沿临界线实——）
    # ξ(½+it) 实值（ξ(s)=ξ(1−s)——共轭——）——所以 log|ξ| = log|实值|——
    # 数值：ξ(½+it) = (1/2)(½+it)(it−½)π^{-(½+it)/2}Γ((½+it)/2)ζ(½+it)
    # 直接数值二阶导——对几个 t——验证与 ΣK^nat 匹配
    
    def xi_half(t):
        s = mp.mpc(0.5, t)
        xi = mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
        return xi
    
    # S_F(t) = ∂²log|ξ|——用数值二阶导（log|ξ| 在 t——）
    def S_F_num(t):
        h = mp.mpf('0.01')
        f = lambda x: float(mp.log(abs(xi_half(x))))
        return (f(t+h) + f(t-h) - 2*f(t))/(float(h)**2)
    
    # 对几个 t 验证 S_F ≈ ΣK^nat_ρ（零点项——）
    print("\nS_F(t) vs ΣK^nat_ρ(t)（t 远离零点——）:")
    for t in [30, 50, 80]:
        # ΣK^nat_ρ(t)——用零点——K^nat(t) = (δ²−(t−γ)²)/(δ²+(t−γ)²)²——δ=0——
        K_sum = np.sum([-(t-g)**2/((t-g)**2)**2 if abs(t-g) > 1e-6 else 0 for g in z])
        # δ=0: K = (0−(t−γ)²)/(0+(t−γ)²)² = −(t−γ)²/(t−γ)⁴ = −1/(t−γ)²
        K_sum = np.sum([-1.0/(t-g)**2 for g in z if abs(t-g) > 0.1])
        S_val = S_F_num(t)
        print(f"  t={t}: S_F(数值) = {S_val:.4f}——ΣK^nat = {K_sum:.4f}——差（S_reg——Gamma 项——）= {S_val - K_sum:.4f}")

if __name__ == "__main__":
    main()
