#!/usr/bin/env python3
"""
严格化推导——基础验证 2：修正符号问题
(1/π)∫q d[argζ] = Σ s_k·q(γ_k)——s_k = ±1（arg ζ 在零点 γ_k 的跳跃方向——）
跳跃方向：ζ(½+it) 穿过零点时 arg 变化 ±π——
——由 Riemann-Siegel Z(t) 的符号决定：Z(t) = e^{-iθ(t)}ζ(½+it)——实——
——ζ = Z·e^{iθ}——arg ζ = arg(Z e^{iθ}) = (θ mod π 的——) + arg Z——
——Z 实——Z 的符号变化（零点处——）给 arg 的 π 跳跃——
——Z 变号方向（+→− 或 −→+——）决定跳跃符号——

验证：Σ s_k q(γ_k)（符号修正——）vs (1/π)∫q d[argζ] 的期望
以及判据的 D 重构
"""
import numpy as np
from math import log, pi

def q(t):
    return 1.0/(1+t*t)**2

def zeta_half_approx(t):
    """用 Riemann-Siegel 近似算 Z(t)——只用于符号——"""
    # 简化：用 mpmath 太慢——用前几项的 Riemann-Siegel
    # Z(t) ≈ 2Σ_{n≤√(t/2π)} n^{-1/2}cos(θ(t) − t log n)——Riemann-Siegel
    import mpmath as mp
    mp.mp.dps = 12
    # 用 mpmath zeta 直接算（慢——只算少量点——）
    z = mp.zeta(mp.mpc(0.5, t))
    # Z(t) = e^{iθ}ζ——但我们需要的是 arg ζ 的跳跃——直接算 arg ζ
    return float(mp.arg(z))

def main():
    print("="*70)
    print("基础验证 2：arg ζ 跳跃符号（Z 变号——）")
    print("="*70)
    
    z = np.load('data/zeros_odlyzko_100k.npy')
    z = z[:200]  # 只前 200（mpmath 慢——）
    print(f"零点: {len(z)}")
    
    # 用 mpmath 算 arg ζ 在零点两侧的值——确定跳跃方向
    import mpmath as mp
    mp.mp.dps = 12
    signs = []
    for i, g in enumerate(z):
        # arg ζ 在 g 两侧（小偏移——）
        a1 = mp.arg(mp.zeta(mp.mpc(0.5, g - 0.01)))
        a2 = mp.arg(mp.zeta(mp.mpc(0.5, g + 0.01)))
        # 跳跃 = a2 − a1（mod 2π——）——接近 ±π——
        jump = a2 - a1
        # 规范化到 (−π, π]
        while jump > pi: jump -= 2*pi
        while jump <= -pi: jump += 2*pi
        signs.append(1 if jump > 0 else -1)
    
    signs = np.array(signs)
    print(f"跳跃方向: +{np.sum(signs>0)} / −{np.sum(signs<0)}——交替？")
    
    # Σ s_k q(γ_k)（符号修正——）
    S_signed = np.sum(signs * q(z))
    S_unsigned = np.sum(q(z))
    print(f"\nΣ q(γ)（全正——）= {S_unsigned:.8f}")
    print(f"Σ s_k q(γ)（符号——）= {S_signed:.8f}")
    
    # ∫q dN₀
    ts = np.linspace(10, z[-1], 50000)
    N0p = np.log(ts/(2*pi))/(2*pi)
    int_q_dN0 = np.trapz(q(ts)*N0p, ts)
    print(f"∫q dN₀ = {int_q_dN0:.8f}")
    
    # Backlund: N(t) = (1/π)arg ξ(½+it) + 1——arg ξ = arg ζ + θ——
    # dN = (1/π)d[arg ξ]——arg ξ 的跳跃（零点——）= arg ζ 的跳跃（θ 光滑——）
    # Σq(γ) = ∫q dN = (1/π)∫q d[argξ] = (1/π)∫q d[argζ] + (1/π)∫q dθ
    # (1/π)∫q d[argζ] = Σ s_k q(γ_k)（跳跃符号——）
    # (1/π)∫q dθ = ∫q θ'(t)/π dt——θ'(t) = N₀'(t)π？（θ/π + 1 = N₀——）
    # θ(t)/π + 1 = N₀(t)——θ' = πN₀'——(1/π)∫q dθ = ∫q N₀'dt = ∫q dN₀ ✓
    # 所以 Σq(γ) = Σs_k q(γ_k) + ∫q dN₀——检验：
    print(f"\n检验: Σs_k·q + ∫q dN₀ = {S_signed + int_q_dN0:.8f}")
    print(f"     Σq(γ)（直接——）= {S_unsigned:.8f}")
    print(f"     差 = {S_signed + int_q_dN0 - S_unsigned:.8f}")
    
    # 8/31 的正确式子应该是：Σq(γ) − ∫q dN₀ = Σs_k q(γ_k)（带符号——）
    print(f"\n8/31 式子的修正版: (1/π)∫q d[argζ] = Σs_k q(γ_k) = {S_signed:.8f}")
    print(f"   （8/31 用 Σq（全正——）是错的——应为 Σs_k q（带符号——））")

if __name__ == "__main__":
    main()
