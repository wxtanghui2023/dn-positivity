# Notes on conversion criteria and their obstructions

**Abstract.** These are nine short, self-contained observations from the `dn-project` archive. Each states one sharply delimited fact: a small structural identity, a numerical scaling law, an explanatory dichotomy, or a negative result about a *specific* proposed route. **None of them is progress toward a proof of the Riemann hypothesis, and nothing here is offered as such.** Every observation is either (a) a restatement of a classical fact the archive verified in a small instance, or (b) a negative statement about a route the archive tested, scoped exactly as the archive scopes it. Two conventions are used throughout: the archive's honesty rule, that a certificate **not found** is reported as "not found here" and never as "does not exist"; and its labels, 核验 (verified here), 引用 (quoted from a source), 推导 (derived here), 猜想 (conjecture).

---

**N1. Rank deficiency of a positive semidefinite Toeplitz matrix is exactly the content of the classical
"real zeros" mechanism.** [引用] Carathéodory–Fejér (1911): if `T` is a Hermitian positive semidefinite
Toeplitz matrix of size `n+1` and rank `n`, and `ξ ∈ ker T`, then all roots of `P(z) = Σ_{j≤n} ξ_j z^j` lie on
the unit circle (Corollary 1.1 of the Connes–van Suijlekom framework, `docs/CVS4-corollary-and-hurwitz-route.md`
§1). [核验] The archive verified the mechanism on the minimal family of symmetric measures with `r = n/2`
atoms: `rank T = n`, deficiency `1`, palindrome defect `≤ 7·10⁻¹³`, `max|root| − 1 ≤ 7·10⁻¹³`, in 6 of 6 cases
(`docs/CVS1-verified-minimal-instance.md` §1). [推导] Two control runs isolate the two necessary hypotheses:
`r = n` atoms gives full rank, so nothing is forced; a signed weight breaks positive semidefiniteness, so
nothing is forced. Because Corollary 1.1 is a direct corollary of a 1911 theorem, this is a verification of a
*classical* mechanism, not a new result. [推导] The structural reading the archive adds is that **full rank
means vacuous and rank deficiency means content** — which is why instantiating such a criterion with the
zeros themselves degenerates (`docs/TPX-verdict-tp-instantiation-degenerates.md`; summarised in
`docs/E23-lee-yang-dqpt-report.md` §6). Source: `docs/CVS1-verified-minimal-instance.md`,
`docs/CVS4-corollary-and-hurwitz-route.md`.

**N2. Positivity methods admit a trichotomy, and only the RH-equivalent branch is sharp.** [推导] Let `P ≥ 0`
be a positivity form on a configuration space and call its zero set the *vanishing locus*. Then exactly three
cases arise: (i) the locus is everything (`P ≡ 0`) and the form carries no information; (ii) the locus is too
small (`P > 0` everywhere) and the form can only exclude open regions, never an individual configuration; and
(iii) the locus is exactly the set of off-critical configurations, in which case the form's positivity *is*
the Riemann hypothesis. Hence "find a stronger positivity form" is not a viable programme: a form that is both
sharp and non-empty is RH-equivalent, and a form that is provable is one of the first two cases. [核验] The
classical instance behaves exactly this way: `3 + 4cos t + cos 2t = 2(1 + cos t)² ≥ 0` vanishes precisely at
`t ≡ π (mod 2π)`, which is why the de la Vallée Poussin region's margin `c/(log t)^{2/3}(log log t)^{1/3}`
shrinks without ever becoming uniform (`docs/POS1-positivity-dichotomy.md` §0, §1). Source:
`docs/POS1-positivity-dichotomy.md`.

**N3. Six provably-positive mechanisms are known, and none escapes.** [推导] The archive enumerates the known
sources of *provable* non-negativity and records where each one ends: (1) squares and sums of squares;
(2) reproducing kernels; (3) theta/Weil-type quadratic forms; (4) operator-algebraic complete positivity
(Stinespring dilations); (5) Hodge-type polarisation; (6) Perron–Frobenius for non-negative transfer
operators. Each is either insufficient (finite order, thin vanishing locus) or equivalent-to-RH/already
falsified for this purpose (`docs/POS3-provably-positive-mechanisms-enumeration.md` §2). The resulting positive
description of what is missing is a *seventh* class: canonically generated, infinite-type, provably
non-negative, and outside the six (`docs/POS3` §3). [推导] A parallel family — the universal inequalities
(Robin, Nicolas, Lagarias) — sidesteps the rigidity/adaptivity trade-off of positivity but lands in the same
gap, being `Π₁` statements that no finite verification can prove (`docs/POS3` §4). **Honesty boundary:** this
is an enumeration of the *identified* mechanisms; it is **not** a theorem that no seventh class exists
(`docs/POS3` §6). Source: `docs/POS3-provably-positive-mechanisms-enumeration.md`, `docs/POS2-positivity-paradigm-closure.md`.

