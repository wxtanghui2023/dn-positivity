#!/usr/bin/env python3
"""步骤二（telescoping）的独立数值验证
命题：幂型权 W=abc 时 ω_p = 3(1_{p|b+c} − 1_{p|c})
检验混合权 W = rad(abc)/(abc) 时 ω_p^mix = ω_p^rad + 3(1_{p|c} − 1_{p|b+c})
（若成立，则定理对混合权同样成立 ⟹ 允许类描述正确）
"""
def v_p(n, p):
    k = 0
    while n and n % p == 0:
        n //= p; k += 1
    return k

def rad_small(n):
    r = 1; m = n; d = 2
    while d*d <= m:
        if m % d == 0:
            r *= d
            while m % d == 0: m //= d
        d += 1
    if m > 1: r *= m
    return r

def four_states(a, b):
    c = a + b
    u = rad_small(c); u2 = rad_small(b + c)
    return dict(S=(a,b,c), SA=(b,c,b+c), SM=(u*a,u*b,u*c), SAM=(u2*b,u2*c,u2*(b+c)))

def w_rad(T, p):      # radical 型：log(rad a rad b rad c) 的 p 系数 = 整除指示之和
    return sum(1 for x in T if x % p == 0)

def w_pow(T, p):      # 幂型：v_p(a b c)
    return sum(v_p(x, p) for x in T)

def w_mix(T, p):      # 混合 W = rad(abc)/(abc)
    return w_rad(T, p) - w_pow(T, p)

def omega(fn, a, b, p):
    T = four_states(a, b)
    return fn(T['SAM'],p) + fn(T['S'],p) - fn(T['SA'],p) - fn(T['SM'],p)

N = 300
for p in [2,3,5]:
    bad_pow = bad_mix = 0; tested = 0
    for a in range(1, N):
        for b in range(a, N-a+1):
            tested += 1
            c = a + b
            pred_pow = 3*((1 if (b+c) % p == 0 else 0) - (1 if c % p == 0 else 0))
            if omega(w_pow, a, b, p) != pred_pow: bad_pow += 1
            pred_mix = (omega(w_rad,a,b,p) + 3*((1 if c%p==0 else 0) - (1 if (b+c)%p==0 else 0)))
            if omega(w_mix, a, b, p) != pred_mix: bad_mix += 1
    print('p=%d:  样本 %d   telescoping 反例 %d   混合权反例 %d' % (p, tested, bad_pow, bad_mix))
print()
print('若反例为 0：步骤二成立；且混合权同属允许类 ⟹ 定理适用范围描述正确')
