#!/usr/bin/env python3
"""
ARI 第一轮数值——E(X) 尺度行为探索
E(X) = (Ψ(X)−X)/X^{1/2}——用素数数据（到 10^9——）算 Ψ(X) 部分和
探索：
1. E(X) 的振荡结构（模态——）
2. 尺度关系 E(X^a) vs E(X)——(用 X^a ≤ 10^9——)
3. 守恒量候选
"""
import numpy as np

def load_primes():
    """加载素数到 10^8（够算 Ψ 到 10^8——log 尺度到 ~18.4——）"""
    return np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')

def psi_at(X, primes, prime_powers=False):
    """Ψ(X) = Σ_{p^k≤X} log p——用素数（素数幂修正——）"""
    # 素数部分：Σ_{p≤X}log p
    idx = np.searchsorted(primes, X, side='right')
    psi = np.sum(np.log(primes[:idx].astype(float)))
    # 素数幂修正：p^k ≤ X——p ≤ X^{1/k}——加 log p 每幂
    k = 2
    while True:
        root = X**(1.0/k)
        if root < 2:
            break
        idx2 = np.searchsorted(primes, root, side='right')
        psi += np.sum(np.log(primes[:idx2].astype(float)))
        k += 1
    return psi

def main():
    print("="*70)
    print("ARI 第一轮——E(X) 尺度行为")
    print("="*70)
    primes = load_primes()
    print(f"素数到 {primes[-1]:.0f}——Ψ 可算到 ~10^8")
    
    # 1. E(X) 在几个 X 的值
    print("\n1. E(X) = (Ψ(X)−X)/X^{1/2}:")
    for X in [1e4, 1e5, 1e6, 1e7, 1e8]:
        psi = psi_at(X, primes)
        E = (psi - X)/np.sqrt(X)
        print(f"   X={X:.0e}: Ψ={psi:.1f}——E={E:+.4f}")
    
    # 2. 尺度关系（a=2——X^a ≤ 1e8——）
    print("\n2. 尺度关系 E(X^a) vs E(X)（a=2——）:")
    print(f"   {'X':>8} {'E(X)':>10} {'E(X²)':>10} {'E(X²)−E(X)':>12} {'E(X²)/E(X)':>10}")
    for X in [100, 300, 1000, 3000, 10000]:
        psi1 = psi_at(X, primes)
        psi2 = psi_at(X*X, primes)
        E1 = (psi1 - X)/np.sqrt(X)
        E2 = (psi2 - X*X)/np.sqrt(X*X)
        ratio = E2/E1 if abs(E1) > 1e-6 else float('nan')
        print(f"   {X:>8.0f} {E1:>+10.4f} {E2:>+10.4f} {E2-E1:>+12.4f} {ratio:>10.4f}")
    
    # 3. E(X) 的"模态"检查——用 E 的符号变化估计
    print("\n3. 模态结构观察:")
    print("   E(X) 振荡（零点模态——）——RH 下 E ~ 有界振荡（X^ε——）")
    print("   关键：E(X^a) 与 E(X) 的关系——如果模态 e^{iγt}——")
    print("   E(X^a)/E(X) ~ e^{iγ(a−1)logX} 类——相位差——非简单比——")

if __name__ == "__main__":
    main()
