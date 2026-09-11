#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 切换过程候选 2：平滑截断 ζ_X(s) = Σ_{n>=1} n^{-s} e^{-n/X}
# X 增大——零点轨迹（continuation）——是否"形成"到 ζ 的零点（β=½, γ=14.13...）
import mpmath as mp
import numpy as np
mp.mp.dps = 20

def zeta_smooth(s, X, nmax_factor=30):
    """Σ_{n<=nmax} n^{-s} e^{-n/X}——nmax = 30X（e^{-30} 可忽略）"""
    nmax = max(int(30*X), 100)
    n = np.arange(1, nmax+1)
    # 用 mpmath 逐项（numpy 复数精度不够 dps20）
    total = mp.mpc(0)
    for k in n:
        total += mp.mpf(k)**(-s) * mp.e**(-mp.mpf(k)/X)
    return total

def track_zero(start_guess, X_list):
    z = start_guess
    traj = []
    for X in X_list:
        try:
            def f(s):
                return zeta_smooth(s, X)
            z = mp.findroot(f, z, tol=1e-9, maxsteps=50)
            traj.append((X, float(mp.re(z)), float(mp.im(z))))
        except Exception as e:
            traj.append((X, None, None))
    return traj

# 初始猜测：ζ 的前几个零点（γ1=14.13, γ2=21.02, γ3=25.01——）
seeds = [(0.5, 14.1347), (0.5, 21.0220), (0.5, 25.0109), (0.5, 30.4249)]
X_list = [10, 20, 30, 50, 80, 120, 200, 300, 500]

print("=== 平滑截断 ζ_X(s) = Σ n^{-s} e^{-n/X}——零点轨迹（X 增大——） ===")
for (b0, g0) in seeds:
    print(f"\n--- 种子 ρ ≈ {b0} + {g0}i（ζ 零点——） ---")
    traj = track_zero(mp.mpc(b0, g0), X_list)
    for X, b, g in traj:
        if b is not None:
            print(f"   X={X:>4}: β = {b:+.4f}  γ = {g:.4f}  (目标 γ = {g0:.2f})")
        else:
            print(f"   X={X:>4}: 追踪失败")
