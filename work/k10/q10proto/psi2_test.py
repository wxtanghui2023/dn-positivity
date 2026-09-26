#!/usr/bin/env python3
"""① Ψ₂/Z₂（距离-2 非码字对的 o(x)o(y) 相关）在 Q=0 vs Q>0 上是否稳定区分
 ② 可拼接性: doubling / product 是否保 Q=0  ③ 对照组: perfect(7,16), product 码"""
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
def metrics(n,C):
    N,L1,B1,full=setup(n)
    Cs=set(C); cm=0
    for c in C: cm|=1<<c
    b=[bin(B1[x]&cm).count('1') for x in range(N)]
    if any(v==0 for v in b): return None
    Q=sum((v-1)*(v-2)//2 for v in b)
    o={x:sum(b[y]-1 for y in range(N) if bin(x^y).count('1')<=1) for x in range(N) if x not in Cs}
    Psi=0; Z=0; cnt=0
    for x,y in itertools.combinations([z for z in range(N) if z not in Cs],2):
        if bin(x^y).count('1')==2:
            cnt+=1
            Psi+=o[x]*o[y]
            if o[x]==0 and o[y]==0: Z+=1
    return dict(Q=Q,Psi=Psi,Z=Z,pairs=cnt,E=len(C)*(n+1)-N,o=Counter(o.values()))
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
random.seed(4242)
print("=== A. Ψ₂/Z₂ 在 Q=0 vs Q>0 上的分布 ===")
for n,M,how,lab in ((4,4,"enum","Q=0"),(5,7,"enum","Q>0"),(6,12,"search","Q>0"),(5,8,"search","Q=0"),(4,5,"enum","Q>0")):
    cs=enum_codes(n,M) if how=="enum" else search_codes(n,M)
    rs=[r for r in (metrics(n,C) for C in cs) if r]
    if not rs: continue
    zs=[r for r in rs if r['Q']==0]; nz=[r for r in rs if r['Q']>0]
    def rng(v,k): return (min(x[k] for x in v), max(x[k] for x in v)) if v else None
    print(f"[n={n} M={M} {lab}] 码 {len(rs)}（Q=0 的 {len(zs)} 个）")
    print(f"    Q=0 组:  Ψ₂∈{rng(zs,'Psi')}  Z₂∈{rng(zs,'Z')}")
    print(f"    Q>0 组:  Ψ₂∈{rng(nz,'Psi')}  Z₂∈{rng(nz,'Z')}")
    print(f"    (M=K? {'是' if (n,M) in ((4,4),(5,7),(6,12)) else '否'})  E={rs[0]['E']}")
print()
print("=== B. 可拼接性测试 ===")
# doubling: C -> {(c,0),(c,1)}
def double(C,n):
    return [c<<1 for c in C]+[(c<<1)|1 for c in C]
C4=enum_codes(4,4)[0]
r=metrics(4,C4); print(f"  基码 n=4 M=4: Q={r['Q']} ✓")
C5=double(C4,4); r5=metrics(5,C5)
print(f"  doubling → n=5 M={len(C5)}: Q={r5['Q'] if r5 else '未覆盖 ✗'}  ⟹ {'保 Q=0 ✗' if r5 and r5['Q']>0 else '保 Q=0 ✓'}")
# product of perfect codes
def product(A,na,B,nb):
    return [ (a<<nb)|b for a in A for b in B ]
P2=[0b00,0b11]; P3=[0b000,0b111]
C4p=product(P2,2,P2,2); rp=metrics(4,C4p)
print(f"  perfect(2,2)×perfect(2,2) → n=4 M={len(C4p)}: Q={rp['Q'] if rp else '未覆盖'}  E={rp['E'] if rp else '-'}")
C6p=product(P3,3,P3,3); rp6=metrics(6,C6p)
print(f"  perfect(3,2)×perfect(3,2) → n=6 M={len(C6p)}: Q={rp6['Q'] if rp6 else '未覆盖'}  E={rp6['E'] if rp6 else '-'}")
# perfect Hamming (7,16)
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
r7=metrics(7,H7); print(f"  Hamming(7,16) perfect → Q={r7['Q']}  E={r7['E']}  o分布={dict(list(r7['o'].items())[:4])}")