**N4. Phase locking at `x = log p`: an unconditional `O_p(log X)` with a sharp numerical signature.**
[核验] For fixed prime `p`, the partial sums `Σ_{γ_k ≤ X} sin(γ_k log p)` are numerically `O(1)` over two
million zeros at exactly `x = log p = 3.8501476017` (`log 47`), with `max|Σ sin| = 6.03`, while a relative
perturbation of `10⁻⁷` in `x` inflates the same quantity to `3.3·10⁴`. [推导] The mechanism is Guinand's
explicit formula: at `x = log n` the resonant term carries `sin(T·0) = 0`, so every prime term is
`O(1/|x − log n|)`, giving `Σ sin = O_p(log X)` **unconditionally**; off resonance the nearest prime `n ≈ e^x`
forces a factor `√n log n / |x − log n|`. [推导] The distinction that matters: `O_p(log X)` is provable, but
a *genuine* `O(1)` uniform in the height is RH-equivalent, since the Weil formula's off-line zeros contribute
`e^{(β−1/2)γ log p}`. [核验] Partial maxima grow like `c√p` (`c ≈ 1–2`), which the leading term `O(log X/x)`
does not explain; recorded as an open numerical question. Source: `docs/phase-locking-guinand.md` §1–§4, §7.

**N5. A Nyman–Beurling detection threshold, with the Burnol constant appearing as its scale.** [推导] An
off-axis zero `(σ₀ = ½ + δ, γ₀)` entering the Nyman–Beurling distance `d_N` leaves a signature
`d_N² ~ N^{2δ}·A(γ₀)/log²N` with `A ~ 1/γ₀²`, so detection against the on-line baseline `C/log N` requires
`N* ~ (γ₀²·C/log N*)^{1/(2δ)}` (`docs/CVS3-cvs5-findings-and-nb-threshold.md` §3, quoting the archive's own
script header). [核验] The constant used there is Burnol's, `C_burnol = 2 + 0.5772 − log(4π) ≈ 0.0462`. [推导]
Consequence for the "conversion-rate" question: for fixed `δ`, `N*` grows polynomially in `γ₀`, i.e. this
criterion is of **weak type** (`γ₀ ≲ N^δ`), not of the `T²` type that a Li-coefficient criterion exhibits. The
archive registers the measurement as a small quantitative note (`docs/REACH-TABLE-2026-09-11.md` §四). Source:
`docs/CVS3-cvs5-findings-and-nb-threshold.md` §3; `docs/ALIGN-A4-nyman-beurling.md`;
`docs/REACH-TABLE-2026-09-11.md`.

**N6. On the random-matrix side, the two halves of the problem buy different things.** [推导] The archive's
reading of the Hermite-model/random-matrix route is asymmetric: the ordinate (`γ`) side buys the *tail*
behaviour — GORZ's Hermite modelling proves the GUE prediction in the derivative aspect — whereas the real
part (`β`) side retains only *exceptions*, since the statement "all zeros are on the line" is not a
statistical statement and no spectral statistic of the ensemble delivers it
(`docs/ALIGN-A6-A8-A9-A10-A11-B5-B7-A13.md` §B7; `docs/REACH-TABLE-2026-09-11.md` §四). [推导] The observation
is deliberately weak: it says the ensemble machinery is adequate for `γ`-statistics and inadequate for `β`,
and it is registered as a note, not a theorem. Source: `docs/ALIGN-A6-A8-A9-A10-A11-B5-B7-A13.md` §B7,
`docs/REACH-TABLE-2026-09-11.md` §四.

**N7. Negative result: extensive finite inertia does not transfer.** [推导] For finite compressions `K_N` of
the Weil form, `n₋(K_N) = N` does **not** imply the existence of a uniformly negative infinite-dimensional
sector: the negative directions can migrate to the spectral edge `0`, so that `n₋(K) = ∞` while
`inf_{‖x‖=1} −⟨Kx,x⟩ = 0`. Everything is pinned by the standard 2×2 family
`K_j = [[1, −(1+1/j)], [−(1+1/j), 1]]`, whose negative eigenvalue is `−1/j → 0⁻`. [核验] The per-orbit
negative inertia was **corrected from 1 to 2** by an erratum found while rebuilding the scripts
(`docs/ERRATUM-inertia-factor2.md`; `n₋(K_ρ) = 2`, `n₋(K_off(N)) = 2N`); replacing `N` by `2N` leaves the
qualitative conclusion intact. **Exact scope (reproduce verbatim when citing):** what is established is an
**obstruction to transfer**, not a theorem that `n₋(K_off)` is finite; the archive splits the residual
question into Problem I (`n₋(K_off) = ∞`? — unsettled) and Problem II (uniform negative sector — strong
evidence, not a theorem). Source: `docs/A3-1-moving-edge-necessity.md` §1–§2.

