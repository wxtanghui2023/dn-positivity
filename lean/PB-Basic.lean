/-
Paper B（Brown Thm 2 经典情形）基础引理 —— Lean 4 形式化
2026-09-12 起，逐条形式化，每条即时编译验证。
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace PB

/-- **代数恒等式**（论文 Lemma 1 的基础）：
`x^{k/2} + x^{-k/2} - 2 = (x^{k/4} - x^{-k/4})^2`，对 `x > 0`。

证法：记 `A = x^{k/4}`，`B = x^{-k/4}`。用 `Real.rpow_add` 得
`A·A = x^{k/2}`、`B·B = x^{-k/2}`、`A·B = 1`；再展开右边平方即可。 -/
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

/-- **指数—双曲恒等式**（论文 Lemma 3 的基础）：
`e^v - 2 + e^{-v} = 4 sinh^2(v/2)`。-/
theorem exp_sinh_identity (v : ℝ) :
    Real.exp v - 2 + Real.exp (-v) = 4 * Real.sinh (v / 2) ^ 2 := by
  have h1 : Real.exp v = Real.exp (v / 2) * Real.exp (v / 2) := by
    rw [← Real.exp_add]
    ring_nf
  have h2 : Real.exp (-v) = Real.exp (-(v / 2)) * Real.exp (-(v / 2)) := by
    rw [← Real.exp_add]
    ring_nf
  -- 关键补充：e^{v/2} · e^{-v/2} = 1
  have hprod : Real.exp (v / 2) * Real.exp (-(v / 2)) = 1 := by
    rw [← Real.exp_add, show v / 2 + -(v / 2) = 0 by ring, Real.exp_zero]
  rw [Real.sinh_eq, h1, h2]
  nlinarith [hprod]

end PB
