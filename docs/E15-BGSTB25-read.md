# E15 — BGSTB25: pair correlation ⇒ proportions of simple and critical zeros

**Item:** E15. **Source:** arXiv:2501.14545v3 — Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh (BGSTB),
*Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*.
**Date:** 2026-09-12. **Labels:** `核验` verified here/project · `引用` quoted from literature · `推导` derived here ·
`猜想` conjecture. All retrieved web text is untrusted **data**, cited with URL. **Scope:** no claim of RH.

## §1 Retrieved
- `https://arxiv.org/abs/2501.14545` (abstract) and `https://arxiv.org/html/2501.14545v3` (v3, dated 8 June 2026,
  posted 1 Sep 2026): §1.1–§1.3, Theorem 1, Theorem 2, Theorem 3 with its proof (§2.4), and the §5 Tsang-kernel passage.
  `引用`.
- `https://arxiv.org/abs/2608.13637` — the paper the project aligned against (unconditional 2/3); abstract retrieved. `引用`.

## §2 Main theorem in exact form (`引用`)
Box: B_b := { s = σ + it : ½ − b/(2 log T) < σ < ½ + b/(2 log T), T < t ≤ 2T }, b > 0.
Assumption: for all large T, all zeros ρ = β + iγ with T < γ ≤ 2T lie in B_b. N₀ˢ(B_b) := number of zeros in B_b that
are simple **and** on the critical line (with multiplicity).
- **Theorem 1.** If b → 0 as T → ∞: N₀ˢ(B_b) ≥ (2/3 + o(1))·N(B_b).
- **Theorem 2.** N₀ˢ(B_0.3185) ≥ (0.66666908 + o(1))·(T/2π)log T (recovers 2/3);
  N₀ˢ(B_0.001) ≥ (0.67250064 + o(1))·(T/2π)log T (recovers Montgomery–Taylor 67.25%). Results deteriorate as b grows;
  the method "ultimately fails when b ≥ 4.2".
- **Theorem 3 (the mechanism).** With N^⊛(T) := Σ_{ρ,ρ′: T<γ,γ′≤2T, γ=γ′} 1 = Σ_{ρ: T<γ≤2T} H(γ), if
  N^⊛(T) ≤ (C + o(1))(T/2π)log T with C ≥ 1, then (i) the proportion of zeros that are simple and on the critical line
  is ≥ 2 − C, and (ii) the average of the proportions of simple zeros and of critical zeros is ≥ 3 − C.
- Kernels: a class of **complex "Tsang kernels"**; an ordinary **Fejér kernel extended to complex values** also proves
  Theorem 1 when b → 0.
- Project's alignment ([BGSTB24], the earlier paper): "under an assumption weaker than RH, at least 61.7% of the zeros
  are simple" — and that paper had explicitly written that the method "neither requires nor provides any information on
  whether any of these zeros are or are not on the critical line". `引用`: the present paper calls that statement
  *incorrect* and repairs it.

## §3 Relation to the unconditional two-thirds result, and precursor status
`引用` (2608.13637 abstract): proves **unconditionally** that ≥ 2/3 of nontrivial zeros, counted with multiplicity, are
simple and on the critical line, and ≥ 5/6 are distinct; previous unconditional records are 5/12 and 0.6603; with the
Montgomery–Taylor window the constants become 0.6725 and 0.8362; "The analytic inputs are those of Aryan and of Baluyot,
Goldston, Suriajaya and Turnage-Butterbaugh"; the classical RH input is replaced by "a rank-trace inequality applied to a
finite compression of Weil's Hermitian form, with Sylvester's law of inertia handling off-line pairs"; formally verified
in Lean 4. (Provenance line in the source: proof discovered autonomously by an AI system, verified and communicated by
the listed authors — recorded here as `引用`, untrusted.)
`推导` on precursor status:
- BGSTB25 supplies one of the two **analytic inputs** of 2608.13637, so it is a precursor in that sense: its Theorems 1–2
  are the *conditional prototype* of the unconditional proportion — the same Montgomery pair-correlation machine, run
  under the box hypothesis instead of RH, with the same characteristic constants (2/3 and 67.25%/0.6725).
