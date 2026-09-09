#!/usr/bin/env python3
"""R 的谱分析（k 空间直接 FFT——）——找 R 的来源频率
R 非尾部（泄漏~0）非 δ（相关~0）——它的谱结构？
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 100000
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
t_mid = (z[:-1] + z[1:])/2

primes = []
for n in range(2, 200):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)
cols = []
for p in primes:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
X = np.stack(cols, axis=1)
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)
R = Sbar - X @ coef

print('=== R 的 k 空间谱 ===')
# k 空间直接 FFT（R 是区间序列——k 序数——）
N = len(R)
Rc = R - R.mean()
spec = np.abs(np.fft.fft(Rc * np.hanning(N)))**2
freqs = np.fft.fftfreq(N)
pos = freqs > 0

# 找主峰（排除 DC——）
spec_pos = spec[pos]
fr_pos = freqs[pos]
# 前 10 峰
top = np.argsort(spec_pos)[-10:][::-1]
print('主峰（k 空间频率——周期——）:')
for idx in top:
    f = fr_pos[idx]
    print(f'  频率={f:.5f}/k——周期={1/f:.1f} k——功率={spec_pos[idx]:.1f}（占比 {spec_pos[idx]/spec_pos.sum():.4f}）')

# 累计功率——低频 vs 高频
cum = np.cumsum(spec_pos)/spec_pos.sum()
print()
print('功率分布:')
for f_th, name in [(0.01, '周期>100k'), (0.02, '周期>50k'), (0.05, '周期>20k'), (0.1, '周期>10k'), (0.2, '周期>5k'), (0.3, '周期>3.3k')]:
    idx = np.searchsorted(fr_pos, f_th)
    print(f'  {name}: 功率 {cum[idx] if idx < len(cum) else 1.0:.3f}')

# R 的逐点结构——R 与 Sbar 波包的边界（翻转点）的关系
print()
print('R 的结构（与 Sbar 的关系——）:')
signs = np.sign(Sbar)
flips = np.where(signs[:-1] != signs[1:])[0] + 1
# R 在翻转点附近 vs 远离
R_abs = np.abs(R)
near = np.zeros(len(R), dtype=bool)
for f in flips:
    near[max(0,f-3):min(len(R),f+3)] = True
print(f'  R 在翻转点附近 mean|R|={R_abs[near].mean():.4f}——远离 mean|R|={R_abs[~near].mean():.4f}')

# R 的直方图（分布形状——）
print(f'  R 分布: mean={R.mean():+.4f}——std={R.std():.4f}——偏度={((R-R.mean())**3).mean()/R.std()**3:+.2f}——峰度={((R-R.mean())**4).mean()/R.std()**4:.1f}')
