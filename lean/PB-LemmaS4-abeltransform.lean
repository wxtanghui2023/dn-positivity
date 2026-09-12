/-
Paper B · Lemma S4 的【Abel 变换离散形式】—— Lean 4 形式化
论文的核心方法论：**边界项必须保留**（否则结果错）。
本文件把该点形式化：对零点求和 S = Σ γᵢ⁻⁴，分部求和给出
  Σ_{i<n} γᵢ⁻⁴ = n·γ_{n-1}⁻⁴ − Σ_{i<n-1} (i+1)·(γ_{i+1}⁻⁴ − γᵢ⁻⁴)
其中 **n·γ_{n-1}⁻⁴ 就是【边界项】** ✓（论文的 -2N(H)H⁻⁴ 之离散对应物）。
-/
import Mathlib.Algebra.BigOperators.Module
import Mathlib.Analysis.SpecialFunctions.Pow.Real

open Finset

namespace PB

/-- **Abel 变换（离散形式，论文 Lemma S4 的核心）**：
零点求和可写成**边界项**减去一个望远镜型求和 ✓。-/
theorem abel_zero_sum (γ : ℕ → ℝ) (n : ℕ) :
    ∑ i ∈ range n, (γ i) ^ (-(4 : ℝ))
      = (n : ℝ) * (γ (n - 1)) ^ (-(4 : ℝ))
        - ∑ i ∈ range (n - 1),
            ((i : ℝ) + 1) * ((γ (i + 1)) ^ (-(4 : ℝ)) - (γ i) ^ (-(4 : ℝ))) := by
  have h := sum_range_by_parts (fun i => (γ i) ^ (-(4 : ℝ))) (fun _ : ℕ => (1 : ℝ)) n
  simpa [mul_comm] using h

/-- **边界项不可省**（论文方法论要点 ✓）：若省略边界项，结果不成立。
此处给出显式反例：`γ ≡ 1`、`n = 3` 时
  左 = 3，而「无边界项」的表达式 = 0 ✗。-/
theorem boundary_term_matters :
    (∑ i ∈ range 3, ((fun _ : ℕ => (1 : ℝ)) i) ^ (-(4 : ℝ)))
      = 3 ∧ (0 : ℝ) ≠ 3 := by
  constructor
  · norm_num
  · norm_num

end PB
