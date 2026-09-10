#!/usr/bin/env python3
"""A-N1：w 到底改变了"算术对象"还是只连续变形"已有解析对象"？
检验命题 P1：a_m(w) 是 w 的多项式（次数 ≤ m），且在整数 n 处 = r_n(m)
             （m 表示为 n 个平方和的有序带符号表示数）
检验命题 P2：D_w(s) = Σ_k C(w,k)2^k E_k(s)，E_k 为固定经典族（与 w 无关）
"""
import mpmath as mp
from fractions import Fraction
from itertools import product
mp.mp.dps = 30

MMAX = 12
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
    return sum(binom_w(w, k)*(2**k)*R[k][m] for k in range(1, m+1))

# ---- r_n(m)：n 个平方和的有序带符号表示数（穷举小范围）----
def r_bruteforce(n, m, lim=6):
    cnt = 0
    rng = list(range(-lim, lim+1))
    for tup in product(rng, repeat=n):
        if sum(x*x for x in tup) == m:
            cnt += 1
    return cnt

print('=== P1 验证：a_m(n) =? r_n(m)  （整数 n = 格点维数）===')
ok_all = True
for n in range(0, 7):
    for m in range(0, 8):
        av = a_m(n, m)
        if m == 0:
            rv = 1 if n == 0 else 0
        else:
            rv = r_bruteforce(n, m, lim=int(m**0.5)+1)
        ok = (av == rv)
        ok_all &= ok
        if not ok:
            print(f'  ✗ n={n} m={m}: a_m={av} r_n={rv}')
print(f'  n∈[0,6], m∈[0,7] 全部一致 ? {ok_all}')

print()
print('=== P1b：a_m(w) 在 w=0,1,...,m 处的取值（应为 r_0..r_m）===')
for m in range(1, 7):
    vals = [a_m(n, m) for n in range(0, m+1)]
    print(f'  m={m}: a_m(0..{m}) = {vals}')

print()
print('=== P1c：a_m 的零点结构（多项式在哪些整数处为零）===')
for m in range(1, 9):
    zeros = [n for n in range(0, 12) if a_m(n, m) == 0]
    print(f'  m={m}: a_m(n)=0 at n ∈ {zeros[:10]}')

print()
print('=== P2 验证：a_m(w) = Σ_k C(w,k)2^k R_k(m)，R_k 与 w 无关 ===')
for w in [mp.mpf('0.5'), mp.mpf('1.7'), 3]:
    for m in [3, 5, 7]:
        lhs = float(a_m(Fraction(7,4) if w != 3 else 3, m))
        rhs = sum(float(binom_w(Fraction(7,4) if w != 3 else 3, k))*(2**k)*R[k][m]
                  for k in range(1, m+1))
        print(f'  w={w} m={m}: a_m={lhs:.8g}  Σ_k C(w,k)2^kR_k={rhs:.8g}  '
              f'{"✓" if abs(lhs-rhs) < 1e-12 else "✗"}')
