#!/usr/bin/env python3
"""对 unc=2 候选做**完整 1-flip 扫描**（精确、廉价）：是否有单次单词替换可灭两洞 ⟹ k=119 witness?"""
import json
n = 10; N = 1 << n
d = json.load(open("/home/node/.openclaw/workspace/dn-project/work/k10/p2k119_best.json"))
S = sorted(set(d["code"]))
BALL = [[y for y in range(N) if bin(y ^ p).count('1') <= 1] for p in range(N)]

def unc_of(lst):
    cnt = [0]*N
    for p in lst:
        for y in BALL[p]: cnt[y] += 1
    return [y for y in range(N) if cnt[y] == 0]

base = unc_of(S)
print("base unc =", base)
print("d(473,507) =", bin(473 ^ 507).count('1'))

Sset = set(S)
best = (len(base), None)
hit = None
for p in S:
    for cp in range(N):
        if cp in Sset: continue
        new = list(S); new.remove(p); new.append(cp)
        u = unc_of(new)
        if len(u) < best[0]:
            best = (len(u), (p, cp)); 
        if not u:
            hit = (p, cp); break
    if hit: break
print("1-flip 最优 =", best)
if hit:
    print("*** 1-flip WITNESS FOUND: 删 %d 加 %d ***" % hit)
    print("VERIFY_WITNESS")
else:
    print("1-flip 无 witness（unc 最小值 = %d）⟹ 单字邻域确为平台 ✓" % best[0])
print("FLIP_SCAN_DONE")
