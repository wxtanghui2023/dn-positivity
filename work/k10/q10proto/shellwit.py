#!/usr/bin/env python3
"""核验"非private shell incidence => S 或 I 见证"引理
 case(a) y∈C        => v 有方阵外码字邻居 => d_C(v)>=3
 case(b) y∉C, b>=2  => ∃c' 使 d(v,c')=2（d=1 不可能）=> (y,{v,c'}) 计入 S
"""
import itertools, sys
from collections import Counter
def setup(n):
    N=1<<n; BM=[1<<x for x in range(N)]
    for x in range(N):
        for i in range(n): BM[x]|=1<<(x^(1<<i))
    return N,BM
def run(n,C,tag):
    N,BM=setup(n); Cs=set(C)
    b={x:sum(1 for c in C if (BM[c]>>x)&1) for x in range(N)}
    sqs={}
    for u in sorted(Cs):
        for i,j in itertools.combinations(range(n),2):
            a=u^(1<<i); c2=u^(1<<j); ac=u^(1<<i)^(1<<j)
            if a in Cs and c2 in Cs and ac in Cs:
                sqs[frozenset([u,a,c2,ac])]=(u,i,j)
    stat=Counter(); violA=0; violB=0; nC=0; nM=0
    witS=set(); witI=set()
    for verts,(u,i,j) in sqs.items():
        dirs={i,j}
        for v in verts:
            # v 的 shell: v 的两个方阵方向
            # 确定 v 相对 u 的偏移
            off=[k for k in dirs if (v>>k)&1]
            for k in range(n):
                if k in dirs: continue
                y=v^(1<<k)
                if y in Cs:
                    stat['C']+=1; nC+=1
                    dC=b[v]-1
                    if dC<3: violA+=1
                    else: witI.add((v,y))
                elif b[y]==1:
                    stat['P']+=1
                else:
                    stat['M']+=1; nM+=1
                    cov=[c for c in C if (BM[c]>>y)&1 and c!=v]
                    ok=any(bin(c^v).count('1')==2 for c in cov)
                    if not ok: violB+=1
                    else:
                        for c in cov:
                            if bin(c^v).count('1')==2: witS.add((y,frozenset([v,c]))); break
    print(f"[{tag}] 方阵{len(sqs)} 三态={dict(stat)} | (a)违反={violA} (b)违反={violB} | S见证={len(witS)} I见证={len(witI)}")
    return len(witS),len(witI),nC+nM
for n,M,t in ((4,6,"(4,6)>K"),(5,8,"(5,8)>K")):
    for C in itertools.combinations(range(1<<n),M):
        N,BM=setup(n); fullm=(1<<N)-1; cov=0
        for c in C: cov|=BM[c]
        if cov==fullm:
            run(n,list(C),t); break
def syn(x):
    a=0
    for i in range(7):
        if (x>>i)&1: a^=(i+1)
    return a
H7=[x for x in range(128) if syn(x)==0]
C9=[((((h<<1)|bb)<<1)|cc) for h in H7 for bb in (0,1) for cc in (0,1)]
run(9,C9,"(9,64) 我方")
print()
print("=== 引理 ===")
print(" (a) y∈C ⟹ v 有方阵外码字邻居 ⟹ d_C(v) ≥ 3 ✓")
print(" (b) y∉C 非private ⟹ 存在 c' 覆盖 y, c'≠v ⟹ d(c',v) ≤ 2; 且 **d=1 不可能**")
print("     证: d=1 ⟹ y ∈ N[v]∩N[c'] = {v,c'} ⟹ y=v ✗ 或 y=c' ✗(y∉C)")
print("     ⟹ d(c',v)=2 ⟹ (y,{v,c'}) 是非码字中点 incidence ⟹ **计入 S** ✓✓")
