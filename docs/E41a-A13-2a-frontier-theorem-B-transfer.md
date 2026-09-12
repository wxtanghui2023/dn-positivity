# E41(a) / A13-2(a) — Transferring the frontier's Theorem B to Dirichlet L-functions

**Registered as:** exploration item **E41** (`docs/EXPLORATION-POINTS-REGISTER.md`) and register item
**A13-2(a)** (`docs/PENDING-ITEMS-MASTER.md`).
**Naming (the label collision, resolved).** This is the *other* A13-2. `docs/A13-2-theorem-B-transfer.md`
transferred the **project's own classical theorem** — Brown's converse inequality — to `L(s,χ)`; the collision
is documented in `docs/A13-2b-theorem-B-label-collision.md`, whose §4 item N2 records A13-2(a) as not yet
done. That is this note.
**A finding that changes the framing.** The frontier paper's **Theorem B already *is* the Dirichlet
statement** — it says Theorem A "holds verbatim for `L(s,χ)` … for any fixed primitive Dirichlet character
`χ`" — and the paper supplies its own one-paragraph proof of it. So the registered claim ("it holds verbatim
for the L-functions of Dirichlet characters") is the paper's own theorem, not a transfer the project must
construct. This note is therefore an **audit of the paper's transfer step**, hypothesis by hypothesis.
**Retrieval.** `arxiv.org/html/2608.13637v2` and the v2 PDF were retrieved; Theorem A, Theorem B, the inputs
list, the (Z)/(P)/(L) architecture and the paper's *Proof of Theorem B* are quoted from them. `[引用]`
**Labels:** `[核验]` verified here · `[引用]` quoted · `[推导]` derived/read here · `[猜想]` conjecture.
Nothing below claims a proof of RH; the frontier result is a proportion statement, not RH.

---

## §1 The frontier's exact statements `[引用]`

- **Theorem A.** "As T → ∞, (i) `N₀ˢ(T,2T) ≥ (⅔ − o(1))N(T,2T)`, (ii) `N_d(T,2T) ≥ (⅚ − o(1))N(T,2T)`."
  With the Montgomery–Taylor window the constants become `2 − c_MT^{−1} = 0.67250…` and
  `½(3 − c_MT^{−1}) = 0.83625…`; the ceiling over all bandwidth-one certificates is ≈ 0.682 (§7.2).
- **Theorem B (verbatim).** "Theorem A holds verbatim for `L(s,χ)` in place of `ζ(s)`, for any fixed
  primitive Dirichlet character `χ`."
- **The inputs (verbatim).** "Weil's explicit formula, the Riemann–von Mangoldt formula and the bound
  `N(t,t+1) ≪ log t`, Stirling's estimate for `Γ′/Γ`, Chebyshev–Mertens estimates for `Σ_{n≤X}Λ(n)²` and
  `Σ_{n≤X}Λ(n)²/n`, and the Montgomery–Vaughan inequality for the frequencies `{log n : n ≤ X}`, `X ≤ T`.
  No mollifier, zero-density estimate, or zero-free region is used."
- **The paper's own transfer step (verbatim).** "**Proof of Theorem B.** Replace `ζ` by `L(s,χ)`, `χ` primitive
  mod `q`: in (2.1), `μ` gains `−log q/2π` and the `Γ`-factor shifts to `(1+a_χ)/4 + iτ/2`, `Λ(n)` becomes
  `Λ(n)χ(n)`, and the pole terms are absent for `χ ≠ χ₀`. The functional equation still pairs `ρ ↔ 1−ρ̄`.
  Propositions 4.1–5.5 and Theorem 5.7 go through with `O_q(·)` errors (`|χ| ≤ 1`); the chain (1.2) is
  unchanged."
  *(The fractional constants are rendered from PDF extraction and are lossy at the ½, ¼ level; read them
  against the counting constants in §4.)*
- **Implied-constant scope (verbatim).** "Throughout §§4–6 the implied constants depend only on `χ` and `ψ`."
- **The chain (1.2) and its ingredients.** `(Z)`: up to a trace-norm `o(1)` tail, `G̃ = P + Q`, each distinct
  on-line zero contributing a rank-one positive form to `P` and each off-line pair `{ρ, 1−ρ̄}` a block of
  signature `(1,1)` to `Q`; `tr P ≤ N₀`, `n₊(Q) ≤ p`, `N ≥ s₁ + 2s₂ + 2p`, `tr G̃ = (1+o(1))N`. `(P)`:
  `‖G̃‖²_HS = (R(ψ) + o(1))N`, with `R(ψ)` window-only (`R(ψ₀) = 4/3`, `R(ψ_MT) = c_MT^{−1}`). `(L)`:
  `rank P₁ ≥ 2 tr P₁ + 4 tr Q′ − 4b − ‖P₁ + Q′‖²_HS` (Lemma 3.2; `n₊(Q′) ≤ b`). Then
  `N₀ˢ + o(N) ≥ rank P₁ ≥ 4 tr G̃ − 2N − ‖G̃‖²_HS = (2 − R(ψ) − o(1))N`.

