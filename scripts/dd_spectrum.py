#!/usr/bin/env python3
"""追 Δδ 可预测性的来源: 谱结构 + 与已知量（dS/S——）的关系
1. Δδ 的 FFT 谱（低频峰? 准周期?——）
2. Δδ 与 dS（=1-ΔN0——）/S 的关系——又是零点读出?
3. 结构 vs 纯统计（dS 的 AR——对照——）
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = 100000
z = z[:K]
dg = np.diff(z)
N0v = np.array([(t/(2*pi))*(log(t/(2*pi))-1)+7.0/8 for t in z[:-1]])
S_right = np.arange(1, K) - N0v
dS = np.diff(S_right)  # ΔS
N0pv = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
d = (dg - 1.0/N0pv)[:K-1]
dd = np.diff(d)

# 1. Δδ 的谱
print('=== Δδ 的 FFT 谱 ===')
L = len(dd)
spec = np.abs(np.fft.rfft(dd - dd.mean()))**2
freqs = np.fft.rfftfreq(L)
# 找主峰（排除 DC——）
spec[0] = 0
top = np.argsort(spec)[-5:][::-1]
print('主频（周期——）:')
for i in top:
    print(f'  频率 {freqs[i]:.5f}——周期 {1/freqs[i] if freqs[i]>0 else 0:.1f} 零点——能量占比 {spec[i]/spec.sum():.4f}')
# 低频集中度
low_frac = spec[freqs < 0.01].sum()/spec.sum()
print(f'低频（周期>100）能量占比: {low_frac:.4f}')

# 2. Δδ vs dS 的关系
print()
print('=== Δδ 与 dS 的关系 ===')
print(f'corr(Δδ, dS) = {np.corrcoef(dd, dS[1:])[0,1]:+.4f}')
print(f'corr(Δδ, dS[:-1]) = {np.corrcoef(dd, dS[:-1])[0,1]:+.4f}')

# dS 的差分可预测性（对照——）
print()
print('=== dS 的差分（对照——）===')
ddS = np.diff(dS)
def ar_r2(seq, k, split=None):
    n = len(seq) - k
    X = np.empty((n, k))
    for j in range(k):
        X[:, j] = seq[j:n+j]
    y = seq[k:n+k]
    XtX = X.T @ X + np.eye(k)*1e-8
    coef = np.linalg.solve(XtX, X.T @ y)
    pred = X @ coef
    return 1 - np.sum((y-pred)**2)/np.sum((y-y.mean())**2)
for k in [2, 5, 10, 20]:
    print(f'  ΔdS AR({k}): R²={ar_r2(ddS, k):.4f}')

# Δδ 与 ΔdS 的相关（如果 ~1——同结构——）
print(f'corr(Δδ, ΔdS) = {np.corrcoef(dd, ddS)[0,1]:+.4f}')

# 3. Δδ 的可预测性是否 = S 的高阶（显式公式读出——）?
# δ ≈ -ΔS/N0'——Δδ ≈ -(Δ²S·N0' - ΔS·N0'')/N0'²——近似 Δ²S/N0' 主导——
print()
print('=== Δδ ≈ -Δ²S/N0\' 的检验 ===')
approx = -np.diff(dS, 2)/N0pv[1:-1]
print(f'corr(Δδ, -Δ²S/N0\') = {np.corrcoef(dd, approx)[0,1]:+.4f}')
