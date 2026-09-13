/-
E45-NearCUE-Instance.lean -- E45: machine-checked numeric hypotheses for our own near-CUE law.

CONTEXT (see docs/E45-ceiling-law-construction.md)
  The frontier's bandwidth-one ceiling theorem is parametric in the grid size N and its only numeric
  hypothesis is the "ramp" condition on the grid form factor S:
        NearCUE S N tau  :=  for all j, 1 <= j -> j < N -> |N * S j - j| <= tau
  E45 constructed laws of our own whose form factor is EXACTLY the ramp, so that tau = 0 and the
  numeric input becomes an identity instead of an interval-arithmetic enclosure (E44's gap).
  This file machine-checks the two numeric facts that the ceiling theorem consumes:
    (1) NearCUE (ramp N) N 0                      -- tau = 0
    (2) |D(1)| <= 1/(2N),  d1 := 1/(2N)           -- the edge bound, with D = C - x^2/2 at x = 1
  plus the resulting constants 1/(6N^2) at N = 4 and N = 6.

WHY THIS IS A STANDALONE FILE, NOT AN INSTANCE OF THE REPO'S THEOREM
  The repository github.com/anthropics/zeta-23-lean pins toolchain leanprover/lean4:v4.33.0-rc2 and a
  specific Mathlib revision, while the local Mathlib is the v4.33.0 release.  Importing
  Zeta23.PairCeiling.ceiling_nearCUE would therefore require building that exact pinned Mathlib
  (multi-gigabyte), which is not available here.  What CAN be checked locally is the arithmetic content
  of the hypotheses, using the repository's own definitions re-stated verbatim below (Defs.lean:
  Csum s m = sum_{j in Icc 1 m} s j, massOf S N j = S j / N, Dfun s N 1 = Csum s N - 1/2).

NOTE ON FIDELITY
  `Csum`, `massOf`, `ramp` and `D1` below mirror Defs.lean and the paper's normalisation.  `D1` is the
  repository's `Dfun s N 1`, for which Defs.lean supplies the lemma `Dfun_one : Dfun s N 1 = Csum s N -
  1/2`.  No claim beyond these arithmetic facts is made here.

Compiled with: cd ~/mathlib4 && lake env lean <this file>   (minimal imports per project discipline)
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

namespace E45

open Finset

noncomputable section

/-- Defs.lean: partial sums of the atom masses, `C_m = sum_{j=1}^{m} s_j`. -/
def Csum (s : ℕ → ℝ) (m : ℕ) : ℝ := ∑ j ∈ Finset.Icc 1 m, s j

/-- Defs.lean / paper: the atom mass of the grid form factor at j is `S j / N`. -/
def massOf (S : ℕ → ℝ) (N : ℕ) (j : ℕ) : ℝ := S j / N

/-- The grid form factor of our constructed law: the ramp `S j = j / N` (E45, sections 9-10). -/
def ramp (N : ℕ) : ℕ → ℝ := fun j => (j : ℝ) / N

/-- Defs.lean's `Dfun s N 1`, i.e. `C(1) - 1^2/2`. -/
def D1 (s : ℕ → ℝ) (N : ℕ) : ℝ := Csum s N - 1 / 2

/-- **(1) The ramp satisfies the ramp condition with tolerance zero**: `NearCUE (ramp N) N 0`. -/
theorem nearCUE_zero (N : ℕ) :
    ∀ j : ℕ, 1 ≤ j → j < N → |(N : ℝ) * ramp N j - (j : ℝ)| ≤ 0 := by
  intro j _ _
  have h : (N : ℝ) * ramp N j = (j : ℝ) := by
    rcases Nat.eq_zero_or_pos N with hN | hN
    · omega
    · simp only [ramp]; field_simp
  rw [h]
  simp

/-- Partial sums of the ramp's masses: `sum_{j<=m} (j/N)/N = m(m+1)/(2N^2)`. -/
theorem Csum_ramp_partial (N m : ℕ) (hN : 0 < N) :
    Csum (fun j => massOf (ramp N) N j) m
      = (m : ℝ) * ((m : ℝ) + 1) / (2 * (N : ℝ) ^ 2) := by
  induction m with
  | zero => simp [Csum]
  | succ k ih =>
    have h1 : (1 : ℕ) ≤ k + 1 := Nat.one_le_iff_ne_zero.mpr (Nat.succ_ne_zero k)
    have hstep : Csum (fun j => massOf (ramp N) N j) (k + 1)
        = Csum (fun j => massOf (ramp N) N j) k + massOf (ramp N) N (k + 1) := by
      simp only [Csum]
      rw [Finset.sum_Icc_succ_top h1]
    rw [hstep, ih]
    simp only [massOf, ramp]
    have hNr : (N : ℝ) ≠ 0 := by positivity
    push_cast
    field_simp
    ring

/-- The total mass of the ramp at grid size N is `(N+1)/(2N)`, i.e. `C(1)` in the paper's notation. -/
theorem Csum_ramp (N : ℕ) (hN : 0 < N) :
    Csum (fun j => massOf (ramp N) N j) N = ((N : ℝ) + 1) / (2 * (N : ℝ)) := by
  have h := Csum_ramp_partial N N hN
  have hNr : (N : ℝ) ≠ 0 := by positivity
  rw [h]
  field_simp

/-- **(2) The edge bound**: `D(1) = 1/(2N)` exactly, hence `|D(1)| <= 1/(2N) =: d1`. -/
theorem D1_ramp (N : ℕ) (hN : 0 < N) :
    D1 (fun j => massOf (ramp N) N j) N = 1 / (2 * (N : ℝ)) := by
  simp only [D1, Csum_ramp N hN]
  have hNr : (N : ℝ) ≠ 0 := by positivity
  field_simp
  ring

/-- The edge bound in the form the ceiling theorem consumes, `|D(1)| <= d1` with `d1 = 1/(2N)`. -/
theorem abs_D1_ramp_le (N : ℕ) (hN : 0 < N) :
    |D1 (fun j => massOf (ramp N) N j) N| ≤ 1 / (2 * (N : ℝ)) := by
  rw [D1_ramp N hN]
  rw [abs_of_nonneg]
  positivity

/-- **N = 4 instance**: tolerance 0 and edge bound `d1 = 1/8`, with theorem constant `1/96`. -/
theorem instance_N4 :
    (∀ j : ℕ, 1 ≤ j → j < 4 → |(4 : ℝ) * ramp 4 j - (j : ℝ)| ≤ 0)
      ∧ |D1 (fun j => massOf (ramp 4) 4 j) 4| ≤ 1 / 8
      ∧ (1 : ℝ) / (6 * (4 : ℝ) ^ 2) = 1 / 96 := by
  refine ⟨nearCUE_zero 4, ?_, by norm_num⟩
  have h := abs_D1_ramp_le 4 (by norm_num)
  norm_num at h
  exact h

/-- **N = 6 instance**: tolerance 0 and edge bound `d1 = 1/12`, with theorem constant `1/216`. -/
theorem instance_N6 :
    (∀ j : ℕ, 1 ≤ j → j < 6 → |(6 : ℝ) * ramp 6 j - (j : ℝ)| ≤ 0)
      ∧ |D1 (fun j => massOf (ramp 6) 6 j) 6| ≤ 1 / 12
      ∧ (1 : ℝ) / (6 * (6 : ℝ) ^ 2) = 1 / 216 := by
  refine ⟨nearCUE_zero 6, ?_, by norm_num⟩
  have h := abs_D1_ramp_le 6 (by norm_num)
  norm_num at h
  exact h

end

end E45