---

## §2 Instantiation
Fix a primitive character `χ mod q` (the eight moduli of interest are `q ∈ {3,4,5,7,8,9,11,13}`). Write
`N_χ(T,2T)`, `N_χ(t,t+1)` for the multiplicities-with-multiplicity counts of `L(s,χ)`, and `s₁, s₂, p` for the
numbers of simple on-line zeros, multiple on-line points and off-line pairs in the window. The window
`ψ`, the modulation grid `α_k = T + 2πk/L` and the matrices `G̃, P, Q, Ẽ` are defined exactly as in the
paper, with `L`, `d` and `N` now the `χ`-dependent quantities of §4. `[推导]`

---

## §3 Hypothesis-by-hypothesis verdict for a primitive `χ mod q`

| # | Input of the argument | Verdict | Why |
|---|---|---|---|
| 1 | Window `ψ`, modulation `α_k = T + 2πk/L`, `d` points in `[T,2T)` (§2) | **holds; one constant changes** | Uses only `T` and the ordinates `γ_ρ`. But the number of points must be ≈ the number of zeros, so `d ≈ N_χ(T,2T)`, not `N(T,2T)` (see §4). |
| 2 | Poisson–Gabor identity (Lemma 2.1) | **verbatim** | Pure Fourier analysis (Poisson summation); no arithmetic, no `χ`. |
| 3 | `(Z)` block structure (Props 4.1–4.3): `P ⪰ 0`, `rank P ≤ N₀*`, pair ↦ signature `(1,1)`, `tr G̃ = (1+o(1))N` | **verbatim up to the counting normalisation** | Rank and inertia are basis-free linear algebra; only the normalisation `N` changes. |
| 4 | The pairing `ρ ↔ 1−ρ̄` (makes `G̃, Ẽ` real symmetric and blocks `Q`) | **holds; the only zeta-specific input** | The paper states "the functional equation still pairs `ρ ↔ 1−ρ̄`". For real `χ` this is the self-duality of `L(s,χ)`; for complex `χ` the involution is the functional equation composed with complex conjugation (which is also why the coefficients are not real). Its fixed points are exactly the on-line zeros (`β = ½`), so the on/off dichotomy and the `(1,1)` blocks survive. `[推导]` |
| 5 | `(L)`: `rank P₁ ≥ 2 tr P₁ + 4 tr Q′ − 4b − ‖P₁ + Q′‖²_HS`; Lemma 3.4 (Weyl) | **verbatim** | Pure linear algebra (Sylvester inertia, von Neumann/Weyl); no arithmetic. |
| 6 | `(P)`: `‖G̃‖²_HS = (R(ψ) + o(1))N`, `R(ψ)` window-only | **shape verbatim; modulus-dependent constants** | `Λ(n) → Λ(n)χ(n)` and `O_q(·)` errors, controlled by `|χ| ≤ 1` (paper, verbatim). `R(ψ₀) = 4/3` and `R(ψ_MT) = c_MT^{−1}` are unchanged, being window-only. |
| 7 | Explicit-formula engine (2.1): `μ` gains `−log q/2π`; `Γ`-factor `(1+a_χ)/4 + iτ/2`; pole terms absent for `χ ≠ χ₀` | **modulus-dependent (bounded, parity only)** | `a_χ = (1−χ(−1))/2 ∈ {0,1}`: the archimedean factor changes by a bounded, `q`-independent amount; a fixed primitive `χ mod q` with `q > 1` is non-principal, so no pole term arises. |
| 8 | Riemann–von Mangoldt + `N(t,t+1) ≪ log t` | **modulus-dependent constants** | For `L(s,χ)`: `N_χ(t,t+1) ≪ log(qt)` and zero density `(1/π)log(qt/2π)`; the constants are computed in the companion note (§4). |
| 9 | Chebyshev–Mertens: `Σ_{n≤X}Λ(n)²`, `Σ_{n≤X}Λ(n)²/n` | **verbatim** | These are `χ`-free sums; the `χ`-twisted versions are dominated by them since `|χ(n)| ≤ 1`. |
| 10 | Montgomery–Vaughan for the frequencies `{log n : n ≤ X}` | **verbatim** | A statement about a frequency set; no `χ` and no `L`-function enters. |
| 11 | Stirling for `Γ′/Γ` | **modulus-dependent constant** | Same estimate with the shifted argument of row 7. |

