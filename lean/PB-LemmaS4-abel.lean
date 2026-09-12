/-
Paper B · Lemma S4 —— 无穷区间积分 + 系数代数（Lean 4 形式化）
① ∫_H^∞ t^{-4} dt = (1/3)H^{-3}（反常积分，用 FTC-2 + 可积性 + 极限）
② S4 的系数代数：Abel 变换后主项系数 = 论文所给
   (8a/3 − 2a) = 2a/3，  (8a/9 + 8b/3 − 2b) = 8a/9 + 2b/3
-/
import Mathlib.MeasureTheory.Integral.IntegralEqImproper
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

open MeasureTheory intervalIntegral Filter

namespace PB

/-- **反常积分**：`∫_H^∞ t^{-4} dt = (1/3)H^{-3}`（`H > 0`）。-/
theorem integral_Ioi_rpow_neg4 (H : ℝ) (hH : 0 < H) :
    ∫ t in Set.Ioi H, t ^ (-(4 : ℝ)) = (1 / 3) * H ^ (-(3 : ℝ)) := by
  have hcont : ContinuousWithinAt (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ))) (Set.Ici H) H := by
    refine ContinuousWithinAt.const_mul ?_ _
    exact ContinuousWithinAt.rpow_const continuousWithinAt_id
      (Or.inl (ne_of_gt hH))
  have hderiv : ∀ x ∈ Set.Ioi H, HasDerivAt (fun y : ℝ => -(1 / 3) * y ^ (-(3 : ℝ))) (x ^ (-(4 : ℝ))) x := by
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

/-- **S4 系数代数**（论文 Abel 变换后的关键计算 ✓）：
主项系数由 `8∫ (at log t)·t^{-5}dt − 2(aH log H)·H^{-4}` 等项合并而来，结果为
`2a/3`（配 `H^{-3}log H`）与 `8a/9 + 2b/3`（配 `H^{-3}`）。-/
theorem S4_coefficients (a b : ℝ) :
    (8 * a / 3 - 2 * a = 2 * a / 3) ∧ (8 * a / 9 + 8 * b / 3 - 2 * b = 8 * a / 9 + 2 * b / 3) := by
  constructor <;> ring

/-- **S4 主项的显式合并**（把 Abel 变换的贡献写成论文形式 ✓）：
`8·[a/3·L + a/9 + b/3] − 2·(a·L + b) = (2a/3)·L + (8a/9 + 2b/3)`，
其中 `L = H^{-3} log H` 型的项已按 `H^{-3}log H` 与 `H^{-3}` 归类（此处以 `L` 代表前者、`1` 代表后者）。-/
theorem S4_assembly (a b L : ℝ) :
    8 * (a / 3 * L + a / 9 + b / 3) - 2 * (a * L + b)
      = (2 * a / 3) * L + (8 * a / 9 + 2 * b / 3) := by
  ring

end PB

/-- **log 型反常积分**：`∫_H^∞ t^{-4}·log t dt = (1/3)H^{-3}·log H + (1/9)H^{-3}`（`H > e`）。
原函数 `G(t) = -(1/3)(t^{-3}·log t) - (1/9)t^{-3}`，`G' = t^{-4}log t`；
可积性用比较 `log t ≤ t`（`t > 1`）⟹ `t^{-4}log t ≤ t^{-3}`；
极限 `G → 0`（`t^{-3}log t → 0` 由 `log t/t³ → 0`）。-/
theorem integral_Ioi_rpow_neg4_log (H : ℝ) (hH : Real.exp 1 < H) :
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
