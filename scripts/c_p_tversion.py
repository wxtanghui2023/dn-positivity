#!/usr/bin/env python3
"""K_p 的含 t 推广验证：c_p(s) = ⟨ψ_{p,s}, ψ_{p,1-s}⟩
|c_p|² = (1-a)(1-b)/|1-p^{-1}e^{-2it·log p}|²——a=p^{-2σ}, b=p^{-2+2σ}
猜想：|c_p|² ≤ 1——等号 ⟺ σ=½ 且 t·log p = πk（离散 t——）
——这是 K_p（纯 σ——等号全线）的含 t 版本——等号离散化——
"""
import numpy as np
from math import log, pi

def c_p(p, sigma, t):
    lp = log(p)
    a = p**(-2*sigma)
    b = p**(-2+2*sigma)
    num = (1-a)*(1-b)
    # |1 - p^{-1} e^{-2it lp}|² = 1 - 2p^{-1}cos(2t lp) + p^{-2}
    den = 1 - 2*p**(-1)*np.cos(2*t*lp) + p**(-2)
    return num/den

print('=== |c_p|² 验证（≤1?——等号 σ=½ + t=πk/log p——）===')
for p in [2, 3, 5]:
    # σ=½ 的等号点 t = πk/log p
    lp = log(p)
    print(f'  p={p}（等号点 t_k = kπ/log{p}——）:')
    for k in [0, 1, 2, 3]:
        t_k = k*pi/lp
        val = c_p(p, 0.5, t_k)
        print(f'    t={t_k:.4f}（k={k}）: |c_p|² = {val:.6f}（应 ~1——）')
    # σ≠½ 同 t——应 <1
    t1 = pi/lp
    print(f'    σ=0.4, t=t₁: {c_p(p, 0.4, t1):.6f}——σ=0.6, t=t₁: {c_p(p, 0.6, t1):.6f}（应 <1——）')
    # 非等号 t（无理偏移——）
    print(f'    σ=0.5, t=14.13: {c_p(p, 0.5, 14.13):.6f}（非等号点——<1——）')

# ζ 零点处 |c_p|² 的跨 p 行为
print()
print('=== ζ 零点 vs 非零点：|c_p(½,t)|² 的跨 p 和 ===')
def S(t, pr):
    return sum(c_p(p, 0.5, t) for p in pr)
pr = [2, 3, 5, 7, 11, 13, 17, 19]
for t in [10.0, 14.13, 15.0, 20.0, 21.02, 25.0, 25.01, 30.0, 32.94, 35.0]:
    print(f'  t={t}: Σ_p|c_p(½,t)|² = {S(t, pr):.4f}（N={len(pr)}——若全~1 则 ~N——）')

# 偏离（Σ(|c_p|²-1)——）
print()
print('=== Σ_p(|c_p(½,t)|²−1)（偏离——零点处特殊？）===')
for t in [10.0, 14.13, 14.5, 20.0, 21.02, 25.0, 25.01, 30.0, 32.94]:
    dev = sum(c_p(p, 0.5, t) - 1 for p in pr)
    print(f'  t={t}: Σ(|c_p|²−1) = {dev:+.6f}')
