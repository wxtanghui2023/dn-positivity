# E13 — Christoffel function ↔ the project's Hankel-determinant work: the interface

**Labels:** 核验 = checked here or in-repo；引用 = quoted；推导 = derived in this note；猜想 = conjecture.
**Sources:** in-repo — `docs/p36-3-gram-rigidity.md` (the Hankel/ASF work), `docs/bridge-sym-moments-rn.md`
(symmetric moments of log ξ(½+z)), `docs/r3-iv-layering.md`, `docs/r3-v-archaeology.md`,
`docs/iteration-2-5-infinite-dim-algebraicity.md` (moment determinacy), and the frontier content recorded
in `docs/ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md` §2 (frontier §7.2(d)).
The frontier paper itself was **not** read here. **Not claimed:** no bound on the proportion is produced
below, and RH is not addressed.

## 1. The frontier's object (引用)

With moments m₀ = 1, m₁, …, m_{2m} of the relevant spectral measure known, the sharp lower bound for the
proportion of positive eigenvalues — hence of on-line zeros — is 1 − Λ_m(0), where Λ_m is the Christoffel
function of the moment sequence at 0. By E8 §2,

    Λ_m(0) = 1/(H_m⁻¹)_{00} = det H_m / det B_m ,    H_m = (m_{i+j})_{0≤i,j≤m} .

So the frontier needs exactly two things: (i) the moment sequence of the compression's spectral measure,
and (ii) its truncations. Unconditionally it possesses m₁ (the second-moment evaluation, [BGSTB24, Mon73,
Ary22]) and therefore only Λ₁; higher moments fail in the Rudnick–Sarnak range X^k ≤ T^{2−ε}, which at
X ≍ T permits only k = 1.

## 2. The project's object: P36.3 Hankel rigidity (核验, in-repo)

`docs/p36-3-gram-rigidity.md` studies a Hankel matrix of moments:

    H_N = (M_{i+j}) ,   M_n = Σ_ρ (β_ρ − ½)^{2n} ,   vᵀ H_N v = Σ_ρ w_ρ |P_v(δ_ρ)|² ≥ 0 ,   δ_ρ = β_ρ − ½ .

Recorded findings:

- on-line (all δ = 0): M_n = 0 ⟹ H_N = 0, rank 0;
- off-line: rank(H_N) = the number of distinct δ-orbits (single δ: rank 1) — "an off-line configuration
  is a finite-rank positive measure" (numerically confirmed there);
- the obstruction: M_n = Σ (Re(ρ − ½))^{2n} has **no arithmetic formula**. Explicitly, (Re z)^{2n}
  expands into mixed terms Σ_k binom(2n,k) z^k z̄^{2n−k}, and the mixed sums Σ_ρ ρ^k ρ̄^m have no
  independent evaluation; hence rank, kernel and determinant of H_N are not computable from the primes.

Related in-repo moment material: `docs/bridge-sym-moments-rn.md` (symmetric moments
a_k = −(1/k)Σ_ρ (ρ−½)^{−k} of log ξ(½+z), which terminate in the same circularity);
`docs/r3-iv-layering.md`, `docs/r3-v-archaeology.md`, `docs/iteration-2-5-infinite-dim-algebraicity.md`,
where moment determinacy is a rigidity class: "spectral-trace integrality paired with absoluteness of
ξ-coefficients ⟹ moment-determinate spectrum ⟹ spectrum = ζ zeros — trivial, circular".

## 3. The interface (推导)

The two sides manipulate the same *species* of object and the same functional:

- the Christoffel function is a Hankel-matrix inverse entry, equivalently a ratio of consecutive Hankel
  determinants; the project's H_N and its determinants D_N = det(M_{i+j}) are of exactly this species;
- on both sides the truncation index is the information knob: frontier Λ_m uses order-2m moments, the
  project's H_N uses M₀,…,M_{2N}.

So the interface is not a loose analogy at the level of the object type: **both are truncations of a
moment (Hankel) matrix, and both basic quantities are Christoffel-type contractions of it.**

## 4. Where they are merely analogous, not the same (explicit)

1. **Different measure.** The frontier's moments are those of the spectral measure of a localized Weil
   form, evaluated from the prime side. The project's M_n are even moments of the *real parts* of zeros.
   Σλ^k ≠ Σ(β−½)^{2k}: different functionals of different data.
2. **Opposite normalisation regimes.** The project's H_N is a *defect* matrix — it vanishes identically
   exactly when RH holds. The Christoffel function needs a non-degenerate moment matrix with m₀ = 1
   fixed; Λ_m(0) for an identically zero matrix is meaningless. Defect matrix vs probability-normalised
   moment matrix.
3. **Positivity is free on one side.** H_N ⪰ 0 is trivially true for the project (it is a Gram matrix);
   the frontier's moment positivity is a nontrivial input.

Conclusion: same species, different measure, different regime. The interface is real but transfers no
bound.

## 5. What each side can compute that the other cannot

- **Frontier:** the *values*. m₁, m₂ unconditionally at X ≍ T ⟹ Λ₁(0) and the ceiling; and, under
  Hypothesis HL*(k₀), Λ_m for m ≤ k₀/2.
- **Project:** the *machinery and the negative results*. Explicit, numerically stable Hankel/Christoffel
  evaluation for any **hypothetical** moment sequence (cf. `scripts/r3_sproj_structure.py` and the rank
  tests of P36.3), plus the sharp negative result that the natural δ-moment sequence is not evaluable.

## 6. Is there a new testable quantity?

**Candidate A (推导).** Since Λ_m(0) is decreasing in m, the frontier's bound is c(m) = 1 − Λ_m(0). As the
project can evaluate Λ_m for arbitrary hypothetical data while the frontier has only m ≤ 2, one obtains a
well-posed *requirement curve*: the minimal order 2m* needed to certify a target proportion c, and the
admissible moment data achieving it. Testable form: for the frontier's normalisation, compute the maximal
c(m) for m = 1,2,3 over admissible moment data; any published value of c(2) or c(3) is an immediate check.
This inverts the frontier's theorem into a "what would have to be known" statement.

**Candidate B (类比, flagged).** The frontier's extremal measure attaining Λ_m(0) is finitely supported
(at most m+1 atoms), whereas the project's finding is that off-line configurations give finite-rank
positive measures (rank = number of distinct δ-orbits). Both are finite-rank / finite-support statements
about the same kind of moment matrix. This is an **analogy of sharpness structure, not an identity**; it
is recorded here because it is the only structural point where the two constructions visibly touch.

## 7. Verdict (single decisive sentence)

The interface is genuine at the level of the object — the frontier's Λ_m is precisely a Hankel-matrix
inverse, the species the project manipulated in P36.3 — and it yields a well-posed but currently
one-sided testable quantity (the requirement curve of §6); it yields no new bound on the proportion,
because the two sides use different moment sequences and the frontier's sole advantage is the
availability of m₁, m₂ — exactly the availability the project has shown it cannot reproduce for its own
δ-moments.

## 8. Boundaries

- [核验] in-repo: P36.3, R3-IV/V, bridge-sym-moments, iteration-2-5. [引用] frontier §7.2(d) and HL*(k₀).
- **Unread:** the frontier's §7.2 full text; [BGSTB24]; the project's own ASF documents beyond the register
  entry in `docs/EXPLORATION-POINTS-REGISTER.md` (E13) and `docs/p47-g253-asf-audit.md`.
- No claim about RH is made or implied.
