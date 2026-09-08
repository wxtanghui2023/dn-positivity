#!/usr/bin/env python3
"""
第一性检查：整数因子化的二阶/曲率结构候选

候选：
A. 交换子 [乘p, 乘q]——应平凡（乘法交换——）
B. 分配律缺陷（gcd/lcm 的——）——应零（分配格——）
C. Selberg 型二阶恒等式（Λ*Λ vs Λ·log——）
D. 除数的对合 d ↔ n/d——不动点 √n（½ 出现？——）
E. 因子化路径的"面积"（n→d₁→d₂→n 的 log 和——）
"""
import numpy as np
from math import gcd, log

def lcm(a, b):
    return a*b//gcd(a, b)

def prime_factors(n):
    """素因子（带重数——）"""
    facs = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            facs.append(d)
            n //= d
        d += 1
    if n > 1:
        facs.append(n)
    return facs

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def vonMangoldt(n):
    """Λ(n)"""
    facs = prime_factors(n)
    if len(set(facs)) == 1 and len(facs) >= 1:
        return log(facs[0])
    return 0.0

def main():
    print("="*70)
    print("第一性检查：因子化二阶结构候选")
    print("="*70)
    
    # A. 交换子测试——"乘p后除q" vs "除q后乘p"（在可除性上——）
    print("\nA. 交换子测试（乘/除素数——）:")
    print("   乘法交换 ⟹ 所有乘/除算子交换——交换子 = 0（代数上平凡——）")
    print("   验证 n=60: 除2再乘3 vs 乘3再除2:")
    n = 60
    # 除 2：60/2=30——乘 3：90；乘 3：180——除 2：90——相同 ✓
    print(f"   (60/2)*3 = {n//2*3}——(60*3)/2 = {n*3//2}——相同——交换 ✓")
    
    # B. 分配律缺陷
    print("\nB. 分配律缺陷（gcd/lcm——）:")
    defects = 0
    for a in range(2, 50):
        for b in range(2, 50):
            for c in range(2, 50):
                lhs = gcd(a, lcm(b, c))
                rhs = lcm(gcd(a, b), gcd(a, c))
                if lhs != rhs:
                    defects += 1
    print(f"   gcd(a,lcm(b,c)) vs lcm(gcd(a,b),gcd(a,c))——a,b,c<50——缺陷数 = {defects}（0 = 分配格——）")
    
    # C. Selberg 型恒等式
    print("\nC. Selberg 型二阶恒等式:")
    print("   (Λ*Λ)(n) vs Λ(n)log n——对 n=p^k:")
    for n in [4, 8, 9, 16, 25]:
        # (Λ*Λ)(n) = Σ_{d|n}Λ(d)Λ(n/d)
        conv = sum(vonMangoldt(d)*vonMangoldt(n//d) for d in divisors(n) if d < n)
        lhs = vonMangoldt(n)*log(n)
        print(f"   n={n} (p^k): Λ·log = {lhs:.4f}——(Λ*Λ 对角) = {conv:.4f}——差 = {lhs-conv:.4f}")
    print("   ——Λ*Λ 的 Dirichlet 级数 = (ζ'/ζ)²——奇点在零点——Euler 积闭包——")
    
    # D. 除数对合
    print("\nD. 除数对合 d ↔ n/d——不动点:")
    for n in [16, 36, 100]:
        inv_fixed = [d for d in divisors(n) if d*d == n]
        print(f"   n={n}: 对合不动点 = {inv_fixed}（=√n 当完全平方——）——½ 在指数（平凡——）")
    
    # E. 因子化路径的 log 和（n→d₁→d₂→n——）
    print("\nE. 因子化路径 log 和（闭路——）:")
    for n in [12, 30, 72]:
        ds = divisors(n)
        # 路径 n → d₁ → d₂ → n——要求 d₁|d₂|n 或 d₂|d₁？——取 d₁|n, d₂|n 且 d₁|d₂
        print(f"   n={n}:")
        for d1 in ds[1:-1]:
            for d2 in ds[1:-1]:
                if d1 < d2 and d2 % d1 == 0:
                    # 路径 log 和：log(n/d₁) + log(d₂/d₁) + log(n/d₂)——方向注意——
                    # 实际闭路 n→d₁→d₂→n：步长 log 和 = log(n/d1)+log(d2/d1)+log(n/d2)？——符号——
                    s = log(n/d1) + log(d2/d1) + log(n/d2)
                    if abs(s) < 1e-9:
                        print(f"     ({d1},{d2}): 和 = {s:.2e}（0——可加——）")
                    break
            else:
                continue
            break

if __name__ == "__main__":
    main()
