#!/usr/bin/env python3
"""
M(T) 的零频常数——精确确定
发现：M 的 Cesàro 平均 → ~0.61（非零！）——ΣM_k/k² → 0.37147

问题：
1. Cesàro 平均的精确值（更多数据——外推——）
2. 0.61 的解析候选（γ_E？——log(4π)？——c=-1.13？——）
3. ΣM_k/k² 的精确值（Brent-Platt 型常数——）
4. M(T) - c 是否"干净"（围绕 0 振荡——）
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

def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8

def main():
    print("="*70)
    print("M(T) 零频常数确定")
    print("="*70)
    
    K = 600000
    z = load_zeros(K)
    print(f"零点到 γ={z[-1]:.0f}（K={K}——）")
    
    # M 全程（float128——）
    M_vals = np.zeros(K, dtype=np.float128)
    M_val = np.float128(0.0)
    for k in range(K-1):
        kk = k + 1
        M_val += np.float128(kk)*np.float128(z[k+1]-z[k]) - np.float128(IntN0(z[k+1])-IntN0(z[k]))
        M_vals[k+1] = M_val
    Mf = np.array(M_vals, dtype=float)
    
    # 1. Cesàro 平均的收敛（末段——）
    print("\n1. Cesàro 平均（1/N）ΣM:")
    for N in [100000, 200000, 300000, 400000, 500000, 599999]:
        print(f"   N={N:>7}: = {Mf[:N].mean():+.6f}")
    
    # 2. 解析候选
    print("\n2. 解析候选:")
    gamma_E = 0.5772156649
    print(f"   γ_E = {gamma_E:.6f}")
    print(f"   (1+γ_E)/2 = {(1+gamma_E)/2:.6f}")
    print(f"   log(2π)/2 = {log(2*pi)/2:.6f}")
    print(f"   log(4π)·? = {log(4*pi):.6f}")
    print(f"   γ_E + 0.03 = {gamma_E+0.03:.6f}")
    print(f"   0.61 附近: γ_E + 1/30 = {gamma_E+1/30:.6f}")
    print(f"   c+2 = {-1.1303307+2:.6f}")
    print(f"   7/8·?——0.875·0.7 = {0.875*0.7:.4f}")
    
    # 3. Σ M_k/k²（Brent-Platt 型——）更精确
    print("\n3. Σ_{k} M_k/k² 的收敛:")
    # 用部分和 + 尾估计——Σ_{k>N} M_k/k²——M~0.6——尾 ~ 0.6/N——渐近
    for N in [100000, 200000, 300000, 400000, 500000]:
        s = np.sum(Mf[1:N]/np.arange(1,N)**2)
        # 尾估计 ~ mean·∫_N^∞ dk/k² = mean/N
        tail_est = 0.61/N
        print(f"   N={N:>7}: Σ = {s:+.8f}——尾 ~ {tail_est:.2e}——修正后 ~ {s + 0.61/N:+.8f}")
    
    # 4. M(T) - 0.61 的行为
    print("\n4. M(T) - 0.61（去零频——）:")
    Mc = Mf - 0.61
    print(f"   max|Mc| = {np.abs(Mc).max():.4f}——mean(Mc) = {Mc.mean():+.6f}")
    # Mc 是否更对称？
    print(f"   Mc > 0 比例: {np.mean(Mc>0)*100:.1f}%")

if __name__ == "__main__":
    main()
