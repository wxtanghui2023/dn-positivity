#!/usr/bin/env python3
"""
F(T) 结构探索——找证明路径
F(T) = Σ_p cos(T log p)/(p^{1/2} log²p)

问题：
1. 幅度 ~2.2 来自哪？（低素数主导？——）
2. 部分和的振荡结构（条件收敛如何实现——）
3. 与 1/log²p 积分表示相关的分解
"""
import numpy as np

def load_primes():
    return np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')

def main():
    print("="*70)
    print("F(T) 结构探索")
    print("="*70)
    
    primes = load_primes()
    logp = np.log(primes)
    w = 1.0/(np.sqrt(primes) * logp**2)
    
    # 1. 低素数主导？——不同 p 上限的贡献
    print("\n1. F(T=1000) 的分层贡献:")
    T = 1000.0
    for lo, hi in [(2, 10), (10, 100), (100, 1000), (1000, 10000), (10000, 1e6), (1e6, 1e8)]:
        mask = (primes >= lo) & (primes < hi)
        contrib = np.sum(np.cos(T*logp[mask]) * w[mask])
        print(f"   p∈[{lo:>8}, {hi:>10}): 贡献 = {contrib:+.6f}")
    
    # 2. 权重分布
    print("\n2. 权重 w_p = 1/(p^{1/2}log²p) 的累积:")
    cumw = np.cumsum(w)
    for cutoff in [10, 100, 1000, 10000, 1e5, 1e6, 1e7, 1e8]:
        mask = primes <= cutoff
        print(f"   p≤{cutoff:>9}: Σw = {cumw[mask][-1]:.4f}")
    
    # 3. 相位分布（T log p mod 2π——）
    print("\n3. 相位 T log p mod 2π（p≤10^6——T=1000——）:")
    T = 1000.0
    mask = primes <= 1e6
    phases = (T * logp[mask]) % (2*np.pi)
    # 直方图——看是否均匀
    hist, _ = np.histogram(phases, bins=8, range=(0, 2*np.pi))
    print(f"   相位直方图（8 bin——）: {hist}")
    print(f"   （均匀期望 ~{len(primes[mask])/8:.0f} 每 bin——）")
    
    # 4. F(T) 的涨落随截断
    print("\n4. 部分和 S(X) = Σ_{p≤X} cos(T log p) w_p（T=1000——）:")
    T = 1000.0
    cos_vals = np.cos(T*logp)
    partial = np.cumsum(cos_vals * w)
    # 采样几个 X
    for X in [10, 100, 1000, 10000, 1e5, 1e6, 1e7]:
        mask = primes <= X
        print(f"   X={X:>9}: S(X) = {partial[mask][-1]:+.4f}")

if __name__ == "__main__":
    main()
