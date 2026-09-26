#!/usr/bin/env python3
"""B(2): 定 M=62 局部搜索 (9,62)_1 覆盖码；找到即算 Q（C1 判决 ✓）"""
import random
from collections import Counter
n=9; N=1<<n; M=62
BM=[0]*N
for x in range(N):
    m=1<<x
    for i in range(n): m|=1<<(x^(1<<i))
    BM[x]=m
FULL=(1<<N)-1
def localsearch(tries, maxsteps):
    found=[]
    for t in range(tries):
        C=set(random.sample(range(N),M)); cnt=[0]*N
        for c in C:
            for y in range(N):
                if (BM[c]>>y)&1: cnt[y]+=1
        for st in range(maxsteps):
            zeros=[x for x in range(N) if cnt[x]==0]
            if not zeros: break
            x=random.choice(zeros)
            cands=[x]+[x^(1<<i) for i in range(n)]
            w=random.choice(cands)
            if w in C: continue
            for y in range(N):
                if (BM[w]>>y)&1: cnt[y]+=1
            C.add(w)
            rem=[c for c in C if c!=w and all(cnt[y]>=2 for y in range(N) if (BM[c]>>y)&1)]
            c=random.choice(rem) if rem else random.choice([c for c in C if c!=w])
            for y in range(N):
                if (BM[c]>>y)&1: cnt[y]-=1
            C.discard(c)
        if all(cnt[x]>0 for x in range(N)):
            found.append(frozenset(C))
            if len(found)>=3: break
    return found
random.seed(20260926)
res=localsearch(400, 4000)
print(f"找到覆盖码数 = {len(res)}（M=62）")
for C in res:
    cm=0
    for c in C: cm|=1<<c
    b=[bin(BM[x]&cm).count('1') for x in range(N)]
    Q=sum((v-1)*(v-2)//2 for v in b)
    E=M*(n+1)-N
    print(f"  M={len(C)} Q={Q} E={E} Q-E偶性: Q≡{Q%2}, E≡{E%2} {'一致 ✓' if Q%2==E%2 else '✗'}  min b={min(b)} max b={max(b)}")
    print(f"    b 分布: {dict(sorted(Counter(b).items()))}")
    if Q==0: print("    ⟹ ⛔ **Q=0 ⟹ C1 被反驳** ✓✓")
    else: print(f"    ⟹ ✓ Q={Q}>0 ⟹ 与 C1 预测(Q≥2)一致 ✓")
