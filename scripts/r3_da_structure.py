#!/usr/bin/env python3
"""
R3 考古 v2——D(a) 结构与 zero-blind 饱和测试（唐先生框架——）

D(a) = S_proj(γ_ρ)(a) − W(a)/2 ≥ 0（变分定理——逐点——）
目标：全-a 是否产生比逐点更强的 zero-blind 约束？

核心测试：
1. W(a)/2（Weil 素数侧——zero-blind——）与 Σ1/(a²+γ²)²（零点侧——）全 a 一致性
2. D(a) 小 a 极限（Σ1/γ⁴——Hadamard 可算——）——zero-blind？
3. D(a) 大 a 渐近结构
4. 找 zero-blind 线性泛函 L 使 L[D]=0（饱和——）
"""
import numpy as np
import mpmath as mp
from mpmath import zetazero, log, exp, sqrt, pi, euler, cosh

mp.mp.dps = 25

# ---------- 零点侧 S_proj（直接——用真实零点虚部——） ----------
def S_proj_zeros(gammas, a):
    return sum(1.0/(a*a + g*g)**2 for g in gammas)

# ---------- Weil 侧 W(a)/2（素数——zero-blind——） ----------
# 核：f_a 使 Σf_a(γ) = Σ1/(a²+γ²)²
# Weil 显式公式：Σ_γ g(γ) = (1/2π)∫g(t) ... 或 Fourier 侧：
# 标准：Σ_ρ h((ρ−½)/i) 型——用 8/31 校准的 Guinand-Weil
# W(a) = Σ_γ 1/(a²+γ²)² = 素数项 + Archimedean 项（对核 f_a(t) = 1/(a²+t²)² 的 Weil）
# Weil 公式（实变量形式——f 偶——）：
# Σ_γ f(γ) = (1/π)∫f(t) Im[ζ'/ζ] 类——不用——直接用显式公式：
# Σ_γ φ(γ) 对 φ(t)=1/(a²+t²)²——
# 用已校准事实（8/31）：S_proj(a) = W(a)/2——W 从 Weil 装配（素数 + Archimedean）

def weil_side_primes_only(a, primes, n_max=100000):
    """素数项近似（检验收敛——核 f̂_a(u) = (π/(2a³))(1+2πa|u|)e^{−2πa|u|}——）
    Weil 素数项：Σ_{p^k} log(p) p^{−k/2} f̂_a(k log p)——归一化——"""
    # 只算素数项（不含 Archimedean——不完全——但看结构——）
    total = mp.mpf('0')
    for p in primes:
        lp = log(p)
        k = 1
        pk = p
        while pk < n_max:
            u = k*lp
            fh = (pi/(2*a**3)) * (1 + 2*pi*a*u) * exp(-2*pi*a*u)
            total += log(p) * pk**(-0.5) * fh
            pk *= p
            k += 1
    return total

