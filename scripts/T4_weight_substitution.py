#!/usr/bin/env python3
"""T4（判别性检验）：把权替换成【纯随机】权，看 T1/T2/T3 是否照样通过
若随机权也全通过 ⟹ Δ3≠0 是"非线性的一般现象"，不是算术结构 ⟹ T3 无判别力
同时：把 K2 写成闭式，检查其结构（是否为沿线算术值的【乘积】差）
"""
import math, random
from itertools import combinations

def rad(n):
    r = 1; m = n; d = 2
    while d*d <= m:
        if m % d == 0:
            r *= d
            while m % d == 0: m //= d
        d += 1
    if m > 1: r *= m
    return r

def matmul(X, Y):
    return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
            [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]

def make_model(rfun):
    def UA(a, b): return [[1.0, rfun(a+b)], [0.0, 1.0]]
    def UM(a, b): return [[1.0, 0.0], [rfun(a*b), 1.0]]
    def K2(a, b):
        SA = (a+b, b); SM = (a*b, b)
        PAM = matmul(UM(*SA), UA(a, b)); PMA = matmul(UA(*SM), UM(a, b))
        return [[PAM[i][j]-PMA[i][j] for j in range(2)] for i in range(2)]
    def k2s(a, b): return K2(a, b)[0][0]
    return UA, UM, K2, k2s

random.seed(12345)
_rcache = {}
def r_rand(n):
    if n not in _rcache: _rcache[n] = random.random()
    return _rcache[n]

weights = {
    'log rad(n)': lambda n: math.log(rad(n)),
    'log n':      lambda n: math.log(n),
    'Omega(n)':   None,   # 下面填
    'random':     r_rand,
}
def Omega(n):
    k = 0; m = n; d = 2
    while d*d <= m:
        while m % d == 0: m //= d; k += 1
        d += 1
    if m > 1: k += 1
    return k
weights['Omega(n)'] = lambda n: float(Omega(n))

primes = [2,3,5,7,11]
def run(name, rfun):
    UA, UM, K2, k2s = make_model(rfun)
    nz = tot = 0
    for a in range(1, 40):
        for b in range(1, 40):
            tot += 1
            if abs(k2s(a,b)) > 1e-12: nz += 1
    def f(ps):
        if not ps: return 0.0
        n = 1
        for p in ps: n *= p
        return k2s(n, 1)
    d3nz = 0; d3tot = 0
    for (p,q,s) in combinations(primes, 3):
        v = (f((p,q,s)) - f((p,q)) - f((q,s)) - f((p,s))
             + f((p,)) + f((q,)) + f((s,)))
        d3tot += 1
        if abs(v) > 1e-10: d3nz += 1
    print('  %-12s T1: %5.1f%% 非零   T3: Δ3 非零 %d/%d' % (name, 100*nz/tot, d3nz, d3tot))
    return d3nz, d3tot

print('=== T4：换权后 T1/T3 是否照样通过（含纯随机权）===')
for name, rf in weights.items():
    run(name, rf)

print()
print('=== K2 闭式检查（解析）===')
print('  Π_AM = U_M(a+b,b)·U_A(a,b) = [[1, r(a+b)], [r(b(a+b)), r(a+b)·r(b(a+b))+1]]')
print('  Π_MA = U_A(ab,b)·U_M(a,b) = [[1+r(b(a+1))r(ab), r(b(a+1))], [r(ab), 1]]')
print('  ⟹ K2 的每个分量都是【沿线算术值的乘积之差】')
print('  ⟹ 对任何非可分离权，三阶差分 Δ3 一般非零（与算术无关）')
