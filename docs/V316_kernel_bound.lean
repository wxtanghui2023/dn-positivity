/-
V316 `kernel_bound` 第一层：`kernel_mass`。
数学路线：
  (i)  点态  |s − t| ≤ 1/2 − 2 s t  （s,t ∈ [−1/2,1/2]，角点取等）
  (ii) ∫_{−1/2}^{1/2} t dt = 0      （对称性，用 integral_comp_neg）
  (iii) 故 ∫|s−t| ≤ ∫(1/2 − 2st) = 1/2
-/
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Integral.Prod

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

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **黑盒消费**（不重新展开 `∫|s−t|dt`）：`kernel_mass` 的唯一使用入口。 -/
theorem kernel_mass_black_box {s : ℝ} (hs : s ∈ Icc') :
    ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t| ≤ 1 / 2 := kernel_mass hs

/-- **层 1（`amgm_kernel`）**：点态 AM–GM
`|s−t| |v s| |v t| ≤ (|s−t|/2)(v s² + v t²)`（本质即 `2|ab| ≤ a²+b²` 加 `|s−t| ≥ 0`）。 -/
lemma amgm_kernel (v : ℝ → ℝ) (s t : ℝ) :
    |s - t| * |v s| * |v t| ≤ (|s - t| / 2) * (v s ^ 2 + v t ^ 2) := by
  have h2 : 2 * (|v s| * |v t|) ≤ v s ^ 2 + v t ^ 2 := by
    nlinarith [sq_nonneg (|v s| - |v t|), sq_abs (v s), sq_abs (v t)]
  have h3 : |v s| * |v t| ≤ (v s ^ 2 + v t ^ 2) / 2 := by linarith
  calc |s - t| * |v s| * |v t| = |s - t| * (|v s| * |v t|) := by ring
    _ ≤ |s - t| * ((v s ^ 2 + v t ^ 2) / 2) :=
        mul_le_mul_of_nonneg_left h3 (abs_nonneg _)
    _ = (|s - t| / 2) * (v s ^ 2 + v t ^ 2) := by ring

/-- **层 2（`schur_integrand_bound`）**：把层 1 积分起来。
可积性按唐先生要求**作为显式前提**（不为好看而偷设 `Continuous v`）。 -/
theorem schur_integrand_bound {v : ℝ → ℝ} {μ : Measure ℝ}
    (h1 : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * |v p.1| * |v p.2|) (μ.prod μ))
    (h2 : Integrable (fun p : ℝ × ℝ => (|p.1 - p.2| / 2) * (v p.1 ^ 2 + v p.2 ^ 2)) (μ.prod μ)) :
    ∫ p, |p.1 - p.2| * |v p.1| * |v p.2| ∂(μ.prod μ)
      ≤ ∫ p, (|p.1 - p.2| / 2) * (v p.1 ^ 2 + v p.2 ^ 2) ∂(μ.prod μ) :=
  integral_mono h1 h2 (fun p => amgm_kernel v p.1 p.2)

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- 限制测度（`I × I` 上的 Lebesgue）。 -/
abbrev Irest : Measure ℝ := volume.restrict Icc'

