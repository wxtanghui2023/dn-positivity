#!/usr/bin/env python3
# 平滑截断快速版（numpy 向量化）——ζ_X(s) = Σ n^{-s} e^{-n/X}——零点轨迹
import numpy as np
import mpmath as mp

def zeta_smooth_vec(s, X, nmax_factor=25):
    """向量化：Σ_{n<=nmax} n^{-s} e^{-n/X}——用 mpmath 在最后精化"""
    nmax = max(int(nmax_factor*X), 200)
    n = np.arange(1, nmax+1, dtype=np.float64)
    # log(n) * (-s) = 复数——n^{-s} = exp(-s log n)
    logn = np.log(n)
    s_c = complex(s)
    # 向量化复数幂——精度 float64 够初筛
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def track_zero_fast(start, X_list, tol=1e-8):
    """粗追踪（numpy 向量化 + mpmath 精化）"""
    z = complex(start)
    traj = []
    for X in X_list:
        try:
            # 牛顿迭代（numpy 函数 + 数值导数）
            for it in range(40):
                f = zeta_smooth_vec(z, X)
                # 数值导数（复）
                h = 1e-6 + 1e-6j
                fp = (zeta_smooth_vec(z+h, X) - zeta_smooth_vec(z-h, X)) / (2*h)
                step = f/fp
                z = z - step
                if abs(step) < tol:
                    break
            # mpmath 精化
            zm = mp.mpc(z.real, z.imag)
            def fmp(s):
                return zeta_smooth_mp(s, X)
            zm = mp.findroot(fmp, zm, tol=1e-12, maxsteps=30)
            traj.append((X, float(zm.real), float(zm.imag)))
        except Exception as e:
            traj.append((X, None, None))
    return traj

def zeta_smooth_mp(s, X):
    nmax = max(int(25*X), 200)
    total = mp.mpc(0)
    for k in range(1, nmax+1):
        total += mp.mpf(k)**(-s) * mp.e**(-mp.mpf(k)/X)
    return total

seeds = [(0.5, 14.1347), (0.5, 21.0220), (0.5, 25.0109)]
X_list = [5, 10, 15, 20, 30, 40, 60, 80, 100, 150, 200]

print("=== 平滑截断 ζ_X(s)——零点轨迹（X 增大——） ===")
for (b0, g0) in seeds:
    print(f"\n--- 种子 ρ ≈ {b0} + {g0}i ---")
    traj = track_zero_fast(complex(b0, g0), X_list)
    for X, b, g in traj:
        if b is not None:
            print(f"   X={X:>4}: β = {b:+.4f}  γ = {g:.4f}  (目标 γ = {g0:.2f})")
        else:
            print(f"   X={X:>4}: 追踪失败")
