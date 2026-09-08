#!/usr/bin/env python3
# 从零点约束构造减速机制：D(σ,t) = |Σ v_n|（约束偏差——）沿 σ 的谷结构
# 问题：D 沿 σ 的极小（无条件——每 t——）是否在 σ=1/2？
# 如果 D 的"谷"在 σ=1/2——约束场把运动"吸"到 1/2（减速停止——）

import numpy as np

def zeta_smooth(s, X):
    nmax = max(int(12*X), 200)
    n = np.arange(1, nmax+1)
    return np.sum(n**(-s) * np.exp(-n/X))

X = 3000

def D(sg, t):
    """约束偏差 |Σ v_n| = |ζ 平滑|"""
    return abs(zeta_smooth(complex(sg, t), X))

print("=== D(σ,t) = |Σ v_n| 沿 σ——谷（极小）在哪？===")
# 对多个 t——扫描 σ∈(0.1, 1.0)——找 D 的极小
print("t         D 的极小位置 σ*    D(σ*)")
for t in [3.0, 8.0, 12.0, 14.1347, 16.0, 20.0, 21.022, 25.0, 30.0]:
    best_sg, best_D = 0.5, 1e9
    for sg in np.arange(0.1, 1.0, 0.01):
        d = D(sg, t)
        if d < best_D:
            best_D, best_sg = d, sg
    print(f"{t:>8.2f}   σ*={best_sg:.3f}          D={best_D:.4f}")

print()
print("=== 检查：D 沿 σ 的形状（t=14.1347——零点高度——与 t=16——非零点——）===")
for t in [14.1347, 16.0]:
    print(f"t={t}:")
    for sg in [0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8]:
        print(f"  σ={sg:.2f}: D = {D(sg, t):.4f}")
