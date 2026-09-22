/-
  A2 层（Fermat 两平方）——**只做结构实例化**：其数论内容（鸽笼／模约化／Brahmagupta／整除性）
  以**显式假设**承载（本环境无 Mathlib，未做数论形式化）。
  关键：`derive_Target` 与 `reenter_P` **分离**；h : ¬Target **只**用于 reenter_P。
-/
import Std
import TLDC.Core
import TLDC.Interface

namespace TLDC.Instances.A2

/-- **derive_Target**（不含任何反证假设 h）：由 A2 恒等式 m′ = 1 直接得目标。 -/
theorem derive_Target (p A B m' : Nat) (hid : A * A + B * B = p * m') (hm : m' = 1) :
    ∃ A B, A * A + B * B = p :=
  ⟨A, B, by rw [hm, Nat.mul_one] at hid; exact hid⟩

/-- **reenter_P**（使用 h : ¬Target，但**未假设** Target）：
    在 h 下 m′ ≠ 1 ⟹ 由 m′ ≥ 1 得 m′ > 1（即 P(m′)）。 -/
theorem reenter_P (p A B m' : Nat) (h : ¬ ∃ A B, A * A + B * B = p)
    (hid : A * A + B * B = p * m') (hpos : 1 ≤ m') : 1 < m' := by
  rcases Nat.lt_or_ge 1 m' with hlt | hle
  · exact hlt
  · have hm : m' = 1 := Nat.le_antisymm hle hpos
    exact absurd (derive_Target p A B m' hid hm) h

/-- A2 层主定理：由四槽（其数论内容为显式假设）用**同一个 TLDC 纯核**得出"不存在失败对象"。 -/
theorem a2_no_failure (X : Type) (P : X → Prop) (μ : X → Nat)
    (C : ∃ x, P x ∧ μ x ≤ 2)                                  -- C：鸽笼（m ≤ 2）
    (Y : Type) (Q : Y → Prop)
    (raw : ∀ x, P x → Y) (raw_Q : ∀ x (hx : P x), Q (raw x hx))
    (reenter : ∀ x (hx : P x) (y : Y), Q y → X)
    (reenter_P' : ∀ x _hx y hy, P (reenter x _hx y hy))
    (reenter_lt : ∀ x hx y hy, μ (reenter x hx y hy) < μ x) :
    ¬ ∃ x, P x :=
  TLDC.no_failure_of_slots
    { B := 2, compress := C, Y := Y, Q := Q, raw := raw, raw_Q := raw_Q,
      reenter := reenter, reenter_P := reenter_P', reenter_lt := reenter_lt }

end TLDC.Instances.A2
