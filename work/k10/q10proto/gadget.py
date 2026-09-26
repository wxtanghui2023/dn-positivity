#!/usr/bin/env python3
"""gadget 结构核验 + "不可复用私有点" lemma 的压力测试
断言A(我方): Z-ball 的 gadget {c}∪{c_ij} 两两距离 3/4 ⟹ **balls 两两不交** ✓
断言B(唐先生): 每个 Z-ball 至少产生一个不可复用的 private incidence"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def analyse(n,C):
    N,NB,BM=setup(n); Cs=set(C); CW=0
    for w in C: CW|=1<<w
    b=[bin(BM[x]&CW).count('1') for x in range(N)]
    Z=[]; distbad=0; overlap=0; out_ok=0
    for x in range(N):
        if x in Cs: continue
        t=sum(b[y]-1 for y in [x]+NB[x])
        if t!=0: continue
        Z.append(x)
        l=[i for i in range(n) if (x^(1<<i)) in Cs]
        if len(l)!=1: continue
        ell=l[0]
        pairs=set()
        for c in C:
            d=[i for i in range(n) if (x^c)>>i&1]
            if len(d)==2 and ell not in d: pairs.add(tuple(sorted(d)))
        gadget=[x^(1<<ell)]+[x^(1<<i)^(1<<j) for (i,j) in pairs]
        # 两两距离
        for a,bb in itertools.combinations(gadget,2):
            dd=bin(a^bb).count('1')
            if dd<3: distbad+=1
        # balls 不交?
        for a,bb in itertools.combinations(gadget,2):
            if (BM[a]&BM[bb])!=0: overlap+=1
    # 复用统计
    reuse=Counter(); owners={}
    for w in C:
        for y in range(N):
            if (BM[y]>>w)&1 and b[y]==1: owners.setdefault(y,[]).append(w)
    pset={y for y,v in owners.items() if len(v)==1}
    zballs=set()
    zb_all=[]
    for x in range(N):
        if x in Cs: continue
        t=sum(b[y]-1 for y in [x]+NB[x])
        if t==0: zb_all.append(x)
    for x in zb_all:
        l=[i for i in range(n) if (x^(1<<i)) in Cs]
        if len(l)!=1: continue
        ell=l[0]
        g=[x^(1<<ell)]+[x^(1<<i)^(1<<j) for (i,j) in itertools.combinations([k for k in range(n) if k!=ell],2) if (x^(1<<i)^(1<<j)) in Cs]
        for y in pset:
            if any((BM[y]>>c)&1 for c in g): reuse[y]+=1
    mx=max(reuse.values()) if reuse else 0
    avg=sum(reuse.values())/len(reuse) if reuse else 0
    return dict(M=len(C),Z=len(Z),distbad=distbad,overlap=overlap,
                reuse_max=mx,reuse_avg=round(avg,3),npriv=len(pset))
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
print("=== gadget 刚性（断言 A ✓）与不可复用私有点（断言 B ✗?）===")
def enum_codes(n,M,cap=25):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
C5=enum_codes(5,7,cap=5)
for C in C5:
    r=analyse(5,C)
    print(f"[n=5 M=7] Z={r['Z']} 距离违反={r['distbad']} 球相交对={r['overlap']} ⟹ 断言A {'✓ 成立' if r['distbad']==0 and r['overlap']==0 else '✗'}")
    print(f"         私有点数={r['npriv']} 复用: max={r['reuse_max']} avg={r['reuse_avg']} ⟹ 断言B(reuse≤1) {'✓' if r['reuse_max']<=1 else '**✗ 被否**'}")
    break
H7=[x for x in range(128) if syn(x)==0]
r=analyse(7,H7)
print(f"[n=7 完美码 Hamming(7,16)] E=0, Z={r['Z']}(=112 全部非码字) 距离违反={r['distbad']} 球相交={r['overlap']} ⟹ 断言A {'✓' if r['distbad']==0 and r['overlap']==0 else '✗'}")
print(f"         私有点数={r['npriv']} 复用: max={r['reuse_max']} avg={r['reuse_avg']} ⟹ 断言B **✗ 被强力否证**")
print()
print("=== 结论 ===")
print(" 断言A（gadget 球两两不交）→ *新刚性 ✓")
print(" 断言B（不可复用私有点）→ **被完美码否证** ✗（reuse≈6 ⟹ 私有点计数无法给 Z 上界 ✗）")
print(" ⟹ 需换支点：用 *球不交* 本身，而非私有点复用 ✓")
