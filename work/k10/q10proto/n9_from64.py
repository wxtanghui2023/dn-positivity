#!/usr/bin/env python3
"""B(3): 起点 = doubled(8,32) 码 → (9,64) 覆盖码；再删 2 词（带修复）逼近 62；算 Q"""
import random, itertools
from collections import Counter
n=9; N=1<<n
NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
BM=[1<<x for x in range(N)]
for x in range(N):
    for y in NB[x]: BM[x]|=1<<y
FULL=(1<<N)-1
# doubled (8,32)_1：用真 [7,4] Hamming
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C8=[(h<<1)|b for h in H7 for b in (0,1)]
C9=[(c<<1)|b for c in C8 for b in (0,1)]     # 加一位 → (9,64)
def cov_of(C):
    c=0
    for w in C: c|=BM[w]
    return c
def stats(C):
    cm=cov_of(C)
    b=[bin(BM[x]&cm).count('1') for x in range(N)]
    return sum((v-1)*(v-2)//2 for v in b), min(b), max(b), dict(sorted(Counter(b).items()))
print(f"起点 doubled(8,32)×2 → M={len(C9)}，覆盖? {'是 ✓' if cov_of(C9)==FULL else '否 ✗'}")
Q,mb,xb,dist=stats(C9); print(f"   Q={Q} min b={mb} max b={xb} 分布={dist}")
# 删 2 词 + 修复的局部搜索
def cnt_build(C):
    cnt=[0]*N
    for w in C:
        cnt[w]+=1
        for y in NB[w]: cnt[y]+=1
    return cnt
best=None
random.seed(7)
for trial in range(300):
    C=set(C9)
    # 随机删 2
    for _ in range(2):
        C.discard(random.choice(sorted(C)))
    cnt=cnt_build(C)
    for st in range(1200):
        zeros=[z for z in range(N) if cnt[z]==0]
        if not zeros: break
        x=random.choice(zeros); w=random.choice([x]+NB[x])
        if w in C: continue
        cnt[w]+=1
        for y in NB[w]: cnt[y]+=1
        C.add(w)
        rem=[c for c in C if c!=w and cnt[c]>=2 and all(cnt[y]>=2 for y in NB[c])]
        c=random.choice(rem) if rem else random.choice([q for q in C if q!=w])
        cnt[c]-=1
        for y in NB[c]: cnt[y]-=1
        C.discard(c)
    if all(cnt[z]>0 for z in range(N)) and len(C)<=63:
        if best is None or len(C)<len(best): best=set(C)
        print(f"  试 {trial}: M={len(C)} ✓ 覆盖")
        if len(C)<=62: break
if best:
    Q,mb,xb,dist=stats(best)
    print(f"\n最优 M={len(best)}  Q={Q}  min b={mb} max b={xb}")
    print(f"   b 分布={dist}")
    E=len(best)*(n+1)-N
    print(f"   E={E}; C1/parity 预测（n=9 奇）: Q 偶 ⟹ C1 预测 Q≥2 ⟹ {'✓ 一致' if Q>=2 and Q%2==0 else ('⛔ Q=0 ⟹ C1 被反驳 ✓✓' if Q==0 else '?')}")
else:
    print("\n未能在预算内收到 ≤63 ✗")
