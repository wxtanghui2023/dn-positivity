#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 改进的切换过程验证：追踪"同一个零点"随 N 的连续轨迹（continuation）
# 用 N 的零点作为 N+1 的初始猜测——看 β(N), γ(N) 轨迹——是否趋近 ζ 的零点（β=½）
import mpmath as mp
import numpy as np
mp.mp.dps = 25

def zeta_partial(s, N):
    return mp.nsum(lambda n: n**(-s), [1, N])

def track_zero(start_guess, N_target, steps):
    """从 start_guess 开始——逐步增大 N（continuation）——追踪零点轨迹"""
    z = start_guess
    traj = []
    Ns = np.unique(np.round(np.linspace(steps[0], steps[1], steps[2])).astype(int))
    for N in Ns:
        if N < 2:
            continue
        try:
            def f(s):
                return zeta_partial(s, N)
            z = mp.findroot(f, z, tol=1e-10, maxsteps=60)
            traj.append((N, float(mp.re(z)), float(mp.im(z))))
        except Exception as e:
            traj.append((N, None, None))
    return traj

# 目标：ζ 的前几个零点虚部（已知——γ1=14.13, γ2=21.02, γ3=25.01, γ4=30.42, γ5=32.94）
known_gamma = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351]

print("=== 切换过程：ζ_N 零点随 N 的连续轨迹（continuation——） ===")
# 对每个已知零点附近——在 N=50 找初始零点——然后追踪到 N=200
for gi, gk in enumerate(known_gamma):
    # 初始：N=50 在 γ≈gk 附近找零点
    found = None
    for N0 in [50]:
        # 在 (0.1..0.9, gk±1.5) 区域找零点
        for sigma0 in [0.3, 0.5, 0.7]:
            for t0 in np.arange(gk-1.0, gk+1.0, 0.3):
                s0 = mp.mpc(sigma0, t0)
                try:
                    def f0(s):
                        return zeta_partial(s, N0)
                    r = mp.findroot(f0, s0, tol=1e-10, maxsteps=50)
                    if 0 < float(mp.re(r)) < 1 and abs(float(mp.im(r)) - gk) < 1.0:
                        # 检查是否真的接近 ζ 零点（去重）
                        if found is None or abs(r - found) > 0.2:
                            found = r
                            break
                except Exception:
                    pass
            if found is not None:
                break
        if found is not None:
            break
    if found is None:
        print(f"\nζ 零点 γ≈{gk}: 未在 N=50 找到对应零点")
        continue
    print(f"\nζ 零点 γ≈{gk}: 从 N=50 的 ρ = {float(mp.re(found)):.4f} + {float(mp.im(found)):.4f}i 追踪——")
    traj = track_zero(found, 200, (50, 200, 16))
    for N, b, g in traj:
        if b is not None:
            print(f"   N={N:>4}: β = {b:+.4f}  γ = {g:.4f}  (ζ 的 γ = {gk:.2f})")
