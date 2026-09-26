#!/usr/bin/env python3
"""n=6 加固：171+ 个最优码跨多少 (a) 距离分布签名 (b) 真正的 B_6-等价类？
   若跨多类而 Q 全同 ⟹ pinning 证据显著增强 ✓"""
import random, itertools
from collections import Counter
from itertools import combinations, permutations

def run(n, M, trials=260, iters=400, seed=11):
    random.seed(seed)
    N=1<<n
    nbr=[[v ^ (1<<i) for i in range(n)] for v in range(N)]
    ok={}
    for _ in range(trials):
        C=set(random.sample(range(N),M)); cnt=[0]*N
        for c in C:
            cnt[c]+=1
            for u in nbr[c]: cnt[u]+=1
        for _it in range(iters):
            unc=[x for x in range(N) if cnt[x]==0]
            if not unc: break
            p=random.choice(unc); cadd=random.choice([p]+nbr[p])
            if cadd in C: continue
            C.add(cadd); cnt[cadd]+=1
            for u in nbr[cadd]: cnt[u]+=1
            best,bw=-1,None
            for w in list(C):
                if w==cadd: continue
                cnt[w]-=1
                for u in nbr[w]: cnt[u]-=1
                sc=sum(1 for x in [w]+nbr[w] if cnt[x]==0)
                if bw is None or sc<best: best,bw=sc,w
                cnt[w]+=1
                for u in nbr[w]: cnt[u]+=1
            if bw is not None:
                C.discard(bw); cnt[bw]-=1
                for u in nbr[bw]: cnt[u]-=1
        if min(cnt)>0 and len(C)==M: ok[frozenset(C)]=cnt[:]
    return n, N, ok

n, N, ok = run(6, 12)
E = 12*7-64
print(f"n=6 M=12: 收集 {len(ok)} 个不同最优码")
# (a) 距离分布签名
sig=Counter()
for C in ok:
    A=Counter((a^b).bit_count() for a,b in combinations(sorted(C),2))
    sig[tuple(sorted(A.items()))]+=1
print(f"(a) 距离分布签名种类 = {len(sig)}  （>1 ⟹ 样本跨越多个不同结构 ✓）")
# (b) 真正的 B_6 等价类（坐标置换 720 × 平移 64）
maps=[]
for p in permutations(range(n)):
    base=[]
    for x in range(N):
        y=0
        for i in range(n):
            if (x>>i)&1: y|=1<<p[i]
        base.append(y)
    for t in range(N):
        m=[b^t for b in base]; maps.append(m)
print(f"    群阶 = {len(maps)}")
cls={}
for C in ok:
    best=None
    for mp in maps:
        im=tuple(sorted(mp[x] for x in C))
        if best is None or im<best: best=im
    cls.setdefault(best,0); cls[best]+=1
print(f"(b) **B_6-等价类数 = {len(cls)}**")
q=Counter()
for rep in cls:
    A=sum(1 for a,b in combinations(rep,2) if (a^b).bit_count()<=2)
    q[2*A-E]+=1
print(f"    各类的 Q 值分布 = {dict(sorted(q.items()))}  （若只有 {{4:k}} ⟹ 多类同值 ⟹ pinning 证据强 ✓）")
print(f"    各类代表（前 3）:")
for i,rep in enumerate(sorted(cls)[:3],1):
    print(f"      类{i} (大小{cls[rep]}): {' '.join(format(x,'06b') for x in rep)}")
