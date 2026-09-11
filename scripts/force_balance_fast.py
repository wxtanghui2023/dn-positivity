#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 快速版：ζ_X 零点是否都在 β<½？（numpy 向量化——定性判断）
import numpy as np

def zeta_smooth_vec(s, X, nmax_factor=20):
    nmax = max(int(nmax_factor*X), 200)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def grid_scan(X, sigma_range=(0.0, 1.0), t_max=50.0, threshold=0.3):
    """粗网格——找 |ζ_X| 小的区域（零点候选）——统计 β"""
    sigmas = np.arange(sigma_range[0]+0.02, sigma_range[1], 0.04)
    ts = np.arange(0.5, t_max, 0.2)
    cands = []
    for sg in sigmas:
        for t in ts:
            v = abs(zeta_smooth_vec(complex(sg, t), X))
            if v < threshold:
                cands.append((sg, t, v))
    return cands

print("=== 力的平衡命题（快速验证）：ζ_X 零点 β 分布 ===")
for X in [5, 10, 20, 50]:
    cands = grid_scan(X)
    print(f"\nX={X}: {len(cands)} 个低值候选（|ζ|<0.3——）")
    if cands:
        # 按 |ζ| 排序取前 15 个最可能的零点
        cands.sort(key=lambda c: c[2])
        betas = [c[0] for c in cands[:15]]
        print(f"  最可能零点候选的 β：{[f'{b:.3f}' for b in betas]}")
        over = [b for b in betas if b > 0.5]
        print(f"  β > ½ 的候选数：{len(over)}")
