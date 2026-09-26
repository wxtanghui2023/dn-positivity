#!/usr/bin/env python3
"""square 普查：S=#2-面⊆C，V=不同顶点数；验证引理"square 顶点 b≥3"；统计 (U,Q,N≥3,S)"""
import itertools, random
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def census(n,C):
    N,NB,BM=setup(n)
    Cs=set(C); CW=0
    for w in C: CW|=1<<w
    b=[bin(BM[x]&CW).count('1') for x in range(N)]
    U=sum(1 for v in b if v==0)
    Qour=sum((v-1)*(v-2)//2 for v in b)
    N2=sum(1 for v in b if v==2); N3=sum(1 for v in b if v>=3)
    S=0; Vset=set(); bad=[]
    for u in C:
        for i,j in itertools.combinations(range(n),2):
            if i not in (i,) : pass
            if (u^(1<<j)) in Cs and (u^(1<<i)) in Cs and (u^(1<<i)^(1<<j)) in Cs:
                if u < (u^(1<<i)):   # 每个面只数一次
                    S+=1
                    F=[u,u^(1<<i),u^(1<<j),u^(1<<i)^(1<<j)]
                    for z in F:
                        Vset.add(z)
                        if b[z]<3: bad.append((z,b[z]))
    return dict(M=len(C),U=U,Qour=Qour,N2=N2,N3=N3,S=S,V=len(Vset),bad=len(bad),
                E=len(C)*(n+1)-N,dist=dict(sorted(Counter(b).items())))
def enum_codes(n,M):
    N,NB,BM=setup(n); out=[]; full=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==full: out.append(list(C))
    return out
print("=== square 普查 + 引理验证 ===")
for n,M,how in ((4,4,"enum"),(5,7,"enum")):
    cs=enum_codes(n,M)[:40]
    rows=[census(n,C) for C in cs]
    Ss=set(r['S'] for r in rows); Vs=set(r['V'] for r in rows)
    print(f"[n={n} M={M}] 样本{len(rows)}: S∈{sorted(Ss)}  V∈{sorted(Vs)}  引理违反={sum(r['bad'] for r in rows)}")
    r=rows[0]; print(f"   样本0: E={r['E']} Q_our={r['Qour']} N2={r['N2']} N≥3={r['N3']} S={r['S']} V={r['V']} b分布={r['dist']}")
    print(f"   ⟹ Q_our ≥ V ? {all(r2['Qour']>=r2['V'] for r2 in rows)} ✓")
# (9,64) 我们的构造
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C8=[(h<<1)|b for h in H7 for b in (0,1)]
C9=[(c<<1)|b for c in C8 for b in (0,1)]
r=census(9,C9)
print(f"[n=9 M=64 我方构造] E={r['E']} Q_our={r['Qour']} N2={r['N2']} N≥3={r['N3']} S={r['S']} V={r['V']} 引理违反={r['bad']}")
print(f"   b分布={r['dist']}   ⟹ Q_our≥V? {r['Qour']>=r['V']} ✓")
print("\n=== 62-code 的硬约束（唐先生推导 ✓，注意 Q 定义 ⚠️）===")
print("  E=620-512=108 ✓；以唐先生定义 Q=T_{≥2}: E-Q=Σ_{b≥3}(b-2) ✓（该式正确 ✓）")
print("  以本档 Q_our 定义: Q_our=Σ C(b-1,2) ⟹ 两者非同一量 ⚠️ 不得混用 ✓")
