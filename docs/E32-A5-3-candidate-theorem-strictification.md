# E32 / A5-3 — Strictification plan for the phase-locking candidate theorem

**Date:** 2026-09-12 · **Registered:** E32 / A5-3 "候选定理严格化（Σsin = O_p(log X)）".
**Framework source:** `docs/guinand-theorem-framework.md`, `docs/phase-locking-guinand.md`.
**Labels:** 核验 / 引用 / 推导 / 猜想. **This note contains no proof** — it is a plan with an explicit failure
point, a list of inputs, and a rule for what must be cited rather than re-proved. The project does not prove RH.

## 1. The exact statement to be proved

Fix x > 0 (the case of interest is x = log p, p prime). Let γ_1 ≤ γ_2 ≤ … be the ordinates of the non-trivial
zeros in the upper half-plane, **counted with multiplicity** (**convention (i)**). If instead only zeros on the
critical line are counted (**convention (ii)**, using N_0), the object below changes and the statement becomes
conditional — see §4.3. Fix convention (i) and state everything about it.

**Theorem A (candidate).** For every x > 0 and every X ≥ 2,
  Σ_{0<γ_k≤X} sin(γ_k x) = −(1/(2πx)) · log(X/2π) · cos(Xx) + E(x, X),  with |E(x, X)| ≤ A(x),
where A(x) < ∞ depends on x only. In particular Σ_{0<γ_k≤X} sin(γ_k x) = O_x(log X); for x = log p this is the
project's O_p(log X).

**Corollary (sharpness; elementary).** The bound is attained in order: along X → ∞ with |cos(Xx)| ≥ ½,
|Σ_{0<γ_k≤X} sin(γ_k x)| ≥ c_x · log X with c_x = 1/(4πx) − o(1). Hence O_x(log X) cannot be improved to
o_x(log X) for any x. (Cf. A5-2 §4.)

Status of both: **猜想**. Neither is proved here.

## 2. Inputs available

**Unconditional, citable [引用]:**
- Riemann–von Mangoldt: N(T) = (T/2π) log(T/2π) − T/2π + 7/8 + S(T) + O(1/T), S(T) = π^{−1} arg ζ(½+iT)
  (Titchmarsh, Ch. IX — exact theorem number **未核验** in this pass).
- S(T) = O(log T) unconditionally, with no unconditional improvement known (Titchmarsh §9.11, p. 224).
- Titchmarsh's prime-sum formula S(T) = −(1/π) Σ_{n≤T} Λ(n)/(√n log n) sin(T log n) + O(1) — the mirror of
  Theorem A (location in Titchmarsh **未核验**; formula verified via secondary sources only).
- Guinand / Weil explicit formula for test functions in the standard class (Guinand 1947, Quart. J. Math.
  Oxford 18, 53–64; Guinand 1948, Proc. LMS 50, 107–119), as already used in `guinand-theorem-framework.md`.

**Elementary, provable in one page [推导]:**
- ∫_2^X sin(tx) log(t/2π) dt = −(log(X/2π) cos(Xx) − log(2/2π) cos(2x))/x + O(1/x).
- ∫_2^X sin(tx) cos(t log n) dt = O(1/|x − log n|) off resonance; at log n = x it is O(1) (the sine integrates
  to a cosine of zero mean — the degenerate, "phase-locked" case, which does not blow up).
- Stieltjes integration by parts against dN.

**Numerical (consistency only, never proof) [核验]:**
- Project runs (`docs/phase-locking-guinand.md` §2, §7): 2×10^6 zeros; |Σsin| ≤ 15 for p ≤ 2000;
  max|Σsin| ~ c√p at intermediate truncations; the 1e−7 perturbation experiment. These are consistent with
  A(x) = O_x(1) plus a slow log X drift that is invisible at log X ≈ 14.

## 3. The route (four steps)

**Step 0 — Fix the object.** Declare convention (i) and write Σ_{0<γ_k≤X} sin(γ_k x) = ∫_{[0,X]} sin(tx) dN(t).
Every later claim is about this Stieltjes integral. Without Step 0 the statement is ambiguous and the A5-2
comparison is not meaningful.

