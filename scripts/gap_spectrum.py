#!/usr/bin/env python3
"""物理工具选择：判定 ζ 的"谱隙状态"——ρ_j 的衰减率（指数 vs 幂律）
指数衰减（谱隙——有隙系统——强刚性工具可用）
幂律衰减（无隙——临界——需要"打开能隙"工具）
"""
import numpy as np
import math
from math import log, pi
import gc

def load_zeros(n):
    path = '/home/node/.openclaw/workspace/dn-project/zeros/zeros6'
    z = np.zeros(n)
    with open(path) as f:
        for i in range(n):
            z[i] = float(f.readline())
    return z

z = load_zeros(1000000)
gz = z[:-1]

dg = np.diff(z)
Np = np.log(gz/(2*pi))/(2*pi)
delta = dg - 1.0/Np
del dg, Np, gz
gc.collect()

d = delta - np.mean(delta)
s2 = np.var(delta)

# ρ_j 的衰减——指数 vs 幂律
print("ρ_j 的衰减率（谱隙判定）：")
print(f"{'lag':>6} {'ρ_j':>10} {'log|ρ|':>10} {'log(lag)':>10}")
lags = [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
rhos = []
for lag in lags:
    rho = np.mean(d[:-lag]*d[lag:])/s2
    rhos.append(rho)
    print(f"{lag:6d} {rho:+10.5f} {log(abs(rho)) if rho!=0 else 0:10.4f} {log(lag):10.4f}")

# 指数拟合：log|ρ| vs lag（直线 = 指数）
lags_a = np.array(lags[3:], dtype=float)  # 跳过小 lag
rhos_a = np.array([abs(r) for r in rhos[3:]])
A = np.vstack([lags_a, np.ones(len(lags_a))]).T
coef_exp = np.linalg.lstsq(A, np.log(rhos_a), rcond=None)[0]
print(f"\n指数拟合：log|ρ| ≈ {coef_exp[0]:.5f}·lag + {coef_exp[1]:.3f}")
print(f"  衰减率 λ = {-coef_exp[0]:.5f}（λ>0 = 指数衰减——谱隙——强刚性）")

# 幂律拟合：log|ρ| vs log(lag)（直线 = 幂律）
A2 = np.vstack([np.log(lags_a), np.ones(len(lags_a))]).T
coef_pow = np.linalg.lstsq(A2, np.log(rhos_a), rcond=None)[0]
print(f"幂律拟合：log|ρ| ≈ {coef_pow[0]:.3f}·log(lag) + {coef_pow[1]:.3f}")
print(f"  幂指数 α = {-coef_pow[0]:.3f}（α>0 = 幂律衰减——无隙——临界）")

# 比较 R²
resid_exp = np.sum((np.log(rhos_a) - (coef_exp[0]*lags_a + coef_exp[1]))**2)
resid_pow = np.sum((np.log(rhos_a) - (coef_pow[0]*np.log(lags_a) + coef_pow[1]))**2)
print(f"\n残差：指数 = {resid_exp:.4f} vs 幂律 = {resid_pow:.4f}")
print(f"{'指数衰减（谱隙——强刚性）' if resid_exp < resid_pow else '幂律衰减（无隙——临界——需打开能隙）'}")

del delta, d
gc.collect()
print("内存已释放")
