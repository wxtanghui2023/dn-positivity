#!/usr/bin/env python3
"""
VIII 内部推导——生死关测试：monodromy/orbit 是否区分 on/off-line

核心问题：prime-only monodromy 是否比 Euler 恒等式多一条约束？
测试：on-line 零点配置 vs off-line 扰动的 orbit 结构差异
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20

def main():
    print("="*70)
    print("VIII 生死关——orbit/monodromy 对 on/off-line 的区分")
    print("="*70)
    
    # 用 Odlyzko 零点
    zdata = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
    N = 500
    gammas = zdata[:N]
    
    # 1. 轨道结构：ρ/k 的实部分布
    # on-line: ρ = ½+iγ——ρ/k 实部 = ½/k
    # off-line 扰动: ρ = (½+δ)+iγ——实部 = (½+δ)/k
    print("\n1. 轨道实部分布（k=1..5——前 500 零点——）:")
    print("   on-line: 轨道实部 = {½/k: k=1..5} =", [0.5/k for k in range(1,6)])
    for delta in [0.0, 0.05, 0.1, 0.2]:
        betas = [0.5+delta]
        reals = set()
        for k in range(1, 6):
            for b in betas:
                reals.add(round(b/k, 6))
        print(f"   δ={delta}: 轨道实部集 = {sorted(reals)}")
    
    # 2. 碰撞率：ρ_i/k = ρ_j/ℓ ⟺ k·ρ_i = ℓ·ρ_j（复——）
    # on-line 碰撞（½+iγ_i）/k = (½+iγ_j)/ℓ——实部: ½/k = ½/ℓ ⟹ k=ℓ——虚部 γ_i/k = γ_j/ℓ ⟹ γ_i=γ_j
    # ⟹ on-line 无碰撞（除平凡 k=ℓ, i=j——）！
    # off-line（不同 δ——）不同零点不同 β——β_i/k = β_j/ℓ 可能（如果 β 有理比——）
    print("\n2. 碰撞分析（关键——）:")
    print("   on-line (β=½ 全部——): (½+iγ_i)/k = (½+iγ_j)/ℓ")
    print("     实部: ½/k = ½/ℓ ⟹ k = ℓ——虚部: γ_i = γ_j ⟹ i = j")
    print("     ⟹ on-line 配置【零碰撞】（除平凡——）——缩放轨道不相交！")
    print()
    print("   off-line (β_i 不同——): β_i/k = β_j/ℓ 可能（β_i/β_j = k/ℓ ∈ ℚ——）")
    print("     ⟹ off-line 配置【可能碰撞】（如果 β 比值有理——）")
    print()
    print("   ⚠️ 但这依赖 β 的【比值】——不依赖 β ≠ ½ 本身——")
    print("   ⚠️ 单零点 off-line（一个 δ≠0——其他 ½——）: β_i/k = ½/ℓ")
    print("     ⟹ (½+δ)/k = ½/ℓ ⟹ 2ℓ(½+δ) = k ⟹ ℓ+2ℓδ = k——若 δ 无理——无解——")
    print("     ⟹ 单离轴零点的轨道与在线轨道【也不碰撞】（δ 无理——）")
    
    # 3. monodromy 权重 W(z) 的算术结构
    print("\n3. monodromy 跳跃系数（奇点 ρ/k——）:")
    print("   绕 ρ/k 的跳跃 = μ(k)/k · 2πi（对简单零点——）")
    for k in range(1, 8):
        print(f"     k={k}: μ(k)/k = {mp.mobius(k)}/{k}——跳跃 = {mp.mobius(k)*2*mp.pi/k:.4f}i")
    print("   系数完全由 k 决定（Möbius——）——【与零点位置无关】——")
    
    # 4. 关键：P 的奇点结构是否给零点约束？
    print("\n4. 结构分析（推导结论——）:")
    print("""
   a. P 的奇点 = {ρ/k}——由零点决定（定义性——读出一——）
   b. monodromy 跳跃系数 = μ(k)/k·2πi——与零点无关（纯 k——）
   c. P 从素数级数（Re>1）唯一延拓——接受任何零点配置
   d. on-line 零碰撞——off-line 也基本零碰撞（δ 无理——）——不区分
   e. 自然边界 Re=0——无条件（Hadamard β>0——）——不依赖 β=½

   ⟹ monodromy/orbit 结构是零点的【结果】（读出——）
   ⟹ prime-only 定义不产生额外约束（延拓唯一——）
   """)

if __name__ == "__main__":
    main()
