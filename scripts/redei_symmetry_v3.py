#!/usr/bin/env python3
"""
Rédei 对称性验证 v3——缓存 (a,b) norm 解——比较多方向一致性
"""
import sys, time, itertools
sys.path.insert(0, 'scripts')
import numpy as np, random

# 直接从 redei_v2 导入组件（含 Tonelli——）
from redei_v2 import legendre_sym, solve_norm_sympy, sqrt_mod_p

def redei_cached(a, b, c, cache):
    if (a, b) not in cache:
        cache[(a, b)] = solve_norm_sympy(a, b)
    sol = cache[(a, b)]
    if sol is None:
        return None
    xx, yy = sol
    s = sqrt_mod_p(a % c, c)
    if s is None:
        return None
    b1 = (xx + yy*s) % c
    if b1 == 0:
        return None
    return legendre_sym(b1, c)

def main():
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:400]
    random.seed(5)
    
    n_adm = n_multi = n_consistent = n_inconsistent = 0
    dist = {}
    t0 = time.time()
    cache = {}
    
    for _ in range(600):
        p, q, r = random.sample(p1, 3)
        if not (legendre_sym(p,q)==1 and legendre_sym(q,r)==1 and legendre_sym(r,p)==1):
            continue
        n_adm += 1
        vals, dirs = [], []
        for perm in itertools.permutations([p, q, r]):
            v = redei_cached(*perm, cache)
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
                    print(f"❌ 不一致: ({p},{q},{r})——{list(zip(dirs, vals))}")
    
    print(f"\nadmissible: {n_adm}——多方向: {n_multi}——一致: {n_consistent}——不一致: {n_inconsistent}")
    print(f"耗时: {time.time()-t0:.1f}s——norm 缓存: {len(cache)}")
    print("✅ 对称性通过！" if n_inconsistent == 0 and n_multi > 0 else "❌ inconsistency")
    print(f"分布: {dist}")

if __name__ == "__main__":
    main()
