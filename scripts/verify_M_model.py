#!/usr/bin/env python3
"""验证 M(T) 的积分模型: M ~ Σ (a_p/log p)(1-cos(T log p)) + 常数
如果 Sbar ~ Σ a_p sin(t log p)——∫Sbar dt ~ Σ(a_p/log p)(1-cos)——有界——
"""
import numpy as np
from math import log, pi

path = 'zeros/zeros6'
K = 200000
z = np.zeros(K)
with open(path) as f:
    for i in range(K):
        z[i] = float(f.readline())

dg = np.diff(z[:K])
def IntN0(t):
    if t <= 1: return 0.0
    return t*t/(4*pi)*log(t/(2*pi)) - 3*t*t/(8*pi) + 7*t/8
kk = np.arange(1, K)
IntN = np.array([IntN0(t) for t in z[:K]])
Sbar = kk - (IntN[1:] - IntN[:-1])/dg
M_inc = Sbar * dg
cumM = np.cumsum(M_inc)  # 真实 M（在零点处——）
t_mid = (z[:-1] + z[1:])/2

# 1. 拟合 Sbar 的振幅（用更仔细的方法——分段平均——减少噪声——）
ps = [2, 3, 5, 7, 11, 13, 17, 19, 23]
cols = []
for p in ps:
    cols.append(np.sin(t_mid * log(p)))
    cols.append(np.cos(t_mid * log(p)))
X = np.stack(cols, axis=1)
# 用更多零点拟合（前 10 万——）
coef, _, _, _ = np.linalg.lstsq(X, Sbar, rcond=None)
amps = np.array([np.hypot(coef[2*i], coef[2*i+1]) for i in range(len(ps))])
phases = np.array([np.arctan2(coef[2*i+1], coef[2*i]) for i in range(len(ps))])

print('=== M(T) 积分模型验证 ===')
print('拟合振幅（前 9 素数——）:')
for i, p in enumerate(ps):
    print(f'  p={p}: a={amps[i]:.4f}——a/log p={amps[i]/log(p):.4f}')
print(f'  sum a_p/log p = {np.sum(amps/np.log(ps)):.4f} (M 偏正常数候选——)')

# 2. 模型 M: M_model(T) = Σ (a_p/log p)(1 - cos(T log p))——在零点处求值
M_model = np.zeros(len(t_mid))
for i, p in enumerate(ps):
    M_model += (amps[i]/log(p)) * (1 - np.cos(t_mid * log(p)))

# 真实 M（零点处的累积——）
M_real_at = cumM  # cumM[k] 对应 z[k]——用 t_mid 插值近似
# 对比（采样点——）
sample = np.linspace(1000, len(t_mid)-1, 200).astype(int)
print()
print('真实 M vs 模型 M（采样对比——）:')
print(f'  真实 M: mean={np.mean(cumM[sample]):.3f}——max={np.max(cumM[sample]):.3f}——min={np.min(cumM[sample]):.3f}')
print(f'  模型 M: mean={np.mean(M_model[sample]):.3f}——max={np.max(M_model[sample]):.3f}——min={np.min(M_model[sample]):.3f}')

# 相关系数（真实 vs 模型——）
from numpy import corrcoef
c = corrcoef(cumM[sample], M_model[sample])[0,1]
print(f'  相关: {c:.4f}')

# 残差
residM = cumM - M_model
print(f'  残差: std={residM[sample].std():.3f}——max={np.max(np.abs(residM[sample])):.3f}')

# 3. 只用 log2 的模型（最简——）
M2 = (amps[0]/log(2)) * (1 - np.cos(t_mid * log(2)))
c2 = corrcoef(cumM[sample], M2[sample])[0,1]
print()
print(f'  仅 log2 模型相关: {c2:.4f}——模型幅度 {amps[0]/log(2):.3f}')
print(f'  真实 M 幅度（max-min——）: {np.max(cumM[sample])-np.min(cumM[sample]):.3f}')
