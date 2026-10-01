#!/usr/bin/env python3
"""HN-C2: C(12,6,4) 精确求解（集合覆盖 ILP）
v=12,k=6,t=4. 块=全部 C(12,6)=924; 需覆盖全部 C(12,4)=495 个 4-子集.
① min Σx_B  → 精确最小块数
② 加 Σx_B ≤ 40 → 若不可行则证明 40 不可能（gap 闭合 = 41 最优）
## 仅用于回测研究，不包含实盘下单逻辑
"""
import itertools, numpy as np, sys, time
from scipy.sparse import csr_matrix
from scipy.optimize import milp, LinearConstraint, Bounds
V=12; K=6; T=4
blocks=[sum(1<<i for i in c) for c in itertools.combinations(range(V),K)]
subs  =[sum(1<<i for i in c) for c in itertools.combinations(range(V),T)]
bi={b:i for i,b in enumerate(blocks)}
print(f"块 {len(blocks)}  4-子集 {len(subs)}  理论下界 Schonheim={-(-len(subs)//15)}")
rows=[];cols=[]
for ti,t in enumerate(subs):
    for b,i in bi.items():
        if (b & t)==t: rows.append(ti); cols.append(i)
A=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(subs),len(blocks)))
print(f"非零 {len(rows)}  密度 {len(rows)/(len(subs)*len(blocks)):.4f}")
# ① 最小覆盖
t0=time.time()
res=milp(c=np.ones(len(blocks)), constraints=[LinearConstraint(A,1,np.inf)],
         integrality=np.ones(len(blocks)), bounds=Bounds(0,1),
         options={'time_limit':600,'mip_rel_gap':0.0,'disp':False})
print(f"[① min] status={res.status} {res.message[:40]} obj={res.fun} 用时 {time.time()-t0:.1f}s 对偶界={res.mip_dual_bound}")
sol=np.round(res.x).astype(int) if res.x is not None else None
if sol is not None:
    nb=sol.sum(); cov=A@sol
    print(f"[① 解] 块数={nb}  最小覆盖重数={cov.min()}  完备={cov.min()>=1}")
# ② 40 可行性
t0=time.time()
res2=milp(c=np.zeros(len(blocks)), constraints=[LinearConstraint(A,1,np.inf),
          LinearConstraint(np.ones((1,len(blocks))),-np.inf,40)],
          integrality=np.ones(len(blocks)), bounds=Bounds(0,1),
          options={'time_limit':600,'disp':False})
print(f"[② ≤40] status={res2.status} ({res2.message[:45]}) 用时 {time.time()-t0:.1f}s")
if res2.x is not None and res2.status==0:
    s2=np.round(res2.x).astype(int); print(f"[② 解] 块数={s2.sum()} 完备={(A@s2).min()>=1}")
