/-
Paper B · 最后一步比较（论文 §5 末）—— Lean 4 形式化
论文原文：比较化为单个初等不等式
  (7/24)·(H log2H/π) ≤ 2T(H)  ⟺  T(H) ≥ 7H log2H/(48π)
乘 48π/H 后成为  log H + 64πa/3 ≥ 7 log 2（a = 1/(2π)），
即 log H ≥ 4.852 − 10.667 = **−5.815** ✓ —— 对一切 H > 1 成立 ✓。
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace PB

/-- `64πa/3 = 32/3`（a = 1/(2π)）✓ -/
theorem sixtyfour_pi_a_over_three :
    64 * Real.pi * (1 / (2 * Real.pi)) / 3 = 32 / 3 := by
  have hpi : Real.pi ≠ 0 := Real.pi_ne_zero
  field_simp
  ring

/-- **论文的最后一步**：`H > 1` ⟹ `log H + 64πa/3 ≥ 7 log 2` ✓
（即边际 `log H + 64πa/3 − 7log2 > 0` ✓，等价于论文的 `log H ≥ −5.815` ✓）。-/
theorem final_comparison (H : ℝ) (hH : 1 < H) :
    Real.log H + 64 * Real.pi * (1 / (2 * Real.pi)) / 3 ≥ 7 * Real.log 2 := by
  rw [sixtyfour_pi_a_over_three]
  have hlogH : 0 < Real.log H := Real.log_pos hH
  -- log 2 < 1（因 2 < e ⟹ log 2 < log e = 1）
  have hlog2 : Real.log 2 < 1 := by
    have h := Real.log_lt_sub_one_of_pos (by norm_num : (0:ℝ) < 2) (by norm_num : (2:ℝ) ≠ 1)
    linarith
  linarith

/-- **边际为正**（论文末句 ✓）：`log H + 64πa/3 − 7 log 2 > 0` 对 `H > 1` ✓。-/
theorem final_margin_positive (H : ℝ) (hH : 1 < H) :
    0 < Real.log H + 64 * Real.pi * (1 / (2 * Real.pi)) / 3 - 7 * Real.log 2 := by
  rw [sixtyfour_pi_a_over_three]
  have hlogH : 0 < Real.log H := Real.log_pos hH
  have hlog2 : Real.log 2 < 1 := by
    have h := Real.log_lt_sub_one_of_pos (by norm_num : (0:ℝ) < 2) (by norm_num : (2:ℝ) ≠ 1)
    linarith
  linarith

end PB