/-- **接口黑盒**：唯一出现 `Icc ↔ 区间积分` 换算的地方。 -/
lemma kernel_mass_restrict {s : ℝ} (hs : s ∈ Icc') :
    ∫ t in Icc', |s - t| ≤ 1 / 2 := by
  unfold Icc' at hs ⊢
  rw [MeasureTheory.integral_Icc_eq_integral_Ioc]
  rw [← intervalIntegral.integral_of_le (show -(1 / 2 : ℝ) ≤ 1 / 2 by norm_num)]
  exact kernel_mass hs

/-- **层 3a（`kernel_sq_left`）**：`T₁ ≤ 1/2 ∫ v²`；**唯一使用 `kernel_mass`**（经接口黑盒）。 -/
theorem kernel_sq_left {v : ℝ → ℝ}
    (h1 : IntervalIntegrable (fun s => v s ^ 2 * (∫ t in Icc', |s - t|)) volume
      (-(1 / 2 : ℝ)) (1 / 2))
    (h2 : IntervalIntegrable (fun s => (1 / 2) * v s ^ 2) volume (-(1 / 2 : ℝ)) (1 / 2)) :
    ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 * (∫ t in Icc', |s - t|)
      ≤ (1 / 2) * ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 := by
  have hpt : ∀ s ∈ Icc (-(1 / 2 : ℝ)) (1 / 2),
      v s ^ 2 * (∫ t in Icc', |s - t|) ≤ (1 / 2) * v s ^ 2 := by
    intro s hs
    have hm : (∫ t in Icc', |s - t|) ≤ 1 / 2 := kernel_mass_restrict hs
    nlinarith [hm, sq_nonneg (v s)]
  have hmain := intervalIntegral.integral_mono_on (a := -(1 / 2 : ℝ)) (b := (1 / 2 : ℝ))
    (show -(1 / 2 : ℝ) ≤ 1 / 2 by norm_num) h1 h2 hpt
  rwa [intervalIntegral.integral_const_mul] at hmain

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **层 3b（`kernel_sq_swap`）**：`T₂ = T₁`（盒子对称）。
停在 restricted measure 层：只用 `Measure.prod` 的对称性与 `abs_sub_comm`，
**不涉及 `intervalIntegral`**。 -/
theorem kernel_sq_swap {v : ℝ → ℝ}
    (hInt : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 ^ 2) (Irest.prod Irest)) :
    ∫ p, |p.1 - p.2| * v p.2 ^ 2 ∂(Irest.prod Irest)
      = ∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest) := by
  have hpt : ∀ p : ℝ × ℝ, |p.1 - p.2| * v p.2 ^ 2
      = (fun q : ℝ × ℝ => |q.1 - q.2| * v q.1 ^ 2) p.swap := by
    intro p
    show |p.1 - p.2| * v p.2 ^ 2 = |p.2 - p.1| * v p.2 ^ 2
    rw [abs_sub_comm]
  calc ∫ p, |p.1 - p.2| * v p.2 ^ 2 ∂(Irest.prod Irest)
      = ∫ p, (fun q : ℝ × ℝ => |q.1 - q.2| * v q.1 ^ 2) p.swap ∂(Irest.prod Irest) :=
        MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall hpt)
    _ = ∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest) :=
        MeasureTheory.integral_prod_swap (μ := Irest) (ν := Irest)
          (f := fun q : ℝ × ℝ => |q.1 - q.2| * v q.1 ^ 2)

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **`schur_L2`**：`∬_{I×I} |s−t||v s||v t| ≤ (1/2)∫_I v²`。
组合层：只拼接已通过的 4 条 lemma；measure conversion 只在此处做一次。
可积性**显式前提**（不引入 `Continuous v`，把正则性留给 `Q_pos` 自决）。 -/
theorem schur_L2 {v : ℝ → ℝ}
    (h1 : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * |v p.1| * |v p.2|) (Irest.prod Irest))
    (h2 : Integrable (fun p : ℝ × ℝ => (|p.1 - p.2| / 2) * (v p.1 ^ 2 + v p.2 ^ 2)) (Irest.prod Irest))
    (hA : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 ^ 2) (Irest.prod Irest))
    (hB : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.2 ^ 2) (Irest.prod Irest))
    (hF : IntervalIntegrable (fun s => v s ^ 2 * (∫ t in Icc', |s - t|)) volume
      (-(1 / 2 : ℝ)) (1 / 2))
    (hG : IntervalIntegrable (fun s => (1 / 2) * v s ^ 2) volume (-(1 / 2 : ℝ)) (1 / 2)) :
    ∫ p, |p.1 - p.2| * |v p.1| * |v p.2| ∂(Irest.prod Irest)
      ≤ (1 / 2) * ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 := by
  have step1 := schur_integrand_bound (μ := Irest) h1 h2
  have hsplit : ∫ p, (|p.1 - p.2| / 2) * (v p.1 ^ 2 + v p.2 ^ 2) ∂(Irest.prod Irest)
      = (1 / 2) * (∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest)
          + ∫ p, |p.1 - p.2| * v p.2 ^ 2 ∂(Irest.prod Irest)) := by
    rw [← MeasureTheory.integral_add hA hB, ← MeasureTheory.integral_const_mul]
    exact MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall fun p => by ring)
  have hBA : ∫ p, |p.1 - p.2| * v p.2 ^ 2 ∂(Irest.prod Irest)
      = ∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest) := kernel_sq_swap (v := v) hA
  have hTon : ∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest)
      = ∫ s, v s ^ 2 * (∫ t, |s - t| ∂Irest) ∂Irest := by
    rw [MeasureTheory.integral_prod (f := fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 ^ 2) hA]
    refine MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall fun s => ?_)
    show (∫ y, |s - y| * v s ^ 2 ∂Irest) = v s ^ 2 * ∫ t, |s - t| ∂Irest
    rw [← MeasureTheory.integral_const_mul]
    exact MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall fun t => by ring)
  have hconv : ∫ s, v s ^ 2 * (∫ t, |s - t| ∂Irest) ∂Irest
      = ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 * (∫ t in Icc', |s - t|) := by
    have hL : ∫ s, v s ^ 2 * (∫ t, |s - t| ∂Irest) ∂Irest
        = ∫ s in Icc', v s ^ 2 * (∫ t in Icc', |s - t|) := rfl
    rw [hL]
    unfold Icc'
    rw [MeasureTheory.integral_Icc_eq_integral_Ioc]
    rw [← intervalIntegral.integral_of_le (show -(1 / 2 : ℝ) ≤ 1 / 2 by norm_num)]
  have hleft := kernel_sq_left (v := v) hF hG
  calc ∫ p, |p.1 - p.2| * |v p.1| * |v p.2| ∂(Irest.prod Irest)
      ≤ ∫ p, (|p.1 - p.2| / 2) * (v p.1 ^ 2 + v p.2 ^ 2) ∂(Irest.prod Irest) := step1
    _ = (1 / 2) * (∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest)
          + ∫ p, |p.1 - p.2| * v p.2 ^ 2 ∂(Irest.prod Irest)) := hsplit
    _ = (1 / 2) * (∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest)
          + ∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest)) := by rw [hBA]
    _ = ∫ p, |p.1 - p.2| * v p.1 ^ 2 ∂(Irest.prod Irest) := by ring
    _ = ∫ s, v s ^ 2 * (∫ t, |s - t| ∂Irest) ∂Irest := hTon
    _ = ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 * (∫ t in Icc', |s - t|) := hconv
    _ ≤ (1 / 2) * ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 := hleft

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **`kernel_bound`**：`|B(v)| ≤ (1/2)∫_I v²`，其中 `B(v) = ∬ |s−t| v(s) v(t)`。
依赖链**极短**：积分三角不等式 → 点态绝对值归一 → `schur_L2`。
（不重新触碰 `kernel_mass` / Tonelli / `kernel_sq_swap` —— 它们已封装进 `schur_L2`。） -/
theorem kernel_bound {v : ℝ → ℝ}
    (hmain : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * v p.2) (Irest.prod Irest))
    (habs : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * |v p.1| * |v p.2|) (Irest.prod Irest))
    (h2 : Integrable (fun p : ℝ × ℝ => (|p.1 - p.2| / 2) * (v p.1 ^ 2 + v p.2 ^ 2)) (Irest.prod Irest))
    (hA : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 ^ 2) (Irest.prod Irest))
    (hB : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.2 ^ 2) (Irest.prod Irest))
    (hF : IntervalIntegrable (fun s => v s ^ 2 * (∫ t in Icc', |s - t|)) volume
      (-(1 / 2 : ℝ)) (1 / 2))
    (hG : IntervalIntegrable (fun s => (1 / 2) * v s ^ 2) volume (-(1 / 2 : ℝ)) (1 / 2)) :
    |∫ p, |p.1 - p.2| * v p.1 * v p.2 ∂(Irest.prod Irest)|
      ≤ (1 / 2) * ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 := by
  -- 第一段：积分三角不等式（Bochner 版，实数上即 |∫f| ≤ ∫|f|）
  have h1 : |∫ p, |p.1 - p.2| * v p.1 * v p.2 ∂(Irest.prod Irest)|
      ≤ ∫ p, |(|p.1 - p.2| * v p.1 * v p.2)| ∂(Irest.prod Irest) := by
    simpa only [Real.norm_eq_abs] using
      norm_integral_le_integral_norm (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * v p.2)
  -- 点态绝对值归一（基础 abs 引理，**不用 AM–GM**）
  have h2' : ∫ p, |(|p.1 - p.2| * v p.1 * v p.2)| ∂(Irest.prod Irest)
      = ∫ p, |p.1 - p.2| * |v p.1| * |v p.2| ∂(Irest.prod Irest) := by
    refine MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall fun p => ?_)
    simp only [abs_mul, abs_abs]
  -- 第二段：直接消费 schur_L2
  calc |∫ p, |p.1 - p.2| * v p.1 * v p.2 ∂(Irest.prod Irest)|
      ≤ ∫ p, |(|p.1 - p.2| * v p.1 * v p.2)| ∂(Irest.prod Irest) := h1
    _ = ∫ p, |p.1 - p.2| * |v p.1| * |v p.2| ∂(Irest.prod Irest) := h2'
    _ ≤ (1 / 2) * ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2 := schur_L2 habs h2 hA hB hF hG

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **`Q_pos`**：`Q_λ(v) = ‖v‖² + λ²B(v) ≥ (1/2)‖v‖²`（`0 < λ ≤ 1`）。
V316 中**第一次正式引入 `λ ≤ 1`**。显式两段链，不用 `linarith/nlinarith` 处理混合乘积：
`(1/2)N ≤ N − (1/2)λ²N ≤ N + λ²B`，其中 `N = ∫_I v²`，`B = ∬|s−t|v(s)v(t)`。 -/
theorem Q_pos_alg {N B lam : ℝ} (h0 : 0 < lam) (h1 : lam ≤ 1) (hN : 0 ≤ N)
    (hb : |B| ≤ (1 / 2) * N) : (1 / 2) * N ≤ N + lam ^ 2 * B := by
  have hb1 : -(1 / 2) * N ≤ B := by linarith [(abs_le.mp hb).1]
  have hlam0 : 0 ≤ lam ^ 2 := sq_nonneg lam
  have key : lam ^ 2 * (-(1 / 2) * N) ≤ lam ^ 2 * B :=
    mul_le_mul_of_nonneg_left hb1 hlam0
  have hlam1 : lam ^ 2 ≤ 1 := by nlinarith [h0, h1]
  have hNlam : lam ^ 2 * N ≤ 1 * N := mul_le_mul_of_nonneg_right hlam1 hN
  nlinarith [key, hNlam, hN, hlam0]

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

-- 诊断：elaborated 类型（若 Q_pos 失败，用它与目标逐字比对）
#check @Q_pos_alg

/-- **`Q_pos`**：`Q_λ(v) = ‖v‖² + λ²B(v) ≥ (1/2)‖v‖²`（`0 < λ ≤ 1`）。
statement **直接对齐 `Q_pos_alg` 的结论形状**；body 只负责把 `N, B` 实例化。 -/
theorem Q_pos {v : ℝ → ℝ} {lam : ℝ} (h0 : 0 < lam) (h1 : lam ≤ 1)
    (hN : 0 ≤ ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2)
    (hb : |∫ p, |p.1 - p.2| * v p.1 * v p.2 ∂(Irest.prod Irest)|
      ≤ (1 / 2) * ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2) :
    (1 / 2 : ℝ) * (∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2)
      ≤ (∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2)
        + lam ^ 2 * (∫ p, |p.1 - p.2| * v p.1 * v p.2 ∂(Irest.prod Irest)) := by
  have hQ := Q_pos_alg (N := ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2)
    (B := ∫ p, |p.1 - p.2| * v p.1 * v p.2 ∂(Irest.prod Irest)) h0 h1 hN hb
  exact hQ

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- `θ_λ = λ/√2`（本文件自足定义；项目自身 olean 未生成 ⟹ 不能 import ThmD 模块）。 -/
noncomputable def vtheta (lam : ℝ) : ℝ := lam / Real.sqrt 2

/-- **仿射截距 `C_λ = β = sin ϑ/(√2 λ) + cos ϑ/λ²`**（`ϑ = θ_λ = λ/√2`）。
      语义：`Kv_λ = C_λ·1 − λ⁻²v_λ` 中的**截距**。**严禁**与 `c*_λ` 混用。 -/
noncomputable def vStarAffineConst (lam : ℝ) : ℝ :=
  Real.sin (vtheta lam) / (Real.sqrt 2 * lam) + Real.cos (vtheta lam) / lam ^ 2

/-- **E–L 常数 `D_λ = λ²C_λ`**。`(I + λ²K)v_λ = D_λ·1` 中的常数。**注意 `D_λ ≠ c*_λ`**。 -/
noncomputable def vStarELConst (lam : ℝ) : ℝ := lam ^ 2 * vStarAffineConst lam

/-- 三层关系之一：`D_λ = cos ϑ + ϑ sin ϑ`（`ϑ = λ/√2`）。 -/
theorem vStarELConst_eq {lam : ℝ} (h : lam ≠ 0) :
    vStarELConst lam = Real.cos (vtheta lam) + vtheta lam * Real.sin (vtheta lam) := by
  have hs : Real.sqrt 2 ≠ 0 := by positivity
  have h2 : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  unfold vStarELConst vStarAffineConst vtheta
  field_simp
  nlinarith [h2]

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **原函数引理 ①**：`∫_x^y cos(a t) dt = (sin(a y) − sin(a x))/a`（`a ≠ 0`）。 -/
theorem cos_integral {a x y : ℝ} (ha : a ≠ 0) :
    ∫ t in x..y, Real.cos (a * t) = (Real.sin (a * y) - Real.sin (a * x)) / a := by
  have hderiv : ∀ z ∈ uIcc x y,
      HasDerivAt (fun t : ℝ => Real.sin (a * t) / a) (Real.cos (a * z)) z := by
    intro z _
    have hlin : HasDerivAt (fun t : ℝ => a * t) a z := hasDerivAt_const_mul a
    have h1 : HasDerivAt (fun t : ℝ => Real.sin (a * t)) (Real.cos (a * z) * a) z :=
      (Real.hasDerivAt_sin (a * z)).comp z hlin
    have h2 := h1.div_const a
    have hval : Real.cos (a * z) * a / a = Real.cos (a * z) := by field_simp
    rwa [hval] at h2
  have hint : IntervalIntegrable (fun t : ℝ => Real.cos (a * t)) volume x y :=
    (by continuity : Continuous fun t : ℝ => Real.cos (a * t)).intervalIntegrable _ _
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]
  ring

