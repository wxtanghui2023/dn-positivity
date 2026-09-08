#!/usr/bin/env python3
"""
S̄ 变号频率的 Rice 分析
离散 Rice：零交叉率 ≈ (1/π)·arccos(ρ₁)——ρ₁ = S̄ 一步自相关（实测 0.54——）
预测：率 ≈ arccos(0.54)/π ≈ 0.32——每 3.1 步（实测 3.4——）✓ 接近

问题：
1. ρ₁ 的谱表示——能否从 S̄ 的谱（a_p——）无条件算？
2. 谱截断（Nyquist——p~90——）的影响
3. 变号频率 → M 有界的严格化路径
"""
import numpy as np
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def main():
    print("="*70)
    print("S̄ 变号频率 Rice 分析")
    print("="*70)
    
    K = 100000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    
    def IntN0(t):
        if t <= 1: return 0.0
        return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
    
    kk = np.arange(1, K)
    IntN = np.array([IntN0(t) for t in z[:K]])
    Sbar = kk - (IntN[1:] - IntN[:-1])/dg
    
    # 1. 实测变号率
    signs = np.sign(Sbar)
    flips = np.sum(signs[:-1] != signs[1:])
    rate = flips/len(Sbar)
    print(f"\n1. 实测：变号率 = {rate:.4f}（每 {1/rate:.2f} 步——）")
    
    # 2. Rice 预测（离散——）：率 = arccos(ρ₁)/π
    rho1 = np.corrcoef(Sbar[:-1], Sbar[1:])[0,1]
    print(f"   ρ₁ = {rho1:+.4f}——Rice 预测率 = {np.arccos(rho1)/pi:.4f}（每 {pi/np.arccos(rho1):.2f} 步——）")
    
    # 3. ρ₁ 的谱表示——用拟合的 a_p
    # S̄ ≈ Σ_p a_p sin(γ log p)——ρ₁ = Σ a_p² cos(log p · Δγ̄)/Σ a_p²（近似——）
    # Δγ̄ = 平均间距
    dg_avg = np.mean(dg)
    print(f"\n3. 谱预测 ρ₁（用理论 a_p = -(1/π)/(p^{1/2}log p)——）:")
    # 理论 a_p² ~ 1/(p log²p)——权重
    ps = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    ps = ps[ps <= 1000]  # 截断
    
    # cos 权重（自相关——）Σa²cos(λΔγ)/Σa²
    num = 0.0
    den = 0.0
    for p in ps:
        a2 = 1.0/(p * log(p)**2)  # a_p² 理论（~——）
        phase = log(p) * dg_avg
        num += a2 * np.cos(phase)
        den += a2
    rho1_spectral = num/den
    print(f"   ρ₁(谱——p≤1000——) = {rho1_spectral:+.4f}")
    print(f"   （对比实测 ρ₁ = {rho1:+.4f}——）")
    if abs(rho1_spectral) < 1:
        print(f"   谱 Rice 率 = {np.arccos(rho1_spectral)/pi:.4f}")
    
    # 4. Nyquist 截断检查（不同 p 截断——）
    print(f"\n4. 谱 ρ₁ 的 p 截断敏感性:")
    for pcut in [10, 30, 90, 300, 1000]:
        psub = ps[ps <= pcut]
        num = sum(1.0/(p*log(p)**2)*np.cos(log(p)*dg_avg) for p in psub)
        den = sum(1.0/(p*log(p)**2) for p in psub)
        print(f"   p≤{pcut:>4}: ρ₁ = {num/den:+.4f}")
    
    # 5. 变号率对 M 界的含义
    print(f"\n5. 变号率 → M 界:")
    print(f"   若变号率 ≥ r（无条件——）——每段 ≤ 1/r 步——")
    print(f"   每段面积 ≤ (1/r)·max|S̄|·Δγ̄ ~ (1/0.32)·0.5·0.7 ~ 1.1")
    print(f"   M 的游程需要面积序列的相关控制——仍开放")

if __name__ == "__main__":
    main()
