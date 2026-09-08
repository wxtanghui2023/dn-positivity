#!/usr/bin/env python3
"""
离线玩具实验：如果零点离线——η 的 −1/3 还成立吗？
γ_m（Stieltjes——）的零点表示：高阶项 γ_m ~ Σ_ρ 贡献（1/ρ^(m+1) 类）
构造：真实 γ_m + 一个零点的"在线→离线"变化——重算 η——看渐近

注意：真实 γ_m 是"全在线"的（RH 数值——）——玩具 = 加一个离线零点的
"额外贡献"——但真实 γ_m 已含该零点的在线贡献——所以要"替换"——
简化：γ_m^off = γ_m^real − c_m(ρ_on) + c_m(ρ_off)
"""
import mpmath as mp
mp.mp.dps = 40

def stieltjes_ma(m):
    return (-1)**m * mp.stieltjes(m) / mp.factorial(m)

def zero_contrib(rho, m):
    """单零点对 Maślanka γ_m 的贡献——log 的 m 阶导在 s=1
    d^m/ds^m log(1-s/ρ)|_{s=1} 类——(-1)^m·(m-1)!/(ρ-1)^m 修正：
    实际 γ_m^Maš 与 (d^m/ds^m log ξ)|_{s=1} 相关——用 (-1)^m m! 归一
    用之前验证的：-m!(-1)^m/(ρ-1)^{m+1}——但 γ_m 归一化 m!——测试
    """
    return (-1)**m / (rho - 1)**m  # 试探形式

def compute_etas(gamma_fn, n_max):
    gamma0 = gamma_fn(0)
    if abs(gamma0) < 1e-30:
        return None
    gammas = [gamma_fn(m) for m in range(n_max+1)]
    C = {}
    for k in range(1, n_max+2):
        C[(k,0)] = gamma0**k
        for m in range(1, n_max+1):
            s = mp.mpf(0)
            for i in range(m):
                s += (k*m - (k+1)*i) * gammas[m-i] * C[(k,i)]
            C[(k,m)] = s / (m*gamma0)
    etas = []
    for n in range(n_max):
        s = mp.mpf(0)
        for k in range(n+1):
            s += (-1)**(k+1) / (k+1) * C[(k+1, n-k)]
        etas.append((n+1)*s)
    return etas

def eta_ratio(etas, j):
    if abs(etas[j-1]) > 1e-25:
        return etas[j]/etas[j-1]
    return None

def main():
    print("="*70)
    print("离线玩具：零点离线 → η 的 −1/3 还成立吗？")
    print("="*70)
    n_max = 28
    
    # 真实 η（对照——）
    etas_real = compute_etas(stieltjes_ma, n_max)
    print("\n真实 η 比率:")
    for j in [10, 15, 20, 25]:
        r = eta_ratio(etas_real, j)
        if r: print(f"   j={j}: {mp.nstr(r, 6)}")
    
    # 离线玩具——把 γ=14.13 的零点离线（β: 0.5→0.6——）
    # γ_m 的修正 = contrib(ρ_off) - contrib(ρ_on)
    print("\n把第 1 零点（γ=14.13）离线（β: 0.5→0.6——）:")
    for zeta_form in [False, True]:
        def gamma_off(m):
            g = stieltjes_ma(m)
            rho_on = 0.5 + 1j*14.1347
            rho_off = 0.6 + 1j*14.1347
            # 贡献形式（试探——需要正确缩放——）
            if zeta_form:
                c_on = mp.factorial(m) / rho_on**(m+1)  # Σ1/ρ^{m+1} 类
                c_off = mp.factorial(m) / rho_off**(m+1)
            else:
                c_on = mp.mpf(1) / (rho_on - 1)**m
                c_off = mp.mpf(1) / (rho_off - 1)**m
            return g - c_on + c_off  # 替换贡献
        etas_off = compute_etas(gamma_off, n_max)
        if etas_off:
            print(f"   {'1/ρ^m 形式' if not zeta_form else 'm!/ρ^{m+1} 形式'} η 比率:")
            for j in [10, 15, 20, 25]:
                r = eta_ratio(etas_off, j)
                if r: print(f"      j={j}: {mp.nstr(r, 6)}")
        else:
            print("   （γ₀ 变零——递推失败——）")

    # 关键：γ_0 不变（第一零点离线不影响 γ_0——但影响高阶——）
    print("\n⚠️ 注意：这个玩具的贡献形式未校准（真实 γ_m 的零点分解复杂——）")
    print("   需要正确的高阶 γ_m 公式——先确认 Stieltjes 的零点表示")

if __name__ == "__main__":
    main()
