#!/usr/bin/env python3
"""ΔS = -N0'δ 精度 + P_N 恒等分解（修正——）"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = 200000
z = z[:K]
dg = np.diff(z)  # K-1 个

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

N0v = np.array([N0(t) for t in z[:-1]])  # K-1 个
S_right = np.arange(1, K) - N0v  # S(γ_k+)——k=1..K-1——长度 K-1
dS = np.diff(S_right)  # K-2 个——ΔS_k = S_{k+1}-S_k

# δ_k 用 z[k] 的 N0'（k=1..K-2——与 dS 对齐——）
t_for_delta = z[1:-1]  # γ_{k+1}——k=1..K-2 的 δ_k 用 γ_k 或中点?
# δ_k = Δγ_k - 1/N0'(γ_k)——Δγ_k = z[k+1]-z[k]——dS_k 对应 k（S_k = S(γ_k)——）
# dS_k = S_{k+1} - S_k = 1 - [N0(γ_{k+1})-N0(γ_k)]——N0 差用 z[k], z[k+1]
g_k = z[1:-1]  # γ_k for k=1..K-2（z[i] 是第 i+1 零点——z[1]=γ_2——）
N0p_k = np.array([log(t/(2*pi))/(2*pi) for t in g_k])
# δ_k（k=2..K-2——用 γ_k 的 N0'——）——dg[k-1] = γ_{k+1}-γ_k（k 从 1——）
# dS 索引 0 对应 k=1（S_2-S_1——）——δ_1 = Δγ_1 - 1/N0'(γ_1)——γ_1 = z[0]
N0p_g1 = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])  # γ_1..γ_{K-1}
delta = dg - 1.0/N0p_g1  # δ_k for k=1..K-1
# dS_k（k=1..K-2——）对应 δ_k（k=1..K-2——）
pred = -N0p_g1[:-1] * delta[:-1]
resid = dS - pred
print('=== ΔS = -N0\'δ 精度 ===')
print(f'残差 std: {resid.std():.2e}——max: {np.max(np.abs(resid)):.2e}')
print(f'相关: {np.corrcoef(dS, pred)[0,1]:.10f}')

# 二阶检验
t_mid2 = (z[1:-1] + z[2:])/2
N0pp = np.array([1.0/(2*pi*t) for t in t_mid2])
second = -0.5 * N0pp * dg[1:-1]**2  # k=1..K-2 的二阶
c2 = np.corrcoef(resid, second)[0,1]
print(f'残差 vs 二阶: 相关 {c2:.4f}——比值 {np.mean(resid/second):.4f}')

# P_N 恒等分解
S1 = S_right[0]
print('\n=== P_N 恒等分解 ===')
for N_chk in [1000, 10000, 50000]:
    P_dir = np.sum(S_right[:N_chk] - 0.5)
    dS_j = np.diff(S_right[:N_chk])
    jj = np.arange(1, N_chk)
    P_id = N_chk*(S1-0.5) - np.sum((N_chk-jj)*dS_j)
    print(f'  N={N_chk}: P(直接)={P_dir:+.4f}——P(恒等)={P_id:+.4f}——差={P_dir-P_id:+.2e}')