**Step 1 — Main term.** Insert dN(t) = (1/2π) log(t/2π) dt + dS(t) + (7/8 jump + O(1/t) tail); evaluate the
smooth part exactly by parts → the term −(1/(2πx)) log(X/2π) cos(Xx) + O(1/x) of Theorem A. Elementary; already
carried out in `guinand-theorem-framework.md` §2.4 and reproducible.

**Step 2 — Fluctuation.** Bound ∫_2^X sin(tx) dS(t) = sin(Xx)S(X) − x∫_2^X cos(tx)S(t) dt.
- Boundary piece: |sin(Xx)S(X)| ≤ |S(X)| = O(log X) [引用, §2].
- Interior piece: substitute Titchmarsh's prime-sum formula for S(t) and integrate termwise. Terms with
  log n ≈ x give O(1) (resonance); the remainder contributes Σ_n Λ(n)/(√n log n)/|x − log n| = O_x(1)
  (dominated by the nearest prime powers to e^x; beyond that the sum converges geometrically in n). Hence
  x∫_2^X cos(tx)S(t) dt = O_x(1).
  ⇒ ∫sin(tx) dS(t) = O(log X), to be absorbed into A(x) jointly with the main-term oscillation.

**Step 3 — Assembly and constants.** Track X-dependence term by term: every X-growing piece except the
explicit boundary cosine is either bounded or the same size as the main term. Then A(x) is an explicit function
of x and of the standard |S|-type bounds. If a clean constant is wanted, replace the sharp cutoff in Step 2 by
a smooth window and pay the window loss (recorded as part of A(x)).

**Step 4 — Sharpness.** From Step 1 alone: along X with |cos(Xx)| ≥ ½, |main term| ≥ c_x log X ⇒ Corollary.
No literature input needed; this step is unconditional.

## 4. Where it could fail (in order of likelihood)

**4.1 The sharp cutoff is not admissible [推导 — the first failure point].** The Guinand/Weil formula requires h
entire of the right exponential type with h and ĥ decaying; h(t) = sin(tx)·1_{[2,X]} has Fourier transform
decaying only like 1/u, so the prime side Σ_n (Λ(n)/√n) ĥ(log n) is **not absolutely convergent**, and the
"prime term is O(1)" claim is a statement about a conditionally convergent sum. Unless this is handled
(correct summation order, or a smooth window with an explicit loss), Step 2 of the sharp-cutoff route does not
close. This is the single technical core of the whole item: everything else is bookkeeping.

**4.2 The exponent barrier.** Even granting Step 2, the boundary piece sin(Xx)S(X) is O(log X) and *not*
o(log X); improving it is exactly a statement about S, and no unconditional improvement of S(T) = O(log T) is
known (Titchmarsh §9.11). So Theorem A can be sharpened only conditionally. Say this up front rather than
discovering it later.

**4.3 The definitional fork.** If the sum is over on-line zeros only (convention (ii)), N is replaced by N_0 and
the difference N − N_0 enters the main term; Step 1 is then no longer unconditional in the same way, and the
statement becomes conditional on information about off-line zeros. Fix convention (i).

**4.4 Multiplicities and trivial zeros.** Multiplicities must be declared (convention (i) counts with
multiplicity); trivial zeros contribute to the Γ-side of the explicit formula and must not be summed into the γ's.

## 5. Overlap with known results — cite, do not duplicate

Per A5-2: the *mechanism* (explicit formula; smooth zero density; resonance at n = e^x) is classical, and the
prime-side mirror — Titchmarsh's formula for S(T) together with S(T) = O(log T) — covers the substance of
Steps 1–2 in the literature's own coordinates. Therefore the strictification should:
- cite, not re-prove, Riemann–von Mangoldt and S(T) = O(log T);
- present Steps 1–2 as the zero-side transcription of the classical argument;
- claim as (possibly) new only: the explicit constant A(x), the zero-side normalisation, and the sharpness
  corollary in this exact form.
If, after 4.1 is resolved, that is all that remains, the honest deliverable is a **short note**, not a paper.

## 6. Boundary
No proof is attempted here; no numerical run was performed for this note. **未核验** marks theorem numberings in
Titchmarsh to be pinned down before submission. "not found" ≠ "does not exist". E32 closes as: *plan written;
first failure point identified (4.1); if 4.1 is solvable the result is a small note, not a discovery.*
