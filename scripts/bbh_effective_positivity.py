#!/usr/bin/env python3
"""BBH 有效正定：η̂ = sin²(p̂/2) 在零点本征态中的期望
ψ_z(x) = ζ(z, x+1)（Hurwitz ζ——BBH 本征函数）
sin²(p̂/2) = (1/4)(2 − e^{ip̂} − e^{-ip̂})——e^{ip̂} = 平移 +1
⟨η̂⟩ = (1/2)(1 − Re[overlap])——overlap = ⟨ψ_z|T|ψ_z⟩/⟨ψ_z|ψ_z⟩（正则化）
验证：⟨η̂⟩ > 0（有效正定——谱实——RH 方向）
"""
import numpy as np
import gc
from scipy.special import zeta as hurwitz

# 零点（前几个）
zeros = []
with open('/home/node/.openclaw/workspace/dn-project/zeros/zeros6') as f:
    for i in range(8):
        zeros.append(float(f.readline()))
zeros = np.array(zeros)

def psi(z, x):
    """BBH 本征函数：ψ_z(x) = ζ(z, x+1)——Hurwitz ζ"""
    x = np.asarray(x, dtype=float)
    return hurwitz(z, x + 1.0)

# 正则化的 ⟨η̂⟩：带截断 L 和权重（x 大处 ψ ~ x^{-1/2}——发散——需权重）
# overlap_ratio = ∫_0^L ψ*(x)ψ(x+1)dx / ∫_0^L |ψ(x)|²dx
# 用数值积分（高精度）
from numpy.polynomial.legendre import leggauss
xg, wg = leggauss(16)

def overlap_ratio(z, L=50, nsub=100):
    """平移重叠比（正则化）"""
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

print("BBH 有效正定：⟨η̂⟩_z = (1/2)(1 − Re[overlap]) 在零点本征态：")
print(f"{'零点 γ':>8} {'Re[overlap]':>12} {'⟨η̂⟩':>10} {'有效正定？':>10}")
for gam in zeros:
    z = 0.5 + 1j*gam
    ov = overlap_ratio(z, L=30, nsub=60)
    eta = 0.5*(1 - ov.real)
    print(f"{gam:8.3f} {ov.real:+12.6f} {eta:10.6f} {'✓ 是' if eta > 0 else '✗ 否'}")

# L 依赖（收敛性检验）
print("\n⟨η̂⟩ 的 L 依赖（收敛性——γ₁）：")
for L in [10, 20, 50, 100]:
    ov = overlap_ratio(0.5+1j*zeros[0], L=L, nsub=80)
    eta = 0.5*(1 - ov.real)
    print(f"  L={L:4d}: Re[overlap] = {ov.real:+.6f}  ⟨η̂⟩ = {eta:.6f}")

# 大 γ 检验（本征态更"振荡"——overlap 更小？）
print("\n大 γ 的 ⟨η̂⟩（更高零点）：")
for gam in [100, 500, 1000]:
    ov = overlap_ratio(0.5+1j*gam, L=30, nsub=60)
    eta = 0.5*(1 - ov.real)
    print(f"  γ={gam:5d}: Re[overlap] = {ov.real:+.6f}  ⟨η̂⟩ = {eta:.6f}")

del zeros
gc.collect()
print("内存已释放")
