#!/usr/bin/env python3
"""验证唐先生的构造: κ_p(σ) = √((1-p^{-2σ})(1-p^{-2+2σ}))/(1-p^{-1})
K(s) = ∏_p κ_p(σ)——σ=1/2 时 =1——否则 → 0?
1. κ_p 数值验证（AM-GM 界——σ=1/2 唯一最大——）
2. K(s) 的无限素数极限行为（σ≠1/2 → 0?——收敛速度——）
3. 与 ζ 零点的可能耦合（J1——）探索
"""
import numpy as np
from math import sqrt, log

def kappa_p(p, sigma):
    """κ_p(σ) = √((1-p^{-2σ})(1-p^{-2+2σ}))/(1-p^{-1})"""
    a = p**(-2*sigma)
    b = p**(-2+2*sigma)
    return sqrt((1-a)*(1-b))/(1-1.0/p)

print('=== κ_p(σ) 验证 ===')
for sigma in [0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8]:
    vals = [kappa_p(p, sigma) for p in [2, 3, 5, 7, 11]]
    print(f'  σ={sigma}: κ_2={vals[0]:.6f} κ_3={vals[1]:.6f} κ_5={vals[2]:.6f} κ_7={vals[3]:.6f} κ_11={vals[4]:.6f}')

# σ=1/2 检查（应该 = 1）
print()
print('σ=1/2 时 κ_p（应 = 1——）:')
for p in [2, 3, 5, 7]:
    print(f'  p={p}: κ_p = {kappa_p(p, 0.5):.10f}')

# AM-GM: σ=1/2 唯一最大值验证（κ_p ≤ 1——等号当 σ=1/2——）
print()
print('κ_p 是否 ≤ 1（等号唯一在 σ=1/2——）:')
for p in [2, 3]:
    sigs = np.linspace(0.01, 0.99, 200)
    ks = [kappa_p(p, s) for s in sigs]
    mx = max(ks)
    mx_s = sigs[ks.index(mx)]
    print(f'  p={p}: max κ = {mx:.8f} at σ = {mx_s:.3f}（应 1.0 at 0.5——）')

# K(s) = ∏_p κ_p——数值（前 N 个素数——）
print()
print('=== K(s) = ∏_p κ_p(σ)（前 N 素数——）===')
def primes_below(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = False
    return np.nonzero(sieve)[0]
pr = primes_below(5000)  # 前 ~670 个素数

for sigma in [0.25, 0.4, 0.45, 0.5, 0.55, 0.6, 0.75]:
    # 用 log K = Σ log κ_p——避免下溢
    logK = sum(log(kappa_p(p, sigma)) for p in pr)
    print(f'  σ={sigma}: log K = {logK:.3f}——K = {sqrt(0) if logK < -700 else logK:.2e}')

# 收敛速度: σ≠1/2 时 Σ -log κ_p 发散（p^{-2min(σ,1-σ)} 首阶——）
print()
print('Σ_p -log κ_p 的发散（σ≠1/2——）:')
for sigma in [0.25, 0.4, 0.45]:
    # 分块看增长
    cum = 0
    for i, p in enumerate(pr):
        cum += -log(kappa_p(p, sigma))
        if p in [100, 500, 1000, 2000, 5000]:
            print(f'    p≤{p}: Σ-log κ = {cum:.2f}')
