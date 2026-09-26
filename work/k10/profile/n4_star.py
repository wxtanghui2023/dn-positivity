#!/usr/bin/env python3
"""P1 第1-2步: b=4 中心的星结构分类 + 两中心相容性 (d(x,y)) + 型分解预测检验"""
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
    if cov!=FULL: return None
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    Nj=Counter(bl)
    B4=[x for x in range(N) if bl[x]==4]
    B3=[x for x in range(N) if bl[x]==3]
    A=t=sum(1 for x in B4 if x in Cs)   # x∈C 型 (星型 3-face)
    B=len(B4)-A
    t3A=sum(1 for x in B3 if x in Cs); t3B=len(B3)-t3A
    # 型分解预测
    T112_pred=3*A+t3A; T222_pred=A+4*B+t3B
    # 实测型分解
    tt=Counter()
    for u,v,w in itertools.combinations(C,3):
        d=sorted([bin(u^v).count('1'),bin(u^w).count('1'),bin(v^w).count('1')])
        if max(d)<=2: tt[(1,1,2) if d[0]==1 else (2,2,2)]+=1
    # 中心间距离
    dd=Counter(bin(x^y).count('1') for x,y in itertools.combinations(B4,2))
    # 星集交叠
    Sx={x:set(c for c in C if (BALL[x]>>c)&1) for x in B4}
    ov=Counter()
    for x,y in itertools.combinations(B4,2):
        ov[bin(x^y).count('1')]+=0
    ovd=defaultdict(list)
    for x,y in itertools.combinations(B4,2):
        ovd[bin(x^y).count('1')].append(len(Sx[x]&Sx[y]))
    print(f"[{tag}] N4={len(B4)} (A型 x∈C: {A}, B型 x∉C: {B}) | N3={len(B3)} (A: {t3A}, B: {t3B})")
    print(f"   型分解预测: T112={T112_pred} T222={T222_pred} | 实测: {dict(tt)} ⟹ {'✓✓ 预测吻合' if tt.get((1,1,2),0)==T112_pred and tt.get((2,2,2),0)==T222_pred else '✗'}")
    print(f"   b=4 中心间距离分布 = {dict(sorted(dd.items()))}")
    print(f"   各距离下的星集交叠 |Sx∩Sy| = { {k:sorted(set(v)) for k,v in sorted(ovd.items())} }")
    print(f"   Σ|Sx| = 4N4 = {4*len(B4)} ; 被星覆盖的不同码字数 = {len(set().union(*Sx.values()))}")
    # 可用界
    A1=sum(1 for u,v in itertools.combinations(C,2) if bin(u^v).count('1')==1)
    A2=sum(1 for u,v in itertools.combinations(C,2) if bin(u^v).count('1')==2)
    E=sum(v-1 for v in bl); Q2=sum((v-1)*(v-2)//2 for v in bl)
    print(f"   A1={A1} A2={A2} E={E} Q2={Q2} | 界: 3N4≤E⟹N4≤{E//3} ; 6N4≤2A≤2⟹N4≤{2*(A1+A2)//6} ; 3N4A≤A1⟹N4A≤{A1//3}")
    return dict(tag=tag,A=A,B=B,t3A=t3A,t3B=t3B,dd=dict(dd))
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
