#!/usr/bin/env python3
"""深挖 Q_n(t)：生成函数 + Bell 多项式（无 sympy——数值验证）
exp(−tz/(1−z)) = exp(−t·Σ_{k≥1} z^k)——系数 = 部分 Bell 多项式
[z^n] exp(−tΣ_{k≥1}z^k) = Σ_{k=1}^n (−t)^k/k!·B_{n,k}(1!,2!,3!,...)（Bell 多项式——单项参数）
"""
import numpy as np
import math
from math import comb, factorial

def Qn(t, n):
    s = sum(comb(n-1,k)*(-1)**k*t**k/factorial(k+1) for k in range(n))
    return -n*s

def L_m(x, m):
    return sum(comb(m,k)*(-x)**k/factorial(k) for k in range(m+1))

def int_L_simpson(t, m, N=20000):
    xs = np.linspace(0, t, N+1)
    ys = np.array([L_m(x, m) for x in xs])
    return np.trapz(ys, xs)

# 生成函数系数：1 − exp(−t·Σ_{k≥1}z^k)——展开
# exp(−t·(z+z²+z³+...))——用 Bell 多项式 B_{n,k}(x_1,...,x_{n-k+1})，x_j = j!
# [z^n]exp(Σ_{j≥1} a_j z^j) 的显式：Σ_{k=1}^n (1/k!)·Σ_{j_1+...+j_k=n} a_{j_1}...a_{j_k}
def coeff_gen(n, t):
    """[z^n](1 − exp(−t·Σ_{j≥1}z^j))——a_j = −t 对所有 j"""
    # exp(Σ a_j z^j) 系数 = Σ_{k=1}^n (1/k!)·[组合和]
    # 用递推：f(z) = exp(g(z))——f' = g'f——n f_n = Σ_{j=1}^n j a_j f_{n-j}
    f = [0.0]*(n+1)
    f[0] = 1.0
    a = [-t]*n  # a_j = −t（j=1..n）
    for m in range(1, n+1):
        s = 0.0
        for j in range(1, m+1):
            s += j * a[j-1] * f[m-j]
        f[m] = s / m
    return -f[n]  # 1 − exp(...) 的系数 = −f[n]（n≥1）

print("验证生成函数：∫_0^t L_{n-1}(x)dx = [z^n](1−exp(−tz/(1−z)))")
for n in [1, 2, 3, 4, 5, 8]:
    for tv in [1.0, 2.0]:
        c = coeff_gen(n, tv)
        iv = int_L_simpson(tv, n-1)
        print(f"  n={n} t={tv}: [z^n]={c:+.6f} vs ∫L_{n-1}={iv:+.6f}（差 {abs(c-iv):.2e}）")

print("\n验证 Q_n(t) = −(n/t)·[z^n](...)：")
for n in [2, 3, 5, 10]:
    for tv in [0.5, 2.0, 5.0]:
        c = coeff_gen(n, tv)
        val = -(n/tv)*c
        direct = Qn(tv, n)
        print(f"  n={n} t={tv}: 生成={val:+.6f} vs Qn={direct:+.6f}（差 {abs(val-direct):.2e}）")

# Bell 多项式视角：Q_n 的系数 vs 完全 Bell 多项式
print("\nQ_n(t) 多项式系数（n=6）：")
for k in range(6):
    ck = -6*comb(5,k)*(-1)**k/(factorial(k+1))
    print(f"  c_{k} = {ck:+.6f}（t^{k} 的系数）")
