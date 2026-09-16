/-
V316 `kernel_bound` 第一层：`kernel_mass`。
数学路线：
  (i)  点态  |s − t| ≤ 1/2 − 2 s t  （s,t ∈ [−1/2,1/2]，角点取等）
  (ii) ∫_{−1/2}^{1/2} t dt = 0      （对称性，用 integral_comp_neg）
  (iii) 故 ∫|s−t| ≤ ∫(1/2 − 2st) = 1/2
-/
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
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
