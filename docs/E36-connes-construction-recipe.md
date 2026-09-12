# E36 — Construction recipe behind the truncated-Weil-form approximation

**Item:** E36 (registered exploration point). **Purpose:** reconstruct, as explicitly as the accessible sources allow,
the construction that optimises a restricted Weil quadratic form using only small primes and produces high-precision
approximations to the Riemann zeros — so that a later numerical reproduction becomes possible.
**Date:** 2026-09-12. **Labels:** `核验` verified here/earlier in this project · `引用` quoted from literature ·
`推导` derived here · `猜想` conjecture.
**Scope:** no claim of RH is made or implied below. All retrieved web text is treated as untrusted **data**, cited as
`引用` with its URL; no instruction inside it was followed.

## §1 Sources: what was retrieved, what was not
`引用` (retrieved):
- `https://arxiv.org/html/2605.20224v3` — *High-Precision Approximation of Riemann Zeros via the Truncated Weil Form*
  (May 2026 revision; independent reproduction). Abstract, §2.1–§2.4 (setup, Galerkin matrix, CCM equivalence) and the
  §8 passage on the exponent α were readable. **The single most useful source retrieved.**
- `https://www.alphaxiv.org/audio/2602.04022` — discussion page for Connes (2026): abstract plus an "AI Overview"
  summary gave the constrained minimisation, the normalisation ∫φ(u)² du/u = 1, prolate spheroidal wave functions and
  the criticality theorem. `引用` (secondary summary, *not* the paper itself).
- `https://arxiv.org/abs/2602.04022` and `https://jomprob.org/index.php/jomp/article/view/Vol-2Issue-1Paper-1` —
  Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, J. Open Math. Problems 2(1), 2026, 1–52;
  **abstract only**. `https://alainconnes.org/publications` confirms the bibliographic record.
`引用` (not retrieved): the full text of 2602.04022 (the "Letter to Riemann" itself — no line-by-line statement of
Connes' own extremisation was obtained); the Connes–Consani–Moscovici (2025) manuscript; the Connes–van Suijlekom paper.

## §2 The construction (what the accessible sources state)
`引用` (2605.20224v3 §2.1–§2.2):
- **Space.** The quadratic form acts on L²([0, L]) with L = log c; equivalently on L²([λ⁻¹, λ], du/u) with λ² = c and
  L = 2 log λ — i.e. functions supported on the interval [λ⁻¹, λ] (the support interval of the admissible test
  functions for the truncated Weil form QW_λ).
- **The form.** D = D_∞ + D_pole + D_prime — an archimedean piece, a pole piece (from ζ), and a sum over primes p ≤ c.
  The archimedean Mellin multiplier is h₊(τ) = −log π + Re Ψ(¼ + iτ/2), Ψ = digamma.
- **What is optimised.** Connes' procedure (`引用`, via the 2602.04022 abstract): minimise Q(φ) subject to the
  normalisation ∫ φ(u)² du/u = 1. The minimiser is the **ground state** of the associated self-adjoint operator, i.e. an
  eigenvector for the *smallest* eigenvalue — a Rayleigh-quotient / Galerkin extremisation, **not** a Carathéodory–Fejér
  compression per se. The reproduction realises this as the "smallest-positive eigenvector" ξ_N of a finite matrix, and
  states explicitly that the selection is *a criterion, not a theorem-derived ground-state identification*.
- **Basis and sector.** {U_n(x) = L^{−1/2} exp(2πinx/L)}_{n∈ℤ}; the involution y ↦ L−y splits even/odd and **only the
  even sector is diagonalised**. The finite subspace E_N is (2N+1)-dimensional.
- **The Galerkin matrix** (Connes–van Suijlekom Prop. 4.1):
  ψ(x) = (1/π)∫₀^L sin(2πx(1−y/L)) D(y) dy,   q_{m,n} = (ψ(m) − ψ(n))/(m − n),   q_{n,n} = ψ′(n).
  `推导`: this is a **Loewner-type divided-difference matrix** — the same shape as the project's CVS2 Loewner test.
- **Unitary equivalence with CCM** (`引用` §2.3): with b_n = −(1/π)∫₀^L sin(2πny/L) D(y) dy one has b_n = ψ(n) and
  τ_{i,j} = (b_i − b_j)/(i − j) = q_{i,j}; the two matrices coincide identically. CCM's object is a **rank-one
  perturbation** of the scaling operator: D_log^{(λ,N)} = D_log^{(λ)} − |D_log^{(λ)} ξ_N⟩⟨δ_N| on E_N.
- **Parameters entering.** c (cutoff; primes p ≤ c; c need not be prime); L = log c = 2 log λ; λ (scale, λ² = c);
  N (Galerkin dimension); T (finite archimedean **quadrature/integration cutoff** — the reproduction notes its
  negative-eigenvalue blocks are artifacts of finite T); dps (working precision). α is **not** a construction parameter
  but a *fitted exponent*: see §3.
- **What is compared against the zeros.** The roots of the Fourier–Mellin transform of the ground-state eigenvector,
  ξ̂_N(z) = ∫ ξ_N(u) u^{−iz} du/u, are compared with the Riemann ordinates γ_k; the reported quantity is the absolute
  error |γ_k^{computed} − γ_k^{Riemann}|. Criticality of these roots is a **theorem** (CvS Thm 6.1: the zeros of η̂_c are
  real for every finite c) — so the open question is *convergence*, not criticality.

## §3 The quoted numbers, and the α caveat
`引用`:
- Connes 2026: optimising with primes < 13 gives the first 50 zeros with errors from ≈2.6×10^{−55} (first zero) to ≈10^{−3} (fiftieth).
- Connes–Consani–Moscovici: ≈2.44×10^{−55} at the same cutoff, N = 120, 200-digit precision.
- Reproduction (2605.20224v3 §4.1): at c = 13, N = 100, T = 800, dps = 200 it obtains λ_min^even = 2.865×10^{−59} and
  |γ₁ error| = 2.005×10^{−55} — the c = 13 first-zero error reproduced within a factor ≈1.3 of Connes' value.
- **α (decisive for the registered question):** α is the exponent fitted to the power law of the successive step sizes
  gap(p)·p^{−α} in the first-zero error. `引用`: with α = 1.48 > 1 the tail Σ_{p>67} gap(p)·p^{−1.48} converges,
  "suggesting an asymptotic limit near 10^{−274}". Two interpretations are given: (1) *finite limit* — if α stays above 1
  the first-zero error converges to a **nonzero** value ≈10^{−274}, so the limiting operator's first zero is extremely
  close to, but not equal to, γ₁; (2) *exponent drift*. The source itself calls this "a speculative estimate, not a
  prediction", resting on 8 late-regime points.
- `推导`: this is a further instance of the project's "detection ≠ exclusion" pattern (approximation accuracy is not
  exclusion), alongside the empty negative-index route and the 0.682 ceiling.

