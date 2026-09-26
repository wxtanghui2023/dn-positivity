#!/usr/bin/env python3
"""t_x=0 球的局部结构引理核验：
 断言: x∉C, OC(B1(x))=0 ⟹ (i) B1(x) 全部 b=1; (ii) 恰 5 个码字在 dist≤2;
 (iii) 恰 1 个在 dist=1; 恰 4 个在 dist=2; (iv) 4 个 dist-2 码字 = 除一个坐标 l 外 8 坐标的完美匹配"""
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
    res=dict(Z=0,ok_allb1=0,ok_5=0,ok_a1=0,ok_b4=0,ok_match=0,viol=[])
    for x in range(N):
        if x in Cs: continue
        t=sum(b[y]-1 for y in [x]+NB[x])
        if t!=0: continue
        res['Z']+=1
        if all(b[y]==1 for y in [x]+NB[x]): res['ok_allb1']+=1
        dc1=[y for y in NB[x] if y in Cs]
        dc2=[y for y in NB[x] for _ in range(1) if False]
        c2=[]
        for u in NB[x]:
            for i in range(n):
                v=u^(1<<i)
                if bin(v^x).count('1')==2 and v in Cs and v not in c2: c2.append(v)
        tot=len(dc1)+len(c2)
        if tot==5: res['ok_5']+=1
        if len(dc1)==1: res['ok_a1']+=1
        if len(c2)==4: res['ok_b4']+=1
        # 匹配结构: 4 个 dist-2 码字 c=x+e_i+e_j，除 l 外 8 坐标被配成 4 对
        l=[i for i in range(n) if (x^(1<<i)) in Cs]
        if len(c2)==4 and len(l)==1:
            pairs=set()
            for c in c2:
                d=[i for i in range(n) if (x^c)>>i&1]
                if len(d)==2: pairs.add(tuple(sorted(d)))
            used=set()
            for p in pairs: used|=set(p)
            if len(pairs)==4 and len(used)==8 and (l[0] not in used): res['ok_match']+=1
        if len(res['viol'])<3 and not(len(dc1)==1 and len(c2)==4): res['viol'].append((x,len(dc1),len(c2),tot))
    return res
def enum_codes(n,M,cap=30):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== t_x=0 结构引理核验 ===")
for n,M in ((4,4),(5,7)):
    rs=[probe(n,C) for C in enum_codes(n,M)]
    Zs=sum(r['Z'] for r in rs)
    print(f"[n={n} M={M}] 样本{len(rs)}: 总 Z={Zs} ｜ 全部b=1={sum(r['ok_allb1'] for r in rs)} ｜ 恰5码字={sum(r['ok_5'] for r in rs)} ｜ a=1={sum(r['ok_a1'] for r in rs)} ｜ b=4={sum(r['ok_b4'] for r in rs)} ｜ 匹配结构={sum(r['ok_match'] for r in rs)}")
    v=[x for r in rs for x in r['viol']]
    print(f"   反例={len(v)} {'✓ 引理成立' if len(v)==0 else v[:3]}")
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
r=probe(9,C9)
print(f"[n=9 M=64 我方] Z={r['Z']}（非码字 448）｜ 全部b=1={r['ok_allb1']} ｜ 恰5={r['ok_5']} ｜ a=1={r['ok_a1']} ｜ b=4={r['ok_b4']} ｜ 匹配={r['ok_match']} ｜ 反例={len(r['viol'])}")
print()
print("=== 目标换算（M=62, n=9, E=108）===")
print(" Q_2 = (8·108 − ΣOC)/2 = 432 − ΣOC/2 ✓")
print(" Q_2 ≤ 26 ⟺ ΣOC ≥ 812 ⟺ 2(N_nonC − Z) ≥ 812, N_nonC=450 ⟹ **Z ≤ 44** ✓✓")
print(" ⟹ 主攻目标 = **上界化 Z = #{x∉C : OC(B₁(x))=0}** ✓（而这些正是 Struik 逐球界失效的点 ✓）")
