# P28-UC：必要条件审计——q_M=q_H 第 2 类恒等式——UC 命题未满足

> ⚚ 勘误指针（2026-09-12）：本文中出现的每 orbit 负指标 **1**（或 N 个 orbit 的 **N**）应读作 **2**（或 **2N**）—— 原值源于 G8.1 的一处代数笔误（把对角块写成 −2σₓ 而非 −2I₂）；详见 `ERRATUM-inertia-factor2.md`。**定性结论不受影响**（有限仍有限 ✓）。

> 2026-09-01 · 唐先生 P28 最终收紧 · UC 命题（∃M,δ：inf(η−1)>δ）· transfer lemma 目标

## ⭐ q_M=q_H 的来源——恒等式分类（第 2 类）
**N=8——M=1 验证**：
- q_M = q_H（差 6.4e-5——数值相等）
- **q_BCB（x_M*BC⁻¹B*x_M）= 6.803e5——ratio A/BCB = 1.0000（精确！）**
- λ_crit = −7.3e-5（近零）
- **⚠️ Schur 关系向量级：||x_H − (−C⁻¹B*x_M)||/||x_H|| = 0.94（不接近 0！）——x_H ≠ −C⁻¹B*x_M**
- **但——q 级：q_H（实际）= q_H（Schur 预测 6.803593e5）≈ q_BCB——"三相等"（q_M = q_H = q_BCB）**

## ⭐⭐ 判定——"矩阵结构强制的恒等式"（第 2 类）
- **近零模式（λ≈0）+ η≈1（A 与 BC⁻¹B* 在 x_M 上平衡——ratio 1.0000）⟹ q_M = q_H = q_BCB**
- **不是归一化恒等式（第 1 类）——也不是独立渐近定理（第 3 类）**
- **⚠️ 但——"q 级 Schur 平衡"（非向量级——diff 0.94）——新现象——精确机制需更多分析**

## UC 命题审计（∃M, δ>0：inf_{N≥N₀}(η_{M,N}−1) > δ）
- **M=1：η−1 下降（0.117 → 0.018——N=3-10——趋临界——A 分支）**
- **M=2：η−1 上升（0.005 → 0.183——uniform supercritical 迹象——B 分支？）**
- **混合（M 依赖）——无 uniform 下界（inf(η−1) > δ 未满足——M=1 的 δ 趋零）**
- **C 分支（profile 重组）倾向——但——N≤10 未定**

## ⭐ P28 定稿（唐先生）
- **n₋(K_N)=N——λ_N^crit→0⁻——k_peak^crit→N——P_M K_N P_M ⪰ 0——W_M(N)↓（极限未定）——q_cross supplies negative inertia——η_{M,N} ≳ 1**
- **"Finite inertia is extensive, but its negative directions are nonlocal and produced by inter-block coherence. The critical sector approaches the positivity wall through asymptotic cancellation."**
- **未证明：n₋(K_N)=N ⟹? n₋(K_off)=∞（无合法 implication）**
- **目标：N-uniform 的 cross-coherence → negative-form transfer lemma（∃r,δ,V_N：q_N[v] ≤ −δ||v||²——compactness——固定 V——q_off|_V ≤ −δ——n₋(K_off) ≥ dim V——dim V→∞ ⟹ =∞）**

## ⚠️ 诚实边界
- q_M=q_H 第 2 类判定（基于 N=8——M=1——单点）——需多 N/M 确认
- "q 级 Schur 平衡"（非向量级）——机制未完全理解
- UC 命题未满足（η−1 无 uniform 下界——M 依赖混合）——但——N≤10——未定
- η>1+δ ⟹ uniform negative forms?——不能假定（需控制 mass/奇异值/尺度）

## 下一步
- (a) q 级 Schur 平衡的机制分析（q_H = q_BCB 即使 x_H ≠ −C⁻¹B*x_M）
- (b) η−1 的更大 N（UC 判定——uniform or 重组）
- (c) 唐先生指示
