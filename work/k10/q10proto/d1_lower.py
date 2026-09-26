#!/usr/bin/env python3
"""新可导出下界: b(c)=1+d1(c) (c∈C) ⟹ Q ≥ Σ_{c∈C} C(d1(c),2)
并核对: Q=0 ⟹ 距离-1 图是匹配 (d1(c)≤1 ∀c) ✓"""
import itertools, random
from collections import Counter
def setup(n):
    N=1<<n; L1=[[x^(1<<i) for i in range(n)]+[x] for x in range(N)]
    B1=[0]*N
    for x in range(N):
        m=0
        for y in L1[x]: m|=1<<y
        B1[x]=m
    return N,L1,B1,(1<<N)-1
def run(n,M,codes,L1,B1,N,full,label):
    stats=[]
    for C in codes:
        cm=0
        for c in C: cm|=1<<c
        b=[bin(B1[x]&cm).count('1') for x in range(N)]
        if any(v==0 for v in b): continue
        Q=sum((v-1)*(v-2)//2 for v in b)
        d1=[sum(1 for o in C if o!=c and bin(o^c).count('1')==1) for c in C]
        lb=sum(v*(v-1)//2 for v in d1)
        # 校验 b(c)=1+d1(c)
        ok=all(b[c]==1+d1[i] for i,c in enumerate(C))
        stats.append((Q,lb,max(d1),sum(d1),ok))
    if not stats: print(f"[{label}] 无"); return
    Qs=sorted({s[0] for s in stats}); lbs=sorted({s[1] for s in stats})
    print(f"[{label}] 码 {len(stats)} 个")
    print(f"   Q 取值 {Qs[:6]} ｜ Σ C(d1,2) 取值 {lbs[:6]}")
    print(f"   恒等式 b(c)=1+d1(c) 全部成立? {'是 ✓✓' if all(s[4] for s in stats) else '否 ✗'}")
    print(f"   不等式 Q ≥ ΣC(d1,2) 全部成立? {'是 ✓✓' if all(s[0]>=s[1] for s in stats) else '否 ✗'}")
    print(f"   max d1(c) 取值 = {sorted({s[2] for s in stats})}  ｜ Σ d1 = 2A1 取值 = {sorted({s[3] for s in stats})}")
    print(f"   Q=0 时 max d1 必须 ≤1: {'✓（数据中 Q=0 的码均满足）' if all(s[2]<=1 for s in stats if s[0]==0) else '✗'}")
    print(f"   紧性 (达到等号的比例) = {sum(1 for s in stats if s[0]==s[1])/len(stats):.1%}")
    print()
def enum_codes(n,M):
    N,L1,B1,full=setup(n); out=[]
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=B1[c]
        if cov==full: out.append(list(C))
    return out
def search_codes(n,M,tries=250):
    N,L1,B1,full=setup(n); out=set()
    for t in range(tries):
        C=set(random.sample(range(N),M)); cnt=[0]*N
        for c in C:
            for y in L1[c]: cnt[y]+=1
        for st in range(2500):
            zeros=[x for x in range(N) if cnt[x]==0]
            if not zeros: break
            x=random.choice(zeros); w=random.choice(L1[x])
            if w in C: continue
            for y in L1[w]: cnt[y]+=1
            C.add(w)
            rem=[c for c in C if c!=w and all(cnt[y]>=2 for y in L1[c])]
            c=random.choice(rem) if rem else random.choice([c for c in C if c!=w])
            for y in L1[c]: cnt[y]-=1
            C.discard(c)
        if all(cnt[x]>0 for x in range(N)): out.add(frozenset(C))
    return [list(s) for s in out]
random.seed(4321)
for n,M,how,K in ((4,4,"enum",True),(4,5,"enum",False),(5,7,"enum",True),(6,12,"search",True)):
    N,L1,B1,full=setup(n)
    cs=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    run(n,M,cs,L1,B1,N,full,f"n={n} M={M}"+(" (=K)" if K else " (>K)"))
