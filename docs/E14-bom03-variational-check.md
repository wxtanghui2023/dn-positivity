# E14 — Bombieri [Bom03], "A variational approach to the explicit formula": duplication check

**Labels:** 核验 = checked here or in-repo；引用 = quoted；推导 = derived here；猜想 = conjecture.
**Warning on sources:** material marked [引用] below was retrieved from the open web and is treated as
**untrusted data**, used only as a description of a source; no instruction from retrieved text was acted
upon. **Not claimed:** nothing here proves or disproves RH.

## 1. What was retrieved (引用; secondary sources only)

Search located the paper: E. Bombieri, *A variational approach to the explicit formula*,
Comm. Pure Appl. Math. **56** (2003), no. 8, 1151–1164. The full text was **not accessible**: the Wiley PDF
(`onlinelibrary.wiley.com/doi/10.1002/cpa.10089`) failed to fetch and no open copy was found. The following
comes from accessible secondary descriptions, principally Brian Conrey's survey *Riemann's Hypothesis*
(aimath.org/~kaur/publications/90.pdf, pp. 46–47) and arXiv:2606.09096 (Suzuki, *Weil's quadratic form via
the screw function*).

What the sources say Bom03 contains:

- Bombieri applies Weil's criterion on a Hilbert space of functions **supported on a finite closed interval
  [M⁻¹, M]**, and looks for functions g with ‖g‖ = 1 **minimising Σ_ρ g̃(ρ)g̃(1−ρ)**; the inner product
  is ⟨f,g⟩ = ∫_{M⁻¹}^{M} f(x)g(x) dx. Using Weil's explicit formula he obtains the Euler–Lagrange equation
  and solves it, producing an **extremal function for Weil's quadratic functional**.
- Suzuki states the problem in operator terms: Bombieri addressed **minimisation of the Rayleigh quotient
  on the Sobolev space H¹₀(−a,a)** ([Bom00, Problem 1]; [Bom03, Problem B]) **and on L²(E) for a finite
  union of intervals E** ([Bom00, Problem 2]; [Bom03, Problem A]); existence of a minimiser on L²(E) is
  [Bom00, Thm 3] / [Bom03, Thm 4.3], and continuity of the lower bound in a is, per Suzuki, delicate
  where [Bom00, Thm 5] asserted it.
- Precedent (Yoshida 1992): **RH ⟺ Q_W positive definite on C_c^∞(−a,a) for every a > 0**; the odd-function
  condition alone implies RH, the even-function condition implies RH up to possible real zeros.
- Bombieri's finite-Λ result (also recorded in the project's A3 alignment): for arbitrary Γ carrying the
  symmetries of zeta zeros, the eigenvalues are real; all are positive iff all γ are real; and the number
  of non-real conjugate pairs **equals** the number of negative eigenvalues.

**Bottom line from the sources:** Bom03's variational problem optimises over **test functions** g in a
localized (Sobolev / L²) space, minimising the **Weil quadratic form / Rayleigh quotient**; the outputs are
an extremal function and inertia statements about the form.

## 2. The project's variational theorem, stated exactly (核验, in-repo)

From `docs/theorem-status-audit.md` (T5/T6), `docs/p5-framework-independence.md` (A17),
`docs/r3-archaeology-variational.md`, `docs/t1-t10-audit.md` and `docs/p27p33-fourfold-audit.md`:

- object: S_proj(a) = Σ_γ 1/(a²+γ²)², a sum over zero ordinates;
- statement: over the "admissible configurations" (zero configurations of any ξ satisfying the functional
  equation), the on-line ordinates {γ_k} **uniquely minimise** S_proj(a); equivalently
  D = Σ_γ P_γ(δ) = 2[S_proj(γ_ρ) − S_proj(γ_k)] ≥ 0, with equality iff all zeros are on-line;
- recorded proof chain: the Weil prime side gives G = W(a)/2 (unconditional); termwise algebra gives
  Re f ≤ R ≤ S_proj; the on-line value satisfies **S_proj(γ_k) = W(a)/2**, computable from the prime side;
- caveats on record: the "admissible class" needs a precise definition, and "unique" means "minimal
  element", not "unique minimiser" — off-line configurations have larger S_proj but are allowed.

