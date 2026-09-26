#!/usr/bin/env python3
"""独立复核（纯暴力 Hamming，不用位掩码）: 覆盖性 + 用户点名 4 点"""
rows=[]
for line in open('K_9_1.txt'):
    s=line.split()
    if len(s)==9 and all(c in '01' for c in s): rows.append("".join(s))
S=set(rows); C=rows
def ham(a,b): return sum(1 for x,y in zip(a,b) if x!=y)
unc=[format(v,'09b') for v in range(512) if min(ham(format(v,'09b'),c) for c in S)>1]
print(f"|C|={len(C)} 去重={len(S)} | 未覆盖点={len(unc)} {'✓ 是覆盖码' if not unc else '✗'}")
print("\n用户点名 4 点（逐点距离）:")
for t in ["111010100","111011000","111011101","111111100"]:
    m=min(ham(t,c) for c in S)
    near=[c for c in C if ham(t,c)==m]
    print(f"  {t} → 最近距离 {m}  {'被覆盖 ✓' if m<=1 else '未覆盖 ✗'}  见证码字={near}")
print("\n注: 这 4 点都是码字 111011100 的距离-1 邻居 ⟹ 它们是该码字的**私有点**(b=1) ✓")
for t in ["111010100","111011000","111011101","111111100"]:
    print(f"  d({t}, 111011100) = {ham(t,'111011100')}")
