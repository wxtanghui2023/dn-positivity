#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""同组 (K∩L=3) 双核联合判定: X ∈ {0,1,2,3}^{9x9}
   周期: X[i+3][j-3] = X[i][j]  (核 = <(3,-3)>, 3 重覆盖 ⟹ 有效 27 值)
   margins: 行/列和 = Z_9 profile 多重集
   相关: Q_{a,b} = Σ X[i][j]X[i-a][j-b] = 180 (或 241 当 a·k+b·ℓ=0)
"""
import sys
import numpy as np
from ortools.sat.python import cp_model

N = 9
prof = [18, 15, 15, 15, 13, 12, 12, 12, 9]
print("profile =", prof, flush=True)

m = cp_model.CpModel()
X = [[m.NewIntVar(0, 3, f"x{i}_{j}") for j in range(N)] for i in range(N)]
# 周期性: (3,-3) 生成核
for i in range(N):
    for j in range(N):
        m.Add(X[i][j] == X[(i + 3) % N][(j - 3) % N])
# margins
for i in range(N):
    m.Add(sum(X[i]) == prof[i])
for j in range(N):
    m.Add(sum(X[i][j] for i in range(N)) == prof[j])

# 相关: 对所有 (a,b); 但 X 有周期 ⟹ 同一 z=a·k+b·ℓ 的多个 (a,b) 给同值
# 这里直接对全部 80 个非零 (a,b) 加 Q=180, 对 (0,0) 加 Q=241
nQ = 0
for a in range(N):
    for b in range(N):
        terms = []
        for i in range(N):
            for j in range(N):
                p = m.NewIntVar(0, 9, f"p{a}_{b}_{i}_{j}")
                m.AddMultiplicationEquality(p, [X[i][j], X[(i - a) % N][(j - b) % N]])
                terms.append(p)
        m.Add(sum(terms) == (241 if (a == 0 and b == 0) else 180))
        nQ += 1
print(f"约束数 = {nQ}", flush=True)

solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 200.0
solver.parameters.num_search_workers = 4
st = solver.Solve(m)
print(f"状态 = {solver.StatusName(st)}; 墙钟 = {solver.WallTime():.1f}s; 冲突 = {solver.NumConflicts()}; 分支 = {solver.NumBranches()}", flush=True)
if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    M = np.array([[solver.Value(X[i][j]) for j in range(N)] for i in range(N)])
    print("**找到 X** ✓", flush=True)
    print(M, flush=True)
    ok = all(int(sum(M[i][j]*M[(i-a) % N][(j-b) % N] for i in range(N) for j in range(N))) == (241 if (a, b) == (0, 0) else 180)
             for a in range(N) for b in range(N))
    print(f"独立核验: {ok}", flush=True)
else:
    print(f"⟹ 未决（{solver.StatusName(st)}）—— ⚠️ 不作不存在证据", flush=True)
