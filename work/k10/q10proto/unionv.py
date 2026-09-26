#!/usr/bin/env python3
"""核验 U(v)=∪_{Q∋v}Sh_Q(v): |U(v)| = n − |∩dirs|（交集，非并集 ✗）
 并测 R2 命题: r'=2 且 d_C(v)=2 ⟹ U(v) 中 non-private 点全是 S-见证"""
import itertools
from collections import Counter, defaultdict
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def run(n,C,tag):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    I=sum((b[c]-1)*(b[c]-2)//2 for c in Cs)
    sqs={}
    for u in sorted(Cs):
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i); c2=u^(1<<j); ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs:
                sqs[frozenset([u,a,c2,ac])]=(u,i,j)
    dirs_of=defaultdict(list)
    for verts,(u,i,j) in sqs.items():
        for v in verts: dirs_of[v].append({i,j})
    V=set(dirs_of); Inw=I-len(V)
    okU=0; badU=0; propOK=0; propBad=0; L2=0; Lge3=0
    rows=[]
    for v in sorted(V):
        ds=dirs_of[v]
        inter=set.intersection(*ds) if ds else set()
        union=set().union(*ds)
        U=set(v^(1<<k) for k in range(n) if k not in inter)
        # 同时按并集算（对照）
        Uunion=set(v^(1<<k) for k in range(n) if k not in union)
        if len(U)==n-len(inter): okU+=1
        else: badU+=1
        dC=b[v]-1
        nonpriv=[y for y in U if y not in Cs and b[y]>=2]
        codew=[y for y in U if y in Cs]
        # 命题: inter 大小 2 且 dC=2 ⟹ nonprivate 全给 S 见证
        if len(inter)==2 and dC==2:
            if len(codew)==0: propOK+=1
            else: propBad+=1
        if len(inter)==2: L2+=len(nonpriv)+len(codew)
        else: Lge3+=len(nonpriv)+len(codew)
        rows.append((v,len(ds),len(union),len(inter),n-len(inter),dC,len(nonpriv),len(codew)))
    print(f"[{tag}] |C|={len(C)} 方阵={len(sqs)} |V□|={len(V)} I={I} I_nw={Inw} S={S}")
    print(f"    |U(v)|=n−|∩dirs| 核验: 通过 {okU} / 违反 {badU} ✓")
    print(f"    R2 命题(dC=2, ∩=2 ⟹ 无码字壳点): 通过 {propOK} / 违反 {propBad}")
    print(f"    L2(∩=2 顶点)={L2}  L≥3={Lge3}  合计={L2+Lge3}")
    print(f"    S={S} I_nw={Inw} ⟹ 全式 L≤S+I_nw? {L2+Lge3<=S+Inw}")
    for r in rows[:4]:
        print(f"      v={format(r[0],'0%db'%n)} 方阵数={r[1]} |∪|={r[2]} |∩|={r[3]} |U|={r[4]} d_C={r[5]} nonpriv={r[6]} 码字壳点={r[7]}")
    return L2+Lge3,S,Inw
for n,M,t in ((4,6,"(4,6)"),(4,7,"(4,7)"),(4,8,"(4,8)")):
    N,BM=setup(n); fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            run(n,list(C),t); break
def syn(x):
    a=0
    for i in range(7):
        if (x>>i)&1: a^=(i+1)
    return a
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
run(9,C9,"(9,64)")
