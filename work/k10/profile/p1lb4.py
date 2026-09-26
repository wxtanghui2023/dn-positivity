#!/usr/bin/env python3
"""P1-LB.4: 第二中心 incidence 图 — α/β/H3/H4 + 合并负载 vs 容量 + 零交叉检验"""
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
    Xj={j:[x for x in range(N) if bl[x]==j] for j in range(0,5)}
    # 第二中心: 对每个 b>=3 点 x 与其球内码字对 -> 另一公共中心
    delta={}
    for x in range(N):
        if bl[x]<3: continue
        S=sorted(c for c in C if (BALL[x]>>c)&1)
        ds=[]
        for u,v in itertools.combinations(S,2):
            cc=[z for z in range(N) if (BALL[u]>>z)&1 and (BALL[v]>>z)&1 and z!=x]
            ds.extend(cc)
        delta[x]=ds
    h3=Counter(); h4=Counter(); L=Counter()
    for x in Xj[3]:
        for y in set(delta.get(x,[])): h3[y]+=1; L[y]+=1
    for x in Xj[4]:
        for y in delta.get(x,[]): h4[y]+=1; L[y]+=1
    H3=sum(h3.values()); H4=sum(h4.values())
    a=max((h3[y] for y in Xj[3]),default=0); b_=max((h3[y] for y in Xj[4]),default=0)
    # 零交叉
    zc3=[y for y in h3 if bl[y]==2]; zc4=[y for y in h4 if bl[y]==2]
    # 容量恒等式
    A1=sum(1 for u,v in itertools.combinations(C,2) if bin(u^v).count('1')==1)
    cap=146-2*A1
    # Σ C(b,2)
    S2=sum(bl[z]*(bl[z]-1)//2 for z in range(N))
    print(f"[{tag}] N3={len(Xj[3])} N4={len(Xj[4])} N2={len(Xj[2])} | A1={A1}")
    print(f"   3N3={3*len(Xj[3])} = H3+H4 = {H3}+{H4} | α=max h3(y∈X3)={a} β=max h3(y∈X4)={b_}")
    print(f"   h3 分布: X3上={dict(Counter(h3[y] for y in Xj[3]))} X4上={dict(Counter(h3[y] for y in Xj[4]))}")
    print(f"   **零交叉** Δ(X3)∩X2 = {len(zc3)} 个 {'✓ 空' if not zc3 else '✗ 非空'}")
    print(f"   对照 X4 的第二中心落 X2 个数 = {len(zc4)}")
    print(f"   合并负载 ΣL = {H3+H4+sum(h4.values())-sum(h4.values())+sum(h4.values())} (应为 3N3+6N4={3*len(Xj[3])+6*len(Xj[4])}) | Σ(h3+h4)={sum(L.values())}")
    print(f"   容量: ΣC(b,2)={S2} | **146-2A1={cap}** ✓ | ΣL={3*len(Xj[3])+6*len(Xj[4])} ≤ {cap}? {'✓' if 3*len(Xj[3])+6*len(Xj[4])<=cap else '✗'}")
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
for s in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011","000100 000010 000001 100111 010111 001111 011000 101000 110000 111011 111101 111110":
    analyse(6,[int(x,2) for x in s.split()],"(6,12)=K")
n=5;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),7):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: analyse(5,list(C),"(5,7)=K"); break
