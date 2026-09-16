/-
V316 `kernel_bound` 第一块：|B v| ≤ 1/2 ∫v²，拆成三层（唐先生 2026-09-16 14:22 指令）
  kernel_mass  : ∀ s ∈ I, ∫ t in I, |s − t| ≤ 1/2
  schur_L2     : ∬ |s−t| |v s| |v t| ≤ (1/2) ∫ v²
  kernel_bound : |B v| ≤ (1/2) ∫ v²
数学路线（避免抽象 Schur 算子理论）：
  (a) m(s) := ∫_I |s−t| dt = s² + 1/4 ≤ 1/2   （kernel_mass）
  (b) AM–GM: |v s| |v t| ≤ (v s² + v t²)/2
  (c) Tonelli + 对称性: ∬|s−t||vs||vt| ≤ ∬|s−t|(vs²+vt²)/2 = ∫ vs² m(s) ds ≤ (1/2)∫v²
本文件为**首块编译测试**，只求编译通过。
-/
import Mathlib.MeasureTheory.Integral.IntervalIntegral
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

open MeasureTheory Set intervalIntegral
open scoped Real

noncomputable section

namespace Zeta23.ThmD.V316

/-- 区间 I := [−1/2, 1/2]。 -/
def Icc' : Set ℝ := Set.Icc (-(1 / 2 : ℝ)) (1 / 2)

/-- **(kernel_mass)** 核算子的行质量：对 `s ∈ [−1/2,1/2]`，`∫_t |s−t| ≤ 1/2`。
证明：`∫_{−1/2}^{1/2}|s−t|dt = s² + 1/4 ≤ 1/2`（用 `|s| ≤ 1/2` 得 `s² ≤ 1/4`）。 -/
theorem kernel_mass {s : ℝ} (hs : s ∈ Icc') :
    ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t| ≤ 1 / 2 := by
  have hs' : |s| ≤ 1 / 2 := by
    rcases hs with ⟨h1, h2⟩
    rw [abs_le]
    exact ⟨h1, h2⟩
  -- 先证积分值 = s^2 + 1/4
  have hsplit : ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t|
      = ∫ t in (-(1 / 2 : ℝ))..s, (s - t) + ∫ t in s..(1 / 2), (t - s) := by
    rw [← intervalIntegral.integral_add_adjacent_intervals (c := s)]
    · refine intervalIntegral.integral_congr fun t ht => ?_
      rcases ht with ⟨ht1, ht2⟩
      rw [abs_of_nonneg]
      linarith
    · refine intervalIntegral.integral_congr fun t ht => ?_
      rcases ht with ⟨ht1, ht2⟩
      rw [abs_of_nonpos]
      · ring
      · linarith
  have h1 : ∫ t in (-(1 / 2 : ℝ))..s, (s - t) = (s + 1 / 2) ^ 2 / 2 := by
    have h : ∀ t : ℝ, s - t = -(t - s) := fun t => by ring
    simp only [h]
    rw [integral_neg]
    rw [integral_sub]
    · simp; ring
    · exact intervalIntegral.intervalIntegrable_const
    · exact intervalIntegral.intervalIntegrable_id
  have h2 : ∫ t in s..(1 / 2), (t - s) = (1 / 2 - s) ^ 2 / 2 := by
    rw [integral_sub]
    · simp; ring
    · exact intervalIntegral.intervalIntegrable_id
    · exact intervalIntegral.intervalIntegrable_const
  rw [hsplit, h1, h2]
  nlinarith [sq_nonneg (s + 1 / 2), sq_nonneg (1 / 2 - s), sq_nonneg s, hs',
             abs_nonneg s, sq_abs s]

end Zeta23.ThmD.V316
