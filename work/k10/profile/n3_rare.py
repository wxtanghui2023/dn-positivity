#!/usr/bin/env python3
"""N4≥10 ⟺ N3≤8: 为何三重覆盖点"稀少"? 研究 b=3 点的局部结构与第二中心"""
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
    Nj=Counter(bl)
    X3=[x for x in range(N) if bl[x]==3]; X4=[x for x in range(N) if bl[x]==4]
    print(f"[{tag}] N3={len(X3)} N4={len(X4)} | N3≤8? {'✓' if len(X3)<=8 else '✗'}")
    print(f"   b=3 点: x∈C 的个数={sum(1 for x in X3 if x in Cs)} / x∉C={sum(1 for x in X3 if x not in Cs)}")
    # b=3 点之间的距离分布
    dd=Counter(bin(x^y).count('1') for x,y in itertools.combinations(X3,2))
    print(f"   b=3 点间距离分布={dict(sorted(dd.items()))}")
    # 每个 b=3 点的三个码字 + 三对的"第二中心"及其 b 值
    types=Counter(); second=Counter(); coincide=Counter()
    for x in X3:
        S=sorted(c for c in C if (BALL[x]>>c)&1)
        scs=[]
        for u,v in itertools.combinations(S,2):
            cc=[z for z in range(N) if (BALL[u]>>z)&1 and (BALL[v]>>z)&1 and z!=x]
            if len(cc)==1:
                z=cc[0]; scs.append(z); second[bl[z]]+=1
            else:
                scs.append(None); second[('multi',len(cc))]+=1
        uniq=set(s for s in scs if s is not None)
        coincide[f"{len(uniq)}/{len(scs)}"]+=1
        types['A型(x∈C)' if x in Cs else 'B型(x∉C)']+=1
    print(f"   b=3 点的第二中心 b 值分布={dict(second)}")
    print(f"   每 b=3 点的(不同第二中心数/3)={dict(coincide)}")
    # b=4 点同样结构（对照）
    second4=Counter()
    for x in X4:
        S=sorted(c for c in C if (BALL[x]>>c)&1)
        for u,v in itertools.combinations(S,2):
            cc=[z for z in range(N) if (BALL[u]>>z)&1 and (BALL[v]>>z)&1 and z!=x]
            for z in cc: second4[bl[z]]+=1
    print(f"   [对照] b=4 点的第二中心 b 值分布={dict(second4)}")
    print(f"   类型分布: {dict(types)} | 总量 Σb at b≥3 点 = {3*len(X3)+4*len(X4)}")
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
for i,c in enumerate(load62(),1): analyse(9,c,f"(9,62)=K 码#{i}")
c1=[int(x,2) for x in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011".split()]
analyse(6,c1,"(6,12)=K 类#1")
n=4;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),4):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: analyse(4,list(C),"(4,4)=K"); break
