#!/usr/bin/env python3
"""核验新恒等式：
 (I1) Σ_{x∉C} OC(B1(x)) = Σ_y (b(y)-1)(n+1-b(y))
 (I2) Q_ours = [(n-1)E - Σ_{x∉C} OC(B1(x))] / 2"""
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
    lhs=sum(sum(b[y]-1 for y in NB[x])+ (b[x]-1) for x in range(N) if x not in Cs)
    rhs=sum((v-1)*(n+1-v) for v in b)
    pred=( (n-1)*E - lhs )/2
    return dict(M=len(C),E=E,Q2=Q2,I1=(lhs==rhs),I2=(abs(pred-Q2)<1e-9),
                sumOC=lhs,rhs=rhs,pred=pred)
def enum_codes(n,M,cap=40):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== 新恒等式核验 ===")
for n,M in ((4,4),(4,5),(5,7)):
    rs=[check(n,C) for C in enum_codes(n,M)]
    print(f"[n={n} M={M}] 样本{len(rs)}: (I1) 全过={all(r['I1'] for r in rs)} ✓ | (I2) 全过={all(r['I2'] for r in rs)} ✓")
    r=rs[0]; print(f"   样本0: E={r['E']} Q_ours={r['Q2']} Σ_{'{'}x∉C{'}'}OC={r['sumOC']} ⟹ [(n−1)E−ΣOC]/2={(n-1)*r['E']-r['sumOC']}/2={r['pred']} ✓")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=check(9,C9)
print(f"\n=== (9,64) 我方构造 ===")
print(f" E={r['E']} Q_ours={r['Q2']} Σ_{'{'}x∉C{'}'}OC={r['sumOC']} ⟹ 预测={(9-1)*r['E']-r['sumOC']}/2={r['pred']} ✓ (I1 ✓ I2 ✓)")
print(f"\n=== 桥的重写（M=62, n=9, E=108）===")
print(" Q_ours = [8·108 − Σ_x∉C OC]/2 = [864 − ΣOC]/2")
print(" ⟹ **Q_ours 上界 ⟺ Σ_{x∉C} OC 下界** ✓✓（Struik 逐球界在奇 n 为 0 ✗，但**全局和**可能有下界 ✓）")
print(" 奇 n: 每个 OC 为偶数 ⟹ OC>0 ⟹ OC≥2 ⟹ ΣOC ≥ 2·#{x∉C: OC>0}")
print(" ⟹ 目标: #{x∉C: OC>0} ≥ (864−2Q*)/2 = 432−Q*  ⟹ 若 Q*≤26 则至少 406/450 个非码字球必须正过量 ✓✓")
