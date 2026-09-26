#!/usr/bin/env python3
"""在真实 Wille 码（码#2, M=K=62）上跑 shell 审计"""
import itertools
from collections import Counter, defaultdict
def load2(fn):
    codes=[];cur=[]
    for line in open(fn):
        s=line.split()
        if len(s)==9 and all(c in '01' for c in s): cur.append(int("".join(s),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
n=9;N=512
BALL=[0]*N
for x in range(N):
    m=1<<x
    for i in range(n): m|=1<<(x^(1<<i))
    BALL[x]=m
C=load2('K_9_1_classif.txt')[1]   # 码#2 = Wille 型
Cs=set(C)
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
print(f"=== Wille 码 (码#2) shell 审计 ===")
print(f"|C|={len(C)} 方阵={len(sqs)} |V□|={len(V)} I={I} S={S} I_nw={I-len(V)}")
dirs_of=defaultdict(list)
for verts,(u,i,j) in sqs.items():
    for v in verts: dirs_of[v].append({i,j})
states=Counter(); L=0; wit=defaultdict(int)
for v in sorted(dirs_of):
    ds=dirs_of[v]; inter=set.intersection(*ds); union=set().union(*ds)
    dC=b[v]-1
    print(f"  v={format(v,'09b')} 方阵数={len(ds)} |∪|={len(union)} |∩|={len(inter)} |U|={n-len(inter)} d_C={dC}")
    for k in range(n):
        if k in inter: continue
        y=v^(1<<k)
        if y in Cs: states['C']+=1; L+=1; wit[('I',v,y)]+=1
        elif b[y]==1: states['P']+=1
        else:
            states['M']+=1; L+=1
            cov=sorted(c for c in C if (BALL[c]>>y)&1 and c!=v and bin(c^v).count('1')==2)
            wit[('S',y,frozenset([v,cov[0]])) if cov else ('?',v,y)]+=1
print(f"\n三态 = {dict(states)}")
print(f"L□ = {L}")
dup=[(k,c) for k,c in wit.items() if c>1]
print(f"见证重数>1 的个数 = {len(dup)}")
print(f"**L□={L} ≤ S+I_nw={S+I-len(V)} ? {L <= S+I-len(V)}**")
rge3=[v for v in dirs_of if len(set.intersection(*dirs_of[v]))<2]
print(f"\n|∩|<2 (即 r≥3 方向) 的顶点数 = {len(rge3)} / 各 d_C = {[b[v]-1 for v in rge3]}")
print(f"判定: '|∩|<2 ⟹ d_C≥3' 是否成立: {all(b[v]-1>=3 for v in rge3)}")
