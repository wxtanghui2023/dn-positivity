#!/usr/bin/env python3
"""构造+验证：波包面积的精确递推候选（NS 层递推类比——OpenAI 风格——）"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 200000
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
areas = []; lens = []; gpos = []; mid_g = []
for i in range(len(bounds)-1):
    a, b = bounds[i], bounds[i+1]
    if b - a >= 1:
        areas.append(M_inc[a:b].sum())
        lens.append(b-a)
        gpos.append(z[b-1])
        mid_g.append(z[(a+b)//2])
areas = np.array(areas); lens = np.array(lens); gpos = np.array(gpos)
mid_g = np.array(mid_g)
N = len(areas)
a_abs = np.abs(areas)
sig_areas = np.sign(areas)

print('=== 构造+验证：波包面积精确递推候选 ===')
print()
print('候选1: 比值 r_k = |a_{k+1}|/|a_k| 结构:')
r = a_abs[1:]/np.maximum(a_abs[:-1], 1e-9)
print(f'  mean={r.mean():.4f} 中位={np.median(r):.4f} std={r.std():.4f}')
for i in range(0, N-1, 10000):
    seg = r[i:i+10000]
    print(f'  k={i}-{i+10000}: mean r={seg.mean():.4f}')

print()
print('候选2: |面积| vs 波包长度:')
for L in [1,2,3,4,5,6,8,10,12]:
    m = lens == L
    if m.sum() > 100:
        print(f'  长度{L}: mean|面积|={a_abs[m].mean():.4f} n={m.sum()}')

print()
print('候选3: 面积符号的相位来源:')
best2 = best3 = 0
for phi in np.linspace(0, 2*pi, 40):
    c2 = abs(np.corrcoef(sig_areas, np.sin(mid_g*log(2) + phi))[0,1])
    c3 = abs(np.corrcoef(sig_areas, np.sin(mid_g*log(3) + phi))[0,1])
    best2 = max(best2, c2); best3 = max(best3, c3)
print(f'  面积符号 vs sin(g*log2+phi): {best2:.3f}')
print(f'  面积符号 vs sin(g*log3+phi): {best3:.3f}')

print()
print('候选4: M(交替和) 的锁相:')
alt = np.cumsum(areas)
best4 = 0
for phi in np.linspace(0, 2*pi, 40):
    c = abs(np.corrcoef(alt, np.sin(mid_g*log(2) + phi))[0,1])
    best4 = max(best4, c)
print(f'  M vs sin(g*log2+phi): {best4:.3f}')

# 候选5：面积符号 vs 波包长度的奇偶/其他离散结构
print()
print('候选5: 面积符号 vs 波包起始 k 的奇偶:')
sig_at = sig_areas
# 波包序号的奇偶
even_k = np.arange(N) % 2 == 0
print(f'  偶数波包为正比例: {np.mean(sig_areas[even_k] > 0):.4f}（期望 0.5——）')
print(f'  奇数波包为正比例: {np.mean(sig_areas[~even_k] > 0):.4f}')
