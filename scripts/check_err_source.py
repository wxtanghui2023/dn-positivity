#!/usr/bin/env python3
"""误差来源分析: M - M_main 的常数(1.93)和振荡(0.21)的来源
候选: 常数来自 S 展开的截断/常数项——振荡来自高阶(谐波/尾部)——
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
# M_main 用不同素数上限——看常数是否闭合
for pmax in [1000, 10000, 100000]:
    ps = primes[primes < pmax]
    w_p = 1.0/(np.sqrt(ps) * np.log(ps)**2)
    # M_main 在采样点
    samples = np.arange(0, K, 200)
    M_main_s = np.array([-(1.0/pi)*np.sum(w_p*(1-np.cos(T*np.log(ps)))) for T in z[samples]])
    M_real_s = cumM[samples]
    err = M_real_s - M_main_s
    print(f'p<{pmax}: 误差 mean={err.mean():+.4f}——std={err.std():.4f}')

# 常数候选: -(1/π)Σ1/(√p log²p) 的全部——减去(1/π)Σ cos 的平均?
# S(t) 的展开常数: S(t) ~ -(1/π)Σ sin/(√p log p)——无常数——但 S 的零点表示有
# M 的零点表示: M = Σ(T-γ) - ∫N0——常数来自?
print()
print('常数候选检查:')
# (1/π)Σ_{p}1/(√p log²p) 的总和（全素数——）
ps_all = primes
w_all = 1.0/(np.sqrt(ps_all) * np.log(ps_all)**2)
total_w = np.sum(w_all)
print(f'(1/π)Σ1/(√p log²p)（全素数——）= {total_w/pi:.4f}')
# 如果 M_main ~ -(1/π)Σ(1-cos)/... → DC ~ -total_w/π（cos 平均 0——）
# 但 M_main mean -1.32 vs -total_w/π?
print(f'M_main 理论 DC（如果 cos 平均 0——）= -{total_w/pi:.4f}')

# 真实检查: cos(T log p) 在零点 T 的平均（不是 0?——）
# 采样 T（零点——）——cos(T log 2) 的平均
T_samples = z[np.arange(0, K, 100)]
cos2_mean = np.mean(np.cos(T_samples * log(2)))
print(f'cos(T log2) 在零点处的平均 = {cos2_mean:+.4f}（0 = 无偏——）')

# 误差振荡的来源: 残差的频率——(M-M_main) 的谱
samples = np.arange(0, K, 50)
M_main_s = np.array([-(1.0/pi)*np.sum((1-np.cos(T*np.log(primes[primes<100000])))/
    (np.sqrt(primes[primes<100000])*np.log(primes[primes<100000])**2)) for T in z[samples]])
err = cumM[samples] - M_main_s
err_dc = err - err.mean()
spec = np.abs(np.fft.fft(err_dc * np.hanning(len(err_dc))))**2
fr = np.fft.fftfreq(len(err_dc))
pos = fr > 0
top = np.argsort(spec[pos])[-5:][::-1]
print()
print('误差振荡的主频（采样间隔 50 零点——）:')
for idx in top:
    print(f'  频率={fr[pos][idx]:.5f}/采样——周期={50/fr[pos][idx]:.1f} 零点——')
