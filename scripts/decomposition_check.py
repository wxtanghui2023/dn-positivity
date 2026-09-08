#!/usr/bin/env python3
"""
核心分解验证：M(T) = -(1/π)Σ_p w_p·I_p(T)？
w_p = 1/(p^{1/2} log p)——I_p(T) = Σ_{γ_k≤T} sin(γ̄_k log p)·Δγ_k
如果 S̄ 分解精确（R²=0.90——）——M 应该 ≈ 此和

问题：
1. Σ_p w_p·I_p(T) vs M(T)（真实——）匹配？
2. I_p(T) 的行为（随 T——随 p——）——收敛机制
3. 部分和（p 截止——）的收敛
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
    print("核心分解验证：M vs Σ_p w_p·I_p")
    print("="*70)
    
    K = 50000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    
    # 真实 M(T)（到中点——）
    N0v = N0_arr(z)
    k_range = np.arange(1, K)
    S_left = k_range - N0v[:-1]
    S_right = k_range - N0v[1:]
    Sbar = (S_left+S_right)/2
    M_cum = np.cumsum(Sbar*dg)
    
    # Σ_p w_p·I_p(T)——p 到不同截止
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    
    # 对固定 T（末点——）算 I_p 然后加权
    T_idx = K - 2
    T = mid[T_idx]
    print(f"固定 T = {T:.0f}（k={T_idx}——）")
    
    print(f"\n真实 M(T) = {M_cum[T_idx]:+.4f}")
    
    print("\nΣ_p w_p·I_p(T) 随 p 截止:")
    # I_p 需要每个 p 的 sin 累积——O(P·K)——用分块——只算到 p<10000 的采样
    for p_cut in [20, 50, 100, 200, 500, 1000, 2000]:
        ps = primes[primes <= p_cut]
        total = 0
        for p in ps:
            logp = log(p)
            ph = mid * logp
            I_p = np.sum(np.sin(ph[:T_idx+1]) * dg[:T_idx+1])
            w = 1.0/(np.sqrt(p)*logp)
            total += w * I_p
        print(f"   p≤{p_cut:>5}: Σ w·I = {total:+.4f}（×(-1/π) = {-total/pi:+.4f}）")
    
    # 与真实 M 的差——需要 -1/π 因子和 S̄ 的幅度修正（0.64——之前发现的——）
    print(f"\n真实 M = {M_cum[T_idx]:+.4f}")
    print(f"（S̄ 幅度 vs S_main 理论有 ~0.64 因子——需要校准——）")
    
    # 校准：S̄ = c·S_main？——拟合 c
    # S_main_mid = -(1/π)Σ_p sin(mid log p)/(p^{1/2} log p)
    # 近似用 p<10^6 的 S_main 与 S̄ 回归
    ps = primes[primes < 1e6]
    S_main_mid = np.zeros(len(mid))
    # 分块算（省内存——）
    for p0 in range(0, len(ps), 20000):
        pb = ps[p0:p0+20000]
        logpb = np.log(pb)
        # sin(mid log p) 的矩阵——mid 长度 50000——太大——采样
        pass
    # 简化：直接回归 S̄ ~ c·S_main（用前 5000 中点——p<10^4——）
    ps_small = primes[primes < 10000]
    S_main_5000 = np.zeros(5000)
    for p in ps_small:
        logp = log(p)
        S_main_5000 -= (1/pi)*np.sin(mid[:5000]*logp)/(np.sqrt(p)*logp)
    c = np.sum(Sbar[:5000]*S_main_5000)/np.sum(S_main_5000**2)
    print(f"\n校准因子 c（S̄ ≈ c·S_main——）= {c:.4f}")

if __name__ == "__main__":
    main()
