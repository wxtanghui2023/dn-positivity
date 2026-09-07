#!/usr/bin/env python3
"""
Test B：同一 (a,b)——不同 norm 解 β₁, β₂——符号是否依赖解的选择？
如果依赖——需要 minimal-at-2 normalization（t ∈ {±1,±2}——）
"""
import math, sys
sys.path.insert(0, 'scripts')

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

def solve_conic_multi(a, b, n_sols=3, z_max=40, y_max=30000):
    """找多个解 x²−ay²=bz²"""
    sols = []
    for z in range(1, z_max):
        qz2 = b*z*z
        for y in range(1, y_max):
            x2 = qz2 + a*y*y
            x = math.isqrt(x2)
            if x*x == x2:
                sols.append((x, y, z))
                if len(sols) >= n_sols:
                    return sols
    return sols

def raw_symbol(a, b, c, sol):
    """raw [a,b,c]——用给定解 β=x+y√a（未规范化——）"""
    x, y, z = sol
    if z % c == 0:
        return None
    z_inv = pow(z % c, c-2, c)
    s = sqrt_mod_p(a % c, c)
    if s is None:
        return None
    beta_mod = ((x % c) + (y % c) * s) % c
    beta_mod = (beta_mod * z_inv) % c
    if beta_mod == 0:
        return None
    return legendre_sym(beta_mod, c)

def main():
    import numpy as np, random
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:600]
    random.seed(13)
    
    n_tested = 0
    n_multisol = 0
    n_same = 0
    n_diff = 0
    print("Test B：同一 (a,b,c)——不同解 β 的 raw 符号")
    for _ in range(3000):
        a, b, c = random.sample(p1, 3)
        if not (legendre_sym(a,b)==1 and legendre_sym(b,c)==1 and legendre_sym(c,a)==1):
            continue
        n_tested += 1
        sols = solve_conic_multi(a, b, n_sols=2)
        if len(sols) < 2:
            continue
        n_multisol += 1
        v1 = raw_symbol(a, b, c, sols[0])
        v2 = raw_symbol(a, b, c, sols[1])
        if v1 is None or v2 is None:
            continue
        if v1 == v2:
            n_same += 1
        else:
            n_diff += 1
            if n_diff <= 3:
                print(f"  ❌ 解依赖: (a,b,c)=({a},{b},{c})——β₁={sols[0]} 给 {v1}——β₂={sols[1]} 给 {v2}")
        if n_tested >= 50:
            break
    
    print(f"\nadmissible: {n_tested}——多解: {n_multisol}——符号相同: {n_same}——不同: {n_diff}")
    if n_diff == 0:
        print("→ raw 符号与解无关（不需要 normalization——？——或解恰好在同 twist 类——）")
    else:
        print("→ raw 符号依赖解——需要 minimal-at-2 normalization——确认唐先生诊断")

if __name__ == "__main__":
    main()
