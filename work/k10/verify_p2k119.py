#!/usr/bin/env python3
"""独立复核 p2k119_best.json：|C|=119? 覆盖 1024/1024? 未覆盖点 = ? 1-flip 可行性?"""
import json, itertools

n = 10; N = 1 << n
d = json.load(open("/home/node/.openclaw/workspace/dn-project/work/k10/p2k119_best.json"))
C = d["code"]
print("json.size=%d  json.uncovered=%d  json.witness=%s" % (d["size"], d["uncovered"], d["witness"]))
print("|C|=%d  distinct=%d  in_range=%s" % (len(C), len(set(C)), all(0 <= c < N for c in C)))

S = sorted(set(C))
BALL = [[y for y in range(N) if bin(y ^ p).count('1') <= 1] for p in range(N)]
cnt = [0] * N
for p in S:
    for y in BALL[p]:
        cnt[y] += 1
unc = [y for y in range(N) if cnt[y] == 0]
print("INDEP: 覆盖=%d/1024  未覆盖=%d  => %s" % (N - len(unc), len(unc), unc))
print("witness(unc==0)=%s  |C|==119=%s" % (not unc, len(S) == 119))

# 1-flip 平台核验：能否用单词替换消灭一个洞?
if unc:
    priv = {p: sum(1 for z in BALL[p] if cnt[z] == 1) for p in S}
    print("私有覆盖数 min=%d max=%d（≥2 ⟹ 任一删除至少新开 2 洞）" % (min(priv.values()), max(priv.values())))
    for y in unc:
        # gain: 覆盖洞 y 需要 c' ∈ BALL[y]; 若 c' 已在 S 中则本应已覆盖 y（矛盾）
        cand = [c for c in BALL[y] if c not in set(S)]
        # 距离 ≤1 的两个洞可被同一词覆盖 ⟹ 有共用候选
        print("  洞 y=%d 候选替换词数=%d" % (y, len(cand)))
    if len(unc) == 2:
        inter = set(BALL[unc[0]]) & set(BALL[unc[1]])
        print("  两洞公共 B1 交集 = %s（非空 ⟹ 单次替换可同灭两洞）" % sorted(inter - set(S)))
print("VERIFY_DONE")
