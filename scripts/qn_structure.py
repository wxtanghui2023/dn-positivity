#!/usr/bin/env python3
"""深挖 Q_n(t) 的结构：Laguerre 积分 + 生成函数 + Bell 多项式
Q_n(t) = −n·∫_0^1 L_{n-1}(tu)du = −(n/t)·∫_0^t L_{n-1}(x)dx
生成函数：Σ_{m≥0}[∫_0^t L_m(x)dx]z^m = (1/z)[1−exp(−tz/(1−z))]
⟹ ∫_0^t L_{n-1}(x)dx = [z^n](1−exp(−tz/(1−z)))

exp(−tz/(1−z)) = exp(−tΣ_{k≥1}z^k)——部分 Bell 多项式 B_{n,k}
"""
import numpy as np
import math
from math import comb, factorial

def Qn(t, n):
    """Q_n(t) = −n·Σ_{k=0}^{n−1} C(n−1,k)(−1)^k t^k/(k+1)!"""
    s = sum(comb(n-1,k)*(-1)**k*t**k/factorial(k+1) for k in range(n))
    return -n*s

def L_m(x, m):
    """Laguerre 多项式"""
    return sum(comb(m,k)*(-x)**k/factorial(k) for k in range(m+1))

def int_L(t, m):
    """∫_0^t L_m(x)dx——数值（Simpson）"""
    N = 10000
    xs = np.linspace(0, t, N+1)
    ys = np.array([L_m(x, m) for x in xs])
    return np.trapezoid(ys, xs)

# 验证生成函数：∫_0^t L_{n-1}(x)dx = [z^n](1−exp(−tz/(1−z)))
print("验证生成函数（t=2）：")
from sympy import symbols, exp, series, integrate, lambdify
z, x, t = symbols('z x t')
# 计算 [z^n](1−exp(−tz/(1−z))) 的系数
for n in [1, 2, 3, 4, 5]:
    # 展开到 z^n
    g = 1 - exp(-t*z/(1-z))
    coeff = series(g, z, 0, n+1).coeff(z, n)
    # 数值化（t=2）
    val = float(coeff.subs(t, 2))
    # 直接积分
    iv = int_L(2, n-1)
    print(f"  n={n}: [z^n](1−e^(−tz/(1−z)))@t=2 = {val:+.6f}  vs ∫_0^2 L_{n-1}dx = {iv:+.6f}")

# 验证 Q_n = −(n/t)·[z^n](...)
print("\n验证 Q_n(t) = −(n/t)·[z^n](1−exp(−tz/(1−z)))：")
for n in [2, 3, 5]:
    for tv in [0.5, 1.0, 3.0]:
        g = 1 - exp(-t*z/(1-z))
        coeff = series(g, z, 0, n+1).coeff(z, n)
        val = float(-(n/tv)*coeff.subs(t, tv))
        direct = Qn(tv, n)
        print(f"  n={n} t={tv}: 生成函数 Q={val:+.6f} vs 直接 Qn={direct:+.6f}（差 {abs(val-direct):.2e}）")

# Q_n 的零点（Laguerre 正交性相关）
print("\nQ_n(t) 的零点（n=3,5,8）：")
for n in [3, 5, 8]:
    # 找零点
    ts = np.linspace(-2, 20, 4000)
    qs = np.array([Qn(t, n) for t in ts])
    zeros = []
    for i in range(len(ts)-1):
        if qs[i]*qs[i+1] < 0:
            zeros.append(round((ts[i]+ts[i+1])/2, 4))
    print(f"  n={n}: 零点 ≈ {zeros}")
