#!/usr/bin/env python3
"""三态 Gram determinant Δ_p(σ,t) 的完全化简 + G(s)=∏Δ_p 坍缩测试
三态: ψ_s, ψ_{1-s}, ψ_{1-s̄}
Gram: [[1, c, κ], [c̄, 1, d], [κ, d̄, 1]]
κ = √((1-a)(1-b))/(1-1/p)   (纯 σ——)
c = √((1-a)(1-b))/(1-p^{-1-2it})
d = (1-b)/(1-b·p^{2it})      (a=p^{-2σ}, b=p^{-2+2σ})
Δ_p = 1 - |c|² - |d|² - κ² + 2κ·Re(c·d)   (Gram 行列式——实——≥0——)
"""
import numpy as np
from math import log, sqrt, cos, sin

def gram_det(p, sigma, t):
    """Δ_p(σ,t)——数值——"""
    lp = log(p)
    a = p**(-2*sigma)
    b = p**(-2+2*sigma)
    N = sqrt((1-a)*(1-b))
    # κ 纯实
    kappa = N/(1-1.0/p)
    # c = N/(1-p^{-1-2it})
    c_re = N*(1 - p**(-1)*cos(2*t*lp)) / ((1-p**(-1)*cos(2*t*lp))**2 + (p**(-1)*sin(2*t*lp))**2)
    c_im = N*(p**(-1)*sin(2*t*lp)) / ((1-p**(-1)*cos(2*t*lp))**2 + (p**(-1)*sin(2*t*lp))**2)
    # d = (1-b)/(1-b·p^{2it})——p^{2it} = cos(2t lp)+i sin(2t lp)
    den_re = 1 - b*cos(2*t*lp)
    den_im = -b*sin(2*t*lp)
    den2 = den_re**2 + den_im**2
    d_re = (1-b)*den_re/den2
    d_im = (1-b)*den_im/den2
    # Δ = 1 - |c|² - |d|² - κ² + 2κ·Re(c·d)
    cc = c_re**2 + c_im**2
    dd = d_re**2 + d_im**2
    # c·d 实部
    cd_re = c_re*d_re - c_im*d_im
    return 1 - cc - dd - kappa**2 + 2*kappa*cd_re

print('=== Δ_p(σ,t) 数值（Gram 行列式——应 ≥0——）===')
for sigma in [0.3, 0.5, 0.7]:
    for t in [0, 1, 3, 10, 14.13, 20]:
        vals = [gram_det(p, sigma, t) for p in [2, 3, 5]]
        print(f'  σ={sigma} t={t:6.2f}: Δ_2={vals[0]:.6f} Δ_3={vals[1]:.6f} Δ_5={vals[2]:.6f}')

# 正性检查（Gram 应 ≥0——）
print()
print('Δ_p ≥ 0 检查（随机 σ,t——）:')
rng = np.random.default_rng(1)
neg = 0
for _ in range(1000):
    sigma = rng.uniform(0.1, 0.9)
    t = rng.uniform(0, 50)
    for p in [2, 3, 5, 7]:
        if gram_det(p, sigma, t) < -1e-10:
            neg += 1
print(f'  负值次数: {neg}/4000（应 0——Gram 正定——）')

# G(s) = ∏Δ_p——σ 扫描（t 固定）看零点结构
print()
print('=== G(s) = ∏_p Δ_p(σ,t)——σ 扫描（t=14.13——）===')
def primes_below(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return np.nonzero(sieve)[0]
pr = primes_below(2000)
for t_fix in [0, 14.13, 21.02]:
    print(f'  t={t_fix}:')
    for sigma in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        # log G = Σ log Δ_p（Δ_p 可 = 0——用 log 注意——）
        logG = sum(log(max(gram_det(p, sigma, t_fix), 1e-300)) for p in pr)
        print(f'    σ={sigma}: log G = {logG:.2f}', end='')
    print()
