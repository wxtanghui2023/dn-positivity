#!/usr/bin/env python3
"""n=8 决定性判定：∃ (8,32)_1 covering code 且 b(0) >= 3 ?
   SAT   ⟹ 显式 Q>0 反例 ⟹ n=8 pinning 被击穿 ✗
   UNSAT ⟹ 不存在含三重覆盖点的 (8,32)_1 ⟹ b(x)<=2 ∀x ⟹ Q*(8)=0 ✓（定理级 ✓）
"""
import time, sys
from ortools.sat.python import cp_model
n, N, M = 8, 256, 32
def ball(x): return [x] + [x ^ (1 << i) for i in range(n)]
m = cp_model.CpModel()                      # 单次建模（不重建 ✓）
y = [m.NewBoolVar(f"y{c}") for c in range(N)]
m.Add(sum(y) == M)                          # 恰好 32 个
for x in range(N):                          # 256 条覆盖
    m.Add(sum(y[c] for c in ball(x)) >= 1)
m.Add(sum(y[c] for c in ball(0)) >= 3)      # 指定点三重覆盖
S = cp_model.CpSolver()
S.parameters.max_time_in_seconds = 900
S.parameters.num_workers = 1                # 单线程纪律 ✓
S.parameters.log_search_progress = False
print("模型: vars=%d constraints(约)=%d  —— 开始求解…" % (N, N + 2), flush=True)
t0 = time.time()
st = S.Solve(m)
dt = time.time() - t0
name = S.StatusName(st)
print(f"\n=== 求解完成: status={name}  用时={dt:.1f}s ===", flush=True)
print(f"  conflicts={S.NumConflicts()} branches={S.NumBranches()} wall={S.WallTime():.1f}s", flush=True)
if st == cp_model.OPTIMAL or st == cp_model.FEASIBLE:
    C = [c for c in range(N) if S.Value(y[c])]
    E = M * (n + 1) - N
    b = [sum(1 for c in C if (x ^ c).bit_count() <= 1) for x in range(N)]
    from itertools import combinations
    from collections import Counter
    A1 = sum(1 for a, b2 in combinations(C, 2) if (a ^ b2).bit_count() == 1)
    A2 = sum(1 for a, b2 in combinations(C, 2) if (a ^ b2).bit_count() == 2)
    Q = sum((bb - 1) * (bb - 2) // 2 for bb in b)
    print(f"  |C|={len(C)}  min b={min(b)}  max b={max(b)}  b分布={dict(sorted(Counter(b).items()))}")
    print(f"  A1={A1} A2={A2} A1+A2={A1+A2}  E={E}  **Q={Q}**  核验 2(A1+A2)-E={2*(A1+A2)-E}")
    open('/home/node/.openclaw/workspace/dn-project/work/k10/q10proto/n8_witness_Q_pos.txt','w').write(
        "n=8 M=32 b(0)>=3 witness\n" + " ".join(format(c, '08b') for c in C) + f"\nQ={Q} A1={A1} A2={A2} E={E} bprof={dict(sorted(Counter(b).items()))}\n")
    print("  ⟹ ⛔ **SAT：存在 Q>0 的 (8,32)_1 码 ⟹ n=8 pinning 被击穿** ✗", flush=True)
    print("  witness 已存 work/k10/q10proto/n8_witness_Q_pos.txt ✓", flush=True)
elif st == cp_model.INFEASIBLE:
    print("  ⟹ ✅ **UNSAT：不存在含三重覆盖点的 (8,32)_1 码**", flush=True)
    print("  ⟹ b(x) ≤ 2 ∀x ⟹ **Q*(8) = 0（定理级 ✓）**", flush=True)
    open('/home/node/.openclaw/workspace/dn-project/work/k10/q10proto/n8_UNSAT_log.txt','w').write(
        f"INFEASIBLE proof: model n=8 N=256 M=32 cover>=1 all x, and b(0)>=3\n"
        f"status={name} time={dt:.1f}s conflicts={S.NumConflicts()} branches={S.NumBranches()} wall={S.WallTime():.1f}s\n"
        f"model: 256 bool, sum=32, 256 cover constraints, 1 triple constraint (ball(0) size 9)\n")
    print("  UNSAT 日志已存 work/k10/q10proto/n8_UNSAT_log.txt ✓", flush=True)
else:
    print(f"  ⚠️ 未决（{name}）—— 不得当作结论 ✗；建议提高时限或换编码重跑 ✓", flush=True)
