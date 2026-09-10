#!/usr/bin/env python3
"""复核 Tang 的拦截 + 建立严格版定理的适用条件
(1) 验证反例：rad(c) mod p 不是 c mod p 的函数
(2) 检验实际 ω_p^rad 是否落在 span{1, 1_{ua+vb≡0}} 内
    —— 若否，则"ω_p = Σ c_j 1_{p|ℓ_j}"这一假设对 radical 型【过强】，
       必须退到"ω_p 是 (a,b) mod p 的函数"这一更一般的（仍足够）形式
"""
from fractions import Fraction as F
from itertools import product

def rad_small(n):
    r = 1; m = n; d = 2
    while d*d <= m:
        if m % d == 0:
            r *= d
            while m % d == 0: m //= d
        d += 1
    if m > 1: r *= m
    return r

print('=== (1) 反例验证：rad(c) mod p 不是 c mod p 的函数 ===')
for (c1, c2, p) in [(10, 25, 3), (10, 25, 5), (6, 15, 7)]:
    print('  c=%d, c\'=%d, p=%d:  c≡c\' (mod p)? %s |  rad(c)=%d≡%d,  rad(c\')=%d≡%d  ⟹ %s'
          % (c1, c2, p, c1 % p == c2 % p, rad_small(c1), rad_small(c1) % p,
             rad_small(c2), rad_small(c2) % p,
             '反例成立 ✗' if (c1 % p == c2 % p and rad_small(c1) % p != rad_small(c2) % p) else '无反例'))

def omega_p_rad(a, b, p):
    c = a + b
    u = rad_small(c); u2 = rad_small(b + c)
    S = (a, b, c); SA = (b, c, b + c)
    SM = (u*a, u*b, u*c); SAM = (u2*b, u2*c, u2*(b + c))
    tot = 0
    for T, sg in [(SAM, +1), (S, +1), (SA, -1), (SM, -1)]:
        for comp in T:
            if comp % p == 0: tot += sg
    return tot

def omega_p_pow(a, b, p):
    c = a + b
    u = rad_small(c); u2 = rad_small(b + c)
    S = (a, b, c); SA = (b, c, b + c)
    SM = (u*a, u*b, u*c); SAM = (u2*b, u2*c, u2*(b + c))
    def vp(n):
        k = 0
        while n % p == 0: n //= p; k += 1
        return k
    tot = 0
    for T, sg in [(SAM, +1), (S, +1), (SA, -1), (SM, -1)]:
        for comp in T:
            tot += sg * vp(comp)
    return tot

def in_span(target, cols):
    """精确有理高斯消元：判断 target 是否在 cols 的张成中"""
    rows = len(target); n = len(cols) + 1
    M = [[F(cols[j][i]) for j in range(len(cols))] + [F(target[i])] for i in range(rows)]
    r = 0
    for c in range(len(cols)):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x/pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][k] - f*M[r][k] for k in range(n)]
        r += 1
    for i in range(r, rows):
        if all(M[i][j] == 0 for j in range(len(cols))) and M[i][n-1] != 0:
            return False
    return True

print()
print('=== (2) 实际 ω_p 是否落在 span{1, 1_{ua+vb≡0 (mod p)}} 内 ===')
for p in [2, 3, 5]:
    # 候选列：常数 1 + 每个方向的线性式指示（归一化：首非零系数=1）
    dirs = [(u, v) for u, v in product(range(p), repeat=2) if (u, v) != (0, 0)]
    norm = {}
    for (u, v) in dirs:
        if u != 0:
            inv = pow(u, p-2, p)
            key = (1, (v*inv) % p)
        else:
            key = (0, 1)
        if key not in norm: norm[key] = (key[0], key[1])
    cands = []
    cands.append([1]*(p*p))                     # 常数
    for (u, v) in norm.values():
        cands.append([1 if (u*a + v*b) % p == 0 else 0 for a in range(p) for b in range(p)])
    for name, fn in [('radical型', omega_p_rad), ('幂型', omega_p_pow)]:
        tgt = [fn(a, b, p) for a in range(p) for b in range(p)]
        ok = in_span(tgt, cands)
        print('  p=%d  %s: ω_p 值表 = %s' % (p, name, tgt))
        print('          落在 span{1, 1_{ℓ≡0}} 内 ? %s   （候选维数 %d vs F_p² 维数 %d）'
              % ('是' if ok else '【否】', len(cands), p*p))
