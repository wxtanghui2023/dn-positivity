#!/usr/bin/env python3
"""新颖性审计：Ψ₂/Ψ̃₂/Z₂/中点泛函 是否被 code distance distribution 决定？
分组 = (A1..An)；若组内恒定 ⟹ 只是旧数据重编码 ✗"""
import itertools, random
from collections import defaultdict
def setup(n):
    N=1<<n; L1=[[x^(1<<i) for i in range(n)]+[x] for x in range(N)]
    B1=[0]*N
    for x in range(N):
        m=0
        for y in L1[x]: m|=1<<y
        B1[x]=m
    return N,L1,B1,(1<<N)-1
def feats(n,C):
    N,L1,B1,full=setup(n)
    Cs=set(C); cm=0
    for c in C: cm|=1<<c
    b=[bin(B1[x]&cm).count('1') for x in range(N)]
    if any(v==0 for v in b): return None
    Q=sum((v-1)*(v-2)//2 for v in b)
    dist=[0]*(n+1)
    for a,c2 in itertools.combinations(C,2): dist[bin(a^c2).count('1')]+=1
    D={}
    for x in range(N):
        if x in Cs: continue
        d1=sum(1 for c in C if bin(x^c).count('1')==1)
        d2=sum(1 for c in C if bin(x^c).count('1')==2)
        o=sum(b[y]-1 for y in range(N) if bin(x^y).count('1')<=1)
        D[x]=(d1+d2,o)
    Psi=0;Z=0;SM=0;PM=0
    pts=[x for x in range(N) if x not in Cs]
    for x,y in itertools.combinations(pts,2):
        if bin(x^y).count('1')==2:
            Psi+=D[x][1]*D[y][1]
            if D[x][1]==0 and D[y][1]==0: Z+=1
    for a,c2 in itertools.combinations(C,2):
        d=bin(a^c2).count('1')
        if d!=2: continue
        diff=[i for i in range(n) if (a^c2)>>i&1]
        m1=a^(1<<diff[0]); m2=a^(1<<diff[1])
        o1=D.get(m1,(0,0))[1]; o2=D.get(m2,(0,0))[1]
        SM+=o1+o2; PM+=o1*o2
    return dict(Q=Q,dist=tuple(dist[1:]),Psi=Psi,Z=Z,SM=SM,PM=PM,
                PsiT=Psi//4 if n%2 else None, E=len(C)*(n+1)-N)
def enum_codes(n,M):
    N,L1,B1,full=setup(n); out=[]
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=B1[c]
        if cov==full: out.append(list(C))
    return out
def search_codes(n,M,tries=150):
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
random.seed(777)
for n,M,how in ((4,4,"enum"),(4,5,"enum"),(5,7,"enum"),(5,8,"search"),(6,12,"search")):
    cs=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    rows=[r for r in (feats(n,C) for C in cs) if r]
    g=defaultdict(set)
    for r in rows: g[(r['dist'],r['Q'])].add((r['Psi'],r['Z'],r['SM'],r['PM']))
    print(f"[n={n} M={M}] 码 {len(rows)}｜按 (距离分布,Q) 分组数 = {len(g)}")
    for k,v in sorted(g.items())[:4]:
        print(f"   dist={k[0]} Q={k[1]}  ⟹ 组内 (Ψ₂,Z₂,SM,PM) 取值数={len(v)} {'**恒定 ⟹ 被距离分布决定 ✗**' if len(v)==1 else '**组内变化 ⟹ 新信息 ✓✓**'}")
        if len(v)>1: print(f"      {sorted(v)[:3]}")
    # 更严: 固定距离分布(不分 Q) 时 Ψ₂ 是否恒定
    g2=defaultdict(set)
    for r in rows: g2[r['dist']].add((r['Q'],r['Psi'],r['SM'],r['PM']))
    multi=[(k,v) for k,v in g2.items() if len(v)>1]
    print(f"   固定距离分布下(跨 Q)出现多值的分布族: {len(multi)} / {len(g2)}")
    print()
