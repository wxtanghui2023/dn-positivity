#!/usr/bin/env python3
"""
Euclid 曲率的反对称性验证：
Ω(p,q,r)·Ω(p,r,q) = ?——如果恒 = -1——Ω 是交替 3-形式（结构——非随机——）
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

def load_primes(n=20000):
    p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    return p[:n].tolist()

def main():
    primes = load_primes(20000)
    print(f"素数: {len(primes)}")
    random.seed(17)
    
    print("="*70)
    print("验证：Ω(p,q,r)·Ω(p,r,q) 是否恒 = −1（反对称——）")
    print("="*70)
    n_minus = 0
    n_plus = 0
    n_total = 2000
    for _ in range(n_total):
        p, q, r = random.sample(primes[1:], 3)
        Om1 = omega_euclid(p,q)*omega_euclid(q,r)*omega_euclid(r,p)
        Om2 = omega_euclid(p,r)*omega_euclid(r,q)*omega_euclid(q,p)
        prod = Om1 * Om2
        if prod == -1:
            n_minus += 1
        else:
            n_plus += 1
    print(f"Ω(p,q,r)·Ω(p,r,q): 乘积=−1 次数: {n_minus}——乘积=+1 次数: {n_plus}")
    if n_plus == 0:
        print("→ 恒反对称（Ω 是交替 3-形式——）——强结构！")
    else:
        print(f"→ 非恒反对称（{n_plus} 次例外——）——检查例外模式")
    
    # 看是否有更一般的置换结构
    print("\n测 Ω 在 6 个置换下的取值模式：")
    for _ in range(5):
        p, q, r = random.sample(primes[1:], 3)
        def Om(a, b, c):
            return omega_euclid(a,b)*omega_euclid(b,c)*omega_euclid(c,a)
        # 循环不变：Om(p,q,r) = Om(q,r,p) = Om(r,p,q)
        # 反循环：Om(p,r,q) = Om(r,q,p) = Om(q,p,r)
        circ = Om(p,q,r)
        anti = Om(p,r,q)
        print(f"  ({p},{q},{r}): 循环值={circ}——反循环值={anti}——比率={circ*anti}")
    
    # 更深入：Ω 是否是"叉积型"（Ω(p,q,r) = sgn 结构 × 单体函数——）
    # 检查 Ω(p,q,r) 是否 = χ(p)χ(q)χ(r)·sgn(p,q,r) 型（可分离×置换符号——）
    print("\n检查 Ω 的'完全可分离×置换符号'假设：")
    print("（若 Ω(p,q,r) = s(p,q,r)·χ(p)χ(q)χ(r)——则 Ω(p,q,r)·sgn 可分离——）")
    # 测：对固定 p——Ω(p,q,r)Ω(p,q',r)Ω(p,q,r')Ω(p,q',r') 的符号——若 Ω=χ(p)χ(q)χ(r)·sgn——此积 = +1
    # （因为 χ 部分消——sgn 部分…… sgn(p,q,r) 不是 2 可加的——复杂）
    # 直接测 Ω 的"2-可分离度"：固定 p,q——Ω 随 r——是否 = 常数×χ_{pq}(r)（模 pq 字符——）
    print("\n测 Ω(p,q,r) 对固定 (p,q) 是否 = χ_{pq}(r)·常数（模 pq——）")
    p, q = random.sample(primes[100:3000], 2)
    pq = p*q
    by_class = {}
    for r in primes[100:20000]:
        Om = omega_euclid(p,q)*omega_euclid(q,r)*omega_euclid(r,p)
        by_class.setdefault(r % pq, set()).add(Om)
    n_inconsistent = len([1 for v in by_class.values() if len(v) > 1])
    print(f"  p={p}, q={q}: {n_inconsistent}/{len(by_class)} 类不一致——"
          f"{'模 pq 字符（死——）' if n_inconsistent == 0 else '非模 pq 字符（活——）'}")

if __name__ == "__main__":
    main()
