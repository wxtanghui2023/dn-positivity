#!/usr/bin/env python3
"""M_main 修正: 截断展开积分的正确形式（含 cos(p log p)——）
∫₀^T S_titch(t)dt = -(1/π)Σ_p ∫_p^T sin(t log p)/(√p log p)dt
  = -(1/π)Σ_p [cos(p log p) - cos(T log p)]/(√p log²p)
（截断 p≤t 的换序——下限 p 而非 0——）
对比: 我之前用的 M_main = -(1/π)Σ(1-cos(T log p))/(√p log²p)（下限 0——）
"""
import numpy as np
from math import log, pi

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 100000
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
cumM = np.cumsum(Sbar * dg)

primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
ps = primes[primes < 100000]
c_p = 1.0/(np.sqrt(ps) * np.log(ps)**2)
cos_pp = np.cos(ps * np.log(ps))  # cos(p log p) 常数

print('=== M_main 修正（cos(p log p)——）===')
samples = np.arange(0, K, 100)
T_s = z[samples]
M_real_s = cumM[samples]

# 版1: 旧（下限 0——1-cos——）
M1_s = np.array([-(1.0/pi)*np.sum(c_p*(1-np.cos(T*np.log(ps)))) for T in T_s])
# 版2: 新（下限 p——cos(p log p)-cos(T log p)——）
M2_s = np.array([-(1.0/pi)*np.sum(c_p*(np.cos(ps*np.log(ps))-np.cos(T*np.log(ps)))) for T in T_s])

for name, Mk in [('旧(1-cos)', M1_s), ('新(cos pp - cos Tp)', M2_s)]:
    err = M_real_s - Mk
    print(f'{name}: mean={Mk.mean():+.4f}——误差 mean={err.mean():+.4f}——误差 std={err.std():.4f}——'
          f'相关={np.corrcoef(M_real_s, Mk)[0,1]:.4f}')

# 常数项: -(1/π)Σcos(p log p)/(√p log²p)
dc_const = -(1.0/pi)*np.sum(cos_pp * c_p)
print(f'常数 -(1/π)Σcos(p log p)/(√p log²p) = {dc_const:+.4f}')
print(f'如果误差 ~ -常数——则 M ~ M2 - 常数?——')

# 检查: M 的 DC（0.6）vs M2 的 DC
# 版3: M3 = M2 的负 = (1/π)Σ[cos(T log p) - cos(p log p)]/...
M3_s = -M2_s
err3 = M_real_s - M3_s
print(f'版3(-M2): 误差 mean={err3.mean():+.4f}——std={err3.std():.4f}——相关={np.corrcoef(M_real_s, M3_s)[0,1]:.4f}')
