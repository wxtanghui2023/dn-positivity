#!/usr/bin/env python3
"""核验壳层容量不等式:
 (a) p(c) <= n - d_C(c) + [d_C=0 且 b(c)=1]      （私有点 ⊆ 自由邻居 + 自身）
 (b) 每方阵给每顶点一个专属壳 ⟹ s_v <= p(v)
 (c) 4*S_q <= N_1  与  4*S_q <= Q2
"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def analyse(n,C,tag):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    dC={c:b[c]-1 for c in C}
    priv={c:[x for x in range(N) if (BM[c]>>x)&1 and b[x]==1] for c in C}
    p={c:len(priv[c]) for c in C}
    N1=sum(1 for x in range(N) if b[x]==1)
    Q2=sum((v-1)*(v-2)//2 for v in b.values())
    # 方阵数 + 每顶点方阵数
    sv=Counter(); sqsets=set()
    for u in C:
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i); c2=u^(1<<j); ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs:
                verts=frozenset([u,a,c2,ac]); sqsets.add(verts)
    tot_sv=0
    for verts in sqsets:
        # 每个顶点在该方阵的数（4 顶点各计 1）
        for v in verts: sv[v]+=1
    tot_sv=sum(sv.values())
    # (a) 检查
    violA=[(c,dC[c],p[c]) for c in C if p[c] > n-dC[c]+(1 if (dC[c]==0 and b[c]==1) else 0)]
    # (b) s_v <= p(v)
    violB=[(v,sv[v],p[v]) for v in C if sv[v]>p[v]]
    Sq=len(sqsets)
    print(f"[{tag}] S_q={Sq} N1={N1} Q2={Q2} | Σs_v={tot_sv} | "
          f"(a)违反={len(violA)} (b)违反={len(violB)} | 4Sq={4*Sq} ≤N1? {4*Sq<=N1} ≤Q2? {4*Sq<=Q2} | Σs_v≤N1? {tot_sv<=N1}")
    if violA[:2]: print(f"    (a) 例: {violA[:2]}")
    if violB[:2]: print(f"    (b) 例: {violB[:2]}")
    return dict(Sq=Sq,N1=N1,Q2=Q2,tot=tot_sv)
def enum_codes(n,M,cap=6):
    N,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
for n,M,t in ((4,4,"(4,4)=K"),(4,5,"(4,5)>K"),(4,6,"(4,6)>K"),(5,7,"(5,7)=K"),(5,8,"(5,8)>K")):
    for C in enum_codes(n,M,cap=4): analyse(n,C,t)
def syn(x):
    a=0
    for i in range(7):
        if (x>>i)&1: a^=(i+1)
    return a
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
analyse(9,C9,"(9,64) 我方")
