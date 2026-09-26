#!/usr/bin/env python3
"""P1-LB.4 终刀: Δ(x) 三点内部几何分类 + 是否强制的 X3↔X4 构型"""
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
    N,BALL=build(n); Cs=set(C); FULL=(1<<N)-1
    cov=0
    for c in C: cov|=BALL[c]
    if cov!=FULL: return
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    X3=[x for x in range(N) if bl[x]==3]
    pat=Counter(); dist=Counter(); dx3=Counter(); pair_b=Counter()
    x4recv=Counter()
    for x in X3:
        S=sorted(c for c in C if (BALL[x]>>c)&1)
        ds=[]
        for u,v in itertools.combinations(S,2):
            cc=[z for z in range(N) if (BALL[u]>>z)&1 and (BALL[v]>>z)&1 and z!=x]
            ds.extend(cc)
        dd=sorted(set(ds))
        bpat=tuple(sorted(bl[y] for y in dd))
        pat[bpat]+=1
        # 与 x 的距离
        dist[tuple(sorted(bin(y^x).count('1') for y in dd))]+=1
        dx3[len([y for y in dd if bl[y]==3])]+=1
        for y in dd:
            if bl[y]==4: x4recv[y]+=1
        # 三点两两距离
        if len(dd)==3:
            pd=tuple(sorted(bin(a^b).count('1') for a,b in itertools.combinations(dd,2)))
            pair_b[pd]+=1
    print(f"[{tag}] N3={len(X3)}")
    print(f"   Δ(x) 的 b 值模式分布 = {dict(pat)}")
    print(f"   Δ(x) 到 x 的距离向量分布 = {dict(dist)}")
    print(f"   |Δ(x)∩X3| 分布 = {dict(dx3)}")
    print(f"   Δ(x) 三点两两距离分布 = {dict(pair_b)}")
    print(f"   X4 接收者 = {len(x4recv)} 个，各自收到 {dict(Counter(x4recv.values()))}")
    if x4recv:
        ys=sorted(x4recv)
        print(f"   这些 X4 点间的距离 = {dict(Counter(bin(a^b).count('1') for a,b in itertools.combinations(ys,2)))}")
    return dict(pat=dict(pat),dx3=dict(dx3),nrecv=len(x4recv))
def load62():
    codes=[];cur=[]
    for line in open('../c62/K_9_1_classif.txt'):
        a=line.split()
        if len(a)==9 and all(c in '01' for c in a): cur.append(int("".join(a),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
r=[]
for i,c in enumerate(load62(),1): r.append(analyse(9,c,f"(9,62)=K 码#{i}"))
print("\n=== 两码是否同型？ ===")
if len(r)==2:
    for k in ('pat','dx3','nrecv'):
        print(f"  {k}: {r[0][k]} vs {r[1][k]} {'✓一致' if r[0][k]==r[1][k] else '✗不同'}")
