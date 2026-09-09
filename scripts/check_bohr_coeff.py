#!/usr/bin/env python3
"""展开定理基石: S(t) 的 Bohr 平均系数
a_p = lim_{T→∞} (1/T)∫₀^T S(t)·sin(t log p)dt（和 cos——）
如果存在且匹配 Sbar 拟合系数——S 的"平均谱"确立——展开定理有基础——
"""
import numpy as np
from math import log, pi

path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

def N0(t):
    if t <= 1: return 0.0
    return (t/(2*pi))*(log(t/(2*pi)) - 1) + 7.0/8

# S(t) 在区间内的值（零点之间——）——S(t) = k - N0(t)（γ_k <= t < γ_{k+1}——）
# 采样 t（均匀——每 0.5 一个——）
print('构建 S(t)（采样——）...')
t_samples = []
S_samples = []
# 用二分找每个采样 t 的零点计数——或用累积
# 简化: 在零点之间线性扫描——每区间取几个点
step_interval = 2  # 每区间 2 个点
for k in range(K-1):
    g0, g1 = z[k], z[k+1]
    for j in range(step_interval):
        t = g0 + (g1-g0)*(j+0.5)/step_interval
        t_samples.append(t)
        S_samples.append((k+1) - N0(t))  # N(t) = k+1（区间内——）

t_samples = np.array(t_samples)
S_samples = np.array(S_samples)
print(f'采样点: {len(t_samples)}——S mean={S_samples.mean():+.4f}——std={S_samples.std():.4f}')

# Bohr 系数: (1/T)∫₀^T S(t) sin(t log p) dt——用累积积分
print()
print('Bohr 系数（S 的平均谱——）:')
for p in [2, 3, 5, 7]:
    # 积分 ∫S sin(t log p)dt（累积——）
    integrand = S_samples * np.sin(t_samples * log(p))
    cum_int = np.cumsum(integrand * np.gradient(t_samples))
    T = t_samples[-1]
    # (1/T)∫——在不同 T 的值（收敛?——）
    vals = []
    for frac in [0.25, 0.5, 0.75, 1.0]:
        idx = int(len(cum_int)*frac) - 1
        vals.append(cum_int[idx]/t_samples[idx])
    print(f'  p={p}: (1/T)∫S sin(t log p) → ' + ' '.join(f'{v:+.5f}' for v in vals))
    # cos 版
    integrand2 = S_samples * np.cos(t_samples * log(p))
    cum_int2 = np.cumsum(integrand2 * np.gradient(t_samples))
    vals2 = []
    for frac in [0.25, 0.5, 0.75, 1.0]:
        idx = int(len(cum_int2)*frac) - 1
        vals2.append(cum_int2[idx]/t_samples[idx])
    print(f'      (1/T)∫S cos(t log p) → ' + ' '.join(f'{v:+.5f}' for v in vals2))
    print(f'      → 幅度 ≈ {np.hypot(vals[-1], vals2[-1]):.4f}（Sbar 拟合: p={p}: {0.2147 if p==2 else (0.1671 if p==3 else (0.1186 if p==5 else 0.0927))}——）')
