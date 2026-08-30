# Post-Freeze Issue Log（v2.15 起）

> 冻结声明：v2.13.2 = Submission Candidate Freeze——No mathematical
> modification after freeze——Only formatting/metadata/journal-specific
> requirements.
>
> 任何新发现**记录于此**——不直接修改 manuscript——待外部验证后统一处理。

| # | 日期 | 发现 | 类型（数学/工程） | 状态 |
|---|------|------|-------------------|------|
| 1 | 08-30 | **Test 1（零背景重建）因子检查点 [A]：S = −(1/2)ΣK_ρ——不是 ΣK_ρ——主恒等式零点部分含 −1/2 因子——1/2 吸收位置须逐项确认（w_H 闭式含 1/2——可能已吸收——但必须核对）** | 数学 | open |
| 2 | 08-30 | **Test 1 因子检查点 [B]：K̂_δ 的 Fourier 因子须在 2π convention 下独立重算（冻结表 −π|ω|e^{−|δ||ω|} 与 convention 一致性）** | 数学 | open |
| 3 | 08-30 | 唐先生专家评估：最大风险 = 主恒等式第一行（Q 的零点谱精确表示）——任何 regularization/Gamma/trivial/零频/重数项不精确抵消 ⟹ R≠0 ⟹ 正性不能推 RH；H_0 合法性/Weil 扩展接口/Δ_H 闭式须独立重推 | 数学 | open |

## 原则

- "内部全绿" ≠ 数学正确性已获外部确认。
- 专家独立重算 7 项（H_0 合法性 / Δ_H 全谱正性 / K_ρ-S 恒等式 / 交换 /
  主恒等式 / 等号刚性 / **无隐藏 RH**）。
- 除非外部验证发现新数学问题——不创建 v2.15.x 数学修订分支。

## 专家验证核心入口

1. `theorem_dependency_graph.md` —— 哪步依赖外部定理/哪步原创/哪步假设
2. `assumption_inventory.md` —— 最小假设表（No step assumes RH）
3. `critical_identities.md` —— 10 条关键恒等式（独立重算用）

## 状态措辞（冻结）

> The manuscript presents a criterion equivalent to the Riemann
> Hypothesis under the stated distributional framework and verified
> analytic identities.
>
> **不是**：The Riemann Hypothesis has been proved.
| 4 | 08-30 | **Test 1 决定性检查（⟨K_δ(·−γ),H_0⟩ 直接数值积分）：数值 = −5.53（γ=14,δ=0）——冻结 w_H(γ,0) = +2.58e-5——符号相反 + 量级差 ~20 万倍——不匹配。δ=0.1：数值 −5.28 vs 冻结 +2.85e-4——同样不符。⚠️ 冻结的 w_H 闭式（正小）与 K_δ-H_0 配对（负大）不一致——主恒等式 Q−Q'_RH=Σ[w_H(γ,δ)−w_H(γ,0)] 的 w_H 来源需彻底重查（convention [B]/H_0 符号/K_0 在线发散需有限部分/或 w_H 定义非 ⟨K_ρ,H_0⟩）** | 数学 | open |
