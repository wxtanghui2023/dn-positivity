#!/usr/bin/env python3
"""δ 的 R/S 分析——赫斯特指数（分形时间序列）
如果 H < 0.5——反持久（均值回归）——Σδ = O(1) 的解释
H → 0——完全反持久（完全刚性）
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

z = load_zeros(1000000)

dg = np.diff(z)
Np = np.log(z[:-1]/(2*pi))/(2*pi)
delta = dg - 1.0/Np
d = delta - np.mean(delta)

def RS_analysis(series, scales):
    """R/S 分析：对每个尺度 n，计算 R/S"""
    results = []
    for n in scales:
        n = int(n)
        nblocks = len(series)//n
        if nblocks < 3: break
        RS_vals = []
        for i in range(nblocks):
            block = series[i*n:(i+1)*n]
            mean = np.mean(block)
            cumdev = np.cumsum(block - mean)
            R = np.max(cumdev) - np.min(cumdev)
            S = np.std(block)
            if S > 0:
                RS_vals.append(R/S)
        results.append((n, np.mean(RS_vals)))
    return results

scales = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
rs = RS_analysis(d, scales)
print("R/S 分析（δ 序列）：")
print(f"{'n':>8} {'R/S':>10} {'log n':>8} {'log R/S':>8}")
for n, rsv in rs:
    print(f"{n:8d} {rsv:10.3f} {log(n):8.3f} {log(rsv):8.3f}")

# H 拟合
ns = np.array([n for n, _ in rs], dtype=float)
rsvs = np.array([v for _, v in rs], dtype=float)
A = np.vstack([np.log(ns), np.ones(len(ns))]).T
coef = np.linalg.lstsq(A, np.log(rsvs), rcond=None)[0]
print(f"\nH = {coef[0]:.3f}（R/S ~ n^H）")
print(f"  H < 0.5：反持久（均值回归）——Σδ = O(1) 的解释")
print(f"  H ≈ 0：完全反持久——完全刚性")

# 对比：白噪声的 H ≈ 0.5
rng = np.random.default_rng(42)
white = rng.standard_normal(len(d))
rs_w = RS_analysis(white, scales)
ns_w = np.array([n for n, _ in rs_w], dtype=float)
rsv_w = np.array([v for _, v in rs_w], dtype=float)
A_w = np.vstack([np.log(ns_w), np.ones(len(ns_w))]).T
coef_w = np.linalg.lstsq(A_w, np.log(rsv_w), rcond=None)[0]
print(f"\n白噪声 H = {coef_w[0]:.3f}（应 ≈ 0.5——对照）")
