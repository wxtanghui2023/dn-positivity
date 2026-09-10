#!/usr/bin/env python3
"""A5-1/A5-2：θ(x)^w 的算术结构审计
θ(x) = 1 + u, u = 2Σ_{n≥1}e^{-πn²x}
θ^w = Σ_k C(w,k) u^k  ⟹  a_m(w) = Σ_{k≥1} C(w,k)·2^k·R_k(m)
   R_k(m) = #{(n_1..n_k)∈Z_{≥1}^k : Σn_i² = m}   （有序）
审计：① 验证 Σa_m e^{-πmx} = θ^w  ② 乘法性 a_{mn}=a_m a_n ?
     ③ 整数 w 的经典 divisor 公式对照
"""
import mpmath as mp
from fractions import Fraction
from math import gcd
mp.mp.dps = 30

MMAX = 60

# ---- R_k(m)：有序 k 元正整数平方和 ----
R = [[0]*(MMAX+1) for _ in range(MMAX+1)]
R[0][0] = 1
for k in range(1, MMAX+1):
    for m in range(k, MMAX+1):
        s = 0
        j = 1
        while j*j <= m:
            s += R[k-1][m - j*j]
            j += 1
        R[k][m] = s

def binom_w(w, k):
    """C(w,k)，w 可为非整数（浮点/有理）"""
    p = Fraction(1)
    for i in range(k):
        p *= (Fraction(w) - i)
    for i in range(1, k+1):
        p /= i
    return p

def a_m(w, m):
    tot = Fraction(0)
    for k in range(1, m+1):
        if R[k][m] == 0: continue
        tot += binom_w(w, k) * (2**k) * R[k][m]
    return tot

# ---- ① 验证 Σ a_m e^{-πmx} = θ(x)^w ----
def theta(x):
    return 1 + 2*mp.nsum(lambda n: mp.e**(-mp.pi*n*n*x), [1, mp.inf])

print('=== ① 系数公式验证：Σ a_m(w)e^{-πmx} ?= θ(x)^w − 1 ===')
for w in ['0.5', '1', '2', '4', mp.mpf('0.01')]:
    ws = str(w)
    for x in [mp.mpf(1), mp.mpf('1.5')]:
        lhs = sum(float(a_m(ws, m))*float(mp.e**(-mp.pi*m*x)) for m in range(1, MMAX+1))
        rhs = float(theta(mp.mpf(x))**mp.mpf(ws)) - 1
        print(f'  w={ws:>5} x={float(x)}: Σ={lhs:.12f}  θ^w−1={rhs:.12f}  '
              f'差={abs(lhs-rhs):.2e}')

# ---- ② 乘法性 ----
print()
print('=== ② 乘法性：a_{mn} ?= a_m·a_n（互素对）===')
for w in ['0.01', '0.5', '1', '2', '3', '4', '8']:
    bad = []
    for m in range(2, 12):
        for n in range(2, 12):
            if gcd(m, n) != 1 or m*n > MMAX: continue
            am, an, amn = a_m(w, m), a_m(w, n), a_m(w, m*n)
            if am != 0 and an != 0 and amn != am*an:
                bad.append((m, n, amn, am*an))
    verdict = '【乘法性成立】' if not bad else f'【破坏】{len(bad)} 例，如 {bad[0][:2]}'
    sample = None
    if bad:
        m, n, amn, prod = bad[0]
        sample = (m, n, float(amn), float(prod))
    print(f'  w={w:>5}: {verdict}' + (f'  (m={sample[0]},n={sample[1]}: '
          f'a_mn={sample[2]:.6g} vs a_m·a_n={sample[3]:.6g})' if sample else ''))

# ---- ③ 整数 w 的经典 divisor 公式对照 ----
print()
print('=== ③ 整数 w 的对照（r_2, r_4, r_8 经典公式）===')
def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]
def d1_d3(m):     # 奇偶分解 mod 4
    return sum(1 for d in divisors(m) if d % 4 == 1) - sum(1 for d in divisors(m) if d % 4 == 3)
def r2(m): return 4*d1_d3(m)
def r4(m): return 8*sum(d for d in divisors(m) if d % 4 != 0)
def r8(m): return 16*sum(d**3 for d in divisors(m) if d % 4 != 0)
ok2 = all(a_m('2', m) == r2(m) for m in range(1, MMAX+1))
ok4 = all(a_m('4', m) == r4(m) for m in range(1, MMAX+1))
ok8 = all(a_m('8', m) == r8(m) for m in range(1, MMAX+1))
print('  a_m(2) == r_2(m) = 4(d1-d3)(m)   ?  ' + str(ok2))
print('  a_m(4) == r_4(m) = 8*sum_{d|m,4nd} d    ?  ' + str(ok4))
print('  a_m(8) == r_8(m) = 16*sum_{d|m,4nd} d^3  ?  ' + str(ok8))
print('  a_m(1) = 2*[m is square]         ?  ' + str(
      all(a_m('1', m) == (2 if int(m**0.5)**2 == m else 0) for m in range(1, MMAX+1))))
print()
print('  前 12 项对照（w=0.5 vs w=2）：')
print('   m :  a_m(0.5)        a_m(2)')
for m in range(1, 13):
    print(f'  {m:>2} : {float(a_m("0.5", m)):>12.6f} {int(a_m("2", m)):>12}')
