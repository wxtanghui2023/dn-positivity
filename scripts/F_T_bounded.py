#!/usr/bin/env python3
"""
γ 层振荡项突破：F(T) = Σ_p cos(T·log p)/(p^{1/2}·log²p) 的一致有界性
M_main(T) = -(1/π)[Σ w_p - F(T)]——F(T) 有界 ⟹ M_main 有界

任务：
1. 数值扫描 F(T) 对 T——确认一致有界
2. 看 F(T) 的结构（振荡幅度——是否有界——）
3. 尾部行为（素数到多少够——）
"""
import numpy as np
import gc

def load_primes():
    p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    return p

def F_of_T(T, primes, logp):
    """F(T) = Σ_p cos(T log p)/(p^{1/2} log²p)"""
    cos_vals = np.cos(T * logp)
    w = 1.0/(np.sqrt(primes) * logp**2)
    return np.sum(cos_vals * w)

def main():
    print("="*70)
    print("F(T) 一致有界性验证")
    print("="*70)
    
    primes = load_primes()
    logp = np.log(primes)
    print(f"素数到 10^8: {len(primes)} 个")
    
    # 1. F(T) 扫描
    print("\n1. F(T) 扫描（素数到 10^8——）:")
    Ts = np.linspace(10, 20000, 200)
    Fs = []
    for T in Ts:
        Fs.append(F_of_T(T, primes, logp))
    Fs = np.array(Fs)
    print(f"   F(T) 范围: [{Fs.min():+.6f}, {Fs.max():+.6f}]")
    print(f"   max|F| = {np.max(np.abs(Fs)):.6f}")
    
    # 2. 更宽扫描（稀疏——）
    print("\n2. 宽扫描（T 到 10^6——稀疏——）:")
    Ts2 = np.logspace(1, 6, 100)
    Fs2 = []
    for T in Ts2:
        Fs2.append(F_of_T(T, primes, logp))
    Fs2 = np.array(Fs2)
    print(f"   F(T) 范围: [{Fs2.min():+.6f}, {Fs2.max():+.6f}]")
    print(f"   max|F| = {np.max(np.abs(Fs2)):.6f}")
    
    # 3. 截断效应（素数截断——）
    print("\n3. 截断效应（T=1000——）:")
    for cutoff in [1000, 10000, 100000, 1000000, 10000000]:
        mask = primes <= cutoff
        w = 1.0/(np.sqrt(primes[mask]) * logp[mask]**2)
        F = np.sum(np.cos(1000*logp[mask]) * w)
        print(f"   p≤{cutoff:>9}: F = {F:+.6f}")
    
    # 4. 常数项对比
    print("\n4. Σ w_p（常数项——）:")
    w = 1.0/(np.sqrt(primes) * logp**2)
    print(f"   Σ_p w_p（到 10^8——）= {np.sum(w):.4f}")
    print(f"   M_main = -(1/π)[Σw - F(T)]——F 有界 ⟹ M_main ∈ [-Σw/π-maxF/π, ...]")

if __name__ == "__main__":
    main()
