#!/usr/bin/env python3
"""
IX 推导——Archimedean 权重结构探索
核心：权重律 |α|=1（RH——）需要 char-0 实现——先看 Archimedean 侧（Γ——）的"权重"

探索：
1. Γ 因子的"权重"——ξ = ½s(s−1)π^{−s/2}Γ(s/2)ζ——Γ(s/2) 的模在临界线
2. α_ρ = e^{ρ−1/2}——乘性特征酉性
3. 平凡零点（Γ 极点——）的"权重"vs 非平凡（目标——）
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def main():
    print("="*70)
    print("IX 推导——Archimedean 权重结构")
    print("="*70)
    
    # 1. Γ(s/2) 的模在临界线 vs 其他地方
    print("\n1. Γ(s/2) 的模（Archimedean 权重——）:")
    print("   |Γ(σ/2+it/2)| 沿 σ（固定 t——）:")
    for t in [10.0, 21.0, 50.0]:
        vals = []
        for sigma in [0.3, 0.5, 0.7, 1.0]:
            g = mp.gamma(sigma/2 + 1j*t/2)
            vals.append((sigma, float(abs(g))))
        print(f"   t={t}: " + "——".join(f"σ={s}:|Γ|={v:.4e}" for s, v in vals))
    
    # 2. α_ρ = e^{ρ−1/2}——模
    print("\n2. α_ρ = e^{ρ−1/2} 的模（权重——）:")
    print("   ρ = β+iγ——|α| = e^{β−1/2}——RH ⟺ |α|=1")
    for beta in [0.3, 0.5, 0.7]:
        print(f"   β={beta}: |α| = e^{{{beta}-0.5}} = {np.exp(beta-0.5):.4f}")
    
    # 3. 平凡零点的"权重"（Γ 极点——）
    print("\n3. 平凡零点（s = −2n——Γ(s/2) 极点——）的权重观:")
    print("   ξ 的平凡零点来自 Γ(s/2) 极点——Archimedean——")
    print("   函数方程：s ↔ 1−s——平凡零点 −2n ↔ 1+2n（非零点——）")
    print("   → 平凡零点不是 FE 配对的（它们在实轴负侧——）")
    print("   → '权重'结构：平凡零点（Γ——Archimedean——）实——非平凡（ζ——素数——）复")
    
    # 4. 乘性特征 χ_ρ(n) = n^{ρ−1/2}
    print("\n4. 乘性特征 χ_ρ(n) = n^{ρ−1/2}:")
    print("   RH ⟺ χ_ρ 酉（|χ_ρ(n)| = 1 所有 n——）")
    for beta in [0.5, 0.6]:
        gamma1 = 14.1347
        mod_at_n = {2: np.exp((beta-0.5)*np.log(2)), 100: np.exp((beta-0.5)*np.log(100))}
        print(f"   β={beta}: |χ_ρ(2)|={mod_at_n[2]:.4f}——|χ_ρ(100)|={mod_at_n[100]:.4f}")
    
    # 5. 结构观察——ζ 的 Dirichlet 级数在 σ=½ 的"平衡"
    print("\n5. ζ(s) = Σn^{−s}——σ=½ 的平衡点:")
    print("   n^{−s} = n^{−σ}·e^{−it log n}——'模'= n^{−σ}——'相位'= e^{−it log n}")
    print("   部分和 Σ_{n≤X} n^{−σ}e^{−it log n} 的模²（t=γ₁——）:")
    for sigma in [0.4, 0.5, 0.6]:
        # 数值
        t = 14.1347
        X = 100000
        # 用积分近似 + 直接部分和（抽样——）
        ssum = 0
        for n in range(1, 20000):
            ssum += n**(-sigma) * np.exp(-1j*t*np.log(n))
        print(f"   σ={sigma}: |Σ_{'{n≤2e4}'}| = {abs(ssum):.4f}（部分和——）")

if __name__ == "__main__":
    main()
