# A Pair-Positivity Criterion for the Generalized Riemann Hypothesis, with Eight-Modulus Verification and the GRH → Goldbach Chain

**Hui Tang** — Independent Researcher — ORCID 0009-0003-5745-4820
Draft v1, 2026-09-12. Companion note: `docs/A13-2-theorem-B-transfer.md`.

**Labels used below:** 核验 (verified numerically) · 引用 (from the literature) · 推导 (derived) · 猜想 (conjecture).

---

## Abstract

We present an **equivalent criterion** for the Generalized Riemann Hypothesis (GRH) and verify it numerically for eight moduli. For a primitive Dirichlet character χ mod q, with L(s,χ) its L-function and ρ = ½ + δ_ρ + iγ_ρ its nontrivial zeros, we define a spectral functional Q_χ and its projection Q′_{RH,χ} (obtained by δ_ρ ↦ 0) and prove the **orbit identity**
  Q_χ − Q′_{RH,χ} = Σ_{orbits} m_ρ P_{γ_ρ}(δ_ρ),   P_γ(δ) = δ²M₂/(2U²D₊D₋),
where P_γ is a closed-form **pair discrepancy** with all-positive coefficients whenever γ > 1/√5. Every L-zero has γ ≥ 6.02 > 1/√5, so P_γ(δ) ≥ 0 with equality iff δ = 0, hence **Q_χ = Q′_{RH,χ} ⟺ all zeros of L(s,χ) lie on Re s = ½**.

**This is a criterion, not a proof.** The orbit identity is unconditional [推导]; the *equality* Q_χ = Q′_{RH,χ} is **not proved** and is exactly as hard as GRH — it has the same logical status as Weil positivity or Li's criterion. We claim no proof of RH or GRH. Concretely, **unconditional** are the kernel/test-object algebra, the closed forms of w_H and P_γ, the orbit identity, the convergence lemmas, and the criterion equivalence itself; **conditional on GRH** are ψ(x;q,a) = x/φ(q) + O(x^{1/2}log²x) and the Goldbach asymptotic R(n) ~ (S(n)/2)·n/log²n for sufficiently large even n. Numerically (moduli 3, 4, 5, 7, 8, 9, 11, 13) all computed zeros lay on the critical line, the identity Q_χ − Q′_{RH,χ} = ΣP_γ held to machine precision (max relative deviation 1.4×10⁻¹⁰), and P_γ decayed as γ⁻⁶. A previously attempted unconditional proof of the equality is recorded as **broken** and is not resurrected.

---

## 1. Introduction and statement of the criterion

RH and its generalization GRH to Dirichlet L-functions remain open. There is a family of **equivalent characterisations**: classical Weil positivity for the explicit formula [引用, Weil 1952; Barner 1981] and Li's criterion λ_n ≥ 0 for all n [引用, Li 1997; Lagarias 2007]. The criterion below belongs to this family: it is an equivalent reformulation built from a symmetric kernel with a **pair-positivity** property of a function-equation orbit.

**Setup.** Let χ be primitive mod q, L(s,χ) = Σ_{n≥1} χ(n)n^{−s}, completed function
  ξ_χ(s) = (q/π)^{(s+a)/2} Γ((s+a)/2) L(s,χ),  a = (1 − χ(−1))/2 ∈ {0,1},
with ξ_χ(s) = ε_χ ξ_{χ̄}(1−s), |ε_χ| = 1. Nontrivial zeros are ρ = ½ + δ_ρ + iγ_ρ with multiplicity m_ρ. The functional equation together with conjugation symmetry forces the zero set to be closed under ρ ↦ 1 − ρ̄ (same height γ, opposite δ) — an **orbit**: off-line orbits carry two zeros {½+δ+iγ, ½−δ+iγ}, on-line orbits one (δ = 0) [推导; complex-character case: `docs/grh-strict-a1-orbit.md`].

**Objects (universal — independent of q and χ).**
  K^nat_ρ(t) = (δ_ρ² − (t−γ_ρ)²)/(δ_ρ² + (t−γ_ρ)²)²  [推导, Hadamard; 引用 Davenport],
  H₀(t) = −(1/4π) log(1+t²) + 1/(2π(1+t²)),  H₀″(t) = O(t^{−2}) ∈ L¹,
  w_H(γ,δ) = [a²(a+1) + δγ²]/[2(a²+γ²)²],  a = 1+δ,
