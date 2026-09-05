#!/usr/bin/env python3
# 运动机制深入：不同"筛/平滑"的零点运动——终点普适性？
# 筛的变体：①指数 e^{-n/X} ②高斯 e^{-(n/X)^2} ③幂 e^{-(n/X)^0.5}
# 每种筛——追踪 γ1 零点随"尺度参数"的运动——看终点（是否都 ½——）
import numpy as np

def zeta_smooth_generic(s, X, kind='exp', nmax_factor=15):
    """ζ_X(s) = Σ n^{-s} w(n/X)——不同权重"""
    nmax = max(int(nmax_factor*X), 300)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    if kind == 'exp':
        w = np.exp(-n/X)
    elif kind == 'gauss':
        w = np.exp(-(n/X)**2)
    elif kind == 'sqrt':
        w = np.exp(-np.sqrt(n/X))
    elif kind == 'power2':
        w = np.exp(-(n/X)**2)  # same as gauss
    return np.sum(ns * w)

def beta_at(X, gamma, kind, beta_guess=0.5):
    """找 ζ_X（kind 筛——）在 γ≈gamma 的零点实部"""
    z = complex(beta_guess, gamma)
    for it in range(60):
        f = zeta_smooth_generic(z, X, kind)
        h = 1e-6 + 1e-6j
        fp = (zeta_smooth_generic(z+h, X, kind) - zeta_smooth_generic(z-h, X, kind))/(2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-10:
            break
    return z.real

gamma1 = 14.1347
print("=== 不同筛的零点运动（γ1——β(X) 随尺度——）终点普适性 ===")
print("X       exp(指数)   gauss(高斯)   sqrt(慢衰减)")
# 不同筛的"有效尺度"不同——用各自 X 的 β
for X in [10, 30, 60, 100, 200]:
    row = []
    for kind in ['exp', 'gauss', 'sqrt']:
        b = beta_at(X, gamma1, kind)
        row.append(f"{b:.4f}")
    print(f"{X:>4}    {row[0]}      {row[1]}      {row[2]}")
