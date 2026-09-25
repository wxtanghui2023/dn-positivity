#!/usr/bin/env python3
"""核心禁形检验（真实码 C_120）：
   d(x,q)=3 的所有码字对，检查三个一级中间点 x^(1<<r) 是否可能成为 x 的私有点。
   若恒不可能 ⟹ 分离引理核心情形由码结构排除。
"""
import sys, itertools
from collections import Counter
sys.argv=['x','5','none']
exec(open('exact_pack.py').read().split('def main()')[0])
d=lambda a,b:(a^b).bit_count()
owners={}
for i,w in enumerate(WORDS):
    for v in [w]+[w^(1<<j) for j in range(10)]:
        owners.setdefault(v,set()).add(i)

pairs=0; priv_hit=0; hits=[]
size_hist=Counter()
for xi in range(120):
    x=WORDS[xi]
    for qi in range(120):
        if qi==xi: continue
        q=WORDS[qi]
        if d(x,q)!=3: continue
        pairs+=1
        S=[r for r in range(10) if ((x^q)>>r)&1]
        for r in S:
            p=x^(1<<r)
            ow=owners.get(p,set())
            size_hist[len(ow)]+=1
            if ow=={xi}:
                priv_hit+=1
                if len(hits)<8: hits.append((xi,qi,x,q,r,sorted(ow)))
print(f"d(x,q)=3 的码字对数 = {pairs}（每对 3 个中间点，共 {3*pairs} 个）")
print(f"中间点的 owner 集大小分布 = {dict(sorted(size_hist.items()))}")
print(f"★ 中间点成为 x 的私有点（owner={x}）的次数 = {priv_hit}  （0 即核心禁形成立）")
for h in hits: print("   ", h)
print()
# 对照：d(x,q)=2 的情形（理论已排除）
p2=0; hit2=0
for xi in range(120):
    x=WORDS[xi]
    for qi in range(120):
        if qi==xi: continue
        q=WORDS[qi]
        if d(x,q)!=2: continue
        for r in [t for t in range(10) if ((x^q)>>t)&1]:
            p=x^(1<<r)
            if owners.get(p,set())=={xi}: hit2+=1
        p2+=1
print(f"对照 d(x,q)=2: 码字对 {p2}，其中某中间点为 x 私有点的次数 = {hit2}")
