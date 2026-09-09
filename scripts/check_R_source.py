#!/usr/bin/env python3
"""R 的 6.4k 周期来源: 波包结构? Sbar 谐波? 拍频?
检验:
1. R 是否 ~ 波包边界的效应（翻转点——）
2. R 是否含 Sbar 的谐波（2×log p——）或拍频（log p - log q——）
3. R 的周期随高度漂移吗（像 log 频率的坐标效应——还是固定 k 周期——）
"""
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

print('=== R 的 6.4k 周期来源 ===')

# 1. 分段谱——6.4k 周期随高度漂移?
print('1. R 的分段主周期（k 空间——随高度漂移?）:')
for i0 in range(0, 150000, 30000):
    Rseg = R[i0:i0+30000]
    Rseg = Rseg - Rseg.mean()
    spec = np.abs(np.fft.fft(Rseg * np.hanning(len(Rseg))))**2
    fr = np.fft.fftfreq(len(Rseg))
    pos = fr > 0
    pk = fr[pos][np.argmax(spec[pos])]
    print(f'  k={i0}-{i0+30000} (γ~{z[i0]:.0f}): 主周期={1/pk:.2f} k——频率={pk:.4f}')

# 2. R 与候选信号的比较: 谐波（2 log p——）拍频（log p − log q——）
print()
print('2. R 与候选频率的相关（拟合幅度——）:')
cands = {
    '2·log2': 2*log(2), '2·log3': 2*log(3), 'log3-log2': log(3)-log(2),
    'log5-log2': log(5)-log(2), 'log7-log3': log(7)-log(3),
    'log2+log3': log(2)+log(3), '1.5·log2': 1.5*log(2),
}
# 用 k 空间（t_mid 与 k 的关系——近似 log 频率的 k 空间 = log p/log γ 类——）
# 直接在 t 空间拟合 R（低频——R 的 k 空间 6.4 周期 ~ t 空间什么频率?）
# Δγ ~ 2π/log γ——k 空间 6.4 周期对应 t 空间 Δt ~ 6.4·2π/log γ——频率 ~ log γ/6.4
for name, w in cands.items():
    # t 空间拟合
    cols = [np.sin(t_mid * w), np.cos(t_mid * w)]
    Xc = np.stack(cols, axis=1)
    c, _, _, _ = np.linalg.lstsq(Xc, R, rcond=None)
    amp = np.hypot(c[0], c[1])
    print(f'  {name} (ω={w:.3f}): 拟合幅度={amp:.5f}（vs R std 0.064——）')

# 3. R 与波包边界（翻转点——）的精确关系
print()
print('3. R 与翻转点的关系:')
signs = np.sign(Sbar)
flips = np.where(signs[:-1] != signs[1:])[0] + 1
# 构造'翻转指示'信号（翻转点处 ±——）
flip_signal = np.zeros(len(R))
# 每个翻转点: R 在翻转后的行为——平均 R 的'段模式'
# 段的模式（相对翻转——）
seg_patterns = []
for f in flips[:20000]:
    # 翻转点前 10 和后 10 的 R
    if f > 10 and f < len(R)-10:
        seg_patterns.append(R[f-10:f+10])
seg_patterns = np.array(seg_patterns)
mean_pat = seg_patterns.mean(axis=0)
print('  翻转点附近 R 的平均模式（-10..+10——）:')
print('  ' + ' '.join(f'{v:+.4f}' for v in mean_pat))
