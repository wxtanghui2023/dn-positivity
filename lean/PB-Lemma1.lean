/-
Paper B · Lemma 1（单调性）—— Lean 4 形式化
论文陈述：F(x) := x^{k/2} + x^{-k/2} - 2 在 x > 1 上严格递增。
Lean 走【初等路线】（导数引理在本 Mathlib 版本中名字不同，故避开）。
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Order.Monotone.Basic

namespace PB

/-- **代数恒等式**（见 `PB-Basic.lean`，此处重复声明以便单文件编译）。-/
theorem F_eq_sq (x : ℝ) (hx : 0 < x) (k : ℝ) :
    x ^ (k / 2) + x ^ (-(k / 2)) - 2 = (x ^ (k / 4) - x ^ (-(k / 4))) ^ 2 := by
  have hAA : x ^ (k / 4) * x ^ (k / 4) = x ^ (k / 2) := by
    rw [← Real.rpow_add hx, show k / 4 + k / 4 = k / 2 by ring]
  have hBB : x ^ (-(k / 4)) * x ^ (-(k / 4)) = x ^ (-(k / 2)) := by
    rw [← Real.rpow_add hx, show -(k / 4) + -(k / 4) = -(k / 2) by ring]
  have hAB : x ^ (k / 4) * x ^ (-(k / 4)) = 1 := by
    rw [← Real.rpow_add hx, show k / 4 + -(k / 4) = 0 by ring, Real.rpow_zero]
  have hexp : (x ^ (k / 4) - x ^ (-(k / 4))) ^ 2
      = x ^ (k / 4) * x ^ (k / 4) - 2 * (x ^ (k / 4) * x ^ (-(k / 4)))
        + x ^ (-(k / 4)) * x ^ (-(k / 4)) := by ring
  rw [hexp, hAA, hBB, hAB]
  ring


/-- 辅助：`t ↦ (t - t⁻¹)^2` 在 `t > 1` 上严格递增。-/
lemma sq_sub_inv_strictMonoOn : StrictMonoOn (fun t : ℝ => (t - t⁻¹) ^ 2) (Set.Ioi 1) := by
  intro a ha b hb hab
  simp only [Set.mem_Ioi] at ha hb
  have ha0 : 0 < a := by linarith
  -- 逆序：b⁻¹ < a⁻¹
  have h1 : b⁻¹ < a⁻¹ := by
    have := one_div_lt_one_div_of_lt ha0 hab
    simpa [one_div] using this
  -- 于是 a - a⁻¹ < b - b⁻¹
  have h2 : a - a⁻¹ < b - b⁻¹ := by linarith
  -- 且两边为正
  have h3 : 0 < a - a⁻¹ := by
    have := inv_lt_one_of_one_lt₀ ha
    linarith
  have h4 : 0 < b - b⁻¹ := by
    have := inv_lt_one_of_one_lt₀ hb
    linarith
  exact sq_lt_sq' (by linarith) h2

/-- **论文 Lemma 1（单调性）**：`k > 0` 时，`F(x) = x^{k/2} + x^{-k/2} - 2` 在 `x > 1` 上严格递增。-/
theorem mono_F (k : ℝ) (hk : 0 < k) :
    StrictMonoOn (fun x : ℝ => x ^ (k / 2) + x ^ (-(k / 2)) - 2) (Set.Ioi 1) := by
  have hk4 : 0 < k / 4 := by linarith
  intro a ha b hb hab
  simp only [Set.mem_Ioi] at ha hb
  have ha0 : 0 < a := by linarith
  have hb0 : 0 < b := by linarith
  -- 化归为平方形式（先 beta 归约 ✓）
  show a ^ (k / 2) + a ^ (-(k / 2)) - 2 < b ^ (k / 2) + b ^ (-(k / 2)) - 2
  rw [F_eq_sq a ha0, F_eq_sq b hb0,
      Real.rpow_neg (le_of_lt ha0) (k / 4), Real.rpow_neg (le_of_lt hb0) (k / 4)]
  -- 再用辅助引理（基变 y = x^{k/4}）
  exact sq_sub_inv_strictMonoOn
    (Real.one_lt_rpow ha hk4)
    (Real.one_lt_rpow hb hk4)
    (Real.rpow_lt_rpow (le_of_lt ha0) hab hk4)

end PB
