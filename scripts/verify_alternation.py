#!/usr/bin/env python3
"""验证完美交替的精确性 + 符号翻转驱动（log3 相位——）"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 400000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z[:K])
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
M_inc = Sbar * dg

signs = np.sign(Sbar)
flips = np.where(signs[:-1] != signs[1:])[0] + 1
bounds = np.concatenate([[0], flips, [len(Sbar)]])
areas = []; lens = []; start_k = []; mid_g = []
for i in range(len(bounds)-1):
    a, b = bounds[i], bounds[i+1]
    if b - a >= 1:
        areas.append(M_inc[a:b].sum())
        lens.append(b-a)
        start_k.append(a)
        mid_g.append(z[(a+b)//2])
areas = np.array(areas); lens = np.array(lens)
start_k = np.array(start_k); mid_g = np.array(mid_g)
N = len(areas)
sig = np.sign(areas)

print('=== 验证完美交替的精确性（400k 零点——）===')
print(f'波包数: {N}')
# 面积符号 vs (−1)^k（k = 波包序号——）或 vs (−1)^{起始零点位置——}？
# 波包起始位置 start_k（零点序数——）——面积符号 vs (−1)^{start_k}?
alt1 = np.array([(-1)**k for k in range(N)])
match1 = np.mean(sig == alt1)
print(f'面积符号 == (−1)^k（波包序号——）: {match1:.6f}')

# 更自然的: 面积符号 vs (−1)^{start_k}（起始零点序数的奇偶——）
alt2 = np.array([(-1)**sk for sk in start_k])
match2 = np.mean(sig == alt2)
print(f'面积符号 == (−1)^(起始零点序数): {match2:.6f}')

# 或者: 面积的符号由'正负区间的长度'决定——第一个区间的符号——
# 检验: 面积符号与 Sbar[start_k]（波包起始的 Sbar 符号——）的关系
Sbar_start = Sbar[start_k]
match3 = np.mean(sig == np.sign(Sbar_start))
print(f'面积符号 == Sbar(波包起始)符号: {match3:.6f}')

# 符号翻转的驱动：什么时候波包长度>1（符号在波包内变——）
print()
print('=== 符号翻转驱动分析 ===')
# 面积符号 vs log3 相位（在波包边界——）
# 翻转点 = flips——看翻转点的相位
flip_g = z[flips]  # 翻转处的 γ
phi3 = (flip_g * log(3)) % (2*pi)
phi2 = (flip_g * log(2)) % (2*pi)
# 翻转点的相位分布（应该集中——如果相位驱动翻转——）
print('翻转点相位分布（log3——）:')
h, edges = np.histogram(phi3, bins=8, range=(0, 2*pi))
print('  ' + ' '.join(f'{h[i]:6d}' for i in range(8)))
print('  均匀期望: ', len(phi3)/8)
h2, _ = np.histogram(phi2, bins=8, range=(0, 2*pi))
print('翻转点相位分布（log2——）:')
print('  ' + ' '.join(f'{h2[i]:6d}' for i in range(8)))

# 长度>1 的波包——内部有符号翻转——面积符号 vs 翻转次数
print()
print(f'长度分布: 1={np.sum(lens==1)} 2={np.sum(lens==2)} 3={np.sum(lens==3)} >=4={np.sum(lens>=4)}')

# M 的精确锁相验证：M(波包边界) vs A*sin(g*log2+phi)——拟合
alt = np.cumsum(areas)
# 拟合 M = A*sin(g*log2) + B*cos(g*log2) + C
X = np.stack([np.sin(mid_g*log(2)), np.cos(mid_g*log(2)), np.ones_like(mid_g)], axis=1)
coef, _, _, _ = np.linalg.lstsq(X, alt, rcond=None)
fit = X @ coef
resid = alt - fit
print()
print('=== M 的 log2 锁相拟合 ===')
print(f'  M = {coef[0]:+.3f}·sin(g·log2) {coef[1]:+.3f}·cos(g·log2) {coef[2]:+.3f}')
print(f'  |M| max={np.max(np.abs(alt)):.3f}——拟合残差 max={np.max(np.abs(resid)):.3f}——std={resid.std():.3f}')
print(f'  拟合 R² = {1 - resid.var()/alt.var():.4f}')
