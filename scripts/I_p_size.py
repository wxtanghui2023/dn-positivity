#!/usr/bin/env python3
"""
I_p(T) 的实际大小——理解 Σ_p a_p·I_p 为何收敛（M(T)=O(1)——）
I_p(T) = Σ_{γ≤T} sin(γ̄ log p)·Δγ——Riemann 和
如果 |I_p| ~ C_p 且 Σ_p |a_p|·C_p 收敛——M 收敛——看 C_p 行为
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
    print("I_p(T) 大小 vs p——收敛机制")
    print("="*70)
    
    K = 50000
    z = load_zeros(K)
    mid = (z[:-1]+z[1:])/2
    dg = np.diff(z[:K])
    T_idx = K - 2
    
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    
    # 对多个 T 采样——看 I_p 的稳定大小
    print("\nI_p(T) 在不同 T:")
    Ts = [10000, 20000, 30000, 40000, 49998]
    
    # 先算每个 p 的 I_p 在多个 T
    ps = primes[primes < 5000]
    print(f"\n{'p':>6} | I_p 在 T=1e4 | T=2e4 | T=3e4 | T=4e4 | T=5e4（采样——）")
    for p in ps[ps <= 200]:
        logp = log(p)
        ph = mid*logp
        contrib = np.sin(ph)*dg
        cum = np.cumsum(contrib)
        vals = [cum[t-1] for t in Ts]
        print(f"{p:>6} | " + " | ".join(f"{v:+.2f}" for v in vals))
    
    # max|I_p| over T（到 T_idx——）
    print(f"\nmax|I_p|（到 T={mid[T_idx]:.0f}——）:")
    data = []
    for p in ps:
        logp = log(p)
        ph = mid*logp
        contrib = np.sin(ph)*dg
        cum = np.cumsum(contrib)
        data.append((p, np.abs(cum).max()))
    
    print(f"\n{'p':>6} {'max|I_p|':>12} {'理论 2/log p':>12} {'a_p':>10} {'a_p·max|I|':>12}")
    total = 0
    for p, mI in data[:40]:
        a = 1/(np.sqrt(p)*log(p))  # w_p
        contrib = a*mI
        total += contrib
        print(f"{p:>6} {mI:>12.3f} {2/log(p):>12.3f} {a:>10.4f} {contrib:>12.4f}")
    print(f"\nΣ w_p·max|I_p|（p<{ps[40] if len(ps)>40 else 'end'}——部分——）= {total:.3f}")

if __name__ == "__main__":
    main()
