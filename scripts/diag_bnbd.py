#!/usr/bin/env python3
# 诊断 BNBD 实现: μ 筛 + V_N vs 1/ζ
import numpy as np
import mpmath as mp

def mobius_sieve(N):
    mu = np.ones(N+1, dtype=np.int8)
    is_prime = np.ones(N+1, dtype=bool)
    is_prime[:2] = False
    for i in range(2, int(N**0.5)+1):
        if is_prime[i]:
            is_prime[i*i::i] = False
            for j in range(i, N+1, i):
                mu[j] *= -1
            i2 = i*i
            for j in range(i2, N+1, i2):
                mu[j] = 0
    return mu

mp.mp.dps = 30
N = 1000
mu = mobius_sieve(N)
print(f"μ 检查: μ(1)={mu[1]} μ(2)={mu[2]} μ(3)={mu[3]} μ(4)={mu[4]} μ(6)={mu[6]} μ(30)={mu[30]}")
print(f"预期: μ(1)=1 μ(2)=-1 μ(3)=-1 μ(4)=0 μ(6)=1 μ(30)=-1")

# 在 s 较大处检查 V_N ≈ 1/ζ
# V_N(s) 系数
logN = np.log(N)
ns = np.arange(1, N+1)
coeff = (1 - np.log(ns)/logN) * mu[1:N+1]

for s_real in [2.0, 1.5]:
    # V_N(s_real) = Σ coeff n^{-s_real}
    vn = np.sum(coeff * ns**(-s_real))
    inv_zeta = 1/mp.zeta(s_real)
    print(f"s={s_real}: V_N={vn:.6f}  1/ζ={float(inv_zeta):.6f}  差={abs(vn-float(inv_zeta)):.6f}")

# 在临界线上检查 (s = ½+it)
for t in [0, 5, 14.1347, 20]:
    # V_N(½+it)
    vn = np.sum(coeff * ns**(-0.5) * np.exp(-1j*t*np.log(ns)))
    zeta_val = complex(mp.zeta(0.5 + 1j*t))
    prod = zeta_val * vn
    print(f"t={t:.4f}: ζV_N = {prod.real:.4f}{prod.imag:+.4f}i  |1-ζV_N| = {abs(1-prod):.4f}")
