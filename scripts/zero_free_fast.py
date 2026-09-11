#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 聚焦快速版：粗扫找 u 过零区间 → 精化 u=0 → 只在这些点算 v（快——）
import mpmath as mp
import numpy as np
mp.mp.dps = 15

print("=== σ>½ 无零点验证（聚焦——t 到 200——）===")
for sg in [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85]:
    # 粗扫（步长 0.5——）找 u 过零区间
    intervals = []
    ts = np.arange(2, 200, 0.5)
    prev_u = None
    for t in ts:
        u = float(mp.re(mp.zeta(complex(sg, t))))
        if prev_u is not None and prev_u*u < 0:
            intervals.append((t-0.5, t))
        prev_u = u
    # 精化每个区间的 u=0 点——算 v
    min_abs_v = 1e9; n_close = 0; n_u0 = 0
    for (a, b) in intervals:
        # 二分找 u=0
        lo, hi = a, b
        for _ in range(30):
            mid = (lo+hi)/2
            um = float(mp.re(mp.zeta(complex(sg, mid))))
            ul = float(mp.re(mp.zeta(complex(sg, lo))))
            if ul*um < 0: hi = mid
            else: lo = mid
        t0 = (lo+hi)/2
        v0 = abs(float(mp.im(mp.zeta(complex(sg, t0)))))
        n_u0 += 1
        min_abs_v = min(min_abs_v, v0)
        if v0 < 0.05: n_close += 1
    print(f"σ={sg}: u=0 点 {n_u0} 个——min|v| = {min_abs_v:.5f}——|v|<0.05 的 {n_close} 个{'⚠️ 接近零点!' if n_close else '（全错开✓）'}")
