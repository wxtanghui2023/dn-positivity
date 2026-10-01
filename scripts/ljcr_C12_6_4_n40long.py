#!/usr/bin/env python3
"""HN-C2: C(12,6,4) 精确判定（CP-SAT 可行性）
① n=40 可行性: 若有解 ⟹ 上界 41→40（记录改进）
② 若 40 不可行 ⟹ C(12,6,4)=41 精确（gap 闭合）
## 仅用于回测研究，不包含实盘下单逻辑
"""
import itertools, time
from ortools.sat.python import cp_model
V,K,T=12,6,4
blocks=[tuple(c) for c in itertools.combinations(range(V),K)]
subs=[frozenset(c) for c in itertools.combinations(range(V),T)]
bsets=[frozenset(b) for b in blocks]
occ={}   # t-subset -> list of block indices
for i,b in enumerate(bsets):
    for s in itertools.combinations(sorted(b),T):
        occ.setdefault(frozenset(s),[]).append(i)
print(f"块 {len(blocks)}  4-子集 {len(subs)}  Schonheim 下界 {-(-len(subs)//15)}")
def solve(n,tl):
    m=cp_model.CpModel()
    x=[m.NewBoolVar(f"x{i}") for i in range(len(blocks))]
    for s in subs:
        m.Add(sum(x[i] for i in occ[s])>=1)
    m.Add(sum(x)<=n)
    sol=cp_model.CpSolver(); sol.parameters.max_time_in_seconds=tl; sol.parameters.num_search_workers=4
    st=sol.Solve(m); t=time.time()
    name={cp_model.OPTIMAL:'OPTIMAL',cp_model.FEASIBLE:'FEASIBLE',cp_model.INFEASIBLE:'INFEASIBLE',cp_model.UNKNOWN:'UNKNOWN'}[st]
    print(f"[n≤{n}] {name}  用时 {sol.WallTime():.1f}s  冲突 {sol.NumConflicts()}  分支 {sol.NumBranches()}")
    if st in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        sel=[i for i in range(len(blocks)) if sol.Value(x[i])>0.5]
        cov=set()
        for i in sel: cov |= {s for s in occ if i in occ[s]}
        print(f"        选中块数 {len(sel)}  覆盖 {len(cov)}/{len(subs)}  完备 {len(cov)==len(subs)}")
        print("        BLOCKS:", [blocks[i] for i in sel])
        return True
    return False
pass
solve(40,1800)
