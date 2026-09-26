#!/usr/bin/env python3
"""核验: Struik/van Wee 局部不等式 OC(B1(x)) ≥ (R+1)(⌈(n+1)/(R+1)⌉−(n+1)/(R+1))
 R=1: 偶 n ⟹ 下界 1 ✓; 奇 n ⟹ 下界 0 ⟹ 空不等式 ✗
检查实测 OC(B1(x)) 分布，看奇 n 是否出现 0"""
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
def enum_codes(n,M):
    N,L1,B1,full=setup(n); out=[]
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=B1[c]
        if cov==full: out.append(list(C))
    return out
def search_codes(n,M,tries=200):
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
random.seed(8888)
for n,M,how,K in ((4,4,"enum",True),(5,7,"enum",True),(6,12,"search",True)):
    N,L1,B1,full=setup(n)
    cs=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    dist=Counter(); minv=999; zero=0; tot=0
    for C in cs:
        Cs=set(C); cm=0
        for c in C: cm|=1<<c
        b=[bin(B1[x]&cm).count('1') for x in range(N)]
        if any(v==0 for v in b): continue
        tot+=1
        for x in range(N):
            if x in Cs: continue
            oc=sum(b[y]-1 for y in range(N) if bin(x^y).count('1')<=1)   # OC(B1(x))
            dist[oc]+=1; minv=min(minv,oc)
            if oc==0: zero+=1
    lb = 2*( (n+2)//2 - (n+1)/2 )   # R=1: (R+1)(⌈(n+1)/(R+1)⌉-(n+1)/(R+1))
    print(f"=== n={n} M={M}(=K) 码 {tot} 个｜Struik 下界(R=1) = {lb} ===")
    print(f"   OC(B1(x)) 分布: {dict(sorted(dist.items())[:6])}")
    print(f"   最小值 = {minv}（{'=0 ⟹ 不等式空 ✗' if minv==0 else '≥1 ✓'}）；出现 0 的次数 = {zero}/{sum(dist.values())}")
    print()
