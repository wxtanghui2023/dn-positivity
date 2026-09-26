#!/usr/bin/env python3
"""方阵 shell 三态分类: private / 码字 / 第二覆盖；逐坐标 i 容量守恒"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def run(n,C,tag):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    N1=sum(1 for x in range(N) if b[x]==1)
    # 收集方阵（规范形：最小顶点 + 两方向）
    sqs={}
    for u in sorted(Cs):
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i); c=u^(1<<j); ac=u^(1<<i)^(1<<j)
            if a in Cs and c in Cs and ac in Cs:
                verts=frozenset([u,a,c,ac]); sqs[verts]=(u,i,j)
    print(f"=== {tag}: |C|={len(C)} 方阵数={len(sqs)} N1={N1} b 分布={dict(sorted(Counter(b.values()).items()))} ===")
    totP=totC=totM=0
    for verts,(u,i,j) in list(sqs.items())[:2]:
        dirs={i,j}
        P=[];CC=[];MM=[]
        percoord={}
        for k in range(n):
            if k in dirs: continue
            shell=[u^(1<<k), u^(1<<i)^(1<<k), u^(1<<j)^(1<<k), u^(1<<i)^(1<<j)^(1<<k)]
            st=[]
            for y in shell:
                if y in Cs: st.append('C'); CC.append(y)
                elif b[y]==1: st.append('P'); P.append(y)
                else: st.append('M'); MM.append(y)
            percoord[k]=st
        totP+=len(P); totC+=len(CC); totM+=len(MM)
        print(f"  方阵@{format(u,'09b')} 方向{{{i},{j}}}: P={len(P)}(private) C={len(CC)}(码字) M={len(MM)}(第二覆盖) 总={len(P)+len(CC)+len(MM)} (应为 4(n−2)={4*(n-2)})")
        # 抽 2 个坐标看逐坐标形态
        ks=sorted(percoord)[:2]
        for k in ks: print(f"     坐标 k={k}: {percoord[k]}")
    print(f"  前 2 方阵合计: P={totP} C={totC} M={totM} ⟹ L□(第二覆盖+码字)={totC+totM}")
    return dict(Sq=len(sqs),N1=N1)
def enum_codes(n,M,cap=3):
    N,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
for n,M,t in ((4,6,"(4,6)>K"),(5,8,"(5,8)>K")):
    for C in enum_codes(n,M,cap=2): run(n,C,t)
def syn(x):
    a=0
    for i in range(7):
        if (x>>i)&1: a^=(i+1)
    return a
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
run(9,C9,"(9,64) 我方")
