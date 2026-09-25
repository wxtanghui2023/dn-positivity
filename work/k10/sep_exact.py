#!/usr/bin/env python3
"""精确分离性：紧型下，(q∈Q, 簇锚点 x_i)（i≠q 所属簇）的距离谱；并与"目标字 x_t"对比。"""
import random, sys, itertools
from collections import Counter
sys.argv=['x','5','none']
exec(open('exact_pack.py').read().split('def main()')[0])
d=lambda a,b:(a^b).bit_count()
random.seed(31337)
spec_cluster=Counter(); spec_target=Counter(); bad=[]
inst=0
for _ in range(300):
    D=tuple(sorted(random.sample(range(120),4)))
    Xw=[WORDS[i] for i in D]; U=U_of(D)
    if U==0: continue
    pts=[v for v in range(1024) if (U>>v)&1]
    Cs=[[q for q in pts if d(q,x)<=1] for x in Xw]
    for t in range(4):
        x=Xw[t]; other=[i for i in range(4) if i!=t]
        for Q in itertools.product(*[Cs[i] for i in other]):
            if min(d(Q[a],Q[b]) for a,b in itertools.combinations(range(3),2))<3: continue
            rs=tuple(sorted(d(q,x) for q in Q))
            if rs not in ((2,3,3),(3,3,3)): continue
            B1x=[x]+[x^(1<<j) for j in range(10)]
            F=[v for v in B1x if all(d(v,q)>=3 for q in Q)]
            if len(F)!=2 or not [v for v in F if v not in pts]: continue
            inst+=1
            for k,ci in enumerate(other):
                xi=Xw[ci]
                for j in range(3):
                    q=Q[j]
                    if other[j]==ci: continue          # 跳过本簇自己的点
                    dd=d(q,xi)
                    spec_cluster[dd]+=1
                    if dd<=3 and len(bad)<6: bad.append((list(D),t,ci,q,xi,dd))
            for q in Q: spec_target[d(q,x)]+=1
print(f"紧型实例 {inst}")
print(f"(q, 簇锚点 x_i) 距离谱 = {dict(sorted(spec_cluster.items()))}   ⟹ 最小 = {min(spec_cluster) if spec_cluster else '-'}")
print(f"(q, 目标字 x_t) 距离谱 = {dict(sorted(spec_target.items()))}")
print(f"簇锚点对中距离 ≤3 的违例数 = {len(bad)}")
for b in bad: print("   ",b)
