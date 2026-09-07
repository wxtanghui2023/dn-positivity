#!/usr/bin/env python3
"""
检查 ξ ∈ D_P 的可能性——KPS (2023) Prop 26 / (4.16)-(4.18)

核心：
ξ(√z) = Θ(z) = Σ γ(n)/n! zⁿ
γ(n) = n!/(2n)! · (3/2)^{2n} · [F(2n−2) − F(2n)/2^{2n−1}]    (4.16)
F(n) = ∫₁^∞ (log x)ⁿ x^{−3/4} θ'(x) dx——θ'(x) = 导数 of theta 级数

ξ ∈ D_P 需要 ∃Ψ∈N_D: ξ = J_Ψ——即 (4.18):
φ(n+1) = −G(2n)/(8(n+1)G(2n+2))——G(2n) = 64n(2n−1)F(2n−2)/F(2n) − 1

检查 φ 序列是否"像" Bernstein 函数（N 类——凸——增长——特定渐近 Ψ(u)~u²/ℓ(u)）
"""
import mpmath as mp

mp.mp.dps = 40

def theta_deriv(x):
    """θ'(x) = -π Σ n² e^{-π n² x}"""
    s = mp.mpf(0)
    n = 1
    while True:
        term = mp.mpf(n)**2 * mp.exp(-mp.pi * n*n * x)
        s += term
        if term < mp.mpf(10)**(-50):
            break
        n += 1
    return -mp.pi * s

def F_int(n):
    """F(n) = ∫₁^∞ (log x)ⁿ x^{−3/4} θ'(x) dx——用变量替换 x = e^t——t∈[0,∞)"""
    # x = e^t: dx = e^t dt——(log x)ⁿ = tⁿ——x^{−3/4} = e^{−3t/4}
    # F(n) = ∫₀^∞ tⁿ e^{−3t/4} θ'(e^t) e^t dt = ∫₀^∞ tⁿ e^{t/4} θ'(e^t) dt
    integrand = lambda t: t**n * mp.e**(t/4) * theta_deriv(mp.e**t)
    # θ'(e^t) ~ -πe^{-πe^t}·(e^t 修正)——收敛极快——t 到 ~30 足够
    val = mp.quad(integrand, [0, mp.mpf(30)])
    return val

def main():
    print("="*70)
    print("ξ ∈ D_P 可能性检查——KPS (4.16)-(4.18)")
    print("="*70)
    
    N_MAX = 8  # 需要 F(0..2N)——先算 F(0)..F(16)
    print("\n计算 F(n)——theta 积分数值（n=0..16——高精度——慢——）")
    F = {}
    for n in range(0, 2*N_MAX + 1):
        F[n] = F_int(n)
        print(f"  F({n}) = {mp.nstr(F[n], 10)}")
    
    print("\nγ(n)（ξ 的 Taylor 系数——）与 φ 序列检查")
    print(f"{'n':>3} {'γ(n)':>15} {'G(2n)':>15} {'φ(n+1)':>18}")
    G = {}
    phi = {}
    for n in range(0, N_MAX):
        # γ(n) = n!/(2n)! · (3/2)^{2n} · [F(2n−2) − F(2n)/2^{2n−1}]（4.16 的 F(2n-2) 项——n=0 特殊）
        # G(2n) = 64n(2n−1)F(2n−2)/F(2n) − 1
        if n == 0:
            continue
        G_val = 64*n*(2*n-1)*F[2*n-2]/F[2*n] - 1
        G[2*n] = G_val
        # φ(n+1) = −G(2n)/(8(n+1)G(2n+2))
        G_next = 64*(n+1)*(2*(n+1)-1)*F[2*n]/F[2*n+2] - 1
        G[2*(n+1)] = G_next
        phi_val = -G_val / (8*(n+1)*G_next)
        phi[n+1] = phi_val
        print(f"{n:>3} {'':>15} {mp.nstr(G_val, 12):>15} {mp.nstr(phi_val, 15):>18}")
    
    # 检查 φ 的 Bernstein 型特征
    print("\n" + "="*70)
    print("φ 序列的 Bernstein 型检查")
    print("="*70)
    print("Bernstein 函数特征：φ(u)/u 完全单调——φ 凸——φ(0)=0——增长 ~u²/ℓ(u)")
    vals = [phi[n] for n in range(1, N_MAX)]
    print(f"φ(1..{N_MAX-1}) = {[mp.nstr(v, 8) for v in vals]}")
    # 符号
    signs = [mp.sign(v) for v in vals]
    print(f"符号: {signs}——全 {'正' if all(s > 0 for s in signs) else '有负!'}")
    # 增长率（φ(n) ~ n²/ℓ(n)？——比值 φ(n+1)/φ(n)）
    if len(vals) > 2:
        ratios = [float(vals[i+1]/vals[i]) for i in range(len(vals)-1)]
        print(f"比值 φ(n+1)/φ(n): {[f'{r:.3f}' for r in ratios]}——增长 {'超线性' if all(r > 1 for r in ratios) else '?'}")
    # 凸性检查（φ(n+1)-φ(n) 增——）
    if len(vals) > 3:
        diffs = [float(vals[i+1]-vals[i]) for i in range(len(vals)-1)]
        d2 = [diffs[i+1]-diffs[i] for i in range(len(diffs)-1)]
        print(f"二阶差分: {[f'{d:.3f}' for d in d2]}——凸性 {'凸' if all(d > 0 for d in d2) else '非凸!'}")

if __name__ == "__main__":
    main()
