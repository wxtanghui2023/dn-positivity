#!/usr/bin/env python3
"""
存活空间检查：λ(n) 和 μ²(n) 的 Dirichlet 级数奇点结构
λ: ζ(2s)/ζ(s)——极点 s=ρ_k/2（ζ(2s) 零点的一半——！）
μ²: ζ(s)/ζ(2s)——零点 s=ρ_k/2

关键观察：ζ(2s) 的零点 = 2s = ρ_k ⟹ s = ρ_k/2——【零点的一半】
如果 ρ_k = ½+iγ_k——ρ_k/2 = ¼+iγ_k/2——实部 ¼！
——"零点的一半"有实部 ¼——不是 ½——但这是 λ/μ² 级数的自然奇点位置

问题：这些结构的"½"或"¼"是否可能编码刚性（不经显式公式——）？
"""
import numpy as np

def main():
    print("="*70)
    print("λ/μ² 级数奇点结构——存活空间检查")
    print("="*70)
    
    # 1. 奇点位置分析
    print("\n1. 奇点位置（RH 下——）:")
    print("   λ(n): Σλ(n)n^{−s} = ζ(2s)/ζ(s)")
    print("     极点: s=1（ζ(s)——）——s=ρ_k/2（ζ(2s)=0——）")
    print("   μ²(n): Σμ²(n)n^{−s} = ζ(s)/ζ(2s)")
    print("     极点: s=1（ζ(s)——）——零点: s=ρ_k/2")
    print("\n   若 ρ_k = ½+iγ_k（RH——）:")
    print("   ρ_k/2 = ¼ + iγ_k/2——【实部 ¼】——不是 ½！")
    print("   ——'零点的一半'落在实部 ¼——垂直压缩——")
    
    # 2. 关键问题：ζ(2s) 的"零点的一半"的实部 = β_k/2
    #    如果 β_k ≠ ½——ρ_k/2 的实部 ≠ ¼——但——λ 级数的收敛横坐标？
    print("\n2. 收敛横坐标分析:")
    print("   Σλ(n)n^{−s} 的收敛横坐标 = sup(1, β_k/2 的 sup——)")
    print("   = max(1, Θ/2)——Θ = sup β_k")
    print("   ——λ 级数收敛横坐标 ~ Θ/2（如果 Θ/2 > 1？——不——Θ<1——）")
    print("   ——λ 级数在 σ > max(1,Θ/2)——Θ<1——所以 σ>1——平凡")
    print("   ——μ² 级数同理——在 σ>1 收敛——奇点在 ≤1——够不到——")
    
    # 3. 数值：λ 部分和的增长（与 x^{Θ/2} 比较——）
    print("\n3. λ 部分和 L(x) 的数值增长:")
    N = 1000000
    # 用筛法算 λ
    lam = np.ones(N+1, dtype=np.int8)  # λ(1)=1
    # 简单筛：对每个素数 p——翻转 p 的倍数——再翻转 p² 的倍数——
    is_comp = np.zeros(N+1, dtype=bool)
    for p in range(2, int(N**0.5)+1):
        if not is_comp[p]:
            lam[p::p] *= -1
            pp = p*p
            for k in range(pp, N+1, pp):
                is_comp[k] = True
    # 处理素数幂（λ(p^k) = (−1)^k——）——上述翻转给 (−1)^{Ω}——检查
    # λ(n) = (−1)^{Ω(n)}——上面 lam[p::p] *= −1 对所有倍数翻转一次——对 p² 的倍数
    # 应该翻两次（Ω 加 2——）——修正：
    lam = np.ones(N+1, dtype=np.int8)
    is_prime = np.ones(N+1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(N**0.5)+1):
        if is_prime[p]:
            is_prime[p*p::p] = False
    # 对每个素数幂翻转
    for p in range(2, N+1):
        if is_prime[p]:
            pk = p
            k = 1
            while pk <= N:
                lam[pk::pk] *= (-1)**k  # λ(p^k·m) 翻 (−1)^k
                pk *= p
                k += 1
    # L(x) = Σ_{n≤x}λ(n)
    L = np.cumsum(lam)
    # 检查 max |L(x)|/x^{1/4} 和 /x^{1/2}
    xs = np.array([int(10**(i/10)) for i in range(10, 61)])
    xs = xs[xs <= N]
    print(f"   L(x) 在 x≤{N}:")
    for x in xs[-8:]:
        lx = abs(L[x])
        print(f"   x={x}: |L(x)| = {lx:.0f}——/x^{{1/4}} = {lx/x**0.25:.3f}——/x^{{1/2}} = {lx/x**0.5:.5f}")

if __name__ == "__main__":
    main()
