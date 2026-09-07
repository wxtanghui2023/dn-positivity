#!/usr/bin/env python3
"""
R1：三体不可约性——第一层
测试 Rédei 符号 R(a,b,c) 是否可被低阶（单体/模类）信息解释

设计：
1. 收集大量 admissible triple 的 R 值
2. 检查 R 是否依赖模类（a,b,c mod 8/16——）——按模类分层看 R 分布
3. 同模类内 R 是否变化（若变——R 依赖非模类结构——三体信号候选）
4. F₂ 秩测试：R 能否被 pairwise 模类特征线性表示
"""
import math, sys, itertools, random
sys.path.insert(0, 'scripts')
from redei_v4 import redei_v4, legendre
import numpy as np

def main():
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    # 用小素数（解方程快——）
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5 and p < 20000][:800]
    print(f"素数池: {len(p1)}（最大 {p1[-1]}）")
    random.seed(41)
    
    # 收集数据
    data = []  # (a, b, c, R)
    n_adm = 0
    for _ in range(5000):
        a, b, c = random.sample(p1, 3)
        if not (legendre(a,b)==1 and legendre(b,c)==1 and legendre(c,a)==1):
            continue
        n_adm += 1
        R = redei_v4(a, b, c)
        if R is not None:
            data.append((a, b, c, R))
        if len(data) >= 400:
            break
    
    print(f"admissible: {n_adm}——有效 R: {len(data)}")
    Rs = [d[3] for d in data]
    n_plus = sum(1 for r in Rs if r == 1)
    print(f"R 分布: +1: {n_plus}——−1: {len(Rs)-n_plus}——比例: {n_plus/len(Rs):.3f}")
    
    # 测试 1：R 是否依赖 a mod 8？（分层——）
    print("\n按 a mod 8 分层的 R 分布：")
    by_a8 = {}
    for a, b, c, R in data:
        by_a8.setdefault(a % 8, []).append(R)
    for k in sorted(by_a8):
        v = by_a8[k]
        print(f"  a≡{k} mod 8: {len(v)} 样本——+1 比例 {sum(1 for r in v if r==1)/len(v):.3f}")
    
    # 测试 2：同模类内 R 是否变化（固定 a,b,c mod 8——随机换素数——）
    print("\n同模类内 R 的变化（固定 (a,b,c) mod 8 类——不同素数——）:")
    # 对几个模类——收集多组——看 R 是否多变
    by_class = {}
    for a, b, c, R in data:
        key = (a % 8, b % 8, c % 8)
        by_class.setdefault(key, []).append(R)
    n_varied = 0
    n_const = 0
    for key, vals in by_class.items():
        if len(vals) >= 3:
            if len(set(vals)) > 1:
                n_varied += 1
            else:
                n_const += 1
    print(f"  模类内 R 变化: {n_varied} 类——恒定: {n_const} 类")
    if n_varied > 0:
        print("  → R 在同模类内变化——依赖非模类结构（素数本身——）")
    if n_const > 0 and n_varied == 0:
        print("  → R 完全由模类决定？——需要更大样本确认——")
    
    # 测试 3：尝试 F₂ 线性模型（用模 8 类特征——）——R 能否被预测
    print("\nF₂ 线性预测尝试（模 8 单体特征——）:")
    # 用 log 模型（普通回归看解释力——）
    from collections import Counter
    # 简单：R 与模类是否独立（卡方近似——看熵——）
    n_classes = len(by_class)
    n_with_both = sum(1 for vals in by_class.values() if len(set(vals)) >= 2 and len(vals) >= 4)
    print(f"  模类总数: {n_classes}——含 ±1 混合的类: {n_with_both}")
    print(f"  → 若很多类混合 ±1——R 不可由模类解释——三体/深结构信号")

if __name__ == "__main__":
    main()
