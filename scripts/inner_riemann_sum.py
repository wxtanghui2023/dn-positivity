#!/usr/bin/env python3
"""
M(T) 求和次序的关键：内层 Riemann 和
M(T) = Σ_k S̄_k·Δγ_k ≈ -(1/π)Σ_p (1/(p^{1/2}log p))·Σ_k sin(γ̄_k log p)Δγ_k
内层：I_p(T) = Σ_{γ_k≤T} sin(γ̄_k log p)·Δγ_k ≈ ∫_0^T sin(t log p)dt = (1-cos(T log p))/log p

验证：I_p(T) vs (1-cos(T log p))/log p——误差行为
如果误差可控制且 Σ_p w_p·误差可和——M(T)=O(1) 证明路径
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
    print("内层 Riemann 和验证")
    print("="*70)
    
    K = 100000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    
    # 对几个 p——算 I_p(T)（到不同 T——）
    print("\nI_p(T) = Σ_{γ≤T} sin(γ̄ log p)·Δγ vs (1-cos(T log p))/log p:")
    for p in [2, 3, 5]:
        print(f"\n   p={p}:")
        logp = log(p)
        # 累积到不同 T
        ph = mid * logp
        contrib = np.sin(ph) * dg
        cum = np.cumsum(contrib)
        # 理论 (1-cos(T log p))/log p
        for T_idx in [10000, 30000, 50000, 80000, 99999]:
            T = mid[T_idx]
            theory = (1-np.cos(T*logp))/logp
            print(f"   T={T:8.0f}: I_p = {cum[T_idx]:+.4f}——理论 = {theory:+.4f}——误差 = {cum[T_idx]-theory:+.4f}")
    
    # 关键：Σ_p w_p·误差_p——可和性
    print("\n2. 加权误差 Σ_p (1/(p^{1/2}log p))·|I_p - 理论|:")
    # 在固定 T（末点——）对多个 p 算误差
    T_idx = 99999
    T = mid[T_idx]
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    primes = primes[primes < 100000]
    
    total_err = 0
    total_w = 0
    for p in primes:
        logp = log(p)
        ph = mid * logp
        contrib = np.sin(ph) * dg
        I_p = contrib[:T_idx].sum()
        theory = (1-np.cos(T*logp))/logp
        err = abs(I_p - theory)
        w = 1.0/(np.sqrt(p)*logp)
        total_err += w*err
        total_w += w
    print(f"   Σ w_p·|误差_p| = {total_err:.4f}")
    print(f"   Σ w_p = {total_w:.4f}（发散——但加权误差？——）")
    print(f"   平均 |误差| ~ {total_err/max(total_w,1):.4f}")
    
    # 3. 误差的量级 vs p
    print("\n3. 误差随 p 的行为:")
    for p in [2, 5, 11, 29, 53, 101, 211, 503, 1009]:
        logp = log(p)
        ph = mid * logp
        contrib = np.sin(ph) * dg
        I_p = contrib[:T_idx].sum()
        theory = (1-np.cos(T*logp))/logp
        err = abs(I_p - theory)
        print(f"   p={p:>5}: 误差 = {err:.4f}——理论幅度 {2/logp:.3f}——比值 {err*logp/2:.4f}")

if __name__ == "__main__":
    main()
