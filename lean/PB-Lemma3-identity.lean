/-
Paper B · Lemma 3（near）之【恒等式部分】—— Lean 4 形式化
论文陈述：令 v(t) = (k/2)·log(1+t^{-2})，则 F(1+t^{-2}) = 4 sinh²(v(t)/2)。
本文件证明其一般形式：F(1+u) = 4 sinh²( (k/2)·log(1+u) / 2 )。
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

namespace PB

/-- **指数—双曲恒等式**（与 `PB-Basic.lean` 同，此处重复以便单文件编译）。-/
theorem exp_sinh_identity (v : ℝ) :
    Real.exp v - 2 + Real.exp (-v) = 4 * Real.sinh (v / 2) ^ 2 := by
  have h1 : Real.exp v = Real.exp (v / 2) * Real.exp (v / 2) := by
    rw [← Real.exp_add]
    ring_nf
  have h2 : Real.exp (-v) = Real.exp (-(v / 2)) * Real.exp (-(v / 2)) := by
    rw [← Real.exp_add]
    ring_nf
  have hprod : Real.exp (v / 2) * Real.exp (-(v / 2)) = 1 := by
    rw [← Real.exp_add, show v / 2 + -(v / 2) = 0 by ring, Real.exp_zero]
  rw [Real.sinh_eq, h1, h2]
  nlinarith [hprod]

/-- **论文 Lemma 3 的恒等式部分**：
`(1+u)^{k/2} + (1+u)^{-k/2} - 2 = 4 sinh²( ((k/2)·log(1+u)) / 2 )`，对 `1+u > 0`。-/
theorem F_eq_sinh (k u : ℝ) (hu : 0 < 1 + u) :
    (1 + u) ^ (k / 2) + (1 + u) ^ (-(k / 2)) - 2
      = 4 * Real.sinh ((k / 2) * Real.log (1 + u) / 2) ^ 2 := by
  -- 幂 → 指数
  have h1 : (1 + u) ^ (k / 2) = Real.exp (Real.log (1 + u) * (k / 2)) :=
    Real.rpow_def_of_pos hu (k / 2)
  have h2 : (1 + u) ^ (-(k / 2)) = Real.exp (-(Real.log (1 + u) * (k / 2))) := by
    rw [Real.rpow_def_of_pos hu (-(k / 2))]
    ring_nf
  -- 化为 exp 形式后套用指数—双曲恒等式
  have hgoal : (1 + u) ^ (k / 2) + (1 + u) ^ (-(k / 2)) - 2
      = Real.exp (Real.log (1 + u) * (k / 2)) - 2
        + Real.exp (-(Real.log (1 + u) * (k / 2))) := by
    rw [h1, h2]
    ring
  rw [hgoal, exp_sinh_identity]
  have harg : Real.log (1 + u) * (k / 2) / 2 = (k / 2) * Real.log (1 + u) / 2 := by ring
  rw [harg]


/-- **论文 Lemma 3 的比值恒等式**：归一化剖面恰为双曲正弦之比。
（分母非零由 `hsinh` 给出。）-/
theorem F_ratio (k t H : ℝ)
    (ht : 0 < 1 + t ^ (-(2 : ℝ))) (hH : 0 < 1 + H ^ (-(2 : ℝ)))
    (hsinh : Real.sinh ((k / 2) * Real.log (1 + H ^ (-(2 : ℝ))) / 2) ≠ 0) :
    ((1 + t ^ (-(2 : ℝ))) ^ (k / 2) + (1 + t ^ (-(2 : ℝ))) ^ (-(k / 2)) - 2)
        / ((1 + H ^ (-(2 : ℝ))) ^ (k / 2) + (1 + H ^ (-(2 : ℝ))) ^ (-(k / 2)) - 2)
      = (Real.sinh ((k / 2) * Real.log (1 + t ^ (-(2 : ℝ))) / 2)
          / Real.sinh ((k / 2) * Real.log (1 + H ^ (-(2 : ℝ))) / 2)) ^ 2 := by
  rw [F_eq_sinh k (t ^ (-(2 : ℝ))) ht, F_eq_sinh k (H ^ (-(2 : ℝ))) hH]
  field_simp

end PB
