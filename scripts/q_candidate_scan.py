#!/usr/bin/env python3
"""
动作 1：素数系统自然统计量的候选池扫描
目标：从 {p ≤ N} 的纯算术数据构造统计量——看哪些随 N→∞ 自然收敛到 ½
（不预设——让数据说话——收敛到 ½ 的进候选池——其余归档死因）
"""
import numpy as np

def load_primes():
    """加载素数数据（primes_1e8.npy——5.76M 素数——）"""
    try:
        p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
        print(f"加载 primes_1e8.npy：{len(p)} 个素数——最大 {p[-1]}")
        return p
    except Exception as e:
        print(f"加载失败: {e}——现场生成")
        # 现场生成到 1e7
        from sympy import primerange
        return np.array(list(primerange(2, 10_000_000)), dtype=np.int64)

def main():
    primes = load_primes()
    # 采样点 N（用素数个数索引——）
    n_pts = [1000, 10_000, 100_000, 1_000_000, len(primes)]
    results = {k: [] for k in range(1, 16)}
    
    print("\n统计量扫描（值随 N 变化——→极限）")
    print("="*80)
    header = f"{'N':>10}" + "".join(f"{f'S{i}':>12}" for i in range(1, 13))
    print(header)
    
    for n in n_pts:
        p = primes[:n]
        N = p[-1]
        logN = np.log(N)
        
        # S1: π(N)·logN/N → 1（素数定理）
        s1 = n * logN / N
        # S2: θ(N)/N → 1
        s2 = np.sum(p) / N  # 错——θ = Σ log p
        s2 = np.sum(np.log(p)) / N
        # S3: Σ1/p / loglogN → 1（Mertens）
        s3 = np.sum(1.0/p) / np.log(np.log(N)) if np.log(np.log(N)) > 0 else np.nan
        # S4: 模 4 的类 1 密度 → ½（预期——代数——）
        p1mod4 = p[p % 4 == 1]
        s4 = len(p1mod4) / n
        # S5: 模 3 的类 1 密度 → ½（预期——代数——）
        p1mod3 = p[p % 4 == 3]
        s5 = len(p1mod3) / n
        # S6: Σ(−1)^{(p−1)/2}/n（模 4 偏置密度——）→ 0
        s6 = np.sum(np.where(p % 4 == 1, 1.0, -1.0)) / n
        # S7: |模4偏置|·logN/√N（GRH 类标度——）→ 波动有界？
        bias = np.sum(np.where(p % 4 == 1, 1.0, -1.0))
        s7 = abs(bias) * logN / np.sqrt(N)
        # S8: Σ logp/p / logN → 1
        s8 = np.sum(np.log(p)/p) / logN
        # S9: Σ1/√p·logN/√N → 2（预期——）
        s9 = np.sum(1.0/np.sqrt(p)) * logN / np.sqrt(N)
        # S10: log(Π(1−1/p))·logN → −e^γ ≈ −0.5615（Mertens——）取正
        s10 = abs(np.sum(np.log(1 - 1.0/p)) * logN)
        # S11: 孪生归一 π₂·log²N/N → c₂≈1.32（猜想——）
        twin = sum(1 for i in range(n-1) if p[i+1] - p[i] == 2)
        s11 = twin * logN**2 / N
        # S12: 素数的 log 尺度中位数分数——log p_{n/2}/log p_n → ?
        s12 = np.log(p[n//2]) / np.log(p[-1])
        
        print(f"{N:>10.0e}" + "".join(f"{s:>12.4f}" for s in [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]))
    
    print("\n" + "="*80)
    print("预期分析：")
    print("  S1→1（素数定理——）S2→1（PNT——）S3→1（Mertens——）")
    print("  S4→½（模4类密度——代数——需Dirichlet）S5→½（模4的3类——代数——）")
    print("  S6→0（模4偏置密度——）S7→波动（GRH 类——）")
    print("  S8→1 S9→2 S10→e^{-γ}≈0.5615（非½！）S11→c₂≈1.32（猜想——）S12→1")
    print("\n  ⭐ 预期只有模类（S4/S5——代数½——）给 ½——其余 1/0/常数")
    print("  关键问题：有没有非代数的自然量收敛到 ½？")

if __name__ == "__main__":
    main()
