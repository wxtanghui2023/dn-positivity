#!/usr/bin/env python3
"""
审计：Euclid 路径 = continued-fraction dynamics？
1. 对称长度定义的 Ω（ω'(p,q) = (-1)^{E(max,min)}）——还有结构吗？
2. 素数对的连分数 vs 随机对的连分数——统计有差异吗（素数特殊性测试）？
"""
import numpy as np
import random
from math import gcd

def euclid_symmetric(a, b):
    """对称 Euclid 长度（= 连分数长度——）"""
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return steps

def cf_partial_quotients(p, q):
    """p/q 的连分数部分商 [a0; a1, ..., an]"""
    a = p
    b = q
    pqs = []
    while b:
        pqs.append(a // b)
        a, b = b, a % b
    return pqs

def load_primes(n=30000):
    p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    return p[:n].tolist()

def main():
    primes = load_primes(30000)
    print(f"素数: {len(primes)}")
    random.seed(21)
    
    print("\n" + "="*70)
    print("测试 1：对称长度 ω'(p,q) 的三角和乐——还有非平凡结构吗？")
    print("="*70)
    # 对称：E'(p,q) = E(max,min)——ω' 对称——Ω' 的反对称应该消失
    def omega_sym(p, q):
        return (-1)**(euclid_symmetric(max(p,q), min(p,q)) % 2)
    n_anti = 0
    n_total = 2000
    for _ in range(n_total):
        p, q, r = random.sample(primes[1:], 3)
        Om1 = omega_sym(p,q)*omega_sym(q,r)*omega_sym(r,p)
        Om2 = omega_sym(p,r)*omega_sym(r,q)*omega_sym(q,p)
        if Om1 * Om2 == -1:
            n_anti += 1
    print(f"Ω(p,q,r)·Ω(p,r,q) = −1 比例: {n_anti/n_total:.4f}（0 = 对称——无手性——）")
    # Ω 的分布（对称——）
    dist = {}
    for _ in range(3000):
        p, q, r = random.sample(primes[1:], 3)
        Om = omega_sym(p,q)*omega_sym(q,r)*omega_sym(r,p)
        dist[Om] = dist.get(Om, 0) + 1
    print(f"对称 Ω 分布: {dist}——{'仍非平凡' if len(dist) > 1 else '恒 1（平凡——）'}")
    
    print("\n" + "="*70)
    print("测试 2：素数对连分数 vs 随机对连分数——部分商统计差异")
    print("="*70)
    # 素数对的连分数长度分布 vs 随机互素对的
    def length_dist(samples, is_prime_pair):
        lens = []
        for _ in range(samples):
            if is_prime_pair:
                p, q = random.sample(primes[100:], 2)
            else:
                # 随机数对（互素——）
                p = random.randint(1000, 100000)
                q = random.randint(1000, 100000)
                if gcd(p, q) != 1:
                    continue
            lens.append(len(cf_partial_quotients(p, q)))
        return lens
    
    n_s = 3000
    lens_prime = length_dist(n_s, True)
    lens_rand = length_dist(n_s, False)
    import statistics
    print(f"连分数长度: 素数对 mean={statistics.mean(lens_prime):.3f} std={statistics.stdev(lens_prime):.3f}")
    print(f"            随机对 mean={statistics.mean(lens_rand):.3f} std={statistics.stdev(lens_rand):.3f}")
    # 部分商分布（Gauss-Kuzmin 预测 P(a) = log₂(1+1/(a(a+2)))——）
    print("\n部分商分布 vs Gauss-Kuzmin 预测：")
    # 收集所有部分商（素数对——）
    all_pq = []
    for _ in range(2000):
        p, q = random.sample(primes[100:], 2)
        all_pq.extend(cf_partial_quotients(p, q)[1:])  # 去 a0
    from collections import Counter
    cnt = Counter(all_pq)
    total = sum(cnt.values())
    print(f"  a=1: 实际 {cnt[1]/total:.4f}——GK 预测 {np.log2(4/3):.4f}")
    print(f"  a=2: 实际 {cnt[2]/total:.4f}——GK 预测 {np.log2(9/8):.4f}")
    print(f"  a=3: 实际 {cnt[3]/total:.4f}——GK 预测 {np.log2(16/15):.4f}")
    
    print("\n" + "="*70)
    print("结论分析")
    print("="*70)
    print("""
如果素数对连分数 = Gauss-Kuzmin 统计（与随机对无差异——）：
→ Euclid 路径 = 连分数 = Gauss map 动力学——γ 层（测度论——）
→ 素数没有特殊连分数结构——判死（modular/CF 换皮确认——）

如果素数对有差异（部分商/长度偏离 GK——）：
→ 素数在连分数层有特殊结构——值得继续（稀有——）
""")

if __name__ == "__main__":
    main()
