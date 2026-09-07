#!/usr/bin/env python3
"""
Rédei 符号 [p,q,r]——路径 A v2（sympy diophantine 求解 norm 方程——）
验证：多方向对称性一致性 + 符号分布
"""
import math, sys, itertools
sys.path.insert(0, 'scripts')
import sympy as sp
from sympy.solvers.diophantine import diophantine
from sympy.abc import x, y

def solve_norm_sympy(D, N):
    """解 x² − D y² = N——sympy——取最小正解"""
    try:
        sols = diophantine(x**2 - D*y**2 - N)
    except Exception:
        return None
    best = None
    for sx, sy in sols:
        if sx.is_integer and sy.is_integer:
            sx_i, sy_i = int(sx), int(sy)
            if sx_i > 0 and sy_i > 0 and sx_i**2 - D*sy_i**2 == N:
                if best is None or sy_i < best[1]:
                    best = (sx_i, sy_i)
    return best

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

def redei_dir(a, b, c):
    """[a,b,c]——x²−ay²=b——β=x+y√a——Q(√a) 中 c 上方素点"""
    if a % 4 != 1 or b % 4 != 1 or c % 4 != 1:
        return None
    if not (legendre_sym(a,b)==1 and legendre_sym(b,c)==1 and legendre_sym(c,a)==1):
        return None
    sol = solve_norm_sympy(a, b)
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

if __name__ == "__main__":
    import numpy as np, random, time
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:600]
    random.seed(11)
    
    n_adm = 0
    n_multi = 0
    n_consistent = 0
    n_inconsistent = 0
    dist = {}
    t0 = time.time()
    
    for _ in range(1500):
        p, q, r = random.sample(p1, 3)
        if not (legendre_sym(p,q)==1 and legendre_sym(q,r)==1 and legendre_sym(r,p)==1):
            continue
        n_adm += 1
        vals = []
        dirs = []
        for perm in itertools.permutations([p, q, r]):
            v = redei_dir(*perm)
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
    
    print(f"\nadmissible: {n_adm}——多方向可算: {n_multi}——一致: {n_consistent}——不一致: {n_inconsistent}")
    print(f"耗时: {time.time()-t0:.1f}s")
    if n_inconsistent == 0 and n_multi > 0:
        print("✅ 对称性通过！")
    else:
        print("❌ 有 inconsistency")
    print(f"符号分布: {dist}——比例: {dist.get(1,0)/max(1,sum(dist.values())):.3f} +1")
