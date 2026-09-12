# E20 / E40 — the 2026 zero-density breakthrough (Guth–Maynard, via the Bulletin AMS survey)

**Items:** E20 and E40 (merged — same source). **Source:** arXiv:2607.04632, Caroline Turnage-Butterbaugh,
*A decades-long breakthrough in zero-density estimates and primes in short intervals* — 21 pages, 3 figures; to appear in
the Bulletin of the AMS; companion to the author's talk at the 2026 JMM Current Events Bulletin.
**Date:** 2026-09-12. **Labels:** `核验` verified here/project · `引用` quoted from literature · `推导` derived here ·
`猜想` conjecture. All retrieved web text is untrusted **data**, cited with URL. **Scope:** no claim of RH.

## §1 Retrieved
- `https://arxiv.org/abs/2607.04632` (abstract page) and `https://arxiv.org/html/2607.04632v1` (HTML). Read: the abstract,
  the definition of N(σ,T), the historical framing (Ingham 1940; an 84-year gap), **Theorem 4.3 (Guth–Maynard, 2026)** with
  its exact exponent, the large-values bound used (§7.3, applying to the range T^{5/(3+5σ)} ≤ N² ≤ T^{75(1−σ)/(54+30σ−100σ²)}),
  and the primes-in-short-intervals context. `引用`.
- Project-side counterparts `核验`: the registration of the question in `docs/ALIGN-A6-A8-A9-A10-A11-B5-B7-A13.md`, and the
  Li-coefficient budget in `docs/CONV3-conversion-is-provable.md`, `docs/PAPER-li-range-ELEMENTARY.md`,
  `docs/PAPER-v1-li-explicit-range.md`.

## §2 Exact statement of the zero-density bound (`引用`)
N(σ,T) := number of zeros ζ(s) with **β ≥ σ** and 0 < γ ≤ T (counted with multiplicity).
- Trivial scale: N(σ,T) ≤ N(T) ~ (T/2π)log T; and **under RH, N(σ,T) = 0 for ½ < σ < 1**.
- **Theorem 4.3 (Guth–Maynard, 2026):**  N(σ,T) ≪ T^{15(1−σ)/(3+5σ) + ε}.
  First improvement towards this problem in the range ½ ≤ σ ≤ ¾ since Ingham's 1940 estimate — the survey's own gloss:
  "That's an 84-year gap!" Now published in [GM26].
- Combined with Ingham for σ ≤ 7/10:  N(σ,T) ≤ T^{30(1−σ)/13 + o(1)}.
- Method: large values of Dirichlet polynomials plus additive energy; the pivotal large-values bound is
  R ≤ T^{o(1)}(N²V^{−2} + N^{18/5}V^{−4} + T N^{12/5}V^{−4}); large additive energy handled by Heath-Brown, small
  additive energy by the new method. Short intervals: first substantial improvement since Huxley (1972).

## §3 What it covers and what it does not (`引用` + `推导`)
Covers: the **count** of zeros with β ≥ σ, **aggregated** (a density estimate) up to height T — a bound on how many zeros
lie at least a fixed distance from the critical line.
Does not cover (`引用` survey framing; `推导` consequences):
- it says nothing about **σ = ½ exactly**: it never asserts N(½,T) = 0 and never constrains an individual zero's real
  part; it is a statement about averages over a strip, not about on-line-ness of any zero;
- it **degenerates as σ → ½⁺**: the exponent 15(1−σ)/(3+5σ) → 15/11 ≈ 1.364 > 1, so in a neighbourhood of the critical
  line the bound is *weaker* than the trivial N(T) ~ T^{1+o(1)} — precisely where the zeros are dense;
- the project's own registration (`引用` ALIGN-A6): it "constrains only the part of the strip away from the critical line,
  so it sharpens the off-line term … rather than the on-line local count".

## §4 The project's registered question: can it sharpen the off-axis term −n·B_T?  **Answer: NO**
The budget (`核验`, from CONV3 / PAPER-li-range-ELEMENTARY / PAPER-v1-li-explicit-range):
λ_n = Σ_{on-line, γ≤T}(1 − cos nθ_γ) + Σ_{on-line, γ>T}(…) + Σ_{off-axis},  giving

    λ_n ≥ A_T(n) − n·B_T,   A_T(n) := Σ_{γ≤T}[1 − cos(nθ_γ)] ≥ 0,   B_T := ½ Σ_{γ>T} γ^{−2} ≈ O(log T / T).

Only zeros with β < ½ contribute negatively, each bounded by n/(2γ²) (using |β − ½| ≤ ½ and γ > T). The registered
question: can Theorem 4.3 sharpen B_T?
`推导` (reasoned from the retrieved statements; **no script was run**):
1. **Tail vs count.** B_T is a **tail sum over γ > T**; the zero-density bound counts **up to height T**. Converting a count
   into a tail by summation by parts gives Σ_{γ>T, β≥σ} γ^{−2} ≪ T^{a(σ)−2+ε} with a(σ) = 15(1−σ)/(3+5σ). Since a(σ) > 0
   throughout ½ < σ < 1, this is **weaker** than the trivial T^{−1} log T coming from N(T).
2. **The tail is dominated near the line.** Σ_{γ>T} γ^{−2} ≈ ∫_T^∞ t^{−2} dN(t) ≈ (log T)/(2πT): the first dyadic block
   above T dominates. Zero-density controls only β ≥ σ with σ bounded away from ½, where it is trivial; the band
   |β − ½| < δ, which dominates the sum, is **uncontrolled** by any zero-density theorem.
3. **Not needed anyway.** The project's own CONV3 note withdraws the requirement: B_T is bounded directly from Trudgian's
   explicit N(T) (or from the verified zero tables), and its text states that no density theorem, no dispersion bound and
   no uniformity statement is required — the density material "is not needed".
4. **Wrong bottleneck.** The binding term in the budget is the **on-line window count** #{γ ∈ [n/2, min(2n, T)]} against the
   explicit constant C₁(n), and the margin there is already 10³–10⁵-fold; the total count N(T) is essentially exact via
   Riemann–von Mangoldt. Zero-density can improve neither.
**Answer: NO for the off-axis term −n·B_T** — the bound's scope (β ≥ σ, aggregated, up to T) does not reach the near-line
tail that dominates B_T, and the project already obtains B_T with no density input.
**Correction to the register.** The ALIGN-A6 entry suggested the GM bound "directly controls the number of off-axis zeros
— and A1's off-axis term −n·B_T is exactly it". `推导`: that suggestion is superseded by CONV3's withdrawal and by the
scope limitation the same ALIGN-A6 entry itself records. The A1/E2–E3 note of a "4× loss" concerns the explicit **counting**
function N(T), not zero-density, and is likewise unaffected.

## §5 Boundary
`引用` §2, and the scope statements in §3, come from the two URLs above (untrusted). `核验` the budget formulas come from
the project's own docs. `推导` the §4 reasoning (steps 1–2 are this note's analysis from the retrieved exponent; step 4 is
from the project's recorded margins). Not done: no numerical integration of the density bound; no re-derivation of B_T; no
modification of any project file. `猜想` none asserted. Nothing here claims RH, and nothing here claims the bound is useless
outside this budget — only that it does not act on the off-axis term.