/-- **原函数引理 ②**：`∫_x^y t cos(a t) dt = [t sin(a t)/a + cos(a t)/a²]_x^y`（`a ≠ 0`）。
`KvStar_affine` 的计算核心。 -/
theorem t_cos_integral {a x y : ℝ} (ha : a ≠ 0) :
    ∫ t in x..y, t * Real.cos (a * t)
      = y * Real.sin (a * y) / a + Real.cos (a * y) / a ^ 2
        - (x * Real.sin (a * x) / a + Real.cos (a * x) / a ^ 2) := by
  have hderiv : ∀ z ∈ uIcc x y,
      HasDerivAt (fun t : ℝ => t * Real.sin (a * t) / a + Real.cos (a * t) / a ^ 2)
        (z * Real.cos (a * z)) z := by
    intro z _
    have hlin : HasDerivAt (fun t : ℝ => a * t) a z := hasDerivAt_const_mul a
    have hsin : HasDerivAt (fun t : ℝ => Real.sin (a * t)) (Real.cos (a * z) * a) z :=
      (Real.hasDerivAt_sin (a * z)).comp z hlin
    have hcos : HasDerivAt (fun t : ℝ => Real.cos (a * t)) (-Real.sin (a * z) * a) z :=
      (Real.hasDerivAt_cos (a * z)).comp z hlin
    have h1 : HasDerivAt (fun t : ℝ => t * Real.sin (a * t))
        (Real.sin (a * z) + z * (Real.cos (a * z) * a)) z := by
      have hh := (hasDerivAt_id z).mul hsin
      have hfun : (id * fun t : ℝ => Real.sin (a * t)) = fun t : ℝ => t * Real.sin (a * t) := by
        funext t
        simp [id]
      have hval1 : (1 * Real.sin (a * z) + id z * (Real.cos (a * z) * a))
          = Real.sin (a * z) + z * (Real.cos (a * z) * a) := by
        simp [id]
      rw [hfun, hval1] at hh
      exact hh
    have h2 : HasDerivAt (fun t : ℝ => t * Real.sin (a * t) / a)
        ((Real.sin (a * z) + z * (Real.cos (a * z) * a)) / a) z := h1.div_const a
    have h3 : HasDerivAt (fun t : ℝ => Real.cos (a * t) / a ^ 2)
        ((-Real.sin (a * z) * a) / a ^ 2) z := hcos.div_const (a ^ 2)
    have hval : (Real.sin (a * z) + z * (Real.cos (a * z) * a)) / a
        + (-Real.sin (a * z) * a) / a ^ 2 = z * Real.cos (a * z) := by
      field_simp [ha, pow_ne_zero 2 ha]
      ring
    have h4 := h2.add h3
    rw [hval] at h4
    exact h4
  have hint : IntervalIntegrable (fun t : ℝ => t * Real.cos (a * t)) volume x y :=
    (by continuity : Continuous fun t : ℝ => t * Real.cos (a * t)).intervalIntegrable _ _
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hint]

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- 端点形状规范化 ①：`a * (1/2) = a/2`（共享，避免各 theorem 内重复证明）。 -/
theorem mul_half (a : ℝ) : a * (1 / 2 : ℝ) = a / 2 := by ring

