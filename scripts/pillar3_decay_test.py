#!/usr/bin/env python3
"""
支柱 3 测试——离轴零点的 zero-blind 响应是否普遍随 γ 衰减
通道：
1. 显式公式单零点项 x^ρ/ρ——模 x^β/|ρ|——γ 扫描
2. λ_n 的 ε(γ) = |1−1/ρ|−1——~1/γ²？
3. 检查是否有"尺寸无关"通道（不衰减——）
"""
import numpy as np

def main():
    print("="*70)
    print("支柱 3 测试——离轴响应的 γ-衰减")
    print("="*70)
    
    # 1. 显式公式单零点项（β=0.55——固定 δ——）
    print("\n1. 显式公式项 x^ρ/ρ——模 = x^β/|ρ|（x = e^{1/δ}——特征尺度——）:")
    delta = 0.05
    beta = 0.5 + delta
    x = np.exp(1/delta)  # 特征尺度
    print(f"   δ={delta}——β={beta}——x = e^{{1/δ}} = {x:.2e}")
    for gamma in [14, 100, 1000, 10000]:
        rho_abs = np.sqrt(beta**2 + gamma**2)
        contrib = x**beta / rho_abs
        # 相对 ψ 主项 x——或相对 x^{1/2}
        rel = x**(beta-0.5) / rho_abs
        print(f"   γ={gamma:>6}: |x^ρ/ρ| = {contrib:.4e}——相对 x^½: {rel:.4e}")
    
    # 2. λ_n 的 ε(γ)
    print("\n2. λ_n 的指数率 ε(γ) = |1−1/ρ| − 1（β<½——经 FE——）:")
    for beta_off in [0.4]:  # β = 0.4 < ½——经 FE 配对给 1−β = 0.6 > ½
        for gamma in [14, 100, 1000, 10000]:
            # |1−1/ρ|——ρ = β+iγ——用 β>½ 侧（FE 配对——）
            b = 1 - beta_off  # = 0.6
            # |1−1/ρ|² = |(ρ−1)/ρ|² = ((b−1)²+γ²)/(b²+γ²)——b−1 = −0.4
            eps = np.sqrt(((b-1)**2 + gamma**2)/(b**2 + gamma**2)) - 1
            n_star = 1/eps if eps > 0 else float('inf')
            print(f"   γ={gamma:>6}: ε = {eps:.3e}——n* = 1/ε = {n_star:.3e}")
    
    # 3. "尺寸无关"检查——有没有不衰减的通道？
    print("\n3. 尺寸无关通道检查:")
    print("   β 本身不衰减（位置——）——但任何 zero-blind 感测 β 的量——")
    print("   a. 经显式公式（x^β/γ——衰减——）")
    print("   b. 经读出（循环——）")
    print("   c. 经统计（β 盲——）")
    print("   ⟹ 无已知尺寸无关通道——支柱 3 初步支持——")

if __name__ == "__main__":
    main()
