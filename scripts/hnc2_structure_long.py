#!/usr/bin/env python3
"""HN-C2 L4 决定性判定：用已证等号结构（正则性 + 6 特对 lambda=10/9）压缩搜索
WLOG 取特对为 (1,2),(3,4),...,(11,12)（Aut(S_12) 在完美匹配上传递）
INFEASIBLE => 40 不存在 => C(12,6,4)=41 ;  FEASIBLE => 40 块设计存在
"""
import itertools, time
from ortools.sat.python import cp_model
V,K,T=12,6,4
blocks=[sum(1<<i for i in c) for c in itertools.combinations(range(V),K)]
subs=[sum(1<<i for i in c) for c in itertools.combinations(range(V),T)]
occ={s:[i for i,b in enumerate(blocks) if (b&s)==s] for s in subs}
pairs=[(1<<i)|(1<<j) for i,j in itertools.combinations(range(V),2)]
pocc={p:[i for i,b in enumerate(blocks) if (b&p)==p] for p in pairs}
pairspec={(1<<i)|(1<<(i+1)) for i in range(0,V,2)}   # 6 特对
print(f"块 {len(blocks)}｜4-子集 {len(subs)}｜点对 {len(pairs)}（特对 {len(pairspec)}）")
m=cp_model.CpModel(); x=[m.NewBoolVar(f"x{i}") for i in range(len(blocks))]
for s in subs: m.Add(sum(x[i] for i in occ[s])>=1)
m.Add(sum(x)==40)
for v in range(V):
    m.Add(sum(x[i] for i,b in enumerate(blocks) if (b>>v)&1)==20)
for p in pairs:
    m.Add(sum(x[i] for i in pocc[p])==(10 if p in pairspec else 9))
t0=time.time()
solver=cp_model.CpSolver(); solver.parameters.max_time_in_seconds=3600; solver.parameters.num_search_workers=8
st=solver.Solve(m)
name={cp_model.OPTIMAL:'OPTIMAL',cp_model.FEASIBLE:'FEASIBLE',cp_model.INFEASIBLE:'INFEASIBLE',cp_model.UNKNOWN:'UNKNOWN'}[st]
print(f"[判定] status={name} 用时 {solver.WallTime():.1f}s 冲突 {solver.NumConflicts()} 分支 {solver.NumBranches()}")
if st in (cp_model.OPTIMAL,cp_model.FEASIBLE):
    sel=[i for i in range(len(blocks)) if solver.Value(x[i])>0.5]
    cov=sum(1 for s in subs if any((blocks[i]&s)==s for i in sel))
    print(f"        块数 {len(sel)} 覆盖 {cov}/{len(subs)} 完备 {cov==len(subs)}")
    print("        BLOCKS:", [tuple(i+1 for i in range(V) if (blocks[j]>>i)&1) for j in sel])
elif st==cp_model.INFEASIBLE:
    print("        ⟹ 40 块设计不存在 ⟹ C(12,6,4)=41（gap 闭合 ✓✓）")
else:
    print("        ⟹ UNKNOWN（不作不存在证据；须加时限或换法）")
