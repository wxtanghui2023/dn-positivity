#!/usr/bin/env python3
# 零曲线几何：u=Reζ=0 与 v=Imζ=0 曲线（临界带——）——结构/错开
import mpmath as mp
import numpy as np
mp.mp.dps = 15

# 细网格扫描——记录 u 和 v 沿 t（固定 σ）的符号变化（= 零曲线的 t 位置）
print("=== u=0 与 v=0 曲线（t 位置随 σ——）===")
print("σ       u=0 的 t 位置（前若干——）")
sigmas = np.arange(0.05, 1.0, 0.05)
for sg in sigmas:
    u0_ts, v0_ts = [], []
    ts = np.arange(0.5, 60, 0.1)
    prev_u = zeta_u = None
    for i, t in enumerate(ts):
        s = complex(sg, t)
        u = float(mp.re(mp.zeta(s)))
        v = float(mp.im(mp.zeta(s)))
        if i > 0:
            if prev_u * u < 0: u0_ts.append((t+prev_t)/2)
            if prev_v * v < 0: v0_ts.append((t+prev_t)/2)
        prev_u, prev_v, prev_t = u, v, t
    # 只打印有 u=0 的 σ
    if u0_ts:
        # 压缩显示（前 6 个 + 计数）
        shown = [f"{x:.1f}" for x in u0_ts[:6]]
        print(f"{sg:.2f}   u=0@{len(u0_ts)}: {shown}{'...' if len(u0_ts)>6 else ''}")
    else:
        print(f"{sg:.2f}   u=0 无")