/-- 端点形状规范化 ②：`a * (-(1/2)) = -(a/2)`。 -/
theorem mul_neg_half (a : ℝ) : a * (-(1 / 2 : ℝ)) = -(a / 2) := by ring

/-- **`KvStar_left`**：`L_a(s) = ∫_{−1/2}^{s} (s−t)cos(at)dt`
`= s sin(a/2)/a + sin(a/2)/(2a) − cos(as)/a² + cos(a/2)/a²`。 -/
theorem KvStar_left {a s : ℝ} (ha : a ≠ 0) :
    ∫ t in (-(1 / 2 : ℝ))..s, (s - t) * Real.cos (a * t)
      = s * Real.sin (a / 2) / a + Real.sin (a / 2) / (2 * a)
        - Real.cos (a * s) / a ^ 2 + Real.cos (a / 2) / a ^ 2 := by
  have hcos := cos_integral (a := a) (x := -(1 / 2 : ℝ)) (y := s) ha
  rw [mul_neg_half] at hcos
  rw [Real.sin_neg] at hcos
  have hcos' : ∫ t in (-(1 / 2 : ℝ))..s, Real.cos (a * t)
      = (Real.sin (a * s) + Real.sin (a / 2)) / a := by
    rw [hcos]; ring
  have htc := t_cos_integral (a := a) (x := -(1 / 2 : ℝ)) (y := s) ha
  rw [mul_neg_half] at htc
  rw [Real.sin_neg, Real.cos_neg] at htc
  have htc' : ∫ t in (-(1 / 2 : ℝ))..s, t * Real.cos (a * t)
      = s * Real.sin (a * s) / a + Real.cos (a * s) / a ^ 2
        - Real.sin (a / 2) / (2 * a) - Real.cos (a / 2) / a ^ 2 := by
    rw [htc]; ring
  have hsplit : ∫ t in (-(1 / 2 : ℝ))..s, (s - t) * Real.cos (a * t)
      = s * (∫ t in (-(1 / 2 : ℝ))..s, Real.cos (a * t))
        - ∫ t in (-(1 / 2 : ℝ))..s, t * Real.cos (a * t) := by
    have h1 : ∫ t in (-(1 / 2 : ℝ))..s, s * Real.cos (a * t)
        = s * ∫ t in (-(1 / 2 : ℝ))..s, Real.cos (a * t) :=
      intervalIntegral.integral_const_mul s (fun t : ℝ => Real.cos (a * t))
    have h2 : ∫ t in (-(1 / 2 : ℝ))..s, (s * Real.cos (a * t) - t * Real.cos (a * t))
        = (∫ t in (-(1 / 2 : ℝ))..s, s * Real.cos (a * t))
          - ∫ t in (-(1 / 2 : ℝ))..s, t * Real.cos (a * t) :=
      intervalIntegral.integral_sub
        ((by continuity : Continuous fun t : ℝ => s * Real.cos (a * t)).intervalIntegrable _ _)
        ((by continuity : Continuous fun t : ℝ => t * Real.cos (a * t)).intervalIntegrable _ _)
    have h3 : ∫ t in (-(1 / 2 : ℝ))..s, (s - t) * Real.cos (a * t)
        = ∫ t in (-(1 / 2 : ℝ))..s, (s * Real.cos (a * t) - t * Real.cos (a * t)) := by
      refine intervalIntegral.integral_congr fun t _ => ?_
      ring
    rw [h3, h2, h1]
  rw [hsplit, hcos', htc']
  field_simp [ha, pow_ne_zero 2 ha]
  ring