**Grouped as requested.** *Imaginary-part-only inputs* (rows 1, 2, 3, 5, and the involution of row 4):
unchanged, with row 1's grid size the sole rescaling. *Inputs using the counting function of the L-function*
(rows 1, 8, and the `N` in rows 3 and 6): need `q`'s constants, already written out in the companion note.
*The zeta-specific functional equation* (row 4): the only place where `ζ` is special, and it transfers
because the `χ`-functional equation supplies the same pairing. **Verdict: nothing fails.** Every row is
"verbatim", "verbatim up to a constant", or "modulus-dependent constant".

---

## §4 The modulus-dependent constants (used, and where they come from)
From `docs/A13-2-theorem-B-transfer.md` §3 `[推导]`: RvM for a primitive `χ mod q` gives
`N_χ(T) = (T/π)log(qT/(2πe)) + O(log qT)`, hence `a_q = 1/π` and `b_q = (log(q/2π) − 1)/π`; `3a_q + b_q > 0`
for all `q ≥ 3`; and `b_q < 0 ⟺ q < 2πe ≈ 17.079`, satisfied by all eight moduli. The local zero density
becomes `(1/π)log(qt/2π)` in place of `(1/2π)log(t/2π)`.
Consequence for the present argument: the window length and grid are governed by `L_χ = log(qT/2π)` in place
of `L = log(T/2π)`, and `N_χ(T,2T)/N(T,2T) → 2·log(qT/2π)/log(T/2π) = 2(1 + log q / log T)`. This is a
**ratio-preserving rescaling**: the proportion `⅔` (and `⅚`) is unchanged, and only the `o(1)` quality and
the explicit errors move. Equivalently, the `O_q(·)` errors of the paper's proof are, for these eight moduli,
swollen by the factor `2(1 + log q/log T) = 2 + O(1/log T)`. `[推导]`

---

## §5 Remaining gaps (do not overclaim)

- **G1 — explicitness.** The `O_q(·)` errors are not explicit in the paper; "verbatim" holds for the
  constants `⅔` and `⅚` with an `o(1)` that may depend on `q`.
- **G2 — no uniformity in `q`.** Theorem B is for a **fixed** primitive `χ` (`q` fixed, `T → ∞`). Applying it
  to eight moduli yields eight statements, not one uniform statement. Nothing here should be read as
  uniformity in `q`.
- **G3 — the `χ`-explicit formula.** The form (2.1) with the conductor term in the archimedean factor is
  accepted as standard `[引用]`; it was not re-derived here.
- **G4 — inherited constants.** The explicit constants `c_q, d_q` of the counting hypothesis remain
  **unverified for any of the eight moduli** — the same gap as `docs/A13-2-theorem-B-transfer.md` §4 (G2).
- **G5 — trivial zeros.** Trivial zeros of `L(s,χ)` have `Im = 0` (`s = −2,−4,…` for even `χ`;
  `s = −1,−3,…` for odd `χ`), so they do not enter `Σ_{|Im ρ| > H}`; they affect only the constant term.
  `[推导]`
- **G6 — what E41(a) actually is.** The registered claim is the paper's Theorem B; the project's contribution
  is the hypothesis audit of §3, not a new theorem.

---

## §6 Boundary
The frontier text is untrusted external material; quotations are as retrieved and PDF-rendered.
Nothing in this note asserts a proof of RH. Theorems A and B are proportion results (`⅔`, `⅚`) — upper
bounds below `1` for that certificate class, exactly as the project's "detection ≠ exclusion" line expects
(`docs/A3-1-moving-edge-necessity.md` §5). The eight-moduli application inherits the scope of the upstream
result: fixed `χ`, `T → ∞`, no uniformity in `q`, and the explicit-constant gaps G1/G4.

**One-line summary.** Every hypothesis of the frontier's Theorem B transfers to a fixed primitive `χ mod q`;
several inputs need only bounded, computable modulus-dependent constants (the counting constants already
written out in the companion note), the single zeta-specific input is the functional equation and its pairing
`ρ ↔ 1−ρ̄` survives, and nothing fails — the residual gaps are explicitness and uniformity in `q`, not structure.
