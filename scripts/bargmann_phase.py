#!/usr/bin/env python3
"""θ_p = arg B_p 的验证 + 坍缩检查
B_p = ⟨ψ_s,ψ_{1-s}⟩⟨ψ_{1-s},ψ_{1-s̄}⟩⟨ψ_{1-s̄},ψ_s⟩
公式: θ_p = Σ_k (b^k - p^{-k}) sin(2kt·log p)/k——b = p^{-2+2σ}
检查: Σ_p θ_p 是否 = arg 某 Euler 积（坍缩——）?
"""
import numpy as np
from math import log, sqrt, cos, sin, atan2, pi

def overlap_phase_contrib(p, sigma, t):
    """直接算 B_p 的相位（数值——）vs 展开公式——"""
    lp = log(p)
    a = p**(-2*sigma)
    b = p**(-2+2*sigma)
    R = sqrt((1-a)*(1-b))
    # ⟨ψ_s,ψ_{1-s}⟩ = R/(1-p^{-1}e^{-2itl})——复
    z1_re = 1 - p**(-1)*cos(2*t*lp)
    z1_im = p**(-1)*sin(2*t*lp)  # 1 - p^{-1}e^{-2itl} = 1-p^{-1}cos+ip^{-1}sin
    c_re = R*z1_re/(z1_re**2+z1_im**2)
    c_im = R*z1_im/(z1_re**2+z1_im**2)
    # ⟨ψ_{1-s},ψ_{1-s̄}⟩ = (1-b)/(1-b·p^{2it})——复
    z2_re = 1 - b*cos(2*t*lp)
    z2_im = -b*sin(2*t*lp)
    d_re = (1-b)*z2_re/(z2_re**2+z2_im**2)
    d_im = (1-b)*z2_im/(z2_re**2+z2_im**2)
    # ⟨ψ_{1-s̄},ψ_s⟩ = R/(1-p^{-1})——实
    kappa = R/(1-1.0/p)
    # B = c·d·kappa——相位
    B_re = (c_re*d_re - c_im*d_im)*kappa
    B_im = (c_re*d_im + c_im*d_re)*kappa
    return atan2(B_im, B_re)

def theta_formula(p, sigma, t, kmax=50):
    """展开公式 Σ (b^k - p^{-k}) sin(2kt l)/k"""
    lp = log(p)
    b = p**(-2+2*sigma)
    s = 0.0
    bk = 1.0
    pk = p**(-1)
    for k in range(1, kmax+1):
        bk *= b
        pk *= p**(-1)
        s += (bk - pk)*sin(2*k*t*lp)/k
    return s

print('=== θ_p 验证（数值 vs 公式——）===')
for p in [2, 3, 5]:
    for sigma in [0.3, 0.5, 0.7]:
        for t in [1.5, 5.0, 14.13]:
            d = overlap_phase_contrib(p, sigma, t)
            f = theta_formula(p, sigma, t)
            print(f'  p={p} σ={sigma} t={t}: 数值={d:+.6f} 公式={f:+.6f} 差={d-f:+.2e}')

# Σ_p θ_p 的坍缩检查——θ_p 含 2t 频率（vs arg ζ 的 t 频率——）
print()
print('=== Σ_p θ_p vs arg ζ(1+2it) 类（坍缩检查——）===')
print('（若 Σθ_p = arg∏(1-p^{-z}) 类——坍缩——若 2t 频率——不坍缩——）')
# Σ_p θ_p（前 N 素数——）vs t·log p 频率结构
def primes_below(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return [int(x) for x in np.nonzero(sieve)[0]]
pr = primes_below(2000)

for sigma in [0.4, 0.6]:
    # Σ_p θ_p 随 t（看频率——与 sin(2t·log 2) 的相关——）
    ts = np.linspace(0.1, 50, 500)
    vals = []
    for t in ts:
        s = sum(theta_formula(p, sigma, t, 20) for p in pr[:100])
        vals.append(s)
    vals = np.array(vals)
    # 与 sin(2t log2) 的相关（2t 频率——）vs sin(t log 2)
    c2 = np.corrcoef(vals, np.sin(2*ts*log(2)))[0,1]
    c1 = np.corrcoef(vals, np.sin(ts*log(2)))[0,1]
    print(f'  σ={sigma}: Σθ_p ~ sin(2t·log2)? corr={c2:+.3f}——~sin(t·log2)? corr={c1:+.3f}')
