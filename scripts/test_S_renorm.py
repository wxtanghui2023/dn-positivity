#!/usr/bin/env python3
"""A 的最后一关: S-renormalization test（唐先生 13:29——）
E_ren = Σ_{j<k}[log|k-j+δ_k-δ_j| - log(k-j) - (δ_k-δ_j)/(k-j) + ½(δ_k-δ_j)²/(k-j)²]
δ_j = x_j - j（unfolded 涨落 = -S(γ_j)——）
如果 E_ren = O(1)——A 活（剩非 S 结构——）
如果 E_ren 消失/线性——A = S 的非线性变换——封存——
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

def E_ren_calc(N_test):
    x = np.array([N0(g) for g in z[:N_test]])
    delta = x - np.arange(1, N_test+1)  # δ_j = x_j - j
    # E_ren = Σ_{j<k}[log|k-j+Δδ| - log(k-j) - Δδ/(k-j) + ½Δδ²/(k-j)²]
    E_ren = 0.0
    # 分块（对每 j——后面的 k——）
    for j in range(N_test-1):
        kk = np.arange(j+1, N_test)
        dd = delta[kk] - delta[j]  # Δδ = δ_k - δ_j
        dist = kk - j  # k - j
        # 截断（|Δδ/dist| < 0.5——展开收敛——）
        ratio = dd / dist
        # 精确项 - 展开项
        term = np.log(np.abs(dist + dd) + 1e-30) - np.log(dist) - ratio + 0.5*ratio**2
        # 高阶（ratio³——）小——但近邻 ratio~0.3——0.5·ratio² 是二阶——三阶 ~ratio³/3 ~ 0.009（小——）
        E_ren += np.sum(term)
    return E_ren

print('=== S-renormalization test（E_ren——）===')
print('E_ren = Σ[log|k-j+Δδ| - log(k-j) - Δδ/(k-j) + ½(Δδ/(k-j))²]')
for N_test in [100, 200, 500, 1000, 2000]:
    E_ren = E_ren_calc(N_test)
    print(f'  N={N_test}: E_ren={E_ren:+.4f}' + (f'——E_ren/log N={E_ren/log(N_test):+.4f}' if N_test > 10 else ''))

# 对比: 原始 ΔE（A2 的——）随 N——看 E_ren 是否小（扣掉了 S——）
print()
print('对照（原始 ΔE vs E_ren——）:')
for N_test in [200, 500, 1000]:
    x = np.array([N0(g) for g in z[:N_test]])
    # 原始 E_N - E_uniform
    E = 0.0
    for j in range(N_test-1):
        E += np.sum(np.log(np.abs(x[j+1:] - x[j])))
    u = np.arange(1, N_test+1, dtype=float)
    Eu = 0.0
    for j in range(N_test-1):
        Eu += np.sum(np.log(u[j+1:] - u[j]))
    E_ren = E_ren_calc(N_test)
    print(f'  N={N_test}: ΔE(原始)={E-Eu:+.4f}——E_ren(扣S)={E_ren:+.4f}——剩余占比={abs(E_ren)/abs(E-Eu)*100:.1f}%')
