#!/usr/bin/env python3
"""
Prop 7.3(1) 正确实现 v2——"2-unit up to squares"版
split（a ≡ 1 mod 8）：E⊗Q₂ ≅ Q₂×Q₂——投影 φ₁(x+yω) = x, φ₂ = x+y
β = x+y√a = (x−y) + 2yω——分量 w₁ = x−y（φ₁ 相关——注意 2yω 的 φ₁ 投影——）
等等——β = (x−y) + 2y·ω——φ₁(β) = (x−y) + 2y·φ₁(ω)——φ₁(ω) = 0——所以 φ₁(β) = x−y？
——不对——φ₁: ω→0——β = (x−y)+2yω——φ₁(β) = x−y + 0 = x−y——✓
φ₂: ω→1——φ₂(β) = x−y+2y = x+y——✓

类单位化：对 t ∈ {±1,±2}——分量 t(x−y), t(x+y)——v₂ 都偶 ⟹ 除 2^v 到 unit——测 mod 4
sign ε ∈ {±1} 同时翻转——需要 εu₁ ≡ εu₂ ≡ 1 mod 4
"""
import math

def v2(n):
    n = abs(n)
    if n == 0:
        return 999  # 0 的 valuation——大
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k

def strip_2(n):
    """去掉 2 的幂——返回奇数部分和指数"""
    k = v2(n)
    return n // (2**k), k

def find_t_split(a, x, y):
    """split 情形（a ≡ 1 mod 8——）——找唯一 t ∈ {±1, ±2}
    分量 w₁ = x−y——w₂ = x+y
    t 使 (v₂(tw₁), v₂(tw₂)) 都偶——然后 unit 部分测 mod 4 平方（sign 可调——）"""
    w1 = x - y
    w2 = x + y
    found = []
    for t in [1, -1, 2, -2]:
        tw1, tw2 = t*w1, t*w2
        if tw1 == 0 or tw2 == 0:
            continue
        v1, v2_ = v2(tw1), v2(tw2)
        if v1 % 2 == 0 and v2_ % 2 == 0:
            # unit 部分（去 2 幂——）
            u1 = tw1 // (2**v1)
            u2 = tw2 // (2**v2)
            # sign ε 同时翻转——需要 ∃ε ∈ {±1}: εu1 ≡ εu2 ≡ 1 mod 4
            # εu ≡ 1 mod 4 ⟺ u ≡ ε mod 4（ε = ±1——）
            # 需要 u1 ≡ u2 (mod 4) 且 ∈ {1, 3}
            u1m4 = u1 % 4
            u2m4 = u2 % 4
            if u1m4 == u2m4 and u1m4 in (1, 3):
                # ε = u1m4（1 或 3≡−1——ε=−1 当 u≡3——）
                found.append(t)
    return found

def find_t_inert(a, x, y):
    """inert（a ≡ 5 mod 8——）——O/2O = F₄——单素点
    v_q(β)——f=2——v₂(Nβ) = 2·v_q(β)——v_q(β) = v₂(Nβ)/2 = v₂(z)
    单位化：t 使 v_q 偶——除——然后 F₄ 的平方（全——）——但模 4 的平方是 O/4O 的——"""
    # N(β) = x²−ay²——v_q(β) = v₂(Nβ)/2
    N = x*x - a*y*y
    vN = v2(N)
    if vN % 2 != 0:
        return []  # 理论不该（N = bz²——vN = 2v₂(z) 偶——）
    vq = vN // 2
    found = []
    for t in [1, -1, 2, -2]:
        # tβ 的 v_q = vq + v₂(t)（v₂(t) = 0 或 1——t=±2 时——）
        tv = vq + v2(t)
        if tv % 2 != 0:
            continue
        # 除 2^tv（在 O 中除以 2^tv = 除 π^{2tv}？——f=2——2 = π²·u——）
        # 简化：直接用 O/4O 的严格平方测试——需要 ω 坐标的模 4 表示
        # ω 坐标 (u0, v0) = (x−y, 2y)——tβ 的坐标 = (t(x−y), 2ty)
        # 除以 2^tv（在 O/4O 层面——乘 2 的逆元不存在（2 非单位）——）
        # 用规范化的 β' = tβ/2^tv——坐标 (t(x−y)/2^tv, 2ty/2^tv)——需要整除
        tx, ty = t*(x-y), 2*t*y
        if tx % (2**tv) == 0 and ty % (2**tv) == 0:
            ux, uy = tx // (2**tv), ty // (2**tv)
            # 现在 (ux, uy) 是 unit（模 2 非零——inert——）
            # 测 ±(ux+uy·ω) 是否 O/4O 平方（用严格乘法——）
            for eps in [1, -1]:
                if is_square_mod4O_inert(a, (eps*ux) % 4, (eps*uy) % 4):
                    found.append(eps * (2 if t in (2, -2) else 1) * (1 if t > 0 else -1))
                    break
    return found

def c_val(a):
    return ((1 - a) // 4) % 4

def mul_mod4(a, u1, v1, u2, v2):
    c = c_val(a)
    u = (u1*u2 - c*v1*v2) % 4
    v = (u1*v2 + u2*v1 + v1*v2) % 4
    return u, v

def is_square_mod4O_inert(a, u, v):
    """(O/4O) 平方测试（inert——）——穷举平方根"""
    u %= 4
    v %= 4
    for p in range(4):
        for q in range(4):
            u2, v2 = mul_mod4(a, p, q, p, q)
            if u2 == u and v2 == v:
                return True
    return False

def find_tmin_v2(a, x, y):
    """统一入口——按 a mod 8 分支"""
    if a % 8 == 1:
        return find_t_split(a, x, y)
    else:
        return find_t_inert(a, x, y)

if __name__ == "__main__":
    # 关键测试：β₁ 与 β₂
    print("="*60)
    print("关键多解测试 (a,b) = (3457, 2081)——a ≡ 1 mod 8（split——）")
    print("="*60)
    # β₁ = (49449, 841)——z=8——β₂ = (5901, 100)——z=11
    for name, (x, y) in [("β₁", (49449, 841)), ("β₂", (5901, 100))]:
        ts = find_tmin_v2(3457, x, y)
        print(f"  {name}: (x,y)=({x},{y})——t = {ts}")
        w1, w2 = x-y, x+y
        print(f"    分量 w₁={w1} (v₂={v2(w1)})——w₂={w2} (v₂={v2(w2)})——parity ({(v2(w1))%2},{(v2(w2))%2})")
