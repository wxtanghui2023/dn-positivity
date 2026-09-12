# E23 — The Lee–Yang / DQPT obstruction report: a total-positivity test (TP₅)

> Registered point E23 (`docs/EXPLORATION-POINTS-REGISTER.md`, row E23).
> Self-contained: written for a reader outside this project.
> Labels: 核验 / 引用 / 推导 / 猜想 / 撤回. The project never claims to prove RH.
> Primary sources: `docs/YM-transfer-TP5-fails-and-Turan-holds.md`, `docs/YM-transfer-PF2-test-PASSES.md`,
> `docs/R6-totalpositivity-verdict-and-correction.md`, `docs/TPX-verdict-tp-instantiation-degenerates.md`,
> `docs/TPX4-definitions-pinned-and-err-diagnosed.md`, `docs/YM-transfer-LeeYang-property-for-Phi.md`,
> `docs/YM-breakthrough-2-lee-yang-template.md`, scripts `YM7/YM8/YM9`.

## 1. What total positivity is

[引用] A kernel Λ : ℝ → ℝ is **totally positive of order p** (TP_p) if every p × p or smaller
minor satisfies det(Λ(x_j − y_k)) ≥ 0 for all increasing collections x₁ < … < x_n, y₁ < … < y_n,
n ≤ p; TN_p is the same without strictness. If Λ is also integrable it is a **Pólya frequency (PF)
function**, and a bilateral sequence a is a **PF sequence** iff the doubly infinite Toeplitz matrix
(a_{l_j − m_k}) is TN (Khare–Holtz; Gröchenig, arXiv:2007.12889; Schoenberg, Karlin).
Two classical links matter here: (i) Schoenberg's theorem — Λ is PF iff its two-sided Laplace
transform equals 1/Ψ with Ψ in the Laguerre–Pólya class; (ii) Pólya (1927) — **RH ⟺ Ξ ∈ LP**, where
Ξ(t) = ξ(1/2 + it). Composed, they give the Gröchenig form of RH: [引用]
**RH ⟺ the (bilateral) Laplace inverse transform of 1/Ξ is a Pólya frequency function.**
The same source notes the equivalence had not been tested numerically on ζ. Katkova's known
boundary is order **43**: the coefficient sequence of ξ₁(s) = ξ(1/2 + √s) is TN at least to order 43
and asymptotically PF. TN objects also obey **variation diminution** (Schoenberg): A TN ⟹ S⁻(Ax) ≤ S⁻(x).

## 2. Why a Lee–Yang-type argument for the zeros would need positivity

[引用] The Lee–Yang circle theorem (1952) has the shape
**self-inversive symmetry + positivity (ferromagnetic coefficients) + Asano contraction (1970)
⟹ the zeros are forced onto a fixed trajectory** (the unit circle; Fisher zeros give the same shape
for complex temperature). [推导] RH has the same logical shape
(`docs/YM-breakthrough-2-lee-yang-template.md` §2): the functional equation ρ ↔ 1 − ρ̄ supplies the
symmetry, the critical line Re ρ = 1/2 is the fixed trajectory, and the missing ingredient is exactly
the **positivity** — arithmetic's counterpart of ferromagnetism — whose role in Lee–Yang is to prove
half-plane non-vanishing, i.e. precisely "no zeros with σ > 1/2". [引用] For a *real, sign-definite*
kernel the classical transcription of "positivity ⟹ real zeros" is total positivity (Schoenberg,
Karlin); hence the specific route the project proposed: prove the kernel total positive.

## 3. Exactly what the test computes

[核验] The object tested is the classical integral kernel
Φ(u) = Σ_{n≥1} (2π²n⁴ e^{9u/2} − 3πn² e^{5u/2}) e^{−πn²e^{2u}}, with Ξ(t) = 2∫₀^∞ Φ(u) cos(ut) du
(calibrated: first zero 14.134725142 vs known 14.1347251417; Ξ(0)/2 = 0.2485603891).
The test forms the matrices M = (Φ(|u_i − u_j|)) and evaluates **all minors** of order k = 2 … 6:
- Test A — uniform grids u ∈ [0, 2], steps h = 0.05 / 0.1 / 0.2 (11 points): C(11,2)=55, C(11,3)=165,
  C(11,4)=330, C(11,5)=462, C(11,6)=462 minors.
- Test B — non-uniform random point sets (the genuine TP test, since TP is not confined to grids).
All determinants are evaluated in `mpmath` at 30, 60 and 120 decimal digits (`scripts/YM8_highprec_k5_check.py`),
because Φ spans roughly 1e−197 while the offending minors are of size 1e−9 — float64 alone is not
trustworthy at that contrast.

## 4. What the seven negative minors mean

[核验] Results as archived:
- Test A: k = 2, 3, 4 → **zero** negative minors; k = 5 → **7** negatives, minimum
  **−2.473647891e−9**; k = 6 → 142 negatives.
- The same minimum value is reproduced **bit-for-bit at dps = 30, 60 and 120**, so it is not rounding noise.
- The most negative order-5 minor sits on the points (0.2, 0.3, 0.4, 0.5, 0.6) — i.e. in the **core**
  of the tested window, not at an edge.
- Test B (random sets): 0, 0, 0 negatives at k = 2, 3, 4; **31** at k = 5 and **50** at k = 6.
Meaning: the kernel Φ is TN up to order 4 and **fails TP₅** on the tested domain. A single negative
minor is enough to refute TP_p for every p ≥ 5; the archival statement is the order-5 failure, and
higher orders were not needed. A separate computation on the same day found a *positive* result at
**coefficient level** [核验]: for Ξ(t) = 2Σ(−1)ⁿ M_n t^{2n}/(2n)!, all M_n > 0 (n = 0 … 10), so the
Taylor coefficients alternate; and the log-concavity ratios r_n = a_n²/(a_{n−1}a_{n+1}) exceed 1 for
n = 1 … 9 with margin r_n − 1 ≈ c/n, c ≈ 1.2–1.3 — a Turán-type inequality that holds **but decays**.

