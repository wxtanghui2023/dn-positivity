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

namespace PB

/-- 辅助（与 `PB-LemmaS4-abel.lean` 同，此处重复以便单文件编译 ✓）：
`∫_H^∞ t⁻⁴dt = (1/3)H⁻³` ✓。-/
theorem integral_Ioi_rpow_neg4' (H : ℝ) (hH : 0 < H) :
    ∫ t in Set.Ioi H, t ^ (-(4 : ℝ)) = (1 / 3) * H ^ (-(3 : ℝ)) := by
  have hcont : ContinuousWithinAt (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ))) (Set.Ici H) H := by
    refine ContinuousWithinAt.const_mul ?_ _
    exact ContinuousWithinAt.rpow_const continuousWithinAt_id (Or.inl (ne_of_gt hH))
  have hderiv : ∀ x ∈ Set.Ioi H,
      HasDerivAt (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ))) (x ^ (-(4 : ℝ))) x := by
    intro x hx
    have hx0 : x ≠ 0 := ne_of_gt (lt_trans hH hx)
    have h1 : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ)))
        (1 * (-(3 : ℝ)) * x ^ (-(3 : ℝ) - 1)) x :=
      (hasDerivAt_id x).rpow_const (Or.inl hx0)
    have h2 : HasDerivAt (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ)))
        (-(1 / 3) * (1 * (-(3 : ℝ)) * x ^ (-(3 : ℝ) - 1))) x :=
      h1.const_mul (-(1 / 3))
    convert h2 using 1
    rw [show (-(3 : ℝ) - 1) = -(4 : ℝ) by norm_num]
    ring_nf
  have hint : IntegrableOn (fun x : ℝ => x ^ (-(4 : ℝ))) (Set.Ioi H) volume :=
    integrableOn_Ioi_rpow_of_lt (by norm_num) hH
  have hlim : Tendsto (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ))) atTop (nhds 0) := by
    have h := (tendsto_rpow_neg_atTop (show (0 : ℝ) < 3 by norm_num)).const_mul (-(3 : ℝ)⁻¹)
    simpa using h
  rw [integral_Ioi_of_hasDerivAt_of_tendsto hcont hderiv hint hlim]
  ring

