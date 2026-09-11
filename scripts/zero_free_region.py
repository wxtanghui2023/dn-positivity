#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 扩展验证：σ∈(½,1)——t∈(0,200)——确认无零点（u=v=0 共同——）+ 错开间隙
import mpmath as mp
import numpy as np
mp.mp.dps = 15

print("=== σ>½ 无零点扩展验证（t 到 200——）===")
# 对 σ 网格——找 u=0 和 v=0 的 t——检查共同点
for sg in [0.55, 0.60, 0.65, 0.70, 0.75, 0.80]:
    u0s, v0s = [], []
    ts = np.arange(2, 200, 0.05)
    prev_u = prev_v = None
    for t in ts:
        s = complex(sg, t)
        u = float(mp.re(mp.zeta(s))); v = float(mp.im(mp.zeta(s)))
        if prev_u is not None:
            if prev_u*u < 0: u0s.append((t+prev_t)/2)
            if prev_v*v < 0: v0s.append((t+prev_t)/2)
        prev_u, prev_v, prev_t = u, v, t
    # 共同零点检查
    common = []
    min_gap = 1e9
    for su in u0s:
        # 找最近的 v0
        dv = min(abs(su-sv) for sv in v0s)
        min_gap = min(min_gap, dv)
        if dv < 0.03: common.append(su)
    print(f"σ={sg}: u=0@{len(u0s)}  v=0@{len(v0s)}  最近间隙={min_gap:.4f}  共同零点={len(common)}")