where w_H is the termwise pairing ⟨K^nat_δ(·−γ), H₀⟩ taken through the L¹ Fourier product (§2).

**Main identity.** Define Q_χ = −Σ_ρ m_ρ w_H(γ_ρ,δ_ρ) and Q′_{RH,χ} = −Σ_ρ m_ρ w_H(γ_ρ,0) (projection of every zero onto the critical line, preserving ordinate and multiplicity). Then [推导]
  **Q_χ − Q′_{RH,χ} = Σ_{orbits} m_ρ P_{γ_ρ}(δ_ρ) ≥ 0,  P_γ(δ) = 0 ⟺ δ = 0.**

**Theorem 1.1 (criterion).** For ζ (trivial character, q = 1) and for every primitive χ: Q = Q′_{RH} ⟺ all zeros satisfy Re ρ = ½. Equivalently, RH holds iff the ζ-criterion holds, and GRH holds iff the χ-criterion holds for every χ. **Theorem 1.2 (family consistency).** K^nat, H₀, w_H, P_γ do not depend on q or χ; hence GRH ⟺ Q_χ = Q′_{RH,χ} for all χ [推导].

**Standing disclaimer.** The criterion is an *equivalent characterisation*; it does not prove RH or GRH, since proving Q_χ = Q′_{RH,χ} is no easier than the original problem (§5). The repository's own position is recorded in `verification/independent_core_note.md` ("**Not** a proof of RH") and `docs/CHAIN-AUDIT-do-we-have-a-proof-chain.md` ("证明链不存在").

---

## 2. The pair-positivity computation and its exact form

**2.1 The weight (Parseval, termwise).** In the 2π-convention f̂(u) = ∫f(t)e^{−2πiut}dt, one has K̂^nat_δ(u) = 2π²|u|e^{−2πδ|u|} and Ĥ₀(u) = e^{−2π|u|}[1/(4π|u|)+½], so K̂^nat_δ·Ĥ₀ = (π/2)e^{−2πa|u|} + π²|u|e^{−2πa|u|} ∈ L¹ (the |u|·1/|u| singularity at u = 0 cancels). Two elementary integrals give [推导; 核验 to 100 digits, `docs/grh-criterion-proof.md` §3.2]
  **w_H(γ,δ) = [a²(a+1) + δγ²]/[2(a²+γ²)²],  a = 1+δ,  w_H(γ,0) = (1+γ²)^{−2} =: w_target(γ).**
The pairing is defined **termwise**; we do not claim it equals a single pairing of ∂_t²log|ξ_χ| against H₀ (§5 of `docs/grh-criterion-proof.md`).

**2.2 Pair discrepancy (exact algebra).** With U = 1+γ², D_± = ((1±δ)²+γ²)²,
  **P_γ(δ) = 2w_H(γ,0) − w_H(γ,δ) − w_H(γ,−δ) = δ² M₂/(2U²D₊D₋)**,
  M₂ = 8U²(5γ²−1) + 4(5U²−16U+16)δ² + 16(U−2)δ⁴ + 4δ⁶.
For |δ| < ½ and γ > 1/√5 the coefficients are positive: 5γ²−1 > 0; 5U²−16U+16 > 0 (discriminant −64 < 0); U−2 > 0. Hence **P_γ(δ) > 0 for δ ≠ 0 and P_γ(0) = 0** [推导; 核验]. Since every L-zero satisfies γ ≥ γ_{1,χ} ≥ 6.02 > 1/√5 (smallest: β mod 4) [引用/核验, `docs/grh-family-consistency.md` §2], positivity is automatic. **Observation 2.1 (decay).** For fixed δ, γ → ∞, P_γ(δ) ~ 20δ²γ^{−6}: the positive term decays as the sixth power of the height [推导; 核验 γ⁶P_γ → 0.200000 at δ = 0.1, `docs/grh-migration-probe.md` 扩展6].