/-- 辅助：`∫_H^∞ t⁻⁴ log t dt = (1/3)H⁻³log H + (1/9)H⁻³`（`H > e`）✓。-/
theorem integral_Ioi_rpow_neg4_log' (H : ℝ) (hH : Real.exp 1 < H) :
    ∫ t in Set.Ioi H, t ^ (-(4 : ℝ)) * Real.log t
      = (1 / 3) * H ^ (-(3 : ℝ)) * Real.log H + (1 / 9) * H ^ (-(3 : ℝ)) := by
  have hH0 : 0 < H := lt_trans (Real.exp_pos 1) hH
  have hH1 : 1 < H := lt_trans (by norm_num : (1 : ℝ) < Real.exp 1) hH
  have hcont : ContinuousWithinAt
      (fun y : ℝ => -(1 / 3) * (y ^ (-(3 : ℝ)) * Real.log y) - (1 / 9) * y ^ (-(3 : ℝ)))
      (Set.Ici H) H := by
    refine ContinuousWithinAt.sub ?_ ?_
    · refine ContinuousWithinAt.const_mul ?_ _
      exact (ContinuousWithinAt.rpow_const continuousWithinAt_id (Or.inl (ne_of_gt hH0))).mul
        (Real.continuousAt_log (ne_of_gt hH0)).continuousWithinAt
    · refine ContinuousWithinAt.const_mul ?_ _
      exact ContinuousWithinAt.rpow_const continuousWithinAt_id (Or.inl (ne_of_gt hH0))
  have hderiv : ∀ x ∈ Set.Ioi H,
      HasDerivAt (fun y : ℝ => -(1 / 3) * (y ^ (-(3 : ℝ)) * Real.log y) - (1 / 9) * y ^ (-(3 : ℝ)))
        (x ^ (-(4 : ℝ)) * Real.log x) x := by
    intro x hx
    have hxpos : 0 < x := lt_trans hH0 hx
    have hx0 : x ≠ 0 := ne_of_gt hxpos
    have hA0 : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ)))
        (1 * (-(3 : ℝ)) * x ^ (-(3 : ℝ) - 1)) x :=
      (hasDerivAt_id x).rpow_const (Or.inl hx0)
    have hA' : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ))) (-(3 : ℝ) * x ^ (-(4 : ℝ))) x := by
      convert hA0 using 1
      rw [show (-(3 : ℝ) - 1) = -(4 : ℝ) by norm_num]
      ring_nf
    have hl : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log hx0
    have hxpow : x ^ (-(3 : ℝ)) * x⁻¹ = x ^ (-(4 : ℝ)) := by
      rw [← Real.rpow_neg_one x, ← Real.rpow_add hxpos]
      norm_num
    have hprod : HasDerivAt (fun y : ℝ => y ^ (-(3 : ℝ)) * Real.log y)
        ((-(3 : ℝ)) * (x ^ (-(4 : ℝ)) * Real.log x) + x ^ (-(4 : ℝ))) x := by
      have h := hA'.mul hl
      have hval : (-(3 : ℝ) * x ^ (-(4 : ℝ))) * Real.log x + x ^ (-(3 : ℝ)) * x⁻¹
          = (-(3 : ℝ)) * (x ^ (-(4 : ℝ)) * Real.log x) + x ^ (-(4 : ℝ)) := by
        rw [hxpow]
        ring
      rw [hval] at h
      exact h
    have h1 : HasDerivAt (fun y : ℝ => -(1 / 3) * (y ^ (-(3 : ℝ)) * Real.log y))
        (-(1 / 3) * ((-(3 : ℝ)) * (x ^ (-(4 : ℝ)) * Real.log x) + x ^ (-(4 : ℝ)))) x :=
      hprod.const_mul (-(1 / 3))
    have h2 : HasDerivAt (fun y : ℝ => (1 / 9) * y ^ (-(3 : ℝ)))
        ((1 / 9) * (-(3 : ℝ) * x ^ (-(4 : ℝ)))) x := hA'.const_mul (1 / 9)
    have h3 := h1.sub h2
    have hval : -(1 / 3) * (-(3 : ℝ) * (x ^ (-(4 : ℝ)) * Real.log x) + x ^ (-(4 : ℝ)))
        - (1 / 9) * (-(3 : ℝ) * x ^ (-(4 : ℝ))) = x ^ (-(4 : ℝ)) * Real.log x := by ring
    rw [hval] at h3
    exact h3
  have hint : IntegrableOn (fun x : ℝ => x ^ (-(4 : ℝ)) * Real.log x) (Set.Ioi H) volume := by
    have hbase : IntegrableOn (fun x : ℝ => x ^ (-(3 : ℝ))) (Set.Ioi H) volume :=
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
      have hrpow_nn : 0 ≤ x ^ (-(4 : ℝ)) := Real.rpow_nonneg hxpos.le _
      rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hrpow_nn hlog_nn)]
      calc x ^ (-(4 : ℝ)) * Real.log x ≤ x ^ (-(4 : ℝ)) * x :=
            mul_le_mul_of_nonneg_left hlog_le hrpow_nn
        _ = x ^ (-(3 : ℝ)) := by
            have h1 : x ^ (-(4 : ℝ)) * x = x ^ (-(4 : ℝ)) * x ^ (1 : ℝ) := by rw [Real.rpow_one]
            rw [h1, ← Real.rpow_add hxpos]
            norm_num
  have hlim : Tendsto
      (fun y : ℝ => -(1 / 3) * (y ^ (-(3 : ℝ)) * Real.log y) - (1 / 9) * y ^ (-(3 : ℝ)))
      atTop (nhds 0) := by
    have hlog_div : Tendsto (fun y : ℝ => Real.log y / y ^ (3 : ℝ)) atTop (nhds 0) := by
      have h := isLittleO_log_rpow_atTop (show (0 : ℝ) < 3 by norm_num)
      simpa using h.tendsto_div_nhds_zero
    have hrpow : Tendsto (fun y : ℝ => y ^ (-(3 : ℝ))) atTop (nhds 0) :=
      tendsto_rpow_neg_atTop (by norm_num)
    have h1 : Tendsto (fun y : ℝ => -(1 / 3) * (y ^ (-(3 : ℝ)) * Real.log y)) atTop (nhds 0) := by
      have h2' : Tendsto (fun y : ℝ => -(1 / 3) * (Real.log y / y ^ (3 : ℝ))) atTop (nhds 0) := by
        have h := hlog_div.const_mul (-(1 / 3))
        rw [show -(1 / 3) * 0 = (0 : ℝ) by ring] at h
        exact h
      refine Filter.Tendsto.congr' ?_ h2'
      filter_upwards [eventually_gt_atTop 0] with y hy
      rw [Real.rpow_neg hy.le 3]
      ring
    have h2 : Tendsto (fun y : ℝ => (1 / 9) * y ^ (-(3 : ℝ))) atTop (nhds 0) := by
      have h := hrpow.const_mul (1 / 9)
      rw [show (1 / 9) * 0 = (0 : ℝ) by ring] at h
      exact h
    simpa using h1.sub h2
  rw [integral_Ioi_of_hasDerivAt_of_tendsto hcont hderiv hint hlim]
  ring

