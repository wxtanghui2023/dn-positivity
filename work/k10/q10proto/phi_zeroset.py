#!/usr/bin/env python3
"""Φ( c ) 的零集分析 + 非负原子分解核验
Φ(c)=d2(c)+3d3(c)-C(q,2)
 原子1 (浪费容量) A1 = d2+3d3 - Σ_w κ(w)
 原子2 (覆盖松弛) A2 = Σ_w κ(w) - C(q,2)
 κ(w) = w 覆盖的 shadow 对数 (w 距 c 为 2 或 3)
Φ=0 ⟺ A1=A2=0 ⟺ 每个 d=2/3 码字满容量 且 每个 shadow 恰被覆盖一次且全覆盖"""
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
def analyze(n,C,L1,B1,N,full):
    cm=0
    for c in C: cm|=1<<c
    b=[bin(B1[x]&cm).count('1') for x in range(N)]
    if any(v==0 for v in b): return None
    Cs=set(C); rows=[]
    for c in C:
        S=[i for i in range(n) if b[c^(1<<i)]==1]
        q=len(S); pairs=[frozenset(p) for p in itertools.combinations(S,2)]
        m=len(pairs)
        d2=[w for w in C if w!=c and bin(w^c).count('1')==2]
        d3=[w for w in C if bin(w^c).count('1')==3]
        kap={}
        for w in d2+d3:
            supp=frozenset(i for i in range(n) if (w^c)>>i & 1)
            kap[w]=sum(1 for p in pairs if p<=supp)
        Sk=sum(kap.values())
        A1=len(d2)+3*len(d3)-Sk
        A2=Sk-m
        rows.append((len(d2),len(d3),q,m,A1,A2,A1+A2,kap,d2,d3,pairs))
    return rows
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
random.seed(99)
for n,M,how,K in ((4,4,"enum",True),(4,5,"enum",False),(5,7,"enum",True),(6,12,"search",True)):
    N,L1,B1,full=setup(n)
    codes=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    allphi=[]; alla1=[]; alla2=[]; zero_struct=Counter(); negA=False
    for C in codes:
        rows=analyze(n,C,L1,B1,N,full)
        if not rows: continue
        for (nd2,nd3,q,m,A1,A2,phi,kap,d2,d3,pairs) in rows:
            if A1<0 or A2<0: negA=True
            allphi.append(phi); alla1.append(A1); alla2.append(A2)
            if phi==0: zero_struct[(nd2,nd3,q,m,A1,A2)]+=1
    tag=f"n={n} M={M}"+("  (=K ✓)" if K else "  (>K)")
    print(f"[{tag}] 码 {len(codes)} 个；中心样本 {len(allphi)}")
    print(f"   Φ 取值分布: {dict(sorted(Counter(allphi).items()))}")
    print(f"   A1(浪费容量) 取值: {sorted(set(alla1))[:8]}   ≥0? {'是 ✓（无一为负）' if not negA else '否 ✗'}")
    print(f"   A2(覆盖松弛) 取值: {sorted(set(alla2))[:8]}")
    print(f"   **Φ=0 的中心数 = {sum(1 for x in allphi if x==0)} / {len(allphi)}**  (占比 {sum(1 for x in allphi if x==0)/len(allphi):.1%})")
    print(f"   Φ=0 时的 (d2,d3,q,m) 结构: {list(zero_struct.keys())[:5]}")
    print()
