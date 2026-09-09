#!/usr/bin/env python3
"""P_N 的积分恒等式验证: P_N = ½S(γ_N)² + ∫S·N₀'dt - N₀(γ₁)?
推导: P_N = N²/2 - ΣN₀(γ_k)——∫S·N₀' = NN₀(γ_N) - ½N₀² - Σ_{2}^N N₀
验证 + 算 ∫S·N₀' 的数值（O(1)? 发散?——）
"""
import numpy as np
from math import log, pi

z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = 200000
z = z[:K]

def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

N0v = np.array([N0(t) for t in z[:-1]])
S_right = np.arange(1, K) - N0v
S1 = S_right[0]
P_direct = np.cumsum(S_right - 0.5)

# ∫S·N₀'——S 在区间内 = k - N0(t)——用分段精确积分
# ∫_{γ_k}^{γ_{k+1}} (k - N0(t))·N0'(t)dt = k[N0] - ½[N0²]
dg = np.diff(z)
dN0 = np.diff(N0v)  # N0(γ_{k+1}) - N0(γ_k)
dN0sq = np.diff(N0v**2)
# ∫S·N0' 到 γ_N = Σ_{k=1}^{N-1}[k·dN0_k - ½·dN0sq_k]
# k 从 1（区间 γ_1-γ_2——）——区间 k 的 S = k（第 k 零点后——）
# S(t) = k on [γ_k, γ_{k+1})——N(γ_k+) = k——区间 k（γ_k 到 γ_{k+1}——）
k_vals = np.arange(1, K)  # 区间 k 的 S = k
int_part = k_vals * dN0 - 0.5 * dN0sq  # 每区间的 ∫S·N0'
cum_int = np.cumsum(int_part)  # 到区间 N-1 = 到 γ_N

print('=== P_N 积分恒等式验证 ===')
for N_chk in [1000, 10000, 50000, 100000]:
    # 到 γ_N——N_chk 个零点——区间 1..N_chk-1
    idx = N_chk - 2  # cum_int 索引（区间 N_chk-1——）
    int_val = cum_int[idx]
    S_N = S_right[N_chk-1]
    # 恒等式: P_N = ½S_N² + ∫S·N0' - N0(γ₁)?（推导的——）
    P_id = 0.5*S_N**2 + int_val - N0v[0]
    P_dir = P_direct[N_chk-1]
    print(f'  N={N_chk}: P(直接)={P_dir:+.4f}——P(恒等)={P_id:+.4f}——差={P_dir-P_id:+.4f}')

# ∫S·N0' 的数值（到 N——O(1)?）
print()
print('∫S·N0\' 的数值:')
for N_chk in [1000, 10000, 50000, 100000, 199999]:
    idx = N_chk - 2
    if idx < len(cum_int):
        print(f'  到 N={N_chk}: ∫S·N0\'={cum_int[idx]:+.3f}')

# ∫S·N0' 的分段增长（O(1)? log?）
print()
print('∫S·N0\' 分段:')
for i in range(0, len(cum_int), 20000):
    print(f'  到区间{i+1} (N~{i+1}): ∫S·N0\'={cum_int[i]:+.3f}')
