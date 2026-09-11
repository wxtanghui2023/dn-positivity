#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 精确找 ζ'/ζ 的零点（素数运动平衡——）——实部分布
import mpmath as mp
mp.mp.dps = 15

def L(s):
    return mp.diff(mp.zeta, s)/mp.zeta(s)

# 粗网格找 |L| 局部极小（候选零点——）
candidates = []
best = {}
sg_range = mp.arange(0.1, 0.95, 0.05)
t_range = mp.arange(3.0, 40.0, 0.2)
for sg in sg_range:
    for t in t_range:
        try:
            v = L(mp.mpc(sg, t))
            a = abs(v)
            # 记录每 (t 附近——) 的最小
            key = int(t*5)
            if key not in best or a < best[key][0]:
                best[key] = (a, sg, t)
        except:
            pass

# 取真正的极小（|L| 很小——）
print("=== ζ'/ζ 零点候选（|L| 局部极小——）===")
found = []
for key in sorted(best):
    a, sg, t = best[key]
    if a < 0.3:
        found.append((a, sg, t))

# 合并邻近
merged = []
for a, sg, t in found:
    if not merged or t - merged[-1][2] > 0.5:
        merged.append([a, sg, t])
    else:
        if a < merged[-1][0]:
            merged[-1] = [a, sg, t]

print("（粗候选——需精化——）")
for a, sg, t in merged:
    print(f"  t={float(t):.2f}: σ≈{float(sg):.2f} |L|={float(a):.4f}")

# 精化第一个候选（二维——固定 t 扫 σ 更细——）
print()
print("=== 精化：对每个 t 候选——细扫 σ 找 Re=0（ζ'/ζ 零点——）===")
for a0, sg0, t0 in merged[:6]:
    t = t0
    # 沿 t 细扫（找 |L| 极小——）
    tb = t - 0.15
    ta = t + 0.15
    bestv = None
    for tt in mp.arange(tb, ta, 0.02):
        for ss in mp.arange(0.1, 0.95, 0.02):
            try:
                v = L(mp.mpc(ss, tt))
                av = abs(v)
                if bestv is None or av < bestv[0]:
                    bestv = (av, ss, tt)
            except:
                pass
    if bestv and bestv[0] < 0.05:
        print(f"  t={float(bestv[2]):.3f}: σ={float(bestv[1]):.3f} |L|={float(bestv[0]):.2e}")
    else:
        print(f"  t 附近 {float(t):.2f}: 未找到精确零点（|L|min={float(bestv[0]) if bestv else 99}——）")