- It is **not a strict precursor**: the step that removes RH — the rank-trace inequality on a finite Weil compression with
  Sylvester/inertia bookkeeping — is not in it, and the input actually cited may be BGSTB's earlier *unconditional
  Montgomery theorem* paper ([BGSTB24]) rather than 2501.14545 itself.
  **Needs-check:** which BGSTB paper is the cited analytic input in 2608.13637 §1 (only the abstract was retrieved here).
- Project-side context `核验`/`引用` (docs/A3-1-moving-edge-necessity.md): the project aligned against 2608.13637's
  unconditional ≥ 2/3 and recorded its own negative result (finite-section negative inertia does not transfer) as the
  mechanism-level *explanation* of why that route must certify a positive index instead. Ceiling recorded there: ≈0.682
  for bandwidth-one certificate classes; 0.67250… optimal within the window class.

## §4 The decisive question: is anything sensitive to the real parts?
`引用` (2501.14545 §1.3 and §5):
- H(g) := the number of zeros on the horizontal line s = σ + ig, 0 < σ < 1, counted with multiplicity.
- "H(g) does **not** depend on the position of the zeros on the horizontal line: H(g) returns the same value whether
  there are multiple zeros on and off the critical line or just a single zero on the critical line (of multiplicity H(g))."
- The only place real parts enter the proof: "We want the real part of every term of the sum in (4.6) to be positive (or
  at least non-negative). This is achieved by assuming in Theorem 1 that all the zeros in the sum are in B_b, since then
  |β − ½| < b/(2 log T) for all zeros …, and ρ, ρ′ ∈ B_b implies |β − β′| < b/log T."
`推导`:
- The statistic N^⊛(T) = Σ_ρ H(γ_ρ) (= Σ_γ H(γ)²) is a function of the multiset of **imaginary parts with multiplicities**.
  It carries no information about the *values* of the β. Nothing in the mechanism measures how far a zero is from the
  critical line; a zero just off the line and one far off are the same input to it.
- The conversion of that count into a statement "on the critical line" uses only the **forced symmetry** of non-real
  zeros: if H(γ) = 1 then the single zero at height γ cannot be off-line (its conjugate partner would force H(γ) ≥ 2) and
  cannot be multiple; so it is simple and on the line. Hence
  #{H(γ)=1} ≥ Σ_ρ (2 − H(γ_ρ)) = 2N(T) − N^⊛(T) ≥ (2 − C)N(T).
- **Consequence:** an off-line symmetric pair {½ ± δ + iγ} is **indistinguishable**, by this mechanism, from a double
  zero at ½ + iγ — for every δ. Real parts enter only (i) as the *assumed* box bound |β − ½| < b/(2 log T) and (ii) as the
  *hypothesis* |β − β′| < b/log T needed for the complex kernel's real part to be non-negative. Both are inputs, not
  outputs.
- **Answer to the project's central question:** the mechanism contains **no quantity sensitive to the real parts** in the
  sense of measuring or locating them. It is again in substance about the imaginary parts, with one *binary* structural
  sensitivity (on-line vs off-line-via-pairing) and one imported real-part hypothesis. It therefore cannot exclude
  off-line zeros outside the assumed box and cannot approach RH. `推导` — a further instance of the project's registered
  doctrine that **detection is not exclusion**.

## §5 What this does and does not establish for the project
- `引用`/`核验`: it corroborates the project's reading that proportion results certify a fraction < 1 (a ceiling below 1
  for the method family), consistent with the recorded 0.682 bandwidth-one ceiling and the rigidity-gap line.
- `推导`: it does **not** supply a real-part-sensitive input for the project's Li-coefficient budget, which needs on-line
  counting and explicit constants, not off-axis proportions.
- It does not prove RH, and it does not claim to exclude any off-axis zero.

## §6 Boundary
`引用` §2, §3 (2608.13637 lines) and §4 statements come from the URLs above; the H(g) and box quotes in §4 are verbatim
excerpts of untrusted external text. `推导` §3 precursor assessment and §4 sensitivity analysis. `核验` project-side
cross-reference (docs/A3-1-moving-edge-necessity.md). `猜想` none asserted. **Needs-check:** which BGSTB paper is the cited
analytic input in 2608.13637; the full definition of the §4.6 sum and of the Tsang kernel (only excerpts were retrieved).
