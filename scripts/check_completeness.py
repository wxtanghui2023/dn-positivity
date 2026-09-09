#!/usr/bin/env python3
"""完备性检验: Sbar = Σ_{all p} a_p sin(t log p)？（纯几乎周期——）还是含非周期部分
加更多素数（P 增——）——残差方差/积分的行为——如果残差→0——展开完备——
如果残差饱和（不可约——）——Sbar 含非周期部分（其积分 O(1) 需另证——）
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
M_inc = Sbar * dg
t_mid = (z[:-1] + z[1:])/2

# 素数列表（到 200——）
primes = []
for n in range(2, 200):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)

print('=== 完备性检验: Sbar 的几乎周期展开 ===')
print(f'Sbar 方差: {Sbar.var():.4f}——std: {Sbar.std():.4f}')

# 逐步加素数——看残差
for P_count in [3, 6, 10, 15, 20, 30, 40, 46]:
    ps = primes[:P_count]
    cols = []
    for p in ps:
        cols.append(np.sin(t_mid * log(p)))
        cols.append(np.cos(t_mid * log(p)))
    X = np.stack(cols, axis=1)
    coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)
    fit = X @ coef
    resid = Sbar - fit
    # 残差的积分（M 的贡献——）
    resid_M = np.cumsum(resid * dg)
    print(f'  P≤{ps[-1]:3d} ({P_count}素数): 残差std={resid.std():.4f}——'
          f'R²={1-resid.var()/Sbar.var():.4f}——∫R max|={np.max(np.abs(resid_M)):.3f}')

# 残差的频谱（看是否还有"未拟合的峰"——还是平坦噪声——）
print()
print('残差频谱（P≤200 后——）——看是否有结构峰:')
ps = primes  # 46 个到 199
cols = []
for p in ps:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
X = np.stack(cols, axis=1)
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)
fit = X @ coef
resid = Sbar - fit
print(f'  P≤199 残差 std={resid.std():.4f}——R²={1-resid.var()/Sbar.var():.4f}')
# 残差的自相关（看结构——）
for lag in [1, 2, 5, 10, 20]:
    c = np.corrcoef(resid[:-lag], resid[lag:])[0,1]
    print(f'  残差 ρ({lag}) = {c:+.4f}')
