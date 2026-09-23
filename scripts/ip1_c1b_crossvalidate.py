#!/usr/bin/env python3
# ip1_c1b_crossvalidate.py —— IP-1-C1b：S={-1,a} 族的 r(a) 定律 vs 逐例实测 ec
# 【目的】符号求 r(a)；对 grid 上每个 a 逐例算 ec（sympy 权威计数），与定律 [r(a)∈[-1,1] ⟹ ec=1] 对比
# 【输出】out/out_ip1_c1b.txt
import sympy as sp
x, a = sp.symbols('x a')
V = [sp.chebyshevt(1, x), sp.chebyshevt(2, x), sp.chebyshevt(3, x)]

# --- r(a)：从核消元 ---
M = sp.Matrix([[f.subs(x, -1) for f in V], [f.subs(x, a) for f in V]])
v = M.nullspace()[0]
p = sp.expand(sum(sp.simplify(v[i]) * V[i] for i in range(3)))
q2 = sp.cancel(p / ((x + 1) * (x - a)))
ra = sp.simplify(sp.solve(sp.Eq(q2, 0), x)[0])
print("[C1b] p_a(x) =", sp.factor(p))
print("[C1b] r(a) =", sp.factor(ra))
print("[C1b] r(r(a)) - a =", sp.simplify(ra.subs(a, ra) - a), "  dr/da =", sp.simplify(sp.diff(ra, a)))

# --- 逐例实测 vs 定律 ---
grid = [sp.Rational(k, 4) for k in range(-4, 5)]
ok = bad = 0
rows = []
for av in grid:
    if av == -1 or av == sp.Rational(1, 2):
        continue
    S = [-1, av]
    Ms = sp.Matrix([[f.subs(x, s) for f in V] for s in S])
    ns = Ms.nullspace()
    if not ns:
        continue
    vv = ns[0]
    pp = sp.expand(sum(sp.simplify(vv[i]) * V[i] for i in range(3)))
    ec = sp.Poly(pp, x).count_roots(-1, 1) - len(S)
    rv = sp.simplify(ra.subs(a, av))
    pred = 1 if (-1 <= rv <= 1) else 0
    good = (str(pred) == str(ec))
    ok += good; bad += (not good)
    rows.append((str(av), str(rv), str(sp.N(rv, 6)), str(ec), str(pred), "OK" if good else "MISMATCH"))
print("[C1b] a | r(a) | r 数值 | 实测 ec | 预测 ec | 一致")
for t in rows:
    print("     " + " | ".join(t))
print(f"[C1b] 一致={ok} 不一致={bad}")

# --- 极点 a=1/2 的结构读法 ---
av = sp.Rational(1, 2)
M2 = sp.Matrix([[f.subs(x, s) for f in V[:2]] for s in [-1, av]])
print("[C1b] a=1/2: span{T1,T2} 在 S 上的核维数 =", len(M2.nullspace()), "⟹ 前缀降秩 ⟹ d_V=q+1=2（flag 类别改变）")
