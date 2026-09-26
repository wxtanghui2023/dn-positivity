#!/usr/bin/env python3
"""B: 由 Kamenetsky (10,120)_1 缩短 + 贪心修复 + 去冗余，构造 (9,M)_1 覆盖码并算 Q"""
import itertools, random
from collections import Counter
W10=[int(x,2) for x in open('/home/node/.openclaw/workspace/dn-project/work/k10/kamenetsky120.txt').read().split()]
n=9; N=1<<n
def ball_mask(x,nn):
    m=1<<x
    for i in range(nn): m|=1<<(x^(1<<i))
    return m
BM=[ball_mask(x,n) for x in range(N)]
def covering(C):
    cov=0
    for c in C: cov|=BM[c]
    return cov==(1<<N)-1
def Q_of(C):
    cm=0
    for c in C: cm|=1<<c
    b=[bin(BM[x]&cm).count('1') for x in range(N)]
    return (sum((v-1)*(v-2)//2 for v in b), min(b), max(b), Counter(b).most_common(3))
best=None
for i in range(10):
    for v in (0,1):
        C=[(w>>(9-i))<<i | (w & ((1<<i)-1)) for w in W10 if (w>>(9-i))&1==v] if False else []
        # 删去第 i 位（0-based, 高位优先）
        C=[]
        for w in W10:
            bit=(w>>(9-i))&1
            if bit==v:
                lo=w & ((1<<i)-1); hi=(w>>(i+1))
                C.append((hi<<i)|lo)
        C=set(C)
        # 贪心修复
        while not covering(C):
            cov=0
            for c in C: cov|=BM[c]
            unc=[x for x in range(N) if not (cov>>x)&1]
            best_w=None; best_gain=-1
            for cand in unc:
                gain=0
                for y in range(N):
                    if BM[cand]>>y&1 and not (cov>>y)&1: gain+=1
                if gain>best_gain: best_gain=gain; best_w=cand
            C.add(best_w)
        # 去冗余
        changed=True
        while changed:
            changed=False
            for c in list(C):
                C2=C-{c}
                if covering(C2): C=C2; changed=True; break
        q,mb,xb,top=Q_of(C)
        print(f"  坐标{i} 值{v}: M={len(C)}  Q={q}  min b={mb} max b={xb}")
        if best is None or len(C)<best[0]: best=(len(C),q,i,v)
print(f"\n最优(最小 M): M={best[0]}, Q={best[1]}, 坐标{best[2]}, 值{best[3]}")
print(f"（K(9,1) 文献记 62 ⚠️；C1/parity 预测: n=9 为奇 ⟹ E=M*10-512 ⟹ Q 偶 ⟹ C1 预测 Q≥2）")
