#!/usr/bin/env python3
"""ρ(lag) 的精确衰减律——方差压缩的结构
Σρ → −½ 的收敛速度——ρ(lag) ~ ?（1/lag²? 指数? 振荡?）
Σlag·ρ(lag) 的收敛（= Var(P_N) 的——O(1) 需要——）
"""
import numpy as np
from math import log, pi

z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = min(len(z), 200000)
z = z[:K]

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
S_z = np.arange(1, K) - N0v
dS = np.diff(S_z)
N = len(dS)

print('=== ρ(lag) 衰减律 ===')
# 用 FFT 相关（快——）
dS_c = dS - dS.mean()
# 自相关（FFT 方法——）
f = np.fft.fft(dS_c, n=2*N)
acf = np.fft.ifft(f * np.conj(f)).real[:N] / (N * dS_c.var())
rho = acf / acf[0]

# 采样 ρ(lag) 的对数（衰减律——）
print('ρ(lag) 采样:')
for lag in [1, 2, 3, 5, 10, 20, 50, 100, 200, 500]:
    print(f'  lag={lag:4d}: ρ={rho[lag]:+.6f}')

# 衰减律拟合（|ρ| ~ C/lag^α?）
print()
print('|ρ| 的衰减指数（log|ρ| vs log lag——）:')
for lo, hi in [(1, 10), (10, 100), (100, 500)]:
    lags = np.arange(lo, hi+1)
    vals = np.abs(rho[lags])
    if vals.min() > 0:
        alpha = -np.polyfit(np.log(lags), np.log(vals), 1)[0]
        print(f'  lag∈[{lo},{hi}]: α≈{alpha:.3f}（|ρ| ~ lag^(-α)——）')

# Σρ 和 Σlag·ρ 的收敛
print()
cum_rho = 0
cum_lag_rho = 0
for lag in range(1, N):
    cum_rho += rho[lag]
    cum_lag_rho += lag * rho[lag]
    if lag in [10, 50, 100, 200, 500, 1000, 5000, 20000]:
        print(f'  lag≤{lag}: Σρ={cum_rho:+.5f}——Σlag·ρ={cum_lag_rho:+.3f}')

# Var(P_N) 的直接（对照——）
P_N = np.cumsum(dS_c)
print(f'\nVar(P_N)（直接——）: {P_N[-1]**2/len(P_N):.4f}（用末值——不对——用均方——）')
print(f'P_N 均方: {np.mean(P_N**2):.4f}')
print(f'理论 Var ~ σ²[N(1+2Σρ) - 2Σlag·ρ]——σ²={dS_c.var():.4f}——')
