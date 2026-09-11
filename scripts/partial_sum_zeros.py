#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# "切换过程"实验：部分和 ζ_N(s) = Σ_{n<=N} n^{-s} 的零点——N 增大——零点实部如何移动？
# 问题：正整数的离散和（X 轴）→ 零点的"切换"——β 的轨迹是否揭示 β=½ 的选择？
import mpmath as mp
import numpy as np

mp.mp.dps = 25

def zeta_partial(s, N):
    """Σ_{n=1..N} n^{-s}"""
    return mp.nsum(lambda n: n**(-s), [1, N])

def find_zeros_partial(N, sigma_range=(0.0, 1.0), t_max=40.0):
    """找 ζ_N 在临界带内的零点（粗网格 + 牛顿）"""
    zeros = []
    # 粗网格扫描找符号变化（实部/虚部同时为零）
    sigmas = np.arange(sigma_range[0], sigma_range[1], 0.05)
    ts = np.arange(0.5, t_max, 0.2)
    for sg in sigmas:
        for t in ts:
            s = mp.mpc(sg, t)
            try:
                val = zeta_partial(s, N)
                if abs(val) < 0.05:  # 粗筛——接近零点
                    # 牛顿迭代精化
                    def f(z):
                        return zeta_partial(z, N)
                    try:
                        root = mp.findroot(f, s, tol=1e-12, maxsteps=50)
                        # 去重
                        dup = False
                        for r in zeros:
                            if abs(root - r) < 0.05:
                                dup = True
                                break
                        if not dup and 0 < float(mp.re(root)) < 1 and float(mp.im(root)) > 0:
                            zeros.append(root)
                    except Exception:
                        pass
            except Exception:
                pass
    return sorted(zeros, key=lambda z: float(mp.im(z)))

print("=== ζ_N(s) = Σ_{n<=N} n^{-s} 的零点（临界带内）——N 增大——β 轨迹 ===")
for N in [5, 10, 20, 30, 50, 80, 120]:
    zs = find_zeros_partial(N)
    if zs:
        betas = [float(mp.re(z)) for z in zs]
        gammas = [float(mp.im(z)) for z in zs]
        print(f"\nN={N}: {len(zs)} zeros in (0,1)x(0,40)")
        for z, b, g in zip(zs, betas, gammas):
            print(f"   ρ = {b:.4f} + {g:.4f}i")
    else:
        print(f"\nN={N}: no zeros found in strip")
