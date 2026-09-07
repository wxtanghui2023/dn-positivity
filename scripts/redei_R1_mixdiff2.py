#!/usr/bin/env python3
"""
R1 四点混合差分——构造性采样版
两阶段：先固定 b——收集 a 池（与 b 互余——）再收集 c 池（与 a1,a2,b 全互余——）
"""
import math, sys, random
sys.path.insert(0, 'scripts')
from redei_v4 import redei_v4, legendre
import numpy as np

def R_F2(a, b, c):
    v = redei_v4(a, b, c)
    return None if v is None else (0 if v == 1 else 1)

def main():
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5 and p < 10000][:400]
    print(f"素数池: {len(p1)}")
    random.seed(47)
    
    n_test = 0
    n_nonzero = 0
    n_zero = 0
    
    # 固定 b——找 a 池
    for trial in range(200):
        b = random.choice(p1)
        # a 池：与 b 互余
        a_pool = [a for a in p1 if a != b and legendre(a, b) == 1]
        if len(a_pool) < 30:
            continue
        # 取 a1, a2（互余——(a1/a2) 不需要——但四点的 c 需要与全互余——）
        a1, a2 = random.sample(a_pool, 2)
        # c 池：与 a1, a2, b 全互余
        c_pool = []
        for c in p1:
            if c in (a1, a2, b):
                continue
            if legendre(b, c) == 1 and legendre(a1, c) == 1 and legendre(a2, c) == 1:
                c_pool.append(c)
        if len(c_pool) < 20:
            continue
        c1, c2 = random.sample(c_pool, 2)
        # 四点
        triples = [(a1,b,c1), (a2,b,c1), (a1,b,c2), (a2,b,c2)]
        vals = []
        ok = True
        for (x, y, z) in triples:
            v = R_F2(x, y, z)
            if v is None:
                ok = False
                break
            vals.append(v)
        if not ok:
            continue
        n_test += 1
        delta = (vals[0] + vals[1] + vals[2] + vals[3]) % 2
        if delta != 0:
            n_nonzero += 1
        else:
            n_zero += 1
        if n_test >= 80:
            break
    
    print(f"\n四点测试: {n_test}——Δ≠0: {n_nonzero}——Δ=0: {n_zero}")
    if n_test > 0:
        print(f"→ Δ≠0 比例: {n_nonzero/n_test:.2f}" + ("——真三体信号！" if n_nonzero > 0 else "——pairwise 可分解候选——"))

if __name__ == "__main__":
    main()