end PB

namespace PB

/-- `t⁻⁴ log t` 在 `(H,∞)` 上可积（`H > e`）✓。用比较 `log t ≤ t` ⟹ `t⁻⁴log t ≤ t⁻³` ✓。-/
theorem integrableOn_Ioi_rpow_neg4_log (H : ℝ) (hH : Real.exp 1 < H) :
    IntegrableOn (fun t : ℝ => t ^ (-(4 : ℝ)) * Real.log t) (Set.Ioi H) := by
  have hH0 : 0 < H := lt_trans (Real.exp_pos 1) hH
  have hH1 : 1 < H := lt_trans (by norm_num : (1 : ℝ) < Real.exp 1) hH
  have hbase : IntegrableOn (fun x : ℝ => x ^ (-(3 : ℝ))) (Set.Ioi H) volume :=
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
    have hrpow_nn : 0 ≤ x ^ (-(4 : ℝ)) := Real.rpow_nonneg hxpos.le _
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hrpow_nn hlog_nn)]
    calc x ^ (-(4 : ℝ)) * Real.log x ≤ x ^ (-(4 : ℝ)) * x :=
          mul_le_mul_of_nonneg_left hlog_le hrpow_nn
      _ = x ^ (-(3 : ℝ)) := by
          have h1 : x ^ (-(4 : ℝ)) * x = x ^ (-(4 : ℝ)) * x ^ (1 : ℝ) := by rw [Real.rpow_one]
          rw [h1, ← Real.rpow_add hxpos]
          norm_num

end PB

namespace PB

