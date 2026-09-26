#!/usr/bin/env python3
"""修正版: 验 T3 = #三角形 是否对任意二元码成立 (T3 = Σ_x C(b(x),3) ✓)"""
import itertools, random
from collections import Counter
def build(n):
    N=1<<n; BALL=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        BALL[x]=m
    return N,BALL
def check(n,C,tag):
    N,BALL=build(n)
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    T3=sum(v*(v-1)*(v-2)//6 for v in bl)          # ✓ 每个点一次
    tri=0; mus=Counter()
    for u,v,w in itertools.combinations(C,3):
        if max(bin(u^v).count('1'),bin(u^w).count('1'),bin(v^w).count('1'))<=2:
            tri+=1
        mus[bin(BALL[u]&BALL[v]&BALL[w]).count('1')]+=1
    print(f"[{tag:26}] |C|={len(C):3} T3={T3:5} #tri={tri:4} 恒等={'✓✓' if T3==tri else '✗✗'} μ∈{sorted(mus)} μ≥2个数={sum(c for m,c in mus.items() if m>=2)}")
print("=== 极值码 ===")
n=4;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),4):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: check(4,list(C),"(4,4)=K"); break
n=5;N,BALL=build(n);FULL=(1<<N)-1
for C in itertools.combinations(range(N),7):
    cov=0
    for c in C: cov|=BALL[c]
    if cov==FULL: check(5,list(C),"(5,7)=K"); break
c1=[int(x,2) for x in "000000 000001 000010 001111 010111 011100 100111 101100 110100 111001 111010 111011".split()]
check(6,c1,"(6,12)=K 类#1")
print("\n=== 非极值覆盖码 ===")
random.seed(7)
def rc(n,M,tr=300000):
    N,BALL=build(n);F=(1<<N)-1
    for _ in range(tr):
        C=random.sample(range(N),M); cov=0
        for c in C: cov|=BALL[c]
        if cov==F: return C
    return None
for (n,M) in ((4,5),(4,6),(4,7),(4,8),(5,8),(5,9),(5,10)):
    C=rc(n,M)
    if C: check(n,C,f"({n},{M})>K")
print("\n=== 任意码（不覆盖）===")
random.seed(11)
for (n,M) in ((5,5),(6,6),(6,10),(7,8),(8,10)):
    check(n,random.sample(range(1<<n),M),f"({n},{M}) 任意")
