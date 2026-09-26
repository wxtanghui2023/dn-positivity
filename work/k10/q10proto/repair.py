#!/usr/bin/env python3
"""d_C=3 局部结构 + 删除/移位修复实测"""
import itertools
from collections import Counter
def setup(n):
    N=1<<n; NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
    BM=[1<<x for x in range(N)]
    for x in range(N):
        for y in NB[x]: BM[x]|=1<<y
    return N,NB,BM
def covers(BM,N,C):
    cov=0
    for c in C: cov|=BM[c]
    return cov==(1<<N)-1
def analyse(n,C):
    N,NB,BM=setup(n); Cs=set(C); full=(1<<N)-1
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    priv={c:[x for x in range(N) if (BM[c]>>x)&1 and b[x]==1] for c in C}
    out=[]
    for x in C:
        dC=b[x]-1
        if dC<3: continue
        nbrs=[y for y in NB[x] if y in Cs]
        # 取前三个邻居
        trip=nbrs[:3]
        second=[x^a^c for a,c in itertools.combinations(trip,2)]
        r=sum(1 for m in second if m in Cs)
        px=priv[x]
        free=[y for y in NB[x] if y not in Cs]
        loc=Counter('free' if p in free else ('neighbor' if p in nbrs else 'self') for p in px)
        # 删除 x
        Cdel=[c for c in C if c!=x]
        cov=0
        for c in Cdel: cov|=BM[c]
        uncov=bin(full^cov).count('1') if cov!=full else 0
        # 移位 x -> p (私有点)
        shifts=[]
        for tgt in (px[:1]+second[:2]):
            Csh=[c for c in C if c!=x]+[tgt]
            if len(set(Csh))==len(C): shifts.append((tgt, covers(BM,N,Csh)))
        out.append(dict(x=x,dC=dC,r=r,npriv=len(px),loc=dict(loc),
            uncov_on_delete=uncov, shifts=shifts, b_of_x=b[x]))
    return dict(M=len(C),h=len(out),items=out,S=sum(b[y]*(b[y]-1)//2 for y in range(N) if y not in Cs),
        E=sum(v-1 for v in b.values()), I=sum((b[x]-1)*(b[x]-2)//2 for x in Cs))
print("=== d_C≥3 局部结构 + 修复实测 ===")
def enum_codes(n,M,cap=40):
    N,NB,BM=setup(n); out=[]; fullm=(1<<N)-1
    for C in itertools.combinations(range(N),M):
        cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            out.append(list(C))
            if len(out)>=cap: break
    return out
for n,M in ((4,5),(4,6),(5,8)):
    rs=[r for r in (analyse(n,C) for C in enum_codes(n,M,cap=40)) if r['h']>0]
    if not rs: print(f"[n={n} M={M}] 无 d_C≥3 样本"); continue
    tot=sum(r['h'] for r in rs)
    locs=Counter()
    for r in rs:
        for it in r['items']: locs.update(it['loc'])
    delok=sum(1 for r in rs for it in r['items'] if it['uncov_on_delete']==0)
    shok=sum(1 for r in rs for it in r['items'] for (t,g) in it['shifts'] if g)
    shn=sum(1 for r in rs for it in r['items'] for (t,g) in it['shifts'])
    print(f"[n={n} M={M}] 样本{len(rs)} 高内部度码字共{tot}个")
    print(f"   私有点位置分布={dict(locs)}  |  删除后仍覆盖={delok}/{tot}  |  移位成功={shok}/{shn}")
    r=rs[0]; it=r['items'][0]
    print(f"   例: E={r['E']} Q₂={r['I']} S={r['S']} | x 的 d_C={it['dC']} r={it['r']} 私有点数={it['npriv']} 删后失覆盖={it['uncov_on_delete']} 移位={it['shifts']}")
print()
print("=== 读数 ===")
print(" ① 私有点位置: 若全在 free（非码字邻居）则支持'私有点在自由邻居中' ✓")
print(" ② 删除后仍覆盖 = 0 ⟹ 最小性阻止纯删除（与之前的 minimality 推论一致 ✓）")
print(" ③ 移位成功次数 > 0 ⟹ 存在同大小覆盖码（不构成矛盾 ✗，但给出局部可动性 ✓）")
