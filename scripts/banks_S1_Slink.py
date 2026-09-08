#!/usr/bin/env python3
"""
Σ₁ 涨落机制：与零点 S 修正（相位均匀性）的连接
γ_k = N⁻¹(k)——γ_k 的精确值 = N₀ 反转主项 + S(γ_k) 修正
φ(γ_k) 的修正 ~ 2πS(γ_k)——Σ₁ 涨落 ↔ Σ[S(γ_k)−½]（相位均匀性——）
数值验证：Σ₁ 涨落 vs Σ[S(γ_k)−½] 的累积对比
"""
import numpy as np
from math import pi, log
import cmath

def chi_X(g):
    t = g
    if t < 1: return complex(0, 0)
    phase = 1j*t*cmath.log(t/(2*pi*cmath.e))
    return cmath.exp(complex(-1j*pi/4)) * cmath.exp(phase)

def N0(t):
    """零点计数主项——(t/2π)log(t/2πe) + 7/8"""
    if t < 2: return 0
    return (t/(2*pi))*log(t/(2*pi*cmath.e).real) + 7.0/8

def main():
    print("="*70)
    print("Σ₁ 涨落 vs Σ[S(γ_k)−½]（相位均匀性）")
    print("="*70)
    
    z = np.load('/tmp/zeros_odlyzko_100k.npy')
    xi = 0.5
    coeff = 1.0/pi
    
    cum_xi = 0j       # Σ₁ 累积
    cum_S = 0.0       # Σ[S(γ_k)−½] 累积（相位均匀性）
    S_k_sum = 0.0     # ΣS(γ_k)
    
    # 记录几个检查点
    fluct_at = {}
    Ssum_at = {}
    
    for k, g in enumerate(z[:30000]):
        n = k + 1  # 第 n 个零点
        # Σ₁ 项
        term = xi**(-(0.5+1j*g)) * chi_X(g)
        cum_xi += term
        # S(γ_k) = N(γ_k) − N₀(γ_k) − 1——N(γ_k) = n（第 n 零点——γ_k 处计数 = n——）
        # 但 S 在 γ_k 的"跳跃值"——用右极限 S(γ_k⁺) = n − N₀(γ_k) − 1 + (跳跃/2)？
        # 简化：S_mid = n − N₀(γ_k) − 1（N(γ_k) 取 n——阶梯中间——）
        S_mid = n - N0(g) - 1
        S_k_sum += S_mid
        cum_S += (S_mid - 0.5)
        
        if n in [1000, 5000, 10000, 20000, 30000]:
            fluct = cum_xi - coeff*g
            fluct_at[n] = fluct
            Ssum_at[n] = cum_S
    
    print(f"\n零点 S(γ_k) 统计（前 30000——）:")
    print(f"  mean S(γ_k) = {S_k_sum/30000:.4f}（期望 ~½——）")
    print(f"  Σ[S(γ_k)−½] = {cum_S:+.2f}（相位均匀性——O(1)？——）")
    
    print(f"\n检查点对比（Σ₁ 涨落 vs Σ[S−½] 累积——）:")
    for n in [1000, 5000, 10000, 20000, 30000]:
        f = fluct_at[n]
        print(f"  零点{n:>6}: Σ₁涨落={f.real:+8.2f}{f.imag:+6.2f}i——|涨落|={abs(f):6.2f}"
              f"——Σ[S−½]={Ssum_at[n]:+8.2f}")

if __name__ == "__main__":
    main()