/-- **`KvStar_right`**：`R_a(s) = ∫_s^{1/2} (t−s)cos(at)dt`
`= −s sin(a/2)/a + sin(a/2)/(2a) − cos(as)/a² + cos(a/2)/a²`（区间方向按纸面 `s..1/2`）。 -/
theorem KvStar_right {a s : ℝ} (ha : a ≠ 0) :
    ∫ t in s..(1 / 2 : ℝ), (t - s) * Real.cos (a * t)
      = -(s * Real.sin (a / 2) / a) + Real.sin (a / 2) / (2 * a)
        - Real.cos (a * s) / a ^ 2 + Real.cos (a / 2) / a ^ 2 := by
  have hcos := cos_integral (a := a) (x := s) (y := (1 / 2 : ℝ)) ha
  rw [mul_half] at hcos
  have hcos' : ∫ t in s..(1 / 2 : ℝ), Real.cos (a * t)
      = (Real.sin (a / 2) - Real.sin (a * s)) / a := hcos
  have htc := t_cos_integral (a := a) (x := s) (y := (1 / 2 : ℝ)) ha
  rw [mul_half] at htc
  have htc' : ∫ t in s..(1 / 2 : ℝ), t * Real.cos (a * t)
      = Real.sin (a / 2) / (2 * a) + Real.cos (a / 2) / a ^ 2
        - (s * Real.sin (a * s) / a + Real.cos (a * s) / a ^ 2) := by
    rw [htc]; ring
  have hsplit : ∫ t in s..(1 / 2 : ℝ), (t - s) * Real.cos (a * t)
      = (∫ t in s..(1 / 2 : ℝ), t * Real.cos (a * t))
        - s * (∫ t in s..(1 / 2 : ℝ), Real.cos (a * t)) := by
    have h1 : ∫ t in s..(1 / 2 : ℝ), s * Real.cos (a * t)
        = s * ∫ t in s..(1 / 2 : ℝ), Real.cos (a * t) :=
      intervalIntegral.integral_const_mul s (fun t : ℝ => Real.cos (a * t))
    have h2 : ∫ t in s..(1 / 2 : ℝ), (t * Real.cos (a * t) - s * Real.cos (a * t))
        = (∫ t in s..(1 / 2 : ℝ), t * Real.cos (a * t))
          - ∫ t in s..(1 / 2 : ℝ), s * Real.cos (a * t) :=
      intervalIntegral.integral_sub
        ((by continuity : Continuous fun t : ℝ => t * Real.cos (a * t)).intervalIntegrable _ _)
        ((by continuity : Continuous fun t : ℝ => s * Real.cos (a * t)).intervalIntegrable _ _)
    have h3 : ∫ t in s..(1 / 2 : ℝ), (t - s) * Real.cos (a * t)
        = ∫ t in s..(1 / 2 : ℝ), (t * Real.cos (a * t) - s * Real.cos (a * t)) := by
      refine intervalIntegral.integral_congr fun t _ => ?_
      ring
    rw [h3, h2, h1]
  rw [hsplit, hcos', htc']
  field_simp [ha, pow_ne_zero 2 ha]
  ring

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **abs 拆分**：`∫_{−1/2}^{1/2}|s−t|cos(at) = ∫_{−1/2}^{s}(s−t)cos(at) + ∫_s^{1/2}(t−s)cos(at)`。 -/
theorem KvStar_abs_split {a s : ℝ} (hs1 : -(1 / 2 : ℝ) ≤ s) (hs2 : s ≤ 1 / 2) :
    ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t| * Real.cos (a * t)
      = (∫ t in (-(1 / 2 : ℝ))..s, (s - t) * Real.cos (a * t))
        + ∫ t in s..(1 / 2), (t - s) * Real.cos (a * t) := by
  have h1 : ∫ t in (-(1 / 2 : ℝ))..s, |s - t| * Real.cos (a * t)
      = ∫ t in (-(1 / 2 : ℝ))..s, (s - t) * Real.cos (a * t) := by
    refine intervalIntegral.integral_congr fun t ht => ?_
    rcases ht with ⟨ht1, ht2⟩
    have hts : t ≤ s := by
      have h := ht2
      rwa [max_eq_right hs1] at h
    rw [abs_of_nonneg (by linarith : (0:ℝ) ≤ s - t)]
  have h2 : ∫ t in s..(1 / 2), |s - t| * Real.cos (a * t)
      = ∫ t in s..(1 / 2), (t - s) * Real.cos (a * t) := by
    refine intervalIntegral.integral_congr fun t ht => ?_
    rcases ht with ⟨ht1, ht2⟩
    have hst : s ≤ t := by
      have h := ht1
      rwa [min_eq_left hs2] at h
    rw [abs_of_nonpos (by linarith : s - t ≤ 0)]
    ring
  have hf : IntervalIntegrable (fun t : ℝ => |s - t| * Real.cos (a * t)) volume
      (-(1 / 2 : ℝ)) s :=
    (by continuity : Continuous fun t : ℝ => |s - t| * Real.cos (a * t)).intervalIntegrable _ _
  have hg : IntervalIntegrable (fun t : ℝ => |s - t| * Real.cos (a * t)) volume
      s (1 / 2 : ℝ) :=
    (by continuity : Continuous fun t : ℝ => |s - t| * Real.cos (a * t)).intervalIntegrable _ _
  have hadd := intervalIntegral.integral_add_adjacent_intervals
    (μ := volume) (a := -(1 / 2 : ℝ)) (b := s) (c := (1 / 2 : ℝ))
    (f := fun t : ℝ => |s - t| * Real.cos (a * t)) hf hg
  rw [← hadd, h1, h2]

