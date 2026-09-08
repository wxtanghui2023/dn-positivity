#!/usr/bin/env python3
"""
e_k（位置偏离——）的回归结构分析
e_k = γ_k - G_k（Gram 点——N0(G_k) = k 类）
M(T)=O(1) ⟺ Σe_k = O(1)（位置偏离累积——）

问题：
1. e_k 的行为（有界？——回归 0？——）
2. e_k 的自相关（反持久？——像 δ 的 -0.36？——）
3. e_k 与 δ_k 的关系（e_{k+1}-e_k = δ_k？——）
4. Σe_k 的累积（是否 O(1)——M 的离散版——）
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
    if t < 1: return 0.0
    return (t/(2*pi))*log(t/(2*pi)) - t/(2*pi) + 7/8

def G_k(k):
    """Gram 点：N0(G) = k 类——用 N0 反函数（数值——牛顿——）"""
    # N0(t) ≈ k——粗解——牛顿
    t = k*2*pi  # 初始猜测
    for _ in range(20):
        val = N0(t) - k
        # N0'(t) = log(t/2π)/(2π)
        dval = log(t/(2*pi))/(2*pi)
        if abs(dval) < 1e-10: break
        t = t - val/dval
    return t

def main():
    print("="*70)
    print("e_k（位置偏离——）回归结构")
    print("="*70)
    
    K = 200000
    z = load_zeros(K)
    
    # e_k = γ_k - G_k——用 N0(γ_k) - k 的近似（e ≈ (N0(γ_k)-k)/N0'(γ_k)——）
    # 更精确：N0(G_k) = k——N0(γ_k) - N0(G_k) ≈ N0'(γ_k)(γ_k-G_k) = N0(γ_k) - k
    # e_k = (N0(γ_k) - k)/N0'(γ_k)
    N0v = N0(z)
    N0p = np.log(z/(2*pi))/(2*pi)
    e = (N0v - np.arange(1, K+1))/N0p
    
    print(f"\n1. e_k 统计:")
    print(f"   max e = {e.max():+.4f}——min e = {e.min():+.4f}——max|e| = {np.abs(e).max():.4f}")
    print(f"   mean e = {e.mean():+.6f}——std e = {e.std():.4f}")
    
    # 2. e 的自相关
    print(f"\n2. e_k 自相关:")
    for j in [1, 2, 3, 5, 10, 20]:
        c = np.corrcoef(e[:-j], e[j:])[0,1]
        print(f"   ρ(e_k, e_k+{j}) = {c:+.4f}")
    
    # 3. e 与 δ 的关系（e_{k+1}-e_k vs δ_k——）
    print(f"\n3. Δe_k = e_{{k+1}} - e_k vs δ_k:")
    dg = np.diff(z)
    Np = np.log(z[:-1]/(2*pi))/(2*pi)
    delta = dg - 1.0/Np
    de = np.diff(e)
    corr_de_delta = np.corrcoef(de, delta)[0,1]
    print(f"   corr(Δe, δ) = {corr_de_delta:.4f}（应 ~1 如果 e'=δ——）")
    
    # 4. Σe_k（位置偏离累积——目标 O(1)——）
    print(f"\n4. Σe_k 累积:")
    Se = np.cumsum(e)
    print(f"   最终 Σe = {Se[-1]:+.4f}——max|Σe| = {np.abs(Se).max():.4f}")
    print(f"   分块采样:")
    for k in range(0, K, 20000):
        print(f"   k={k:>7}: Σe = {Se[k]:+.4f}")
    
    # 5. Σe vs M（M 应该 ~Σe 类——）
    print(f"\n5. 对比 M（前面算的——范围 [−0.77, +0.58]——）:")
    print(f"   Σe 范围 [{Se.min():+.4f}, {Se.max():+.4f}]——同量级？——")

if __name__ == "__main__":
    main()
