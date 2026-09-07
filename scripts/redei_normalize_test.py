#!/usr/bin/env python3
"""
minimal-at-2 normalization：对 β = x+y√a——找唯一 t ∈ {±1, ±2} 使 tβ 是 (O/4O) 的平方
O = Z[√a]——a ≡ 1 mod 4 素数——(O/4O) 有限环

平方检查：γ = u+v√a mod 4 是平方 ⟺ ∃ (p,q): γ ≡ (p+q√a)² mod 4
= (p²+aq²) + 2pq√a mod 4
"""
import math, sys
sys.path.insert(0, 'scripts')

def is_square_mod4O(a, u, v):
    """γ = u+v√a mod 4 是否平方（在 O/4O——）"""
    u %= 4
    v %= 4
    a_mod = a % 4
    for p in range(4):
        for q in range(4):
            # (p+q√a)² = p² + 2pq√a + a q²
            u2 = (p*p + a_mod*q*q) % 4
            v2 = (2*p*q) % 4
            if u2 == u and v2 == v:
                return True
    return False

def normalize_t(a, x, y, z):
    """找 t ∈ {±1, ±2} 使 tβ 模 4O 是平方（β = x+y√a——）
    注意：β 可能含 z² 因子（N(β)=bz²——）——规范化用 β' = β/z（范数 b——）？
    但 β' 可能分数（x/z——）——先处理整数情形（z 的因子吸收进平方——）
    用原始 β = x+y√a（整数——）——tβ 的平方性——"""
    candidates = [1, -1, 2, -2]
    found = []
    for t in candidates:
        u = (t*x) % 4
        v = (t*y) % 4
        if is_square_mod4O(a, u, v):
            found.append(t)
    return found

def legendre_sym(a, p):
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p-1)//2, p)
    return 1 if v == 1 else -1

def main():
    import numpy as np, random
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:300]
    random.seed(17)
    
    print("minimal-at-2 normalization 测试（找 t 的分布——）")
    print("a ≡ 1 mod 4 素数——β = x+y√a 从 x²−ay²=bz² 来——")
    t_dist = {}
    n_found = 0
    n_multi = 0
    for _ in range(3000):
        a, b = random.sample(p1, 2)
        if legendre_sym(a, b) != 1:
            continue
        # 找解（小——）
        sol = None
        for z in range(1, 20):
            for y in range(1, 3000):
                x2 = b*z*z + a*y*y
                x = math.isqrt(x2)
                if x*x == x2:
                    sol = (x, y, z)
                    break
            if sol:
                break
        if sol is None:
            continue
        x, y, z = sol
        ts = normalize_t(a, x, y, z)
        if len(ts) == 1:
            n_found += 1
            t_dist[ts[0]] = t_dist.get(ts[0], 0) + 1
        elif len(ts) > 1:
            n_multi += 1
            if n_multi <= 3:
                print(f"  多 t: (a,b)=({a},{b})——β=({x},{y})——t ∈ {ts}")
        # 也测 -β 的（解的正负——）
        if n_found + n_multi >= 30:
            break
    
    print(f"\n唯一 t 找到: {n_found}——多 t: {n_multi}")
    print(f"t 分布: {t_dist}")
    print("（期望：几乎全唯一——Prop 7.3(1)——多 t 可能是数值问题或特例——）")

if __name__ == "__main__":
    main()
