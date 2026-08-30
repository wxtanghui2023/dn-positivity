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
| 5 | 08-30 | **PROVENANCE AUDIT 结论（Go/No-Go）**：✅ w_H 闭式来源已独立重建——w_H(γ,δ) = ⟨K^nat_δ(·−γ), H_0^correct⟩——K^nat = (δ²−x²)/(δ²+x²)²（S 自然单项——无 2——无符号反转）——H_0^correct = −(1/4π)log(1+t²) + 1/(2π(1+t²))（ŵ_target/K̂_0 的 2π convention 构造——第二项正）——解析推导 = [a²(a+1)+δγ²]/(2(a²+γ²)²) = 冻结 w_H 闭式——γ=14 数值匹配（比 1.0002）——γ=30+ 数值失败（quad 振荡精度——方法问题非数学）。🔴 冻结定义 2 错误：①K_δ = 2(x²−δ²)/(x²+δ²)² = −2K^nat（归一化+符号）②冻结 H_0 第二项 −1/(2π(1+t²))（正确 +）——冻结配对 ⟨K_δ^frozen,H_0^frozen⟩ = −2.20 vs w_H +2.58e-5 断裂。⚠️ 主恒等式需在正确定义（K^nat/H_0^correct）下完整重推（Q 零点部分 = −Σm_ρw_H——符号/结构重核） | 数学 | open |
| 6 | 08-30 | **v2.15.1 符号闭合**：K^nat := L'' = (δ²−x²)/(δ²+x²)²（单零点二阶导——数值比 1.000000000000 锁定）——S = +Σm_ρK^nat + S_reg——S_reg = 0（解析——显式项 t 线性——尾项解析估计 −(1/2π)(log(T/2π)+1)/T 解释 0.02 为截断伪差）——**Q − Q'_RH = −Σm_ρΔ_H（负号——统一 K^nat 定义后）**——⚠️ 冻结版 +ΣΔ_H 符号需修正为 −ΣΔ_H（等号条件不变——等价性结论不受影响） | 数学 | open |
| 7 | 08-30 | **v2.15.2 D3 决定性发现（NO-GO 级）**：独立推导 w_H(γ,δ) = [a²(a+1)+δγ²]/(2(a²+γ²)²)——a=1+δ——**实际 δ（非 |δ|）**——Δ_H(γ,δ) = w_H(γ,δ) − w_H(γ,0)——**δ<0 时为负**（γ=14：δ=−0.1 → −2.59e-4；δ=−0.3 → −7.76e-4）——**成对和（δ 与 −δ——函数方程强制）Δ_H(δ)+Δ_H(−δ) = −2.6e-8（负）**——冻结方向正性失败。⚠️ 出路候选：反向 Δ_H' := w_H(γ,0) − w_H(γ,δ)——成对和 +2.6e-8（二阶正——一阶抵消）——但逐点不保持正——判别结构需按零点对重构（二阶小量）。冻结版 |δ| 化 w_H 无独立推导支持——疑似"凑正性" | 数学 | open |
