#!/usr/bin/env python3
# 定量验证：u=Re ζ=0 的密度（沿 t——）随 σ 的衰减——是否遵循 ζ(2σ) 类定律？
import mpmath as mp
import numpy as np
mp.mp.dps = 15

def count_u0(sg, t_max=100.0, step=0.05):
    """数 u=Re ζ 沿 t（0.5 到 t_max）的过零次数"""
    cnt = 0
    ts = np.arange(0.5, t_max, step)
    prev = None
    for t in ts:
        u = float(mp.re(mp.zeta(complex(sg, t))))
        if prev is not None and prev*u < 0:
            cnt += 1
        prev = u
    return cnt

print("=== u=0 密度随 σ（t 到 100——）vs ζ(2σ) ===")
print("σ       u=0 计数     ζ(2σ)     log10 计数")
for sg in np.arange(0.30, 0.95, 0.05):
    cnt = count_u0(sg)
    z2s = float(mp.zeta(2*sg))
    print(f"{sg:.2f}   {cnt:>6}      {z2s:>8.3f}    {np.log10(cnt+1):.3f}")
