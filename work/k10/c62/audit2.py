#!/usr/bin/env python3
"""审计两个已知 (9,62) 码: 不变量是否一致?"""
import itertools
from collections import Counter
def load2(fn):
    codes=[]; cur=[]
    for line in open(fn):
        s=line.split()
        if len(s)==9 and all(c in '01' for c in s): cur.append(int("".join(s),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
def audit(C,tag):
    n=9; N=512
    BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    cov=0
    for w in C: cov|=BALL[w]
    FULL=(1<<N)-1; ok=(cov==FULL)
    b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
    E=sum(v-1 for v in b.values()); Q=sum(1 for v in b.values() if v>=2)
    Q2=sum((v-1)*(v-2)//2 for v in b.values())
    I=sum((b[c]-1)*(b[c]-2)//2 for c in C)
    S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in set(C))
    N1=sum(1 for v in b.values() if v==1)
    dmax=max(b[c]-1 for c in C)
    A1=A2=0
    for u,v in itertools.combinations(C,2):
        d=bin(u^v).count('1')
        if d==1: A1+=1
        elif d==2: A2+=1
    Cs=set(C); sqs=set()
    for u in C:
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i); c2=u^(1<<j); ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs: sqs.add(frozenset([u,a,c2,ac]))
    V=set()
    for s in sqs: V|=s
    prof=dict(sorted(Counter(b.values()).items()))
    print(f"[{tag}] |C|={len(C)} 覆盖={ok} | E={E} Q={Q} Q2={Q2} I={I} S={S} N1={N1}")
    print(f"      A1={A1} A2={A2} 2A≤2={2*(A1+A2)} vs E+Q2={E+Q2} {'✓' if 2*(A1+A2)==E+Q2 else '✗'} | 2A2={2*A2} vs I+S={I+S} {'✓' if 2*A2==I+S else '✗'}")
    print(f"      S_q={len(sqs)} |V□|={len(V)} **I_nw={I-len(V)}** **d_max={dmax}** 剖面={prof}")
    return dict(E=E,Q2=Q2,I=I,S=S,A1=A1,A2=A2,Sq=len(sqs),V=len(V),Inw=I-len(V),dmax=dmax,prof=prof)
cs=load2('K_9_1_classif.txt')
print(f"classif 文件含 {len(cs)} 个码\n")
rs=[audit(c,f"已知码 #{i+1}") for i,c in enumerate(cs)]
if len(rs)==2:
    a,b=rs
    print()
    print("=== 两码是否共享不变量? ===")
    for k in ['E','Q2','I','S','A1','A2','Sq','V','Inw','dmax']:
        same = a[k]==b[k] if k!='prof' else a[k]==b[k]
        print(f"  {k:5}: {a[k]} vs {b[k]}  {'一致 ✓' if same else '**不同 ✗**'}")
