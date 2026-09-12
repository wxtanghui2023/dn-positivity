/-
Paper B · Lemma S4 的【误差项估计】所需积分 —— Lean 4 形式化
论文误差项：`|error| ≤ (4c log H + c/2 + 4d)H^{-4}`，来自 8∫_H^∞ ε(t)·t^{-5}dt 的估计 ✓
需要：
  ∫_H^∞ t^{-5} dt        = (1/4)H^{-4}
  ∫_H^∞ t^{-5} log t dt  = (1/4)H^{-4} log H + (1/16)H^{-4}
-/
import Mathlib.MeasureTheory.Integral.IntegralEqImproper
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

open MeasureTheory Filter

namespace PB

/-- **∫_H^∞ t⁻⁵ dt = (1/4)H⁻⁴**（`H > 0`）✓。-/
theorem integral_Ioi_rpow_neg5 (H : ℝ) (hH : 0 < H) :
    ∫ t in Set.Ioi H, t ^ (-(5 : ℝ)) = (1 / 4) * H ^ (-(4 : ℝ)) := by
  have hcont : ContinuousWithinAt (fun y : ℝ => -(1 / 4) * y ^ (-(4 : ℝ))) (Set.Ici H) H := by
    refine ContinuousWithinAt.const_mul ?_ _
    exact ContinuousWithinAt.rpow_const continuousWithinAt_id (Or.inl (ne_of_gt hH))
  have hderiv : ∀ x ∈ Set.Ioi H,
      HasDerivAt (fun y : ℝ => -(1 / 4) * y ^ (-(4 : ℝ))) (x ^ (-(5 : ℝ))) x := by
    intro x hx
    have hx0 : x ≠ 0 := ne_of_gt (lt_trans hH hx)
    have h1 : HasDerivAt (fun y : ℝ => y ^ (-(4 : ℝ)))
        (1 * (-(4 : ℝ)) * x ^ (-(4 : ℝ) - 1)) x :=
      (hasDerivAt_id x).rpow_const (Or.inl hx0)
    have h2 : HasDerivAt (fun y : ℝ => -(1 / 4) * y ^ (-(4 : ℝ)))
        (-(1 / 4) * (1 * (-(4 : ℝ)) * x ^ (-(4 : ℝ) - 1))) x :=
      h1.const_mul (-(1 / 4))
    convert h2 using 1
    rw [show (-(4 : ℝ) - 1) = -(5 : ℝ) by norm_num]
    ring_nf
  have hint : IntegrableOn (fun x : ℝ => x ^ (-(5 : ℝ))) (Set.Ioi H) volume :=
    integrableOn_Ioi_rpow_of_lt (by norm_num) hH
  have hlim : Tendsto (fun y : ℝ => -(1 / 4) * y ^ (-(4 : ℝ))) atTop (nhds 0) := by
    have h := (tendsto_rpow_neg_atTop (show (0 : ℝ) < 4 by norm_num)).const_mul (-(4 : ℝ)⁻¹)
    simpa using h
  rw [integral_Ioi_of_hasDerivAt_of_tendsto hcont hderiv hint hlim]
  ring

