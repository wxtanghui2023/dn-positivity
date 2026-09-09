#!/usr/bin/env python3
"""深挖: δ 的部分和一致有界性（Abel 求和的关键——）
Σδ = O(1)（8/23 无条件——）但需要部分和 Σ_{j<=m}δ_j = O(1)（一致——）
——如果部分和一致有界——P_N（相位均匀性——）从 Abel 可推——
"""
import numpy as np
from math import log, pi

z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = min(len(z), 500000)
z = z[:K]

dg = np.diff(z)
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0p
D_cum = np.cumsum(delta)  # δ 的部分和

print('=== δ 部分和的一致有界性 ===')
print(f'δ 部分和: 末值={D_cum[-1]:+.3f}——max|={np.max(np.abs(D_cum)):.3f}——min={np.min(D_cum):+.3f}')

# 分段——部分和的漂移
print('分段（每 5 万——）:')
for i in range(0, K-1, 50000):
    idx = min(i+49999, len(D_cum)-1)
    print(f'  到零点{idx}: Σδ={D_cum[idx]:+.3f}')

# 部分和的"最大漂移"随 N——看增长（O(1)? log? √N?）
print('\nmax|Σδ| 随 N（增长——）:')
for N in [10000, 50000, 100000, 200000, 400000]:
    print(f'  N={N}: max|Σδ(前N)|={np.max(np.abs(D_cum[:N])):.3f}')

# 关键: P_N 与加权 δ 的 Abel 关系——直接验证 P_N 的 δ 表达
# P_N = N(S1-1/2) - Σ_j (N-j) N0'(γ_j) δ_j
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
kk = np.arange(1, K)
S_right = kk - N0v
P_direct = np.cumsum(S_right - 0.5)

# 用 δ 表达（对几个 N——验证——）
print('\nP_N 的 δ 表达验证:')
S1 = S_right[0]
for N_idx in [1000, 10000, 50000, 100000]:
    j = np.arange(1, N_idx)  # j=1..N-1（0 基——j 对应零点 j——）
    # Σ_{j<k<=N} N0'(γ_j)δ_j——每 δ_j 被 (N-j) 个 S 项包含
    weighted = np.sum((N_idx - j) * N0p[j-1] * delta[j-1])  # j 从 1 到 N-1
    P_delta = N_idx*(S1 - 0.5) - weighted
    # 直接
    P_d = P_direct[N_idx-1]
    print(f'  N={N_idx}: P(δ表达)={P_delta:+.4f}——P(直接)={P_d:+.4f}——差={P_delta-P_d:+.6f}')
