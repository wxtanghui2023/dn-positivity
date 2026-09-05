#!/usr/bin/env python3
# 单调性机制：追踪 u=0 与 v=0 的 t 位置随 σ（σ>½——）——看漂移结构
import mpmath as mp
import numpy as np
mp.mp.dps = 15

def u_of(s): return float(mp.re(mp.zeta(s)))
def v_of(s): return float(mp.im(mp.zeta(s)))

def find_zeros_line(sg, t_range, step=0.2):
    """沿固定 σ 线——找 u=0 和 v=0 的 t（粗扫+二分精化）"""
    u0s, v0s = [], []
    ts = np.arange(t_range[0], t_range[1], step)
    prev_u = prev_v = None
    for t in ts:
        u = u_of(complex(sg, t)); v = v_of(complex(sg, t))
        if prev_u is not None:
            if prev_u*u < 0:
                # 二分精化 u=0
                lo, hi = prev_t, t
                for _ in range(25):
                    mid = (lo+hi)/2
                    if u_of(complex(sg, lo))*u_of(complex(sg, mid)) < 0: hi = mid
                    else: lo = mid
                u0s.append((lo+hi)/2)
            if prev_v*v < 0:
                lo, hi = prev_t, t
                for _ in range(25):
                    mid = (lo+hi)/2
                    if v_of(complex(sg, lo))*v_of(complex(sg, mid)) < 0: hi = mid
                    else: lo = mid
                v0s.append((lo+hi)/2)
        prev_u, prev_v, prev_t = u, v, t
    return u0s, v0s

print("=== u=0 与 v=0 的 t 位置随 σ（追踪漂移——）===")
# 追踪几个特定的 u=0 点（σ=0.55 处的——）随 σ
print("\n--- u=0 点追踪（从 σ=0.55 开始——continuation）---")
# 在 σ=0.55 找 u=0 点——然后随 σ 追踪
u0s_055, v0s_055 = find_zeros_line(0.55, (5, 60))
print(f"σ=0.55: u=0 在 t={[f'{t:.2f}' for t in u0s_055]}")
print(f"σ=0.55: v=0 在 t={[f'{t:.2f}' for t in v0s_055[:8]]}...（共{len(v0s_055)}）")

# 追踪前几个 u=0 点随 σ（continuation——从 0.55 的——）
seeds = u0s_055[:5]
print("\n追踪 u=0 点的 t(σ)——")
for sg in [0.56, 0.58, 0.60, 0.63, 0.66, 0.70]:
    u0s, v0s = find_zeros_line(sg, (5, 80), step=0.3)
    print(f"σ={sg}: u=0 在 t={[f'{t:.1f}' for t in u0s[:8]]}（共{len(u0s)}）  v=0 前几个 {[f'{t:.1f}' for t in v0s[:5]]}")