/-- **∫_H^∞ t⁻⁵ log t dt = (1/4)H⁻⁴log H + (1/16)H⁻⁴**（`H > e`）✓。
原函数 `G(t) = -(1/4)(t⁻⁴log t) − (1/16)t⁻⁴`，`G' = t⁻⁵log t` ✓。-/
theorem integral_Ioi_rpow_neg5_log (H : ℝ) (hH : Real.exp 1 < H) :
    ∫ t in Set.Ioi H, t ^ (-(5 : ℝ)) * Real.log t
      = (1 / 4) * H ^ (-(4 : ℝ)) * Real.log H + (1 / 16) * H ^ (-(4 : ℝ)) := by
  have hH0 : 0 < H := lt_trans (Real.exp_pos 1) hH
  have hH1 : 1 < H := lt_trans (by norm_num : (1 : ℝ) < Real.exp 1) hH
  have hcont : ContinuousWithinAt
      (fun y : ℝ => -(1 / 4) * (y ^ (-(4 : ℝ)) * Real.log y) - (1 / 16) * y ^ (-(4 : ℝ)))
      (Set.Ici H) H := by
    refine ContinuousWithinAt.sub ?_ ?_
    · refine ContinuousWithinAt.const_mul ?_ _
      exact (ContinuousWithinAt.rpow_const continuousWithinAt_id (Or.inl (ne_of_gt hH0))).mul
        (Real.continuousAt_log (ne_of_gt hH0)).continuousWithinAt
    · refine ContinuousWithinAt.const_mul ?_ _
      exact ContinuousWithinAt.rpow_const continuousWithinAt_id (Or.inl (ne_of_gt hH0))
  have hderiv : ∀ x ∈ Set.Ioi H,
      HasDerivAt (fun y : ℝ => -(1 / 4) * (y ^ (-(4 : ℝ)) * Real.log y) - (1 / 16) * y ^ (-(4 : ℝ)))
        (x ^ (-(5 : ℝ)) * Real.log x) x := by
    intro x hx
    have hxpos : 0 < x := lt_trans hH0 hx
    have hx0 : x ≠ 0 := ne_of_gt hxpos
    have hA0 : HasDerivAt (fun y : ℝ => y ^ (-(4 : ℝ)))
        (1 * (-(4 : ℝ)) * x ^ (-(4 : ℝ) - 1)) x :=
      (hasDerivAt_id x).rpow_const (Or.inl hx0)
    have hA' : HasDerivAt (fun y : ℝ => y ^ (-(4 : ℝ))) (-(4 : ℝ) * x ^ (-(5 : ℝ))) x := by
      convert hA0 using 1
      rw [show (-(4 : ℝ) - 1) = -(5 : ℝ) by norm_num]
      ring_nf
    have hl : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log hx0
    have hxpow : x ^ (-(4 : ℝ)) * x⁻¹ = x ^ (-(5 : ℝ)) := by
      rw [← Real.rpow_neg_one x, ← Real.rpow_add hxpos]
      norm_num
    have hprod : HasDerivAt (fun y : ℝ => y ^ (-(4 : ℝ)) * Real.log y)
        ((-(4 : ℝ)) * (x ^ (-(5 : ℝ)) * Real.log x) + x ^ (-(5 : ℝ))) x := by
      have h := hA'.mul hl
      have hval : (-(4 : ℝ) * x ^ (-(5 : ℝ))) * Real.log x + x ^ (-(4 : ℝ)) * x⁻¹
          = (-(4 : ℝ)) * (x ^ (-(5 : ℝ)) * Real.log x) + x ^ (-(5 : ℝ)) := by
        rw [hxpow]
        ring
      rw [hval] at h
      exact h
    have h1 : HasDerivAt (fun y : ℝ => -(1 / 4) * (y ^ (-(4 : ℝ)) * Real.log y))
        (-(1 / 4) * ((-(4 : ℝ)) * (x ^ (-(5 : ℝ)) * Real.log x) + x ^ (-(5 : ℝ)))) x :=
      hprod.const_mul (-(1 / 4))
    have h2 : HasDerivAt (fun y : ℝ => (1 / 16) * y ^ (-(4 : ℝ)))
        ((1 / 16) * (-(4 : ℝ) * x ^ (-(5 : ℝ)))) x := hA'.const_mul (1 / 16)
    have h3 := h1.sub h2
    have hval : -(1 / 4) * (-(4 : ℝ) * (x ^ (-(5 : ℝ)) * Real.log x) + x ^ (-(5 : ℝ)))
        - (1 / 16) * (-(4 : ℝ) * x ^ (-(5 : ℝ))) = x ^ (-(5 : ℝ)) * Real.log x := by ring
    rw [hval] at h3
    exact h3
  have hint : IntegrableOn (fun x : ℝ => x ^ (-(5 : ℝ)) * Real.log x) (Set.Ioi H) volume := by
    have hbase : IntegrableOn (fun x : ℝ => x ^ (-(4 : ℝ))) (Set.Ioi H) volume :=
      integrableOn_Ioi_rpow_of_lt (by norm_num) hH0
    rw [IntegrableOn] at hbase ⊢
    refine hbase.mono' ?_ ?_
    · refine ContinuousOn.aestronglyMeasurable ?_ measurableSet_Ioi
      intro x hx
      refine ContinuousAt.continuousWithinAt ?_
      refine ContinuousAt.mul ?_ ?_
      · exact continuousAt_id.rpow_const (Or.inl (ne_of_gt (lt_trans hH0 hx)))
      · exact Real.continuousAt_log (ne_of_gt (lt_trans hH0 hx))
    · filter_upwards [ae_restrict_mem measurableSet_Ioi] with x hx
      have hxpos : 0 < x := lt_trans hH0 hx
      have hx1 : 1 < x := lt_trans hH1 hx
      have hlog_le : Real.log x ≤ x := by
        have h := Real.log_le_sub_one_of_pos hxpos
        linarith
      have hlog_nn : 0 ≤ Real.log x := Real.log_nonneg hx1.le
      have hrpow_nn : 0 ≤ x ^ (-(5 : ℝ)) := Real.rpow_nonneg hxpos.le _
      rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hrpow_nn hlog_nn)]
      calc x ^ (-(5 : ℝ)) * Real.log x ≤ x ^ (-(5 : ℝ)) * x :=
            mul_le_mul_of_nonneg_left hlog_le hrpow_nn
        _ = x ^ (-(4 : ℝ)) := by
            have h1 : x ^ (-(5 : ℝ)) * x = x ^ (-(5 : ℝ)) * x ^ (1 : ℝ) := by rw [Real.rpow_one]
            rw [h1, ← Real.rpow_add hxpos]
            norm_num
  have hlim : Tendsto
      (fun y : ℝ => -(1 / 4) * (y ^ (-(4 : ℝ)) * Real.log y) - (1 / 16) * y ^ (-(4 : ℝ)))
      atTop (nhds 0) := by
    have hlog_div : Tendsto (fun y : ℝ => Real.log y / y ^ (4 : ℝ)) atTop (nhds 0) := by
      have h := isLittleO_log_rpow_atTop (show (0 : ℝ) < 4 by norm_num)
      simpa using h.tendsto_div_nhds_zero
    have hrpow : Tendsto (fun y : ℝ => y ^ (-(4 : ℝ))) atTop (nhds 0) :=
      tendsto_rpow_neg_atTop (by norm_num)
    have h1 : Tendsto (fun y : ℝ => -(1 / 4) * (y ^ (-(4 : ℝ)) * Real.log y)) atTop (nhds 0) := by
      have h2' : Tendsto (fun y : ℝ => -(1 / 4) * (Real.log y / y ^ (4 : ℝ))) atTop (nhds 0) := by
        have h := hlog_div.const_mul (-(1 / 4))
        rw [show -(1 / 4) * 0 = (0 : ℝ) by ring] at h
        exact h
      refine Filter.Tendsto.congr' ?_ h2'
      filter_upwards [eventually_gt_atTop 0] with y hy
      rw [Real.rpow_neg hy.le 4]
      ring
    have h2 : Tendsto (fun y : ℝ => (1 / 16) * y ^ (-(4 : ℝ))) atTop (nhds 0) := by
      have h := hrpow.const_mul (1 / 16)
      rw [show (1 / 16) * 0 = (0 : ℝ) by ring] at h
      exact h
    simpa using h1.sub h2
  rw [integral_Ioi_of_hasDerivAt_of_tendsto hcont hderiv hint hlim]
  ring

end PB
