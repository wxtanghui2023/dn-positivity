#!/usr/bin/env python3
"""T₃ 几何拆分 + A≤2 链接：
 T₃ = I + II + III，I=Σ_{x∈C}C(d(x),2)，II=Σ_{x∈C}C(d(x),3)，III=Σ_{x∉C}C(b(x),3)
 我方推导: I ≤ 2A₂（每个距离-2 对至多 2 个码字中点）
 并验证 κ = max|N[c₁]∩N[c₂]∩N[c₃]| ≤ 1"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def analyse(n,C):
    N,NB,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    assert all(v>=1 for v in b.values())
    E=sum(v-1 for v in b.values()); Q2=sum((v-1)*(v-2)//2 for v in b.values())
    T3=sum(v*(v-1)*(v-2)//6 for v in b.values())
    I=sum((b[x]-1)*(b[x]-2)//2 for x in Cs)
    II=sum((b[x]-1)*(b[x]-2)*(b[x]-3)//6 for x in Cs)
    III=sum(b[x]*(b[x]-1)*(b[x]-2)//6 for x in range(N) if x not in Cs)
    A1=A2=0
    for c1,c2 in itertools.combinations(C,2):
        d=bin(c1^c2).count('1')
        if d==1: A1+=1
        elif d==2: A2+=1
    # κ: 三重球交的最大值
    kappa=0
    for trip in itertools.combinations(C,3):
        cnt=sum(1 for x in range(N) if all((BM[c]>>x)&1 for c in trip))
        kappa=max(kappa,cnt)
    return dict(M=len(C),E=E,Q2=Q2,T3=T3,I=I,II=II,III=III,sum3=I+II+III,
        A1=A1,A2=A2,ok_sum=(T3==I+II+III),ok_I=(I<=2*A2),kappa=kappa,
        ratioI=round(I/max(1,2*A2),3))
def enum_codes(n,M,cap=20):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== T₃ 几何拆分 + A≤2 链接 ===")
for n,M in ((4,4),(4,5),(5,7)):
    rs=[analyse(n,C) for C in enum_codes(n,M)]
    ok_s=all(r['ok_sum'] for r in rs); ok_I=all(r['ok_I'] for r in rs)
    print(f"[n={n} M={M} {'=K' if (n,M) in ((4,4),(5,7)) else '>K'}] 样本{len(rs)}")
    print(f"   T₃=I+II+III 全过={ok_s} ✓ | **I ≤ 2A₂ 全过={ok_I}** ✓ | κ_max={max(r['kappa'] for r in rs)}")
    r=rs[0]; print(f"   样本0: T₃={r['T3']} I={r['I']} II={r['II']} III={r['III']} | A₁={r['A1']} A₂={r['A2']} 2A₂={2*r['A2']} I/2A₂={r['ratioI']}")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=analyse(9,C9)
print(f"[n=9 M=64] T₃={r['T3']} **I={r['I']} II={r['II']} III={r['III']}** | A₁={r['A1']} A₂={r['A2']} 2A₂={2*r['A2']} | I≤2A₂? {r['ok_I']} | κ={r['kappa']}")
print()
print("=== 读数 ===")
print(" I = Σ_{x∈C}C(d(x),2) = G₁(C) 中**楔形数**（x 与两个码字邻居）✓")
print(" 每个这样的楔形 ⟹ {c_i,c_j} 是距离-2 码字对 ✓；该对至多 2 个码字中点 ⟹ **I ≤ 2A₂** ✓✓")
print(" ⟹ **T₃ ≤ 2A₂ + II + III**：A≤2 第一次真正进入 T₃ 的界 ✓（部分 ✓）")
print(" 剩余缺口: II（G₁(C) 的三角形数×中点重数）与 III（非码字中心的三邻点块）仍需 A≤2 化 ✗")
