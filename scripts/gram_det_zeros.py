#!/usr/bin/env python3
"""Δ_p 的完整数值分析: (σ,t) 零点结构——G(s)=∏Δ_p 的行为
+ 关键: Δ_p(σ=0.5, t)=0（ψ_{1-s̄}=ψ_s 退化——）vs Δ_p(t=0)=0
问题: Δ_p 的零点（σ≠0.5 时——）是离散的还是区域的?
G(s) 是否含离散零点（耦合 ζ——）还是纯区域（σ=0.5 线 + 别的——）?
"""
import numpy as np
from math import log, sqrt, cos, sin

def gram_det(p, sigma, t):
    lp = log(p)
    a = p**(-2*sigma)
    b = p**(-2+2*sigma)
    N = sqrt((1-a)*(1-b))
    kappa = N/(1-1.0/p)
    # c = N/(1-p^{-1-2it})
    u = 2*t*lp
    den_c = (1-p**(-1)*cos(u))**2 + (p**(-1)*sin(u))**2
    c_re = N*(1 - p**(-1)*cos(u))/den_c
    c_im = N*(p**(-1)*sin(u))/den_c
    # d = (1-b)/(1-b·p^{2it})
    den_re = 1 - b*cos(u)
    den_im = -b*sin(u)
    den2 = den_re**2 + den_im**2
    d_re = (1-b)*den_re/den2
    d_im = (1-b)*den_im/den2
    cc = c_re**2 + c_im**2
    dd = d_re**2 + d_im**2
    cd_re = c_re*d_re - c_im*d_im
    return 1 - cc - dd - kappa**2 + 2*kappa*cd_re

def primes_below(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]
pr = primes_below(3000)

# Δ_p 的 (σ,t) 零点结构（σ≠0.5——t 扫描找零点——）
print('=== Δ_p 的零点（σ 固定——t 扫描——）===')
for p in [2, 3]:
    for sigma in [0.3, 0.4]:
        zeros = []
        ts = np.linspace(0.01, 30, 6000)
        prev = None
        for t in ts:
            v = gram_det(p, sigma, t)
            if prev is not None and prev[1] > 0 > v:
                zeros.append((prev[0]+t)/2)
            prev = (t, v)
        print(f'  p={p} σ={sigma}: {len(zeros)} 个零点——t = {[f"{z:.2f}" for z in zeros[:10]]}')

# 零点的 t log p 位置检查（是否 t·log p = 常数——）
print()
print('零点位置 t·log p（检查是否常数——）:')
for p in [2, 3, 5]:
    sigma = 0.4
    zeros = []
    ts = np.linspace(0.01, 20, 4000)
    prev = None
    for t in ts:
        v = gram_det(p, sigma, t)
        if prev is not None and prev[1] > 0 > v:
            zeros.append((prev[0]+t)/2)
        prev = (t, v)
    print(f'  p={p}: t·log p = {[f"{z*log(p):.3f}" for z in zeros[:8]]}')

# G(s) = ∏Δ_p——σ 扫描（t 固定——）
print()
print('=== G(s) = ∏_p Δ_p(σ,t)（log——）===')
for t_fix in [5.0, 14.13, 21.02, 30.0]:
    out = []
    for sigma in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        logG = sum(log(max(gram_det(p, sigma, t_fix), 1e-320)) for p in pr)
        out.append(f'σ={sigma}:{logG:.1f}')
    print(f'  t={t_fix}: ' + ' '.join(out))
