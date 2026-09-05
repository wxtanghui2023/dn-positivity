#!/usr/bin/env python3
# Stadlmann 参数 slack 检查: 条件 (I)(II)(III) of Proposition 3
# 参数: A_n=0.253 (A的上界), δ=0.028, ξ1=0.38, ξ2=ξ3=0.4, ε=0.0075, ϵ=1e-10
An = 0.253
delta = 0.028
xi1, xi2, xi3 = 0.38, 0.4, 0.4
eps_paper = 1e-10

print("=== Proposition 3 条件 (I)(II)(III) slack 检查 ===")
print(f"A_n={An}, δ={delta}, ξ1={xi1}, ξ2={xi2}, ξ3={xi3}\n")

# (I) Type I: min(ξ1 - 4A_n + 2/3, 9/7 - 34A_n/7) - 2ϵ > δ
t1 = xi1 - 4*An + 2/3
t2 = 9/7 - 34*An/7
condI_lhs = min(t1, t2) - 2*eps_paper
print(f"(I) Type I: min({t1:.4f}, {t2:.4f}) - 2ϵ = {condI_lhs:.4f} > δ={delta}? {condI_lhs > delta}")
print(f"    slack = {condI_lhs - delta:.4f}")

# (II) Type II: 19/2 - 36A_n - 13δ + 100ϵ >= 0 AND min(ξ2/10 - 32A_n/10 + 8/10, ξ2/4 + 11/16 - 3A_n) - 2ϵ >= δ
t3 = 19/2 - 36*An - 13*delta + 100*eps_paper
print(f"\n(IIa) 19/2 - 36A_n - 13δ = {t3:.4f} >= 0? {t3 >= 0}")
t4 = xi2/10 - 32*An/10 + 8/10
t5 = xi2/4 + 11/16 - 3*An
condII_lhs = min(t4, t5) - 2*eps_paper
print(f"(IIb) min({t4:.4f}, {t5:.4f}) - 2ϵ = {condII_lhs:.4f} >= δ={delta}? {condII_lhs >= delta}")
print(f"    slack = {condII_lhs - delta:.4f}")

# (III) Type III: 11/8 - 7A_n/2 - 9ξ3/8 - 2ϵ > δ
t6 = 11/8 - 7*An/2 - 9*xi3/8
condIII_lhs = t6 - 2*eps_paper
print(f"\n(III) Type III: 11/8 - 7A_n/2 - 9ξ3/8 - 2ϵ = {condIII_lhs:.4f} > δ={delta}? {condIII_lhs > delta}")
print(f"    slack = {condIII_lhs - delta:.4f}")

print("\n=== A 的扫描 (其他参数固定): 条件 (I)(II)(III) 允许的最大 A ===")
print(f"{'A':>8} {'(I) slack':>10} {'(IIb) slack':>12} {'(III) slack':>12} {'全满足':>6}")
for A_test in [0.253, 0.26, 0.27, 0.28, 0.29, 0.30, 0.32, 0.35]:
    t1 = xi1 - 4*A_test + 2/3
    t2 = 9/7 - 34*A_test/7
    cI = min(t1, t2) - delta  # > 0 需要
    t4 = xi2/10 - 32*A_test/10 + 8/10
    t5 = xi2/4 + 11/16 - 3*A_test
    cII = min(t4, t5) - delta  # >= 0 需要
    t6 = 11/8 - 7*A_test/2 - 9*xi3/8
    cIII = t6 - delta  # > 0 需要
    ok = cI > 0 and cII >= 0 and cIII > 0
    print(f"{A_test:>8.3f} {cI:>10.4f} {cII:>12.4f} {cIII:>12.4f} {'✓' if ok else '✗':>6}")
