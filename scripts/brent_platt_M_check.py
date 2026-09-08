#!/usr/bin/env python3
"""
Brent-Platt 框架对 M(T) 的验证
关键恒等式（Lemma 2——）：∫_T^∞ S(t)/t²dt = -(S₁(T)-c)/T² + 2∫_T^∞(S₁(t)-c)/t³dt

如果 M(T)=S₁(T)=O(1)（数值——）——尾部 ∫S/t² 应该 ~O(1/T²)
验证：用零点数据算 S(t)——算尾部积分——看量级
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

def N0_arr(t):
    t = np.maximum(t, 1.0)
    return (t/(2*pi))*np.log(t/(2*pi)) - t/(2*pi) + 7/8

def main():
    print("="*70)
    print("Brent-Platt 框架验证（M(T)——）")
    print("="*70)
    
    K = 200000
    z = load_zeros(K)
    
    # S(t) 在零点区间的值——S(t) = k - N0(t) 在 (γ_k, γ_{k+1})
    # 用密集采样算 S 的积分量
    def S_at(t):
        """S(t) = N(t) - N0(t)——N(t) = #{γ ≤ t}"""
        idx = np.searchsorted(z, t)
        return idx - N0_arr(t)
    
    # S₁(T) = M(T)——用闭式（前面——）
    def IntN0(t):
        if t <= 1: return 0.0
        return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
    
    # M(T) 到 T（零点数据——）——用 k 的递推 + 中间点修正
    # 简化：M(γ_k) 的递推——(前面算过——) 但需要任意 T 的 M(T)
    # M(T) = Σ_{γ≤T}(T-γ) - ∫_0^T N0 = N(T)·T - Σ_{γ≤T}γ - ∫N0(T)
    def M_of_T(T):
        idx = np.searchsorted(z, T)
        if idx == 0: return 0.0
        zsub = z[:idx]
        sum_g = zsub.sum()
        return idx*T - sum_g - IntN0(T)
    
    print("\n1. M(T) = S₁(T) 在几个 T:")
    for T in [10000, 50000, 100000, 150000, 200000]:
        print(f"   T={T:>7}: M = {M_of_T(T):+.4f}")
    
    # 2. 尾部 ∫_T^∞ S(t)/t²dt——用 Brent-Platt 的 (7) 验证
    # 从数据算 ∫_T^Tmax S/t²（Tmax = 最后零点——）+ 尾估计
    print("\n2. ∫_T^Tmax S(t)/t²dt（数值——）:")
    # 密集网格算 S——用零点精确
    # S(t) 逐段（k - N0(t)——）——积分精确：每段 ∫(k-N0(t))/t²dt
    def tail_integral(T, Tmax):
        # 段 [γ_k, γ_{k+1}] 与 [T, Tmax] 相交的部分
        total = 0.0
        k0 = np.searchsorted(z, T)
        k1 = np.searchsorted(z, Tmax)
        # T 到 γ_{k0}（如果 T < γ_{k0}——）
        if k0 > 0 and z[k0-1] < T:
            # 段 (γ_{k0-1}, γ_{k0})——但 T 在其中——需要 N(T) 在 T
            pass
        # 简化：只算零点到零点间的完整段
        for k in range(k0, k1):
            a = max(z[k], T)
            b = z[k+1] if k+1 < len(z) else Tmax
            if b <= a: continue
            # ∫_a^b (kk - N0(t))/t²dt——kk = N(t) = k+1 在 (γ_k, γ_{k+1})
            kk = k + 1
            # ∫ kk/t²dt = -kk/t |_a^b
            # ∫ N0(t)/t²dt——N0(t) = (t/2π)(log(t/2π)-1) + 7/8
            # N0/t² = (1/2π)(log(t/2π)-1)/t + 7/(8t²)
            # ∫ = (1/2π)[(1/2)log²(t/2π)·? - log t]... 
            # ∫ (log(t/a))/t dt = (1/2)log²(t/a)——∫ (log(t/a)-1)/t dt = (1/2)log²(t/a) - log t
            def F_int(t):
                # ∫ N0(u)/u² du 从某点——不定积分：
                # ∫ (1/2π)(log(u/2π)-1)/u du = (1/2π)[(1/2)log²(u/2π) - log(u)]
                # ∫ 7/(8u²) du = -7/(8u)
                return (1/(2*pi))*((0.5*log(t/(2*pi))**2) - log(t)) - 7/(8*t)
            int_N0 = F_int(b) - F_int(a)
            int_k = -kk/b + kk/a  # ∫ kk/t²dt from a to b = kk(1/a - 1/b)
            total += int_k - int_N0
        return total
    
    T = 50000
    Tmax = z[-1]
    ti = tail_integral(T, Tmax)
    print(f"\n   T={T}: ∫_T^{Tmax:.0f} S/t² dt = {ti:+.6f}")
    print(f"   理论（Brent-Platt——）：|尾部| ≤ (2A0+0.5A1+2A1 log T)/T²")
    A0, A1 = 2.067, 0.059
    bound = (2*A0 + 0.5*A1 + 2*A1*log(T))/T**2
    print(f"   显式界 ≈ {bound:.6f}——数值 {abs(ti):.6f}——比较")

if __name__ == "__main__":
    main()
