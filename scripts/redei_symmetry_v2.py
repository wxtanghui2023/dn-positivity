#!/usr/bin/env python3
"""
Rédei 对称性测试 v2：比较任意 ≥2 个可算方向的符号一致性
[p,q,r] 的对称性 = 定理——用不同方向（norm 可解——）算——应一致
"""
import math, sys, itertools
sys.path.insert(0, 'scripts')

def solve_violent(D, N, y_max=3000000):
    for y in range(1, y_max):
        x2 = N + D*y*y
        if x2 < 0:
            continue
        x = math.isqrt(x2)
        if x*x == x2:
            return (x, y)
    return None

def legendre_sym(a, p):
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p-1)//2, p)
    return 1 if v == 1 else -1

def sqrt_mod_p(a, p):
    a %= p
    if a == 0:
        return 0
    if p == 2:
        return a
    if legendre_sym(a, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p+1)//4, p)
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while legendre_sym(z, p) != -1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q+1)//2, p)
    while t != 1:
        i = 0
        temp = t
        while temp != 1:
            temp = temp*temp % p
            i += 1
            if i == m:
                return None
        b = pow(c, 2**(m-i-1), p)
        m = i
        c = b*b % p
        t = t*c % p
        r = r*b % p
    return r

def redei_one_direction(a, b, c):
    """[a,b,c]——用 x²−ay²=b（β=x+y√a——N=b）——在 Q(√a) 中 c 的素点"""
    if a % 4 != 1 or b % 4 != 1 or c % 4 != 1:
        return None
    if legendre_sym(a, b) != 1 or legendre_sym(b, c) != 1 or legendre_sym(c, a) != 1:
        return None
    sol = solve_violent(a, b)
    if sol is None:
        return None
    x, y = sol
    s = sqrt_mod_p(a % c, c)
    if s is None:
        return None
    b1 = (x + y*s) % c
    if b1 == 0:
        return None
    return legendre_sym(b1, c)

def main():
    import numpy as np, random
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:800]
    random.seed(11)
    
    n_adm = 0
    n_multi = 0
    n_consistent = 0
    n_inconsistent = 0
    dist = {}
    
    for _ in range(3000):
        p, q, r = random.sample(p1, 3)
        if not (legendre_sym(p,q)==1 and legendre_sym(q,r)==1 and legendre_sym(r,p)==1):
            continue
        n_adm += 1
        # 收集所有可算方向
        vals = []
        dirs = []
        for perm in itertools.permutations([p, q, r]):
            v = redei_one_direction(*perm)
            if v is not None:
                vals.append(v)
                dirs.append(perm)
        if len(vals) >= 2:
            n_multi += 1
            if len(set(vals)) == 1:
                n_consistent += 1
                dist[vals[0]] = dist.get(vals[0], 0) + 1
            else:
                n_inconsistent += 1
                if n_inconsistent <= 3:
                    print(f"❌ 不一致: ({p},{q},{r})——方向值: {list(zip(dirs, vals))}")
    
    print(f"admissible: {n_adm}——多方向可算: {n_multi}——一致: {n_consistent}——不一致: {n_inconsistent}")
    if n_inconsistent == 0 and n_multi > 0:
        print("✅ 对称性通过（多方向一致——）")
    else:
        print("❌ 有 inconsistency——实现需修正")
    print(f"符号分布: {dist}")

if __name__ == "__main__":
    main()
