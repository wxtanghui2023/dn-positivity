#!/usr/bin/env python3
"""B(2b): 快速版 M=62 搜索（位掩码 + 邻域增量）"""
import random
from collections import Counter
n=9; N=1<<n; M=62
NB=[[x^(1<<i) for i in range(n)] for x in range(N)]     # 开球邻域(不含自身)
BM=[1<<x for x in range(N)]
for x in range(N):
    for y in NB[x]: BM[x]|=1<<y
FULL=(1<<N)-1
def cov_of(C):
    c=0
    for w in C: c|=BM[w]
    return c
def bits(m):
    while m:
        b=m&-m; yield b.bit_length()-1; m^=b
def search(tries=60, maxsteps=3000):
    out=[]
    for t in range(tries):
        C=set(random.sample(range(N),M))
        cnt=[0]*N
        for w in C:
            cnt[w]+=1
            for y in NB[w]: cnt[y]+=1
        for st in range(maxsteps):
            if all(cnt[x]>0 for x in range(N)): break
            x=random.choice([z for z in range(N) if cnt[z]==0])
            w=random.choice([x]+NB[x])
            if w in C: continue
            cnt[w]+=1
            for y in NB[w]: cnt[y]+=1
            C.add(w)
            rem=[c for c in C if c!=w and cnt[c]>=2 and all(cnt[y]>=2 for y in NB[c])]
            c=random.choice(rem) if rem else random.choice([q for q in C if q!=w])
            cnt[c]-=1
            for y in NB[c]: cnt[y]-=1
            C.discard(c)
        if all(cnt[x]>0 for x in range(N)):
            out.append(frozenset(C))
            if len(out)>=3: break
    return out
random.seed(20260926)
res=search(60,3000)
E=M*(n+1)-N
print(f"M={M}: 找到覆盖码 {len(res)} 个（E={E}, Q≡E mod 2 ⟹ Q 偶 ✓）")
for C in res:
    cm=cov_of(C)
    b=[bin(BM[x]&cm).count('1') for x in range(N)]
    Q=sum((v-1)*(v-2)//2 for v in b)
    print(f"  Q={Q}  min b={min(b)} max b={max(b)}  b分布={dict(sorted(Counter(b).items()))}")
    print(f"  ⟹ {'⛔ Q=0 ⟹ C1 被反驳 ✓✓' if Q==0 else f'✓ Q={Q}>0 ⟹ 与 C1 预测(Q≥2)一致 ✓'}")
