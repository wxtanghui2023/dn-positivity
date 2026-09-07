#!/usr/bin/env python3
"""
Euclid 连接曲率结构：非字符但有意义吗？
测：Ω(p,q,r) = ω(p,q)ω(q,r)ω(r,p)——ω(p,q) = (-1)^{欧几里得步数}
1. 曲率是否有系统性偏向（特定构型——）还是纯随机？
2. 曲率随尺度（素数大小——）有没有演化？
"""
import numpy as np
import random

def euclid_steps(a, b):
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return steps

def omega_euclid(p, q):
    return (-1)**(euclid_steps(p, q) % 2)

def load_primes(n=50000):
    p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    return p[:n].tolist()

def main():
    primes = load_primes(50000)
    print(f"素数: {len(primes)}（最大 {primes[-1]}）")
    random.seed(5)
    
    print("\n" + "="*70)
    print("测试 1：Euclid 连接的单连接值 ω(p,q) 结构")
    print("="*70)
    # ω(p,q) = (-1)^{步数}——步数分布
    steps_dist = {}
    for _ in range(3000):
        p, q = random.sample(primes[1:], 2)
        s = euclid_steps(p, q)
        steps_dist[s] = steps_dist.get(s, 0) + 1
    print(f"步数分布: {dict(sorted(steps_dist.items()))}")
    # ω 的偏向
    omega_plus = sum(v for k, v in steps_dist.items() if k % 2 == 0)
    omega_minus = sum(v for k, v in steps_dist.items() if k % 2 == 1)
    print(f"ω=+1: {omega_plus}——ω=−1: {omega_minus}——偏向: {omega_plus/(omega_plus+omega_minus):.3f}")
    
    print("\n" + "="*70)
    print("测试 2：曲率 Ω 随尺度的偏向")
    print("="*70)
    # 分尺度带测 Ω 偏向
    bands = [(100, 1000), (1000, 5000), (5000, 20000), (20000, 100000)]
    for lo, hi in bands:
        band_primes = [p for p in primes[1:] if lo <= p <= hi]
        if len(band_primes) < 100:
            continue
        plus = 0
        minus = 0
        for _ in range(1000):
            p, q, r = random.sample(band_primes, 3)
            Om = omega_euclid(p,q)*omega_euclid(q,r)*omega_euclid(r,p)
            if Om == 1:
                plus += 1
            else:
                minus += 1
        print(f"  p,q,r ∈ [{lo},{hi}]: Ω=+1: {plus}——Ω=−1: {minus}——偏向: {plus/(plus+minus):.3f}")
    
    print("\n" + "="*70)
    print("测试 3：曲率是否依赖'大小关系'（p<q<r vs 乱序——）")
    print("="*70)
    # 排序 vs 乱序的曲率
    for _ in range(3):
        p, q, r = random.sample(primes[100:5000], 3)
        s = sorted([p, q, r])
        Om_sorted = omega_euclid(s[0],s[1])*omega_euclid(s[1],s[2])*omega_euclid(s[2],s[0])
        # 乱序（不同环向——）
        Om_other = omega_euclid(p,r)*omega_euclid(r,q)*omega_euclid(q,p)
        print(f"  ({p},{q},{r}): 排序环 Ω={Om_sorted}——反环 Ω={Om_other}——乘积={Om_sorted*Om_other}")
    
    print("\n" + "="*70)
    print("测试 4：曲率的'对-依赖'（是否 = A(p,q)B(q,r)C(r,p) 型——测 4 点混合）")
    print("="*70)
    # 4 点：测 logΩ 的 3-上闭链性——跳过复杂部分——直接测 2 体可分离性
    print("测 log₂ω(p,q)（步数奇偶）是否可分离成 u(p)+v(q)：")
    # 若 ω(p,q) = u(p)v(q)——ω(p,q)ω(p,q')ω(p',q)ω(p',q') = 1 恒——测 4 点积
    anomalous = 0
    for _ in range(500):
        p, p2, q, q2 = random.sample(primes[1:10000], 4)
        prod = (omega_euclid(p,q)*omega_euclid(p,q2)*omega_euclid(p2,q)*omega_euclid(p2,q2))
        if prod != 1:
            anomalous += 1
    print(f"  4 点积 ≠ 1 的比例: {anomalous/500:.3f}（0 = 可分离——非 0 = 真 2 体不可约——）")

if __name__ == "__main__":
    main()
