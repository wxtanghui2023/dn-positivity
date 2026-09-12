#!/usr/bin/env python3
"""Weighted δ 测试第 2 步: P_N 与 Σ(N-n)δ_n 的精确关系
S_n = n - N0(γ_n)——γ_n = γ̄_n + ε_n（γ̄ = N0^{-1}——）
δ_n = Δγ_n - 1/N0'(γ_n)（间距偏差——）
P_N = Σ(S_n - 1/2)——用 δ 表达（无 N0' 权重的——）？
验证: P_N vs Σ(N-n)δ_n——P_N vs Σ(N-n)N0'δ_n——P_N vs 去中心 B——
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = min(len(z), 200000)
z = z[:K]

dg = np.diff(z)
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0v = np.array([N0(t) for t in z[:-1]])
S_right = np.arange(1, K) - N0v
P_direct = np.cumsum(S_right - 0.5)

N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0p

# 候选 1: Σ(N-n)δ_n（唐先生的——无 N0'）
W1 = np.zeros(K-1)
cum = 0
for n in range(1, K-1):
    pass
# 向量化: W1(N) = Σ_{n<=N}(N-n)δ_n = Σ_{m<=N}A(m)（A = Σδ 前缀——）
A_cum = np.cumsum(delta)
W1 = np.cumsum(A_cum)  # Σ_m A(m)——权重 1（每 δ_n 被 (N-n) 个 A 包含——但 A(m) 权重 1 不是 Δγ——）

# 候选 2: Σ(N-n)δ_n·Δγ 类（∫A dx 的——B——）
B_cum = np.cumsum(A_cum * dg)

# 候选 3: Σ(N-n)N0'(γ_n)δ_n（我的——）
# W3(N) = Σ_{n<=N-1}(N-n)N0'(γ_n)δ_n——直接
W3 = np.zeros(K-1)
for N in range(2, K-1, 100):  # 采样——省时间
    nn = np.arange(1, N)
    W3[N] = np.sum((N-nn)*N0p[:N-1]*delta[:N-1])

# 去中心的 A——∫(A - Ā)
A_mean = np.mean(A_cum[-1000:])  # 末段中心
B_dc = np.cumsum((A_cum - A_mean) * dg)

print('=== P_N vs 各候选 δ 表达 ===')
samples = np.arange(1000, K-2, 500)
for name, W in [('Σ(N-n)δ_n', W1), ('∫A dx (B)', B_cum), ('Σ(N-n)N0\'δ', W3), ('∫(A-Ā)dx', B_dc)]:
    # 对齐长度
    W_s = W[samples]
    P_s = P_direct[samples]
    c = np.corrcoef(P_s, W_s)[0,1]
    # 残差（线性拟合后——）
    A_fit = np.polyfit(P_s, W_s, 1)
    resid = W_s - np.polyval(A_fit, P_s)
    print(f'{name}: 相关={c:+.4f}——线性拟合后残差 std={resid.std():.3f}')

# 直接: P_N 与每个的"去趋势"关系
print()
print('P_N 的分段（对照——）:')
for i in range(0, K-2, 40000):
    print(f'  N={i}: P_N={P_direct[i]:+.3f}——W1(Σ(N-n)δ)={W1[i]:+.1f}——B={B_cum[i]:+.1f}')
