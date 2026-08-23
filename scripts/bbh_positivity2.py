#!/usr/bin/env python3
"""BBH 有效正定（修复版）：自己实现 Hurwitz ζ（欧拉-麦克劳林）
ψ_z(x) = ζ(z, x+1)——EM 公式（Re z = ½ > 0——适用）
⟨η̂⟩ = (1/2)(1 − Re[overlap])——overlap = 平移重叠比（正则化）
"""
import numpy as np
import gc
from math import log, pi, factorial

# Bernoulli 数（前几个）
BERNOULLI = [1, -1/2, 1/6, 0, -1/30, 0, 1/42, 0, -1/30, 0, 5/66, 0, -691/2730, 0, 7/6, 0, -3617/510, 0, 43867/798, 0, -174611/330]

def hurwitz_zeta(z, x, N=50, K=8):
    """Hurwitz ζ(z,x)——欧拉-麦克劳林（Re z > 0）"""
    z = complex(z)
    # Σ_{n=0}^{N-1}(x+n)^{-z}
    total = sum((x+n)**(-z) for n in range(N))
    # 积分项：(x+N)^{1-z}/(z−1)
    total += (x+N)**(1-z)/(z-1)
    # ½(x+N)^{-z}
    total += 0.5*(x+N)**(-z)
    # EM 余项：Σ B_{2k}/(2k)!·(z)_{2k-1}·(x+N)^{-z-2k+1}
    for k in range(1, K+1):
        if k >= len(BERNOULLI): break
        b2k = BERNOULLI[2*k] if 2*k < len(BERNOULLI) else 0
        if b2k == 0: continue
        # (z)_{2k-1} = z(z+1)...(z+2k-2)（升阶乘）
        poch = 1.0
        for j in range(2*k-1):
            poch *= (z + j)
        total += b2k/factorial(2*k) * poch * (x+N)**(-z-2*k+1)
    return total

# 零点
zeros = []
with open('/home/node/.openclaw/workspace/dn-project/zeros/zeros6') as f:
    for i in range(8):
        zeros.append(float(f.readline()))
zeros = np.array(zeros)

def psi(z, x):
    return hurwitz_zeta(z, x+1.0)

from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(16)

def overlap_ratio(z, L=30, nsub=60):
    num = 0.0
    den = 0.0
    for i in range(nsub):
        lo = L*i/nsub
        hi = L*(i+1)/nsub
        ts = 0.5*(hi-lo)*xg + 0.5*(hi+lo)
        p1 = psi(z, ts)
        p2 = psi(z, ts+1.0)
        num += 0.5*(hi-lo)*np.sum(wg*np.conj(p1)*p2)
        den += 0.5*(hi-lo)*np.sum(wg*np.abs(p1)**2)
    return num/den if den != 0 else 0

print("Hurwitz ζ 验证（ζ(2,1) = π²/6 ≈ 1.6449——ζ(0.5+14.135i, 1.5)）：")
print(f"  ζ(2,1) = {hurwitz_zeta(2, 1):.6f}（π²/6 = {pi**2/6:.6f}）")
print(f"  ζ(0.5,1) = {hurwitz_zeta(0.5, 1):.4f}（ζ(0.5) ≈ −1.460——应该接近）")

print("\nBBH 有效正定：⟨η̂⟩_z = (1/2)(1 − Re[overlap])：")
print(f"{'零点 γ':>8} {'Re[overlap]':>12} {'⟨η̂⟩':>10} {'有效正定？':>10}")
for gam in zeros:
    z = 0.5 + 1j*gam
    ov = overlap_ratio(z, L=20, nsub=40)
    eta = 0.5*(1 - ov.real)
    print(f"{gam:8.3f} {ov.real:+12.6f} {eta:10.6f} {'✓ 是' if eta > 0 else '✗ 否'}")

del zeros
gc.collect()
print("内存已释放")
