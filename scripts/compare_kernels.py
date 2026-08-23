#!/usr/bin/env python3
"""关键检查：f̃ 核 vs f_n 核的黎曼和差——哪个是 r(n) 的振荡？
f_n(t) = 4sin²(nθ₁)，θ₁ = arctan(1/2t)（8/22 r(n) 权威核）
f̃(t) = 2sin(cθ)sin(θ/2)，θ = π−2arctan(2t) = 2θ₁，c = n+½（8/23 ε_m 核）

关系：f_n = 2 − 2cos(2nθ₁)；f̃ = cos(2nθ₁) − cos((2n+2)θ₁)
黎曼和差：Σf(γ_k) − ∫f N₀' dt

问题：Σf̃ − ∫f̃ N₀' 是否 = Σf_n − ∫f_n N₀'（或差常数）？
"""
import numpy as np
from numpy.polynomial.legendre import leggauss

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

def N0p(t):
    return np.log(t/(2*np.pi))/(2*np.pi)

def th1(t):
    return np.arctan(1/(2*t))

def fn(t, n):
    return 4*np.sin(n*th1(t))**2

def ftilde(t, c):
    th = np.pi - 2*np.arctan(2*t)
    return 2*np.sin(c*th)*np.sin(th/2)

K = 2000000
z = load_zeros(K)
Tmax = z[-1]

xg, wg = leggauss(8)

def riemann_sum_diff(fun, n_or_c, n, Tmax):
    """Σ f(γ_k) − ∫_2^Tmax f N₀' dt（抽样 Gauss）"""
    # Σ f(γ_k)（到 γ_max）
    if fun is fn:
        Sf = np.sum(fn(z, n))
    else:
        Sf = np.sum(ftilde(z, n_or_c))
    # ∫_2^Tmax——每5区间 8点 Gauss
    sel = np.arange(0, K-1, 5)
    total = 0.0
    for k in sel:
        a, b = z[k], z[k+1]
        ts = 0.5*(b-a)*xg + 0.5*(a+b)
        if fun is fn:
            total += 0.5*(b-a)*np.sum(wg*fn(ts, n)*N0p(ts))
        else:
            total += 0.5*(b-a)*np.sum(wg*ftilde(ts, n_or_c)*N0p(ts))
    total *= 5
    # 尾部 [Tmax, ∞)
    if fun is fn:
        # f_n ~ n²/t²（t 大）
        tail = n**2*(np.log(Tmax/(2*np.pi))/Tmax + 1/Tmax)/(2*np.pi)
    else:
        # f̃ ~ cθ·θ/2 ≈ c/t²（t 大——θ≈1/t）
        tail = n_or_c*(np.log(Tmax/(2*np.pi))/Tmax + 1/Tmax)/(2*np.pi)
    return Sf, total+tail, Sf-(total+tail)

ref = {50: 2.25, 100: 1.38, 200: 2.89, 500: -0.07, 1000: 2.51}
print(f"{'n':>5} | {'f_n 核: Σ':>10} {'∫':>10} {'差':>10} | {'f̃ 核: Σ':>10} {'∫':>10} {'差':>10} | r(n)参考")
for n in [50, 100, 200, 500, 1000]:
    c = n + 0.5
    S1, I1, D1 = riemann_sum_diff(fn, None, n, Tmax)
    S2, I2, D2 = riemann_sum_diff(ftilde, c, n, Tmax)
    r_ref = ref.get(n, float('nan'))
    print(f"{n:5d} | {S1:+10.3f} {I1:+10.3f} {D1:+10.3f} | {S2:+10.3f} {I2:+10.3f} {D2:+10.3f} | {r_ref}")
