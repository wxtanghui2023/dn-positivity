#!/usr/bin/env python3
"""归一化 theta 残差测试——塔 Q ⊂ L=Q(√2) ⊂ M=Q(√2,√3)
R(t) = log[Θ_{Ô_M}(t)/Θ_{Ô_L^r}(t)]——Ô = covolume 归一化
——看 R(t) 是否有稳定内生符号（→ 可能的正性候选）还是交叉（→ 死）
"""
import numpy as np
from math import exp, pi, log, sqrt

def theta_lattice(points_fn, dim, covol_sq, t, Rmax):
    """Θ(t) = Σ_{x∈格} e^{-πt|x|²}——x 归一化（covol 1——）——截断 |x| ≤ Rmax（原尺度——）"""
    # 归一化缩放：原格 covol² = covol_sq——归一化（covol²=1）→ 缩放 s = covol_sq^{-1/dim}
    # |x|² → |x|²/covol_sq^{2/dim}——Θ_Ô(t) = Σ e^{-πt |x|² / covol_sq^{2/dim}}
    s = covol_sq**(-1.0/dim)  # 归一化缩放（|x|² → s²|x|²——s² = covol_sq^{-2/dim}）
    total = 0.0
    cnt = 0
    for x2 in points_fn(Rmax):
        # x2 = |x|²（原尺度——）
        total += exp(-pi*t*x2*s*s)
        cnt += 1
    return total, cnt

# ===== L = Q(√2)——格（Minkowski ℝ²——）点 (a+b√2, a−b√2)——|x|² = 2a²+4b² = 2(a²+2b²) =====
s2 = sqrt(2.0)
def L_points(Rmax):
    # a²+2b² ≤ Rmax²/2——枚举
    out = []
    amax = int(Rmax/sqrt(2))+1
    bmax = int(Rmax/2)+1
    for a in range(-amax, amax+1):
        for b in range(-bmax, bmax+1):
            x2 = 2*(a*a + 2*b*b)
            if x2 <= Rmax*Rmax:
                out.append(x2)
    return out
covol_L2 = 8.0  # Δ_L = 8（covol² = |Δ|——对全实——）

# ===== M = Q(√2,√3)——格（ℝ⁴——）点 (共轭——) =====
s3 = sqrt(3.0)
s6 = sqrt(6.0)
def M_points(Rmax):
    out = []
    amax = int(Rmax)+1
    for a in range(-amax, amax+1):
        for b in range(-amax, amax+1):
            for c in range(-amax, amax+1):
                for d in range(-amax, amax+1):
                    # 4 共轭：a ± b√2 ± c√3 ± d√6——|x|²（Minkowski）= Σ σ_i(x)² = 4a²+8b²+12c²+24d²
                    # （Tr(x²)——从 Gram 对角（4,8,12,24）——但那是基的——x = a+...+d√6——|x|² = Σσ²
                    # σ 和 = 4(a²+2b²+3c²+6d²)？——算：Σ_±± (a+s2sb+s3sc+s2s3s6d)² 展开 = 4a²+4·2b²·？——直接用 Tr(x·conj x)=Tr(x²)
                    # Minkowski |x|² = Σ_k σ_k(x)² = 4a² + 4·2b² + 4·3c² + 4·6d²（交叉消——）= 4a²+8b²+12c²+24d²
                    x2 = 4*a*a + 8*b*b + 12*c*c + 24*d*d
                    if x2 <= Rmax*Rmax:
                        out.append(x2)
    return out
covol_M2 = 576.0  # Δ_M = 576（应——8²·3²——）

# L² 基准：Θ_{Ô_L²}(t) = Θ_{Ô_L}(t)²（直和——每拷贝归一化 covol² = 8^{1/2}？——
# Ô_L（ℝ²——covol²=1——）= L 缩放——Ô_L²（ℝ⁴——）= (Ô_L)² 直和——covol²（Ô_L²）= 1·1=1 ✓
# 所以 Θ_{Ô_L²}(t) = Θ_{Ô_L}(t)²——Ô_M（ℝ⁴——covol²=1）直接算——

print('=== 归一化 theta 残差 R(t) = log[Θ_ÔM/Θ_ÔL²] ===')
print('（稳定正 → 候选——交叉/混合 → 死——）')
print()
Rmax = 12
LM = L_points(Rmax)
MM = M_points(Rmax)
print(f'L 点数（R≤{Rmax}）= {len(LM)}——M 点数 = {len(MM)}')
for t in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0]:
    th_L, _ = theta_lattice(None, 2, covol_L2, t, Rmax) if False else (sum(exp(-pi*t*x2*covol_L2**(-1.0)) for x2 in LM), 0)
    # 归一化：ℝ²——covol² 8——s² = 8^{-2/2} = 1/8？——covol_sq^{2/dim} = 8^{1} = 8——|x|²/8
    th_Ln = sum(exp(-pi*t*x2/8.0) for x2 in LM)  # Ô_L（covol²=1——缩放 s²=1/8？——det G=8——Ĝ = G/8^{1}——|x|̂²=|x|²/8 ✓
    # Ô_M：ℝ⁴——covol² 576——s² = 576^{-2/4} = 576^{-1/2} = 1/24——|x|²/24
    th_Mn = sum(exp(-pi*t*x2/24.0) for x2 in MM)
    # Ô_L² 基准 = th_Ln²（直和——）
    R = log(th_Mn) - 2*log(th_Ln)
    print(f'  t={t}: Θ_ÔM = {th_Mn:.6f}——Θ_ÔL² = {th_Ln**2:.6f}——R(t) = {R:+.6f}')
