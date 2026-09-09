#!/usr/bin/env python3
"""用 Bohr 系数重建 M 模型——验证 M 的 DC 闭合
M(T) = ∫S̄——S̄ = Σ a_p sin(t log p)（Bohr 系数——）+ 残差
M DC = Σ a_p/log p + ∫残差 DC——对比真实 M DC(0.6)——
"""
import numpy as np
from math import log, pi

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
cumM = np.cumsum(Sbar * dg)
t_mid = (z[:-1] + z[1:])/2

primes = []
for n in range(2, 300):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)

# Bohr 系数（Sbar 的——）对前 ~60 个素数——(1/T)∫Sbar sin(t log p)dt
T = t_mid[-1]
print('=== Bohr 系数重建 M 模型 ===')
a_p = {}
for p in primes:
    if p > 200: break
    s_int = np.sum(Sbar * np.sin(t_mid * log(p)) * dg)  # 加权积分
    a_p[p] = s_int / T

# Σ a_p/log p（Bohr DC——）
dc_bohr = sum(a_p[p]/log(p) for p in a_p)
print(f'Bohr DC: Σa_p/log p（p≤200——）= {dc_bohr:.4f}')

# 残差（S̄ − Bohr 展开——）的积分 DC
R = Sbar.copy()
for p in a_p:
    R = R - a_p[p] * np.sin(t_mid * log(p))
print(f'残差 std={R.std():.4f}——mean={R.mean():+.5f}')
cumR = np.cumsum(R * dg)
print(f'残差积分: 末值={cumR[-1]:+.3f}——(DC 贡献 = 末值/T 类——不——累积的末值 = ∫R——)')

# M 真实
print()
print(f'真实 M: 末值={cumM[-1]:+.3f}——mean(采样)={np.mean(cumM[::200]):+.3f}')

# M 模型（Bohr——）: M_model = Σ a_p(1-cos(T log p))/log p——在末点
M_model_end = sum(a_p[p]*(1-np.cos(t_mid[-1]*log(p)))/log(p) for p in a_p)
print(f'M 模型(Bohr) 末值 = {M_model_end:+.3f}——真实 M 末值 = {cumM[-1]:+.3f}')

# 采样对比（相关——）
samples = np.arange(0, K, 200)
M_model_s = np.zeros(len(samples))
for j, idx in enumerate(samples):
    t = t_mid[idx]
    M_model_s[j] = sum(a_p[p]*(1-np.cos(t*log(p)))/log(p) for p in a_p)
M_real_s = cumM[samples]
err = M_real_s - M_model_s
print(f'M 真实 vs 模型(Bohr): 相关={np.corrcoef(M_real_s, M_model_s)[0,1]:.4f}')
print(f'误差: mean={err.mean():+.4f}——std={err.std():.4f}——max|={np.max(np.abs(err)):.3f}')

# 误差的 DC（应该 ~0.2——缺口——）
# 残差积分的贡献（加到模型——）
err_withR = err - cumR[samples]
print(f'误差-残差积分: mean={err_withR.mean():+.4f}——std={err_withR.std():.4f}')
