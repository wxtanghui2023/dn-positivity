#!/usr/bin/env python3
"""方向 A（快速版——N=5万——正规方程——）: 零点序列低维生成律
"""
import numpy as np
from math import log, pi

z = np.load('/tmp/zeros_odlyzko_2M.npy')
K = 50000
z = z[:K]
dg = np.diff(z)
N0pv = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0pv
d = delta[:K-1]
N = len(d)
print(f'δ 序列: N={N}——std={d.std():.4f}', flush=True)

def ar_r2(seq, k):
    """AR(k) 用正规方程——R²"""
    n = len(seq) - k
    # X: n×k（每行 [d_i, ..., d_{i+k-1}]——）
    X = np.empty((n, k))
    for j in range(k):
        X[:, j] = seq[j:n+j]
    y = seq[k:n+k]
    XtX = X.T @ X
    Xty = X.T @ y
    XtX += np.eye(k)*1e-8  # 岭
    coef = np.linalg.solve(XtX, Xty)
    pred = X @ coef
    ss_res = np.sum((y-pred)**2)
    ss_tot = np.sum((y-y.mean())**2)
    return 1 - ss_res/ss_tot

print('=== AR(k) R² ===', flush=True)
for k in [1, 2, 3, 5, 10, 20]:
    r2 = ar_r2(d, k)
    print(f'  AR({k}): R²={r2:.4f}', flush=True)

print('=== SVD 延迟嵌入（m=20——）===', flush=True)
m = 20
L = 20000
dL = d[:L]
H = np.empty((L-m, m))
for j in range(m):
    H[:, j] = dL[j:L-m+j]
U, S, Vt = np.linalg.svd(H, full_matrices=False)
S2 = S**2
frac = S2/S2.sum()
print('  奇异谱（前 8——）:', flush=True)
for i in range(8):
    print(f'    σ{i+1}: {frac[i]:.4f}（累积 {frac[:i+1].sum():.4f}）', flush=True)
print(f'  前 3 占比: {frac[:3].sum():.4f}——前 5: {frac[:5].sum():.4f}——（噪声预期前5~{5/m:.3f}）', flush=True)

print('=== 真实 vs AR1 合成（AR(2) 预测——）===', flush=True)
r1 = np.corrcoef(d[:-1], d[1:])[0,1]
rng = np.random.default_rng(7)
d_ar = np.zeros(N)
d_ar[0] = rng.normal(0, d.std())
for i in range(1, N):
    d_ar[i] = r1*d_ar[i-1] + rng.normal(0, d.std()*np.sqrt(1-r1**2))
for name, seq in [('真实', d), ('AR1合成', d_ar)]:
    r2 = ar_r2(seq, 2)
    print(f'  {name}: AR(2) R²={r2:.4f}', flush=True)
