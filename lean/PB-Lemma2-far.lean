/-
Paper B · Lemma 2（far）—— Lean 4 形式化
论文陈述：F(1+u) ≤ (k²/4)u²(1+u)^{(k-4)/2}
思路：F(x) = (x^{k/2}-1)²/x^{k/2}（x=1+u），再对 x^{k/2}-1 用 MVT 型引理。
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Pow.Continuity
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.Convex.Deriv

namespace PB

/-- 代数恒等式（与 `PB-Basic.lean` 同）。-/
theorem F_eq_sq (x : ℝ) (hx : 0 < x) (k : ℝ) :
    x ^ (k / 2) + x ^ (-(k / 2)) - 2 = (x ^ (k / 4) - x ^ (-(k / 4))) ^ 2 := by
  have hAA : x ^ (k / 4) * x ^ (k / 4) = x ^ (k / 2) := by
    rw [← Real.rpow_add hx, show k / 4 + k / 4 = k / 2 by ring]
  have hBB : x ^ (-(k / 4)) * x ^ (-(k / 4)) = x ^ (-(k / 2)) := by
    rw [← Real.rpow_add hx, show -(k / 4) + -(k / 4) = -(k / 2) by ring]
  have hAB : x ^ (k / 4) * x ^ (-(k / 4)) = 1 := by
    rw [← Real.rpow_add hx, show k / 4 + -(k / 4) = 0 by ring, Real.rpow_zero]
  have hexp : (x ^ (k / 4) - x ^ (-(k / 4))) ^ 2
      = x ^ (k / 4) * x ^ (k / 4) - 2 * (x ^ (k / 4) * x ^ (-(k / 4)))
        + x ^ (-(k / 4)) * x ^ (-(k / 4)) := by ring
  rw [hexp, hAA, hBB, hAB]
  ring

/-- MVT 型幂增长界（见 `PB-Lemma2-mvt.lean`）。-/
theorem rpow_sub_one_le_mul (a x : ℝ) (ha : 1 ≤ a) (hx : 1 ≤ x) :
    x ^ a - 1 ≤ a * (x - 1) * x ^ (a - 1) := by
  rcases lt_or_eq_of_le hx with hx' | rfl
  · rcases lt_or_eq_of_le ha with ha' | rfl
    · have hcont : ContinuousOn (fun t : ℝ => t ^ a) (Set.Icc 1 x) := by
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
    · simp
  · simp

/-- **论文 Lemma 2（far）主不等式**：`k ≥ 2`，`u ≥ 0` ⟹
`F(1+u) ≤ (k²/4)·u²·(1+u)^{(k-4)/2}`。-/
theorem F_far (k u : ℝ) (hk : 2 ≤ k) (hu : 0 ≤ u) :
    (1 + u) ^ (k / 2) + (1 + u) ^ (-(k / 2)) - 2
      ≤ (k ^ 2 / 4) * u ^ 2 * (1 + u) ^ ((k - 4) / 2) := by
  have hx : 0 < 1 + u := by linarith
  have hx1 : 1 ≤ 1 + u := by linarith
  have hk1 : 1 ≤ k / 2 := by linarith
  have hkp : 0 < (1 + u) ^ (k / 2) := Real.rpow_pos_of_pos hx _
  -- ① F(1+u) = ((1+u)^{k/2} - 1)^2 / (1+u)^{k/2}
  have hform : (1 + u) ^ (k / 2) + (1 + u) ^ (-(k / 2)) - 2
      = ((1 + u) ^ (k / 2) - 1) ^ 2 / (1 + u) ^ (k / 2) := by
    rw [F_eq_sq (1 + u) hx k]
    have hA2 : ((1 + u) ^ (k / 4)) ^ 2 = (1 + u) ^ (k / 2) := by
      rw [sq, ← Real.rpow_add hx, show k / 4 + k / 4 = k / 2 by ring]
    have hB : (1 + u) ^ (-(k / 4)) = ((1 + u) ^ (k / 4))⁻¹ :=
      Real.rpow_neg (le_of_lt hx) (k / 4)
    have hAne : (1 + u) ^ (k / 4) ≠ 0 := ne_of_gt (Real.rpow_pos_of_pos hx _)
    rw [hB, ← hA2]
    field_simp
  rw [hform]
  -- ② MVT 型引理
  have hbound : (1 + u) ^ (k / 2) - 1 ≤ k / 2 * ((1 + u) - 1) * (1 + u) ^ (k / 2 - 1) :=
    rpow_sub_one_le_mul (k / 2) (1 + u) hk1 hx1
  have hnonneg : 0 ≤ (1 + u) ^ (k / 2) - 1 := by
    have h1 : (1 : ℝ) ≤ (1 + u) ^ (k / 2) := Real.one_le_rpow hx1 (by linarith)
    linarith
  -- ③ 平方（两边非负）
  have hsq_exp : ((1 + u) ^ (k / 2 - 1)) ^ 2 = (1 + u) ^ (k - 2) := by
    rw [sq, ← Real.rpow_add hx, show k / 2 - 1 + (k / 2 - 1) = k - 2 by ring]
  have hmid : ((1 + u) ^ (k / 2) - 1) ^ 2
      ≤ (k / 2 * ((1 + u) - 1) * (1 + u) ^ (k / 2 - 1)) ^ 2 := by
    have hA : 0 ≤ k / 2 := by linarith
    have hB : 0 ≤ (1 + u) - 1 := by linarith
    have hC : 0 ≤ (1 + u) ^ (k / 2 - 1) := Real.rpow_nonneg (le_of_lt hx) _
    nlinarith [hbound, hnonneg, hA, hB, hC]
  have hsq : ((1 + u) ^ (k / 2) - 1) ^ 2
      ≤ (k ^ 2 / 4) * u ^ 2 * (1 + u) ^ (k - 2) := by
    refine le_trans hmid (le_of_eq ?_)
    rw [show (1 + u) - 1 = u by ring]
    rw [mul_pow, mul_pow, hsq_exp]
    ring
  -- ④ 除以 (1+u)^{k/2}
  have hdiv := div_le_div_of_nonneg_right hsq (le_of_lt hkp)
  refine le_trans hdiv (le_of_eq ?_)
  rw [mul_div_assoc, ← Real.rpow_sub hx]
  rw [show k - 2 - k / 2 = (k - 4) / 2 by ring]

end PB
