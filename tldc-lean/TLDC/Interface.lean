/-
  TLDC · Interface —— 四槽接口与"下降义务"的组装（仍**零污染**：不出现任何具体实例对象）。
  C 独立压缩（含定量界 B）｜R 失败保持（原始输出层）｜K 送回 X｜D 严格下降
-/
import Std
import TLDC.Core

namespace TLDC

/-- 四槽接口（与 X, P, μ 无关的具体数学一概不出现）。 -/
structure DescentData (X : Type) (P : X → Prop) (μ : X → Nat) where
  B : Nat                                              -- C：受控尺度界
  compress : ∃ x, P x ∧ μ x ≤ B                        -- C：独立压缩（定量见证）
  Y : Type                                             -- R/D/K 的原始输出空间
  Q : Y → Prop
  raw : ∀ x, P x → Y                                   -- 原始下降步
  raw_Q : ∀ x (hx : P x), Q (raw x hx)                 -- R：原始输出仍"失败"
  reenter : ∀ x (hx : P x) (y : Y), Q y → X            -- K：送回 X
  reenter_P : ∀ x (hx : P x) (y : Y) (hy : Q y), P (reenter x hx y hy)   -- R/K
  reenter_lt : ∀ x (hx : P x) (y : Y) (hy : Q y), μ (reenter x hx y hy) < μ x  -- D

/-- 由四槽组装出的**下降义务**。 -/
theorem step_of_slots {X : Type} {P : X → Prop} {μ : X → Nat} (D : DescentData X P μ) :
    ∀ x, P x → ∃ y, P y ∧ μ y < μ x :=
  fun x hx =>
    ⟨D.reenter x hx (D.raw x hx) (D.raw_Q x hx),
     D.reenter_P x hx (D.raw x hx) (D.raw_Q x hx),
     D.reenter_lt x hx (D.raw x hx) (D.raw_Q x hx)⟩

/-- 四槽 ⟹ 不存在失败对象（**调用唯一的 TLDC 纯核**）。 -/
theorem no_failure_of_slots {X : Type} {P : X → Prop} {μ : X → Nat}
    (D : DescentData X P μ) : ¬ ∃ x, P x :=
  no_failure P μ (step_of_slots D)

end TLDC
