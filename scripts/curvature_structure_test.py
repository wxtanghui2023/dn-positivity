#!/usr/bin/env python3
"""
曲率结构分析：三角和乐 Ω(p,q,r) 的依赖结构
问题：Ω 的"非平凡"是有限型的（依赖 mod m 类——字符化）还是真随素数不可约变化？
测：固定 (p,q)——Ω(p,q,r) 作为 r 的函数——检查是否 = 字符 × 常数（有限型）或真复杂
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

def load_primes(n=20000):
    p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    return p[:n].tolist()

def main():
    primes = load_primes(20000)
    print(f"素数: {len(primes)}（最大 {primes[-1]}）")
    
    print("\n" + "="*70)
    print("测试：固定 (p,q)——Ω(p,q,r) 随 r 的结构")
    print("="*70)
    random.seed(3)
    
    # 对 Legendre
    print("\n【Legendre 连接】")
    p, q = random.sample(primes[1:], 2)
    print(f"固定 p={p}, q={q}")
    # 测 Ω 随 r——r 取不同模类的素数
    for r_class in [1, 3, 5, 7]:
        # 取模 8 = r_class 的素数（前几个——）
        rs = [r for r in primes[1:4000] if r % 8 == r_class][:5]
        vals = {}
        for r in rs:
            Om = legendre_sym(p,q)*legendre_sym(q,r)*legendre_sym(r,p)
            vals[r] = Om
        # 检查同模类内是否一致
        uniq = set(vals.values())
        print(f"  r≡{r_class} mod 8: Ω 值集合 = {uniq}（{'同模类一致' if len(uniq)==1 else '同模类内变化！'}）")
    
    # 更系统：测 Ω 是否依赖 r mod m（扫描 m=4,8,12,16,24）
    print("\n  Ω(p,q,r) 依赖 r mod m 吗？（扫描模——）")
    for m in [4, 8, 12, 16, 20, 24]:
        r_samples = random.sample(primes[1:20000], 400)
        class_consistent = True
        by_class = {}
        for r in r_samples:
            Om = legendre_sym(p,q)*legendre_sym(q,r)*legendre_sym(r,p)
            by_class.setdefault(r % m, set()).add(Om)
        inconsistent = [k for k, v in by_class.items() if len(v) > 1]
        if inconsistent:
            print(f"    mod {m}: 有 {len(inconsistent)}/{len(by_class)} 个类内部不一致——非有限型")
        else:
            print(f"    mod {m}: 全部类内一致——Ω 依赖 r mod {m}")
    
    # 对 Euclid 连接同样测试
    print("\n【Euclid 连接】")
    p2, q2 = random.sample(primes[1:], 2)
    print(f"固定 p={p2}, q={q2}")
    for m in [4, 8, 12, 16]:
        r_samples = random.sample(primes[1:20000], 300)
        by_class = {}
        for r in r_samples:
            Om = omega_euclid(p2,q2)*omega_euclid(q2,r)*omega_euclid(r,p2)
            by_class.setdefault(r % m, set()).add(Om)
        inconsistent = [k for k, v in by_class.items() if len(v) > 1]
        if inconsistent:
            print(f"    mod {m}: 有 {len(inconsistent)}/{len(by_class)} 个类内部不一致——非有限型")
        else:
            print(f"    mod {m}: 全部类内一致——Ω 依赖 r mod {m}")

if __name__ == "__main__":
    main()
