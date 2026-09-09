#!/usr/bin/env python3
"""Test 4: 74 漂移的来源——模型不完备 vs 测度转换
对照: 同一个模型（Bohr k=1——）——两种测度（零点区间平均 vs 固定窗口——）
如果残差积分都 ~74——模型不完备（k=1 不够——）
如果区间平均 ~1（固定 ~74——）——测度是原因（dS 项——）
"""
import numpy as np
from math import log, pi
from bisect import bisect_right

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

def N0(t):
    if t <= 1: return 0.0
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

primes_t = []
for n in range(2, 100):
    if all(n % p for p in primes_t if p*p <= n):
        primes_t.append(n)

# ===== 测度 1: 零点区间平均（精确——IntN——）=====
dg = np.diff(z)
def IntN0(t):
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar_z = kk - (IntN[1:] - IntN[:-1])/dg
t_mid_z = (z[:-1] + z[1:])/2
T_z = t_mid_z[-1]

# Bohr k=1 模型（零点区间的 Sbar——）
model_z = np.zeros(len(Sbar_z))
for p in primes_t:
    a = np.trapz(Sbar_z * np.sin(t_mid_z*log(p)), t_mid_z)/T_z  # 非均匀 trapz
    model_z += a * np.sin(t_mid_z*log(p))
R_z = Sbar_z - model_z
cumR_z = np.cumsum(R_z * dg)
print('=== Test 4: 测度对照 ===')
print(f'测度1（零点区间平均——）: 残差 std={R_z.std():.4f}——∫R max|={np.max(np.abs(cumR_z)):.3f}——末值={cumR_z[-1]:+.3f}')

# ===== 测度 2: 固定窗口（H≈零点间距的平均 0.7——）=====
def S_at(u):
    k = bisect_right(z, u)
    return k - N0(u)
t0, t1 = 500.0, 60000.0
ds = 0.3
t_grid = np.arange(t0, t1, ds)
S_grid = np.array([S_at(t) for t in t_grid])
for H in [0.7, 1.0]:
    nH = max(1, int(round(H/ds)))
    kernel = np.ones(nH)/nH
    sb = np.convolve(S_grid, kernel, mode='valid')
    tb = t_grid[nH//2 : nH//2 + len(sb)]
    T = tb[-1]
    model = np.zeros(len(tb))
    for p in primes_t:
        a = np.trapz(sb * np.sin(tb*log(p)), tb)/T
        model += a * np.sin(tb*log(p))
    R_f = sb - model
    cumR_f = np.cumsum(R_f) * ds
    print(f'测度2（固定 H={H}——）: 残差 std={R_f.std():.4f}——∫R max|={np.max(np.abs(cumR_f)):.3f}——末值={cumR_f[-1]:+.3f}')

# ===== 测度 3: 零点采样（ΣR(γ_n)——带 dN 权——）=====
# R 在零点处（插值——）
R_at_z = np.interp(z[1:-1], t_mid_z, R_z)  # R 在零点位置的近似
# ΣR(γ_n)·(1/N0'(γ_n)) 类（∫R dN₀ 的——）vs ΣR(γ_n)（dN 的——）
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[1:-1]])
sum_R_dN0 = np.sum(R_at_z / N0p)  # ∫R dN₀ ≈ ΣR(γ)/N0'(γ)·(密度~1——)？——不——直接 ΣR(γ)
sum_R_z = np.sum(R_at_z)
print(f'\n测度3（零点求和——）: ΣR(γ_n)={sum_R_z:+.1f}——（vs ∫R dt 的 ~74——）')
print(f'  ΣR(γ_n)/N0\'(γ_n)（∫R dN₀ 类——）= {sum_R_dN0:+.1f}')
