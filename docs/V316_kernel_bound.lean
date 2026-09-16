/-
V316 `kernel_bound` 第一层：`kernel_mass`。
数学路线：
  (i)  点态  |s − t| ≤ 1/2 − 2 s t  （s,t ∈ [−1/2,1/2]，角点取等）
  (ii) ∫_{−1/2}^{1/2} t dt = 0      （对称性，用 integral_comp_neg）
  (iii) 故 ∫|s−t| ≤ ∫(1/2 − 2st) = 1/2
-/
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic

open MeasureTheory Set intervalIntegral
open scoped Real

noncomputable section

namespace Zeta23.ThmD.V316

def Icc' : Set ℝ := Set.Icc (-(1 / 2 : ℝ)) (1 / 2)

/-- 双线性版：`s - t + 2 s t ≤ 1/2`（盒约束下）。 -/
lemma bilin_le {s t : ℝ} (hs1 : -(1 / 2 : ℝ) ≤ s) (hs2 : s ≤ 1 / 2)
    (ht1 : -(1 / 2 : ℝ) ≤ t) (ht2 : t ≤ 1 / 2) : s - t + 2 * s * t ≤ 1 / 2 := by
  by_cases ht : 0 ≤ t
  · have h2s : 2 * s - 1 ≤ 0 := by linarith
    have hmul : t * (2 * s - 1) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos ht h2s
    nlinarith [hmul]
  · have htneg : t < 0 := lt_of_not_ge ht
    have hu2 : -t ≤ 1 / 2 := by linarith
    have h1m : 0 ≤ 1 - 2 * s := by linarith
    have hmul : (-t) * (1 - 2 * s) ≤ (1 / 2) * (1 - 2 * s) :=
      mul_le_mul_of_nonneg_right hu2 h1m
    nlinarith [hmul]

/-- 点态不等式：`|s − t| ≤ 1/2 − 2 s t`。 -/
lemma abs_sub_le_half_sub_two_mul {s t : ℝ} (hs : |s| ≤ 1 / 2) (ht : |t| ≤ 1 / 2) :
    |s - t| ≤ 1 / 2 - 2 * s * t := by
  have hs' : -(1 / 2 : ℝ) ≤ s ∧ s ≤ 1 / 2 := by rw [abs_le] at hs; exact hs
  have ht' : -(1 / 2 : ℝ) ≤ t ∧ t ≤ 1 / 2 := by rw [abs_le] at ht; exact ht
  rw [abs_le]
  constructor
  · have h := bilin_le ht'.1 ht'.2 hs'.1 hs'.2
    linarith
  · have h := bilin_le hs'.1 hs'.2 ht'.1 ht'.2
    linarith

/-- `∫_{-1/2}^{1/2} t dt = 0`。 -/
lemma integral_self_zero : ∫ t in (-(1 / 2 : ℝ))..(1 / 2), t = 0 := by
  have h : ∫ t in (-(1 / 2 : ℝ))..(1 / 2), t
      = ∫ t in (-(1 / 2 : ℝ))..(1 / 2), (-t) := by
    rw [intervalIntegral.integral_comp_neg (f := fun t : ℝ => t)]
    norm_num
  rw [intervalIntegral.integral_neg] at h
  linarith

/-- **(kernel_mass)**：`∀ s ∈ [−1/2,1/2]，∫_t |s − t| ≤ 1/2`。 -/
theorem kernel_mass {s : ℝ} (hs : s ∈ Icc') :
    ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t| ≤ 1 / 2 := by
  have hs' : |s| ≤ 1 / 2 := by
    rcases hs with ⟨h1, h2⟩
    rw [abs_le]
    exact ⟨h1, h2⟩
  have hpt : ∀ t ∈ Icc (-(1 / 2 : ℝ)) (1 / 2), |s - t| ≤ 1 / 2 - 2 * s * t := by
    intro t ht
    rw [Set.mem_Icc] at ht
    exact abs_sub_le_half_sub_two_mul hs' (by rw [abs_le]; exact ⟨ht.1, ht.2⟩)
  have hcont1 : Continuous fun t : ℝ => |s - t| := by continuity
  have hcont2 : Continuous fun t : ℝ => 1 / 2 - 2 * s * t := by continuity
  have hmain : ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t|
      ≤ ∫ t in (-(1 / 2 : ℝ))..(1 / 2), (1 / 2 - 2 * s * t) :=
    intervalIntegral.integral_mono_on (a := -(1 / 2 : ℝ)) (b := (1 / 2 : ℝ))
      (by norm_num) (hcont1.intervalIntegrable _ _) (hcont2.intervalIntegrable _ _) hpt
  have hval : ∫ t in (-(1 / 2 : ℝ))..(1 / 2), (1 / 2 - 2 * s * t) = 1 / 2 := by
    have hI1 : IntervalIntegrable (fun _ : ℝ => (1 / 2 : ℝ)) volume (-(1 / 2 : ℝ)) (1 / 2) :=
      continuous_const.intervalIntegrable _ _
    have hI2 : IntervalIntegrable (fun t : ℝ => 2 * s * t) volume (-(1 / 2 : ℝ)) (1 / 2) :=
      (by continuity : Continuous fun t : ℝ => 2 * s * t).intervalIntegrable _ _
    rw [intervalIntegral.integral_sub hI1 hI2, intervalIntegral.integral_const]
    have hmul : ∫ t in (-(1 / 2 : ℝ))..(1 / 2), (2 * s * t)
        = (2 * s) * ∫ t in (-(1 / 2 : ℝ))..(1 / 2), t :=
      intervalIntegral.integral_const_mul (2 * s) (fun t : ℝ => t)
    rw [hmul, integral_self_zero]
    ring
  linarith [hmain, hval]

end Zeta23.ThmD.V316
