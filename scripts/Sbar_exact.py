#!/usr/bin/env python3
"""
S̄ 几乎周期分解的严格化探索
S̄_k = 区间 (γ_k, γ_{k+1}) 内 S 的平均
S(t) 的展开在逐点意义条件收敛——但区间平均（积分——）可能让 Abel/平均收敛合法

关键：S̄_k 的精确表达式——用 S(t) 的 Selberg 积分表示
S(t) = -(1/π)∫... 或 S 在区间的积分 = M 增量

目标：找到 S̄_k 的严格可证分解——无条件
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
    print("S̄ 分解严格化探索")
    print("="*70)
    
    K = 50000
    z = load_zeros(K)
    
    # S̄_k 精确：区间 (γ_k, γ_{k+1}) 的 S 平均
    # S(t) = N(t) - N0(t)——N(t)=k 在区间——所以 S̄_k = k - (1/Δγ)∫N0
    # 精确：S̄_k = k - ∫_{γ_k}^{γ_{k+1}}N0(t)dt/Δγ_k
    # 但 ∫N0 有显式形式！N0(t) = (t/2π)(log(t/2π)-1) + 7/8
    # ∫N0 dt = (t²/4π)(log(t/2π) - 3/2) + 7t/8？——分部积分——检查
    
    # ∫ t log(t/a) dt = (t²/2)log(t/a) - t²/4
    # ∫ (t/2π)(log(t/2π)-1)dt = (1/2π)[(t²/2)(log(t/2π)-1) - t²/4]·？
    # 直接：∫ (t/2π)log(t/2π)dt = (1/2π)[(t²/2)log(t/2π) - t²/4]
    # ∫ (t/2π)·(-1)dt = -t²/(4π)
    # ∫ (t/2π)(log(t/2π)-1)dt = (1/2π)[(t²/2)log(t/2π) - t²/4] - t²/(4π)
    #   = t²/(4π)·log(t/2π) - t²/(8π) - t²/(4π) = t²/(4π)·log(t/2π) - 3t²/(8π)
    # + ∫(7/8)dt = 7t/8
    # ∫N0 = t²/(4π)·log(t/2π) - 3t²/(8π) + 7t/8——验证导数
    # d/dt = t/(2π)·log(t/2π) + t²/(4π)·(1/t) - 3t/(4π) + 7/8
    #   = t/(2π)log(t/2π) + t/(4π) - 3t/(4π) + 7/8 = t/(2π)log(t/2π) - t/(2π) + 7/8 ✓
    
    def IntN0(t):
        """∫_0^t N0(u)du"""
        if t <= 1: return 0.0
        return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
    
    # S̄_k = k - [IntN0(γ_{k+1}) - IntN0(γ_k)]/Δγ_k
    # 直接算
    dg = np.diff(z[:K])
    IntN = np.array([IntN0(t) for t in z[:K]])
    k_range = np.arange(1, K+1)
    # S̄ 对区间 (γ_k, γ_{k+1})——k=1..K-1
    Sbar_exact = k_range[:-1] - (IntN[1:] - IntN[:-1])/dg
    
    # 之前的中点近似
    N0v = np.array([max(t,1.0) for t in z[:K]])
    # 用数组算 N0
    def N0_arr(t):
        return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8
    N0v = N0_arr(z[:K])
    kk = np.arange(1, K)
    S_left = kk - N0v[:-1]
    S_right = kk - N0v[1:]
    Sbar_approx = (S_left+S_right)/2
    
    print(f"\n1. 精确 S̄ vs 中点近似:")
    print(f"   corr = {np.corrcoef(Sbar_exact, Sbar_approx)[0,1]:.6f}")
    print(f"   max|差| = {np.abs(Sbar_exact-Sbar_approx).max():.6f}")
    
    # M 增量（精确——）= S̄_exact·Δγ = k·Δγ - (IntN 差)
    M_inc = Sbar_exact * dg
    M_cum = np.cumsum(M_inc)
    print(f"\n2. 精确 M(T)（用 IntN0 闭式——）:")
    print(f"   max|M| = {np.abs(M_cum).max():.4f}——末值 = {M_cum[-1]:+.4f}")
    
    # 3. 关键：S̄ 的结构——与 N0 曲率的关系
    # S̄_k = k - ΔIntN/Δγ——ΔIntN/Δγ ≈ N0(中点) + N0''·Δγ²/24（Euler-Maclaurin——）
    # S̄_k ≈ k - N0(mid) - N0''Δγ²/24——k - N0(mid) = S(mid)（近似——）
    # 所以 S̄_k ≈ S(γ̄_k) - N0''(γ̄_k)Δγ_k²/24——修正项（小——）
    print(f"\n3. S̄ 的分解：S̄_k = S(mid) - N0''Δγ²/24?")
    mid = (z[:-1]+z[1:])/2
    N0mid = N0_arr(mid)
    # S(mid) = k - N0(mid)（N(t)=k 在区间——）
    S_mid = kk - N0mid
    # N0'' = d/dt[t/(2π)log(t/2π) - t/(2π) + 7/8] = (1/2π)(log(t/2π)+1) - 1/(2π) = log(t/2π)/(2π)·？ 
    # N0'(t) = log(t/2π)/(2π)——N0'' = 1/(2πt)
    N0pp = 1.0/(2*pi*mid)
    corr_term = N0pp * dg**2/24
    Sbar_pred = S_mid - corr_term
    print(f"   corr(S̄_exact, S(mid) - N0''Δγ²/24) = {np.corrcoef(Sbar_exact, Sbar_pred)[0,1]:.8f}")

if __name__ == "__main__":
    main()
