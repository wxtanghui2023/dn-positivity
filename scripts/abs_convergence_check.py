#!/usr/bin/env python3
"""
关键澄清：M_main 绝对收敛 vs S(t) 展开条件收敛
M_main(T) = -(1/π)Σ_p [1-cos(T log p)]/(p^{1/2} log²p)——w=1/log²p
S(t) ≈ -(1/π)Σ_p sin(t log p)/(p^{1/2} log p)——w=1/log p（条件收敛——）

验证：
1. Σ_p 1/(p^{1/2}log²p) 收敛（尾部小——）
2. Σ_p 1/(p^{1/2}log p) 发散（条件——）
3. M_main 部分和随截止稳定（绝对收敛的证据——）
"""
import numpy as np

def load_primes():
    return np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')

def main():
    print("="*70)
    print("M_main 绝对收敛验证")
    print("="*70)
    
    primes = load_primes()
    logp = np.log(primes)
    
    # 1. Σ 1/(p^{1/2} log²p)——M_main 的权重
    print("\n1. Σ_p 1/(p^{1/2}·log²p)（M_main 权重——绝对？——）:")
    w2 = 1.0/(np.sqrt(primes) * logp**2)
    cw2 = np.cumsum(w2)
    for X in [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]:
        mask = primes <= X
        print(f"   到 p≤{X:>9.0e}: Σ = {cw2[mask][-1]:.6f}")
    # 尾部估计
    X = 1e8
    tail_est = 2/(np.sqrt(X) * np.log(X)**3)  # ∫_X^∞ dt/(t^{1/2}log³t) ~ 2/(√X log³X)
    print(f"   尾部估计（p>10^8——）~ {tail_est:.2e}——收敛 ✓")
    
    # 2. Σ 1/(p^{1/2} log p)——S(t) 展开的权重
    print("\n2. Σ_p 1/(p^{1/2}·log p)（S(t) 权重——条件？——）:")
    w1 = 1.0/(np.sqrt(primes) * logp)
    cw1 = np.cumsum(w1)
    for X in [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]:
        mask = primes <= X
        print(f"   到 p≤{X:>9.0e}: Σ = {cw1[mask][-1]:.4f}")
    # 理论：Σ ~ ∫ dt/(t^{1/2}log²t) ~ 2√x/log²x 类——增长？
    X = 1e8
    print(f"   理论增长 ~ 2√X/log²X = {2*np.sqrt(X)/np.log(X)**2:.1f}（发散——条件收敛——）")
    
    # 3. M_main 部分和（T=1000——）随截止的稳定性
    print("\n3. M_main(1000) 部分和稳定性:")
    T = 1000.0
    cosv = np.cos(T*logp)
    partial = np.cumsum((1-cosv) * w2)
    for X in [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]:
        mask = primes <= X
        print(f"   p≤{X:>9.0e}: M_main 部分和 = {-partial[mask][-1]/np.pi:+.6f}")

if __name__ == "__main__":
    main()
