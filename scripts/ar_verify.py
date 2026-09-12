#!/usr/bin/env python3
"""验证 AR(20) R²=0.69 的真实性: PACF/系数结构/分段平稳/合成对照
"""
import numpy as np
from math import log, pi

z = np.load('data/zeros_odlyzko_2M.npy')
K = 50000
z = z[:K]
dg = np.diff(z)
N0pv = np.array([log(t/(2*pi))/(2*pi) for t in z[:-1]])
delta = dg - 1.0/N0pv
d = delta[:K-1]
N = len(d)

def ar_coefs(seq, k):
    n = len(seq) - k
    X = np.empty((n, k))
    for j in range(k):
        X[:, j] = seq[j:n+j]
    y = seq[k:n+k]
    XtX = X.T @ X
    Xty = X.T @ y
    XtX += np.eye(k)*1e-8
    return np.linalg.solve(XtX, Xty)

# 1. AR(20) 的系数结构
print('=== AR(20) 系数（前 20——）===', flush=True)
c20 = ar_coefs(d, 20)
for i, c in enumerate(c20):
    print(f'  a{i+1} = {c:+.4f}', flush=True)
print(f'  系数 L1 范数: {np.abs(c20).sum():.3f}——L2: {np.sqrt((c20**2).sum()):.3f}', flush=True)

# 2. PACF（偏自相关——用 AR(k) 的末系数——）
print()
print('=== PACF（AR(k) 的末系数 a_k——）===', flush=True)
for k in [1, 2, 3, 5, 8, 10, 15, 20]:
    ck = ar_coefs(d, k)
    print(f'  a_{k}（PACF at lag {k}）= {ck[-1]:+.4f}', flush=True)

# 3. 分段平稳（前/后段 AR(10) R²——）
print()
print('=== 分段 AR(10) R²（平稳性——）===', flush=True)
def ar_r2(seq, k):
    n = len(seq) - k
    X = np.empty((n, k))
    for j in range(k):
        X[:, j] = seq[j:n+j]
    y = seq[k:n+k]
    XtX = X.T @ X + np.eye(k)*1e-8
    coef = np.linalg.solve(XtX, X.T @ y)
    pred = X @ coef
    return 1 - np.sum((y-pred)**2)/np.sum((y-y.mean())**2)
half = N//2
print(f'  前段（0-{half}）: AR(10) R²={ar_r2(d[:half], 10):.4f}', flush=True)
print(f'  后段（{half}-{N}）: AR(10) R²={ar_r2(d[half:], 10):.4f}', flush=True)

# 4. 合成对照（AR1 匹配——）的 AR(20) R²（过拟合检查——）
print()
print('=== 合成对照（过拟合检查——）===', flush=True)
r1 = np.corrcoef(d[:-1], d[1:])[0,1]
rng = np.random.default_rng(7)
d_ar = np.zeros(N)
d_ar[0] = rng.normal(0, d.std())
for i in range(1, N):
    d_ar[i] = r1*d_ar[i-1] + rng.normal(0, d.std()*np.sqrt(1-r1**2))
print(f'  AR1合成: AR(2) R²={ar_r2(d_ar, 2):.4f}——AR(20) R²={ar_r2(d_ar, 20):.4f}', flush=True)
# 白噪声对照
d_w = rng.normal(0, d.std(), N)
print(f'  白噪声: AR(2) R²={ar_r2(d_w, 2):.4f}——AR(20) R²={ar_r2(d_w, 20):.4f}', flush=True)
