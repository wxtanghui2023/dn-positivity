#!/usr/bin/env python3
"""B(N) = Σ_{k<=N}(N-k)δ_k 的隐藏恒等式——直接攻击（唐先生 13:07——）
推导: Σ(N-k)Δγ_k = Σ_{k=2}^N γ_k - (N-1)γ_1（精确——）
→ B(N) = Σ(N-k)δ_k = Σ(N-k)Δγ_k - Σ(N-k)/N0'(γ_k)
验证 B(N) 的结构——是否 = 零点位置和（Σγ_k——）的——能否脱离零点——
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = min(len(z), 200000)
z = z[:K]

dg = np.diff(z)
def N0(t):
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8
N0p = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0p

print('=== B(N) = Σ(N-k)δ_k 的结构 ===')
# 恒等式验证: Σ_{k=1}^{N-1}(N-k)Δγ_k = Σ_{k=2}^{N}γ_k - (N-1)γ_1?
for N_chk in [1000, 10000]:
    kk = np.arange(1, N_chk)  # k=1..N-1
    lhs = np.sum((N_chk-kk) * dg[:N_chk-1])  # Δγ_k = dg[k-1]
    rhs = np.sum(z[1:N_chk]) - (N_chk-1)*z[0]  # Σ_{k=2}^N γ_k - (N-1)γ_1
    print(f'  N={N_chk}: Σ(N-k)Δγ = {lhs:.1f}——Σγ_k-(N-1)γ_1 = {rhs:.1f}——差={lhs-rhs:.6f}')

# B(N) = Σ(N-k)δ_k——直接
print()
print('B(N) 的数值（增长——）:')
for N_chk in [1000, 10000, 50000, 100000]:
    kk = np.arange(1, N_chk)
    B = np.sum((N_chk-kk) * delta[:N_chk-1])
    print(f'  N={N_chk}: B(N)={B:+.1f}——B/N={B/N_chk:+.4f}')

# B(N) 的分解: Σ(N-k)Δγ_k（→Σγ） - Σ(N-k)/N0'
print()
print('B(N) 分解（Σ(N-k)Δγ vs Σ(N-k)/N0\'——）:')
for N_chk in [10000, 50000]:
    kk = np.arange(1, N_chk)
    t1 = np.sum((N_chk-kk) * dg[:N_chk-1])  # Σ(N-k)Δγ（→Σγ——）
    t2 = np.sum((N_chk-kk) / N0p[:N_chk-1])  # Σ(N-k)/N0'
    print(f'  N={N_chk}: Σ(N-k)Δγ={t1:+.1f}——Σ(N-k)/N0\'={t2:+.1f}——B={t1-t2:+.1f}')

# 关键: B(N) vs 零点位置和 Σγ_k（的偏差——）——B 是否 ~ Σγ 类（大——）
print()
print('B(N) vs Σγ_k（量级——）:')
for N_chk in [10000, 100000]:
    B = np.sum((np.arange(1, N_chk)) * delta[:N_chk-1])
    sum_g = np.sum(z[:N_chk])
    print(f'  N={N_chk}: B={B:+.1f}——Σγ_k={sum_g:.1f}——B/Σγ={B/sum_g:.6f}')
