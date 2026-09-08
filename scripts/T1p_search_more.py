#!/usr/bin/env python3
"""
T1' 抽象搜索（续）：更多双约束类别
C. Thue-Morse 字：自相似规则 A(t(2n)=t(n)) vs 移位 B(t(n+1))
D. 幂等/投影对：模 p 筛 A vs 模 q 筛 B（两个局部约束的交换——）
E. 双射/对合：n ↔ n+d（平移——）vs n ↔ p·n（乘素数——）的交换缺陷

测：交换子是否给"尺度平衡/½"
"""
import numpy as np
from math import log, gcd

def test_C():
    """Thue-Morse: t(2n)=t(n), t(2n+1)=-t(n)——自相似 A vs 移位 B"""
    print("="*70)
    print("C. Thue-Morse: 自相似 vs 移位")
    print("="*70)
    N = 4096
    # 生成 Thue-Morse
    t = np.zeros(N+1, dtype=int)
    for n in range(1, N+1):
        t[n] = 1 - 2*(bin(n).count('1') % 2)  # (-1)^{s_2(n)}
    # A: 自相似约束——"缺陷" = t(2n) - t(n) 和 t(2n+1) + t(n)
    defect_A = 0
    for n in range(1, N//2):
        if t[2*n] != t[n]: defect_A += 1
        if t[2*n+1] != -t[n]: defect_A += 1
    print(f"   A 缺陷（t(2n)≠t(n)——）: {defect_A}/{(N//2-1)*2}（应 0——自相似精确——）")
    # B: 移位——t(n+1) 的"结构"——相邻乘积
    adj = t[1:N] * t[2:N+1]
    print(f"   B: t(n)t(n+1) = {'+1' if np.mean(adj)>0 else '-1'} 平均——均值 {np.mean(adj):.3f}")
    # 交换子：A 作用（自相似变换）后 B vs B 后 A
    # A 作为映射：n → 2n（乘 2——）——B：n → n+1（——）
    # Δ(n) = t(2(n+1)) - t(2n+1) 类？——乘 2 和加 1 的交换
    D = np.zeros(N//2)
    for n in range(1, N//2 - 1):
        # 先 A（乘2）后 B（加1）：t(2(n+1)) = t(2n+2)——先 B 后 A：t(2n + 1)
        # Δ = |t(2n+2) - t(2n+1)| 的统计——1 表示非交换（总是——乘2和加1不交换——）
        D[n] = abs(t[2*n+2] - t[2*n+1])
    print(f"   Δ（乘2/加1的交换缺陷——）: 非零比例 = {np.mean(D>0):.3f}（——1=总非交换——平凡——）")
    print("   ——乘 2 和加 1 不交换（算术基本事实——）——但无尺度结构——")

def test_D():
    """模 p 筛 vs 模 q 筛——两个局部约束"""
    print("\n" + "="*70)
    print("D. 模 p 筛 A_p vs 模 q 筛 A_q（两个局部约束——）")
    print("="*70)
    p, q = 2, 3
    N = 3000
    # A_p: n 被 p 整除的指示——(A_p x)(n) = x(n) if p|n
    # 两个"约束"（筛——）的交换：A_p A_q = A_q A_p（平凡——整除交换——）
    # Δ = A_p A_q - A_q A_p = 0——平凡！
    print(f"   A_p（p|n 投影——）和 A_q（q|n——）的交换子 = 0（平凡——）")
    print(f"   ——两个'局部约束'（整除——）自动交换——无缺陷——")
    print(f"   ——除非约束'非交换'（如筛的选择依赖——）——人为——")

def test_E():
    """平移 n→n+d vs 乘素数 n→pn——交换缺陷的尺度"""
    print("\n" + "="*70)
    print("E. 平移（加 d——）vs 乘法（乘 p——）在数上")
    print("="*70)
    # Δ(n) = (pn + d) - p(n+d) = d(1-p) 类？——加法和乘法算子
    # 作为函数：A_d(n) = n+d——B_p(n) = pn——[A_d, B_p](n) = A_d(B_p(n)) - B_p(A_d(n))
    # = (pn + d) - p(n+d) = d - pd = d(1-p)——常数！
    for d, p in [(1, 2), (1, 3), (2, 3)]:
        D = d*(1-p)
        print(f"   d={d}——p={p}: Δ = A_d B_p − B_p A_d = {D}（常数——）")
    print("   ——平移和乘法的交换子 = 常数（仿射群——）——无 n 依赖——")
    print("   ——仿射变换的交换子——尺度结构——但常数——无 ½——")

def test_F():
    """关键测试：什么算子的交换子有'尺度平衡'？——检查膨胀型"""
    print("\n" + "="*70)
    print("F. 尺度互补算子搜索——膨胀 D_λ 与逆尺度")
    print("="*70)
    print("   膨胀 D_λ: n → λn（对数尺度 +logλ——）")
    print("   膨胀互相交换——[D_λ, D_μ] = 0——")
    print("   平移和膨胀：[T_d, D_λ](n) = (λn+d) - λ(n+d) = d(1-λ)——常数——")
    print("   ——仿射群（平移+膨胀——）的交换子都是常数或 0——")
    print("   无'尺度平衡点'（交换子不依赖 n 的尺度——）——")

if __name__ == "__main__":
    test_C()
    test_D()
    test_E()
    test_F()
