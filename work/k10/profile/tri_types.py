#!/usr/bin/env python3
"""三角形按边型分类 + 共同中心类型 (x∈C?) + 与 N3/N4 的关系"""
import itertools
from collections import Counter
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
    if cov!=FULL: return None
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    Nj=Counter(bl)
    T3=sum(v*(v-1)*(v-2)//6 for v in bl)
    tup=Counter(); ctr=Counter()
    for u,v,w in itertools.combinations(C,3):
        d=sorted([bin(u^v).count('1'),bin(u^w).count('1'),bin(v^w).count('1')])
        if max(d)<=2:
            tup[tuple(d)]+=1
            m=BALL[u]&BALL[v]&BALL[w]
            x=m.bit_length()-1
            ctr['x∈C' if x in Cs else 'x∉C']+=1
    print(f"[{tag:20}] T3={T3:3} #tri={sum(tup.values()):3} | 型分布={dict(tup)} | 中心={dict(ctr)}")
    print(f"      剖面 N3={Nj.get(3,0)} N4={Nj.get(4,0)} | 3阶恒等 T3=N3+4N4={Nj.get(3,0)+4*Nj.get(4,0)} {'✓' if T3==Nj.get(3,0)+4*Nj.get(4,0) else '✗'} | 格计数 Σ_x C(b,3) 分解:")
    # 每个 b=3 点贡献 1, b=4 点贡献 4
    print(f"        b=3 点贡献 {Nj.get(3,0)}×1={Nj.get(3,0)} ; b=4 点贡献 {Nj.get(4,0)}×4={4*Nj.get(4,0)} ; 合计 {Nj.get(3,0)+4*Nj.get(4,0)}")
n=4;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),4):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: analyse(4,list(C),"(4,4)=K"); break
n=5;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),7):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: analyse(5,list(C),"(5,7)=K"); break
for s in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011","000100 000010 000001 100111 010111 001111 011000 101000 110000 111011 111101 111110":
    analyse(6,[int(x,2) for x in s.split()],"(6,12)=K")
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
