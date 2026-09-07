#!/usr/bin/env python3
"""
子问题 B——k(u) 归一化校准
Riemann 原始（Connes 引用）：
Ξ(t) = 4∫₁^∞ d/dx[x^{3/2}ψ'(x)]·x^{−1/4}cos(½t log x)dx——ψ = theta
k(u) = u^{1/2}(π/2)Σ_{n≥1}(2πn²u²−3)n²u²e^{−πn²u²} 类？
先校准：Ξ(0) = ξ(½) 数值——然后调 k 使 k̂(0) = Ξ(0)
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 15

def xi_xi(t):
    s = 0.5 + 1j*t
    return mp.zeta(s) * 0.5*s*(s-1) * mp.pi**(-s/2) * mp.gamma(s/2)

def main():
    print("="*70)
    print("校准：Ξ(0) 与 k 的归一化")
    print("="*70)
    
    # 1. Ξ(0) = ξ(½)
    xi0 = xi_xi(0)
    print(f"Ξ(0) = ξ(½) = {complex(xi0):.6f}")
    
    # 2. Riemann 的 theta 函数 ψ(x) = Σe^{−n²πx}
    # k 的标准形式（Riemann 1859——）：
    # ξ(s) = ∫₀^∞ ψ'(x) x^{s/2−1}dx 类——或——
    # 用 Letter 的：Ξ(t) = 4∫₁^∞ d/dx[x^{3/2}ψ'(x)]x^{−1/4}cos(½t log x)dx
    # 令 Φ(x) = d/dx[x^{3/2}ψ'(x)]·x^{−1/4}——Ξ(t) = 4∫₁^∞Φ(x)cos(½t log x)dx
    # 或 Mellin：Ξ(t) = ∫₀^∞ k(u)u^{it}d*u——k(u) = ?——从 Φ 变换
    # 直接数值：用 theta 算 Ξ(t)——验证 zeta 路径
    print("\nΞ(t) 数值（zeta 路径——几个值——）:")
    for t in [0, 5, 10, 14.1347, 21.022]:
        xi = xi_xi(t)
        print(f"  Ξ({t:.4f}) = {complex(xi):.6e}")
    
    # 3. 用 theta 级数直接算 Ξ（交叉验证——）
    # ξ(s) = ½s(s−1)∫₀^∞ ψ'(x)... 复杂——直接用已知：Ξ 实值（t 实——）
    # 关键校准：k(u) 的 Mellin = Ξ——k(u) = E(h)——h 的常数需使匹配
    print("\n3. k 的常数校准:")
    # Riemann k：k(u) = 2Σ(2π²n⁴e^{9u}...)—不同参数化——跳过复杂——直接看 Letter h
    # Letter: h(u) = π/2·u²(2πu²−3)e^{−πu²}——k = E(h) = u^{1/2}Σh(nu)
    # k̂(0) = ∫k(u)d*u——数值——
    def h(u):
        return mp.pi/2 * u**2 * (2*mp.pi*u**2 - 3) * mp.e**(-mp.pi*u**2)
    # h 有负区（2πu²−3 < 0 当 u² < 3/(2π)——u < 0.69——）——所以 h 变号——k 也变号？
    # Riemann 的 k 应该正？——检查 h 的积分
    hint = mp.quad(lambda u: h(u), [0, mp.inf])
    print(f"  ∫h(u)du = {float(hint):.6f}（应=0？——h 是零积分组合——）")
    # k(u) = u^{1/2}Σh(nu)——k̂(0) = ∫k(u)/u du = ∫u^{−1/2}Σh(nu)du
    # = Σ∫u^{−1/2}h(nu)du = Σn^{−1/2}∫v^{−1/2}h(v)dv = ζ(½)·∫v^{−1/2}h(v)dv？
    # 不收敛（ζ(½) 发散级数——）——需要正则——说明 k 定义需仔细

if __name__ == "__main__":
    main()
