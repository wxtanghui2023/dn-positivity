#!/usr/bin/env python3
"""回测: 按顶点去重口径下, L□ ≤ S+I_nw 是否还失败? (此前 (4,8) 逐(Q,k)口径失败 ✗)"""
import itertools
from collections import Counter, defaultdict
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
def analyse(n,C,tag):
    N,BALL=build(n); Cs=set(C)
    FULL=(1<<N)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return None
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    I=sum((b[c]-1)*(b[c]-2)//2 for c in C)
    sqs={}
    for u in sorted(Cs):
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i);c2=u^(1<<j);ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs: sqs[frozenset([u,a,c2,ac])]=(u,i,j)
    V=set()
    for s in sqs: V|=s
    dirs_of=defaultdict(list)
    for verts,(u,i,j) in sqs.items():
        for v in verts: dirs_of[v].append({i,j})
    # 口径 A: 逐 (Q,k) 计数（旧 ✗）
    LA=0
    for verts,(u,i,j) in sqs.items():
        for v in verts:
            for k in range(n):
                if k in (i,j): continue
                y=v^(1<<k)
                if y in Cs or b[y]>=2: LA+=1
    # 口径 B: 按顶点去重（U(v) 内 distinct 非 private 点）
    LB=0
    for v in V:
        inter=set.intersection(*dirs_of[v])
        seen=set()
        for k in range(n):
            if k in inter: continue
            y=v^(1<<k)
            if y in seen: continue
            seen.add(y)
            if y in Cs or b[y]>=2: LB+=1
    res=dict(tag=tag,S=S,I=I,Inw=I-len(V),LA=LA,LB=LB,rhs=S+I-len(V),Sq=len(sqs),V=len(V))
    print(f"[{tag}] S_q={len(sqs)} |V□|={len(V)} S={S} I_nw={res['Inw']} | 口径A L□={LA} {'✓' if LA<=res['rhs'] else '✗失败'} | 口径B L□={LB} {'✓' if LB<=res['rhs'] else '✗失败'}")
    return res
print("=== 回测 (4,8): 逐(Q,k) vs 按顶点去重 ===")
n=4;N,BALL=build(n);FULL=(1<<N)-1
done=0
for C in itertools.combinations(range(N),8):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL:
        r=analyse(n,list(C),"(4,8)"); done+=1
        if done>=3: break
print()
for n,M in ((4,6),(4,7)):
    N,BALL=build(n);FULL=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BALL[c]
        if cov==FULL: analyse(n,list(C),f"({n},{M})"); break
