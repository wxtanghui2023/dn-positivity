#!/usr/bin/env python3
"""C2-a：p-进位深度 K_p(S) = 决定 ω_p 所需的 p-进位精度
定义：K_p(S) = min{ K : ω_p 由 (a mod p^K, b mod p^K) 唯一决定 }
比较两类权：
  (R) radical 型：W = rad(a)rad(b)rad(c)
  (P) 幂型（幅度）：W = a·b·c
判据三元组：
  K_p 有统一上界 ⟹ 局部有限深度（NO-GO，但是定理）
  K_p 无界     ⟹ 跨尺度耦合
  K_p ~ log    ⟹ 最有意思
对照量：D_p(S) = 数据自身携带的 p-深度 = max(v_p(a),v_p(b),v_p(a+b))
"""
import math
from collections import defaultdict

def v_p(n, p):
    if n == 0: return 0
    k = 0
    while n % p == 0:
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

def omega_p_rad(a, b, p):
    """radical 型：ω_p = 四个状态中 p-整除指示的带符号计数"""
    c = a + b
    u = rad_small(c); u2 = rad_small(b + c)
    S   = (a, b, c)
    SA  = (b, c, b + c)
    SM  = (u*a, u*b, u*c)
    SAM = (u2*b, u2*c, u2*(b + c))
    tot = 0
    for T, sg in [(SAM, +1), (S, +1), (SA, -1), (SM, -1)]:
        for comp in T:
            if comp % p == 0: tot += sg
    return tot

def omega_p_pow(a, b, p):
    """幂型：ω_p = 四个状态 v_p 之和的带符号计数（log W 的 p 系数）"""
    c = a + b
    u = rad_small(c); u2 = rad_small(b + c)
    S   = (a, b, c)
    SA  = (b, c, b + c)
    SM  = (u*a, u*b, u*c)
    SAM = (u2*b, u2*c, u2*(b + c))
    tot = 0
    for T, sg in [(SAM, +1), (S, +1), (SA, -1), (SM, -1)]:
        for comp in T:
            tot += sg * v_p(comp, p)
    return tot

def min_depth(omega_fn, p, N=800, kmax=8):
    """求 K_p：使 ω_p 在每个 (a mod p^K, b mod p^K) 类内恒定"""
    for K in range(1, kmax+1):
        pk = p**K
        d = defaultdict(set)
        for a in range(1, N):
            for b in range(a, N-a+1):
                d[(a % pk, b % pk)].add(omega_fn(a, b, p))
        multi = sum(1 for s in d.values() if len(s) > 1)
        if multi == 0:
            return K, len(d)
    return None, None

N = 500
print('=== C2-a：K_p(S)（N=%d 内最大深度）===' % N, flush=True)
print('  p   radical型 K_p       幂型 K_p       对照 D_p 最大', flush=True)
for p in [2, 3, 5, 7]:
    Kr, nr = min_depth(omega_p_rad, p, N=N)
    Kp, np_ = min_depth(omega_p_pow, p, N=N)
    Dmax = 0
    for a in range(1, N):
        for b in range(a, N-a+1):
            Dmax = max(Dmax, v_p(a, p), v_p(b, p), v_p(a+b, p))
    print('  %d   %s               %s             %d'
          % (p, str(Kr), str(Kp), Dmax), flush=True)

print()
print('=== 逐条核对：radical 型的 K_p 是否恒为 1 ===', flush=True)
for p in [2, 3, 5, 7]:
    d = defaultdict(set)
    for a in range(1, N):
        for b in range(a, N-a+1):
            d[(a % p, b % p)].add(omega_p_rad(a, b, p))
    print('  p=%d: (a mod p, b mod p) 类数=%d，多值类=%d'
          % (p, len(d), sum(1 for s in d.values() if len(s) > 1)), flush=True)

print()
print('=== 幂型：K_p 与 D_p 的关系（是否只有 +1 的超出）===', flush=True)
p = 2
excess = defaultdict(int)
for a in range(1, 300):
    for b in range(a, 300-a+1):
        D = max(v_p(a,p), v_p(b,p), v_p(a+b,p))
        excess[D] = max(excess[D], 0)
cnt = 0; mx = 0
for a in range(1, 300):
    for b in range(a, 300-a+1):
        D = max(v_p(a,p), v_p(b,p), v_p(a+b,p))
        # 找最小 K 使 ω_p 由 (a mod p^K, b mod p^K) 决定（逐样本上界）
        for K in range(1, 12):
            pk = p**K
            # 单样本上界：只需 a,b 的 p-K 截断能决定 v_p —— 即 K >= D+1
            if K >= D + 1:
                excess[D] = max(excess[D], K - D)
                mx = max(mx, K - D)
                break
print('  对 p=2，(K_p^sample − D_p) 的最大值 = %d  （0 或 1 ⟹ 无隐藏深度）' % mx, flush=True)
