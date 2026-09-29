#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§5.4a 下界侧校准：用 HiGHS 判定 min = 62（即"61 词覆盖不存在"）

做法：minimize Σx，覆盖约束，设 objective_bound(cutoff)=61
      ⟹ 若最终 dual bound ≥ 62，则已证 61 不可能（与文献 K(9,1)=62 一致）
纪律：单线程；600s 上限；结果落盘
"""
import time, os, numpy as np
from scipy.sparse import csr_matrix
import highspy

N = 9
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "out")

rows, cols, vals = [], [], []
for t in range(Q):
    for v in NB[t]:
        rows.append(t)
        cols.append(v)
        vals.append(1.0)
A = csr_matrix((np.array(vals), (np.array(rows), np.array(cols))), shape=(Q, Q))

lp = highspy.HighsLp()
lp.num_col_ = Q
lp.num_row_ = Q
lp.col_cost_ = np.ones(Q)
lp.col_lower_ = np.zeros(Q)
lp.col_upper_ = np.ones(Q)
lp.row_lower_ = np.ones(Q)
lp.row_upper_ = np.full(Q, highspy.kHighsInf)
Ac = A.tocsr()
lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
lp.a_matrix_.start_ = Ac.indptr.astype(np.int32)
lp.a_matrix_.index_ = Ac.indices.astype(np.int32)
lp.a_matrix_.value_ = Ac.data
lp.a_matrix_.num_col_ = Q
lp.a_matrix_.num_row_ = Q
lp.integrality_ = np.full(Q, highspy.HighsVarType.kInteger)   # ★ 必须：否则只是 LP 松弛

h = highspy.Highs()
h.setOptionValue("output_flag", True)
h.setOptionValue("time_limit", 600.0)
h.setOptionValue("mip_rel_gap", 0.0)
h.setOptionValue("threads", 1)
h.setOptionValue("presolve", "on")
h.setOptionValue("mip_abs_gap", 0.0)
h.passModel(lp)

t0 = time.time()
h.run()
dt = time.time() - t0

info = h.getInfo()
print("=" * 70)
print(f"status={h.modelStatusToString(h.getModelStatus())}  用时 {dt:.1f}s")
print(f"objective={info.objective_function_value}  dual_bound={info.mip_dual_bound}  "
      f"gap={info.mip_gap}  nodes={info.mip_node_count}  lp_bound=51.2（已验证）")
if info.mip_dual_bound is not None and info.mip_dual_bound >= 61.999:
    print("★ 已证：不存在 ≤61 词覆盖 ⟹ K(9,1) ≥ 62 ✓（与文献一致）")
if info.objective_function_value is not None and info.objective_function_value <= 61.999:
    print("⚠️ 找到 ≤61 解 ⟹ 与文献冲突，须复核（异常优先怀疑己方）")
sol = h.getSolution()
C = [v for v in range(Q) if sol.col_value[v] > 0.5]
print(f"当前最好解 |C|={len(C)}")
if 0 < len(C) <= 70:
    cnt = [0] * Q
    for v in C:
        for x in NB[v]:
            cnt[x] += 1
    unc = sum(1 for c in cnt if c == 0)
    print(f"   核验：覆盖={Q-unc}/512 未覆盖={unc}")
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "n9_highs_incumbent.txt")
    with open(p, "w") as f:
        f.write(f"# HiGHS incumbent |C|={len(C)} dual_bound={info.mip_dual_bound}\n")
        for v in sorted(C):
            f.write(" ".join(str((v >> i) & 1) for i in range(N)) + "\n")
    print(f"   已写 {os.path.relpath(p)}")
