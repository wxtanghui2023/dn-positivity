#!/usr/bin/env python3
"""验证 A 定义锁死：2·A_{<=2} = E + Q_2，其中 A_{<=2} = A_1 + A_2（无序码字对）"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def check(n,C):
    N,NB,BM=setup(n); Cs=set(C); CW=0
    for w in C: CW|=1<<w
    b=[bin(BM[x]&CW).count('1') for x in range(N)]
    E=sum(v-1 for v in b); Q2=sum((v-1)*(v-2)//2 for v in b)
    sb2=sum(v*(v-1)//2 for v in b)
    A1=A2=0
    for a,c in itertools.combinations(C,2):
        d=bin(a^c).count('1')
        if d==1: A1+=1
        elif d==2: A2+=1
    return dict(M=len(C),E=E,Q2=Q2,sumC2=sb2,A1=A1,A2=A2,Ale=A1+A2,
        ok1=(sb2==E+Q2), ok2=(2*(A1+A2)==E+Q2), ok3=(sb2==2*(A1+A2)))
def enum_codes(n,M,cap=20):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 锁死验证: 2·A_{<=2} = E + Q_2 ===")
for n,M in ((4,4),(5,7)):
    rs=[check(n,C) for C in enum_codes(n,M)]
    print(f"[n={n} M={M}] 样本{len(rs)}: Σ C(b,2)=E+Q_2 全过={all(r['ok1'] for r in rs)} ✓ | "
          f"2(A₁+A₂)=E+Q_2 全过={all(r['ok2'] for r in rs)} ✓ | ΣC(b,2)=2(A₁+A₂) 全过={all(r['ok3'] for r in rs)} ✓")
    r=rs[0]; print(f"   样本0: E={r['E']} Q_2={r['Q2']} ΣC(b,2)={r['sumC2']} A₁={r['A1']} A₂={r['A2']} A≤2={r['Ale']} ✓")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=check(9,C9)
print(f"[n=9 M=64] E={r['E']} Q_2={r['Q2']} ΣC(b,2)={r['sumC2']} A₁={r['A1']} A₂={r['A2']} A≤2={r['Ale']}")
print(f"   2·A≤2={2*r['Ale']} == E+Q_2={r['E']+r['Q2']} ⟹ {'✓ 锁死成立' if r['ok2'] else '✗'}")
print()
print("=== M=62, n=9 的目标换算 ===")
print(" E=108 ⟹ A≤2 = (108 + Q_2)/2 = 54 + Q_2/2 ✓")
print(" ⟹ 若 Q_2 ≤ 26 则 A≤2 ≤ 67 ✓；若 b∈{1,3} 则 Q_2=N₃=54 ⟹ A≤2 = 81 ✓")
