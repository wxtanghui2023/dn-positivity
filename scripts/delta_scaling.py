#!/usr/bin/env python3
"""发散性思维检查：Σδ_k 的标度律——O(1)？O(log N)？N^H（亚扩散）？
物理类比：反持久性时间序列（H≈0.2——8/22发现）——亚扩散
如果 Σδ ~ N^H——H 是多少？——决定"刚性"的强度
"""
import numpy as np
import math
from math import log, pi

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

K = 2000000
z = load_zeros(K)

dg = np.diff(z)
Np = np.log(z[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np

Sd = np.cumsum(delta)

# 不同 N 的 max|Σδ|
print("Σδ_k 的标度律（max|Σδ| 随 N）：")
print(f"{'N':>10} {'max|Σδ|':>10} {'log N':>8} {'max/log N':>10}")
for N in [10**3, 10**4, 10**5, 5*10**5, 10**6, 2*10**6]:
    mx = np.max(np.abs(Sd[:N]))
    print(f"{N:10d} {mx:10.3f} {log(N):8.3f} {mx/log(N):10.3f}")

# 赫斯特指数拟合：max|Σδ| ~ N^H
print("\nH 拟合（log max vs log N）：")
Ns = np.array([10**3, 10**4, 10**5, 5*10**5, 10**6, 2*10**6], dtype=float)
mxs = np.array([np.max(np.abs(Sd[:int(N)])) for N in Ns], dtype=float)
A = np.vstack([np.log(Ns), np.ones(len(Ns))]).T
coef = np.linalg.lstsq(A, np.log(mxs), rcond=None)[0]
print(f"  log(max|Σδ|) ≈ {coef[0]:.3f}·log N + {coef[1]:.3f}")
print(f"  H = {coef[0]:.3f}（0 = O(1)——0.5 = 随机游走——0.2 = 亚扩散）")

# 对比：随机游走（打乱 δ）
rng = np.random.default_rng(42)
shuffled = rng.permutation(delta)
Sd_shuf = np.cumsum(shuffled)
mx_shuf = np.max(np.abs(Sd_shuf[:100000]))
print(f"\n随机游走对比（打乱 δ——N=1e5）：max|Σδ| = {mx_shuf:.1f} vs 真实 {np.max(np.abs(Sd[:100000])):.2f}")
print(f"压缩比 = {mx_shuf/np.max(np.abs(Sd[:100000])):.0f} 倍")
