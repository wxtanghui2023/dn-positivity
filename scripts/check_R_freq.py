#!/usr/bin/env python3
"""验证: 残差 R 的频率含量——高频（尾部素数 log p > 5.3——）主导？
如果 R 是高频（尾部——）——积分有界平凡（Σ 收敛——）
如果 R 有低频成分（非尾部——）——低频积分 O(1) 需另解——
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

# 拟合 P≤199
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

print('=== 残差 R 的频率含量 ===')
print(f'R std={R.std():.4f}——log p > 5.3 对应 p > 199（高频——）')

# 在 t 空间（实际高度——）的谱——R 的高频含量
# R 是区间序列（k——）——用 t_mid 插值到均匀网格——FFT
t_unif = np.linspace(t_mid[0], t_mid[-1], 50000)
R_unif = np.interp(t_unif, t_mid, R)
R_unif = R_unif - R_unif.mean()
spec = np.abs(np.fft.fft(R_unif * np.hanning(len(R_unif))))**2
freqs = np.fft.fftfreq(len(R_unif), t_unif[1]-t_unif[0])
pos = freqs > 0

# 累计功率 vs 频率（log p 阈值——）
cum_power = np.cumsum(spec[pos]) / spec[pos].sum()
# log2 = 0.69——log199 = 5.3——log1000 = 6.9——log200 = 5.3
for f_th in [0.69, 1.1, 1.6, 2.0, 3.0, 4.0, 5.3, 7.0]:
    frac = cum_power[np.searchsorted(freqs[pos], f_th)] if np.searchsorted(freqs[pos], f_th) < len(cum_power) else 1.0
    print(f'  频率 < {f_th:.1f}（p < {np.exp(f_th):.0f}——）: 功率占比 {frac:.3f}')

# 残差在低频（< log 199 = 5.3——）的功率——如果有——是"非尾部"成分
print()
print('关键: 残差中 p < 199 的功率占比（应为 0 如果拟合完备——）')
# 检验: R 与已拟合的 sin(t log p) 正交吗（应该——最小二乘——）
# 泄漏检验: R 与 p=200-1000 的 sin 的相关（未拟合的尾部——）
print('R 与未拟合素数 sin 的相关（泄漏——）:')
for p_test in [200, 300, 500, 1000]:
    c = np.corrcoef(R, np.sin(t_mid * log(p_test)))[0,1]
    c2 = np.corrcoef(R, np.cos(t_mid * log(p_test)))[0,1]
    print(f'  p={p_test}: sin 相关={c:+.3f}——cos 相关={c2:+.3f}')

# R 的积分贡献（分段——看是否随区间增长——）
cumR = np.cumsum(R * dg)
print()
print('∫R 分段（增长?——）:')
for i in range(0, K, 20000):
    print(f'  零点{i}: ∫R={cumR[i]:+.3f}')
