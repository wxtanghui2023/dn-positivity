#!/usr/bin/env python3
"""核验: 方阵数 s 与 I 的关系"""
import itertools
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def nsq(n,C):
    Cs=set(C); cnt=0
    for u in C:
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i); b=u^(1<<j); ab=u^(1<<i)^(1<<j)
            if a in Cs and b in Cs and ab in Cs: cnt+=1
    return cnt//4
def analyse(n,C,tag):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    I=sum((b[x]-1)*(b[x]-2)//2 for x in Cs)
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    Q2=sum((v-1)*(v-2)//2 for v in b.values())
    s=nsq(n,C)
    print(f"[{tag}] I={I} S={S} Q2={Q2} | 方阵数 s={s} | 4s={4*s} | I-4s={I-4*s}")
def syn(x):
    a=0
    for i in range(7):
        if (x>>i)&1: a^=(i+1)
    return a
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
analyse(9,C9,"n=9 我方 (9,64)")
def enum_codes(n,M,cap=3):
    N,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
for n,M,tag in ((4,4,"(4,4)=K"),(5,7,"(5,7)=K"),(4,6,"(4,6)>K")):
    for C in enum_codes(n,M,cap=2): analyse(n,C,tag)
