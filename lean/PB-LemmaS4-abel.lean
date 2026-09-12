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
    have h := (tendsto_rpow_neg_atTop (show (0:ℝ) < 3 by norm_num)).const_mul (-(1 / 3))
    simpa [one_div] using h
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
