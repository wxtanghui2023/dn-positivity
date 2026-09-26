#!/usr/bin/env python3
"""重复见证检验: 找"顶点落在 >=2 方阵"的码, 测重数与 L□ <= S + I_nw"""
import itertools, random
from collections import Counter, defaultdict
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def analyse(n,C,tag):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    N1=sum(1 for x in range(N) if b[x]==1)
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in Cs)
    I=sum((b[c]-1)*(b[c]-2)//2 for c in Cs)
    sqs={}
    for u in sorted(Cs):
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i); c2=u^(1<<j); ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs:
                sqs[frozenset([u,a,c2,ac])]=(u,i,j)
    V=set()
    for verts in sqs: V|=verts
    Inw=I-len(V)
    vsq=Counter()
    for verts in sqs:
        for v in verts: vsq[v]+=1
    multi=[v for v in vsq if vsq[v]>=2]
    # shell 三态 + 见证
    states=Counter(); wit=defaultdict(int); Lsq=0
    for verts,(u,i,j) in sqs.items():
        dirs={i,j}
        for v in verts:
            for k in range(n):
                if k in dirs: continue
                y=v^(1<<k)
                if y in Cs:
                    states['C']+=1; Lsq+=1; wit[('I',v,y)]+=1
                elif b[y]==1: states['P']+=1
                else:
                    states['M']+=1; Lsq+=1
                    cov=sorted(c for c in C if (BM[c]>>y)&1 and c!=v and bin(c^v).count('1')==2)
                    if cov: wit[('S',y,frozenset([v,cov[0]]))]+=1
                    else: wit[('?',v,y)]+=1
    mdup=[(k,c) for k,c in wit.items() if c>1]
    print(f"[{tag}] |C|={len(C)} 方阵={len(sqs)} |V□|={len(V)} I={I} I_nw={Inw} S={S} N1={N1}")
    print(f"    三态={dict(states)} L□={Lsq} | 顶点多重数>=2 的个数={len(multi)} | 见证重数>1 的个数={len(mdup)}")
    if multi[:2]:
        for v in multi[:2]: print(f"      v={format(v,'0%db'%n)} 方阵数={vsq[v]} d_C(v)={b[v]-1} 该点 I 贡献={((b[v]-1)*(b[v]-2))//2}")
    print(f"    **L□={Lsq} <= S+I_nw={S+Inw} ? {Lsq<=S+Inw}**")
    return dict(L=Lsq,S=S,Inw=Inw)
def enum_codes(n,M,cap=400):
    N,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 找『顶点在 >=2 方阵』的实例 ===")
found=0
for n in (4,5):
    for M in range(4, 12):
        cs=enum_codes(n,M,cap=200)
        for C in cs:
            N,BM=setup(n); Cs=set(C)
            sqs=0; vsq=Counter()
            for u in sorted(Cs):
                for i,j in itertools.combinations(range(n),2):
                    a=u^(1<<i); c2=u^(1<<j); ac=u^(1<<i)^(1<<j)
                    if a in Cs and c2 in Cs and ac in Cs:
                        for v in (u,a,c2,ac): vsq[v]+=1
            if any(c>=2 for c in vsq.values()):
                analyse(n,C,f"n={n} M={M} 共享顶点 ★")
                found+=1
                break
        if found>=3: break
    if found>=3: break
if found==0: print(" ✗ 未找到共享顶点的实例（小 n 全枚举范围）")
