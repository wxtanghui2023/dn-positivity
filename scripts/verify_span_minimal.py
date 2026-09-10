#!/usr/bin/env python3
"""最小重算：ω_p^rad 是否落在 span{1, 1_{ua+vb≡0 mod p}} 内
（p=3, p=5；精确有理高斯消元）"""
from fractions import Fraction as F
from itertools import product

def omega_p_rad(a, b, p):
    def rad(n):
        r = 1; m = n; d = 2
        while d*d <= m:
            if m % d == 0:
                r *= d
                while m % d == 0: m //= d
            d += 1
        if m > 1: r *= m
        return r
    c = a + b
    u = rad(c); u2 = rad(b + c)
    S = (a, b, c); SA = (b, c, b + c)
    SM = (u*a, u*b, u*c); SAM = (u2*b, u2*c, u2*(b + c))
    tot = 0
    for T, sg in [(SAM, +1), (S, +1), (SA, -1), (SM, -1)]:
        for comp in T:
            if comp % p == 0: tot += sg
    return tot

def rank(M):
    M = [[F(x) for x in row] for row in M]
    rows = len(M); cols = len(M[0]) if rows else 0
    r = 0
    for c in range(cols):
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
                M[i] = [M[i][k]-f*M[r][k] for k in range(cols)]
        r += 1
    return r

for p in [3, 5]:
    # 候选：常数 + 每个方向的线性式指示（方向归一化，去重）
    keys = set()
    for (u, v) in product(range(p), repeat=2):
        if (u, v) == (0, 0): continue
        if u != 0:
            inv = pow(u, p-2, p)
            keys.add((1, (v*inv) % p))
        else:
            keys.add((0, 1))
    cols = [[1]*(p*p)]
    for (u, v) in sorted(keys):
        cols.append([1 if (u*a+v*b) % p == 0 else 0 for a in range(p) for b in range(p)])
    tgt = [omega_p_rad(a, b, p) for a in range(p) for b in range(p)]
    M = [[cols[j][i] for j in range(len(cols))] for i in range(p*p)]
    r0 = rank(M)
    M2 = [[cols[j][i] for j in range(len(cols))] + [tgt[i]] for i in range(p*p)]
    r1 = rank(M2)
    print('p=%d:  ω_p^rad 值表（a 外层, b 内层）= %s' % (p, tgt))
    print('      rank(候选) = %d,  rank(候选+目标) = %d  ⟹ 目标在 span 内 ? %s'
          % (r0, r1, '是 ✓' if r1 == r0 else '【否】'))
    print('      （候选数 %d, F_p² 维数 %d）' % (len(cols), p*p))
