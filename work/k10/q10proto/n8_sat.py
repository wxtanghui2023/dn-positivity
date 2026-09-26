#!/usr/bin/env python3
"""n=8 决策（纯 CNF/SAT 路线）：∃ 32 字覆盖 Q8 且 b(0)>=3 ?
   vars y_c (256) + CardEnc.equals(=32) + 256 覆盖子句(>=1) + atleast(ball(0))>=3"""
import time
from pysat.card import CardEnc, EncType
from pysat.solvers import Glucose4
n, N, M = 8, 256, 32
def ball(x): return [x] + [x ^ (1 << i) for i in range(n)]
y = {c: c + 1 for c in range(N)}          # DIMACS 变量 1..256
cnf = []
cnf += CardEnc.equals(lits=list(y.values()), bound=M, top_id=N, encoding=EncType.seqcounter).clauses
for x in range(N):
    cnf.append([y[c] for c in ball(x)])   # >=1
cnf += CardEnc.atleast(lits=[y[c] for c in ball(0)], bound=3, top_id=N, encoding=EncType.seqcounter).clauses
print(f"CNF: vars={N} clauses={len(cnf)}  —— 开始求解…", flush=True)
t0 = time.time()
with Glucose4(bootstrap_with=cnf) as s:
    sat = s.solve()
    dt = time.time() - t0
    print(f"\n=== status = {'SAT' if sat else 'UNSAT'}  用时={dt:.1f}s ===", flush=True)
    if sat:
        C = [c for c in range(N) if s.get_model()[c] > 0]
        from itertools import combinations
        from collections import Counter
        E = M * (n + 1) - N
        b = [sum(1 for c in C if (x ^ c).bit_count() <= 1) for x in range(N)]
        A1 = sum(1 for a, b2 in combinations(C, 2) if (a ^ b2).bit_count() == 1)
        A2 = sum(1 for a, b2 in combinations(C, 2) if (a ^ b2).bit_count() == 2)
        Q = sum((bb - 1) * (bb - 2) // 2 for bb in b)
        print(f"  |C|={len(C)} b分布={dict(sorted(Counter(b).items()))} A1={A1} A2={A2} E={E} **Q={Q}**")
        open('n8_witness_Q_pos_SAT.txt', 'w').write(" ".join(format(c, '08b') for c in C) + f"\nQ={Q} A1={A1} A2={A2} b={dict(sorted(Counter(b).items()))}\n")
        print("  ⟹ ⛔ SAT：Q>0 的 (8,32)_1 码存在 ⟹ n=8 pinning 被击穿 ✗（witness 已存 ✓）", flush=True)
    else:
        open('n8_UNSAT_log_SAT.txt', 'w').write(f"UNSAT (Glucose4) time={dt:.1f}s clauses={len(cnf)} vars={N}\n")
        print("  ⟹ ✅ UNSAT：不存在含三重覆盖点的 (8,32)_1 码 ⟹ b(x)≤2 ∀x ⟹ **Q*(8)=0（定理级 ✓）**", flush=True)
