#!/usr/bin/env python3
"""
Prop 7.3(1) 严格实现——O_a/4O_a 有限环运算
ω = (1+√a)/2——β = x+y√a = (x-y) + 2y·ω——坐标 (u,v) = (x-y, 2y) 对基 (1, ω)
ω² = ω - c——c = (1-a)/4（整数——a ≡ 1 mod 4）

乘法（模 4）：(u+vω)(u'+v'ω) = (uu' - c·vv') + (uv'+u'v+vv')ω
平方：(u+vω)² = (u² - c·v²) + (2uv+v²)ω

算法：对 s ∈ {1,2} × ε ∈ {±1}——γ = ε·s·β——
如果 γ 是 2-单位 且 γ ∈ (O/4O)×²——(s,ε) 唯一——t = ε·s
"""
import math

def c_val(a):
    """c = (1-a)/4 mod 4——整数"""
    return ((1 - a) // 4) % 4

def mul_mod4(a, u1, v1, u2, v2):
    """(u1+v1ω)(u2+v2ω) mod 4——返回 (u,v)"""
    c = c_val(a)
    u = (u1*u2 - c*v1*v2) % 4
    v = (u1*v2 + u2*v1 + v1*v2) % 4
    return u, v

def square_mod4(a, u, v):
    """(u+vω)² mod 4"""
    return mul_mod4(a, u, v, u, v)

def is_unit_mod2(a, u, v):
    """γ = u+vω（模 2 坐标——）是否 2-单位
    a ≡ 1 mod 8: split——F₂×F₂——φ₁: ω→0（值 u——）φ₂: ω→1（值 u+v——）
    a ≡ 5 mod 8: inert——F₄——(u,v) ≠ (0,0)"""
    u %= 2
    v %= 2
    if a % 8 == 1:
        # split——需两个分量都非零
        return (u % 2 == 1) and ((u + v) % 2 == 1)
    else:
        # inert——F₄——非零即可
        return not (u == 0 and v == 0)

def is_square_mod4O(a, u, v):
    """γ = u+vω ∈ (O/4O)× 是否平方——穷举平方根 (p,q) mod 4"""
    u %= 4
    v %= 4
    # 先检查单位（模 2——）
    if not is_unit_mod2(a, u, v):
        return False
    for p in range(4):
        for q in range(4):
            # 平方根自身也须单位——但先穷举全部
            u2, v2 = square_mod4(a, p, q)
            if u2 == u and v2 == v:
                return True
    return False

def find_tmin_strict(a, x, y):
    """Prop 7.3(1)：唯一 t ∈ {±1, ±2}——(s ∈ {1,2}) × (ε ∈ {±1})
    β = x+y√a——ω 坐标：(u₀, v₀) = (x-y, 2y)
    对 s ∈ {1,2}——γ = s·β——坐标 (s·u₀, s·v₀)
    对 ε——εγ——坐标 (ε·s·u₀, ε·s·v₀)——模 4
    唯一 (s,ε) 使 γ 单位且平方——返回 t = ε·s"""
    u0 = (x - y) % 4
    v0 = (2 * y) % 4
    found = []
    for s in [1, 2]:
        for eps in [1, -1]:
            u = (eps * s * u0) % 4
            v = (eps * s * v0) % 4
            if is_square_mod4O(a, u, v):
                found.append(eps * s)
    return found

def find_tmin_with_unit_first(a, x, y):
    """两步：先 valuation 归一（s ∈ {1,2} 使单位——）再 sign（ε 使平方——）
    返回 t = ε·s"""
    u0 = (x - y) % 4
    v0 = (2 * y) % 4
    # Step 1: 找 s 使 sβ 单位（模 2——）
    s_found = None
    for s in [1, 2]:
        if is_unit_mod2(a, (s*u0) % 2, (s*v0) % 2):
            s_found = s
            break
    if s_found is None:
        return None
    # Step 2: sign ε 使 ε·s·β 模 4O 平方
    for eps in [1, -1]:
        u = (eps * s_found * u0) % 4
        v = (eps * s_found * v0) % 4
        if is_square_mod4O(a, u, v):
            return eps * s_found
    return None

def legendre_sym(a, p):
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p-1)//2, p)
    return 1 if v == 1 else -1

def main():
    import numpy as np, random
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:300]
    random.seed(23)
    
    n_found = 0
    n_multi = 0
    n_none = 0
    t_dist = {}
    for _ in range(3000):
        a, b = random.sample(p1, 2)
        if legendre_sym(a, b) != 1:
            continue
        sol = None
        for z in range(1, 15):
            for y in range(1, 2500):
                x2 = b*z*z + a*y*y
                x = math.isqrt(x2)
                if x*x == x2:
                    sol = (x, y, z)
                    break
            if sol:
                break
        if sol is None:
            continue
        x, y, z = sol
        g = math.gcd(math.gcd(x, y), z)
        x, y, z = x//g, y//g, z//g
        # 测试严格版
        ts = find_tmin_strict(a, x, y)
        if len(ts) == 1:
            n_found += 1
            t_dist[ts[0]] = t_dist.get(ts[0], 0) + 1
        elif len(ts) > 1:
            n_multi += 1
            if n_multi <= 3:
                print(f"  多 t: (a,b)=({a},{b}) z={z}——β=({x},{y})——t∈{ts}——a mod 8 = {a%8}")
        else:
            n_none += 1
        if n_found + n_multi + n_none >= 40:
            break
    
    print(f"严格版: 唯一 {n_found}——多 {n_multi}——无 {n_none}")
    print(f"t 分布: {t_dist}")
    
    # 关键测试：多解样本 (3457, 2081, 3361)
    print("\n" + "="*60)
    print("关键多解测试：(a,b) = (3457, 2081)——c = 3361")
    print("="*60)
    beta1 = (49449, 841, 8)
    beta2 = (5901, 100, 11)
    for name, (x, y, z) in [("β₁", beta1), ("β₂", beta2)]:
        g = math.gcd(math.gcd(x, y), z)
        xg, yg, zg = x//g, y//g, z//g
        ts = find_tmin_strict(3457, xg, yg)
        print(f"  {name} = ({x},{y},{z})——primitive ({xg},{yg},{zg})——t = {ts}")

if __name__ == "__main__":
    main()
