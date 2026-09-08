#!/usr/bin/env python3
"""
Rédei 符号 [p,q,r]——路径 A 修正版（单点 Legendre——）
验证：六置换对称性 + norm 解独立性 + 值域分布
"""
import sys, math
sys.path.insert(0, 'scripts')
from pqa_solver import solve_norm_fast

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

def redei(p, q, r):
    """[p,q,r]——p,q,r ≡1 mod 4——两两互余——单点 Legendre 符号
    用 β = x+y√p——N(β)=q——[p,q,r] = (β/p)_r（Q(√p) 中 r 的素点——）"""
    if p % 4 != 1 or q % 4 != 1 or r % 4 != 1:
        return None
    if legendre_sym(p, q) != 1 or legendre_sym(q, r) != 1 or legendre_sym(r, p) != 1:
        return None
    sol = solve_norm_fast(p, q)
    if sol is None:
        return None
    x, y = sol
    s = sqrt_mod_p(p % r, r)
    if s is None:
        return None
    b1 = (x + y*s) % r
    if b1 == 0:
        return None  # 分歧情形——暂跳过
    return legendre_sym(b1, r)

def main():
    import numpy as np, random
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:1500]
    random.seed(42)
    
    print("="*70)
    print("六置换对称性测试 [p,q,r] = [q,p,r] = [p,r,q] = ...")
    print("="*70)
    import itertools
    n_full = 0
    n_sym_ok = 0
    n_sym_fail = 0
    n_partial = 0
    dist = {}
    
    for _ in range(4000):
        p, q, r = random.sample(p1, 3)
        if not (legendre_sym(p,q)==1 and legendre_sym(q,r)==1 and legendre_sym(r,p)==1):
            continue
        # 六种顺序（用统一的"第一个参数"做 norm 方程——需要 q 是 norm——）
        # [a,b,c]——用 a 做 norm 方程（x²−ay²=b——）
        def sym_val(a, b, c):
            return redei(a, b, c)
        vals = {}
        for perm in itertools.permutations([p, q, r]):
            a, b, c = perm
            v = sym_val(a, b, c)
            vals[perm] = v
        # 收集非 None 的
        non_none = {k: v for k, v in vals.items() if v is not None}
        if len(non_none) == 6:
            n_full += 1
            vs = set(non_none.values())
            if len(vs) == 1:
                n_sym_ok += 1
                dist[vs.pop()] = dist.get(list(vs)[0] if len(vs)==1 else 0, 0) + 1
            else:
                n_sym_fail += 1
                if n_sym_fail <= 3:
                    print(f"  六置换不一致: ({p},{q},{r})——vals={ {k[:2]: v for k,v in non_none.items()} }")
        elif len(non_none) >= 2:
            n_partial += 1
            vs = set(non_none.values())
            if len(vs) == 1:
                n_sym_ok += 1
            else:
                n_sym_fail += 1
                if n_sym_fail <= 5:
                    print(f"  部分置换不一致: ({p},{q},{r})——{non_none}")
    
    print(f"\n全 6 置换可算: {n_full}——部分: {n_partial}——对称 OK: {n_sym_ok}——FAIL: {n_sym_fail}")
    if n_sym_fail == 0:
        print("✅ 对称性全部通过！")
    else:
        print("❌ 对称性失败——实现有误！")
    print(f"符号分布（对称性通过的——）: {dist}")

if __name__ == "__main__":
    main()
