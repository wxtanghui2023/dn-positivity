# E29 / A5-4 — Is the Burnol–Li isomorphism already in the literature?

**Date:** 2026-09-12 · **Registered:** E29 / A5-4 "查证 Burnol↔Li 同构是否已见于文献".
**Project suspicion** (`docs/ALIGN-A4-A5-with-our-results.md` §1, §3): Burnol's projection framework (vectors
indexed by a zero ρ and an order k, the k-th order being the sensitive one) and Li's coefficient criterion are
"the same object in two guises"; the √log in Burnol's lower bound comes from the order budget k ~ log(1/λ); and
(1 − 1/ρ)^n = Σ_k C(n,k)(−1)^k ρ^{−k} makes the identification explicit.
**Labels:** 核验 / 引用 / 推导 / 猜想. No claim about RH is made or implied.

## 1. The two frameworks, as published

**Burnol / Nyman–Beurling side.**
- J.-F. Burnol, "A lower bound in an approximation problem involving the zeros of the Riemann zeta function",
  Adv. Math. **170** (2002) 56–70 (arXiv:math/0103058). 引用.
- Its content per two independent secondary sources: BBLS proved unconditionally lim inf_N d_N² log N ≥
  Σ_{Re ρ=1/2} 1/|ρ|², and "the constant was later improved by Burnol who showed
  lim inf_N d_N² log N ≥ Σ_{Re ρ=1/2} m(ρ)²/|ρ|²" (AIM/Kaur preprint, "An Optimal Choice of Dirichlet
  Polynomials for the Nyman–Beurling …"); equivalently, Darses–Hillion (arXiv:1805.06733v4, §1): "A stronger
  statement is actually conjectured, namely d_n² ∼ C/log n, where C = 2 + γ − log(4π) … Burnol proved the
  inequality d_n² ≥ (C + o(1))/log n for the same constant C". 引用 (both secondary).
- Burnol's machinery papers: "Entrelacement de co-Poisson", Ann. Inst. Fourier **57** (2007) 525–602
  (arXiv:math/0407443), Théorème 2.12 = the co-Poisson integral formula; and "The explicit formula in simple
  terms" (arXiv:math.NT/9810169). 引用.
- Project reading (A4) reports Burnol Thm 1.2 as lim inf D(λ)·√(log(1/λ)) ≥ √(Σ_ρ 1/|ρ|²), with
  C = 2 + γ − log 4π ≈ 0.04619 — the **same constant** as above. 核验 (constant consistent across three sources).

**Li side.**
- X.-J. Li (1997), J. Number Theory **65**, 325–333: RH ⟺ λ_n ≥ 0 ∀n ≥ 1, where λ_n = Σ_ρ [1 − (1 − 1/ρ)^n].
  引用.
- E. Bombieri & J. C. Lagarias (1999), "Complements to Li's criterion for the Riemann hypothesis",
  J. Number Theory **77**, 274–287. From the abstract: they use the Guinand–Weil explicit formula and "relate
  the conjectural positivity of λ_n to Weil's criterion for the Riemann Hypothesis". 引用 (abstract snippet;
  full text not retrieved).
- J. C. Lagarias (2007), "Li coefficients for automorphic L-functions", Ann. Inst. Fourier **57**, 1689–1740
  (arXiv:math/0404394). Retrieved sentences: "the 'explicit formula' of prime number theory may be used to
  obtain an arithmetic expression for Li's coefficients λ_n … λ_n = S_∞(n) − S_f(n) + 1"; and "each positivity
  condition λ_n ≥ 0 encodes 'Weil positivity' of Weil's quadratic functional for a particular test function
  g_n(x)". 引用.

## 2. The closest published link between the two

- **One-way, in Lagarias (2007) §1.** In setting up the Mellin coordinates for the Weil functional he writes
  that "the Mellin transform extends to an isometry between L²(R_{>0}, dx) and L²(1/2 + iR, dt/2π)", and adds:
  "We treat the 'explicit formula' in these coordinates (**a viewpoint taken in [Burnol]**)." 引用.
  → Lagarias' Li machinery is deliberately presented in **Burnol's coordinates**. This is the closest *published*
  textual bridge found: a shared-coordinates statement, not an isomorphism of criteria.
- **Direct comparison of the two factors: only in an unrefereed preprint.** preprints.org 202506.0772,
  "Spectral and Analytic Structure of the Nyman–Beurling–Báez–Duarte Approximation", §14 "Connection with Li's
  Criterion", labelling φ_n(ρ) = 1 − (1 − 1/ρ)^n the "Li factor" and ψ(ρ) = |1 − 1/ρ|² the "Burnol factor", with
  Prop. 16 called an "Infinite product – Li connection". 引用 **with warning**: non-peer-reviewed, and the same
  preprint elsewhere claims to prove RH; it must not be cited as authority.
