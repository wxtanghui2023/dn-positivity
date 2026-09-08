#!/usr/bin/env python3
"""
桥检验：M(T) = ∫_0^T S（裸——）vs ∫S·g_T（光滑——）
Σδ=O(1) 定理给了 ∫S·g（光滑 g——）= O(1)
如果 M(T) ≈ ∫S·g_T + O(1)——M(T)=O(1) 就成（用光滑逼近——）

设计 g_T：光滑——≈1 在 [0,T]——在 [T, T+w] 过渡到 0
检验：M(T)（直接——零点数据——）vs ∫S·g_T——差是否 O(1)
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

def N0(t):
    """Riemann-von Mangoldt 主项"""
    if t <= 1: return 0
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

def S_value(k, z):
    """S(γ_k) = k - N0(γ_k)（右极限——零点数 k 在 γ_k 前——）"""
    return k - N0(z[k-1])

def main():
    print("="*70)
    print("M(T) vs ∫S·g_T 光滑逼近桥检验")
    print("="*70)
    
    # 用 200k 零点（快速——）
    K = 200000
    z = load_zeros(K)
    print(f"零点到 γ={z[-1]:.0f}（K={K}——）")
    
    # M(T) 的精确计算：M(T) = ∫_0^T S(t)dt
    # S(t) = N(t) - N0(t)——N(t) 阶梯（跳 γ_k——）
    # ∫_0^T S = Σ_{γ_k≤T}(T-γ_k)·1 - ∫_0^T N0(t)dt + ∫_0^T... 
    # 直接：M(T) = Σ_{γ_k≤T}(T - γ_k) - [∫N0 的精确]
    # ∫_0^T N0(t)dt——N0 有显式积分吗？——N0(t) = (t/2π)(log(t/2π)-1) + 7/8
    # ∫N0 = (1/2π)[(t²/2)(log(t/2π) - 3/2)·？——分部——用数值
    def int_N0(T):
        # ∫_0^T N0(t)dt 数值（Simpson——）
        if T < 10: return 0.0
        ts = np.linspace(1, T, 20001)
        vals = N0(ts)
        return np.trapz(vals, ts)
    
    def M_direct(T):
        # Σ_{γ_k≤T}(T-γ_k) - ∫_0^T N0(t)dt + T（+1 的积分——）
        # S = N - N0——∫S = ∫N - ∫N0——∫N = Σ_{γ_k≤T}(T-γ_k)（阶梯积分——）
        # 但 S = N - θ/π - 1？——不同定义——S(t) = N(t) - N0(t) 这里用 N0 含 7/8
        idx = np.searchsorted(z, T)
        sum_Tg = sum(T - z[i] for i in range(idx))
        return sum_Tg - int_N0(T)
    
    # 采样 T
    print("\nM(T) 直接计算（200k 零点——）:")
    for T in [1000, 5000, 10000, 20000, 50000]:
        M = M_direct(T)
        print(f"   T={T:>6}: M(T) = {M:+.4f}")
    
    # 问题：M(T) 计算需要 ∫N0——大数相减——检查量级
    T = 20000
    idx = np.searchsorted(z, T)
    sum_Tg = sum(T - z[i] for i in range(idx))
    intN = int_N0(T)
    print(f"\nT=20000: Σ(T-γ_k) = {sum_Tg:.2f}——∫N0 = {intN:.2f}——差 = {sum_Tg-intN:+.4f}")
    print(f"（大数相减——精度检查——）")

if __name__ == "__main__":
    main()
