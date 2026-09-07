#!/usr/bin/env python3
"""
Rédei 三重符号 [p,q,r]——核心组件原型
算法（Stevenhagen arXiv:1806.06250 公式 48——）：
[p,q,r] = Π_{p点} (β, π)_p——β ∈ Q(√a) 且 N(β) = b——(·,·)_p 二次 Hilbert 符号

对素数 a=p, b=q（≡1 mod 4——(p/q)=1——）：
1. 解 norm 方程 x² − p·y² = q（连分数法——）
2. β = x + y√p——norm q
3. Hilbert 符号 (β, π)_p 对 p|c（c=r——）
"""
import math
from math import gcd

def legendre_sym(a, p):
    """Legendre 符号 (a/p)——p 奇素数"""
    v = pow(a % p, (p-1)//2, p)
    return 0 if v == 0 else (1 if v == 1 else -1)

def sqrt_mod_p(a, p):
    """解 x² ≡ a (mod p)——Tonelli-Shanks"""
    a %= p
    if a == 0:
        return 0
    if p == 2:
        return a
    if legendre_sym(a, p) != 1:
        return None
    if p % 4 == 3:
        return pow(a, (p+1)//4, p)
    # Tonelli-Shanks 通用
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

def solve_norm_eq(p, q, bound=100000):
    """解 x² − p·y² = q——用连分数法（Q(√p) 的单位/Pell——）
    简化：小范围暴力 + 连分数扩展——先暴力小 y"""
    # 暴力（小 q——y 小——）
    # x² ≡ q (mod p)——先找 x mod p——然后 x = x0 + kp——测
    x0 = sqrt_mod_p(q % p, p)
    if x0 is None:
        return None
    # x² − q = p y²——遍历 x = x0 + k·p——测 (x²−q)/p 是否平方
    for k in range(bound):
        x = x0 + k*p
        num = x*x - q
        if num < 0:
            continue
        if num % p != 0:
            continue
        y2 = num // p
        y = math.isqrt(y2)
        if y*y == y2 and y > 0:
            return (x, y)
        # 也试另一个根
        x2 = (p - x0) + k*p
        num2 = x2*x2 - q
        if num2 < 0 or num2 % p != 0:
            continue
        y22 = num2 // p
        y2v = math.isqrt(y22)
        if y2v*y2v == y22 and y2v > 0:
            return (x2, y2v)
    return None

def hilbert_symbol_p(a, b, p):
    """二次 Hilbert 符号 (a,b)_p——p 奇素数
    (a,b)_p = (-1)^{αβ·((p-1)/2)}·(a^β/b^α 的 Legendre 组合——)
    公式：a = p^α·u, b = p^β·v（u,v p-adic 单位——）
    (a,b)_p = (-1)^{αβ(p-1)/2}·(u/p)^β·(v/p)^α（对奇 p——）"""
    # 提 p-adic 估值
    aa, bb = a, b
    alpha = 0
    while aa % p == 0:
        aa //= p
        alpha += 1
    beta = 0
    while bb % p == 0:
        bb //= p
        beta += 1
    aa %= p
    bb %= p
    # 单位部分（mod p——去 p 的幂后可能仍含 p 因子——不对——已除尽——）
    # 但 a 的"单位部分"要 mod p——如果 a 是负/分数——处理整数情形
    u = aa % p
    v = bb % p
    if u == 0:
        u = 1  # 若 a 是 p 的纯幂——单位 1
    if v == 0:
        v = 1
    # (a,b)_p = (-1)^{αβ(p-1)/2} · (u/p)^β · (v/p)^α
    sign = (-1)**((alpha*beta*(p-1)//2) % 2)
    leg = (legendre_sym(u, p)**beta) * (legendre_sym(v, p)**alpha)
    return sign * leg

def main():
    # 验证：Stevenhagen 论文例子的元素
    print("Hilbert 符号验证：")
    print(f"(2, 3)_3 = {hilbert_symbol_p(2, 3, 3)}（应 -1——2 非 3 的平方 mod 3——2≡-1——(-1/3)=-1——）")
    print(f"(5, 5)_5 = {hilbert_symbol_p(5, 5, 5)}")
    
    # norm 方程验证
    print("\nnorm 方程 x²−py²=q 求解：")
    for p, q in [(5, 41), (13, 17), (5, 29)]:
        sol = solve_norm_eq(p, q)
        if sol:
            x, y = sol
            print(f"  x²−{p}y²={q}: x={x}, y={y}——检查 {x*x}−{p}*{y*y} = {x*x-p*y*y} ✓")
        else:
            print(f"  x²−{p}y²={q}: 无解（bound 内——）")
            # 检查必要条件
            leg = legendre_sym(q % p, p)
            print(f"    (q/p) = {leg}（需 1——）")

if __name__ == "__main__":
    main()
