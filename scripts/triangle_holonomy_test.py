#!/usr/bin/env python3
"""
三角和乐测试：算术连接的相位记忆检测
Ω(p,q,r) = ω(p,q)·ω(q,r)·ω(r,p)
- Ω ≡ 1：平凡（可积——无记忆——）
- Ω 可分离（= χ1(p)χ2(q)χ3(r)）：字符化（死——无不可约记忆——）
- Ω 非平凡且不可分离：不可积（有相位记忆——活路信号！）

候选连接：
1. Legendre (p/q)——预期：字符化（唐先生已杀——确认——）
2. 连分数/Euclid 路径相位 ω(p,q) = (-1)^{欧几里得步数}
3. 加法连接 ω(p,q) = (-1)^{Ω(p+q)}（Liouville 于和——）
"""
import numpy as np
from math import gcd

def legendre(a, p):
    """Legendre 符号 (a/p)——p 奇素数"""
    return pow(a % p, (p-1)//2, p) if a % p else 0  # 返回 0/1/p-1——需转 ±1

def legendre_sym(a, p):
    v = pow(a % p, (p-1)//2, p)
    if v == 0:
        return 0
    return 1 if v == 1 else -1

def euclid_steps(a, b):
    """欧几里得算法步数"""
    steps = 0
    while b:
        a, b = b, a % b
        steps += 1
    return steps

def omega_legendre(p, q):
    return legendre_sym(p, q)

def omega_euclid(p, q):
    """欧几里得路径相位：(-1)^{步数}——非群字符候选"""
    return (-1)**(euclid_steps(p, q) % 2)

def omega_add(p, q):
    """加法连接：Liouville 于 p+q——λ(n) = (-1)^{Ω(n)}"""
    n = p + q
    # 因子分解算 Ω(n)
    cnt = 0
    d = 2
    m = n
    while d*d <= m:
        while m % d == 0:
            m //= d
            cnt += 1
        d += 1
    if m > 1:
        cnt += 1
    return (-1)**(cnt % 2)

def load_primes(n=5000):
    try:
        p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
        return p[:n].tolist()
    except:
        print("加载失败")
        return []

def separability_check(Omega_vals, triples):
    """检查 Ω 是否可分离（字符化——）：Ω(p,q,r) = f(p)·g(q)·h(r)？
    用数值方法：如果 Ω 可分离——对所有固定 (q,r)——Ω(p,q,r) 作为 p 的函数只能取少数模式"""
    # 简化检查：统计不同 Ω 值 + 检查是否依赖"模类"（模 4——模 8——）
    # 真可分离性检查复杂——先用"Ω 值的分布 + 与模类的相关性"初步判断
    vals = set(Omega_vals)
    print(f"  Ω 取值集合: {vals}")
    return len(vals)

def main():
    primes = load_primes(3000)
    print(f"素数: {len(primes)} 个（最大 {primes[-1]}）")
    
    print("\n" + "="*70)
    print("测试 1：Legendre 连接 ω(p,q) = (p/q)")
    print("="*70)
    # 随机三角
    import random
    random.seed(42)
    N_test = 2000
    omega_dist = {}
    char_like = True
    for _ in range(N_test):
        p, q, r = random.sample(primes[1:], 3)  # 跳过 2（奇数素数——）
        o1 = omega_legendre(p, q)
        o2 = omega_legendre(q, r)
        o3 = omega_legendre(r, p)
        Om = o1 * o2 * o3
        omega_dist[Om] = omega_dist.get(Om, 0) + 1
    print(f"Ω 分布: {omega_dist}")
    # 检查 Ω 是否依赖 (p,q,r) mod 4 类
    print("检查 Ω 是否只依赖 mod 4 类（字符化信号——）:")
    classes = {}
    for _ in range(500):
        p, q, r = random.sample(primes[1:], 3)
        Om = omega_legendre(p,q)*omega_legendre(q,r)*omega_legendre(r,p)
        key = (p%4, q%4, r%4)
        classes.setdefault(key, set()).add(Om)
    all_single = all(len(v) == 1 for v in classes.values())
    print(f"  每个 mod4 类组合的 Ω 唯一: {all_single}")
    if all_single:
        print(f"  → Ω 只依赖 mod 4 类——完全字符化（死——无记忆——）确认唐先生判断")
    
    print("\n" + "="*70)
    print("测试 2：Euclid 路径连接 ω(p,q) = (-1)^{欧几里得步数}")
    print("="*70)
    omega_dist2 = {}
    for _ in range(N_test):
        p, q, r = random.sample(primes[1:], 3)
        Om = omega_euclid(p,q)*omega_euclid(q,r)*omega_euclid(r,p)
        omega_dist2[Om] = omega_dist2.get(Om, 0) + 1
    print(f"Ω 分布: {omega_dist2}")
    if len(omega_dist2) == 1:
        print("→ Ω 恒 1——平凡（可积——死——）")
    else:
        # 检查是否字符化——Euclid 步数的 mod 4 类依赖？
        classes2 = {}
        for _ in range(500):
            p, q, r = random.sample(primes[1:], 3)
            Om = omega_euclid(p,q)*omega_euclid(q,r)*omega_euclid(r,p)
            key = (p%4, q%4, r%4)
            classes2.setdefault(key, set()).add(Om)
        all_single2 = all(len(v) == 1 for v in classes2.values())
        print(f"  每个 mod4 类组合的 Ω 唯一: {all_single2}")
        # 再看 mod 8/其他
        classes3 = {}
        for _ in range(500):
            p, q, r = random.sample(primes[1:], 3)
            Om = omega_euclid(p,q)*omega_euclid(q,r)*omega_euclid(r,p)
            key = (p%8, q%8, r%8)
            classes3.setdefault(key, set()).add(Om)
        all_single3 = all(len(v) == 1 for v in classes3.values())
        print(f"  每个 mod8 类组合的 Ω 唯一: {all_single3}")
    
    print("\n" + "="*70)
    print("测试 3：加法连接 ω(p,q) = Liouville(p+q)")
    print("="*70)
    omega_dist3 = {}
    for _ in range(2000):
        p, q, r = random.sample(primes[1:], 3)
        Om = omega_add(p,q)*omega_add(q,r)*omega_add(r,p)
        omega_dist3[Om] = omega_dist3.get(Om, 0) + 1
    print(f"Ω 分布: {omega_dist3}")

if __name__ == "__main__":
    main()
