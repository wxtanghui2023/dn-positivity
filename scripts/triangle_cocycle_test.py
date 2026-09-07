#!/usr/bin/env python3
"""
三角和乐 2 上同调测试：Ω 是否可分离成对（2-余边界）？
Δ(p,q,q',r,r') = logΩ(p,q,r) − logΩ(p,q',r) − logΩ(p,q,r') + logΩ(p,q',r') (mod 2)
- Δ ≡ 0：Ω 是 2-余边界（= A(p,q)B(q,r)C(r,p) 型——可分离成对——无真 3 体记忆——死）
- Δ ≠ 0：真 3 体异常（不可约相位记忆——活路信号！）
"""
import numpy as np
from math import gcd

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

def omega_add(p, q):
    """Liouville(p+q)"""
    n = p + q
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

def load_primes(n=3000):
    p = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    return p[:n].tolist()

def Omega(p, q, r, conn):
    return conn(p,q) * conn(q,r) * conn(r,p)

def log2(x):
    return 0 if x == 1 else 1  # mod 2 log

def cocycle_test(primes, conn, name, n_tests=500):
    """混合差分测试——随机 (q,q',r,r')——固定 p——检查 Δ"""
    import random
    random.seed(7)
    nonzero = 0
    total = 0
    delta_dist = {}
    for _ in range(n_tests):
        p, q, q2, r, r2 = random.sample(primes[1:], 5)
        # Δ = logΩ(p,q,r) − logΩ(p,q',r) − logΩ(p,q,r') + logΩ(p,q',r') mod 2
        d = (log2(Omega(p,q,r,conn)) - log2(Omega(p,q2,r,conn)) 
             - log2(Omega(p,q,r2,conn)) + log2(Omega(p,q2,r2,conn))) % 2
        delta_dist[d] = delta_dist.get(d, 0) + 1
        total += 1
        if d != 0:
            nonzero += 1
    print(f"\n[{name}] 混合差分 Δ 分布: {delta_dist}")
    print(f"  非零比例: {nonzero/total:.3f}")
    if nonzero == 0:
        print(f"  → Δ ≡ 0：Ω 是 2-余边界——可分离成对——无真 3 体记忆（死——）")
    else:
        print(f"  → Δ ≠ 0：有真 3 体异常——不可约相位记忆的候选信号！（但需排除是'2-体函数的伪装'——）")

def main():
    primes = load_primes(3000)
    print(f"素数: {len(primes)}（最大 {primes[-1]}）")
    
    print("\n" + "="*70)
    print("上同调混合差分测试（真 3 体记忆检测）")
    print("="*70)
    
    cocycle_test(primes, omega_legendre, "Legendre 连接")
    cocycle_test(primes, omega_euclid, "Euclid 路径连接")
    cocycle_test(primes, omega_add, "加法 Liouville 连接")

if __name__ == "__main__":
    main()
