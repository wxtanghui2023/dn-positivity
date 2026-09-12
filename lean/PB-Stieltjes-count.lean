/-
Paper B · 桥的第 ③′ 步【有限多零点版】—— Lean 4 形式化
**核心结论**：Σᵢ g(γᵢ) = ∫ g d(计数测度) ✓✓
即「对零点求和」= 「对计数测度积分」—— 论文 S₄(H) = ∫_H^∞ t⁻⁴ d(2N(t)) 的形式化基础 ✓。
-/
import Mathlib.MeasureTheory.Measure.Stieltjes
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Topology.Order.LeftRightLim

open MeasureTheory Filter
open scoped Topology

namespace PB

/-- 单原子计数函数：`x ≥ γ` 时为 `1` ✓。-/
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
    · refine (tendsto_const_nhds).congr' ?_
      filter_upwards [self_mem_nhdsWithin] with y hy
      simp only [Set.mem_Ici] at hy
      simp only [if_pos h, if_pos (le_trans h hy)]
    · have hmem : Set.Iio γ ∈ 𝓝[Set.Ici x] x :=
        nhdsWithin_le_nhds ((isOpen_Iio (a := γ)).mem_nhds h)
      refine (tendsto_const_nhds).congr' ?_
      filter_upwards [hmem] with y hy
      simp only [if_neg (not_le.mpr h), if_neg (not_le.mpr (Set.mem_Iio.mp hy))]

/-- `stepAt γ` 按定义展开 ✓。-/
@[simp] theorem stepAt_apply (γ x : ℝ) : ((stepAt γ) : ℝ → ℝ) x = if γ ≤ x then 1 else 0 := rfl

/-- **左侧极限为 0** ✓（`y < γ` 时函数恒为 0 ✓）。-/
theorem leftLim_stepAt (γ : ℝ) : Function.leftLim (stepAt γ) γ = 0 := by
  refine leftLim_eq_of_tendsto ?_
  refine (tendsto_const_nhds).congr' ?_
  filter_upwards [self_mem_nhdsWithin] with y hy
  simp only [Set.mem_Iio] at hy
  show (0 : ℝ) = (if γ ≤ y then (1 : ℝ) else 0)
  rw [if_neg (not_le.mpr hy)]

/-- **测度在原子处 = 1** ✓。-/
theorem measure_singleton_stepAt (γ : ℝ) : (stepAt γ).measure {γ} = 1 := by
  rw [StieltjesFunction.measure_singleton, leftLim_stepAt]
  have h : ((stepAt γ) : ℝ → ℝ) γ = 1 := by
    show (if γ ≤ γ then (1 : ℝ) else 0) = 1
    rw [if_pos le_rfl]
  rw [h, sub_zero]
  exact ENNReal.ofReal_one

/-- ★ **单原子计数测度 = Dirac 测度** ✓。-/
theorem measure_stepAt_eq_dirac (γ : ℝ) : (stepAt γ).measure = Measure.dirac γ := by
  refine Measure.ext_of_Ioc _ _ ?_
  intro a b hab
  rw [StieltjesFunction.measure_Ioc]
  simp only [stepAt_apply]
  by_cases h : γ ∈ Set.Ioc a b
  · rw [Set.mem_Ioc] at h
    have hd : (Measure.dirac γ) (Set.Ioc a b) = 1 := Measure.dirac_apply_of_mem h
    rw [hd, if_pos h.2, if_neg (not_le.mpr h.1)]
    simp
  · have hconj : ¬ (a < γ ∧ γ ≤ b) := by simpa [Set.mem_Ioc] using h
    rw [Measure.dirac_apply' _ measurableSet_Ioc,
      Set.indicator_of_notMem (by intro hc; exact h hc)]
    by_cases hga : γ ≤ a
    · rw [if_pos hga, if_pos (le_trans hga hab.le)]
      simp
    · have hbγ : b < γ := by
        by_contra hnb
        exact hconj ⟨not_le.mp hga, not_lt.mp hnb⟩
      rw [if_neg hga, if_neg (not_le.mpr hbγ)]
      simp

/-- 有限多个零点的**计数函数** ✓（`stepAt` 之和 ✓）。-/
noncomputable def countFn {ι : Type*} (s : Finset ι) (γ : ι → ℝ) : StieltjesFunction ℝ :=
  ∑ i ∈ s, stepAt (γ i)

/-- ★ **计数测度 = Dirac 之和** ✓（`measure_add` 归纳 ✓）。-/
theorem measure_countFn {ι : Type*} (s : Finset ι) (γ : ι → ℝ) :
    (countFn s γ).measure = ∑ i ∈ s, Measure.dirac (γ i) := by
  classical
  induction s using Finset.induction with
  | empty => simp [countFn]
  | insert a s ha ih =>
    have ih' : (∑ i ∈ s, stepAt (γ i)).measure = ∑ i ∈ s, Measure.dirac (γ i) := ih
    rw [countFn, Finset.sum_insert ha, Finset.sum_insert ha, StieltjesFunction.measure_add,
      ih', measure_stepAt_eq_dirac]

/-- ★★ **桥的最终结论（论文 S₄ 的形式化基础）**：
**对零点求和 = 对计数测度积分** ✓✓
`Σᵢ g(γᵢ) = ∫ g d(计数测度)` ✓。-/
theorem integral_countFn {ι : Type*} (s : Finset ι) (γ : ι → ℝ) (g : ℝ → ℝ)
    (hint : ∀ i ∈ s, Integrable g (Measure.dirac (γ i))) :
    ∫ x, g x ∂(countFn s γ).measure = ∑ i ∈ s, g (γ i) := by
  rw [measure_countFn, integral_finsetSum_measure hint]
  simp only [integral_dirac]

end PB
