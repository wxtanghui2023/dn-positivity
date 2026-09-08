#!/usr/bin/env python3
"""
Landau-Gonek 路径验证：M_p2 的有界性
M_p2(T) = a2·Σ_k sin(γ̄_k log 2)·Δγ_k——需要证明有界（数值 1.02——）
Landau-Gonek：Σ_{γ≤T} x^{iγ} = 素数项 + O(误差)——无条件

如果 Σ_k sin(γ_k log 2)Δγ 能表达成 Landau-Gonek 的积分——有界可证
验证：M_p2 vs 连续积分 a2(1-cos(T log 2))/log 2——差的界（Riemann 和误差——）
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
    print("Landau-Gonek 路径验证（M_p2——）")
    print("="*70)
    
    K = 100000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    a2 = -0.20921
    
    # M_p2 数值（先 k——）
    M_p2 = a2 * np.cumsum(np.sin(mid*log(2))*dg)
    
    # 连续积分理论：a2(1-cos(T log 2))/log 2——注意 T 是 γ 空间——用 t=mid
    theory = a2 * (1 - np.cos(mid*log(2)))/log(2)
    
    # 差（Riemann 和误差——）
    err = M_p2 - theory
    print(f"\n1. M_p2 vs 连续积分理论:")
    print(f"   max|M_p2| = {np.abs(M_p2).max():.4f}")
    print(f"   max|理论| = {np.abs(theory).max():.4f}")
    print(f"   max|误差| = {np.abs(err).max():.4f}")
    
    # 误差的界（Landau-Gonek 能给什么？——）
    # 误差 = Σ_k sin(γ̄ log 2)Δγ - ∫sin(t log 2)dt
    # = Riemann 和误差——与零点分布（N(t)——）相关
    # 分部：Σ_k f(γ̄_k)Δγ = ∫f(t)dN(t)（Stieltjes——N 阶梯——）
    # ∫f dN = ∫f dN0 + ∫f dS（N = N0 + S——）
    # ∫f dN0 = ∫f N0' dt = ∫sin(t log2)N0'(t)dt ≈ ∫sin(t log2)·(log(t/2π)/2π)dt
    # ——注意 N0' 不是常数——所以理论积分应该带 N0' 权重！
    
    # 修正理论：∫_0^T sin(t log 2)N0'(t)dt——N0' = log(t/2π)/2π
    N0p = np.log(mid/(2*pi))/(2*pi)
    # ∫sin(t log2)·N0'(t)dt——数值（累积——）
    theory2 = a2 * np.cumsum(np.sin(mid*log(2)) * N0p * dg)
    err2 = M_p2 - theory2
    print(f"\n2. 修正理论（带 N0' 权重——）:")
    print(f"   max|M_p2| = {np.abs(M_p2).max():.4f}")
    print(f"   max|误差2| = {np.abs(err2).max():.4f}")
    
    # 3. 误差2 的行为——是否 O(1)？
    print(f"\n3. 误差2 分段 max（每 20000——）:")
    for i in range(0, K, 20000):
        seg = np.abs(err2[i:i+20000])
        print(f"   k={i:>6}-{i+20000}: max|误差2| = {seg.max():.4f}")
    
    # 4. S 部分（∫f dS——）的贡献——就是误差
    # ∫f dS 分部 = f·S|边界 - ∫S·f'——S 的积分（M——）循环？
    print(f"\n4. 理论：误差2 = ∫sin(t log2)dS(t)（分部——）")
    print(f"   = sin(T log2)S(T) - log2·∫cos(t log2)S(t)dt")
    print(f"   ——∫S·cos(t log2)——加权 M——如果 S 的积分有界——这个也有界？")

if __name__ == "__main__":
    main()
