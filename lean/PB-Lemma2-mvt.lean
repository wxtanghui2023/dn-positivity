/-
Paper B · Lemma 2（far）所需之【MVT 型引理】—— Lean 4 形式化
论文的 far 界等价于：a ≥ 1, x ≥ 1 ⟹ x^a - 1 ≤ a(x-1)x^{a-1}
（由 convexOn_rpow + 割线-导数比较 + MVT 得到）
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.Convex.Deriv

namespace PB

/-- **MVT 型幂增长界**：`a ≥ 1`，`x ≥ 1` ⟹ `x^a - 1 ≤ a(x-1)x^{a-1}`。

证明：`t ↦ t^a` 在 `[1,x]` 上连续、其导数 `t ↦ a t^{a-1}` 在 `(1,x)` 上严格增，
故由割线-导数比较（`StrictMonoOn.exists_slope_lt_deriv`）得内部点 `c` 使
`(x^a-1)/(x-1) < a c^{a-1} < a x^{a-1}`，再乘正数 `x-1` 即得。 -/
theorem rpow_sub_one_le_mul (a x : ℝ) (ha : 1 ≤ a) (hx : 1 ≤ x) :
    x ^ a - 1 ≤ a * (x - 1) * x ^ (a - 1) := by
  rcases lt_or_eq_of_le hx with hx' | rfl
  · rcases lt_or_eq_of_le ha with ha' | rfl
    · -- 主情形：a > 1, x > 1
      have hcont : ContinuousOn (fun t : ℝ => t ^ a) (Set.Icc 1 x) := by
        refine ContinuousOn.rpow_const ?_ ?_
        · fun_prop
        · intro t ht
          right
          linarith [ha]
      have hderiv_mono : StrictMonoOn (deriv (fun t : ℝ => t ^ a)) (Set.Ioo 1 x) := by
        intro s hs t ht hst
        have hs0 : s ≠ 0 := by linarith [hs.1]
        have ht0 : t ≠ 0 := by linarith [ht.1]
        rw [(Real.hasDerivAt_rpow_const (Or.inl hs0)).deriv,
            (Real.hasDerivAt_rpow_const (Or.inl ht0)).deriv]
        have hpow : s ^ (a - 1) < t ^ (a - 1) :=
          Real.rpow_lt_rpow (by linarith [hs.1]) hst (by linarith)
        nlinarith [hpow, ha]
      obtain ⟨c, hc, hlt⟩ := StrictMonoOn.exists_slope_lt_deriv hcont hx' hderiv_mono
      have hc0 : c ≠ 0 := by linarith [hc.1]
      rw [(Real.hasDerivAt_rpow_const (Or.inl hc0)).deriv] at hlt
      have hcx : c ^ (a - 1) < x ^ (a - 1) :=
        Real.rpow_lt_rpow (by linarith [hc.1]) hc.2 (by linarith)
      have hpos : 0 < x - 1 := by linarith
      have hacx : a * c ^ (a - 1) < a * x ^ (a - 1) :=
        mul_lt_mul_of_pos_left hcx (by linarith)
      have h1 : (x ^ a - 1 ^ a) / (x - 1) < a * x ^ (a - 1) := hlt.trans hacx
      rw [div_lt_iff₀ hpos, Real.one_rpow] at h1
      nlinarith [h1]
    · -- a = 1：两边相等
      simp
  · -- x = 1：两边相等
    simp

end PB