def main():
    print("="*70)
    print("R3 考古 v2：D(a) 结构与 zero-blind 饱和测试")
    print("="*70)
    
    # 零点（前 200——）
    N = 200
    gammas = [float(zetazero(k).imag) for k in range(1, N+1)]
    print(f"零点: 前 {N}（γ 到 {gammas[-1]:.1f}）")
    
    # 素数（Weil 素数项——）
    primes = list(mp.primes(2000))
    
    # 1. S_proj(a) 零点侧 vs Weil 素数项（全 a——）
    print("\n1. 零点侧 vs Weil 素数项（截断 200 零点 vs 素数 n≤1e5——）:")
    print(f"{'a':>6} {'S_proj_zeros':>16} {'Weil_prime_terms':>18} {'比值':>8}")
    a_vals = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0]
    for a in a_vals:
        sz = S_proj_zeros(gammas, a)
        wp = weil_side_primes_only(a, primes)
        ratio = sz/wp if wp != 0 else float('inf')
        print(f"{a:>6.1f} {sz:>16.6e} {wp:>18.6e} {ratio:>8.4f}")
    print("  （比值非 1——因为零点截断 200 + Archimedean 项缺失 + 归一化——")
    print("   只用于看 a-依赖结构——）")
    
    # 2. 小 a 极限：Σ1/γ⁴（a→0——）
    print("\n2. 小 a 极限 Σ1/γ⁴（a→0——）——Hadamard 对照:")
    s4 = sum(1.0/g**4 for g in gammas)
    s4_more = sum(1.0/g**4 for g in gammas[:50])
    print(f"  前 50: {s4_more:.6f}——前 200: {s4:.6f}（收敛快——Σ1/γ⁴——）")
    # 全和（外推——尾部 ~ ∫dN/γ⁴——N(T)~T logT/2π——dN ~ logT/2π dT——∫_{T0}^∞ logT/T⁴ dT ~ 小——）
    # 已知：Σ_γ 1/(¼+γ²) = ½(γ_E + log(4π)) − 1 类（从 ξ'/ξ 展开——）
    # Σ1/(γ²+¼) 可算——但 Σ1/γ⁴ 不同——需要更高阶
    print("  对照：Σ_γ 1/(¼+γ²)（从 Hadamard 无条件——）: ")
    # ξ(s) = ξ(0)Π(1−s/ρ)——ξ'/ξ(s) = Σ(1/(s−ρ) + 1/ρ)——s=½: ξ'/ξ(½) = Σ(1/(½−ρ)+1/ρ)
    # 已知公式：Σ_γ 1/(γ²+¼) = ½ log(4π) + γ_E/2 − 1？——验证数值——
    from mpmath import zeta, digamma, pi as mppi, euler as meuler, log as mlog
    # Σ_ρ 1/(ρ(1−ρ)) 类——实际用：
    # 1/(¼+γ²) = ?——(ρ−½)(1−ρ−½) = −(ρ−½)²——γ²+¼ = −(ρ−½)² 当 β=½
    # Σ_γ 1/(γ²+¼) = −Σ 1/(ρ−½)²（在线——）——Σ1/(ρ−½)² 从 ξ'/ξ 二阶——无条件——
    # ξ'/ξ(s) = B + Σ(1/(s−ρ) + 1/ρ)——ξ'/ξ(½+it) 展开——Σ1/(ρ−½)² 可从 s=½ 的二阶导——
    # 数值验证：Σ1/(γ²+¼)（前 200——）
    s_half = sum(1.0/(g*g + 0.25) for g in gammas)
    print(f"  前 200 Σ1/(γ²+¼) = {s_half:.6f}")
    # 理论（无条件——从 ξ'）：ξ'/ξ(s) 在 s=½ 的 Laurent——(ξ'/ξ)'(½) = −Σ1/(ρ−½)²
    # = Σ1/(γ²+¼)（在线——）——数值对照已知常数：
    # 文献：Σ_γ 1/(γ²+¼) = ½[log 4π + γ_E] − 1 + ... ？——直接算：——
    # 用 zeta 二阶：−(ξ'/ξ)'(½)——ξ = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)——数值——
    # 略——先记录结构——
    
    # 3. 渐近结构：a 大——S_proj ~ N_eff/a⁴
    print("\n3. 大 a 渐近（a⁴·S_proj → 零点数——）:")
    for a in [5.0, 8.0, 12.0, 20.0]:
        sz = S_proj_zeros(gammas, a)
        print(f"  a={a:>5.1f}: a⁴·S_proj = {a**4*sz:.4f}（→ 有效零点数——应 < 200——截断效应——）")
    
    # 4. 结构测试：D 的逐点符号 + 导数（用在线零点——D=0 机器精度——验证——）
    print("\n4. 一致性验证（真实零点在线——D(a) = S_proj − Weil = 0?——）:")
    # 注意：真实零点在线——S_proj(γ_ρ) = S_proj(γ_k)——D=0 是"事实"（非约束证明——）
    # Weil 侧完整计算需要 Archimedean + 归一化——此处只验证零点侧 S_proj 的自洽结构
    print("  （Weil 完整装配已在 8/31 验证（D1.3b——a≥2.5 机器精度——）——")
    print("   本轮聚焦：zero-blind 约束搜索——见下方结论——）")

if __name__ == "__main__":
    main()
