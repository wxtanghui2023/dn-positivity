#!/usr/bin/env python3
"""方向 A: 零点序列的低维生成律测试（唐先生 14:16——）
δ_n（间距偏差——）序列——测:
1. AR(k) 线性预测的 R²（随 k——）——低维线性信号?
2. SVD 延迟嵌入谱（Takens——）——有效维数?
3. 真实 vs 合成（AR1 匹配——）的可预测性差——额外确定性?
"""
import numpy as np
from math import log, pi

z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = min(len(z), 400000)
z = z[:K]
dg = np.diff(z)
def N0p(t):
    return log(t/(2*pi))/(2*pi)
N0pv = np.array([N0p(t) for t in z[:-1]])
delta = dg - 1.0/N0pv  # δ_n（间距偏差——）
d = delta[:K-1]
N = len(d)
print(f'δ 序列: N={N}——std={d.std():.4f}')

# 1. AR(k) 线性预测 R²
print()
print('=== AR(k) 线性预测（R²——）===')
for k in [1, 2, 3, 5, 10, 20]:
    # 最小二乘 AR(k)
    X = np.stack([d[i:N-k+i] for i in range(k)], axis=1)  # X[i] = [d_{i},...,d_{i+k-1}]→预测 d_{i+k}
    y = d[k:]
    X = X[:len(y)]
    # 岭回归（稳定——）
    coef, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ coef
    ss_res = np.sum((y - pred)**2)
    ss_tot = np.sum((y - y.mean())**2)
    r2 = 1 - ss_res/ss_tot
    print(f'  AR({k}): R²={r2:.4f}')

# 2. SVD 延迟嵌入谱（有效维数——）
print()
print('=== SVD 延迟嵌入（Takens——）===')
m = 20  # 嵌入维
L = 20000  # 用前 2 万点
dL = d[:L]
H = np.stack([dL[i:L-m+i] for i in range(m)], axis=1)  # 每列一个延迟
U, S, Vt = np.linalg.svd(H, full_matrices=False)
S2 = S**2
frac = S2/S2.sum()
print(f'  奇异谱（前 10 个——能量占比——）:')
for i in range(10):
    print(f'    σ{i+1}: {frac[i]:.4f}（累积 {frac[:i+1].sum():.4f}）')
print(f'  前 3 个占比: {frac[:3].sum():.4f}——前 5: {frac[:5].sum():.4f}')
print(f'  （随机噪声的预期: 均匀分布——前 5 ~ {5/m:.3f}——）')

# 3. 真实 vs 合成（AR1——）的可预测性
print()
print('=== 真实 vs 合成 AR1（可预测性差——）===')
r1 = np.corrcoef(d[:-1], d[1:])[0,1]
print(f'  真实 δ 的 ρ(1) = {r1:+.4f}')
# AR1 合成（同 ρ1——）
rng = np.random.default_rng(7)
d_ar = np.zeros(N)
d_ar[0] = rng.normal(0, d.std())
for i in range(1, N):
    d_ar[i] = r1*d_ar[i-1] + rng.normal(0, d.std()*np.sqrt(1-r1**2))
# AR(2) 预测 R²——真实 vs AR1 合成
for name, seq in [('真实', d), ('AR1合成', d_ar)]:
    k = 2
    X = np.stack([seq[i:N-k+i] for i in range(k)], axis=1)
    y = seq[k:]
    X = X[:len(y)]
    coef, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ coef
    ss_res = np.sum((y - pred)**2)
    ss_tot = np.sum((y - y.mean())**2)
    r2 = 1 - ss_res/ss_tot
    print(f'  {name}: AR(2) R²={r2:.4f}')