## 5. Why a Gaussian control matters

[核验] When a quantity ~1e−9 is extracted from data spanning 1e−197, an exact zero can be destroyed
(or a nonzero value manufactured) by cancellation; the result must therefore be validated against a
kernel whose answer is *known a priori*. The Gaussian kernel e^{−u²/2} is exactly PF∞, so **every**
minor must be ≥ 0. Run at dps = 60, it produced **zero** negative minors. The control therefore certifies
the test harness: the 7 negatives are a property of Φ, not an artefact of the determinant routine.
Both the control and the pass/fail logic are printed by `YM8` itself (its header states the decision rule
in advance: persistence at 60–120 digits ⟹ real; flipping ⟹ cancellation).

## 6. What the result does and does not show

**Shows** [核验]: on the tested domain ([0,2], orders ≤ 6, three grid families plus random sets), the
classical kernel Φ is not totally positive of order 5, with a stable, reproducible, control-validated
minimum.

**Does not show**: RH is false; that the zeros leave the line; that a Lee–Yang-type argument is
impossible; or anything at all beyond the tested orders and window. TP_p for p ≤ 6 on a finite window
is a finite statement; RH quantifies over all orders and the whole line.

**And it now shows less than it first appeared to** [撤回]: a follow-up audit against the original
literature (`docs/R6-totalpositivity-verdict-and-correction.md` §0–§3) established that in
Schoenberg/Gröchenig the RH-relevant PF object is **not Φ** but the bilateral Laplace inverse transform
of **1/Ξ**, whose poles are the zeros ±γ_k on the real axis: Λ(x) ≈ Σ_k c_k e^{∓γ_k x}, c_k = 1/Ξ′(γ_k).
The project's own index classifies the earlier reading of the TP₅ failure as *superseded*
(`docs/E18-NOGO-ALIGNMENT-2.md`, item 33). The honest current status is therefore:
- [核验] the numerical fact about Φ's kernel (unchanged, and reusable);
- [撤回] the claim that this constitutes a new negative result about the Lee–Yang route;
- [核验] a related and still standing negative: instantiating the TP/PF criterion **with the zeros
  themselves** makes it vacuous — a_n = (−1)ⁿ e_n(1/γ_j²) is automatically log-concave by Newton's
  inequality, and the single-sided Toeplitz test is triangular, so the conditions hold for *any* positive
  γ_j and have no discriminating power (`docs/TPX-verdict-tp-instantiation-degenerates.md` §1–§2). This
  is the project's explanation of why the equivalent criterion is described in the 2020 literature as
  "not yet tested": the untested object is structural, not neglected. The only non-vacuous form left is
  the variation-diminution version (Λ PF ⟺ convolution by Λ does not increase the number of sign changes),
  which is computable with explicit test functions but is still *equivalent* to RH.

## 7. A failed positivity test does not refute a conjecture

It refutes a **specific proposed route**. The route refuted here is: "Φ is totally positive, hence the
classical positivity theorem applies, hence the transform's zeros are real." That route is dead at order 5
[核验]. RH itself, and any other route to it, is untouched. This distinction — *detection ≠ exclusion*,
and *a failed sufficient condition ≠ a counterexample* — is the same distinction the project applies to
every physical model (E19) and to the DQPT literature
(`docs/YM-breakthrough-5-dqpt-paper-verdict.md` §2).

## 8. Honest scope: what this bears on, and what it does not

**Bears on** [推导]:
- Any claim that the *naive* total-positivity route to RH succeeds; it does not, at the level tested.
- Any claim that the TP/PF criterion is a ready-made test: with zeros substituted it is vacuous (§6).
- The audit of arXiv:2411.16777 (2D Ising ⟺ ζ zero distribution), whose unit-circle conclusion is
  asserted for a model with random competing (antiferromagnetic) couplings, where the Lee–Yang
  positivity premise fails; the project's audit explicitly cites its TP machinery as the instrument
  (`docs/E39-AUDIT-ising-zeta-claim.md` §2, item 2 — 推导, initial audit, full text unread).
- Literature: it is *compatible with* the classical results (Schoenberg, Pólya 1927, Karlin, Asano 1970,
  Simon–Griffiths 1973, Gröchenig 2020, Katkova's order-43 boundary) and contradicts none of them [引用].

**Does not bear on**:
- RH or any equivalent restatement of it; no zero was moved by this test.
- The variation-diminution form, or the corrected object (the bilateral Laplace inverse transform of
  1/Ξ), neither of which was tested here [未做].
- Finite-range numerical evidence in either direction: the test is local in u and finite in order.
- Lee–Yang / Fisher zero theory as such: the failure is a property of one specific kernel Φ, not of
  the mechanism, and the mechanism's arithmetic transcription remains, at best, an unbuilt construction.

## 9. Boundaries

Notation follows the archive (核验 / 引用 / 推导 / 猜想 / 撤回). The 120-digit run, the Gaussian control,
the minor counts and the Turán ratios are 核验 and reproducible from scripts `YM7`, `YM8`, `YM9`. The
object correction of §6 is 引用 from Gröchenig arXiv:2007.12889 with 推导 for its application to our
object. The audit statement of §8 is 推导 from an initial (not full-text) audit. No model was constructed,
no file outside this note was modified, and no claim of proof — of RH or of any of its equivalents — is made.
