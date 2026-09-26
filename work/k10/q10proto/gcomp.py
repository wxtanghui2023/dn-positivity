#!/usr/bin/env python3
"""G_C（距离-1 图）连通分量普查 + 检验 "I≥3 ⟹ h>0" 是否成立"""
import itertools
from collections import Counter, defaultdict
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def gcomp(n,C):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    I=sum((b[x]-1)*(b[x]-2)//2 for x in Cs)
    h=sum(1 for x in C if b[x]-1>=3)
    deg={c:sum(1 for d in C if bin(c^d).count('1')==1) for c in C}
    adj=defaultdict(list)
    for u,v in itertools.combinations(C,2):
        if bin(u^v).count('1')==1: adj[u].append(v); adj[v].append(u)
    seen=set(); comps=[]
    for c in C:
        if c in seen: continue
        stack=[c]; comp=[]
        while stack:
            u=stack.pop()
            if u in seen: continue
            seen.add(u); comp.append(u)
            stack.extend(adj[u])
        comps.append(comp)
    # 分量类型：路径（max deg<=2 & 连通）还是其它
    types=Counter(); maxpath=0
    for comp in comps:
        dmax=max(deg[v] for v in comp)
        if dmax<=2:
            types['path']+=1; maxpath=max(maxpath,len(comp)-1)
        else:
            types[f'branch(deg{dmax})']+=1
    return dict(M=len(C),I=I,h=h,degmax=max(deg.values()),ncomp=len(comps),
        compsz=dict(sorted(Counter(len(c) for c in comps).items())),
        types=dict(types),maxpath=maxpath,K13=(h>0),sumdeg=sum(deg.values()))
def enum_codes(n,M,cap=60):
    N,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
print("=== G_C 连通分量普查 ===")
for n,M in ((4,4),(4,5),(4,6),(5,7),(5,8)):
    rs=[gcomp(n,C) for C in enum_codes(n,M,cap=60)]
    tag='=K' if (n,M) in ((4,4),(5,7)) else '>K'
    Iv=sorted(set(r['I'] for r in rs)); hv=sorted(set(r['h'] for r in rs))
    dm=sorted(set(r['degmax'] for r in rs))
    tp=Counter()
    for r in rs: tp.update(r['types'])
    print(f"[n={n} M={M} {tag}] 样本{len(rs)}: I∈{Iv} h∈{hv} deg_max∈{dm} | 分量类型={dict(tp)} | maxpath∈{sorted(set(r['maxpath'] for r in rs))}")
    r=rs[0]; print(f"   样本0: 分量数={r['ncomp']} 分量大小={r['compsz']} K_{'{1,3}'}={r['K13']}")
print()
print("=== 检验: I≥3 是否 ⟹ h>0 ===")
bad=0; tot=0; ex=None
for n,M in ((4,5),(4,6),(5,8)):
    for C in enum_codes(n,M,cap=60):
        r=gcomp(n,C); tot+=1
        if r['I']>=3 and r['h']==0:
            bad+=1
            if ex is None: ex=(n,M,r['I'],r['h'],r['degmax'],r['types'],r['maxpath'])
print(f" 样本 {tot} 中 I≥3 且 h=0 的样本数 = {bad}  ⟹ {'**命题假** ✗✓' if bad>0 else '未观察到反例'}")
if ex: print(f" 反例: (n={ex[0]} M={ex[1]}) I={ex[2]} h={ex[3]} deg_max={ex[4]} 分量类型={ex[5]} maxpath={ex[6]}")
print()
print("=== 几何事实复核 ===")
print(" 三角形/K₄: a,b,c 两两距离 1 ⟹ a+b=e_i, b+c=e_j ⟹ a+c=e_i+e_j 权重 2 ✗ ⟹ **无三角形** ✓（诱导子图二分）")
