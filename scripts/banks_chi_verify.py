#!/usr/bin/env python3
"""
精确验证：𝒳(1−ρ) 的 Stirling 近似 vs mpmath 精确值
——确认 Σ₁ 数值（~±T/(2π)——ξ 无关——）是否可信——
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 20
from math import pi, log

def chi_exact(g):
    """𝒳(1−ρ) 精确——ρ=½+iγ——𝒳(s) = 2(2π)^{−s}Γ(s)cos(πs/2)——s = ½−iγ"""
    s = mp.mpc(0.5, -g)
    return 2 * (2*mp.pi)**(-s) * mp.gamma(s) * mp.cos(mp.pi*s/2)

def chi_stirling(g):
    """Stirling 近似——𝒳(½−iγ) = conj(𝒳(½+iγ))——𝒳(½+iγ)≈e^{−iπ/4}e^{iγ log(γ/2πe)}"""
    import cmath
    t = g
    phase = 1j*t*cmath.log(t/(2*pi*cmath.e))
    chi_pos = cmath.exp(complex(-1j*pi/4)) * cmath.exp(phase)
    return chi_pos.conjugate()

def main():
    print("="*70)
    print("𝒳(1−ρ) 精确 vs Stirling——验证实现")
    print("="*70)
    z = np.load('data/zeros_odlyzko_100k.npy')
    print(f"\n前 5 个零点——𝒳(½−iγ) 对比：")
    for g in z[:5]:
        ce = chi_exact(float(g))
        cs = chi_stirling(float(g))
        print(f"  γ={g:>8.3f}: 精确 = {mp.nstr(ce, 8)}——Stirling = ({cs.real:+.4f}{cs.imag:+.4f}i)"
              f"——差 = {abs(complex(ce) - cs):.4f}")
    
    # 用精确 𝒳 算 Σ₁(T)——对 ξ=1/2——小 T——（前 100 零点——mpmath 慢——）
    print("\n" + "="*70)
    print("用精确 𝒳 重算 Σ₁(T)——ξ=1/2——前 200 零点")
    print("="*70)
    zsel = z[:200]
    T = zsel[-1]
    xi = 0.5
    S1_exact = 0j
    S1_stir = 0j
    for g in zsel:
        rho = 0.5 + 1j*g
        S1_exact += xi**(-rho) * complex(chi_exact(float(g)))
        S1_stir += xi**(-rho) * chi_stirling(float(g))
    print(f"T={T:.0f}——200 零点：")
    print(f"  Σ₁(精确) = {S1_exact.real:+10.3f}{S1_exact.imag:+10.3f}i")
    print(f"  Σ₁(Stir) = {S1_stir.real:+10.3f}{S1_stir.imag:+10.3f}i")
    print(f"  |Σ₁|/T：精确 {abs(S1_exact)/T:.4f}——Stirling {abs(S1_stir)/T:.4f}")
    # 预测（Banks：−(μ/φ)T/(2πξ)——ξ=1/2——μ/φ=−1——）= +T/π
    pred = T/pi
    print(f"  Banks 预测主项 −(μ/φ)T/(2πξ) = +T/π = {pred:.1f}")

if __name__ == "__main__":
    main()