/-- **$a$-层恒等式**：`∫_{−1/2}^{1/2}|s−t|cos(at) = sin(a/2)/a + 2cos(a/2)/a² − 2cos(as)/a²`。 -/
theorem KvStar_affine_general {a s : ℝ} (ha : a ≠ 0)
    (hs1 : -(1 / 2 : ℝ) ≤ s) (hs2 : s ≤ 1 / 2) :
    ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t| * Real.cos (a * t)
      = Real.sin (a / 2) / a + 2 * Real.cos (a / 2) / a ^ 2
        - 2 * Real.cos (a * s) / a ^ 2 := by
  rw [KvStar_abs_split hs1 hs2, KvStar_left ha, KvStar_right ha]
  ring

/-- **`KvStar_affine`**：`Kv_λ(s) = C_λ − λ⁻²v_λ(s)`（只证 $C_λ$ 层，不碰 `vStarELConst`）。 -/
theorem KvStar_affine {lam s : ℝ} (h0 : 0 < lam)
    (hs1 : -(1 / 2 : ℝ) ≤ s) (hs2 : s ≤ 1 / 2) :
    ∫ t in (-(1 / 2 : ℝ))..(1 / 2), |s - t| * Real.cos (Real.sqrt 2 * lam * t)
      = vStarAffineConst lam - Real.cos (Real.sqrt 2 * lam * s) / lam ^ 2 := by
  have hsqrt : Real.sqrt 2 ≠ 0 := by positivity
  have ha : Real.sqrt 2 * lam ≠ 0 := mul_ne_zero hsqrt (ne_of_gt h0)
  have ha_sq : (Real.sqrt 2 * lam) ^ 2 = 2 * lam ^ 2 := by
    rw [mul_pow, Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)]
  have hhalf : (Real.sqrt 2 * lam) / 2 = vtheta lam := by
    unfold vtheta
    field_simp
    nlinarith [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)]
  rw [KvStar_affine_general ha hs1 hs2]
  rw [hhalf, ha_sq]
  unfold vStarAffineConst
  field_simp [ne_of_gt h0]
  try ring

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **`vStar_EL`**：E–L 方程 `v_λ(s) + λ²(Kv_λ)(s) = D_λ`，
其中 `v_λ(s) = cos(√2 λ s)`，`D_λ = vStarELConst λ = λ²C_λ`。
**不引入新积分引理**：只代入 `KvStar_affine` ＋ 展开 `vStarELConst` ＋ 纯代数。 -/
theorem vStar_EL {lam s : ℝ} (h0 : 0 < lam)
    (hs1 : -(1 / 2 : ℝ) ≤ s) (hs2 : s ≤ 1 / 2) :
    Real.cos (Real.sqrt 2 * lam * s)
      + lam ^ 2 * (∫ t in (-(1 / 2 : ℝ))..(1 / 2),
          |s - t| * Real.cos (Real.sqrt 2 * lam * t))
      = vStarELConst lam := by
  have hlam : lam ≠ 0 := ne_of_gt h0
  rw [KvStar_affine h0 hs1 hs2]
  unfold vStarELConst vStarAffineConst
  field_simp [hlam]
  try ring

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **① 接线**：`kernel_bound ⟹ |B| ≤ ½N ⟹ Q_pos` —— V316-A 自洽闭环。
不包任何抽象层，直接消费两条已 CLOSED 的定理。 -/
theorem kernel_bound_to_Q_pos {v : ℝ → ℝ} {lam : ℝ} (h0 : 0 < lam) (h1 : lam ≤ 1)
    (hN : 0 ≤ ∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2)
    (hmain : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * v p.2) (Irest.prod Irest))
    (habs : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * |v p.1| * |v p.2|) (Irest.prod Irest))
    (h2 : Integrable (fun p : ℝ × ℝ => (|p.1 - p.2| / 2) * (v p.1 ^ 2 + v p.2 ^ 2)) (Irest.prod Irest))
    (hA : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 ^ 2) (Irest.prod Irest))
    (hB : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.2 ^ 2) (Irest.prod Irest))
    (hF : IntervalIntegrable (fun s => v s ^ 2 * (∫ t in Icc', |s - t|)) volume
      (-(1 / 2 : ℝ)) (1 / 2))
    (hG : IntervalIntegrable (fun s => (1 / 2) * v s ^ 2) volume (-(1 / 2 : ℝ)) (1 / 2)) :
    (1 / 2 : ℝ) * (∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2)
      ≤ (∫ s in (-(1 / 2 : ℝ))..(1 / 2), v s ^ 2)
        + lam ^ 2 * (∫ p, |p.1 - p.2| * v p.1 * v p.2 ∂(Irest.prod Irest)) :=
  Q_pos h0 h1 hN (kernel_bound hmain habs h2 hA hB hF hG)

/-- **② `Qfun` 定义**：只封装现有二次型，**不引入** `B`／inner product／operator／Hilbert 空间。
与 `Q_pos` 中的表达式**逐字对齐**。 -/
noncomputable def Qfun (lam : ℝ) (u : ℝ → ℝ) : ℝ :=
  (∫ s in (-(1 / 2 : ℝ))..(1 / 2), u s ^ 2)
    + lam ^ 2 * (∫ p, |p.1 - p.2| * u p.1 * u p.2 ∂(Irest.prod Irest))

/-- **③-a 点态极化（纯代数层）**：`u(s)u(t) − v(s)v(t) = v(s)(u(t)−v(t)) + (u(s)−v(s))v(t) + (u(s)−v(s))(u(t)−v(t))`。 -/
theorem pol_pointwise (u v : ℝ → ℝ) (s t : ℝ) :
    u s * u t - v s * v t
      = v s * (u t - v t) + (u s - v s) * v t + (u s - v s) * (u t - v t) := by
  ring

/-- **③-b 点态极化（核对）**：核加权版，直接供下一轮积分层使用（`h = u − v`）。 -/
theorem pol_pointwise_kernel (u v : ℝ → ℝ) (s t : ℝ) :
    |s - t| * (u s * u t) - |s - t| * (v s * v t)
      = |s - t| * (v s * (u t - v t)) + |s - t| * ((u s - v s) * v t)
        + |s - t| * ((u s - v s) * (u t - v t)) := by
  ring

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **③″-0 记号**：核双线性式（仅 def，**非新数学对象**；`u,w` 为函数、核 `|s−t|`）。
注意 `Bfun u w = ∬ K(s,t) u(s) w(t)`，而 `Bfun w u = ∬ K(s,t) w(s) u(t)`。 -/
noncomputable def Bfun (u w : ℝ → ℝ) : ℝ :=
  ∫ p, |p.1 - p.2| * u p.1 * w p.2 ∂(Irest.prod Irest)

/-- **③″ 交叉项换序（product-measure symmetry，不引入 Fubini）**：
`Bfun v h = Bfun h v`，即 `∬K(s,t)v(s)h(t) = ∬K(s,t)h(s)v(t)`。
骨架复用已 CLOSED 的 `kernel_sq_swap`：`integral_prod_swap` ＋ `abs_sub_comm`。 -/
theorem Bfun_symm {v h : ℝ → ℝ}
    (hint : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * h p.2) (Irest.prod Irest)) :
    Bfun v h = Bfun h v := by
  have hpt : ∀ p : ℝ × ℝ, |p.1 - p.2| * v p.1 * h p.2
      = (fun q : ℝ × ℝ => |q.1 - q.2| * h q.1 * v q.2) p.swap := by
    intro p
    show |p.1 - p.2| * v p.1 * h p.2 = |p.2 - p.1| * h p.2 * v p.1
    rw [abs_sub_comm]
    ring
  unfold Bfun
  calc ∫ p, |p.1 - p.2| * v p.1 * h p.2 ∂(Irest.prod Irest)
      = ∫ p, (fun q : ℝ × ℝ => |q.1 - q.2| * h q.1 * v q.2) p.swap
          ∂(Irest.prod Irest) :=
        MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall hpt)
    _ = ∫ p, |p.1 - p.2| * h p.1 * v p.2 ∂(Irest.prod Irest) :=
        MeasureTheory.integral_prod_swap (μ := Irest) (ν := Irest)
          (f := fun q : ℝ × ℝ => |q.1 - q.2| * h q.1 * v q.2)

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **③′ 积分极化（方案 (b)：不分拆）**：
`B(u,u) − B(v,v) = ∫ p, [ K·v(p₁)(u(p₂)−v(p₂)) + K·(u(p₁)−v(p₁))v(p₂) + K·(u(p₁)−v(p₁))(u(p₂)−v(p₂)) ]`，
`K(p) = |p.1 − p.2|`。只需 `hUU`/`hVV`；**不用 `integral_add`**（少一组可积性接口，更稳）。
证明绕开函数相等 rw：`← integral_sub` 后用 `integral_congr_ae` ＋ 点态 `ring`。 -/
theorem Bfun_polarization {u v : ℝ → ℝ}
    (hUU : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * u p.1 * u p.2) (Irest.prod Irest))
    (hVV : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * v p.2) (Irest.prod Irest)) :
    Bfun u u - Bfun v v
      = ∫ p, (|p.1 - p.2| * v p.1 * (u p.2 - v p.2)
          + |p.1 - p.2| * (u p.1 - v p.1) * v p.2
          + |p.1 - p.2| * (u p.1 - v p.1) * (u p.2 - v p.2)) ∂(Irest.prod Irest) := by
  unfold Bfun
  rw [← MeasureTheory.integral_sub hUU hVV]
  exact MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall (fun p => by ring))

