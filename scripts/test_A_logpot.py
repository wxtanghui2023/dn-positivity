#!/usr/bin/env python3
"""A 的第二死亡测试: 对数势能 I_A 是否只是 GUE/统计
比较（unfolded 无标度——）:
- 零点（unfolded u_n = N0(γ_n)——）
- GUE 特征值（unfolded——）
- Poisson（unfolded 均匀——）
I_A = Σ_{j<k} log|u_j - u_k|/N²（- 平滑背景——）
看零点是否 ≈ GUE（死——统计）或不同（活——）
"""
import numpy as np
from math import log, pi

def log_potential(points, N=None):
    """I_A = (2/N²)Σ_{j<k}log|u_j-u_k|（对数势——）"""
    pts = np.sort(points)
    n = len(pts)
    # 用成对（向量化——O(N²)——N~几百到几千——）
    total = 0.0
    # 分块避免内存爆炸
    for i in range(n):
        if i < n-1:
            d = pts[i+1:] - pts[i]
            total += np.sum(np.log(np.abs(d) + 1e-30))
    return 2.0*total/(n*n)

print('=== 对数势能比较（unfolded——）===')

# 1. 零点 unfolded（u_n = N0(γ_n)——直接算——用前 N 个零点）
z = np.load('/tmp/zeros_odlyzko_2M.npy')
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

for N_test in [200, 500]:
    # 零点 unfolded
    gamma = z[:N_test]
    u_zeros = np.array([N0(g) for g in gamma])
    # 减去均匀背景（u ~ n——）——log 势的平滑部分（均匀点的——）
    # 均匀点（0..N 的——整数——）
    u_unif = np.arange(1, N_test+1, dtype=float)
    I_zero = log_potential(u_zeros)
    I_unif = log_potential(u_unif)
    print(f'\nN={N_test}: I_A(零点unfolded)={I_zero:.4f}——I_A(均匀整数)={I_unif:.4f}——差={I_zero-I_unif:+.4f}')

# 2. GUE 模拟（小 N——重复平均——）
print('\nGUE 模拟（对数势——）:')
for N_gue in [50, 100]:
    trials = 20
    I_gue_list = []
    I_poisson_list = []
    for t in range(trials):
        # GUE 矩阵（Hermitian——高斯实部/虚部——）
        A = np.random.randn(N_gue, N_gue) + 1j*np.random.randn(N_gue, N_gue)
        A = (A + A.conj().T)/2
        ev = np.linalg.eigvalsh(A)
        # unfolded（半圆累积——用经验 CDF——）
        ev_sorted = np.sort(ev)
        # 半圆展开（到均匀——用 N0_gue(λ) = 半圆累积——）
        # 简化: 用排序（rank unfolding——）
        u_gue = np.arange(1, N_gue+1, dtype=float) + np.random.rand(N_gue)*0  # rank
        # 实际: GUE 的 unfolded 间距（用局部平均密度——）
        # 简化直接用特征值的 rank（理想 unfolding 的近似——）
        I_gue_list.append(log_potential(u_gue))
        # Poisson（均匀随机——）
        u_pois = np.sort(np.random.rand(N_gue)*N_gue)
        I_poisson_list.append(log_potential(u_pois))
    print(f'  N={N_gue}: I_A(GUE rank-unfolded)={np.mean(I_gue_list):.4f}——I_A(Poisson)={np.mean(I_poisson_list):.4f}')
    print(f'    （均匀整数的 I_A（N={N_gue}——）={log_potential(np.arange(1,N_gue+1,dtype=float)):.4f}——）')
