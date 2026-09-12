#!/usr/bin/env python3
"""Test A2/A3: 重正化 log 能量 + 局部 log 能量（判别量——）
A2: E_N - E_uniform（unfolded 零点的 log 能量去均匀背景——）O(1)? log N?
A3: E_local(L) = Σ_{|x_j-x_k|<L} log|x_j-x_k|（短程——排斥敏感——）
    比较: 零点 unfolded vs Poisson（局部密度——）
"""
import numpy as np
from math import log, pi

def log_energy_renorm(x):
    """E_N - E_uniform——x 是 unfolded（~1 密度——）
    E_uniform(N)（整数 1..N 的 log 能量——）"""
    n = len(x)
    xs = np.sort(x)
    # E = Σ_{j<k} log|x_j - x_k|
    E = 0.0
    for i in range(n-1):
        d = xs[i+1:] - xs[i]
        E += np.sum(np.log(np.abs(d)))
    # E_uniform（整数——）——用公式或直接
    u = np.arange(1, n+1, dtype=float)
    E_unif = 0.0
    for i in range(n-1):
        d = u[i+1:] - u[i]
        E_unif += np.sum(np.log(d))
    return E - E_unif, E, E_unif

def local_log_energy(x, L):
    """E_local(L) = Σ_{|x_j-x_k|<L} log|x_j-x_k|——窗口——"""
    xs = np.sort(x)
    n = len(xs)
    total = 0.0
    for i in range(n):
        # 向右找窗口内的
        j = i + 1
        while j < n and xs[j] - xs[i] < L:
            total += log(xs[j] - xs[i])
            j += 1
    return total

print('=== Test A2: 重正化 log 能量 ===')
z = np.load('data/zeros_odlyzko_2M.npy')
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

for N_test in [200, 500, 1000]:
    x_z = np.array([N0(g) for g in z[:N_test]])
    # 减去线性趋势（unfolded ~ n + 涨落——直接用 N0 值——x ~ n 附近——）
    delta, E, Eu = log_energy_renorm(x_z)
    print(f'  N={N_test}: ΔE = E_N - E_uniform = {delta:+.4f}——E_N={E:.2f}——E_unif={Eu:.2f}')

# 随 N 的 ΔE（O(1)? log N?——）
print()
print('ΔE 随 N（增长——）:')
prev = None
for N_test in [100, 200, 500, 1000, 2000]:
    x_z = np.array([N0(g) for g in z[:N_test]])
    delta, _, _ = log_energy_renorm(x_z)
    print(f'  N={N_test}: ΔE={delta:+.4f}' + (f'——ΔE/log N={delta/log(N_test):+.4f}' if N_test > 10 else ''))

print()
print('=== Test A3: 局部 log 能量 ===')
# 零点 unfolded vs Poisson（unfolded 均匀——）
for N_test in [2000]:
    x_z = np.array([N0(g) for g in z[:N_test]])
    # Poisson（unfolded 均匀——N 个点 [0,N]——）
    rng = np.random.default_rng(1)
    for L in [1.0, 2.0, 5.0]:
        E_z = local_log_energy(x_z - np.arange(1, N_test+1), L)  # 去趋势（x-n——涨落——）
        # Poisson 的去趋势涨落
        pois = np.sort(rng.uniform(0, N_test, N_test))
        E_p = local_log_energy(pois - np.arange(1, N_test+1), L)
        # 期望: 局部 log 能量 ~ 窗口内对数间距的和——归一（每点——）
        print(f'  L={L}: E_local(零点)/N={E_z/N_test:.4f}——E_local(Poisson)/N={E_p/N_test:.4f}')