**N8. Negative result: detection supplies an explanation, not a bound.** [推导] On the prime side the
negative index of every finite compression is `0`; the bound `0 ≥ 0` is vacuous, so a route of this type
**bounds nothing** and must certify a positive index and a rank instead. [引用] The observation that the
negative index of finite truncations equals the number of off-line pairs is **Bombieri's** (`[Bom00]`, read
second-hand here through Conrey's survey), and the frontier paper's own record E2 states the vacuity
directly (`docs/ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md` §2; `docs/E18-NOGO-ALIGNMENT.md` §1). [推导]
The archive's own prime-side computation `n₋ = 0` had independently reached the same statement before that
record was read — two independent paths, one statement, no new result. [推导] The joint reading — **detection
is not exclusion**; a method whose ceiling is `0.682` cannot reach `1` — is an observation about two *different*
objects (a certificate class and the archive's rigidity gap), recorded as such and not as a transfer of
theorems. Source: `docs/A3-1-moving-edge-necessity.md` §3–§5; `docs/ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md` §1–§2.

**N9. Negative result of method: accumulating NO-GOs does not shrink a space; only representation theorems
do.** [推导] Negation on an unenumerated infinite space deletes one point per attempt, so the feasible set is
unchanged and the search does not converge: roughly twenty-five rounds of exploration produced about twelve
"bins" of death-causes, with later rounds re-deriving the same bins
(`docs/CLOSED-ROUTES-MAP.md` §A, §E.1). The archive's correction is explicit: the only action that shrinks a
space is a **representation theorem** — "every candidate lies in one of these `N` classes", with proof — and
its one strictly contracting classification was extended from four classes to six, all closed except the
proof-theoretic one (`docs/CLOSED-ROUTES-MAP.md` §E.2–§E.4). [推导] The companion point from the negative-result
inventory: an item recorded as "no counterpart in the literature was found" means exactly that, and
"our own" means only "attributed to no one else in the document" — an uncredited ingredient may still be
classical (`docs/E18-NOGO-ALIGNMENT-2.md` §4–§5). Source: `docs/CLOSED-ROUTES-MAP.md`,
`docs/E18-NOGO-ALIGNMENT.md`, `docs/E18-NOGO-ALIGNMENT-2.md`.

---

**References (repository documents).**
[R1] `docs/CVS1-verified-minimal-instance.md`; [R2] `docs/CVS3-cvs5-findings-and-nb-threshold.md`; [R3] `docs/CVS4-corollary-and-hurwitz-route.md`; [R4] `docs/POS1-positivity-dichotomy.md`; [R5] `docs/POS2-positivity-paradigm-closure.md`; [R6] `docs/POS3-provably-positive-mechanisms-enumeration.md`; [R7] `docs/phase-locking-guinand.md`; [R8] `docs/ALIGN-A4-nyman-beurling.md`; [R9] `docs/ALIGN-A6-A8-A9-A10-A11-B5-B7-A13.md`; [R10] `docs/A3-1-moving-edge-necessity.md`; [R11] `docs/ERRATUM-inertia-factor2.md`; [R12] `docs/ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`; [R13] `docs/E18-NOGO-ALIGNMENT.md`; [R14] `docs/E18-NOGO-ALIGNMENT-2.md`; [R15] `docs/CLOSED-ROUTES-MAP.md`; [R16] `docs/E23-lee-yang-dqpt-report.md`; [R17] `docs/TPX-verdict-tp-instantiation-degenerates.md`; [R18] `docs/REACH-TABLE-2026-09-11.md`; [R19] `docs/EXPLORATION-POINTS-REGISTER.md`.

**References (external).** [E1] Carathéodory–Fejér (1911), as used by Connes–van Suijlekom (CMP 406 (2026)); [E2] T. D. Lee and C. N. Yang (1952), circle theorem; M. E. Fisher (1965), complex-temperature zeros; [E3] A. E. Guinand (1947), explicit formula; [E4] Conrey's survey quotation of E. Bombieri `[Bom00]`, used second-hand; [E5] arXiv:2608.13637 (the frontier proportion paper, cited here only for its recorded vacuous-negative-index remark and its ceiling `0.682`).

**Status.** Notes, not results: no proof of RH, of GRH, or of any equivalent statement is claimed or approached. Each note is reproducible from the source document cited at its end, and each negative statement inherits that document's own scope caveats, including "not found ≠ does not exist".
