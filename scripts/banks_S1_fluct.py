#!/usr/bin/env python3
"""
Σ₁ 涨落结构分析：Σ₁(T) − 主项随 T 的轨迹
主项 = −(μ/φ)·T/(2πξ)（Banks——）
问题：涨落 ~O(1)？~√T？——有无界/振荡结构——来源（δ_k？边界？）
"""
import numpy as np
from math import pi, log, sqrt

def chi_X(g):
    import cmath
    t = g
    if t < 1: return complex(0, 0)
    phase = 1j*t*cmath.log(t/(2*pi*cmath.e))
    return cmath.exp(complex(-1j*pi/4)) * cmath.exp(phase)

def main():
    print("="*70)
    print("Σ₁ 涨落扫描——ξ=1/2——ζ 零点 ξ 扭曲和 − 主项")
    print("="*70)
    
    z = np.load('/tmp/zeros_odlyzko_100k.npy')
    xi = 0.5
    m, q = 1, 2
    mu_phi = -1.0  # μ(2)/φ(2)
    coeff = -(mu_phi)/(2*pi*xi)  # 主项系数 ~ +1/π
    
    # 扫描：在每个零点处记录 Σ₁(T) − 主项
    # Σ₁(T) 在 T=γ_k 处 = 累积到 k——主项 = coeff·γ_k
    cum = 0j
    flucts = []
    Ts = []
    for g in z[:30000]:
        term = xi**(-(0.5+1j*g)) * chi_X(g)
        cum += term
        main = coeff * g
        fluct = cum - main  # 复数涨落
        flucts.append(fluct)
        Ts.append(g)
    
    flucts = np.array(flucts)
    Ts = np.array(Ts)
    
    # 分段统计
    print(f"\n扫描 {len(flucts)} 零点——γ到 {Ts[-1]:.0f}")
    print(f"端点涨落: {flucts[-1].real:+.2f}{flucts[-1].imag:+.2f}i")
    
    print("\n分段 max|涨落|（每 5000 零点——）:")
    for i in range(0, len(flucts), 5000):
        seg = flucts[i:i+5000]
        print(f"  零点{i+1}-{i+len(seg)}: γ={Ts[i]:.0f}-{Ts[min(i+4999,len(flucts)-1)]:.0f}"
              f"——max|涨落|={np.max(np.abs(seg)):.2f}——末值={seg[-1].real:+.2f}{seg[-1].imag:+.2f}i")
    
    # 涨落的实部轨迹的振荡——找主频
    print("\n涨落实部——谱分析（每 100 零点采样——）:")
    import numpy.fft as fft
    sample = flucts[::50].real  # 每 50 零点
    N = len(sample)
    spec = np.abs(fft.fft(sample - sample.mean()))**2
    freqs = fft.fftfreq(N, 50)  # 每 50 零点一个样本——频率单位 1/零点
    top = np.argsort(spec)[-5:][::-1]
    print("  主频（1/零点数——）:")
    for idx in top:
        if freqs[idx] > 0:
            print(f"    频率 {freqs[idx]:.4f}/零点——周期 {1/freqs[idx]:.1f} 零点——功率 {spec[idx]:.0f}")
    
    # 涨落 vs √T 和 O(1)
    print("\n量级检查:")
    for T in [2000, 5000, 10000, 20000]:
        idx = np.searchsorted(Ts, T)
        if idx < len(flucts):
            print(f"  T={T}: |涨落|={abs(flucts[idx]):.2f}——√T={sqrt(T):.1f}——logT={log(T):.1f}")

if __name__ == "__main__":
    main()
