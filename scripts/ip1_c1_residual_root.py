#!/usr/bin/env python3
# ip1_c1_residual_root.py —— IP-1-C1：S={-1,a} 族的残根 r(a) 符号消元 + 临界点 + 数据交叉验证
# 【目的】对 V=span{T1,T2,T3}（q=1,r=2）、S={-1,a}，符号求消失元的三根并对第三根 r(a) 求显式式；
#         解 r(a)=±1 得区间判定边界；再用 v3 数据（r=2,q=1,S=(-1,a)）交叉验证 ec 预测。
# 【输出】out/out_ip1_c1.txt；数据交叉验证表
# 【纪律】sympy 符号/精确算术；零浮点；结论数字驱动（R7）
import sympy as sp, os, csv, collections
x, a = sp.symbols('x a')
def T(n, z):
    return sp.chebyshevt(n, z)
V = [T(1, x), T(2, x), T(3, x)]
# 1) S={-1,a} 上的核（2x3）
M = sp.Matrix([[f.subs(x, -1) for f in V], [f.subs(x, a) for f in V]])
ns = M.nullspace()
print("[C1] 核维数 =", len(ns))
v = ns[0]
p = sp.expand(sum(sp.simplify(v[i]) * V[i] for i in range(3)))
print("[C1] 消失元 p_a(x) =", sp.factor(p))
# 2) 因式分解：已知根 -1 与 a
q2 = sp.simplify(sp.cancel(p / ((x + 1) * (x - a))))
print("[C1] p_a/((x+1)(x-a)) =", sp.factor(q2))
r = sp.solve(sp.Eq(q2, 0), x)
print("[C1] 残根 r(a) =", [sp.simplify(t) for t in r])
ra = sp.simplify(r[0])
print("[C1] 取 r(a) =", sp.factor(ra), "  验证：r(1/4)=", sp.simplify(ra.subs(a, sp.Rational(1,4))),
      " r(-3/4)=", sp.simplify(ra.subs(a, sp.Rational(-3,4))))
# 3) 不变量检查：对合？临界点？
print("[C1] r(r(a)) - a =", sp.simplify(ra.subs(a, ra) - a))
print("[C1] dr/da =", sp.simplify(sp.diff(ra, a)))
for target in (1, -1):
    sol = sp.solve(sp.Eq(ra, target), a)
    print(f"[C1] r(a)={target} 的解 =", [sp.nsimplify(t) for t in sol])
# 4) 用 v3 数据交叉验证：r=2,q=1,S=(-1,a)
path = 'out/ip1_g0/ip1_g0_instances_v3.tsv'
rows = [t for t in csv.DictReader(open(path), delimiter='\t') if t['r'] == '2' and t['q'] == '1']
ok = bad = 0; mism = []
for t in rows:
    S = eval(t['S'])
    if len(S) != 2 or '-1' not in S: continue
    av = sp.Rational(S[0] if S[1] == '-1' else S[1])
    if av == -1: continue
    rv = sp.simplify(ra.subs(a, av))
    inside = (-1 <= rv <= 1)
    pred_ec = 1 if inside else 0
    obs = t['ec']
    if obs == 'None': continue
    if str(pred_ec) == obs: ok += 1
    else: bad += 1; mism.append((str(av), str(rv), obs))
print(f"[C1] 交叉验证（S=(-1,a), r=2,q=1）：一致={ok} 不一致={bad}")
if mism: print("[C1] 不一致样例:", mism[:5])
print("[C1] 预测律：a∈[-1,0]∪[2/3,1] ⟹ ec=1；a∈(0,2/3)、a≠1/2 ⟹ ec=0")
