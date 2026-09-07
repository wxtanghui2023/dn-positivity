#!/usr/bin/env python3
"""
Rédei 三重符号 [p,q,r]——路径 A（Stevenhagen 公式 46-48——最小局部实现）
素数 admissible 情形：p,q,r ≡ 1 mod 4——两两互余

算法：
1. norm 方程 x²−py² = q → β = x+y√p（N(β)=q——）
2. r 在 Q(√p) 分裂（(p/r)=1——）→ √p ≡ ±s mod r
3. [p,q,r] = Π (β, π)_p——p 遍历 Q(√p) 中 r 上方的素点
   对度数 1 素点 p_i（√p ≡ s_i）——(β, π) = Legendre(β mod p_i, r)（β 单位时——）

验证：六置换对称性 [p,q,r] = [p,r,q] = ...——不同 norm 解独立性
"""
import math
from math import gcd

def legendre_sym(a, p):
    """Legendre 符号 (a/p)——p 奇素数——a 任意整数"""
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p-1)//2, p)
    return 1 if v == 1 else -1

def sqrt_mod_p(a, p):
    """Tonelli-Shanks 解 x² ≡ a (mod p)"""
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

def solve_norm_eq(p, q, bound=200000):
    """解 x² − p·y² = q（q 素数——p 素数 ≡1 mod 4——(q/p)=1——）
    用连分数法（Q(√p) 的单位群——）加速——先暴力小——再 Pell 扩展"""
    x0 = sqrt_mod_p(q % p, p)
    if x0 is None:
        return None
    # x² − q = p y²——x = x0 + k·p——测 (x²−q)/p 是否平方
    # 改进：直接解 Pell 型——用模 p 的根做种子——暴力 k 到 bound
    for k in range(bound):
        for sign in [1, -1]:
            x = (x0 if sign == 1 else p - x0) + k*p
            num = x*x - q
            if num < 0:
                continue
            if num % p != 0:
                continue
            y2 = num // p
            y = math.isqrt(y2)
            if y*y == y2 and y > 0:
                return (x, y)
    return None

def redei_symbol(p, q, r, verbose=False):
    """Rédei 符号 [p,q,r]——p,q,r ≡1 mod 4 素数——两两互余
    返回 +1 或 -1（或 None 如果条件不满足——）"""
    # 检查条件
    if p % 4 != 1 or q % 4 != 1 or r % 4 != 1:
        return None
    if legendre_sym(p, q) != 1 or legendre_sym(q, r) != 1 or legendre_sym(r, p) != 1:
        return None
    # norm 方程：x² − p y² = q（β = x+y√p 在 Q(√p)——N(β) = q——）
    sol = solve_norm_eq(p, q)
    if sol is None:
        # 尝试反方向（q 的 norm 表示可能比 p 的容易——）
        return None
    x, y = sol
    # r 在 Q(√p) 分裂——s = √p mod r
    s = sqrt_mod_p(p % r, r)
    if s is None:
        return None
    # β mod 两个素点：x + ys 和 x − ys（模 r——）
    b1 = (x + y*s) % r
    b2 = (x - y*s) % r
    # 局部符号：(β, π)_p_i——β 单位时 = Legendre(β mod p_i, r)
    # 若 β ≡ 0 mod p_i——该素点分歧——(45) 选未分歧的——需要特殊处理
    if b1 == 0 and b2 == 0:
        return None  # 两个都分歧？——不该发生（admissible——）
    # 符号乘积（两个素点——或单点处理——用两种方式——返回两种供验证）
    leg1 = legendre_sym(b1, r) if b1 != 0 else None
    leg2 = legendre_sym(b2, r) if b2 != 0 else None
    if verbose:
        print(f"  p={p}, q={q}, r={r}: x={x}, y={y}——s={s}——b1={b1}, b2={b2}——leg1={leg1}, leg2={leg2}")
    # 若一点分歧（leg None——）用另一点——若两点都单位——乘积？
    if leg1 is not None and leg2 is not None:
        return leg1 * leg2  # 乘积（待验证——可能应取单点——）
    elif leg1 is not None:
        return leg1
    elif leg2 is not None:
        return leg2
    return None

def main():
    # 测试：找一些 admissible 三元组并检查对称性
    import numpy as np
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    p1 = [int(p) for p in primes if p % 4 == 1 and p > 5][:500]
    print(f"≡1 mod 4 素数（前 500——）: 最大 {p1[-1]}")
    
    import random
    random.seed(42)
    n_tested = 0
    n_valid = 0
    sym_ok = 0
    sym_fail = 0
    sym_na = 0
    
    for _ in range(2000):
        p, q, r = random.sample(p1, 3)
        if not (legendre_sym(p,q)==1 and legendre_sym(q,r)==1 and legendre_sym(r,p)==1):
            continue
        n_tested += 1
        # 算所有六种顺序（理论上相同——但 norm 方程方向不同——）
        v1 = redei_symbol(p, q, r)
        if v1 is None:
            continue
        n_valid += 1
        # 对称性测试：算 [p,r,q]（用 norm p→r——）
        v2 = redei_symbol(p, r, q)
        if v2 is None:
            sym_na += 1
            continue
        if v1 == v2:
            sym_ok += 1
        else:
            sym_fail += 1
            if sym_fail <= 3:
                print(f"  不对称！[p,q,r]={v1} vs [p,r,q]={v2}——(p,q,r)=({p},{q},{r})")
    
    print(f"\n测试: {n_tested} admissible——{n_valid} 可算——对称性: {sym_ok} OK——{sym_fail} FAIL——{sym_na} 不可比")
    if sym_fail == 0 and sym_ok > 0:
        print("→ 对称性初步通过（[p,q,r] = [p,r,q]——）")
    elif sym_fail > 0:
        print("→ 对称性失败——实现需修正！")
    
    # 显示几个具体值
    print("\n具体值示例：")
    shown = 0
    for _ in range(500):
        p, q, r = random.sample(p1, 3)
        if not (legendre_sym(p,q)==1 and legendre_sym(q,r)==1 and legendre_sym(r,p)==1):
            continue
        v = redei_symbol(p, q, r, verbose=True)
        if v is not None and shown < 3:
            shown += 1
        if shown >= 3:
            break

if __name__ == "__main__":
    main()
