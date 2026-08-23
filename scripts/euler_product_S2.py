#!/usr/bin/env python3
"""验证 Euler 积路径：S₂(n) = Σ Λ(m)/m·Q_n(log m) − 正规化
Q_n(t) = −n·Σ_{k=0}^{n−1} C(n−1,k)(−1)^k t^k/(k+1)!
正规化：减去 Σ_{j=1}^n C(n,j)(−1)^j (log N)^j / j!（发散抵消）

对比：Coffey 的 S₂(n)（η_j 路径——8/23 已知 [0.60, 1.50] 范围 n≤60）
"""
import numpy as np
import math
from math import comb, log

def Qn(t, n):
    """Q_n(t) = −n·Σ_{k=0}^{n−1} C(n−1,k)(−1)^k t^k/(k+1)!"""
    s = 0.0
    for k in range(n):
        s += comb(n-1, k) * (-1)**k * t**k / math.factorial(k+1)
    return -n * s

def Qn_leading(t, n):
    """主导项：(−1)^n t^{n−1}/(n−1)!"""
    return (-1)**n * t**(n-1) / math.factorial(n-1)

# 检查 Q_n 结构
print("Q_n(t) 检查：")
for n in [2, 3, 5]:
    print(f"  n={n}: Q_n(0)={Qn(0,n):.3f}（理论 −{n}）")
    for t in [0.1, 1.0, 5.0, 10.0]:
        print(f"    Q_{n}({t:.1f}) = {Qn(t,n):+.6f}  主导项 {Qn_leading(t,n):+.6f}")

# von Mangoldt 函数（素数幂）
def Lambda_upto(N):
    lam = np.zeros(N+1)
    # 素数
    sieve = np.ones(N+1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(N**0.5)+1):
        if sieve[i]: sieve[i*i::i] = False
    primes = np.nonzero(sieve)[0]
    for p in primes:
        pk = p
        while pk <= N:
            lam[pk] += log(p)
            pk *= p
    return lam

def S2_euler(n, N):
    """S₂(n) ≈ Σ_{m≤N} Λ(m)/m·Q_n(log m) − 正规化"""
    lam = Lambda_upto(N)
    ms = np.arange(2, N+1)
    total = 0.0
    for m in range(2, N+1):
        if lam[m] > 0:
            total += lam[m]/m * Qn(log(m), n)
    # 正规化：Σ_{j=1}^n C(n,j)(−1)^j (log N)^j / j!
    reg = sum(comb(n,j) * (-1)**j * log(N)**j / math.factorial(j) for j in range(1, n+1))
    return total - reg, total, reg

# Coffey S₂ 参考（8/23：范围 [0.60, 1.50]——n≤60）
print("\nEuler 积 S₂(n) vs Coffey 参考：")
for n in [2, 3, 5, 10, 20]:
    for N in [10**4, 10**5, 10**6]:
        s2, raw, reg = S2_euler(n, N)
        print(f"  n={n:2d} N={N:7d}: S₂={s2:+8.4f}（raw={raw:+10.2f} reg={reg:+10.2f}）")
    print()
