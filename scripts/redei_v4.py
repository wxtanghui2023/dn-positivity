#!/usr/bin/env python3
"""
Rédei 符号 [p,q,r]——完整规范化实现 v4
关键修正（自研——）：
1. 只用 z 奇解（Prop 7.3 假设 N(β) ≡ b mod 4——z 偶时 N ≡ 0 mod 4 不满足——）
2. valuation parity（s ∈ {1,2} 使 split 分量 v₂ 都偶——）
3. sign ε 使单位部分 ≡ (1,1) mod 4（split——）
4. 局部符号 = Legendre(ε·s·β mod c——)
"""
import math, sys, itertools

def v2(n):
    n = abs(n)
    if n == 0:
        return 999
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def tonelli(n, p):
    n %= p
    if n == 0:
        return 0
    if p % 4 == 3:
        return pow(n, (p+1)//4, p)
    q, s = p-1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p-1)//2, p) != p-1:
        z += 1
    m, c = s, pow(z, q, p)
    t, r = pow(n, q, p), pow(n, (q+1)//2, p)
    while t != 1:
        i, temp = 0, t
        while temp != 1:
            temp = temp*temp % p
            i += 1
        bb = pow(c, 2**(m-i-1), p)
        m, c, t, r = i, bb*bb % p, t*bb*bb % p, r*bb % p
    return r

def solve_z_odd(a, b, z_max=30, y_max=40000):
    """解 x²−ay²=bz²——z 奇——"""
    for z in range(1, z_max, 2):  # 只 z 奇
        for y in range(1, y_max):
            x2 = b*z*z + a*y*y
            x = math.isqrt(x2)
            if x*x == x2:
                return (x, y, z)
    return None

def normalize_beta(a, b, x, y, z):
    """规范化 β——返回 (eps, s) 使规范化后满足平方条件
    只适用 z 奇（N(β) ≡ b mod 4——）"""
    if z % 2 == 0:
        return None
    w1, w2 = x - y, x + y
    for s in [1, 2]:
        sw1, sw2 = s*w1, s*w2
        if sw1 == 0 or sw2 == 0:
            continue
        va, vb = v2(sw1), v2(sw2)
        if va % 2 == 0 and vb % 2 == 0:
            u1 = sw1 // (2**va)
            u2 = sw2 // (2**vb)
            if u1 % 4 == 1 and u2 % 4 == 1:
                return (1, s)
            elif u1 % 4 == 3 and u2 % 4 == 3:
                return (-1, s)
    return None

def redei_v4(a, b, c):
    """[a,b,c]——规范化版"""
    if a % 4 != 1 or b % 4 != 1 or c % 4 != 1:
        return None
    if not (legendre(a,b)==1 and legendre(b,c)==1 and legendre(c,a)==1):
        return None
    sol = solve_z_odd(a, b)
    if sol is None:
        return None
    x, y, z = sol
    norm = normalize_beta(a, b, x, y, z)
    if norm is None:
        return None
    eps, s = norm
    # 局部符号：√a mod c
    sq = tonelli(a % c, c)
    if sq is None:
        return None
    beta_c = (x + y*sq) % c
    if beta_c == 0:
        return None
    leg = legendre(beta_c, c)
    # eps·s 的修正（c-单位——）：s=1 时无——s=2 时乘 Legendre(2,c)（2 的类——）
    # eps 的修正：Legendre(eps, c)——eps ∈ {±1}
    corr = 1
    if s == 2:
        corr *= legendre(2, c)
    if eps == -1:
        corr *= legendre(-1, c)
    return leg * corr

def main():
    import numpy as np, random, time
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:400]
    random.seed(29)
    t0 = time.time()
    
    n_adm = n_multi = n_cons = n_incons = 0
    dist = {}
    for _ in range(400):
        p, q, r = random.sample(p1, 3)
        if not (legendre(p,q)==1 and legendre(q,r)==1 and legendre(r,p)==1):
            continue
        n_adm += 1
        vals, dirs = [], []
        for perm in itertools.permutations([p, q, r]):
            v = redei_v4(*perm)
            if v is not None:
                vals.append(v)
                dirs.append(perm)
        if len(vals) >= 2:
            n_multi += 1
            if len(set(vals)) == 1:
                n_cons += 1
                dist[vals[0]] = dist.get(vals[0], 0) + 1
            else:
                n_incons += 1
                if n_incons <= 3:
                    print(f"❌ 不一致: ({p},{q},{r})——{list(zip(dirs, vals))}")
    
    print(f"\nadmissible: {n_adm}——多方向: {n_multi}——一致: {n_cons}——不一致: {n_incons}")
    print(f"耗时: {time.time()-t0:.1f}s")
    print("✅ 对称性通过！" if n_incons == 0 and n_multi > 0 else "❌ inconsistency")
    print(f"分布: {dist}")

if __name__ == "__main__":
    main()