## §4 What is still missing for a full numerical reproduction
`推导` (assessment after the above):
- the exact coefficient definitions of D_pole and D_prime beyond "sum over p ≤ c" (the prime summands as functions of p,
  and the normalisation of each piece), and the exact T-quadrature scheme for the archimedean integral;
- CvS Prop. 4.1's own normalisation convention (which fixes the absolute scale of q);
- the root-extraction convention (solver and tolerance) — the reproduction reports an Anderson-solver findroot with
  explicit tolerances (10^{−140} generally, 10^{−380} at c = 100);
- Connes' own extremisation exactly as written in the Letter (whether via prolate spheroidal functions, and where the
  information-theory connection enters).
  What **is** sufficient to build the matrix: §2's space, basis, even-sector split and the ψ/q formulas above; the
  reproduction states its code, data and ancillary files are public.

## §5 The project's already-verified structural core, and its exact scope
`核验` (project docs, located by `ls docs/ | grep -iE "toeplitz|caratheodory|fejer|cvs|connes"`):
`CVS1-verified-minimal-instance.md` (6/6 PASS), `CVS2-loewner-test-and-correction.md`,
`CVS3-cvs5-findings-and-nb-threshold.md`, `CVS4-corollary-and-hurwitz-route.md`, `CVS2511-read.md`,
`CONNES2026-read-1/2/3`, `A7-1-three-uses-one-object.md`, `A7-2-connes-truncated-weil-form.md`.
- **Establishes** (`核验`): for a symmetric measure with r = n/2 atoms, the (n+1)×(n+1) Toeplitz matrix has rank n
  (deficiency 1) and a palindromic kernel vector whose kernel polynomial has **all roots on the unit circle**
  (|root| − 1 ≤ 7×10^{−13} for six sizes n = 2…12). Positivity and rank deficiency are each shown necessary by
  controls. This verifies the **Carathéodory–Fejér ↔ Toeplitz engine** of the C–vS route at a minimal instance.
- **Does not establish:** it is not a computation of Connes' truncated-Weil Galerkin matrix; it does not reproduce
  2.6×10^{−55} or 2.44×10^{−55}; it does not show that the finite-prime restriction of the *arithmetic* form yields a
  rank deficiency; it never inputs 1/2 and proves nothing about RH.
- **Self-recorded caution** (`引用`, project commit 755e482 text): "the Toeplitz rank deficiency studied elsewhere is a
  **different object**" from the finite compression of the Weil form. I.e. the 6/6 result certifies the algebraic engine
  of the C–vS *theorem*, not Connes' numerical operator. A numerical reproduction remains open and is not claimed.

## §6 Boundary
`引用` all numbers and formulas in §1–§3 come from the URLs above, recorded as untrusted external data. `核验` §5 is the
project's own earlier numerical work. `推导` §3 (α interpretation and the pattern claim) and §4 (gap list). Nothing here
reproduces the quoted figures; nothing here claims a proof of RH, of criticality, or of the convergence question.