end Zeta23.ThmD.V316

namespace Zeta23.ThmD.V316

open MeasureTheory

/-- **`Bfun_quadratic_gap`**：`B(u,u) − B(v,v) = 2B(v,h) + B(h,h)`，`h = u − v`。
路线：`Bfun_polarization` → 拆三项（`integral_add`）→ `Bfun_symm` 换序 → `ring`。
可积性**显式列出**（`hC`/`hD`/`hE`），与文件既有风格一致。 -/
theorem Bfun_quadratic_gap {u v : ℝ → ℝ}
    (hUU : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * u p.1 * u p.2) (Irest.prod Irest))
    (hVV : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * v p.2) (Irest.prod Irest))
    (hC : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * (u p.2 - v p.2))
      (Irest.prod Irest))
    (hD : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * (u p.1 - v p.1) * v p.2)
      (Irest.prod Irest))
    (hE : Integrable (fun p : ℝ × ℝ => |p.1 - p.2| * (u p.1 - v p.1) * (u p.2 - v p.2))
      (Irest.prod Irest)) :
    Bfun u u - Bfun v v
      = 2 * Bfun v (fun t => u t - v t)
        + Bfun (fun t => u t - v t) (fun t => u t - v t) := by
  have hpol := Bfun_polarization (u := u) (v := v) hUU hVV
  have hsym := Bfun_symm (v := v) (h := fun t => u t - v t) hC
  have hsplit : ∫ p, (|p.1 - p.2| * v p.1 * (u p.2 - v p.2)
        + |p.1 - p.2| * (u p.1 - v p.1) * v p.2
        + |p.1 - p.2| * (u p.1 - v p.1) * (u p.2 - v p.2)) ∂(Irest.prod Irest)
      = Bfun v (fun t => u t - v t) + Bfun (fun t => u t - v t) v
        + Bfun (fun t => u t - v t) (fun t => u t - v t) := by
    show ∫ p, (((fun p : ℝ × ℝ => |p.1 - p.2| * v p.1 * (u p.2 - v p.2))
            + fun p : ℝ × ℝ => |p.1 - p.2| * (u p.1 - v p.1) * v p.2) p
          + (fun p : ℝ × ℝ => |p.1 - p.2| * (u p.1 - v p.1) * (u p.2 - v p.2)) p)
        ∂(Irest.prod Irest)
      = Bfun v (fun t => u t - v t) + Bfun (fun t => u t - v t) v
        + Bfun (fun t => u t - v t) (fun t => u t - v t)
    rw [MeasureTheory.integral_add (hC.add hD) hE]
    show ∫ p, (|p.1 - p.2| * v p.1 * (u p.2 - v p.2)
            + |p.1 - p.2| * (u p.1 - v p.1) * v p.2) ∂(Irest.prod Irest)
          + ∫ p, |p.1 - p.2| * (u p.1 - v p.1) * (u p.2 - v p.2) ∂(Irest.prod Irest)
        = Bfun v (fun t => u t - v t) + Bfun (fun t => u t - v t) v
          + Bfun (fun t => u t - v t) (fun t => u t - v t)
    rw [MeasureTheory.integral_add hC hD]
    unfold Bfun
    rfl
  rw [hpol, hsplit, ← hsym]
  ring

end Zeta23.ThmD.V316
