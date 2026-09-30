#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""(乙′-1)+(乙′-2): 双核 9x9 联合 profile + 二维循环相关
   H = K ⊕ L; X[i][j] = f(i·k+j·ℓ) ∈ {0,1,2,3}
   行和=列和=给定 Z_9 profile 多重集; Q_{a,b}(X)=180 ∀(a,b)≠(0,0)
"""
import sys, time
import numpy as np
from ortools.sat.python import cp_model

prof = [18, 15, 15, 15, 13, 12, 12, 12, 9]
print("profile =", prof, "Σ =", sum(prof), "Σ² =", sum(x*x for x in prof), flush=True)

m = cp_model.CpModel()
X = [[m.NewIntVar(0, 3, f"x{i}_{j}") for j in range(9)] for i in range(9)]
for i in range(9):
    m.Add(sum(X[i]) == prof[i])
for j in range(9):
    m.Add(sum(X[i][j] for i in range(9)) == prof[j])

# Q_{a,b} = Σ_{ij} X[i][j] X[i-a][j-b]
nQ = 0
for a in range(9):
    for b in range(9):
        if a == 0 and b == 0:
            continue
        terms = []
        for i in range(9):
            for j in range(9):
                p = m.NewIntVar(0, 9, f"p{a}_{b}_{i}_{j}")
                m.AddMultiplicationEquality(p, [X[i][j], X[(i-a) % 9][(j-b) % 9]])
                terms.append(p)
        m.Add(sum(terms) == 180)
        nQ += 1
print(f"相关约束数 = {nQ}", flush=True)

solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 150.0
solver.parameters.num_search_workers = 4
st = solver.Solve(m)
print(f"状态 = {solver.StatusName(st)}; 墙钟 = {solver.WallTime():.1f}s; 冲突 = {solver.NumConflicts()}; 分支 = {solver.NumBranches()}", flush=True)
if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    M = np.array([[solver.Value(X[i][j]) for j in range(9)] for i in range(9)])
    print("**找到 X** ✓", flush=True)
    print(M, flush=True)
    ok = True
    for a in range(9):
        for b in range(9):
            if a == 0 and b == 0:
                continue
            q = int(sum(M[i][j]*M[(i-a) % 9][(j-b) % 9] for i in range(9) for j in range(9)))
            if q != 180:
                ok = False
                print(f"  ✗ (a,b)=({a},{b}): Q={q}", flush=True)
                break
        if not ok:
            break
    print(f"独立核验 Q=180 ∀(a,b)≠0: {ok}", flush=True)
    print(f"Q_(0,0) = ΣX² = {int((M*M).sum())}", flush=True)
else:
    print(f"⟹ 未决（{solver.StatusName(st)}）—— ⚠️ 不作不存在证据", flush=True)
