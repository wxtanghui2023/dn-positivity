/-
Paper B · 连续版 Abel 的【桥】—— Lean 4 形式化（第一步）
用 `StieltjesFunction.measure` 把"零点计数函数"变成真正的测度 ✓。
本文件：证明单原子计数函数是合法的 `StieltjesFunction` ✓（单调 + 右连续 ✓）。
-/
import Mathlib.MeasureTheory.Measure.Stieltjes
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Topology.Order.LeftRightLim

open MeasureTheory Filter
open scoped Topology

namespace PB

/-- 单原子计数函数：`x ≥ γ` 时为 `1`，否则 `0`（表示"一个零点 γ"）✓。-/
noncomputable def stepAt (γ : ℝ) : StieltjesFunction ℝ where
  toFun := fun x => if γ ≤ x then 1 else 0
  mono' := by
    intro a b hab
    by_cases ha : γ ≤ a
    · simp [ha, le_trans ha hab]
    · by_cases hb : γ ≤ b
      · simp [ha, hb]
      · simp [ha, hb]
  right_continuous' := by
    intro x
    rcases le_or_gt γ x with h | h
    · -- x ≥ γ：在 x 的右侧邻域内取常值 1 ✓
      refine (tendsto_const_nhds).congr' ?_
      filter_upwards [self_mem_nhdsWithin] with y hy
      simp only [Set.mem_Ici] at hy
      simp only [if_pos h, if_pos (le_trans h hy)]
    · -- x < γ：在 x 附近（靠 γ 那侧）取常值 0 ✓
      have hmem : Set.Iio γ ∈ 𝓝[Set.Ici x] x :=
        nhdsWithin_le_nhds ((isOpen_Iio (a := γ)).mem_nhds h)
      refine (tendsto_const_nhds).congr' ?_
      filter_upwards [hmem] with y hy
      simp only [if_neg (not_le.mpr h), if_neg (not_le.mpr (Set.mem_Iio.mp hy))]

/-- **桥的第 ② 步之一**：`stepAt γ` 在 `γ` 处的**左侧极限为 0** ✓
（因 `y < γ` 时函数恒为 0 ✓）。-/
theorem leftLim_stepAt (γ : ℝ) : Function.leftLim (stepAt γ) γ = 0 := by
  refine leftLim_eq_of_tendsto ?_
  refine (tendsto_const_nhds).congr' ?_
  filter_upwards [self_mem_nhdsWithin] with y hy
  simp only [Set.mem_Iio] at hy
  show (0 : ℝ) = (if γ ≤ y then (1 : ℝ) else 0)
  rw [if_neg (not_le.mpr hy)]

/-- **桥的第 ② 步之二（关键）**：计数测度在原子处为 **1** ✓✓
即 `(stepAt γ).measure {γ} = 1` —— **"一个零点贡献一份质量"** ✓。-/
theorem measure_singleton_stepAt (γ : ℝ) : (stepAt γ).measure {γ} = 1 := by
  rw [StieltjesFunction.measure_singleton, leftLim_stepAt]
  have h : ((stepAt γ) : ℝ → ℝ) γ = 1 := by
    show (if γ ≤ γ then (1 : ℝ) else 0) = 1
    rw [if_pos le_rfl]
  rw [h, sub_zero]
  exact ENNReal.ofReal_one

/-- `stepAt γ` 作为函数按定义展开 ✓（便于化简 ✓）。-/
@[simp] theorem stepAt_apply (γ x : ℝ) : ((stepAt γ) : ℝ → ℝ) x = if γ ≤ x then 1 else 0 := rfl

/-- **桥的第 ③ 步之一**：计数测度**就是 Dirac 测度** ✓（单原子情形 ✓）。-/
theorem measure_stepAt_eq_dirac (γ : ℝ) : (stepAt γ).measure = Measure.dirac γ := by
  refine Measure.ext_of_Ioc _ _ ?_
  intro a b hab
  rw [StieltjesFunction.measure_Ioc]
  simp only [stepAt_apply]
  by_cases h : γ ∈ Set.Ioc a b
  · -- γ ∈ (a,b] ✓：左 = 1−0 = 1 ✓，右 = 1 ✓
    rw [Set.mem_Ioc] at h
    have hd : (Measure.dirac γ) (Set.Ioc a b) = 1 := Measure.dirac_apply_of_mem h
    rw [hd, if_pos h.2, if_neg (not_le.mpr h.1)]
    simp
  · -- case 2: gamma not in (a,b]
    have hconj : ¬ (a < γ ∧ γ ≤ b) := by
      simpa [Set.mem_Ioc] using h
    rw [Measure.dirac_apply' _ measurableSet_Ioc,
      Set.indicator_of_notMem (by intro hc; exact h hc)]
    by_cases hga : γ ≤ a
    · -- case: gamma <= a
      rw [if_pos hga, if_pos (le_trans hga hab.le)]
      simp
    · -- case: a < gamma, hence b < gamma by hconj
      have hbγ : b < γ := by
        by_contra hnb
        exact hconj ⟨not_le.mp hga, not_lt.mp hnb⟩
      rw [if_neg hga, if_neg (not_le.mpr hbγ)]
      simp

end PB
