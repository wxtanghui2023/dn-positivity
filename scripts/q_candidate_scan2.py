#!/usr/bin/env python3
"""
动作 1b：动力学类统计量——找"有演化/回复力"的量
重点：误差的标度、局部密度比、加乘耦合、Chebyshev 偏置的符号游走
"""
import numpy as np

def main():
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    
    print("="*80)
    print("动力学类统计量扫描——q_N 是否有 N-演化（回复力/平衡）")
    print("="*80)
    
    # 采样：用素数个数索引（均匀 log 间隔）
    ns = [10_000, 50_000, 100_000, 500_000, 1_000_000, 2_000_000, 4_000_000, 5_761_455]
    
    print(f"{'n':>10} {'π(N)logN/N':>12} {'θ(N)/N':>10} {'π(N;4,1)/π':>12} {'Mertens':>10} {'偏置·logN/√N':>14}")
    for n in ns:
        p = primes[:n]
        N = p[-1]
        logN = np.log(N)
        
        s1 = n * logN / N
        s2 = np.sum(np.log(p)) / N
        s4 = np.sum(p % 4 == 1) / n
        # Mertens: |Σ log(1-1/p)| = loglogN + M + o(1)——减 loglogN → M ≈ 0.2615
        mertens_err = abs(np.sum(np.log(1 - 1.0/p))) - np.log(np.log(N))
        # 模 4 偏置（Chebyshev——）·logN/√N——GRH 下有界——实际游走
        bias = np.sum(np.where(p % 4 == 1, 1, -1))
        s7 = bias * logN / np.sqrt(N)
        
        print(f"{n:>10} {s1:>12.4f} {s2:>10.4f} {s4:>12.4f} {mertens_err:>10.4f} {s7:>14.4f}")
    
    print("\n" + "="*80)
    print("Chebyshev 偏置的符号游走（模 4——）——看有无'回复力'模式")
    print("="*80)
    # 偏置 D(N) = π(N;4,1) − π(N;4,3)——它的符号随 N 的游走
    # 采样块（每块 1e5 素数——）记录 D 的符号变化
    block = 100_000
    D = 0
    sign_changes = []
    signs = []
    for i in range(0, len(primes) - block, block):
        p = primes[i:i+block]
        D += np.sum(p % 4 == 1) - np.sum(p % 4 == 3)
        signs.append(1 if D > 0 else -1)
    n_changes = sum(1 for i in range(1, len(signs)) if signs[i] != signs[i-1])
    print(f"块数: {len(signs)}——符号变化次数: {n_changes}——频率: {n_changes/len(signs):.3f}")
    print(f"D(N) 末值: {D}（π(N;4,1)−π(N;4,3)——）")
    print(f"偏置的'平均回复'：D 的符号 ~ {'多数时间 π(4,3)>π(4,1)' if signs.count(-1) > signs.count(1) else '多数 π(4,1)>π(4,3)'}（Chebyshev 偏置——）")
    print(f"  (-1 次数: {signs.count(-1)}——+1 次数: {signs.count(1)}——)")

    print("\n" + "="*80)
    print("加乘耦合量（非换皮——纯算术——）")
    print("="*80)
    # A. 素数的加法能量标度：E(A)/N³ 类——用部分块
    # B. Σ_{p≤N} 1/(p+q 类型)——跳过（贵）
    # C. "素数与最近整数平方的距离"平均
    ns2 = [100_000, 500_000, 1_000_000]
    for n in ns2:
        p = primes[:n]
        N = p[-1]
        # C1: 素数到最近平方数的距离平均（归一化——）
        sq = np.floor(np.sqrt(p)).astype(np.int64)
        d_sq = np.minimum(p - sq**2, (sq+1)**2 - p)
        c1 = np.mean(d_sq) / np.sqrt(N)  # 归一化——随机 ~ 1/3？1/2？
        # C2: 素数之间的间隔分布——间隔 ≤ logN/2 的比例（泊松 e^{-1/2}？）
        gaps = np.diff(p)
        c2 = np.mean(gaps <= logN/2)
        print(f"  n={n}: 平方距离均值/√N = {c1:.4f}——间隙≤logN/2比例 = {c2:.4f}")

if __name__ == "__main__":
    main()
