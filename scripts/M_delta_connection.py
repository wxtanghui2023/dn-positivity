#!/usr/bin/env python3
"""
M(T) 与 Σδ 的连接探索
已证：Σδ_k = O(1)（8/23——光滑加权——）
目标：M(T) = ∫_0^T S（裸积分——）——能否从 Σδ 或相关量推出？

关系：δ_k = Δγ_k - 1/N₀'(γ_k)——S 的跳跃相关
M(T) = Σ_{γ≤T}(T-γ) - ∫N0

探索：M(T) 与下列量的关系
A. Σδ 累积（已证 O(1)——）
B. S(γ_k) 的加权和
C. M(T) 的增量结构（dM/dT = S(T)——）
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
    print("M(T) 与 Σδ 连接探索")
    print("="*70)
    
    K = 200000
    z = load_zeros(K)
    print(f"零点到 γ={z[-1]:.0f}（K={K}——）")
    
    # δ_k
    dg = np.diff(z)
    Np = np.log(z[:-1]/(2*pi))/(2*pi)
    delta = dg - 1.0/Np
    Sd = np.cumsum(delta)
    
    # M(T) 在零点处：M(γ_k) = Σ_{j≤k}(γ_k-γ_j) - ∫_0^{γ_k}N0
    # 递推：M(γ_{k+1}) = M(γ_k) + k·(γ_{k+1}-γ_k) - ∫_{γ_k}^{γ_{k+1}}N0
    # 简化：用 Simpson 直接算几个 T 的 M(T)
    def int_N0(a, b):
        ts = np.linspace(a, b, 5001)
        return np.trapz(N0_arr(ts), ts)
    
    print("\n1. M(T) vs Σδ 累积（在零点处采样——）:")
    # M(γ_k)：Σ_{j≤k}(γ_k-γ_j) - ∫_0^{γ_k} N0
    # 递推计算（避免大数——用 float128——）
    # 直接用关系：M'(t) = S(t)——S(γ_k) = k - N0(γ_k)（右极限——）
    # M(γ_k) ≈ ∫_0^{γ_k} S——S 在 γ_k 跳跃——分段积分——数值
    # 用大步长直接：M(T) = Σ(T-γ_j) - ∫N0——前面已验证 O(1)
    print("   （前面已验证 M(T) ∈ [-0.68, -0.08]——O(1)——）")
    
    # 2. 关键探索：M(T) 的"增量"与 δ 的关系
    print("\n2. M(T) 的增量结构——dM/dT = S(T)——S 在零点间平滑")
    # S(t) 在 (γ_k, γ_{k+1}) 间 = k - N0(t)（N(t) = k 常数——）
    # M(γ_{k+1}) - M(γ_k) = ∫_{γ_k}^{γ_{k+1}} (k - N0(t))dt
    # = k·Δγ_k - ∫N0
    # 而 δ_k = Δγ_k - 1/N0'(γ_k)——相关！
    
    # 数值：相邻 M 差 vs k·Δγ - ∫N0
    print("\n3. M 的逐点结构（前几个零点——）:")
    # M(γ_k) 递推——用 float128 累积
    M_vals = np.zeros(K, dtype=np.float128)
    # M(γ_1) = 0 - ∫_0^{γ_1} N0 ≈ 0（N0 从 t~1 起——）
    # 递推 M_{k+1} = M_k + k·Δγ_k - ∫_{γ_k}^{γ_{k+1}} N0 dt
    # ∫N0 ≈ N0(γ_k)·Δγ_k + N0'(γ_k)·Δγ_k²/2（局部——）
    M_val = np.float128(0)
    M_sample = []
    for k in range(K-1):
        dg_k = z[k+1] - z[k]
        # ∫_{γ_k}^{γ_{k+1}} N0 dt ≈ (N0(γ_k)+N0(γ_{k+1}))/2 · dg_k（梯形——）
        intN = np.float128((N0_arr(z[k]) + N0_arr(z[k+1]))/2 * dg_k)
        M_val += np.float128(k+1)*np.float128(dg_k) - intN  # N(t)=k+1 在 (γ_k,γ_{k+1}]?
        M_vals[k+1] = M_val
        if (k+1) % 20000 == 0:
            M_sample.append((k+1, float(M_val)))
    print("   M(γ_k) 采样:")
    for k, mv in M_sample:
        print(f"   k={k:>7}（γ={z[k]:.0f}）: M = {mv:+.4f}")
    
    # 4. M 与 Σδ 的关系——都在 O(1)——是否成比例？
    print("\n4. M(γ_k) vs Σδ 累积:")
    for k, mv in M_sample:
        kk = k-1
        print(f"   k={k:>7}: M={mv:+.4f}——Σδ={Sd[kk]:+.4f}")

if __name__ == "__main__":
    main()
