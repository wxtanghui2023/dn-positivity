#!/usr/bin/env python3
"""误差积分检验: M(T) - M_main(T)——Titchmarsh 展开的误差积分
M_main(T) = -(1/π)Σ_p [1-cos(T log p)]/(√p log²p)（9/8 发现——绝对收敛——）
如果误差积分 O(1)——严格化聚焦在误差积分的证明——
如果误差积分大/发散——M 的 O(1) 不来自 M_main——
"""
import numpy as np
from math import log, pi

# 加载零点
path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z)
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
cumM = np.cumsum(Sbar * dg)  # 真实 M（在零点处——）

# M_main(T) = -(1/π)Σ_p [1-cos(T log p)]/(√p log²p)
# 用素数（到 1e7——足够——p>1e6 贡献 <0.005——9/8——）
primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
primes_small = primes[primes < 1000000]
w_p = 1.0/(np.sqrt(primes_small) * np.log(primes_small)**2)

# 在零点处算 M_main（T = z[k]——）
M_main_at = np.zeros(len(z))
for k in range(0, len(z), 100):  # 采样每 100——省时间
    T = z[k]
    M_main_at[k] = -(1.0/pi) * np.sum(w_p * (1 - np.cos(T * np.log(primes_small))))

# 真实 M 在同样位置（插值——）
# cumM[k] 是到零点 k+1 的——M(z[k]) ≈ cumM[k]
sample = np.arange(0, len(z), 100)
M_real_s = cumM[sample]
M_main_s = M_main_at[sample]

print('=== 误差积分检验: M - M_main ===')
print(f'真实 M: mean={M_real_s.mean():.3f}——max={M_real_s.max():.3f}——min={M_real_s.min():.3f}')
print(f'M_main: mean={M_main_s.mean():.3f}——max={M_main_s.max():.3f}——min={M_main_s.min():.3f}')
err = M_real_s - M_main_s
print(f'误差(M-M_main): mean={err.mean():+.3f}——std={err.std():.3f}——max|={np.max(np.abs(err)):.3f}')
c = np.corrcoef(M_real_s, M_main_s)[0,1]
print(f'相关: {c:.4f}')

# 误差的分段（增长?——）
print()
print('误差分段（每 500 采样——）:')
for i in range(0, len(err), 100):
    seg = err[i:i+100]
    print(f'  采样{i}: 误差={seg[-1]:+.3f}——段内max|={np.max(np.abs(seg)):.3f}')
