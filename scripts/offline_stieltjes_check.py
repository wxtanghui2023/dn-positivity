#!/usr/bin/env python3
"""
高零点离线对低阶 γ_m（Stieltjes）的影响——检测边界
如果 λ~_n = O(1) 只依赖低阶 γ_m——高零点离线能否影响它们？
γ_m = ξ 在 s=1 的 Taylor 系数/m!——编码所有零点（Hadamard——）
问题：一个离线零点 ρ₀=β+iγ₀（γ₀ 大——）对 γ_m（m≤15）的贡献多大？
"""
import mpmath as mp
mp.mp.dps = 30

def gamma_m_from_zeros(gammas, betas, m, M_trunc):
    """γ_m 的零点贡献近似（Hadamard log 的 Taylor——）
    log ξ(s) = log ξ(0) + Σ_ρ log(1-s/ρ)——γ_m 相关
    简化：单个零点的贡献到 γ_m
    """
    pass

def single_zero_contribution(rho, m):
    """单个零点 ρ 对 Stieltjes γ_m 的贡献（近似——）
    ξ 的 Hadamard：log ξ(s) = C + Σ_ρ log(1 - s/ρ)
    γ_m 来自 d^m/ds^m log ξ(s) 在 s=1——单零点贡献：
    d^m/ds^m log(1-s/ρ)|_{s=1} = -(m-1)!/(ρ-1)^m 类
    """
    # log(1-s/ρ) 的 m 阶导在 s=1：-d^m/ds^m[(s/ρ)/(1-s/ρ)]...
    # = -(m-1)!/(1-1/ρ)^m·(-1/ρ)^m？——直接：d/ds log(1-s/ρ) = -1/(ρ-s)
    # d^m/ds^m log(1-s/ρ) = -(-1)^m·m!·(-1)^m/(ρ-s)^{m+1}·... 
    # 直接：d^m/ds^m [-1/(ρ-s)] = -m!/(ρ-s)^{m+1}·(-1)^m·(-1)^m = -m!/(ρ-s)^{m+1}?
    # 简化：d/ds log(1-s/ρ) = -1/(ρ-s)——d^m/ds^m = -m!/(ρ-s)^{m+1}·(-1)^m
    # 在 s=1：-m!·(-1)^m/(ρ-1)^{m+1}
    val = -mp.factorial(m) * (-1)**m / (rho - 1)**(m+1)
    return val

def main():
    print("="*70)
    print("高零点离线对低阶 γ_m 的影响")
    print("="*70)
    
    # 1. 单个零点的贡献随 γ₀ 衰减
    print("\n1. 单零点对 γ_m 的贡献（|contribution| vs 高度——）:")
    m = 5
    print(f"   m={m}:")
    for gamma0 in [14, 100, 1000, 1e4, 1e6, 1e8]:
        rho_on = 0.5 + 1j*gamma0
        rho_off = 0.6 + 1j*gamma0  # 离线 β=0.6
        c_on = single_zero_contribution(rho_on, m)
        c_off = single_zero_contribution(rho_off, m)
        diff = abs(c_on - c_off)
        print(f"   γ₀={gamma0:>8.0e}: 在线贡献 |{abs(c_on):.3e}|——离线差 |Δ|={diff:.3e}")
    
    # 2. 累积：所有零点对 γ_5 的贡献 vs 单个离线零点的差
    print("\n2. 关键比值：单离线零点贡献 vs 全部零点总贡献")
    # γ_5 的量级（真实——）
    gamma5_ma = (-1)**5 * mp.stieltjes(5) / mp.factorial(5)
    print(f"   真实 |γ_5^Maš| = {abs(gamma5_ma):.3e}")
    
    # 一个 γ₀=10⁶ 的离线零点对 γ_5 的贡献差：
    for gamma0 in [1e6, 1e8]:
        rho_on = 0.5 + 1j*gamma0
        rho_off = 0.6 + 1j*gamma0
        diff5 = abs(single_zero_contribution(rho_on, 5) - single_zero_contribution(rho_off, 5))
        ratio = diff5 / abs(gamma5_ma)
        print(f"   γ₀={gamma0:.0e} 离线对 γ_5 的差 = {diff5:.3e}——相对 γ_5 = {ratio:.2e}")
    
    # 3. 高零点离线的可检测性总结
    print("\n3. 结论:")
    print("   · 单零点对 γ_m 的贡献 ~ 1/γ₀^(m+1)——高零点贡献极小")
    print("   · 高零点（γ₀>10⁶）离线对低阶 γ_m（m≤15）的影响 ~ 1/γ₀^16——不可检测")
    print("   · 但——低零点（γ₀~14-100——）离线影响大——可检测")
    print("   ⟹ λ~_n = O(1) 对'高零点离线'鲁棒——对'低零点离线'敏感")
    print("   ⚠️ 但反证法说任何离线（含高——）⟹ λ_n 爆炸——")
    print("   ⟹ 若高离线不影响 γ_m 低阶——它必影响高阶（m 随 n 增长——）")
    print("   ⟹ λ~_n = O(1) 的证明需要'所有 m 的 γ_m 结构'——不只是低阶")

if __name__ == "__main__":
    main()
