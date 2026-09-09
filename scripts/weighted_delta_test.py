#!/usr/bin/env python3
"""Weighted δ-sum Lemma 死亡测试（唐先生 11:24 指导——）
A(x) = Σ_{γ_n<=x} δ_n——B(X) = ∫_0^X A(x)dx
P_N 本质对应 B(γ_N)——需要 B(X) = O(1)? 还是 log/X^α?
"""
import numpy as np
from math import log, pi

z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = min(len(z), 500000)
z = z[:K]
print(f'零点: {K}——γ到 {z[-1]:.0f}')

dg = np.diff(z)
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0p  # δ_n（n=1..K-1——）

# A(x) = Σ_{n<=N}δ_n（δ 的部分和——）
A_cum = np.cumsum(delta)
print(f'\nA(N) = Σδ: 末值={A_cum[-1]:+.3f}——max|={np.max(np.abs(A_cum)):.3f}')

# B(X) = ∫A(x)dx——P_N 对应 B——数值（ΣA_n·Δγ_n——累积的累积——）
B_cum = np.cumsum(A_cum * dg)  # Σ_m A(m)·Δγ_m ≈ ∫A dx
print(f'B(N) = ∫A dx: 末值={B_cum[-1]:+.3f}——max|={np.max(np.abs(B_cum)):.3f}')

# 分段——B 的增长（O(1)? log? X^α?）
print('\nB(N) 分段（每 5 万——）:')
for i in range(0, len(B_cum), 50000):
    idx = min(i+49999, len(B_cum)-1)
    print(f'  到零点{idx}: A={A_cum[idx]:+.3f}——B={B_cum[idx]:+.3f}')

# B 的增长标度
print('\nB 的增长标度:')
for N in [10000, 50000, 100000, 200000, 400000]:
    idx = min(N-1, len(B_cum)-1)
    g = z[idx]
    print(f'  N={N} (γ~{g:.0f}): B={B_cum[idx]:+.3f}——log γ={log(g):.2f}——√N={np.sqrt(N):.0f}')

# 关键: P_N vs B 的关系（P_N = N(S1-1/2) + Σ(N-j)ΔS_j——用 δ 的——）
# ΔS_j ≈ -N0'(γ_j)δ_j——P_N ≈ N(S1-1/2) - Σ(N-j)N0'δ_j
# 而 Σ(N-j)N0'δ_j ≈ ∫(N-N(t))N0' dA 类——与 B 的关系?
# 直接验证: P_N 与 B 的相关（数值——）
def N0v_calc(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0v_calc(t) for t in z[:-1]])
S_right = np.arange(1, K) - N0v
P_direct = np.cumsum(S_right - 0.5)
# 采样对比
samples = np.arange(1000, K-1, 1000)
c = np.corrcoef(P_direct[samples], B_cum[samples])[0,1]
print(f'\nP_N vs B 相关: {c:.4f}')
# P_N - B 的残差
resid = P_direct[samples] - B_cum[samples]
print(f'P_N - B: mean={resid.mean():+.3f}——std={resid.std():.3f}——max|={np.max(np.abs(resid)):.3f}')
