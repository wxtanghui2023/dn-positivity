#!/usr/bin/env python3
"""W 超图结构测量：G₂ 图、p(c)-deg 关联、高阶交、候选不等式"""
import itertools
from collections import Counter, defaultdict
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def hyper(n,C):
    N,NB,BM=setup(n); Cs=set(C); idx={c:i for i,c in enumerate(C)}
    W={}
    for x in range(N):
        W[x]=frozenset(c for c in C if (BM[c]>>x)&1)
    assert all(W[x] for x in range(N))
    b={x:len(W[x]) for x in range(N)}
    census=Counter(W.values())          # T -> N_T
    p={c:census.get(frozenset([c]),0) for c in C}
    # G₂: 2-edge 图（T 的大小=2 的边）
    G2=defaultdict(set); E2=0
    for T,cnt in census.items():
        if len(T)==2:
            a,bb=tuple(T); G2[a].add(bb); G2[bb].add(a); E2+=1
    deg={c:len(G2[c]) for c in C}
    iso=[c for c in C if deg[c]==0]
    E=sum(v-1 for v in b.values()); Q=sum(1 for v in b.values() if v>=2)
    Q2=sum((v-1)*(v-2)//2 for v in b.values())
    N1=sum(1 for v in b.values() if v==1); N2=sum(1 for v in b.values() if v==2)
    N3=sum(1 for v in b.values() if v>=3)
    T3=sum(v*(v-1)*(v-2)//6 for v in b.values())
    return dict(M=len(C),E=E,Q=Q,Q2=Q2,N1=N1,N2=N2,N3=N3,T3=T3,
        distinctT=len(census),E2=E2,iso=len(iso),
        pmin=min(p.values()),pmax=max(p.values()),
        degmax=max(deg.values()),degmean=round(sum(deg.values())/len(C),3),
        pdeg=[(p[c],deg[c]) for c in C][:6],
        sum_TA2=sum(cnt for T,cnt in census.items() if len(T)>=2),
        sum_TA3=sum(cnt for T,cnt in census.items() if len(T)>=3))
def enum_codes(n,M,cap=12):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== W 超图结构测量 ===")
for n,M,tag in ((4,4,"=K"),(4,5,">K"),(5,7,"=K"),(5,8,">K")):
    rs=[hyper(n,C) for C in enum_codes(n,M)]
    if not rs: continue
    def rng(k): v=sorted(set(r[k] for r in rs)); return v if len(v)<=4 else f"[{v[0]}..{v[-1]}]({len(v)})"
    print(f"[n={n} M={M} {tag}] 样本{len(rs)}")
    print(f"   E={rng('E')} Q_2={rng('Q2')} N₁={rng('N1')} N₂={rng('N2')} N≥3={rng('N3')} T₃={rng('T3')}")
    print(f"   distinct T={rng('distinctT')} |E(G₂)|={rng('E2')} 孤立点={rng('iso')} p(c)∈{rng('pmin')}-{rng('pmax')} degmax={rng('degmax')}")
    r=rs[0]; print(f"   样本0: (p,deg) 前6={r['pdeg']} ｜ Σ_{'{'}|T|≥2{'}'}N_T={r['sum_TA2']} |T|≥3 点={r['sum_TA3']}")
print()
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=hyper(9,C9)
print(f"[n=9 M=64] E={r['E']} Q_2={r['Q2']} N₁={r['N1']} N₂={r['N2']} N≥3={r['N3']} T₃={r['T3']}")
print(f"   distinct T={r['distinctT']} |E(G₂)|={r['E2']} 孤立点={r['iso']} p(c)∈{r['pmin']}-{r['pmax']} degmax={r['degmax']}")
print(f"   (p,deg) 前6={r['pdeg']} ｜ |T|≥2 点={r['sum_TA2']} |T|≥3 点={r['sum_TA3']}")
print()
print("=== 恒等式 Q_2 ≤ T₃ ≤ ((n+1)/3)Q_2 检验（我方推导）===")
print(" C(k,3)=(k/3)C(k−1,2) ⟹ T₃ ≥ Q_2 ✓（b≥3 时 k/3≥1）且 T₃ ≤ ((n+1)/3)Q_2 ✓")
