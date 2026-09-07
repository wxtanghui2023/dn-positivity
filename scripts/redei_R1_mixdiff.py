#!/usr/bin/env python3
"""
R1 核心：四点混合差分——三体不可约性
若 R(a,b,c) = f(a,b) + g(b,c) + h(c,a)（F₂ 中——pairwise 可分解——）
则对固定 b——四点混合：
Δ = R(a,b,c) + R(a',b,c) + R(a,b,c') + R(a',b,c') = 0（恒——）
（f 的 a-项消——g 不含 a——h 的 c-项消——交叉全消——）

Δ ≠ 0 → R 不可 pairwise 分解——真三体信号
"""
import math, sys, itertools, random
sys.path.insert(0, 'scripts')
from redei_v4 import redei_v4, legendre
import numpy as np

def R_F2(a, b, c):
    """R ∈ {0,1}——F₂ 值"""
    v = redei_v4(a, b, c)
    return None if v is None else (0 if v == 1 else 1)

def main():
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5 and p < 15000][:600]
    print(f"素数池: {len(p1)}")
    random.seed(43)
    
    # 找固定 b——多组 (a,c) 四点
    n_test = 0
    n_nonzero = 0
    n_zero = 0
    n_na = 0
    
    # 先找一些 b（admissible 对多——）
    # 对每个测试：固定 b——取 a, a', c, c'——四点 R 值——算 Δ
    for _ in range(400):
        b, a1, a2, c1, c2 = random.sample(p1, 5)
        # 需要 (a,b,c) 全 admissible——检查六对 Legendre
        # 简化：测四点需要 (a1,b,c1),(a2,b,c1),(a1,b,c2),(a2,b,c2) 都可算
        triples = [(a1,b,c1), (a2,b,c1), (a1,b,c2), (a2,b,c2)]
        ok = True
        for (x, y, z) in triples:
            if not (legendre(x,y)==1 and legendre(y,z)==1 and legendre(z,x)==1):
                ok = False
                break
        if not ok:
            continue
        vals = []
        for (x, y, z) in triples:
            v = R_F2(x, y, z)
            if v is None:
                vals = None
                break
            vals.append(v)
        if vals is None:
            n_na += 1
            continue
        n_test += 1
        delta = (vals[0] + vals[1] + vals[2] + vals[3]) % 2
        if delta != 0:
            n_nonzero += 1
        else:
            n_zero += 1
        if n_test >= 100:
            break
    
    print(f"\n四点测试: {n_test}——Δ≠0: {n_nonzero}——Δ=0: {n_zero}——NA: {n_na}")
    if n_nonzero > 0:
        print(f"→ Δ≠0 比例: {n_nonzero/n_test:.2f}——R 不可 pairwise 分解——真三体信号！")
    else:
        print("→ Δ 全 0——R 可能 pairwise 可分解（待更多测试——）")

if __name__ == "__main__":
    main()
