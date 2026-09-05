#!/usr/bin/env python3
# V_N 逼近 1/ζ 在不同 σ - 找数值可行区域
# 以及: 离轴零点对 ψ 的经典影响 (x^{σ₀}) - 在 σ>½ 的可见性
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

print("=== V_N 逼近 1/ζ 在不同 σ (N=10^4) ===")
N = 10000
mu = mobius_sieve(N)
logN = np.log(N)
ns = np.arange(1, N+1)
coeff = (1 - np.log(ns)/logN) * mu[1:N+1]

for sigma in [0.6, 0.7, 0.8, 0.9, 1.0, 1.2]:
    vn = np.sum(coeff * ns**(-sigma))
    inv_zeta = 1/mp.zeta(sigma)
    print(f"σ={sigma:.1f}: V_N={vn:.6f}  1/ζ={float(inv_zeta):.6f}  |差|={abs(vn-float(inv_zeta)):.6f}  相对={abs(vn-float(inv_zeta))/abs(float(inv_zeta)):.4f}")

print("\n=== 临界线上 V_N(½+it) 随 N 的收敛 (t=5) ===")
for Nt in [1000, 10000, 100000]:
    mu2 = mobius_sieve(Nt) if Nt > N else mu
    logNt = np.log(Nt)
    ns2 = np.arange(1, Nt+1)
    coeff2 = (1 - np.log(ns2)/logNt) * mu2[1:Nt+1]
    vn = np.sum(coeff2 * ns2**(-0.5) * np.exp(-1j*5*np.log(ns2)))
    zeta_val = complex(mp.zeta(0.5 + 5j))
    print(f"N={Nt}: |1-ζV_N| = {abs(1-zeta_val*vn):.4f}")

print("\n=== 离轴零点的经典 ψ 签名 (x^{σ₀}) - 可见性 ===")
# 若有离轴零点 σ₀+iγ₀, ψ(x)-x 的主振荡 ~ x^{σ₀}/γ₀ (4重奏右侧)
# 相对误差 ~ x^{σ₀-1}/γ₀ - 何时超过可观测阈值?
for sigma0 in [0.51, 0.55, 0.6, 0.7]:
    for gamma0 in [10**3, 10**6]:
        # 需要 x^{σ₀-1}/γ₀ ~ 1e-6 (可观测?) -> x = (γ₀·1e-6)^{1/(1-σ₀)}
        if sigma0 < 1:
            x_req = (gamma0 * 1e-6)**(1/(1-sigma0))
            print(f"σ₀={sigma0:.2f} γ₀={gamma0:.0e}: 相对偏差 1e-6 需要 x ~ {x_req:.2e}")
