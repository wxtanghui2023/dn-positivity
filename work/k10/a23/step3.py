#!/usr/bin/env python3
"""A23-D4 Step 3 (修正门 2): 对正确量 |S(D)|=Σ_{B⊆D} g(B) 求 max
   候选 D：① 精确 4-组；② 3-组∪{x}；③ 两个非单组之并(≤4)"""
import pickle, itertools, time, sys
from collections import Counter, defaultdict
t0=time.time()
small=pickle.load(open('/tmp/a23_small.pkl','rb'))   # s -> tuple(blocker idx)
import re
W=[]
for ln in open('a23.6.10.2969H.txt'):
    s=ln.strip()
    if re.fullmatch(r'[0-9A-Fa-f]{5,8}',s): W.append(int(s,16))
W=sorted(set(W))
print(f"C0={len(W)} ✓ 小-blocker 候选={len(small)} ✓",flush=True)
g=Counter(v for v in small.values())          # 精确组计数
print("组大小分布:", dict(sorted(Counter(g.values()).items())), flush=True)
gs={k:0 for k in range(1,5)}
for B in g: gs[len(B)]+=1
print("组数按 |B|:", gs, " |E|(出现的 blocker 数)=", len({c for B in g for c in B}), flush=True)
by=defaultdict(set)   # 元素集(排序元组) -> g 值(已在 g 里)
# 快速查询: 给定排序元组, 取 g
def G(t): return g.get(t,0)
best=(0,None)
# ① 精确 4-组
for B,v in g.items():
    if len(B)==4:
        tot=sum(G(B[:i]+B[i+1:j]+B[j+1:]) for i in range(4) for j in range(i+1,4))
        tot+=sum(G((B[i],)) for i in range(4))+sum(G((B[i],B[j])) for i in range(4) for j in range(i+1,4))
        tot+=v
        if tot>best[0]: best=(tot,B)
print(f"① 精确 4-组: max|S(D)|={best[0]}  用时 {time.time()-t0:.0f}s", flush=True)
# ② 3-组 ∪ {x}
b2=(best[0],best[1])
G1={k[0]:v for k,v in g.items() if len(k)==1}
G2={k:v for k,v in g.items() if len(k)==2}
G3=[k for k in g if len(k)==3]
G4={k:v for k,v in g.items() if len(k)==4}
cnt=0
for B in G3:
    vB=g[B]
    pB=sum(G2.get((B[i],B[j]),0) for i in range(3) for j in range(i+1,3))
    sB=sum(G1.get(B[i],0) for i in range(3))
    for x in range(len(W)):
        if x in B: continue
        D=tuple(sorted(B+(x,)))
        tot=vB+pB+sB+G1.get(x,0)+sum(G2.get(tuple(sorted((x,B[i]))),0) for i in range(3))
        tot+=G4.get(D,0)+sum(g.get(tuple(sorted((x,B[i],B[j]))),0) for i in range(3) for j in range(i+1,3))
        if tot>best[0]: best=(tot,D)
        cnt+=1
print(f"② 3-组∪{{x}}: 检验 {cnt} 个 D, max|S(D)|={best[0]} at {best[1]}  用时 {time.time()-t0:.0f}s", flush=True)
# ③ 两非单组之并(≤4)
G2l=list(G2.keys()); G3l=list(G3)
n2=0
for A in G2l:
    for B in G2l:
        U=tuple(sorted(set(A)|set(B)))
        if len(U)>4: continue
        tot=sum(G(t) for t in [U]+[tuple(c) for c in itertools.combinations(U,3)]+[tuple(c) for c in itertools.combinations(U,2)]+[(c,) for c in U])
        n2+=1
        if tot>best[0]: best=(tot,U)
print(f"③ 2-组×2-组: {n2} 对, max|S(D)|={best[0]}  用时 {time.time()-t0:.0f}s", flush=True)
n3=0
for A in G2l:
    for B in G3l:
        U=tuple(sorted(set(A)|set(B)))
        if len(U)>4: continue
        n3+=1
        tot=sum(G(t) for t in [U]+[tuple(c) for c in itertools.combinations(U,3)]+[tuple(c) for c in itertools.combinations(U,2)]+[(c,) for c in U])
        if tot>best[0]: best=(tot,U)
print(f"③ 2-组×3-组: {n3} 对, max|S(D)|={best[0]}  用时 {time.time()-t0:.0f}s", flush=True)
print(f"\n=== 门 2（修正后）=== max |S(D)| = {best[0]}  at D={best[1]}", flush=True)
print(f"⟹ 若 max < 5 ⟹ 深度≤4 无正收益交换 ⟹ depth-4 局部最优性定理 ✓✓", flush=True)
