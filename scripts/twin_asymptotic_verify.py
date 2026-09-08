#!/usr/bin/env python3
"""
孪生渐近验证：π₂(x) vs 2C₂·x/log²x——孪生常数 C₂ ≈ 0.6602
验证孪生计数与 HL 渐近的比值——收敛到 1
"""
import numpy as np
from math import log

def sieve_primes(N):
    """埃氏筛——返回素数列表"""
    is_prime = np.ones(N+1, dtype=bool)
    is_prime[:2] = False
    for i in range(2, int(N**0.5)+1):
        if is_prime[i]:
            is_prime[i*i::i] = False
    return np.nonzero(is_prime)[0]

def twin_constant(plist):
    """孪生常数 C₂ = Π_{p>2}(1−1/(p−1)²)"""
    C2 = 1.0
    for p in plist:
        if p > 2:
            C2 *= (1 - 1.0/(p-1)**2)
    return C2

def main():
    print("="*70)
    print("孪生渐近验证：π₂(x) vs 2C₂x/log²x")
    print("="*70)
    
    N = 2000000
    primes = sieve_primes(N)
    print(f"素数到 {N}: {len(primes)} 个")
    
    # 孪生常数（用全部素数——收敛快——）
    C2 = twin_constant(primes[:10000])
    print(f"C₂ ≈ {C2:.6f}（文献 0.6602——）")
    
    # 孪生对计数
    pset = set(primes.tolist())
    twin_count = sum(1 for p in primes if (p+2) in pset)
    print(f"孪生对（p, p+2 ≤ {N}）: {twin_count}")
    
    # 渐近比较
    print("\nπ₂(x) vs 2C₂x/log²x:")
    for x in [50000, 100000, 200000, 500000, 1000000, 2000000]:
        pi2_x = sum(1 for p in primes if p <= x and (p+2) in pset)
        asym = 2*C2*x/log(x)**2
        ratio = pi2_x/asym
        print(f"  x={x:>8}: π₂(x)={pi2_x:>5}——渐近={asym:.0f}——比值={ratio:.4f}")
    
    # 带权形式 T(x) = Σ_{p≤x} 1（孪生——不含 log 权——直接素数对）
    # 以及常数修正（低阶项——）——检查 (比值−1)·log x
    print("\n比值→1 的收敛（(比值−1)·logx——低阶修正——）:")
    prev = None
    for x in [50000, 200000, 500000, 1000000, 2000000]:
        pi2_x = sum(1 for p in primes if p <= x and (p+2) in pset)
        asym = 2*C2*x/log(x)**2
        ratio = pi2_x/asym
        corr = (ratio-1)*log(x)
        print(f"  x={x:>8}: 比值={ratio:.4f}——(比值−1)·logx = {corr:+.3f}")

if __name__ == "__main__":
    main()
