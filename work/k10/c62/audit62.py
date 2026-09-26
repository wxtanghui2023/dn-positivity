#!/usr/bin/env python3
"""C₆₂ 审计协议: 验证 + 十项不变量"""
import itertools
from collections import Counter
def load(fn):
    C=[]
    for line in open(fn):
        s=line.split()
        if len(s)==9 and all(c in '01' for c in s):
            C.append(int("".join(s),2))
    return C
C=load('K_9_1.txt')
print(f"=== K_9_1.txt ===")
print(f"|C| = {len(C)}  去重后 = {len(set(C))}")
n=9; N=512
BALL=[0]*N
for x in range(N):
    m=1<<x
    for i in range(n): m|=1<<(x^(1<<i))
    BALL[x]=m
cov=0
for w in C: cov|=BALL[w]
FULL=(1<<N)-1
print(f"覆盖 F_2^9: {cov==FULL} ✓  未覆盖数={512-bin(cov).count('1')}")
if cov!=FULL:
    miss=[x for x in range(N) if not (cov>>x)&1]; print(" 未覆盖:", miss[:20]); raise SystemExit
b={x:sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)}
E=sum(v-1 for v in b.values()); Q=sum(1 for v in b.values() if v>=2)
Q2=sum((v-1)*(v-2)//2 for v in b.values())
I=sum((b[c]-1)*(b[c]-2)//2 for c in C)
S=sum(b[x]*(b[x]-1)//2 for x in range(N) if x not in set(C))
N1=sum(1 for v in b.values() if v==1)
dmax=max(b[c]-1 for c in C)
dC=Counter(b[c]-1 for c in C)
A1=A2=0
for u,v in itertools.combinations(C,2):
    d=bin(u^v).count('1')
    if d==1: A1+=1
    elif d==2: A2+=1
# 方阵
Cs=set(C); sqs=set()
for u in C:
    for i,j in itertools.combinations(range(n),2):
        a=u^(1<<i); c2=u^(1<<j); ac=u^(1<<i)^(1<<j)
        if a in Cs and c2 in Cs and ac in Cs: sqs.add(frozenset([u,a,c2,ac]))
V=set()
for s in sqs: V|=s
print(f"\n=== 十项不变量 ===")
print(f" E={E}  Q={Q}  Q2={Q2}  I={I}  S={S}  N1={N1}")
print(f" A1={A1}  A2={A2}  A≤2={A1+A2}  (2A≤2 = {2*(A1+A2)} vs E+Q2 = {E+Q2})")
print(f" S_q={len(sqs)}  |V□|={len(V)}  **I_nw = I-|V□| = {I-len(V)}**")
print(f" **d_max = {dmax}**   d_C 分布 = {dict(sorted(dC.items()))}")
print(f" b 分布 = {dict(sorted(Counter(b.values()).items()))}")
print(f"\n=== 判据 ===")
print(f" (i)  d_max ≤ 2 ?  {'是 ✓✓' if dmax<=2 else '否 ✗ — 存在 d_C≥3 的码字 '+str(dmax)}")
print(f" (ii) I_nw = 0 ?   {'是 ✓✓' if I-len(V)==0 else '否 ✗ = '+str(I-len(V))}")
print(f" (iii) S_q > 0 ?   {'是 ✓' if len(sqs)>0 else '否'}")
print(f" (iv) 恒等式 2A≤2=E+Q2 ? {'✓' if 2*(A1+A2)==E+Q2 else '✗'}")
print(f" (v) 恒等式 2A2=I+S ?   {'✓' if 2*A2==I+S else '✗'}")
print(f"\n=== Kéri 锚点核对 (c2,c7,c9,c13) ===")
anch=["000001010","000101010","001001010","001101010"]
for a in anch:
    w=int(a,2); print(f"  {a} ∈ C ? {w in Cs}")
