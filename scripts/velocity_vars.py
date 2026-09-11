#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# 速度的变量分析：零点轨迹运动 vs 约束
# 问题1：速度受哪几个变量影响？
# 问题2：零点约束（Σ v_n = 0）是否控制这些速度变量？

import numpy as np

# === 运动学（零点轨迹——主族——）：β 方向的运动 ===
# β_X = β_ζ - c/X（τ=log X 时：β(τ) = β_ζ - c·e^{-τ}）
# 速度：v = dβ/dτ = c·e^{-τ} = (β_ζ - β)
# 变量：β（位置）、β_ζ（终点）
print("=== 速度的变量分析 ===")
print()
print("【运动 A：零点轨迹（ζ_X 的零点随 X）】")
print("β 方向速度：v = dβ/dτ = -(β - β_ζ)")
print("速度受变量：")
print("  1. β（当前位置——零点实部——）")
print("  2. β_ζ（终点——ζ 零点的实部——）")
print("  （γ 方向另有速度：v_γ = dγ/dτ——受 γ、γ_k——）")
print()
print("零点约束（ζ(ρ)=0）是否控制这些变量？")
print("  → 约束控制 β_ζ（终点必须是零点——ζ(β_ζ+iγ_k)=0——）")
print("  → 但不控制 β_ζ = 1/2（离轴零点 β_ζ=σ₀≠1/2 也满足约束——）")
print("  → 所以：零点约束'部分控制'（决定终点是零点）但不'选 1/2'")
print()

# === 运动 B：约束偏差驱动的运动（梯度流——）===
# D(σ) = |Σ v_n|——v = -∂D/∂σ——速度 0 在 D 的极小
print("【运动 B：约束偏差梯度流（v = -∂D/∂σ——D=|Σ v_n|）】")
print("速度受变量：σ（位置）、t（高度——通过 D 的结构——）")
print("零点约束（D=0 在零点——）是否控制？")
print("  → D 的极小（速度0处）在零点高度是 σ=1/2（数据——）")
print("  → 但非零点高度 D 谷在 σ→1（边界——）——不指向 1/2")
print("  → 约束不'无条件控制'速度 0 在 1/2")
print()

# === 关键：速度的完整变量清单（结合运动学——）===
# 从运动学：dβ/dτ = -[Σ n^{1-β}cos(γ log n)e^{-n/X}]·(1/X²)/|ζ_X'| 类——
# 速度实际受：β、γ、X、以及所有 n 的贡献（素数/合数——相位——）
print("【速度的完整变量（从自洽运动学——）】")
print("v_β = Re[-∂ζ_X/∂X / ζ_X'(ρ_X)]——受：")
print("  1. β（位置——）")
print("  2. γ（高度——）")
print("  3. X（截断——时间——）")
print("  4. Σ n^{1-β}e^{-n/X} 的相位结构（所有 n——素数/合数——）")
print("  5. ζ_X'(ρ_X)（零点导数——零点结构——）")
print()

print("=== 零点约束对速度变量的控制 ===")
print("零点约束：Σ_n v_n(ρ) = 0（ζ(ρ)=0——）")
print("  控制 β、γ？（→ 零点位置——但离轴可能——）")
print("  控制 X？（→ 否——X 是外部参数——）")
print("  控制 Σ 的相位？（→ 约束要求总和为 0——相位平衡——）")
print("  控制 ζ_X'？（→ 零点导数——由零点结构决定——）")
