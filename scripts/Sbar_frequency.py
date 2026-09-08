#!/usr/bin/env python3
"""
S̄（区间平均 S——）的频率结构
S(t) ≈ -(1/π)Σ_p sin(t log p)/(p^{1/2} log p)——几乎周期
S̄_k（区间平均——）的波包——是否由低素数频率主导？

检验：
1. S̄_k vs S_main（素数几乎周期项——）的匹配
2. S̄ 的波包长度 vs 低素数周期（2π/log p——）
3. M 增量的主要贡献者
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

def S_main_t(t, primes, logp):
    """S(t) 的素数几乎周期主项"""
    return -(1/pi)*np.sum(np.sin(t*logp)/(np.sqrt(primes)*logp))

def main():
    print("="*70)
    print("S̄ 波包频率结构")
    print("="*70)
    
    K = 50000
    z = load_zeros(K)
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    primes = primes[primes < 1e6]  # 用 p<10^6 够（权重衰减——）
    logp = np.log(primes)
    
    # S̄_k——区间平均（用端点——）
    N0v = N0_arr(z)
    k_range = np.arange(1, K)
    S_left = k_range - N0v[:-1]  # γ_k 右 = k - N0(γ_k)
    S_right = k_range - N0v[1:]  # γ_{k+1} 左 = k - N0(γ_{k+1})
    Sbar = (S_left + S_right)/2
    dg = np.diff(z[:K])
    
    # 1. S̄ vs S_main（在区间中点——）
    print("\n1. S̄_k vs S_main（区间中点——）:")
    mid_t = (z[:-1] + z[1:])/2
    # 采样前 100 区间对比
    S_main_vals = np.array([S_main_t(mid_t[i], primes, logp) for i in range(0, 5000, 100)])
    Sbar_sample = Sbar[0:5000:100]
    corr = np.corrcoef(Sbar_sample[:50], S_main_vals[:50])[0,1] if len(S_main_vals) > 50 else 0
    print(f"   corr(S̄, S_main)（采样——）= {corr:+.4f}")
    
    # 2. 低素数周期
    print("\n2. 低素数在 t 空间的周期:")
    for p in [2, 3, 5, 7, 11]:
        T_p = 2*pi/log(p)
        print(f"   p={p}: 周期 = {T_p:.1f}（t 空间——）——γ 空间 ~ {T_p:.1f}")
    
    # 3. M 增量的自相关结构（波包长度——）
    print("\n3. M 增量的自相关（找波包尺度——）:")
    M_inc = Sbar * dg
    for j in [1, 2, 5, 10, 20, 50, 100, 200]:
        c = np.corrcoef(M_inc[:-j], M_inc[j:])[0,1]
        print(f"   ρ(M_inc, M_inc+{j}) = {c:+.4f}")
    
    # 4. 分块累积的尺度
    print("\n4. M 的分块累积（不同块长——看涨落尺度——）:")
    for block in [100, 1000, 5000, 10000]:
        nb = len(M_inc)//block
        sums = [M_inc[i*block:(i+1)*block].sum() for i in range(nb)]
        sums = np.array(sums)
        print(f"   块长 {block:>6}: 块累积 std = {sums.std():.4f}（随机游走预期 ~{M_inc.std()*np.sqrt(block):.1f}——）")
        print(f"             max|块累积| = {np.abs(sums).max():.4f}")

if __name__ == "__main__":
    main()
