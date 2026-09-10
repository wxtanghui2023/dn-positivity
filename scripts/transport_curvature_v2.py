#!/usr/bin/env python3
"""v2：Ω 的精确素数分解 + C1 可积性 + C2 跨素数耦合 + C3 多步累计曲率"""
import math, statistics
from collections import defaultdict

LIM = 10**6
rad = [1]*(LIM+1); rad[0] = 0
sieve = bytearray([1])*(LIM+1)
primes = []
for p in range(2, LIM+1):
    if sieve[p]:
        primes.append(p)
        for m in range(p, LIM+1, p):
            sieve[m] = 0
            rad[m] *= p

def divs(n):
    """n 的不同素因子集合（n 用筛内 rad 分解）"""
    s = set()
    if n <= LIM:
        m = n
        for p in primes:
            if p*p > m: break
            if m % p == 0:
                s.add(p)
                while m % p == 0: m //= p
        if m > 1: s.add(m)
        return s
    m = n
    for p in primes:
        if p*p > m: break
        if m % p == 0:
            s.add(p)
            while m % p == 0: m //= p
    if m > 1: s.add(m)
    return s

def rad_f(n):
    r = 1
    for p in divs(n): r *= p
    return r

def omega_vec(a, b):
    """返回 dict p -> omega_p（整数），以及 log W 口径的 Ω"""
    c = a + b
    SA = (b, c, b + c)
    u = rad_f(c)
    SM = (u*a, u*b, u*c)
    u2 = rad_f(b + c)
    SAM = (u2*b, u2*c, u2*(b + c))
    S = (a, b, c)
    om = defaultdict(int)
    for T, sign in [(SAM, +1), (S, +1), (SA, -1), (SM, -1)]:
        for comp in T:
            for p in divs(comp):
                om[p] += sign
    return dict(om)

def Omega_num(a, b):
    """数值 Ω（用 rad 乘积）"""
    c = a + b
    SA = (b, c, b + c)
    u = rad_f(c); SM = (u*a, u*b, u*c)
    u2 = rad_f(b + c); SAM = (u2*b, u2*c, u2*(b + c))
    W = lambda T: rad_f(T[0])*rad_f(T[1])*rad_f(T[2])
    return math.log(W(SAM)*W((a,b,c))/(W(SA)*W(SM)))

N = 200
print('=== C0：Ω = Σ_p ω_p log p 精确性 ===')
worst = 0.0
for a in range(1, N):
    for b in range(a, N-a+1):
        om = omega_vec(a, b)
        lhs = sum(v*math.log(p) for p, v in om.items())
        rhs = Omega_num(a, b)
        worst = max(worst, abs(lhs-rhs))
print('  max|Σ ω_p log p − Ω| = %.3e  ⟹ %s' % (worst, '精确成立 ✓' if worst < 1e-9 else '不一致 ✗'))

print()
print('=== C2：ω_p 是否只依赖 (a,b) mod p （p-局部性）===')
seen = defaultdict(set)
for a in range(1, 120):
    for b in range(a, 120-a+1):
        om = omega_vec(a, b)
        for p, v in om.items():
            seen[(p, a % p, b % p)].add(v)
bad = [(k, s) for k, s in seen.items() if len(s) > 1]
print('  键数 = %d，其中取值不唯一的键 = %d' % (len(seen), len(bad)))
if bad:
    k, s = bad[0]
    print('  反例：p=%d, a mod p=%d, b mod p=%d → ω_p ∈ %s' % (k[0], k[1], k[2], sorted(s)))
    print('  ⟹ 【存在跨素数耦合】（ω_p 需要 p 以外的信息）')
else:
    print('  ⟹ ω_p 完全 p-局部（仅依赖 a,b mod p）——无跨素数耦合')

print()
print('=== C1：局部可积性（ω_p 是否为 coboundary）===')
# 沿 A-运输检查：ω_p(T_A S) - ω_p(S) 是否只依赖某个单点势
# 判据：对每个 p，检查 map S ↦ ω_p(S) 沿 A-方向的一阶差分是否可由 p-局部量解释
diff_seen = defaultdict(set)
for a in range(1, 120):
    for b in range(a, 120-a+1):
        om1 = omega_vec(a, b)
        SA_a, SA_b = b, a + b
        if SA_a + SA_b <= 240:
            om2 = omega_vec(SA_a, SA_b)
            for p in set(om1) | set(om2):
                diff_seen[(p, om1.get(p, 0))].add(om2.get(p, 0))
multi = sum(1 for k, s in diff_seen.items() if len(s) > 1)
print('  (p, ω_p(S)) 决定 ω_p(T_A S) 的键中，多值的 = %d / %d' % (multi, len(diff_seen)))
print('  ⟹ %s' % ('ω_p 沿 A 方向不是单值函数 ⟹ 非平凡（不可积迹象）' if multi else 'ω_p 沿 A 方向单值 ⟹ 局部可积'))

print()
print('=== C3：多步累计曲率 Θ_K（交替 A/M 轨道）===')
def orbit(a0, b0, K=6):
    a, b = a0, b0
    out = []
    for k in range(K):
        out.append((a, b))
        if k % 2 == 0:
            a, b = b, a + b           # A-运输
        else:
            c = a + b
            u = rad_f(c)
            a, b = u*a, u*b           # M-运输
    return out

for (a0, b0) in [(1,1),(1,2),(2,3),(3,5),(5,7)]:
    xs = orbit(a0, b0, 6)
    Om = []
    for (a, b) in xs:
        try:
            Om.append(Omega_num(a, b))
        except Exception:
            Om.append(float('nan'))
    Th = []
    s = 0.0
    for v in Om:
        s += v; Th.append(s)
    # 归一化（除以当前 c 的对数尺度）——用 c 的对数
    cs = [math.log(a+b) for (a,b) in xs]
    print('  start=(%d,%d): Ω序列 = %s' % (a0, b0, ' '.join('%.3f' % v for v in Om)))
    print('              Θ_K = %s' % ' '.join('%.3f' % v for v in Th))
    print('              Θ_K/K = %s' % ' '.join('%.3f' % (v/(i+1)) for i, v in enumerate(Th)))
    print('              Θ_K/√K = %s' % ' '.join('%.3f' % (v/math.sqrt(i+1)) for i, v in enumerate(Th)))
