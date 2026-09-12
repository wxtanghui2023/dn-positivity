/-
Paper B · Lemma 3（near）之【sinh x / x 单调性】—— Lean 4 形式化
论文用到：sinh x / x 在 [0,∞) 上递增（Mathlib 无此引理，需自证）。
路线：设 g(x) = x·cosh x − sinh x，g' = x·sinh x > 0 ⟹ g 在 [0,∞) 严格增 ⟹ g > g(0) = 0；
      再对 φ(x) = sinh x / x 用 φ' = g(x)/x² > 0 ⟹ φ 严格增。
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.Calculus.MeanValue

namespace PB

/-- `g(x) = x·cosh x − sinh x > 0` 对 `x > 0`。-/
theorem mul_cosh_sub_sinh_pos (x : ℝ) (hx : 0 < x) :
    0 < x * Real.cosh x - Real.sinh x := by
  have hmono : StrictMonoOn (fun y : ℝ => y * Real.cosh y - Real.sinh y) (Set.Ici 0) := by
    refine strictMonoOn_of_deriv_pos (convex_Ici 0) ?_ ?_
    · refine Continuous.continuousOn ?_
      fun_prop
    · intro y hy
      rw [interior_Ici] at hy
      have hd : deriv (fun z : ℝ => z * Real.cosh z - Real.sinh z) y = y * Real.sinh y := by
        have h1 : HasDerivAt (fun z : ℝ => z * Real.cosh z)
            (1 * Real.cosh y + y * Real.sinh y) y :=
          (hasDerivAt_id y).mul (Real.hasDerivAt_cosh y)
        have h2 : HasDerivAt Real.sinh (Real.cosh y) y := Real.hasDerivAt_sinh y
        have h3 : HasDerivAt (fun z : ℝ => z * Real.cosh z - Real.sinh z)
            (1 * Real.cosh y + y * Real.sinh y - Real.cosh y) y := h1.sub h2
        rw [h3.deriv]
        ring
      rw [hd]
      exact mul_pos hy (Real.sinh_pos_iff.mpr hy)
  have h := hmono (Set.mem_Ici.mpr le_rfl) (Set.mem_Ici.mpr hx.le) hx
  simpa using h

/-- **`sinh x / x` 在 `x > 0` 上严格递增**（论文 Lemma 3 所需）。-/
theorem sinh_div_strictMonoOn : StrictMonoOn (fun x : ℝ => Real.sinh x / x) (Set.Ioi 0) := by
  refine strictMonoOn_of_deriv_pos (convex_Ioi 0) ?_ ?_
  · refine ContinuousOn.div ?_ ?_ ?_
    · fun_prop
    · fun_prop
    · intro x hx
      exact ne_of_gt hx
  · intro x hx
    rw [interior_Ioi] at hx
    have hd : deriv (fun y : ℝ => Real.sinh y / y) x
        = (x * Real.cosh x - Real.sinh x) / x ^ 2 := by
      have h1 : HasDerivAt Real.sinh (Real.cosh x) x := Real.hasDerivAt_sinh x
      have h2 : HasDerivAt (fun y : ℝ => y) 1 x := hasDerivAt_id x
      have h3 : HasDerivAt (fun y : ℝ => Real.sinh y / y)
          ((Real.cosh x * x - Real.sinh x * 1) / x ^ 2) x := h1.div h2 (ne_of_gt hx)
      rw [h3.deriv]
      ring
    rw [hd]
    exact div_pos (mul_cosh_sub_sinh_pos x hx) (pow_pos hx 2)

end PB
