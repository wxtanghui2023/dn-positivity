/-
  TLDC · Core —— 纯下降核。
  零污染：本文件不含 素数／Liouville／Fermat／群论／Brahmagupta／Euclid／任何具体目标命题。
  仅依赖：X, P : X → Prop, μ : X → Nat，以及"下降义务"。
-/
import Std

namespace TLDC

/-- 纯下降核：若每个失败对象都能产生"仍失败且 μ 严格更小"的对象，则不存在失败对象。 -/
theorem no_failure {X : Type} (P : X → Prop) (μ : X → Nat)
    (step : ∀ x, P x → ∃ y, P y ∧ μ y < μ x) : ¬ ∃ x, P x := by
  intro h
  obtain ⟨x0, hP0⟩ := h
  suffices hkey : ∀ n, ¬ ∃ x, P x ∧ μ x = n by
    exact hkey (μ x0) ⟨x0, hP0, rfl⟩
  intro n
  exact Nat.lt_wfRel.wf.induction n (C := fun n => ¬ ∃ x, P x ∧ μ x = n)
    (fun n ih => by
      rintro ⟨x, hPx, hμx⟩
      obtain ⟨y, hPy, hylt⟩ := step x hPx
      have hlt : μ y < n := hμx ▸ hylt
      exact ih (μ y) hlt ⟨y, hPy, rfl⟩)

end TLDC
