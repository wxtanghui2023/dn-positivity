/-
Paper B · Lemma 3（near）之【积分部分】—— Lean 4 形式化
论文用到：∫₀¹ (1+δ)^{-4} dδ = 7/24（精确值）。
-/
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity

open MeasureTheory intervalIntegral

namespace PB

/-- **∫₀¹ (1+δ)⁻⁴ dδ = 7/24**（论文 Lemma 3 中使用的精确值）。

用 FTC，取原函数 `F(δ) = -(1/3)(1+δ)⁻³`，则 `F' = (1+δ)⁻⁴`。 -/
theorem integral_seven_twentyfourths :
    ∫ δ in (0 : ℝ)..1, (1 + δ) ^ (-(4 : ℝ)) = 7 / 24 := by
  have hderiv : ∀ x ∈ Set.uIcc (0 : ℝ) 1,
      HasDerivAt (fun y : ℝ => -(1 / 3) * (1 + y) ^ (-(3 : ℝ))) ((1 + x) ^ (-(4 : ℝ))) x := by
    intro x hx
    have hx0 : (0 : ℝ) ≤ x := by
      have h := hx
      simp only [Set.uIcc_of_le zero_le_one, Set.mem_Icc] at h
      exact h.1
    have hne : (1 + x) ≠ 0 := by linarith
    have h1 : HasDerivAt (fun y : ℝ => 1 + y) 1 x := by
      simpa using (hasDerivAt_id x).const_add 1
    have h2 : HasDerivAt (fun y : ℝ => (1 + y) ^ (-(3 : ℝ)))
        (1 * (-(3 : ℝ)) * (1 + x) ^ (-(3 : ℝ) - 1)) x :=
      h1.rpow_const (Or.inl hne)
    have h3 : HasDerivAt (fun y : ℝ => -(1 / 3) * (1 + y) ^ (-(3 : ℝ)))
        (-(1 / 3) * (1 * (-(3 : ℝ)) * (1 + x) ^ (-(3 : ℝ) - 1))) x :=
      h2.const_mul (-(1 / 3))
    convert h3 using 1
    rw [show (-(3 : ℝ) - 1) = -(4 : ℝ) by norm_num]
    ring
  have hint : IntervalIntegrable (fun y : ℝ => (1 + y) ^ (-(4 : ℝ))) volume (0 : ℝ) 1 := by
    apply ContinuousOn.intervalIntegrable
    refine ContinuousOn.rpow_const ?_ ?_
    · fun_prop
    · intro x hx
      left
      have h0 : (0 : ℝ) ≤ x := by
        have h := hx
        simp only [Set.uIcc_of_le zero_le_one, Set.mem_Icc] at h
        exact h.1
      linarith
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]
  norm_num

end PB