/-- ★★ **Lemma S4 主项总装**（论文的核心计算 ✓）：把 Abel 变换的贡献算成论文所给的系数 ✓
`−2N(H)H⁻⁴ + 8∫_H^∞ N(t)t⁻⁵dt = (2a/3)H⁻³log H + (8a/9 + 2b/3)H⁻³`
其中 `N(t) = a·t·log t + b·t`（计数函数的光滑主项 ✓）✓。-/
theorem S4_main_terms (a b H : ℝ) (hH : Real.exp 1 < H) :
    -(2 * (a * H * Real.log H + b * H)) * H ^ (-(4 : ℝ))
        + 8 * ∫ t in Set.Ioi H, (a * t * Real.log t + b * t) * t ^ (-(5 : ℝ))
      = (2 * a / 3) * H ^ (-(3 : ℝ)) * Real.log H
        + (8 * a / 9 + 2 * b / 3) * H ^ (-(3 : ℝ)) := by
  have hH0 : 0 < H := lt_trans (Real.exp_pos 1) hH
  -- ① 点态拆分 + 积分线性
  have hsplit : (∫ t in Set.Ioi H, (a * t * Real.log t + b * t) * t ^ (-(5 : ℝ)))
      = a * (∫ t in Set.Ioi H, t ^ (-(4 : ℝ)) * Real.log t)
        + b * (∫ t in Set.Ioi H, t ^ (-(4 : ℝ))) := by
    have hpt : Set.EqOn (fun t : ℝ => (a * t * Real.log t + b * t) * t ^ (-(5 : ℝ)))
        (fun t : ℝ => a * (t ^ (-(4 : ℝ)) * Real.log t) + b * t ^ (-(4 : ℝ))) (Set.Ioi H) := by
      intro t ht
      have htpos : 0 < t := lt_trans hH0 (Set.mem_Ioi.mp ht)
      have h1 : t * t ^ (-(5 : ℝ)) = t ^ (-(4 : ℝ)) := by
        have h2 : t * t ^ (-(5 : ℝ)) = t ^ (1 : ℝ) * t ^ (-(5 : ℝ)) := by rw [Real.rpow_one]
        rw [h2, ← Real.rpow_add htpos]
        norm_num
      simp only
      rw [add_mul, mul_assoc b t]
      have h2 : a * t * Real.log t * t ^ (-(5 : ℝ))
          = a * Real.log t * (t * t ^ (-(5 : ℝ))) := by ring
      rw [h2, h1]
      ring_nf
    rw [setIntegral_congr_fun measurableSet_Ioi hpt]
    rw [integral_add ((integrableOn_Ioi_rpow_neg4_log H hH).const_mul a)
      ((integrableOn_Ioi_rpow_of_lt (by norm_num) hH0).const_mul b)]
    rw [integral_const_mul, integral_const_mul]
  rw [hsplit, integral_Ioi_rpow_neg4_log' H hH, integral_Ioi_rpow_neg4' H hH0]
  -- rpow 关系 H·H⁻⁴ = H⁻³（ring 无法自行导出 ✓）
  have hHpow : H * H ^ (-(4 : ℝ)) = H ^ (-(3 : ℝ)) := by
    have h2 : H * H ^ (-(4 : ℝ)) = H ^ (1 : ℝ) * H ^ (-(4 : ℝ)) := by rw [Real.rpow_one]
    rw [h2, ← Real.rpow_add hH0]
    norm_num
  -- 把 H·H⁻⁴ = H⁻³ 分别乘上 a·log H 与 b ✓
  have h1 : a * H * Real.log H * H ^ (-(4 : ℝ)) = a * Real.log H * H ^ (-(3 : ℝ)) := by
    have hm := congrArg (fun z => a * Real.log H * z) hHpow
    simpa [mul_assoc, mul_comm, mul_left_comm] using hm
  have h2 : b * H * H ^ (-(4 : ℝ)) = b * H ^ (-(3 : ℝ)) := by
    have hm := congrArg (fun z => b * z) hHpow
    simpa [mul_assoc, mul_comm, mul_left_comm] using hm
  rw [show -(2 * (a * H * Real.log H + b * H)) * H ^ (-(4 : ℝ))
      = -(2 * (a * H * Real.log H * H ^ (-(4 : ℝ)) + b * H * H ^ (-(4 : ℝ)))) by ring,
    h1, h2]
  ring_nf

end PB

namespace PB

/-- ★ **误差项的分解与论文常数核对**（重要 ✓）：
论文 Lemma S4 给出 `|error| ≤ (4c log H + c/2 + 4d)H⁻⁴` ✓。
我起初只算**积分项**，得 `(2c log H + c/2 + 2d)` ✗ —— 少了**边界项**的 ε 贡献 ✓！
   边界项 `−2N(H)H⁻⁴` 中的 `−2ε(H)H⁻⁴` 贡献 `≤ (2c log H + 2d)H⁻⁴` ✓
   两者相加：`(2c log H + 2d) + (2c log H + c/2 + 2d) = 4c log H + c/2 + 4d` ✓✓
   ⟹ **论文常数正确** ✓；我漏了边界项 ✗ —— 与论文自己的方法论警告（**边界项必须保留** ✓）**同源** ✓✓
本引理即验证这条算术 ✓。-/
theorem S4_error_constant_check (c d L : ℝ) :
    (2 * c * L + 2 * d) + (2 * c * L + c / 2 + 2 * d) = 4 * c * L + c / 2 + 4 * d := by
  ring

end PB
