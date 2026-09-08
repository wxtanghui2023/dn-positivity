#!/usr/bin/env python3
"""
P1-P4 元论证核心验证：
观测 F_f = ∫f(x)(ψ−x)dx——离轴零点 ρ* 的响应 δF ~ M[f](ρ*)/ρ*
M[f](s) = ∫f(x)x^{s−1}dx（Mellin——）

Dichotomy 定量形式：
1. 固定 f（zero-blind——）：响应随 γ* 衰减多快？（Riemann-Lebesgue——）
2. f 的谱含 γ*（响应大——）⟺ f 编码 γ*（不 zero-blind——）？
3. 不同光滑度 k 的衰减率对比（γ^{−k}——）
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def mellin_at(f_type, s):
    """测试函数 f 的 Mellin 变换在 s 的值——用数值积分"""
    sig, t = float(s.real), float(s.imag)
    # f 的 Mellin: M[f](s) = ∫₀^∞ f(x)x^{s−1}dx——换 x=e^u: ∫f(e^u)e^{su}du
    def integrand(u):
        x = np.exp(u)
        return f_type(x) * np.exp(sig*u) * np.cos(t*u)
    def integrand_im(u):
        x = np.exp(u)
        return f_type(x) * np.exp(sig*u) * np.sin(t*u)
    # 数值积分（u 从 -∞ 到 ∞——f 衰减快——截断）
    us = np.linspace(-20, 20, 20001)
    re = np.trapz([integrand(u) for u in us], us)
    im = np.trapz([integrand_im(u) for u in us], us)
    return complex(re, im)

def f_gauss(x):
    """高斯测试函数（C^∞——超快衰减——）"""
    return np.exp(-(np.log(x))**2)  # log-高斯

def f_compact3(x):
    """有限光滑紧支撑（C^3 类——）——在 x∈[e^{-2}, e^2] 支撑"""
    u = np.log(x)
    if abs(u) > 2:
        return 0.0
    # (1-u²/4)³——C^2 在边界
    return max(0, (1 - u**2/4)**3)

def main():
    print("="*70)
    print("Dichotomy 定量验证：固定 f 的响应衰减")
    print("="*70)
    
    # 1. 固定 f 的 Mellin 变换沿垂直线的衰减（Riemann-Lebesgue——）
    print("\n1. |M[f](β+iγ)| 随 γ 的衰减（β=0.6——离轴零点实部——）:")
    for fname, f in [("log-高斯(C^∞)", f_gauss), ("紧支撑C^2", f_compact3)]:
        print(f"\n   f = {fname}:")
        for gamma in [14, 50, 100, 200, 500]:
            s = complex(0.6, gamma)
            M = mellin_at(f, s)
            print(f"   γ={gamma:>5}: |M[f]| = {abs(M):.6e}")
    
    # 2. 响应对比：δF ~ M[f](ρ*)/|ρ*|
    print("\n2. 响应 |δF| ~ |M[f](ρ*)|/|ρ*|（固定 f——）:")
    for fname, f in [("log-高斯(C^∞)", f_gauss), ("紧支撑C^2", f_compact3)]:
        print(f"\n   f = {fname}:")
        for gamma in [14, 50, 100, 200]:
            s = complex(0.6, gamma)
            M = mellin_at(f, s)
            resp = abs(M)/gamma
            print(f"   γ={gamma:>5}: 响应 = {resp:.6e}——(相对 γ=14 的比值: {resp/(abs(mellin_at(f, complex(0.6,14)))/14):.4f})")
    
    # 3. 谱匹配测试：f 依赖 γ*（不 zero-blind——）才能响应大
    print("\n3. 谱匹配——f 振荡匹配 γ*（编码零点——）:")
    print("   若 f 含因子 e^{iγ*·log x}（匹配——）——M[f](β+iγ*) 大——")
    print("   但 f 的构造需要知道 γ*——不 zero-blind——")
    # 演示：f_γ*(x) = e^{−log²x}·e^{iγ* log x}——M 在 γ* 有峰
    for gamma_star in [100, 200]:
        def f_match(x, g=gamma_star):
            return np.exp(-(np.log(x))**2) * np.cos(g*np.log(x))
        vals = []
        for gamma in [gamma_star-10, gamma_star, gamma_star+10]:
            M = mellin_at(f_match, complex(0.6, gamma))
            vals.append(abs(M))
        print(f"   γ*={gamma_star}: |M[f_{{γ*}}]| 在 γ={gamma_star-10},{gamma_star},{gamma_star+10}: {['%.3e'%v for v in vals]}")

if __name__ == "__main__":
    main()
