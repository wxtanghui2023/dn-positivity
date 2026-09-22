/-
  Liouville 层（Prototype-0）——**只做结构实例化**：其数论内容（短代表元引理／下降证书／局部律）
  以**显式假设／内层四槽**承载（本环境无 Mathlib，未做数论形式化）。
  关键：**外层强归纳在本层自证**；core 在**归纳步之内**被调用
        （方向 = ih → 内层四槽 → core → H q，**绝不是** core → j ∈ H）。
-/
import Std
import TLDC.Core
import TLDC.Interface

namespace TLDC.Instances.Liouville

/-- 归纳步的**层内形态**：给定内层四槽（其构造使用 j<q ⟹ H j）与"¬H q ⟹ 失败对象存在"，
    用**同一个纯核**得出 H q（即 j ∈ H）。 -/
theorem H_of_inner {X : Type} {P : X → Prop} {μ : X → Nat}
    (D : TLDC.DescentData X P μ) (H : Prop) (failure_of_not_H : ¬ H → ∃ x, P x) : H :=
  Classical.byContradiction (fun hH => TLDC.no_failure_of_slots D (failure_of_not_H hH))

/-- **外层强归纳在本层自证**：∀ q < Q, H q（步内可调用 core，见 `H_of_inner`）。 -/
theorem outer_induction (Q : Nat) (H : Nat → Prop)
    (step : ∀ q, q < Q → (∀ j, j < q → H j) → H q) : ∀ q, q < Q → H q := by
  intro q
  exact Nat.lt_wfRel.wf.induction q (C := fun q => q < Q → H q) (fun q ih => by
    intro hq
    exact step q hq (fun j hj => ih j hj (by omega)))

/-- Liouville 层的**归纳步**（层内定义）：`ih`（= 所有 j<q 已精确）用于构造内层四槽；
    随后调用**同一个 core** 得到 H q。 -/
theorem liouville_step_via_core (Q : Nat) (H : Nat → Prop) (q : Nat) (_hq : q < Q)
    (_ih : ∀ j, j < q → H j)
    {X : Type} {P : X → Prop} {μ : X → Nat}
    (D : TLDC.DescentData X P μ)                      -- 内层四槽（构造依赖 ih）
    (failure_of_not_H : ¬ H q → ∃ x, P x) :
    H q :=
  H_of_inner D (H q) failure_of_not_H

end TLDC.Instances.Liouville
