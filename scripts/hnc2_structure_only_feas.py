#!/usr/bin/env python3
"""只测等号结构的线性可行性（无覆盖约束）：
sum x = 40 ; 每点度 = 20 ; lambda(x,y) = 10(特对内)/9(特对间)
不可行 ⟹ 40 块设计不存在 ⟹ C(12,6,4)=41
"""
import itertools, time
from ortools.sat.python import cp_model
V,M=12,40
blocks=[sum(1<<i for i in c) for c in itertools.combinations(range(V),6)]
pairs=[(1<<i)|(1<<j) for i,j in itertools.combinations(range(V),2)]
pocc={p:[k for k,b in enumerate(blocks) if (b&p)==p] for p in pairs}
m=cp_model.CpModel(); x=[m.NewBoolVar(f"x{i}") for i in range(len(blocks))]
m.Add(sum(x)==M)
for v in range(V):
    m.Add(sum(x[k] for k,b in enumerate(blocks) if (b>>v)&1)==20)
for i,j in itertools.combinations(range(V),2):
    p=(1<<i)|(1<<j); tgt=10 if i//2==j//2 else 9
    m.Add(sum(x[k] for k in pocc[p])==tgt)
t0=time.time(); s=cp_model.CpSolver(); s.parameters.max_time_in_seconds=300; s.parameters.num_search_workers=4
st=s.Solve(m)
name={cp_model.OPTIMAL:'OPTIMAL',cp_model.FEASIBLE:'FEASIBLE',cp_model.INFEASIBLE:'INFEASIBLE',cp_model.UNKNOWN:'UNKNOWN'}[st]
print(f"[仅结构] status={name} 用时 {s.WallTime():.1f}s 冲突 {s.NumConflicts()} 分支 {s.NumBranches()}")
if st in (cp_model.OPTIMAL,cp_model.FEASIBLE):
    sel=[k for k in range(len(blocks)) if s.Value(x[k])>0.5]
    print(f"        块数 {len(sel)}（结构可行 ⟹ 可用作 S2 起点）")
    print("        BLOCKS:", [tuple(i+1 for i in range(V) if (blocks[k]>>i)&1) for k in sel])
elif st==cp_model.INFEASIBLE:
    print("        ⟹ 等号结构本身不可行 ⟹ 40 不存在 ⟹ C(12,6,4)=41 ✓✓")
