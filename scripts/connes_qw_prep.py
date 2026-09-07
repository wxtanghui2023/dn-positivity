#!/usr/bin/env python3
"""
Connes 6.6 攻击——子问题 C/A 起点：QW_λ 数值实现与最小特征向量
QW_λ(f,f) = Σ_v W_v(f·f~)——限制支撑 [λ⁻¹,λ]——Mellin 变量 t = log x ∈ [−L,L]

W_p(f) = (log p)Σ_m p^{−m/2}(f(p^m)+f(p^{−m}))——p ≤ λ 贡献
W_R(f) = (log 4π+γ)f(1) + ∫₁^∞ [f(x)+f(x⁻¹)−2x^{−1/2}f(1)] x^{1/2}/(x−x⁻¹) d*x

基：Mellin 变量上的三角基 F_j(t)——f(x) = F_j(log x)
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def W_R_diag(F, L, j, Nint=200):
    """W_R(F_j·F_j~)？——不对——Q(f,f) 用 f·f~——先算 Q(f,g) = ΣW_v(f·g~)
    简化：先探索 f = g = Σc_j F_j——Q(f) = ΣW_v(f·f~)——f~ = f(x⁻¹) 共轭"""
    pass

def main():
    print("="*70)
    print("QW_λ 数值探索——准备（结构确认——）")
    print("="*70)
    
    # 1. Weil 公式确认（数值——简单 f——）
    # 测试 f = 高斯型（Mellin 变量——）
    print("1. W_p 与 W_R 的数值测试:")
    print("   W_p(f) = (log p)Σ_m p^{−m/2}(f(p^m)+f(p^{−m}))")
    print("   W_R(f) = (log 4π+γ)f(1) + ∫₁^∞[...]")
    
    # 测试 f：Mellin 高斯 F(t) = e^{−t²}——f(x) = e^{−(log x)²}
    def f_test(x):
        return mp.e**(-(mp.log(x))**2)
    # W_2
    p = 2
    Wp = mp.log(p)*sum(p**(-m/2)*(f_test(p**m)+f_test(p**(-m))) for m in range(1, 20))
    print(f"   W_2(f) = {float(Wp):.6f}（f = e^{{−(log x)²}}——）")
    # W_R——数值积分
    gE = mp.euler
    WR = (mp.log(4*mp.pi)+gE)*f_test(1)
    # ∫₁^∞ [f(x)+f(1/x)−2x^{−1/2}f(1)] x^{1/2}/(x−x^{-1}) d*x——d*x = dx/x
    def integrand(x):
        return (f_test(x)+f_test(1/x)-2*x**(-0.5)*f_test(1)) * x**0.5/(x-x**(-1)) / x
    # 数值积分 1 到 大
    WR_val = mp.quad(integrand, [1, mp.inf])
    WR_total = (mp.log(4*mp.pi)+gE)*f_test(1) + WR_val
    print(f"   W_R(f) = {float(WR_total):.6f}")
    
    # 2. QW_λ 的基与矩阵（设计——）
    print("\n2. QW_λ 离散化设计:")
    print("   Mellin 变量 t ∈ [−L,L]——L = log λ——")
    print("   基：F_j(t) = cos(πjt/L)（偶——）j = 0,1,...,N")
    print("   f_j(x) = F_j(log x)——支撑 [λ⁻¹,λ]")
    print("   QW_λ(i,j) = Q(f_i, f_j)——需要 f_i·f_j~ 的 W_v——")
    print("   f_i·f_j~：乘法群卷积——Mellin 变量 = 卷积——")
    print("   → 矩阵元 QW(i,j) = Σ_v W_v(F_i * F_j)（乘法卷积——）")
    
    # 3. 关键：乘法卷积的 W_v 计算（在 Mellin 变量——）
    print("\n3. 简化路径（先探测——）:")
    print("   Connes 数值 [25] 已做——我们复算需要:")
    print("   a. 乘法卷积 (F_i*F_j)(t) = ∫F_i(u)F_j(t−u)du（Mellin——）")
    print("   b. W_p(F_i*F_j) = (log p)Σ_m p^{−m/2}(F_i*F_j)(±m log p)")
    print("   c. W_R 类似（积分——）")
    print("   → 全部可算（数值——）——但需细致实现——")

if __name__ == "__main__":
    main()
