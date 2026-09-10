#!/usr/bin/env python3
"""A5-1 修正版：归一化乘法性审计 b_m = a_m/a_1（a_1=2w）
θ^w 系数的 Dirichlet 级数有 Euler product ⟺ b_m 乘法
"""
from fractions import Fraction
from math import gcd

MMAX = 60
R = [[0]*(MMAX+1) for _ in range(MMAX+1)]
R[0][0] = 1
for k in range(1, MMAX+1):
    for m in range(k, MMAX+1):
        s = 0; j = 1
        while j*j <= m:
            s += R[k-1][m-j*j]; j += 1
        R[k][m] = s

def binom_w(w, k):
    p = Fraction(1)
    for i in range(k): p *= (Fraction(w)-i)
    for i in range(1, k+1): p /= i
    return p

def a_m(w, m):
    t = Fraction(0)
    for k in range(1, m+1):
        if R[k][m]: t += binom_w(w,k)*(2**k)*R[k][m]
    return t

def b_m(w, m):
    return a_m(w, m)/binom_w(w,1)/2      # 归一化 b_m = a_m/a_1, a_1=2w

print('=== 归一化乘法性 b_{mn} ?= b_m·b_n （互素，mn≤60）===')
print('  w      失败数/测试数   首个失败例')
for w in ['0.01','0.5','0.75','1','2','3','4','5','6','7','8','10','12']:
    fails = []; tot = 0
    for m in range(1, 34):
        for n in range(m+1, 61):
            if gcd(m,n) != 1 or m*n > MMAX: continue
            tot += 1
            if b_m(w, m)*b_m(w, n) != b_m(w, m*n):
                fails.append((m, n, b_m(w,m*n), b_m(w,m)*b_m(w,n)))
    first = ''
    if fails:
        m,n,lhs,rhs = fails[0]
        first = f'(m={m},n={n}: {float(lhs):.6g} vs {float(rhs):.6g})'
    tag = '  <== Euler product' if not fails else ''
    print(f'  {w:>5}   {len(fails):>3}/{tot:<5}   {first}{tag}')

print()
print('=== b_m 前 12 项（对照）===')
print('   m      w=0.01        w=0.5         w=1      w=2      w=4')
for m in range(1, 13):
    vals = [float(b_m(w, m)) for w in ['0.01','0.5','1','2','4']]
    print(f'  {m:>3} ' + ''.join(f'{v:>13.6f}' for v in vals))
