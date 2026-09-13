/-
Paper A · 共享恒等式与相位事实 —— Lean 4 形式化（第 15 个文件）

论文 A 与论文 B **共享的同一恒等式**（论文中作为核心机制）：
    对 ρ = β + iγ（β, γ ∈ ℝ，ρ ≠ 0）：
        |1 − 1/ρ|² = 1 + (1 − 2β)/(β² + γ²)
    特别地，在临界线 β = 1/2 上右边为 1，故 |1 − 1/ρ| = 1 精确成立 ——
    这正是论文 A 用"临界线上零点贡献 1 − cos(nθ_γ) ≥ 0"的依据。

证明要点（三步，纯代数）：
    normSq(1 − 1/ρ) = normSq((ρ−1)/ρ) = normSq(ρ−1)/normSq(ρ)
    normSq(ρ−1) = (β−1)² + γ² ;  normSq(ρ) = β² + γ²
    ⟹ ((β−1)² + γ²)/(β²+γ²) = 1 + (1−2β)/(β²+γ²)

【编译记录】2026-09-13 首次编译 **失败**（3 处 error ✗）⟹ 已修正 **全部 3 处** ✓，
    见下文 `normSq_of_re_im` / `normSq_one_sub_inv` / `normSq_one_sub_inv_half` 内的修正注记。
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

open Complex

namespace PA

/-- `normSq (β + γ*I) = β^2 + γ^2`（β, γ 实）✓。-/
theorem normSq_of_re_im (β γ : ℝ) :
    normSq (β + γ * I) = β ^ 2 + γ ^ 2 := by
  -- 【修正 ①】`simp [normSq_apply]` 只展开到 `β * β + γ * γ = β ^ 2 + γ ^ 2`，
  -- 余项须由 `ring` 收尾（`^ 2` 是 Nat 指数，`ring` 会归一化两边的写法）✓
  simp [normSq_apply]
  ring

/-- ⭐ **共享恒等式**（论文 A 与论文 B 的核心机制 ✓）：
    `|1 − 1/ρ|² = 1 + (1 − 2β)/(β² + γ²)`，其中 ρ = β + iγ ≠ 0 ✓。-/
theorem normSq_one_sub_inv (β γ : ℝ) (h : β ^ 2 + γ ^ 2 ≠ 0) :
    normSq (1 - (1 : ℂ) / (β + γ * I)) = 1 + (1 - 2 * β) / (β ^ 2 + γ ^ 2) := by
  have hz : (β + γ * I : ℂ) ≠ 0 := by
    intro hzero
    apply h
    have := congrArg normSq hzero
    simpa [normSq_of_re_im β γ, map_zero] using this
  have hns : normSq (β + γ * I : ℂ) = β ^ 2 + γ ^ 2 := normSq_of_re_im β γ
  have h1 : normSq (1 - (1 : ℂ) / (β + γ * I)) = normSq ((β - 1) + γ * I) / normSq (β + γ * I) := by
    have hrew : (1 : ℂ) - (1 : ℂ) / (β + γ * I) = ((β - 1) + γ * I) / (β + γ * I) := by
      field_simp
      ring
    rw [hrew, normSq_div]
  rw [h1, hns]
  -- 【修正 ②】`normSq_of_re_im (β - 1) γ` 的模式是 `↑(β - 1)`，
  -- 而目标里是 `↑β - 1`（**强制转换与减法的次序不同** ⟹ `rw` 找不到模式 ✗）
  -- ⟹ 先显式转换 `↑β - 1 = ↑(β - 1)` ✓
  have hcast : ((β : ℂ) - 1) = ↑(β - 1) := by
    push_cast
    ring
  rw [hcast, normSq_of_re_im (β - 1) γ]
  field_simp
  ring

/-- 推论（**论文 A 使用的那一步** ✓）：在临界线 β = 1/2 上，`|1 − 1/ρ|² = 1` ✓。-/
theorem normSq_one_sub_inv_half (γ : ℝ) :
    normSq (1 - (1 : ℂ) / ((1 / 2 : ℝ) + γ * I)) = 1 := by
  -- 【修正 ③】本文件的 import 集下 `positivity` **两种目标都证不出** ✗
  -- （`≠ 0` 与 `0 < (1/2)^2 + γ^2` 均报 "failed to prove positivity/nonnegativity/nonzeroness" ✗；
  --  四个候选的实测表见 `lean/PA-positivity-experiment.md` ⟹ **不是**否定型目标的问题 ✓；
  --  且 `nlinarith` 在本 import 集下**不存在** ✗）
  -- ⟹ 改用 `sq_nonneg` + `add_pos_of_pos_of_nonneg`（**实测通过** ✓），并显式 `norm_num` 证首项为正 ✓
  have hpos : (0 : ℝ) < (1 / 2) ^ 2 + γ ^ 2 := by
    have h1 : (0 : ℝ) < (1 / 2 : ℝ) ^ 2 := by norm_num
    have h2 : (0 : ℝ) ≤ γ ^ 2 := sq_nonneg γ
    exact add_pos_of_pos_of_nonneg h1 h2
  rw [normSq_one_sub_inv (1 / 2) γ (ne_of_gt hpos)]
  -- 分子 `1 − 2·(1/2) = 0` ⟹ 右端即 `1` ✓
  rw [show (1 - 2 * (1 / 2) : ℝ) = 0 by norm_num]
  simp

end PA
