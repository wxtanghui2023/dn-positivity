#!/usr/bin/env python3
# 验证：ζ_X(s) = Σ n^{-s} e^{-n/X} 的零点（临界带内）是否都在 β < ½？
# 力的平衡命题：零点集在左侧（β<½）——从不越过 ½
import numpy as np
import mpmath as mp
mp.mp.dps = 20

def zeta_smooth_mp(s, X):
    nmax = max(int(20*X), 200)
    total = mp.mpc(0)
    for k in range(1, nmax+1):
        total += mp.mpf(k)**(-s) * mp.e**(-mp.mpf(k)/X)
    return total

def find_zeros(X, sigma_range=(0.0, 1.0), t_max=50.0):
    """粗网格找 ζ_X 零点（临界带——）"""
    zeros = []
    sigmas = np.arange(sigma_range[0]+0.01, sigma_range[1], 0.06)
    ts = np.arange(0.5, t_max, 0.3)
    for sg in sigmas:
        for t in ts:
            s0 = mp.mpc(sg, t)
            try:
                val = zeta_smooth_mp(s0, X)
                if abs(val) < 0.15:
                    def f(z):
                        return zeta_smooth_mp(z, X)
                    root = mp.findroot(f, s0, tol=1e-10, maxsteps=40)
                    r = root
                    dup = any(abs(r-z2) < 0.08 for z2 in zeros)
                    if not dup and 0 < float(mp.re(r)) < 1 and float(mp.im(r)) > 0.1:
                        zeros.append(r)
            except Exception:
                pass
    return sorted(zeros, key=lambda z: float(mp.im(z)))

print("=== 力的平衡命题验证：ζ_X 零点都在 β < ½？ ===")
for X in [8, 20, 50, 100]:
    zs = find_zeros(X)
    if not zs:
        print(f"X={X}: 临界带内无零点找到")
        continue
    betas = [float(mp.re(z)) for z in zs]
    gams = [float(mp.im(z)) for z in zs]
    maxb = max(betas)
    print(f"\nX={X}: {len(zs)} 个零点——β 范围 [{min(betas):.4f}, {maxb:.4f}]——max β = {maxb:.4f}")
    over = [i for i,b in enumerate(betas) if b > 0.5]
    if over:
        print(f"  ⚠️ 有 {len(over)} 个零点 β > ½！")
        for i in over[:5]:
            print(f"    ρ = {betas[i]:.4f} + {gams[i]:.4f}i")
    else:
        print(f"  ✓ 全部零点 β < ½")
    # 列出几个
    for i in range(min(5, len(zs))):
        print(f"    ρ_{i+1} = {betas[i]:.4f} + {gams[i]:.4f}i")