**2.3 Orbit identity and convergence.** Splitting over orbits gives Q_χ − Q′_{RH,χ} = Σ_{ρ/~} m_ρ P_{γ_ρ}(δ_ρ). Termwise absolute convergence follows from |P_γ(δ)| ≤ Cγ^{−6} and N_χ(T) = O(T log T) [引用, standard]. The exchange of summation and pairing is justified by the difference-form estimate |w_H(γ,δ) − w_H(γ,0)| ≤ C|δ|·|H₀″(γ)| with C ≤ 4 uniformly for γ ∈ [6.02, 10⁵], δ ∈ [0.01, 0.49] [核验; `docs/grh-criterion-proof.md` §5]. (An earlier claim C ≤ π fails near γ = 6.02 and was corrected — see the erratum trail there.)

---

## 3. Eight-modulus verification

Zeros of L(s,χ) were located numerically for eight moduli; all had Re ρ = 0.500000, and for each modulus the identity Q_χ − Q′_{RH,χ} = ΣP_γ was checked against its closed form. "Max deviation" is the largest relative deviation over the tested heights and δ ∈ [0.01, 0.49]; "decay" is the exponent in P_γ ≍ γ^{−exp} [核验/推导].

| q | character (order; parity) | zeros computed | max rel. deviation | decay exp. |
|---|---|---|---|---|
| 3 | real quadratic (2; odd) | 98 (γ < 200) | 9.9×10⁻¹⁵ | 6 |
| 4 | real (χ₄ = β, 2; odd) | 168 (γ < 300) | 2.7×10⁻¹⁴ | 6 |
| 5 | complex (4; odd) | 83 (γ < 150) | 2.0×10⁻¹⁴ | 6 |
| 5 | real quadratic (2; even) | n.r. | 1.4×10⁻¹² | 6 |
| 7 | complex (6; odd) | 60 (γ < 120) | 1.4×10⁻¹⁰ | 6 |
| 8 | real quadratic (2; even) | n.r. | 2.3×10⁻¹¹ | 6 |
| 9 | complex (6; odd; composite modulus) | 59 | 1.1×10⁻¹¹ | 6 |
| 11 | complex (10; odd) | 56 (γ < 100) | 1.4×10⁻¹¹ | 6 |
| 13 | complex (12; odd) | 53 | 3.6×10⁻¹² | 6 |

**Notes (honest).** (1) "n.r." = the count is **not recorded** in the archived document; only the deviation range was logged for that character — we do not supply numbers the archive lacks. (2) On-line findings are **finite-range numerical evidence**, not GRH (a necessary-condition check) [核验]. (3) The decay exponent 6 is *universal* (algebraic), so that column cross-checks the closed form rather than measuring each modulus independently. (4) Discriminating power was tested separately: 100 random off-axis configurations gave Q−Q′ = ΣP_γ > 0 (minimum +1.5×10⁻¹⁷), all-on-line gave a zero signal [核验, `docs/grh-migration-probe.md` 扩展5]. (5) The orbit-closure lemma for complex characters (moduli 5, 7, 9, 11, 13) has a proof script `scripts/a1_orbit_verify.py` [推导/核验].

| Claim | Evidence |
|---|---|
| w_H closed form | `docs/grh-criterion-proof.md` §2.1, §3.2; `verification/independent_core_note.md` (O3) |
| P_γ closed form, positivity | `docs/grh-criterion-proof.md` §3.3; `docs/grh-criterion-theorem.md` |
| Orbit identity Q−Q′ = ΣP_γ | `docs/grh-criterion-proof.md` §4; `docs/rh-discriminator-theorem.md` |
| γ⁻⁶ decay, constant 20δ² | `docs/grh-migration-probe.md` 扩展6; §2 Obs. 2.1 |
| Eight-modulus table (counts, deviations) | `docs/grh-migration-probe.md` 扩展1–5; `docs/grh-criterion-theorem.md` |
| γ_{1,χ} ≥ 6.02 | `docs/grh-family-consistency.md` §2 |
| Orbit closure, complex χ | `docs/grh-strict-a1-orbit.md`; `scripts/a1_orbit_verify.py` |
| Exchange/convergence, C ≤ 4 | `docs/grh-criterion-proof.md` §5 |
| "Not a proof of RH" status | `verification/independent_core_note.md`; `docs/CHAIN-AUDIT-do-we-have-a-proof-chain.md` |

