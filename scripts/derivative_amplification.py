#!/usr/bin/env python3
"""
微分放大验证——ψ'(x)（平滑——）的零点项是否无 1/ρ 衰减？
ψ(x) = x − Σ_ρ x^ρ/ρ − ...
ψ'(x) = 1 − Σ_ρ x^{ρ−1} + ...（导数——零点项无 1/ρ！）

检查：单离轴零点在 ψ' 的贡献 x^{ρ−1}——模 x^{β−1}——无 1/γ——
vs ψ 的贡献 x^ρ/ρ——模 x^β/γ——有 1/γ——
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def main():
    print("="*70)
    print("微分放大验证——ψ' 的零点项无 1/ρ")
    print("="*70)
    
    # 1. 显式公式导数结构
    print("\n1. 结构确认:")
    print("   ψ(x) = x − Σ_ρ x^ρ/ρ − log2π − ½log(1−x^{−2})")
    print("   ψ'(x) = 1 − Σ_ρ x^{ρ−1} − [尾部项导数]")
    print("   → ψ' 的零点项 x^{ρ−1}——【无 1/ρ 权重】——微分放大！")
    
    # 2. 数值对比：单零点贡献（离轴 ρ = β+iγ——）
    print("\n2. 单零点贡献对比（δ=0.05——β=0.55——）:")
    delta = 0.05
    beta = 0.55
    print(f"{'γ':>6} {'ψ项 x^β/γ（x=e^{1/δ}）':>24} {'ψ\'项 x^{β−1}（x=e^{1/δ}）':>24}")
    x_star = np.exp(1/delta)
    for gamma in [14, 100, 1000, 10000]:
        psi_contrib = x_star**beta / gamma
        psip_contrib = x_star**(beta-1)  # 无 1/γ！
        print(f"{gamma:>6} {psi_contrib:>24.6e} {psip_contrib:>24.6e}")
    
    # 3. 相对在线基准（x^{−1/2}——）
    print("\n3. 相对在线基准 x^{−1/2}（归一化——）:")
    for gamma in [14, 100, 1000]:
        x_star = np.exp(1/delta)
        psi_rel = x_star**delta / gamma  # x^β/γ ÷ x^{1/2} = x^δ/γ
        psip_rel = x_star**delta  # x^{β−1} ÷ x^{−1/2} = x^δ——无 1/γ！
        print(f"   γ={gamma}: ψ 相对 = {psi_rel:.4f}（~1/γ——）——ψ' 相对 = {psip_rel:.4f}（O(1)——！）")
    
    # 4. 含义
    print("\n4. 含义分析:")
    print("   ψ'(x)（平滑——素数数据——zero-blind ✓——）的离轴零点贡献 x^{β−1}")
    print("   相对在线基准 x^{−1/2}：x^δ——【不衰减】（O(1)——非 1/γ——）")
    print("   → 微分通道逃逸 1/γ 衰减——支柱 3 的'原始观测衰减'需修正！")
    print("   → 但——limsup 判别 = RH 等价（已知——）——证明层面循环——")

if __name__ == "__main__":
    main()
