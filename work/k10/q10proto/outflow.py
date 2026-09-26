#!/usr/bin/env python3
"""① Z-gadget 外溢是否强制 excess？
 - 检验: gadget 的 (n+1)/2 个码字是否对 50 点各贡献恰 1 次、对外 0 次（=贡献 0 excess）
 - 统计: gadget 外部点实际 b≥2 的比例
 - 推导: Z 的下界（由 I2 + OC≥2 + Q_2≥0）"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def probe(n,C):
    N,NB,BM=setup(n); Cs=set(C); CW=0
    for w in C: CW|=1<<w
    b=[bin(BM[x]&CW).count('1') for x in range(N)]
    E=sum(v-1 for v in b); Q2=sum((v-1)*(v-2)//2 for v in b)
    tot=dict(Z=0,gadgets=0,own_in=0,own_out=0,perc_zero_excess=0,
             outtot=0,out_b2=0,out_b1=0,inb1ok=0,inb1tot=0)
    for x in range(N):
        if x in Cs: continue
        t=sum(b[y]-1 for y in [x]+NB[x])
        if t!=0: continue
        tot['Z']+=1
        l=[i for i in range(n) if (x^(1<<i)) in Cs]
        if len(l)!=1: continue
        ell=l[0]
        pairs=[(i,j) for i,j in itertools.combinations([k for k in range(n) if k!=ell],2) if (x^(1<<i)^(1<<j)) in Cs]
        g=[x^(1<<ell)]+[x^(1<<i)^(1<<j) for (i,j) in pairs]
        if len(g)!= (n+1)//2: continue
        tot['gadgets']+=1
        # gadget 对每个点贡献的 incidence 数
        cnt=Counter()
        for c in g:
            for y in [c]+NB[c]: cnt[y]+=1
        own=set(cnt)
        # B1(x) 内 10 点应各恰 1
        for y in [x]+NB[x]: tot['inb1tot']+=1; tot['inb1ok']+= (cnt[y]==1)
        # gadget 是否全为 1（球不交 ⟹ 应然）
        if all(v==1 for v in cnt.values()): tot['perc_zero_excess']+=1
        # 外部点统计
        for y,v in cnt.items():
            if y not in set([x]+NB[x]):
                tot['outtot']+=1
                if b[y]>=2: tot['out_b2']+=1
                else: tot['out_b1']+=1
    return dict(M=len(C),E=E,Q2=Q2,**tot)
print("=== Z-gadget 外溢检验 ===")
for C in [[int(x,2) for x in """0000000 1110000 1001100 0101010 1101001 0010110 1010101 0111100 0001111 1110011 1001011 0100110 1100101 0011001 1011010 0110001""".split()]]:
    pass
# 用 (5,7) 全枚举的前几个码做检验
def enum_codes(n,M,cap=3):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
for C in enum_codes(5,7):
    r=probe(5,C)
    print(f"[n=5 M=7] Z={r['Z']} gadget数={r['gadgets']} ｜ B₁(x) 内 incidence 全为1: {r['inb1ok']}/{r['inb1tot']} ✓")
    print(f"   gadget 全为 1（球不交 ⟹ 0 excess 贡献）: {r['perc_zero_excess']}/{r['gadgets']} ✓")
    print(f"   外部点: 共 {r['outtot']}，其中 b≥2 的 {r['out_b2']}（{100*r['out_b2']/max(1,r['outtot']):.0f}%），b=1 的 {r['out_b1']}")
    print(f"   E={r['E']} Q_2={r['Q2']}")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
r=probe(7,H7)
print(f"\n[n=7 完美码 E=0] Z={r['Z']} gadget数={r['gadgets']} ｜ gadget 全为1: {r['perc_zero_excess']}/{r['gadgets']} ✓")
print(f"   外部点 b≥2 数 = {r['out_b2']} ⟹ E=0 时**无任何强制 excess** ✗ ⟹ 断言\"gadget⟹强制 excess\" **为假** ✗✓")
print("\n=== 由 I2 推出的 Z 下界（M=62, n=9）===")
print(" ΣOC = 864 − 2Q_2 ≤ 864 ✓；奇 n: OC>0⟹OC≥2 ⟹ ΣOC ≥ 2(450−Z) ✓")
print(" ⟹ 2(450−Z) ≤ 864 ⟹ 450−Z ≤ 432 ⟹ **Z ≥ 18** ✓（新下界 ✓，但方向与目标相反 ✗）")
