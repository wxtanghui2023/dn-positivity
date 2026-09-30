#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""f-层精确可行性: f ∈ {0,1,2,3}^{Z_9^2}, Σf = 121, (f⋆f)(z) = 180 (z≠0)
   等价: |f̂(χ)|² = 61 (χ≠1) —— 由 (a)+(b) 推出之必要条件
   模型: CP-SAT, 81 整数变量 + 80 个乘积和约束
"""
import sys, time
from ortools.sat.python import cp_model

N = 9
idx = {}
pts = []
for a in range(N):
    for b in range(N):
        idx[(a, b)] = len(pts)
        pts.append((a, b))
n = len(pts)
print(f"n = {n}", flush=True)

m = cp_model.CpModel()
f = [m.NewIntVar(0, 3, f"f{i}") for i in range(n)]
m.Add(sum(f) == 121)

# 级计数约束 (矩族): N_j = #{f = j}
lev = [[m.NewBoolVar(f"y{i}_{j}") for j in range(4)] for i in range(n)]
for i in range(n):
    m.Add(sum(lev[i][j] for j in range(4)) == 1)
    for j in range(4):
        m.Add(f[i] == j).OnlyEnforceIf(lev[i][j])
        m.Add(f[i] != j).OnlyEnforceIf(lev[i][j].Not())
# t := N3 ∈ [0,19] (t=20 已被 19/4 论证排除)
t = m.NewIntVar(0, 19, "t")
m.Add(sum(lev[i][3] for i in range(n)) == t)
m.Add(sum(lev[i][2] for i in range(n)) == 60 - 3 * t)
m.Add(sum(lev[i][1] for i in range(n)) == 1 + 3 * t)
m.Add(sum(lev[i][0] for i in range(n)) == 20 - t)

# 自相关约束 (80 个)
t0 = time.time()
prod_count = 0
for z in pts:
    if z == (0, 0):
        continue
    terms = []
    for x in pts:
        y = ((x[0] - z[0]) % N, (x[1] - z[1]) % N)
        p = m.NewIntVar(0, 9, f"p{idx[x]}_{idx[z]}")
        m.AddMultiplicationEquality(p, [f[idx[x]], f[idx[y]]])
        terms.append(p)
        prod_count += 1
    m.Add(sum(terms) == 180)
print(f"乘积变量 = {prod_count}, 建模耗时 {time.time()-t0:.1f}s", flush=True)

solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = float(sys.argv[1]) if len(sys.argv) > 1 else 280.0
solver.parameters.num_search_workers = 4
solver.parameters.log_search_progress = False
print("求解中...", flush=True)
st = solver.Solve(m)
print(f"状态 = {solver.StatusName(st)}", flush=True)
print(f"墙钟 = {solver.WallTime():.1f}s;  冲突 = {solver.NumConflicts()};  分支 = {solver.NumBranches()}", flush=True)
if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    F = [solver.Value(f[i]) for i in range(n)]
    print("**找到可行 f** ✓", flush=True)
    print("t =", solver.Value(t), flush=True)
    # 独立核验
    ok = True
    for z in pts:
        if z == (0, 0):
            continue
        s = sum(F[idx[x]] * F[((x[0]-z[0]) % N, (x[1]-z[1]) % N)] for x in pts)
        if s != 180:
            ok = False
            print(f"  ✗ z={z}: (f⋆f)={s} ≠ 180", flush=True)
            break
    print(f"独立核验 (f⋆f)(z)=180 ∀z≠0: {ok}", flush=True)
    print(f"Σf = {sum(F)}; Σf² = {sum(v*v for v in F)}", flush=True)
    import collections
    print("级计数:", dict(collections.Counter(F)), flush=True)
    print("F =", F, flush=True)
else:
    print(f"⟹ 未决（{solver.StatusName(st)}）—— ⚠️ 不作不存在证据", flush=True)
