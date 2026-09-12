/-
Paper B · Lemma S4 所需之【两个幂积分】—— Lean 4 形式化
论文（Abel 变换后）用到：
  ∫_H^∞ t^{-4} dt = (1/3)H^{-3}
  ∫_H^∞ t^{-4} log t dt = (1/3)H^{-3} log H + (1/9)H^{-3}
本文件证明其【有限区间】版本（X 有限），其 X→∞ 极限即上两式。
-/
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

open MeasureTheory intervalIntegral

namespace PB

/-- **有限版本 1**：`∫_H^X t^{-4} dt = (1/3)(H^{-3} - X^{-3})`（`0 < H ≤ X`）。-/
theorem integral_rpow_neg4_finite (H X : ℝ) (hH : 0 < H) (hHX : H ≤ X) :
    ∫ t in H..X, t ^ (-(4 : ℝ)) = (1 / 3) * (H ^ (-(3 : ℝ)) - X ^ (-(3 : ℝ))) := by
  have hderiv : ∀ x ∈ Set.uIcc H X,
      HasDerivAt (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ))) (x ^ (-(4 : ℝ))) x := by
    intro x hx
    rw [Set.uIcc_of_le hHX] at hx
    have hx0 : x ≠ 0 := ne_of_gt (lt_of_lt_of_le hH hx.1)
    have h1 : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ)))
        (1 * (-(3 : ℝ)) * x ^ (-(3 : ℝ) - 1)) x :=
      (hasDerivAt_id x).rpow_const (Or.inl hx0)
    have h2 : HasDerivAt (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ)))
        (-(1 / 3) * (1 * (-(3 : ℝ)) * x ^ (-(3 : ℝ) - 1))) x :=
      h1.const_mul (-(1 / 3))
    convert h2 using 1
    rw [show (-(3 : ℝ) - 1) = -(4 : ℝ) by norm_num]
    ring
  have hint : IntervalIntegrable (fun x : ℝ => x ^ (-(4 : ℝ))) volume H X := by
    apply ContinuousOn.intervalIntegrable
    rw [Set.uIcc_of_le hHX]
    refine ContinuousOn.rpow_const ?_ ?_
    · fun_prop
    · intro x hx
      left
      exact ne_of_gt (lt_of_lt_of_le hH hx.1)
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]
  ring

/-- **有限版本 2**：`∫_H^X t^{-4} log t dt = (1/3)H^{-3}log H - (1/3)X^{-3}log X + (1/9)(H^{-3} - X^{-3})`。
原函数 `G(t) = -(1/3)t^{-3} log t - (1/9)t^{-3}`，`G' = t^{-4} log t`。-/
theorem integral_rpow_neg4_log_finite (H X : ℝ) (hH : 0 < H) (hHX : H ≤ X) :
    ∫ t in H..X, t ^ (-(4 : ℝ)) * Real.log t
      = -(1 / 3) * X ^ (-(3 : ℝ)) * Real.log X - (1 / 9) * X ^ (-(3 : ℝ))
        + ((1 / 3) * H ^ (-(3 : ℝ)) * Real.log H + (1 / 9) * H ^ (-(3 : ℝ))) := by
  have hderiv : ∀ x ∈ Set.uIcc H X,
      HasDerivAt (fun y : ℝ => -(1 / 3) * (y ^ (-(3 : ℝ)) * Real.log y) - (1 / 9) * y ^ (-(3 : ℝ)))
        (x ^ (-(4 : ℝ)) * Real.log x) x := by
    intro x hx
    rw [Set.uIcc_of_le hHX] at hx
    have hxpos : 0 < x := lt_of_lt_of_le hH hx.1
    have hx0 : x ≠ 0 := ne_of_gt hxpos
    -- (t^{-3})' = -3 t^{-4}
    have hA : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ)))
        (1 * (-(3 : ℝ)) * x ^ (-(3 : ℝ) - 1)) x :=
      (hasDerivAt_id x).rpow_const (Or.inl hx0)
    have hA' : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ))) (-(3 : ℝ) * x ^ (-(4 : ℝ))) x := by
      convert hA using 1
      rw [show (-(3 : ℝ) - 1) = -(4 : ℝ) by norm_num]
      ring
    have hl : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log hx0
    have hprod : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ)) * Real.log y)
        ((-(3 : ℝ) * x ^ (-(4 : ℝ))) * Real.log x + x ^ (-(3 : ℝ)) * x⁻¹) x := hA'.mul hl
    have hprod' : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ)) * Real.log y)
        ((-(3 : ℝ)) * (x ^ (-(4 : ℝ)) * Real.log x) + x ^ (-(4 : ℝ))) x := by
      convert hprod using 1
      have hxpow : x ^ (-(3 : ℝ)) * x⁻¹ = x ^ (-(4 : ℝ)) := by
        rw [← Real.rpow_neg_one x, ← Real.rpow_add hxpos]
        norm_num
      rw [hxpow]
      ring
    have h1 : HasDerivAt (fun y : ℝ => -(1 / 3) * (y ^ (-(3 : ℝ)) * Real.log y))
        (-(1 / 3) * ((-(3 : ℝ)) * (x ^ (-(4 : ℝ)) * Real.log x) + x ^ (-(4 : ℝ)))) x :=
      hprod'.const_mul (-(1 / 3))
    have h2 : HasDerivAt (fun y : ℝ => (1 / 9) * y ^ (-(3 : ℝ)))
        ((1 / 9) * (-(3 : ℝ) * x ^ (-(4 : ℝ)))) x := hA'.const_mul (1 / 9)
    have h3 := h1.sub h2
    have hval : -(1 / 3) * (-3 * (x ^ (-(4 : ℝ)) * Real.log x) + x ^ (-(4 : ℝ)))
        - (1 / 9) * (-3 * x ^ (-(4 : ℝ))) = x ^ (-(4 : ℝ)) * Real.log x := by ring
    rw [hval] at h3
    exact h3
  have hint : IntervalIntegrable (fun x : ℝ => x ^ (-(4 : ℝ)) * Real.log x) volume H X := by
    apply ContinuousOn.intervalIntegrable
    rw [Set.uIcc_of_le hHX]
    refine ContinuousOn.mul ?_ ?_
    · refine ContinuousOn.rpow_const ?_ ?_
      · fun_prop
      · intro x hx
        left
        exact ne_of_gt (lt_of_lt_of_le hH hx.1)
    · refine ContinuousOn.log ?_ ?_
      · fun_prop
      · intro x hx
        exact ne_of_gt (lt_of_lt_of_le hH hx.1)
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]
  ring

end PB
