#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# BNBD 通道测试 1: 真实 ζ 的 d_N² 基线 (在线)
# d_N² = (1/2π)∫|1-ζ(½+it)V_N(½+it)|² dt/(¼+t²)
# V_N(s) = Σ_{n≤N} (1-logn/logN)μ(n)/n^s (Bettin-Conrey-Farmer 最优)
# 预期 (Burnol): d_N² ~ C/log N, C = 2+γ-log4π ≈ 0.079...
import numpy as np
import mpmath as mp

def mobius_sieve(N):
    """筛 μ(n) 到 N"""
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

def dN2(N, mu, t_max=60, n_pts=400):
    """d_N²: (1/2π)∫|1-ζV_N|² dt/(¼+t²)
    V_N(½+it) = Σ_{n≤N}(1-logn/logN)μ(n)n^{-½-it}
    用 mpmath 算 ζ(½+it)"""
    # 预计算 V_N 系数
    logN = np.log(N)
    ns = np.arange(1, N+1)
    coeff = (1 - np.log(ns)/logN) * mu[1:N+1]
    coeff = coeff.astype(np.complex128)
    
    # 积分点 (t 网格)
    ts = np.linspace(-t_max, t_max, n_pts)
    dt = ts[1] - ts[0]
    
    total = 0.0
    # 分块计算 (避免内存爆炸)
    for t in ts:
        # ζ(½+it) 用 mpmath
        zeta_val = complex(mp.zeta(0.5 + 1j*t))
        # V_N(½+it) = Σ coeff_n · n^{-½-it}
        # n^{-½-it} = n^{-½}·e^{-it log n}
        logns = np.log(ns)
        vn = np.sum(coeff * ns**(-0.5) * np.exp(-1j*t*logns))
        val = 1 - zeta_val * vn
        weight = 1.0/(0.25 + t*t)
        total += abs(val)**2 * weight * dt
    return total / (2*np.pi)

if __name__ == "__main__":
    mp.mp.dps = 30
    print("BNBD d_N² 基线测试 (真实 ζ - 在线)")
    print(f"预期 Burnol 常数 C = 2+γ-log4π = {2+0.5772156649015329-np.log(4*np.pi):.6f}")
    
    Nmax = 20000
    print(f"筛 μ 到 {Nmax}...")
    mu = mobius_sieve(Nmax)
    print("完成")
    
    print(f"\n{'N':>8} {'d_N²':>14} {'d_N²·logN':>14} {'C/logN 预测':>14}")
    for N in [100, 500, 1000, 2000, 5000, 10000, 20000]:
        d2 = dN2(N, mu)
        C = 2 + 0.5772156649015329 - np.log(4*np.pi)
        print(f"{N:>8} {d2:>14.6e} {d2*np.log(N):>14.6f} {C/np.log(N):>14.6e}")
