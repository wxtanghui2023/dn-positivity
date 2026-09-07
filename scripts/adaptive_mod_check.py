#!/usr/bin/env python3
"""
自适应模字符检查：Ω(p,q,r) 是否依赖 r mod pq（Legendre 预期是——Euclid 测试——）
如果 Ω 对固定 (p,q) 是 r 的模 pq 字符——仍是字符机制（死——模随对增长——）
如果连 mod pq 都不依赖——真非字符（相位记忆候选——活——）
"""
import numpy as np
import random

def legendre_sym(a, p):
    v = pow(a % p, (p-1)//2, p)
    if v == 0:
        return 0
    return 1 if v == 1 else -1

def euclid_steps(a, b):
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return steps

def omega_legendre(p, q):
    return legendre_sym(p, q)

def omega_euclid(p, q):
    return (-1)**(euclid_steps(p, q) % 2)

def load_primes(n=50000):
    p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    return p[:n].tolist()

def test_mod_pq(primes, conn, name, n_pairs=10, n_per=8):
    """对几对 (p,q)——测 Ω(p,q,r) 是否依赖 r mod pq"""
    random.seed(11)
    print(f"\n[{name}] Ω(p,q,r) 对固定 (p,q) 是否 = χ(r mod pq)？")
    for _ in range(n_pairs):
        p, q = random.sample(primes[100:5000], 2)  # 中等的 p,q
        # 找同余类 r ≡ a mod pq 的多个素数——测 Ω 是否一致
        # 直接：取 r1, r2 满足 r1 ≡ r2 mod pq——测 Ω(r1) vs Ω(r2)
        pq = p * q
        consistent = 0
        total = 0
        for _ in range(20):
            r1, r2 = random.sample(primes[100:20000], 2)
            # 找与 r1 同余 mod pq 的 r2'——用 r1 + k·pq（素数性不保——改用最近素数——难）
            # 替代：直接测 Ω 是否 = f(r mod pq)——取不同模类比较
            # 简化：检查 Ω 的 2-周期（r → r + pq 的素数——不一定素——）
            pass
        # 直接方案：对同余类采样——用小 pq（p,q 取小——）
        break
    
    # 用小 p,q（pq 小——同余类可采样）
    print("用小 p,q（pq ≤ 2000——同余类采样——）")
    small = [p for p in primes[1:2000] if p > 5]
    for _ in range(5):
        p, q = random.sample(small, 2)
        pq = p*q
        if pq > 3000:
            continue
        # 收集 r mod pq 的类——每个类多个素数——测一致性
        by_class = {}
        for r in primes[100:50000]:
            if r > pq * 3:  # 限制范围（够采样——）
                break
            Om = conn(p,q)*conn(q,r)*conn(r,p)
            by_class.setdefault(r % pq, set()).add(Om)
        multi = {k: v for k, v in by_class.items() if len(v) > 1}
        # 检查每个类是否一致
        n_inconsistent = len([1 for v in by_class.values() if len(v) > 1])
        n_classes = len(by_class)
        print(f"  p={p}, q={q} (pq={pq}): {n_inconsistent}/{n_classes} 个类内不一致"
              f"——{'模 pq 字符化 ✓（死）' if n_inconsistent == 0 else '非模 pq 字符！'}")
        if n_inconsistent > 0:
            # 看看不一致长什么样
            ex = [k for k, v in by_class.items() if len(v) > 1][:2]
            for k in ex:
                print(f"    类 r≡{k} mod {pq}: Ω ∈ {by_class[k]}")

def main():
    primes = load_primes(50000)
    print(f"素数: {len(primes)}（最大 {primes[-1]}）")
    
    test_mod_pq(primes, omega_legendre, "Legendre")
    test_mod_pq(primes, omega_euclid, "Euclid")

if __name__ == "__main__":
    main()