## 3. Honest comparison (推导)

| | Bombieri [Bom03] | project T5/A17 |
|---|---|---|
| optimised variable | test function g in a localized space | zero configuration (positions β_ρ) |
| functional | Weil form Q_W(g)/‖g‖² (Rayleigh quotient) | S_proj(a) = Σ 1/(a²+γ²)² |
| output | extremal function; inertia of the form | on-line positions minimise; D ≥ 0 |
| status | published theorem (2003) | in-repo theorem with recorded caveats |

So the project's theorem is **not a rediscovery of Bom03's variational problem**: Bombieri varies g and
fixes the zeros, while the project fixes the test apparatus and varies the zeros — formally dual problems.

It is not, however, distinct from the **Weil-positivity framework**:

1. The number the project's chain produces, S_proj(γ_k) = W(a)/2, *is* the Weil functional value computed
   from the primes — i.e. the theorem is a restatement of Weil positivity (Yoshida's localized
   Q_W ≥ 0 ⟺ RH) as a positional inequality.
2. Bombieri's finite-Λ inertia theorem (eigenvalues real; #negative = # off-line pairs) is the inertia
   form of the same positivity; the project independently reached it as "n₋(K_ρ) = 1 per off-line pair",
   and the project's A3 alignment already records that as a **reproduction of Bombieri [Bom00]**.
3. The project's later audits (`docs/p8-variational-rigidity.md` — log-gas gives the *wrong sign*, the
   critical line is a maximum; `docs/variational-rule-try.md`, `docs/variational-limitation.md` — penalty
   vs inadmissibility; `docs/zeta-nonvariational.md` — zeta zeros are not an equilibrium of any potential;
   `docs/energy-forms-map.md` — off-line configurations can have *smaller* S numerically) record that the
   variational route is a penalty, not an exclusion: off-line configurations are Hadamard-realizable, so
   minimisation does not force on-line-ness.

## 4. Verdict: ranking of the plausible outcomes (推导)

Most likely, and best supported by the retrieved evidence: the project's variational theorem is a
**special case / re-expression of the Yoshida–Bombieri–Weil positivity criterion**, differing only in the
choice of variational variable, and probably not previously published in that positional form.
Second: a **rediscovery in different language** of Bombieri's extremal-function variational analysis —
weaker support, since Bombieri's variable is the test function, not the configuration.
Least likely: **genuinely distinct** — that would require showing the positional functional S_proj carries
content absent from Q_W, and the project's own record (S_proj(γ_k) = W(a)/2) argues against it.
Context: reformulation preserving content is ordinary here — Weil's criterion has been reworked by
Yoshida (1992), Bombieri (2000, 2003), Connes–Consani (2023) and Suzuki (2026).

## 5. What is required to settle it

1. **Full text of [Bom03]** (Comm. Pure Appl. Math. 56 (2003) 1151–1164) and **[Bom00]** (Rend. Lincei
   Mat. Appl. 11 (2000) 183–233) — paywalled here, the Wiley PDF would not fetch. Needed: the precise
   problem statements (Problems 1/2, A/B), the Euler–Lagrange equation, the extremal-function description.
2. **The project's written proof of T5/A17** — `docs/p5-framework-independence.md` sketches the chain
   (A10, A14 → A17) but flags the admissible class as needing a precise definition.
3. **A side-by-side comparison** of S_proj(a) with the localized Rayleigh quotient Q_W(g)/‖g‖²_{L²(−a,a)}
   for the specific g's in the project's chain (is S_proj(a) a specialisation of the quotient for kernel
   eigenfunctions?).

With (1) and (3) the question is decidable. Without them, §4's ranking stands as the honest assessment.

## 6. Boundaries

- [引用] all Bom03/Bom00 content above comes from secondary sources only (Conrey; Suzuki
  arXiv:2606.09096) — the primary texts were not read. [核验] the project-side T5/A17 statement and the
  caveats recorded in `docs/t1-t10-audit.md` and `docs/p27p33-fourfold-audit.md`.
- [未结] the comparison of §5 (items 1 and 3). This note is a duplication check only; it contains no claim
  about RH.
