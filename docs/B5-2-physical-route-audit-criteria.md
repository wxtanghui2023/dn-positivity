# B5-2 — Reusable audit criteria for claims that a physical or statistical model is equivalent to the zeros

**Status:** internal alignment note. Registered as item **B5-2** in `docs/PENDING-ITEMS-MASTER.md`.
**Depends on:** `E39-AUDIT-ising-zeta-claim.md`, `E39-AUDIT-v2-complete.md`, `ALIGN-A6-A8-A9-A10-A11-B5-B7-A13.md`.
**Source case:** the audit of **arXiv:2411.16777** (2D Ising model `M_{FI+SGI}^{2D}` claimed equivalent
to the zero distribution of `L(s,χ_k)` / `ζ(s)`), items **B5-1 / B5-3**.
**Label convention:** `[核验]` verified numerically here · `[引用]` quoted from literature ·
`[推导]` derived here · `[猜想]` conjecture.
**Scope warning:** these are **audit criteria**, not a theorem. A failed test marks a claim **unproven**,
never **false**; and a structure not found here is not thereby asserted not to exist.

---

## §0 Why a reusable checklist

The B5 audit found that a published model→zeros claim failed for **structural** reasons, not for lack of
detail. The failure modes are generic to the whole "physical/statistical model ⟹ zeros" genre, so the
findings are turned into a **protocol** to apply to any future such claim.

The five findings of the source audit, each of which becomes one criterion:

- **F1 — circularity.** `[引用]` The source's final theorem (Thm 5) proves the conclusion by assuming it:
  its proof asserts *"no nontrivial zeros lie off the critical line"* (this **is** RH), then argues that
  Hardy's theorem (infinitely many zeros on the line) together with numerical verification *"fixes the real
  part"*. Hardy gives infinitely many, not all; the numerics cover the first `~10¹¹`–`10¹²` zeros, not all
  heights. Neither excludes an off-line zero at some other height. The step **presupposes the conclusion**.
- **F2 — unsatisfied positivity premise.** `[核验]` The unit-circle (Fisher / Lee–Yang, 1952) conclusion
  requires **ferromagnetic / positivity (Markov) structure**; the model has a randomly competitive
  (antiferromagnetic) direction, so the premise is **not** met as specified. The project's total-positivity
  test (`TP₅`) produced **seven negative minors at 120 digits** (stable, with a Gaussian control),
  confirming sub-positivity failure for that coupling structure.
- **F3 — imprecise distributional claim.** `[引用]` "randomly distributed as the Dirichlet function /
  as `μ(n)`" names no statistic; "distributed as `μ(n)`" has no truth value until a statistic is fixed.
- **F4 — operator not exhibited.** `[引用]` No self-adjoint operator together with its spectral identity is
  given; eigenvectors are merely asserted to "form the Hilbert–Pólya space".
- **F5 — the circle→line map is the conjecture.** `[引用]` The map `u = s/(1−s)` is the classical
  equivalence `|u| = 1 ⟺ |1 − 1/ρ| = 1 ⟺ Re ρ = 1/2`; it restates a known RH criterion rather than
  supplying a proof of it.

---

## §1 The protocol

Apply every item to **any** claim that a physical or statistical model is equivalent to the zeros. Each
item has a one-line test. Grade `PASS` / `FAIL` / `NOT DETERMINED`.

**1. Presupposition test — does the construction assume the conclusion?**
*One-line test:* delete the sentence(s) that assert the conclusion, then ask whether the proof still
derives it; if the derivation collapses, the construction presupposes it. *(Ref: F1.)*

**2. Positivity-premise test — is the positivity the model needs actually verified for the model as
specified?**
*One-line test:* state the exact premise the conclusion requires (ferromagnetic / Markov / Lee–Yang
positivity) and exhibit a certificate for the model's **actual** couplings; a certificate for a
*simplified or substituted* model does not count. *(Ref: F2; tool: total-positivity / minor-sign tests.)*

**3. Meaning test — is the claimed eigenvalue-distribution statement given a precise meaning?**
*One-line test:* name the statistic (empirical spectral measure? pair-correlation function? moment
sequence?) and its normalization; if the sentence cannot be rewritten as one, it has no truth value yet.
*(Ref: F3.)*

**4. Operator test — is a self-adjoint operator exhibited together with the spectral identity?**
*One-line test:* point to an explicit self-adjoint operator `H` and an explicit identity
`spec(H) = {γ}` (or a stated bijection), each with proof; "the eigenvectors form the space" is not an
operator. *(Ref: F4.)*

**5. Mapping-content test — does the circle-to-line mapping carry distributional content?**
*One-line test:* ask whether the map preserves the **zero distribution** or merely the **geometry**; if
the distributional statement is equivalent to a known RH criterion, then the mapping **is** the content of
the conjecture and not a proof of it. *(Ref: F5.)*

---

## §2 Using the protocol

- **Grading rule.** `FAIL` on items 1 or 5 means the core of the argument is unavailable (presupposition /
  restatement) — this is decisive. `FAIL` on items 2–4 means the claim is **unproven as stated**, not
  false; the model may still be salvageable by supplying the missing certificate, meaning, or operator.
- **`NOT DETERMINED` is a first-class outcome.** It must be recorded as "not found here", **never** as
  "does not exist". (Example: for the source case, no verified positivity certificate was found; that is
  not a claim that none exists.)
- **Symmetry requirement.** Apply the same five tests to the project's **own** conditional statements
  before citing them. A criterion that only fires on others is not a criterion.
- **Order matters.** Test 1 before tests 2–4: a presupposed conclusion cannot be repaired by adding
  positivity or an operator.

## §3 Honesty boundary for the source audit

- `[引用]` The source paper's full text was not read at first pass; the v2 audit read `Definition 1` and
  `Theorems 1–5` together with their proof-critical passages. The judgement concerns the **published
  reasoning chain**, not the authors' honesty — the paper itself names the equivalence as *"the main
  obstacle of the path"*.
- `[核验]` The positivity finding (F2) is **ours**: a total-positivity test yielding seven negative minors
  at 120 digits on the stated coupling structure, with a Gaussian control. We did **not** recompute the
  model's eigenvalue count (that would require its full model definition, `B5-3`).
- `[推导]` The circularity finding (F1) is a reading of the published proof text, not a numerical result.

## §4 What this note does NOT claim

- Not a claim that **no** physical or statistical model can be equivalent to the zeros — that would be a
  "does not exist" statement, which this note is expressly forbidden from making.
- Not a claim that the source paper's theorem is **false**; the claim is that its published argument does
  not **establish** it.
- Not an RH proof or disproof of any kind.
- Not a claim that the checklist is complete or that passing all five tests would prove RH; the criteria
  are necessary-style audit gates, not a proof template.
- Not a claim that the five tests are independent of one another; tests 1 and 5 can co-fire.

---

**One-line summary.** Before accepting any "model ⟺ zeros" claim, run five gates: presupposition,
positivity-premise, precise meaning, exhibited self-adjoint operator, and distributional content of the
circle-to-line map — and record "not found" as "not found", never as "does not exist". `[推导]`

**Cross-refs:** source audit → `E39-AUDIT-v2-complete.md` (§3–§4) and `E39-AUDIT-ising-zeta-claim.md`;
positivity tool (TP₅) → E39 §3; status rows → `PENDING-ITEMS-MASTER.md` (B5-1 / B5-2 / B5-3).
