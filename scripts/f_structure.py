#!/usr/bin/env python3
"""推导 -n·c_n 的解析结构——为什么与正规化抵消？
c_n = ∫_0^∞ L_{n-1}(x)F(x)dx，F(x) = Σ_{m>e^x}Λ(m)/(m log m)
F 的 Mellin 表示：F(x) = Σ_{m>e^x}Λ(m)/(m log m)
Laguerre 谱 vs 正规化的抵消——检查"主项"来自哪里
"""
import numpy as np
import math
from math import comb, factorial, log

def L_m(x, m):
    if m == 0: return np.ones_like(x)
    L0 = np.ones_like(x); L1 = 1 - x
    if m == 1: return L1
    for k in range(2, m+1):
        L2 = ((2*k-1-x)*L1 - (k-1)*L0)/k
        L0, L1 = L1, L2
    return L1

def Lambda_upto(N):
    lam = np.zeros(N+1)
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

Nmax = 10**6
lam = Lambda_upto(Nmax)
ms = np.arange(2, Nmax+1)
pref = np.cumsum(lam[2:Nmax+1] / (ms * np.log(ms)))
pref = np.concatenate([[0.0], pref])
Ptotal = pref[-1]

def F_fast(x):
    m0 = min(int(math.exp(x)), Nmax)
    if m0 < 2: return Ptotal
    return Ptotal - pref[m0-1]

xmax = log(Nmax)
xs = np.linspace(0, xmax, 6000)
Fx = np.array([F_fast(x) for x in xs])

# 分解 F = F_main + F_osc（主项 + 振荡）
# F(x) = Σ_{m>e^x}Λ(m)/(m log m)——素数定理主项：Σ_{m≤N}Λ(m)/(m log m) ~ log log N + C
# 所以 F(x) ~ log log(∞) - log log(e^x) = 大数 - log log e^x = ∞ - log x？——发散？
# 实际上：Σ_{m≤N}Λ(m)/(m log m) = log log N + C + o(1)（Mertens——无条件）
# F(x) = Σ_{m>e^x} = (log log ∞ + C) - (log log e^x + C) = ∞ - log x——发散！？
# 不对——log log ∞ 发散——但 Σ Λ(m)/(m log m) 收敛？（Mertens 的 ΣΛ(m)/m ~ log N——除以 log m 更慢）
# Σ_{m≤N}Λ(m)/(m log m)——Σ Λ(m)/m ~ log N——除以 log m ~ 1/log m——Σ ~ log N/log N ~ 常数？——收敛！

# 检查 F 的主项
print("F(x) 的结构——与 log x 比较：")
for x in [1.0, 2.0, 3.0, 5.0, 8.0, 12.0]:
    print(f"  x={x:5.1f}: F={F_fast(x):.6f}  log(x)={log(x):.4f}  1/x={1/x:.4f}")

# 关键：F(x) 的"光滑主项"——如果 F(x) ≈ A - B·g(x)（g 缓变）
# 用 F 的差分看导数
print("\nF 的差分（导数估计）：")
dx = xs[1]-xs[0]
dF = np.diff(Fx)/dx
for i in [100, 500, 1000, 2000, 4000]:
    print(f"  x={xs[i]:5.1f}: F'≈{dF[i]:+.6f}  (-1/x 参考 {-1/xs[i]:.6f})")

# Laguerre 谱 vs 正规化的"主项"分析
print("\n正规化项的代数结构：reg = Σ_{j=1}^n C(n,j)(-1)^j (log N)^j/j!")
print("这是 (1-e^{-t}) 类展开在 t=log N 处——(1-e^{-log N})^n = (1-1/N)^n")
print("(1-1/N)^n = Σ C(n,j)(-1)^j N^{-j}——而 reg 用 (log N)^j/j! 代替 N^{-j}")
print("→ reg ≈ (1-1/N)^n 的'对数版本'——不是同一个展开！")
