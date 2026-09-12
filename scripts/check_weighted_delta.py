#!/usr/bin/env python3
"""验证加权 δ 抵消: Σ_{j}(N-j)·(-N0'δ_j) ≈ N(S1-1/2) - P_N（攻点确认——）
P_N = N(S1-1/2) + Σ(N-j)ΔS_j（精确——）——ΔS_j ≈ -N0'(γ_j)δ_j
→ 验证: Σ(N-j)(-N0'δ_j) vs Σ(N-j)ΔS_j（差 = 二阶/高阶——小?——）
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = 200000
z = z[:K]
dg = np.diff(z)

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
S_right = np.arange(1, K) - N0v
S1 = S_right[0]

# ΔS_j（精确——）和 -N0'δ_j（近似——）
dS = np.diff(S_right)
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
# δ_j: Δγ_j = z[j+1]-z[j]（j=0 是 γ2-γ1——δ 的第 j 个——与 dS_j 对齐? dS[0] = S2-S1）
# dS_j = S_{j+1}-S_j = 1 - [N0(γ_{j+1}) - N0(γ_j)]——j 从 1（γ_1,γ_2——）
# 用 γ_j = z[j-1]（第 j 零点——）——N0' 在 γ_j——δ_j = dg[j-1] - 1/N0p[j-1]?
# dg[0] = z[1]-z[0] = γ_2-γ_1 = Δγ_1——δ_1 = Δγ_1 - 1/N0'(γ_1)——N0p[0] = N0'(z[0]) = N0'(γ_1)
delta = dg - 1.0/N0p  # δ_j for j=1..K-1（delta[0]=δ_1——）

print('=== 加权 δ 抵消验证 ===')
for N_chk in [1000, 10000, 50000, 100000]:
    # 精确的加权 ΔS
    jj = np.arange(1, N_chk)
    w_dS = np.sum((N_chk-jj)*dS[:N_chk-1])  # ΔS_1..ΔS_{N-1}——dS[0]=ΔS_1
    # δ 版: Σ(N-j)(-N0'δ_j)——δ_j 用 N0'(γ_j)（左端点——）——j=1..N-1
    w_delta = np.sum((N_chk-jj)*(-N0p[:N_chk-1])*delta[:N_chk-1])
    # 精确目标: -N(S1-1/2) + P_N
    P_dir = np.sum(S_right[:N_chk] - 0.5)
    target = -(N_chk*(S1-0.5)) + P_dir  # Σ(N-j)ΔS_j 的精确值（= P_N - N(S1-1/2)——符号——）
    print(f'  N={N_chk}: Σ(N-j)ΔS_j(精确)={w_dS:+.4f}——δ版={w_delta:+.4f}——差={w_dS-w_delta:+.4f}')

# δ 版与精确的差的增长（二阶——）
print()
print('δ 版误差（二阶——）随 N:')
for N_chk in [1000, 10000, 50000, 100000]:
    jj = np.arange(1, N_chk)
    w_dS = np.sum((N_chk-jj)*dS[:N_chk-1])
    w_delta = np.sum((N_chk-jj)*(-N0p[:N_chk-1])*delta[:N_chk-1])
    err = w_dS - w_delta
    print(f'  N={N_chk}: 二阶误差={err:+.4f}（~N 量级? {err/N_chk:.4f}——）')
