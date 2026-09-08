#!/usr/bin/env python3
"""
关键验证：λ~_n（Maślanka 振荡——ξ 层——）vs γ 层相位均匀性
问题：λ~_n = O(1) ⟹ λ_n = 趋势 + O(1) ≥ 0 ⟹ RH？
      λ~_n 从 ξ 算（η——Stieltjes——）——ξ 编码 β——无 S(t) 的 β 缺口？

验证：
A. λ_n = λ⁻_n(趋势) + λ~_n(振荡)——分解确认
B. λ~_n 的 n-行为（用 Stieltjes 常数——高精度——小 n——）
C. 关键：λ~_n = O(1) 是否足以 λ_n ≥ 0（趋势主导——）
"""
import mpmath as mp
mp.mp.dps = 30

def stieltjes_ma(k):
    """Maślanka 约定：γ_k^Maš = (−1)^k/k!·γ_k^标准"""
    return (-1)**k * mp.stieltjes(k) / mp.factorial(k)

def lambda_full(n, K):
    """λ_n 从 Stieltjes 常数算（ξ 层——无条件——）
    λ_n = n·γ_0^{n-1}... 用 Li 系数公式：λ_n = Σ... 简化——用振荡公式
    实际：λ_n = -n*η_{n-1} 类——这里用 Maślanka 2.4 的趋势+振荡
    """
    pass

def main():
    print("="*70)
    print("关键验证：λ~_n（ξ层——）的 β 独立性 vs S(t)")
    print("="*70)
    
    # A. 核心概念验证：ξ 编码 β 的方式
    print("\nA. ξ(s) 编码零点（含 β——）的方式:")
    print("   ξ(s) = ½s(s-1)π^{-s/2}Γ(s/2)ζ(s)——整函数——Hadamard:")
    print("   ξ(s) = ξ(0)·Π_ρ(1-s/ρ)——每个零点（含 β——）都在积里")
    print("   ⟹ ξ 的 Taylor 系数（在 s=1——）编码 β——但ξ的值无条件可算")
    print("   ⟹ λ_n（从 ξ Taylor 算——）含 β 信息【但不需先知道 β】")
    print("   ⟹ 与 S(t)（arg ζ 虚部——纯 γ 层——）本质不同！")
    
    # B. λ~_n = O(1) 的数值（小 n——高精度 Stieltjes——）
    print("\nB. λ~_n（振荡——从 η 算——小 n——）:")
    # η_n = (n+1)Σ_{k=0}^n (-1)^{k+1}/(k+1)·c^{(k+1)}_{n-k}
    # c^{(k)}_m 递推复杂——用简化：λ_n 的 ξ-导数定义直接算
    # 替代：λ_n = (1/(n-1)!)·(d^n/ds^n)[s^{n-1}log ξ(s)]|_{s=1}（Li——）
    # 用 mpmath 数值微分近似小 n
    from mpmath import diff, log, zeta, gamma, pi, sqrt, factorial
    
    def xi(s):
        return 0.5*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
    
    def li_coeff(n):
        """λ_n = 1/(n-1)! · d^n/ds^n [s^{n-1} log ξ(s)]|_{s=1}"""
        def f(s):
            return s**(n-1) * log(xi(s))
        # n 阶导数在 s=1
        return diff(f, 1, n) / factorial(n-1)
    
    print(f"   λ_n（ξ 直接——无条件——无零点——）:")
    vals = []
    for n in range(1, 9):
        try:
            L = li_coeff(n)
            vals.append((n, L))
            print(f"   n={n}: λ_n = {mp.nstr(L, 8)}")
        except Exception as e:
            print(f"   n={n}: 失败 {str(e)[:50]}")
    
    # C. 趋势 vs 振荡
    print("\nC. 趋势 λ⁻_n ~ ½nlogn + cn（n 大正——）:")
    c = 0.5*(mp.euler - 1 - mp.log(2*mp.pi))
    print(f"   c = {mp.nstr(c, 8)}")
    for n in [10, 50, 100]:
        trend = 0.5*n*mp.log(n) + c*n
        print(f"   n={n}: 趋势 = {mp.nstr(trend, 6)}（正——大 n 主导——）")
    print("   ⟹ 若 λ~_n = O(1)——λ_n = 趋势 + O(1) ≥ 0 对大 n 自动")
    print("   ⟹ RH 的证明 ⟺ λ~_n = O(1)（不是 λ_n ≥ 0 逐点——）")

if __name__ == "__main__":
    main()