- Also inspected at secondary level: Wikipedia "Li's criterion" ("Bombieri and Lagarias also show that Li's
  criterion follows from Weil's criterion for the Riemann hypothesis") and MathOverflow 514905 (an integral
  form of Li's criterion in terms of N(T)) — user-level, not published. 引用 (secondary).

**Not found** by this search: any peer-reviewed paper whose title/abstract states that Burnol's projection
framework (his barrier/obstruction vectors X_{λρ,k}) *is* the Li test-function family g_n, or that the
Nyman–Beurling distance and the Li coefficients are two faces of one object.

## 3. The project's claim, restated for checking 推导

With z_ρ = 1 − 1/ρ one has z_ρ^n = Σ_k C(n,k)(−1)^k ρ^{−k}, so λ_n = Σ_ρ [1 − z_ρ^n] is Σ_k-weighted with the
k-th order ρ^{−k}-sensitive. Burnol's lower bound has the same shape with effective order k ≍ log(1/λ) (the
"order budget"), which is why both yield √log-type constants. A5-4 asks whether **someone has already written
down this identification**; the answer below separates what is known from what is not.

## 4. Verdict

**Partial**, in three parts:
1. **Known (published):** Li's positivity ⟺ Weil positivity for specific test functions g_n — Bombieri–Lagarias
   1999, developed in Lagarias 2007. [引用]
2. **Known (published), one-way:** the Weil functional / Li coefficients are treated in Burnol's Mellin
   coordinates, with Burnol cited for the viewpoint — Lagarias 2007 §1. [引用]
3. **Apparently new (not found):** an explicit statement that Burnol's projection vectors and the Li test
   functions are the same family, or that Burnol's lower bound and the Li asymptotic are one identity with the
   order index re-parametrised k ≍ log(1/λ). [not found — searched: Burnol's titles/abstracts, Bombieri–Lagarias,
   Lagarias 2007, BBLS, Darses–Hillion, Balazard–de Roton, de Roton's Beurling–Nyman generalisation, the
   Vasyunin/cotangent-sum literature, and the preprints surfaced by search.]

**Consequence for registration.** A5-4 may be marked: *ingredients known; explicit isomorphism not found; the
claim must pass the source check of §5 before being asserted as new.* It must **not** be registered as a project
discovery on the present evidence.

## 5. The sentences that would settle it (exact check-list)

1. **Burnol, Adv. Math. 170 (2002) 56–70 — open access as arXiv:math/0103058.** Look for (i) any citation of
   Bombieri–Lagarias [BL99] or of Li; (ii) in the section introducing the projection (Grenander–Rosenblatt) and
   the vector X_{λρ,k}, a sentence identifying the k-index with an order of vanishing / a power of ρ^{−1}, and
   any asymptotic k ≍ log(1/λ); (iii) a remark that the extremal sequence is the Li-tested family. A sentence of
   the shape "these are exactly the test functions of [BL99]" settles it as **known**.
2. **Bombieri & Lagarias 1999, J. Number Theory 77, 274–287.** Their λ_n formula comes from the Guinand–Weil
   explicit formula; check whether the test-family they use is indexed in a way that matches Burnol's order
   index, and whether they cite Burnol. If yes → **known**.
3. **Lagarias 2007, Ann. Inst. Fourier 57, 1689–1740 (arXiv:math/0404394), §1–§4.** Whether the g_n are
   identified with the Nyman–Beurling / projection family. The paper cites Burnol for the coordinates, so an
   identification, if it exists, is most likely to be stated here.
4. **Bombieri 2000, "Remarks on Weil's quadratic functional in the theory of prime numbers, I",
   Rend. Mat. Acc. Lincei IX, 11, 183–233.** Search for the Nyman–Beurling approximation inside the Weil form
   and any comparison with Li coefficients.
5. **Darses–Hillion (arXiv:1805.06733) §1** and **Balazard–de Roton (Int. J. Number Theory 6 (2010) 883–903)**:
   their bibliographies collect the Burnol/NB line and would reveal any existing NB↔Li bridge.

Until at least (1) and (3) are checked, the honest label is: **partial; explicit isomorphism not found**.

## 6. Boundary
Read in this pass: arXiv metadata/abstracts (Burnol 2002, Burnol 2004/2007, Lagarias 2007), Bombieri–Lagarias
1999 abstract, Darses–Hillion §1, the AIM/Kaur preprint, the unrefereed preprints.org item, Wikipedia
"Li's criterion", MathOverflow 514905. **Not read:** full texts of Burnol 2002, Bombieri–Lagarias 1999,
Lagarias 2007, Bombieri 2000. "not found" = *not found by this search*. This note closes A5-4 as a
**literature check only**; it makes no theorem claim and no RH claim.
