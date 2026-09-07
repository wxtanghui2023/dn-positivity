#!/usr/bin/env python3
"""
Rédei 符号 [p,q,r]——路径 A v3（正确 norm：x²−py²=qz²——圆锥曲线——）
β = x+y√p——N(β) = qz²——β 的范数类 = q（mod 平方——）

[p,q,r] 的局部符号计算：
- β = x+y√p——N(β) = qz²
- r 在 Q(√p) 分裂（(p/r)=1——）——素点对应 √p ≡ ±s (mod r)
- 局部符号 (β, π) = Legendre(β·z^{-1} 类——) 需要小心（β 的范数含 z²——单位部分——）

注意：范数类 = q 才重要——β 可乘任意单位——局部符号应只依赖范数类？
验证：不同解 (x,y,z) 应给相同 [p,q,r]（规范独立性——）
"""
import math, sys, itertools
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

def solve_conic_small(p, q, z_max=50, y_max=20000):
    """解 x²−py²=qz²——小搜索"""
    for z in range(1, z_max):
        qz2 = q*z*z
        for y in range(1, y_max):
            x2 = qz2 + p*y*y
            x = math.isqrt(x2)
            if x*x == x2:
                return (x, y, z)
    return None

def redei_dir(a, b, c):
    """[a,b,c]——用 β = x+y√a——N(β)=bz²——在 Q(√a) 的 c-素点算局部符号
    关键：β 与 β·(任意平方) 给相同符号——局部符号 = (β/p) 类
    但 β 的范数 = bz²——β 的'单位化'——除以 z？——β/z 范数 b？——β/z ∈ Q(√a)？——z 有理——β/z = x/z + (y/z)√a——是的！——N(β/z) = N(β)/z² = b——所以 β' = β/z 是范数恰 b 的元素！
    但 β' 可能不在代数整数环（x/z 分数——）——局部符号仍可算（β' 模 c 的 Legendre——只要分母与 c 互素——）
    """
    if a % 4 != 1 or b % 4 != 1 or c % 4 != 1:
        return None
    if not (legendre_sym(a,b)==1 and legendre_sym(b,c)==1 and legendre_sym(c,a)==1):
        return None
    sol = solve_conic_small(a, b)
    if sol is None:
        return None
    x, y, z = sol
    # β' = β/z = x/z + (y/z)√a——模 c 的值：需 z 模 c 可逆（c 素数——z < c 或 gcd(z,c)=1——）
    if z % c == 0:
        return None
    z_inv = pow(z % c, c-2, c)
    s = sqrt_mod_p(a % c, c)
    if s is None:
        return None
    # β' mod c（素点对应 √a ≡ s——）：
    beta_mod = ((x % c) + (y % c) * s) % c
    beta_mod = (beta_mod * z_inv) % c
    if beta_mod == 0:
        return None
    return legendre_sym(beta_mod, c)

if __name__ == "__main__":
    import numpy as np, random, time
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:400]
    random.seed(5)
    
    n_adm = n_multi = n_consistent = n_inconsistent = 0
    dist = {}
    t0 = time.time()
    
    for _ in range(400):
        p, q, r = random.sample(p1, 3)
        if not (legendre_sym(p,q)==1 and legendre_sym(q,r)==1 and legendre_sym(r,p)==1):
            continue
        n_adm += 1
        vals, dirs = [], []
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
    
    print(f"\nadmissible: {n_adm}——多方向: {n_multi}——一致: {n_consistent}——不一致: {n_inconsistent}")
    print(f"耗时: {time.time()-t0:.1f}s")
    print("✅ 对称性通过！" if n_inconsistent == 0 and n_multi > 0 else "❌ inconsistency")
    print(f"分布: {dist}")