---

## 4. The end-to-end chain GRH → primes in AP → Goldbach asymptotic

The chain has three links: (A) the criterion above; (B) GRH ⟹ distribution of primes in arithmetic progressions; (C) circle method ⟹ Goldbach asymptotic.

**(A) Criterion [ours; 推导, conditional in its equality].** Link (A) supplies the *equivalence* GRH_χ ⟺ Q_χ = Q′_{RH,χ}; it does **not** supply GRH. Its role is logical: were the equality established for all χ, GRH would follow and activate (B).

**(B) GRH ⟹ AP [引用, standard; conditional on GRH].** The explicit formula for ψ(x;q,a) = Σ_{n≤x, n≡a (q)} Λ(n), ψ(x;q,a) = x/φ(q) − Σ_χ χ̄(a) Σ_ρ x^ρ/ρ + …, is **unconditional** as an identity [引用, Davenport]. Under GRH, ψ(x;q,a) = x/φ(q) + O(x^{1/2}log²x) for q ≤ x [引用, conditional].

**(C) AP ⟹ Goldbach [引用, standard; conditional on GRH].** By the Hardy–Littlewood circle method, under GRH the unordered representation function satisfies R(n) = (S(n)/2)·n/log²n·(1+o(1)), with S(n) = 2C₂ Π_{p|n, p>2}(p−1)/(p−2), for **sufficiently large** even n [引用, Hardy–Littlewood 1923]; Goldston's refinement gives E(x) ≪ x^{1/2}log³x [引用].

| Step | Status |
|---|---|
| Kernel/H₀/w_H/P_γ algebra; orbit identity; criterion equivalence (Thm 1.1–1.2) | **unconditional** [推导] |
| Eight-modulus numerical checks (zeros on line; identity to machine precision) | **finite-range evidence** [核验] |
| Explicit formula for ψ(x;q,a) (identity) | **unconditional** [引用] |
| ψ(x;q,a) = x/φ(q) + O(x^{1/2}log²x) | **conditional on GRH** [引用] |
| R(n) = (S(n)/2)·n/log²n·(1+o(1)), sufficiently large n; E(x) ≪ x^{1/2}log³x | **conditional on GRH** [引用] |
| Equality Q_χ = Q′_{RH,χ} (hence GRH) | **NOT proved** (§5) |

**Numerical chain checks [核验, finite range].** With primes up to 10⁹: mod-5 residue-class counts are uniform to ratio 0.9999–1.0001 with deviation ∼√x, consistent with the GRH error term [核验, `docs/grh-migration-probe.md` 扩展8]; the Goldbach ratio R(n)/((S(n)/2)n/log²n) → 1 with (ratio−1)log n ≈ 2.2 [核验, 扩展7]. These are finite observations, not proofs.

---

## 5. Honest limitations

**5.1 What is *not* proved.** The equality Q_χ = Q′_{RH,χ} is unproved; only the *equivalence* "equality ⟺ GRH_χ" is proved. The criterion therefore has exactly the status of Weil positivity or Li's criterion: a restatement of GRH, not a route to it. No arithmetic input is used beyond the functional equation and N_χ(T) = O(T log T) [引用].

