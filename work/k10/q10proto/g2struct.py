#!/usr/bin/env python3
"""Q=0 时 G2 的全局结构：是否 matching / 每边两点中点 / 固定 c 的距离-2 邻域兼容模式"""
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
def g2prof(n,C):
    deg=Counter(); edges=0
    for a,b in itertools.combinations(sorted(C),2):
        d=bin(a^b).count('1')
        if d<=2:
            edges+=1
    for c in C:
        deg[sum(1 for o in C if o!=c and bin(o^c).count('1')<=2)]+=1
    return edges, dict(sorted(deg.items()))
random.seed(31337)
for n,M,how in ((4,4,"enum"),(5,8,"search")):
    N,L1,B1,full=setup(n)
    cs=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    zero=[]
    for C in cs:
        cm=0
        for c in C: cm|=1<<c
        b=[bin(B1[x]&cm).count('1') for x in range(N)]
        if any(v==0 for v in b): continue
        if sum((v-1)*(v-2)//2 for v in b)==0: zero.append((C,b))
    print(f"=== n={n} M={M}: Q=0 的码 {len(zero)} 个 ===")
    edges=Counter(); degs=Counter()
    for C,b in zero:
        e,dg=g2prof(n,C); edges[e]+=1; degs[tuple(sorted(dg.items()))]+=1
    print(f"   G2 边数分布: {dict(edges)}")
    print(f"   G2 度数谱分布(前4): {dict(list(degs.items())[:4])}")
    # 每边中点是否恰 2 个且非码字 (前面已验证 ✓)，此处查 G2 是否 matching
    mm=all(max(dg.keys())<=1 for _,dg in [(None,g2prof(n,C)[1]) for C,b in zero[:20]])
    print(f"   G2 最大度 ≤1 (matching)? {mm}")
    # 距离-2 邻域兼容: 固定 c，其距离-2 邻域内的点对的坐标交叉模式
    pat=Counter()
    for C,b in zero[:20]:
        for c in C:
            n2=[o for o in C if bin(o^c).count('1')==2]
            for a,bb in itertools.combinations(n2,2):
                sa=frozenset(i for i in range(n) if (a^c)>>i&1); sb=frozenset(i for i in range(n) if (bb^c)>>i&1)
                pat[len(sa&sb)]+=1
    print(f"   距离-2 邻域内 pair 的 |supp∩supp'| 分布: {dict(sorted(pat.items()))}")
    print()
