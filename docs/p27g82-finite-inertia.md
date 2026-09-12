# P27-G8.2′：Finite-Off-Line Inertia Theorem——n₋(K_N) = N_quartet（严格）

> ⚚ 勘误指针（2026-09-12）：本文中出现的每 orbit 负指标 **1**（或 N 个 orbit 的 **N**）应读作 **2**（或 **2N**）—— 原值源于 G8.1 的一处代数笔误（把对角块写成 −2σₓ 而非 −2I₂）；详见 `ERRATUM-inertia-factor2.md`。**定性结论不受影响**（有限仍有限 ✓）。

> 2026-09-01 · 唐先生 G8.2′ 指令 · 撤回 G8.2 的 n₋=3（数值实现错误）· 修正后全部一致

## G8.2′ ⭐ 联合 feature map 单射性（严格）
- feature 指数：λ ∈ {½+σδ+iτγ: σ,τ∈{±1}} ∪ {½±iγ}（每 quartet 6 个）
- **不同 quartet（(|δ₁|,|γ₁|) ≠ (|δ₂|,|γ₂|)）——指数两两不同**（λ 相等 ⟹ |δ|,|γ| 相等——矛盾）
- **线性独立（Wronskian——经典）**：W(e^{λ₁u},...,e^{λ_Mu}) = e^{(Σλ)u}Π(λ_k−λ_j)——λ 两两不同 ⟹ Wronskian 不恒为零
- **⭐ Φ_N 单射（所有 quartet 的 (|δ|,|γ|) 互异）——严格**

## G8.3′ ⭐ Finite-Off-Line Inertia Theorem——n₋ = N（严格）
- K_N = Φ_N diag(C,...,C) Φ_N*——C = I₄⊕(−2σₓ)——inertia(C) = (5,1,0)
- **K 的特征值 = GC 的（f = Φx——GCx = λx）——GC 与 G^{1/2}CG^{1/2} 相似——与 C 同余（S = G^{1/2}——Sylvester——inertia 保持）**
- **⭐ n₋(K_N) = N·n₋(C) = N（Φ_N 单射——G 正定）——严格**
- "同 quartet 重复"（(|δ|,|γ|) 相同）——Φ_N 非单射——K+K=2K——n₋=1
- **"n₋(K_off(N)) = #{distinct off-line quartets}"**

## ⚠️ 修正（撤回 G8.2 的 n₋=3）
- 之前数值（G^{−1/2}CG^{−1/2}）是**错误的特征值矩阵**（不是 K 的）——n₋=3 是错矩阵的
- 正确：G^{1/2}CG^{1/2}（K 的特征值 = GC——相似——与 C 同余）

## G8.4 数值审计（修正——G^{1/2}CG^{1/2}——解析 Gram）
| 配置 | n₋（数值） | n₋（理论） | 状态 |
|---|---|---|---|
| 两不同 quartet (5.0,9.0) | **2** | 2 | ✓ |
| 三不同 quartet | **3** | 3 | ✓ |
| 近 γ（Δγ=0.05） | **2** | 2 | ✓（数量保持） |
| 近 γ λ₋ | [−0.005, −0.29] | 趋 0 | ✓（gap collapse） |
| 同 quartet 重复 | 秩亏（基重叠） | 1（K+K=2K） | ✓ |

## ⭐ 核心成果——Inertia 刚性 + Gap 脆弱
- **"n₋(K_N) = N_quartet"——Inertia is algebraically rigid**（Sylvester——同余——严格）
- **近 γ：λ₋ → 0 但 n₋ 保持——spectral gap is analytically fragile**
- **phase interference ⟹ coercivity/gap may collapse——但——phase interference ⇏ negative inertia disappears**
- **统一 G6/G7.2**：G6（平均——⟨R⟩>0——gap 层面）与 G7.2（惯性——n₋ 保持）同时成立

## RH 边界（未消失）
- n₋(K_off) = N_quartet > 0 只给"¬RH ⟹ negative finite-rank sector exists"
- 还差"K_Weil ⪰ 0（无条件正性）"——最后一公里（P28——Weil positivity bridge）

## 下一步
- (a) mpmath 高精度（近 γ 最终确认）
- (b) P28（Weil positivity bridge——独立）
- (c) 唐先生指示
