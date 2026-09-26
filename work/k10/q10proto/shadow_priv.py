#!/usr/bin/env python3
"""private-neighbor shadow 实验：
 q(c)=#{i: b(c+e_i)=1};  Q_priv=Σ_c C(q(c),2);  对照 A2+3A3;  检验 Φ(c)=d2(c)+3d3(c)-C(q(c),2) ≥ 0"""
import itertools, random
from collections import Counter

def setup(n):
    N=1<<n
    L1=[[x^(1<<i) for i in range(n)]+[x] for x in range(N)]
    B1=[0]*N
    for x in range(N):
        m=0
        for y in L1[x]: m|=1<<y
        B1[x]=m
    return N,L1,B1,(1<<N)-1

def stats(n,C,L1,B1,N,full):
    cm=0
    for c in C: cm|=1<<c
    b=[bin(B1[x]&cm).count('1') for x in range(N)]
    if any(v==0 for v in b): return None
    Q=sum((v-1)*(v-2)//2 for v in b)
    A=[0]*(n+1)
    for a,c in itertools.combinations(sorted(C),2):
        A[bin(a^c).count('1')]+=1
    qs=[]; eps=0; phis=[]
    for c in C:
        q=sum(1 for y in L1[c][:-1] if b[y]==1)   # 距离 1 的邻点中 b=1 者
        e=1 if b[c]==1 else 0
        qs.append(q); eps+=e
        # 局部量
        d2=sum(1 for o in C if o!=c and bin(o^c).count('1')==2)
        d3=sum(1 for o in C if bin(o^c).count('1')==3)
        phis.append(d2+3*d3-q*(q-1)//2)
    return dict(Q=Q,A=A,Ale=A[1]+A[2],N1=b.count(1),
                Qpriv=sum(v*(v-1)//2 for v in qs), qsum=sum(qs), qmax=max(qs),
                eps=eps, rsum=sum(v*(v-1)//2 for v in qs),   # = Q_priv by def
                phi_min=min(phis), phi_sum=sum(phis),
                A23=A[2]+3*A[3], qs=tuple(sorted(qs)))

def enum_codes(n,M,maxn=None):
    N,L1,B1,full=setup(n)
    out=[]
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=B1[c]
        if cov==full: out.append(list(C))
        if maxn and len(out)>maxn: break
    return out
def search_codes(n,M,tries=300):
    N,L1,B1,full=setup(n)
    out=set()
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

random.seed(1234)
jobs=[(4,4,"enum"),(4,5,"enum"),(4,6,"enum"),(5,7,"enum"),(5,8,"search"),(6,12,"search")]
res={}
for n,M,how in jobs:
    N,L1,B1,full=setup(n)
    codes = enum_codes(n,M) if how=="enum" else search_codes(n,M)
    S=[stats(n,C,L1,B1,N,full) for C in codes]
    S=[s for s in S if s]
    if not S: print(f"n={n} M={M}: 无"); continue
    tag=f"n={n} M={M}"+(" (=K)" if (n,M) in ((4,4),(5,7),(6,12)) else " (>K)")
    print(f"[{tag}] 收集 {len(S)} 个覆盖码")
    for k in ['Q','Ale','N1','Qpriv','qmax','eps','phi_min','A23']:
        vals=sorted({s[k] for s in S})
        print(f"    {k:8s}: {vals[:6]}{' …' if len(vals)>6 else ''}  ⟹ {'**钉住 ✓**' if len(vals)==1 else '变化 ✗'}")
    xs=[s['Qpriv'] for s in S]; ys=[s['A23'] for s in S]
    if len(set(xs))>1 or len(set(ys))>1:
        import statistics
        mx,my=statistics.mean(xs),statistics.mean(ys)
        num=sum((a-mx)*(c-my) for a,c in zip(xs,ys))
        den=(sum((a-mx)**2 for a in xs)*sum((c-my)**2 for c in ys))**.5
        print(f"    corr(Qpriv, A2+3A3) = {num/den if den else float('nan'):+.4f}")
    # 精确关系检验: Qpriv = A2+3A3 - phi_sum  (按定义 phi_sum = Σ(d2+3d3) - Qpriv)
    ok=all(s['phi_sum']==(sum(1 for _ in []) or (2*s['A'][2]+3*2*s['A'][3]-s['Qpriv'])) for s in S)
    print(f"    恒等核验 Qpriv = Σ(d2+3d3) - ΣΦ : ", all(s['Qpriv']==(2*s['A'][2]+6*s['A'][3]-s['phi_sum']) for s in S))
    print()
