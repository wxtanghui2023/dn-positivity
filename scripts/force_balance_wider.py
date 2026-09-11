#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 更广验证：ζ_X 临界带零点（0<σ<1）是否都在 σ<½？——X=100,200——t 到 100
import numpy as np

def zeta_smooth_vec(s, X, nmax_factor=15):
    nmax = max(int(nmax_factor*X), 400)
    n = np.arange(1, nmax+1, dtype=np.float64)
    logn = np.log(n)
    s_c = complex(s)
    ns = np.exp(-s_c * logn)
    w = np.exp(-n/X)
    return np.sum(ns * w)

def refine(seed, X):
    z = complex(seed)
    for it in range(80):
        f = zeta_smooth_vec(z, X)
        h = 1e-6 + 1e-6j
        fp = (zeta_smooth_vec(z+h, X) - zeta_smooth_vec(z-h, X))/(2*h)
        step = f/fp
        z = z - step
        if abs(step) < 1e-12: break
    return z

def find_strip_zeros(X, t_max=100.0):
    """临界带零点（0<σ<1, 0.5<t<t_max）——网格+精化+去重"""
    zeros = []
    # 用 ζ 的已知零点虚部做种子（追踪——更可靠）
    # 先粗网格找低值区
    cands = []
    for sg in np.arange(0.05, 1.0, 0.08):
        for t in np.arange(2, t_max, 0.5):
            v = abs(zeta_smooth_vec(complex(sg, t), X))
            if v < 0.5:
                cands.append((sg, t, v))
    cands.sort(key=lambda c: c[2])
    for sg, t, v in cands:
        try:
            z = refine(complex(sg, t), X)
            if 0 < z.real < 1 and z.imag > 1:
                dup = any(abs(z - z2) < 0.05 for z2 in zeros)
                if not dup:
                    zeros.append(z)
        except Exception:
            pass
    return sorted(zeros, key=lambda z: z.imag)

print("=== 更广验证：ζ_X 临界带零点 β 分布（X=100, 200——） ===")
for X in [100, 200]:
    zs = find_strip_zeros(X)
    if not zs:
        print(f"X={X}: 未找到零点")
        continue
    betas = [z.real for z in zs]
    gams = [z.imag for z in zs]
    maxb = max(betas)
    over = [i for i, b in enumerate(betas) if b > 0.5]
    print(f"\nX={X}: {len(zs)} 个临界带零点——β ∈ [{min(betas):.4f}, {maxb:.4f}]——max β = {maxb:.4f}")
    print(f"  β > ½ 的零点数: {len(over)}")
    # 与 ζ 零点比较（前几个 γ）
    print(f"  前 8 个: " + ", ".join(f"{b:.3f}+{g:.1f}i" for b, g in zip(betas[:8], gams[:8])))
