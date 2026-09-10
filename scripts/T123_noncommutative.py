#!/usr/bin/env python3
"""T1/T2/T3：非交换算术状态传播的可证伪实验
状态 S=(a,b)；A(a,b)=(a+b,b)，M(a,b)=(ab,b)
内部状态 Π = 有序算子积（算子由算术权构造）
  U_A(a,b) = [[1, r(a+b)],[0,1]]
  U_M(a,b) = [[1, 0],[r(ab),1]]      r(n) = log rad(n)
  Π_AM = U_M(A(S))·U_A(S)     Π_MA = U_A(M(S))·U_M(S)
  K2(S) = Π_AM − Π_MA
T1：K2 ≢ 0 ？  T2：同端点不同 Π ？  T3：Δ3(p,q,r) ≠ 0 ？
"""
import math
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

def r(n): return math.log(rad(n))

def matmul(X, Y):
    return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
            [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]

def UA(a, b): return [[1.0, r(a+b)], [0.0, 1.0]]
def UM(a, b): return [[1.0, 0.0], [r(a*b), 1.0]]

def K2(a, b):
    SA = (a+b, b); SM = (a*b, b)
    PAM = matmul(UM(*SA), UA(a, b))
    PMA = matmul(UA(*SM), UM(a, b))
    return [[PAM[i][j]-PMA[i][j] for j in range(2)] for i in range(2)]

def K2scalar(a, b):        # 取 (0,0) 分量作为标量不变量
    return K2(a, b)[0][0]

print('=== T1：非交换性 F_M F_A ≠ F_A F_M ===')
nz = tot = 0
for a in range(1, 60):
    for b in range(1, 60):
        tot += 1
        if abs(K2scalar(a,b)) > 1e-12: nz += 1
print('  K2 ≠ 0 : %d/%d = %.4f' % (nz, tot, nz/tot))
k = K2(3, 5)
print('  例 K2(3,5) = [[%.6f, %.6f],[%.6f, %.6f]]' % (k[0][0],k[0][1],k[1][0],k[1][1]))
print('  ⟹ T1 %s' % ('通过 ✓' if nz/tot > 0.9 else '不通过'))

print()
print('=== T2：同端点、不同内部状态（b=1 族：AM 与 MA 端点相同）===')
same_pt_diff_pi = 0; tested = 0
for a in range(1, 40):
    S = (a, 1)
    end_AM = ((a+1)*1, 1)      # M(A(S)) 的端点
    end_MA = (a*1+1, 1)        # A(M(S)) 的端点
    tested += 1
    if end_AM == end_MA:
        PAM = matmul(UM(*((a+1), 1)), UA(a, 1))
        PMA = matmul(UA(*((a), 1)), UM(a, 1))
        if any(abs(PAM[i][j]-PMA[i][j]) > 1e-12 for i in range(2) for j in range(2)):
            same_pt_diff_pi += 1
print('  端点相同且 Π 不同 : %d/%d' % (same_pt_diff_pi, tested))
print('  ⟹ T2 %s （端点只是当前整数，Π 携带路径）' % ('通过 ✓' if same_pt_diff_pi == tested else '不通过'))

print()
print('=== T3：不可分解三体项 Δ3(p,q,r) ===')
def f(primes):
    if not primes: return 0.0
    n = 1
    for p in primes: n *= p
    return K2scalar(n, 1)

def Delta3(p, q, s):
    return (f((p,q,s)) - f((p,q)) - f((q,s)) - f((p,s))
            + f((p,)) + f((q,)) + f((s,)))

primes = [2,3,5,7,11]
vals = []
for (p,q,s) in combinations(primes, 3):
    v = Delta3(p,q,s)
    vals.append(abs(v))
    print('  Δ3(%d,%d,%d) = %+.10f' % (p,q,s,v))
print('  非零个数 = %d/%d，绝对值中位 = %.6f'
      % (sum(1 for v in vals if v > 1e-12), len(vals),
         sorted(vals)[len(vals)//2] if vals else 0.0))
print('  ⟹ T3 %s' % ('系统非零 ✓' if sum(1 for v in vals if v > 1e-10) >= len(vals)-1 else '≈0 ⟹ 关闭'))
