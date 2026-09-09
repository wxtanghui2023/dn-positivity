#!/usr/bin/env python3
"""四态 Gram（ψ_s, ψ_{s̄}, ψ_{1-s}, ψ_{1-s̄}）——det 的 t 扫描
问: 四态 det 是否产生含 t 的离散零点（耦合结构——）还是区域零?
"""
import numpy as np
from math import log, sqrt, cos, sin

def overlap(p, s1, s2):
    """⟨ψ_{p,s1}, ψ_{p,s2}⟩——s1 = σ1+it1, s2 = σ2+it2"""
    sig1, t1 = s1
    sig2, t2 = s2
    N = sqrt((1-p**(-2*sig1))*(1-p**(-2*sig2)))
    re = sig1 + sig2
    u = (t1 - t2)*log(p)
    # 1 - p^{-re} e^{-iu}——模和实部虚部
    zr = 1 - p**(-re)*cos(u)
    zi = p**(-re)*sin(u)  # 1 - p^{-re}(cos u - i sin u)?? —— 1-p^{-re}e^{-iu} = 1-p^{-re}cos u + i p^{-re} sin u
    den = zr*zr + zi*zi
    return complex(N*zr/den, N*zi/den)

def four_det(p, sigma, t):
    """四态 Gram det: (ψ_s, ψ_{s̄}, ψ_{1-s}, ψ_{1-s̄})——s = σ+it——纯虚部相关量"""
    s = (sigma, t)
    sbar = (sigma, -t)
    oms = (1-sigma, -t)   # 1-s = 1-σ-it
    omsbar = (1-sigma, t)  # 1-s̄ = 1-σ+it
    states = [s, sbar, oms, omsbar]
    G = np.zeros((4,4), dtype=complex)
    for i in range(4):
        for j in range(4):
            G[i,j] = overlap(p, states[i], states[j])
    return np.linalg.det(G)

print('=== 四态 Gram det（p=2——σ 扫描——）===')
for sigma in [0.3, 0.4, 0.45, 0.5]:
    vals = [four_det(2, sigma, t).real for t in [0, 1, 3, 5, 10, 14.13, 20, 30]]
    print(f'  σ={sigma}: ' + ' '.join(f'{v:.4f}' for v in vals))

# det 的 t 扫描（找零点——）
print()
print('四态 det 的零点（t 扫描——σ 固定——）:')
for p in [2, 3]:
    for sigma in [0.3, 0.45]:
        zeros = []
        ts = np.linspace(0.05, 30, 8000)
        prev = None
        for t in ts:
            v = four_det(p, sigma, t).real
            if prev is not None and prev[1] > 0 > v:
                zeros.append((prev[0]+t)/2)
            prev = (t, v)
        print(f'  p={p} σ={sigma}: {len(zeros)} 个零点——{zeros[:8]}')

# det 的虚部检查（应实——）
print()
print('四态 det 的虚部（应 ~0——）:')
for t in [1, 5, 14.13]:
    d = four_det(2, 0.4, t)
    print(f'  t={t}: Re={d.real:.6f} Im={d.imag:.2e}')
