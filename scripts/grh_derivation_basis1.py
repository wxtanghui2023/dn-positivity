#!/usr/bin/env python3
"""
严格化推导——基础验证 1：
判据 D 的有限分析重构（从 F 本身——不经零点枚举——）
D = Σq(γ_ρ) − Σq(t_ρ)（判据的差——）
其中 Σq(γ_ρ) = (1/π)∫q d[arg F] − ∫q dN₀（Stieltjes——零点跳跃计入——）
验证：对 ζ（RH 数值成立——零点在线——）——D 应该 = 0——
以及——Σq(γ) 的 Stieltjes 表达式是否精确（8/31 bug 是否可解——）
"""
import numpy as np
from math import log, pi

# q(t) = 1/(1+t²)²——测试函数（8/31 的——）
def q(t):
    return 1.0/(1+t*t)**2

def theta(t):
    """ζ 的 Riemann-Siegel θ——Gamma 相位"""
    if t < 10: t = 10.0
    z = 0.25 + 0.5j*t
    lz = np.log(z)
    lg = (z-0.5)*lz - z + 0.5*np.log(2*np.pi) + 1.0/(12*z)
    return float(np.imag(lg)) - 0.5*t*np.log(pi)

def N0(t):
    return theta(t)/pi + 1

def main():
    print("="*70)
    print("基础验证：Σq(γ_ρ) 的 Stieltjes 重构")
    print("="*70)
    
    z = np.load('data/zeros_odlyzko_100k.npy')
    # 用前 2000 零点（γ < ~3000）
    z = z[:2000]
    print(f"零点: {len(z)}——γ范围: {z[0]:.1f} 到 {z[-1]:.1f}")
    
    # 1. 直接算 Σq(γ_ρ)（从零点——）
    S_direct = np.sum(q(z))
    print(f"\n1. Σq(γ_ρ)（直接——从零点——）= {S_direct:.10f}")
    
    # 2. Stieltjes 重构：(1/π)∫q d[arg ζ] − ∫q dN₀
    # arg ζ(½+it) 的跳跃：在零点 γ_ρ 处跳 π（ζ 穿过——符号 ±π——）
    # (1/π)∫q d[arg ζ] = Σ q(γ_ρ)·(跳跃/π)——跳跃 = ±π——所以 = Σ±q(γ_ρ)
    # ——但"跳跃的符号"（+π 或 −π——）——ζ 在零点穿过实轴的方向——
    # 简化假设：跳跃都是 +π（arg ζ 连续分支——零点处 +π——）
    # 实际上 arg ζ(½+it) 的净跳跃——每零点 ±π——Σ 符号 = S 相关——
    # 这里——(1/π)∫q d[argζ] 用"总变差"版——不对——需要净跳跃
    # ——让我们用数值：arg ζ 的连续分支——太难（需要 ζ 值——）
    # 改用：Σq(γ) 的 N(t) 积分——∫q dN——N 的跳跃在零点（1——）
    # ∫q dN(t) = Σq(γ_ρ)（N 在 γ_ρ 跳 1——）——直接——trivial——
    # ——真正的 Stieltjes：N(t) = (1/π)arg ζ + N₀ + 1（Backlund——）
    # dN = (1/π)d[arg ζ] + dN₀——所以 ∫q dN = (1/π)∫q d[argζ] + ∫q dN₀
    # Σq(γ) = (1/π)∫q d[argζ] + ∫q dN₀——（N 的定义——）
    # 所以 (1/π)∫q d[argζ] = Σq(γ) − ∫q dN₀——（8/31 的式子——）
    # ——但——8/31 写的是 Σq(γ) = (1/π)∫q d[argζ] − ∫q dN₀——差个符号？
    # ——N(t) = (1/π)arg ξ(½+it) + 1？——arg ξ = arg ζ + arg Γ——N₀ 含 θ——
    # ——让我直接数值验证：∫q dN（用零点——Σq(γ)——）vs (1/π)∫q d[argζ] ± ∫q dN₀
    
    # ∫q dN₀（数值——N₀ 光滑——）
    # 用分部积分：∫q dN₀ = ∫q(t)N₀'(t)dt——N₀'(t) = (1/2π)log(t/2π)（RvM——）
    ts = np.linspace(10, z[-1], 100000)
    N0p = np.log(ts/(2*pi))/(2*pi)
    int_q_dN0 = np.trapz(q(ts)*N0p, ts)
    print(f"2. ∫q dN₀ = {int_q_dN0:.10f}（N₀' = (1/2π)log(t/2π)——）")
    
    # (1/π)∫q d[arg ζ]——用 Backlund：arg ζ 的净跳跃 = π·(N(t) − N₀(t) − 1) 的变化——
    # 实际上——Σq(γ) 在 [γ₁, γₙ] = ∫q dN——而 dN = dN₀ + (1/π)d[argζ]——（N = N₀ + (1/π)argζ + 1——）
    # 所以 Σq(γ) = ∫q dN₀ + (1/π)∫q d[argζ]——（在零点区间内——端点注意——）
    # ⟹ (1/π)∫q d[argζ] = Σq(γ) − ∫q dN₀——检验：
    lhs = S_direct - int_q_dN0  # (1/π)∫q d[argζ] 的估计
    print(f"3. (1/π)∫q d[argζ] ≈ Σq(γ) − ∫q dN₀ = {lhs:.10f}")
    
    # 8/31 的式子：Σq(γ) = (1/π)∫q d[argζ] − ∫q dN₀——如果这是对的——
    # (1/π)∫q d[argζ] = Σq(γ) + ∫q dN₀——与我们的差 2∫q dN₀——符号问题！
    print(f"   ——8/31 式子给 (1/π)∫q d[argζ] = Σq(γ) + ∫q dN₀ = {S_direct + int_q_dN0:.10f}")
    print(f"   ——两种相差 2∫q dN₀ = {2*int_q_dN0:.10f}——【符号约定问题——需确认——】")
    
    # arg ζ 的实际跳跃——正负交替（S(t) 的——）——净跳跃的符号——
    # (1/π)∫q d[argζ] = Σ±q(γ)——（每零点 ±π 跳跃——符号 = ζ 穿过的方向——）
    # 如果符号交替（近似——）——Σ±q(γ) 比 Σq(γ) 小（抵消——）
    # ——用 S(γ_k) 的跳跃结构（右极限 mean +½——）——跳跃符号与 Gram 相关——
    
    print("\n——符号问题是 8/31 bug 的核心——需要 arg ζ 的连续分支——")
    print("——下一步：用 Riemann-Siegel Z(t) 的符号（零点处 Z 变号——）确定跳跃符号——")

if __name__ == "__main__":
    main()
