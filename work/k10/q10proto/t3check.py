#!/usr/bin/env python3
"""核验不等式对 Q_2 ≤ T_3 ≤ ((n+1)/3)Q_2 在所有样本上成立"""
import itertools
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def check(n,C):
    N,BM=setup(n); W={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    if any(v==0 for v in W.values()): return None
    Q2=sum((v-1)*(v-2)//2 for v in W.values())
    T3=sum(v*(v-1)*(v-2)//6 for v in W.values())
    return dict(Q2=Q2,T3=T3,lo=(Q2<=T3),hi=(T3<=(n+1)/3*Q2+1e-9),n=n)
def enum_codes(n,M,cap=25):
    N,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 不等式对核验: Q_2 ≤ T_3 ≤ ((n+1)/3)·Q_2 ===")
tot=0; bad=0
for n,M in ((4,4),(4,5),(4,6),(5,7)):
    rs=[r for r in (check(n,C) for C in enum_codes(n,M,cap=25)) if r]
    ok=all(r['lo'] and r['hi'] for r in rs); tot+=len(rs); bad+=sum(1 for r in rs if not(r['lo'] and r['hi']))
    print(f"[n={n} M={M}] 样本{len(rs)}: 全部满足={ok} ✓ ｜ Q_2∈{sorted(set(r['Q2'] for r in rs))} T_3∈{sorted(set(r['T3'] for r in rs))}")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=check(9,C9)
print(f"[n=9 M=64] Q_2={r['Q2']} T_3={r['T3']} 下界✓={r['lo']} 上界✓={r['hi']}")
print(f"\n总样本 {tot}，违反 {bad} ⟹ {'不等式对成立 ✓✓' if bad==0 else '✗ 有违反'}")
