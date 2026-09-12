#!/usr/bin/env python3
"""扩展验证: K = 1/(1+x²) 的边际守恒——大 N + 排除密度效应
λ_N^req = -2Σ_{j<N}1/(1+(γ_N-γ_j)²)
如果 ~常数（不随 γ_N 的密度 ρ(γ_N)~log(γ)/2π 变——）→ 真守恒信号
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')

def lam_req_at(idx):
    """γ_idx 的 λ = -2Σ_{j<idx}1/(1+(γ_idx-γ_j)²)——用截断（近的精确——远的渐近——）"""
    g = z[idx]
    # 近的（|d| < 500——）精确
    lo = max(0, idx - 3000)
    gs = z[lo:idx]
    d = g - gs
    near = np.sum(1.0/(1+d*d))
    # 远的（j < lo——）用渐近 Σ 1/d² ~ ∫ρ(y)/(g-y)² dy——小——直接算（分块——）
    # 远的贡献: Σ_{j<lo}1/(1+(g-γ_j)²) ≈ Σ 1/(g-γ_j)²——用粗块
    far = 0.0
    block = 500
    for b in range(0, lo, block):
        gb = z[b:b+block]
        db = g - gb
        far += np.sum(1.0/(db*db))
    return -2*(near + far)

print('=== λ_N^req(1/(1+x²)) 大 N 验证 ===')
print('（密度 ρ(γ) = log(γ/2π)/(2π)——随 γ 增长——如果 λ 常数——非密度效应——）')
idxs = [1000, 5000, 10000, 20000, 50000, 100000, 200000, 400000]
for i in idxs:
    lam = lam_req_at(i)
    g = z[i]
    rho = log(g/(2*pi))/(2*pi)
    print(f'  零点{i}: γ={g:.0f}——ρ={rho:.4f}——λ_req={lam:+.3f}')
