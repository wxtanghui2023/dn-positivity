#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 全过程分析：主族零点从起点到终点的完整运动（相图——速度-位置——）
import numpy as np

# 主族零点的运动学：β(τ) = β_ζ - c·e^{-τ}（τ = log X——）
# 速度：v = dβ/dτ = c·e^{-τ} = β_ζ - β（线性恢复——）
# 相图：v vs β——直线（斜率 -1——截距 β_ζ——）

print("=== 全过程分析：β vs 速度 v（主族 γ1——c=1.537——β_ζ=1/2）===")
print("τ=log X——从 X=20 到 X=10^6——")
c = 1.537
beta_zeta = 0.5
print("X        β          速度 v      加速度 a     v = β_ζ-β?")
for Xv in [20, 50, 100, 200, 500, 1000, 5000, 20000, 100000, 1000000]:
    tau = np.log(Xv)
    beta = beta_zeta - c*np.exp(-tau)
    v = c*np.exp(-tau)
    a = -v
    check = abs(v - (beta_zeta - beta))
    print(f"{Xv:>8}  {beta:.8f}  {v:.6e}  {a:.6e}  差={check:.2e}")

print()
print("=== 全过程的结构（不假设 β_ζ——从数据看）===")
print("v vs β 的关系（沿过程——）：")
print("X        β          v        斜率 Δv/Δβ")
prev = None
for Xv in [20, 50, 100, 200, 500, 1000, 5000]:
    beta = 0.5 - c/Xv
    v = c/Xv
    if prev:
        slope = (v - prev[1])/(beta - prev[0])
        print(f"{Xv:>5}  {beta:.6f}  {v:.6e}  斜率={slope:.3f}")
    else:
        print(f"{Xv:>5}  {beta:.6f}  {v:.6e}")
    prev = (beta, v)

print()
print("=== 关键：全过程的外推（v→0 的 β——不依赖 β_ζ 假设——）===")
print("（从有限 X 的数据——v vs β 线性——外推到 v=0——得到终点——）")
# 用 X=100 和 X=1000 两点外推 v=0
X1, X2 = 100, 1000
b1, v1 = 0.5 - c/X1, c/X1
b2, v2 = 0.5 - c/X2, c/X2
slope = (v2 - v1)/(b2 - b1)
b0 = v1 - slope*b1  # v=0 时的 β（v = slope·β + b0——）
print(f"两点（X=100, 1000——）：斜率={slope:.4f}（≈-1——线性——）")
print(f"外推 v=0：β* = {-b0/slope:.6f}（应 = β_ζ = 0.5——）")
print("——但——β_ζ=0.5 已用于生成数据（c 和 β 用 β_ζ=0.5 算——）——循环——")
print("——真正的独立：从'自洽运动学'（数值积分——RK4——）不用 β_ζ——")