**5.2 The failed attempt (recorded; not resurrected).** `docs/candidate-proof-v1.md` attempted to prove D = Σ_ρ[h̃(ρ) − h̃(½+iγ_ρ)] = 0 **unconditionally**, via a Hadamard evaluation of Σ_ρ[1−(ρ−½)²]^{−2} in closed form. It is broken for two recorded reasons. (i) **Projection obstacle:** D = Q − Q′_{RH} cannot be evaluated from ξ_χ without the zero configuration; there is no non-zero-configuration source for D [推导; `docs/grh-strict-b1-obstacle.md`]. The "closed-form" step assumes the on-line configuration it aims to prove (the identity Σq(γ_ρ) = C₁ holds termwise only when δ_ρ = 0). (ii) **β-wall:** the Weil explicit formula is a *γ-channel* — it sums h over the ordinates γ_ρ only and cannot see β = ½ + δ; the discrepancy is δ²-order and thus invisible to the arithmetic side [推导; `docs/grh-conduction-chain-rederive.md` §3–4; `docs/ARCHIVE-P34-FINAL-2026-09-02.md` "β 墙的形态清单"]. A companion attempt to derive GRH from RH by "mechanism unity" (`docs/grh-conduction-chain-v3.md`, `docs/grh-strictify-under-RH.md`) is likewise broken: it fails at the *member-transfer* step (ζ's on-line configuration does not put χ's configuration in the zero set) and at the **mod-q information gap** (RH is a conductor-1 statement; ψ_χ needs χ-weighted information RH does not supply) [推导; `docs/grh-derivation-endpoint.md`]. An attempt to render D as a finite "arg ζ + N₀ + Weil" expression (`docs/finite-analysis-D.md`) was recorded as hitting walls in all finite-isation routes [推导; `docs/SUMMARY-NEW-FRAMEWORK-2026-09-02.md` §2.1]. We record these so the equality is *not* claimed and the failed routes are not repeated.

**5.3 Scope caveats.** (a) S_{reg,χ} (trivial-zero / Γ-constant background) does not enter Q or Q′ and is excluded at the level of definition; the criterion does not require S_{reg,χ} = 0 [推导; `docs/grh-criterion-proof.md` §6]. (b) The Weil-interface check for L(s,χ) (prime side, absolute convergence via |χ(p)| ≤ 1) is an optional cross-check, not a dependency [推导; `docs/grh-criterion-theorem.md` §2.3]. (c) The "sufficiently large" threshold in (C) is of Hardy–Littlewood type (~10⁵⁰) and cannot be bridged to the finite verification range (4×10¹⁸): GRH yields the asymptotic plus an exception count, **not** Goldbach for every even integer [推导/引用; `docs/grh-goldbach-proof-chain.md` C6]. (d) The construction's status is "equivalent characterisation, pending independent verification"; the repository's INVALID-first protocol applies [核验; `verification/independent_core_note.md`]. (e) The repository also carries an internal erratum correcting a per-orbit inertia count from 1 to 2 (factor 2) in the separate negative-index/Bombieri line [核验; `docs/ERRATUM-inertia-factor2.md`]; that line is *not* the criterion studied here, and the criterion's P_γ positivity and the orbit identity are unaffected.

**5.4 No RH/GRH proof claimed.** As this project's standing discipline requires: nothing here proves RH or GRH, and the equality that would do so is open. The contribution is a criterion with explicit positive structure, eight-modulus numerical support, and an honest map of the end-to-end conditional chain.

---

## References

Only works already cited in the repository's own documents are listed.

1. A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265.
2. K. Barner, *On A. Weil's explicit formula*, J. Reine Angew. Math. **323** (1981), 139–152.
3. X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory **65** (1997), 325–333.
4. J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst. Fourier **57** (2007), 1689–1740.
5. H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer (2000).
6. H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. **53** (2004).
7. G. H. Hardy, J. E. Littlewood, *Some problems of "Partitio numerorum" III*, Acta Math. **44** (1923), 1–70.
8. D. A. Goldston, *On Hardy and Littlewood's contribution to the Goldbach conjecture* (exception count under GRH).
9. E. Bombieri, J. C. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, J. Number Theory **77** (1999), 274–287.
10. F. C. S. Brown, *Li's criterion and zero-free regions of L-functions*, J. Number Theory **111** (2005), 1–32.
11. A. D. Droll, *Variations of Li's criterion for an extension of the Selberg class*, PhD thesis, Queen's University, 2012.
12. N. Palojärvi, *Explicit zero-free regions and a τ-Li-type criterion*, arXiv:1807.01506.
13. W. Banks, arXiv:2303.09510 (GRH ⟺ RH plus mod q uniformity).
14. S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. **214** (2024), 357–376.
15. L. Guth, J. Maynard, zero-density theorem (2024 announcement; published 2026).
