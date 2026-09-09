#!/usr/bin/env python3
"""E(t) = S(t) - S_titch(t) 的逐点结构——为什么 ∫E = O(1)?
S_titch(t) = -(1/π)Σ_{p<=t} sin(t log p)/(√p log p)（Titchmarsh 截断——）
"""
import numpy as np
from math import log, pi

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 100000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

def N0(t):
    if t <= 1: return 0.0
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

# S(t) 逐点（在零点右极限——）
N0v = np.array([N0(t) for t in z[:-1]])
S_pt = np.arange(1, K) - N0v  # S(γ_k+)

# S_titch(t)（在零点处——截断 p<=t——）
primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
print('计算 S_titch（采样——）...')
step = 20
t_s = z[:-1][::step]
S_pt_s = S_pt[::step]
S_titch_s = np.zeros(len(t_s))
for i, t in enumerate(t_s):
    ps = primes[primes <= t]
    S_titch_s[i] = -(1.0/pi) * np.sum(np.sin(t*np.log(ps))/(np.sqrt(ps)*np.log(ps)))

E = S_pt_s - S_titch_s
print(f'=== E(t) = S - S_titch 的结构 ===')
print(f'S_pt: mean={S_pt_s.mean():+.4f}——std={S_pt_s.std():.4f}')
print(f'S_titch: mean={S_titch_s.mean():+.4f}——std={S_titch_s.std():.4f}')
print(f'E: mean={E.mean():+.4f}——std={E.std():.4f}——max|={np.max(np.abs(E)):.4f}')

# E 的积分（数值——）
cumE = np.cumsum(E)
print(f'ΣE（每 {step} 零点——）: 末值={cumE[-1]:+.3f}——max|={np.max(np.abs(cumE)):.3f}')

# E 的振荡特征——符号游程（高频?——）
sg = np.sign(E)
flips = np.where(sg[:-1] != sg[1:])[0]
runs = np.diff(np.concatenate([[0], flips, [len(E)-1]]))
print(f'E 符号游程: 平均长={runs.mean():.2f}（1-2 = 高频振荡——）')

# E 的自相关
print('E 自相关:')
for lag in [1, 2, 5, 10, 20]:
    c = np.corrcoef(E[:-lag], E[lag:])[0,1]
    print(f'  ρ({lag}) = {c:+.4f}')

# E 的分段（漂移?——）
print()
print('E 分段（每 1000 采样——）:')
for i in range(0, len(E), 1000):
    seg = E[i:i+1000]
    print(f'  采样{i} (γ~{t_s[i]:.0f}): mean={seg.mean():+.4f}——std={seg.std():.4f}')
