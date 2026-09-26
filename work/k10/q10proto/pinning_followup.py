#!/usr/bin/env python3
"""核验：① P = N₁ ?  ② 极值壳上 profile 是否被强制 ?  ③ L(c)≥1 是否刻画最优性 ?"""
import itertools, random
from collections import Counter
def build(n):
    N=1<<n; ball=[0]*N
    for x in range(N):
        m=1<<x
        for i in range(n): m|=1<<(x^(1<<i))
        ball[x]=m
    return N,ball,(1<<N)-1
def rows(n,M,codes,ball,full,N):
    out=[]
    for C in codes:
        cm=0
        for c in C: cm|=1<<c
        cov=0
        for c in C: cov|=ball[c]
        if cov!=full: continue
        b=[bin(ball[x]&cm).count('1') for x in range(N)]
        r=[]
        for c in C:
            bit=1<<c
            r.append(sum(1 for x in range(N) if (ball[x]&cm)==bit))
        prof=tuple(sorted(Counter(b).items()))
        out.append(dict(C=tuple(C),b=b,r=tuple(r),P=sum(r),N1=b.count(1),
                        Q=sum((v-1)*(v-2)//2 for v in b),prof=prof))
    return out
for n,Ms in ((4,(4,5,6)),(5,(7,))):
    N,ball,full=build(n)
    for M in Ms:
        rs=rows(n,M,itertools.combinations(range(N),M),ball,full,N)
        if not rs: continue
        eq=all(x['P']==x['N1'] for x in rs)
        print(f"n={n} M={M}: 覆盖码 {len(rs)} 个 | **P = N₁ ? {'全部成立 ✓✓' if eq else '不成立 ✗'}**")
        print(f"   profile 取值数 = {len({x['prof'] for x in rs})}  ⟹ {'恒定 ✓（强制）' if len({x['prof'] for x in rs})==1 else '变化 ✗'}")
        print(f"   profile 样例: {rs[0]['prof']}")
        print(f"   Q 取值 = {sorted({x['Q'] for x in rs})} | rmin = {sorted({min(x['r']) for x in rs})} | rmax = {sorted({max(x['r']) for x in rs})}")
        print(f"   L(c)≥1 全部成立? {'是 ✓' if all(min(x['r'])>=1 for x in rs) else '否 ✗（有 rmin=0 者）'}")
        u=Counter(x['r'] for x in rs)
        print(f"   r 向量不同取值数 = {len(u)}; 最常见: {u.most_common(2)}")
        print()
N5,ball5,full5=build(5)
random.seed(7)
samp=list(dict.fromkeys(tuple(sorted(random.sample(range(32),8))) for _ in range(120000)))
rs=rows(5,8,samp,ball5,full5,N5)
print(f"n=5 M=8（采样）: 覆盖码 {len(rs)} 个")
print(f"   P = N₁ ? {'全部成立 ✓✓' if all(x['P']==x['N1'] for x in rs) else '不成立 ✗'}")
print(f"   profile 取值数 = {len({x['prof'] for x in rs})} ⟹ {'恒定' if len({x['prof'] for x in rs})==1 else '变化 ✗（自由度已释放）'}")
print(f"   profile 前5: {[p for p,_ in Counter(x['prof'] for x in rs).most_common(5)]}")
print(f"   rmin 取值 = {sorted({min(x['r']) for x in rs})};  rmax 取值 = {sorted({max(x['r']) for x in rs})}")
