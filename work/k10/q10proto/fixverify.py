#!/usr/bin/env python3
"""确认修正恒等式: Σ_{pairs}|holes({c,c'})| = (M-1)N1 + N2"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def check(n,C):
    N,NB,BM=setup(n); Cs=set(C)
    W={x:frozenset(c for c in C if (BM[c]>>x)&1) for x in range(N)}
    b={x:len(W[x]) for x in range(N)}
    if any(v==0 for v in b.values()): return None
    N1=sum(1 for v in b.values() if v==1); N2=sum(1 for v in b.values() if v==2)
    tot=0; ev=0
    for c1,c2 in itertools.combinations(C,2):
        S=frozenset([c1,c2])
        h=sum(1 for x in range(N) if W[x] and W[x]<=S); tot+=h
        ev+=sum(1 for x in range(N) if W[x]==S)
    return dict(M=len(C),N1=N1,N2=N2,tot=tot,ev=ev,pred=(len(C)-1)*N1+N2,ok=(tot==(len(C)-1)*N1+N2),ok2=(ev==N2))
def enum_codes(n,M,cap=15):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 修正恒等式实测 ===")
for n,M in ((4,4),(5,7)):
    rs=[r for r in (check(n,C) for C in enum_codes(n,M)) if r]
    print(f"[n={n} M={M}] 样本{len(rs)}: Σ|holes|=(M−1)N₁+N₂ 全过={all(r['ok'] for r in rs)} ✓ | Σe=N₂ 全过={all(r['ok2'] for r in rs)} ✓")
    r=rs[0]; print(f"   样本0: M={r['M']} N₁={r['N1']} N₂={r['N2']} Σ|holes|={r['tot']} 预测={r['pred']} ✓ ｜ Σe={r['ev']} ✓")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=check(9,C9)
print(f"[n=9 M=64] M={r['M']} N₁={r['N1']} N₂={r['N2']} Σ|holes|={r['tot']} 预测={r['pred']} ⟹ {'✓✓' if r['ok'] else '✗'} ｜ Σe={r['ev']}=N₂? {'✓' if r['ok2'] else '✗'}")
