#!/usr/bin/env python3
"""C/D 最小对象：约数两通道差值 Δ_n(δ)——2026-09-09
Δ_n(δ) = E⁻(δ) − E⁺(δ)——E⁺(δ) = Σ_{d|n, d<√n}(d/√n)^δ
——E⁻(δ) = Σ_{d|n, d>√n}(d/√n)^δ——验证：
① 奇对称 Δ(−δ) = −Δ(δ)（J 反演——）
② δΔ(δ) > 0（δ≠0——单调——）
③ 纯代数（√n——无 log/ζ/ρ/谱半径——）
④ γ 通道缺失检查（Δ 只有 δ 无 γ——）
"""
from math import sqrt

def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]

def E_plus(n, delta):
    """小约数侧（d < √n）——"""
    s = 0.0
    r = sqrt(n)
    for d in divisors(n):
        if d < r:
            s += (d/r)**delta
    return s

def E_minus(n, delta):
    """大约数侧（d > √n）——"""
    s = 0.0
    r = sqrt(n)
    for d in divisors(n):
        if d > r:
            s += (d/r)**delta
    return s

def Delta(n, delta):
    return E_minus(n, delta) - E_plus(n, delta)

print('=== ① 奇对称检查：Δ(−δ) = −Δ(δ)？===')
for n in [12, 30, 60, 72, 100, 210]:
    ok = all(abs(Delta(n, d) + Delta(n, -d)) < 1e-10 for d in [0.1, 0.3, 0.7, 1.5])
    print(f'  n={n}: 奇对称 = {ok}——Δ(0.3)={Delta(n,0.3):+.6f}, '
          f'Δ(−0.3)={Delta(n,-0.3):+.6f}')

print()
print('=== ② 符号检查：δΔ(δ) > 0（δ≠0——）？===')
for n in [12, 30, 60, 72, 100]:
    vals = []
    for d in [-1.5, -0.7, -0.3, -0.1, 0.1, 0.3, 0.7, 1.5]:
        dv = Delta(n, d)
        vals.append((d, dv, d*dv > 0))
    all_ok = all(v[2] for v in vals if abs(v[0]) > 1e-9)
    print(f'  n={n}: δΔ>0 全部 = {all_ok}——样例: {vals[3]} {vals[4]}')

print()
print('=== ③ Δ 的单调性（E⁺ 递减——Δ 递增——）===')
for n in [60, 210]:
    ds = [-1.0, -0.5, 0, 0.5, 1.0]
    print(f'  n={n}: Δ({ds}) = {[f"{Delta(n,d):+.6f}" for d in ds]}')

print()
print('=== ④ γ 通道检查（Δ 的构造含 γ 吗？）===')
print('  Δ_n(δ) = Σ_{d|n}(d/√n)^δ·sgn——【只有 δ——无 γ——】')
print('  零点 ρ = ½+δ+iγ 需要 γ（相位通道——）——')
print('  约数结构（整除——）= 无相位——【γ 通道缺失】')
