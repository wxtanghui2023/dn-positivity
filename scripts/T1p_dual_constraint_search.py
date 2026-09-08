#!/usr/bin/env python3
"""
T1' 抽象搜索：同一离散对象上的双约束/交换子结构

候选（同一对象——两个独立来源的关系——交换子非平凡——）：
A. 算术函数空间：乘性求和 (Af)(n)=Σ_{d|n}f(d) vs 前缀和 (Bf)(n)=Σ_{m≤n}f(m)
B. 整数：整除 σ(n) vs 加法 n→n+1
C. 数的二进表示：Thue-Morse 自相似 vs 移位

测：交换子 Δ 的结构——尺度——是否有"平衡点"
"""
import numpy as np
from math import log, sqrt

# ---------- A. 乘性求和 vs 前缀和 ----------
def sum_div(f, n):
    """(Af)(n) = Σ_{d|n} f(d)"""
    s = 0
    for d in range(1, n+1):
        if n % d == 0:
            s += f[d]
    return s

def prefix_sum(f, n):
    """(Bf)(n) = Σ_{m≤n} f(m)"""
    return sum(f[1:n+1])

def test_A():
    print("="*70)
    print("A. 乘性求和 A(Σ_{d|n}) vs 前缀和 B(Σ_{m≤n})——算术函数上")
    print("="*70)
    N = 500
    # f = 1（常值——）
    f = [0] + [1]*N
    # BA f: 先 A 后 B
    BA = np.zeros(N+1)
    AB = np.zeros(N+1)
    Af = np.zeros(N+1)
    Bf = np.zeros(N+1)
    for n in range(1, N+1):
        Af[n] = sum_div(f, n)       # d(n)
        Bf[n] = prefix_sum(f, n)    # n
    for n in range(1, N+1):
        BA[n] = prefix_sum(Af, n)   # Σ_{m≤n} d(m)
        AB[n] = sum_div(Bf, n)      # Σ_{d|n} n/d = σ(n)
    D = BA - AB
    print("\nf=1: Δ(n) = BA(n) − AB(n) = Σ_{m≤n}d(m) − σ(n)")
    for n in [10, 50, 100, 200, 500]:
        print(f"   n={n}: BA={BA[n]:.0f}（~nlogn——）——AB={AB[n]:.0f}——Δ={D[n]:.0f}——Δ/n={D[n]/n:.3f}")
    print(f"   Δ 尺度 ~ nlogn 主导——Δ/n = {D[-1]/N:.2f}——不给互补尺度——")
    # 精细结构：Δ 的波动（O(√n)——含零点经显式公式？）
    print("\n   Δ 的波动部分（去 nlogn 趋势——）:")
    trend = np.array([n*np.log(n) + (2*0.57721-1)*n for n in range(1, N+1)])
    D_detrended = D[:N] - trend
    print(f"   去趋势后 Δ' 的 max|Δ'| = {np.max(np.abs(D_detrended)):.1f}——√N 量级？√500={sqrt(500):.1f}")
    return D

# ---------- B. 整除 σ vs 加法 n→n+1 ----------
def test_B():
    print("\n" + "="*70)
    print("B. 整数上：A=σ(n)（因子和——）vs B=n→n+1（加法——）")
    print("="*70)
    N = 2000
    # σ(n)
    sigma = np.zeros(N+3)
    for d in range(1, N+1):
        for m in range(d, N+1, d):
            sigma[m] += d
    # Δ(n) = A(B(n)) − B(A(n)) = σ(n+1) − σ(n) − 1？——A 是"取因子和"——A(n+1)=σ(n+1)——B(A(n))=σ(n)+1
    D = np.zeros(N)
    for n in range(1, N):
        D[n] = sigma[n+1] - (sigma[n] + 1)
    print("\nΔ(n) = σ(n+1) − σ(n) − 1")
    print(f"   max|Δ| = {np.max(np.abs(D)):.0f}——均值 {np.mean(D):.3f}——std {np.std(D):.2f}")
    print(f"   σ(n) 波动 ~ n^{{0.5+ε}} 类（——）——Δ 的尺度——")
    # Δ 是否有结构（与 n 的因子——）
    big = np.argsort(np.abs(D))[-5:]
    print(f"   |Δ| 最大的 n: {[int(n) for n in big]}——对应 σ 大跳（高合成数——）")
    print("   ——σ(n+1)−σ(n) 的'跳跃'在高合成数——无 ½ 信号——")

if __name__ == "__main__":
    D = test_A()
    test_B()
