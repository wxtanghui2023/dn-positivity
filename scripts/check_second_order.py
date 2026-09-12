#!/usr/bin/env python3
"""验证: Σ(N-k)N0'δ_k = -N(S1-1/2) + P_N + 二阶?——二阶项的量级
二阶 = Σ(N-k)(N0'Δγ_k - ΔN₀_k)——O(1)? 还是线性?
如果二阶 O(1)——隐藏恒等式（纯代数——不经零点统计——）成立——
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
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0p
dN0 = np.diff(N0v)  # ΔN₀_k（精确——）

print('=== 二阶项验证 ===')
# 二阶项 = Σ(N-k)(N0'Δγ_k - ΔN0_k)——N0'Δγ vs ΔN0 的差
for N_chk in [1000, 10000, 50000, 100000]:
    kk = np.arange(1, N_chk)
    # N0'Δγ_k - ΔN0_k（每项——）
    diff_k = N0p[:N_chk-1]*dg[:N_chk-1] - dN0[:N_chk-1]
    second = np.sum((N_chk-kk) * diff_k)
    print(f'  N={N_chk}: 二阶项 Σ(N-k)(N0\'Δγ-ΔN0) = {second:+.4f}——/N={second/N_chk:+.4f}')

# 主恒等式验证: Σ(N-k)N0'δ_k vs -N(S1-1/2) + P_N
S1 = S_right[0]
P_direct = np.cumsum(S_right - 0.5)
print()
print('恒等式: Σ(N-k)N0\'δ_k = -N(S1-1/2) + P_N + 二阶?')
for N_chk in [1000, 10000, 50000]:
    kk = np.arange(1, N_chk)
    wn = np.sum((N_chk-kk) * N0p[:N_chk-1] * delta[:N_chk-1])
    target = -(N_chk*(S1-0.5)) + P_direct[N_chk-1]
    print(f'  N={N_chk}: Σ(N-k)N0\'δ = {wn:+.2f}——-N(S1-½)+P_N = {target:+.2f}——差={wn-target:+.2f}')

# 二阶项的'来源'——每项的 N0'Δγ-ΔN0（~½N0''Δγ²——）
print()
print('每项 N0\'Δγ-ΔN0 的量级（~二阶——）:')
diff_k_all = N0p*dg - dN0
print(f'  mean={diff_k_all.mean():+.2e}——std={diff_k_all.std():.2e}——max={np.max(np.abs(diff_k_all)):.2e}')
# 理论: ½N0''Δγ² ~ ½·(1/(2πt))·(2π/log)² ~ π/(t log²)
t_mid = (z[:-1]+z[1:])/2
th2 = 0.5 * (1.0/(2*pi*t_mid)) * dg**2
print(f'  理论 ½N0\'\'Δγ²: mean={th2.mean():+.2e}——相关 with diff: {np.corrcoef(diff_k_all, th2)[0,1]:.4f}')
