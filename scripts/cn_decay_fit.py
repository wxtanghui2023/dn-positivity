#!/usr/bin/env python3
"""拟合 c_n 的衰减率——c_n ~ O(1/n^α)？——与 F 的奇点结构比较
Laguerre 系数奇点理论：F 在 x_j 的跳跃贡献 ~ jump·L_{n-1}(x_j)·(权重)
L_{n-1}(x) 在 x 固定时的渐近：L_{n-1}(x) ~ e^{x/2}·(π√(n-1))^{-1/2}·cos(2√((n-1)x) − π/4)·(nx)^{-1/4}... 
粗略：|L_{n-1}(x)| ~ e^{x/2}/(π^{1/2}(n-1)^{1/4} x^{1/4})（x > 0 固定）
"""
import numpy as np
import math
from math import comb, factorial, log

def L_m(x, m):
    if m == 0: return np.ones_like(x)
    L0 = np.ones_like(x); L1 = 1 - x
    if m == 1: return L1
    for k in range(2, m+1):
        L2 = ((2*k-1-x)*L1 - (k-1)*L0)/k
        L0, L1 = L1, L2
    return L1

# 用渐近公式验证 L_{n-1}(log m) 的量级
print("L_{n-1}(log m) 的渐近检查（m 固定——n 大）：")
for m in [2, 3, 5]:
    x = log(m)
    print(f"  m={m} (x={x:.3f}):")
    for n in [20, 50, 100, 200]:
        Lv = L_m(np.array([x]), n-1)[0]
        asym = math.exp(x/2)/(math.pi**0.5 * (n-1)**0.25 * x**0.25)
        print(f"    n={n}: L={Lv:+.6f}  渐近幅~{asym:.4f}  比值={abs(Lv)/asym:.3f}")

# 跳跃贡献模型：c_n ≈ Σ_m jump_m·L_{n-1}(log m)——jump_m = Λ(m)/(m log m)
# 每项 ~ Λ(m)/(m log m)·e^{log m/2}·(π√n)^{-1/2}(log m)^{-1/4}
# = Λ(m)/(m^{1/2} log m)·e^{...}——Σ_m Λ(m)/(m^{1/2}(log m)^{5/4})——收敛？Σ 1/(m^{1/2}log m) 发散！
print("\n跳跃贡献的收敛性：Σ_m Λ(m)/(m^{1/2}·(log m)^{5/4})——m 大时 Λ=0 或 log p——~Σ 1/(m^{1/2}) 发散")
print("→ 跳跃模型给 c_n ~ O(n^{-1/4})（发散和——需要抵消）——数值 c_n = O(1/n) 更快")
print("→ F 的光滑部分主导 c_n 的衰减——奇点跳跃不是主要来源")

# 直接拟合：log|c_n| vs log n
print("\nc_n 衰减率拟合：")
data = [(2, 44.54), (3, 99.95), (5, 97.16), (10, 20.66), (20, 9.46), (40, 1.90), (60, 3.86), (100, 0.95), (150, 0.74), (200, 0.84), (300, 0.51)]
import numpy as np
ns = np.array([d[0] for d in data], dtype=float)
cns = np.array([d[1] for d in data], dtype=float)
# 用 n>=20 拟合
mask = ns >= 20
A = np.vstack([np.log(ns[mask]), np.ones(mask.sum())]).T
coef = np.linalg.lstsq(A, np.log(cns[mask]), rcond=None)[0]
print(f"  log|c_n| ≈ {coef[0]:.3f}·log n + {coef[1]:.3f}（n≥20）→ c_n ~ n^{coef[0]:.3f}")
print(f"  α = {-coef[0]:.3f}（如果 α=1——c_n = O(1/n)）")
