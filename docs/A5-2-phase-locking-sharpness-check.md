# A5-2 — Is the phase-locking sharpness statement already in the literature?

**Date:** 2026-09-12 · **Registered question:** `docs/EXPLORATION-POINTS-REGISTER.md` E29 / A5-2,
"查证相位锁定的锐利性是否为文献已有".
**Object to check (project):** for fixed prime p, Σ_{0<γ_k≤X} sin(γ_k log p) = O_p(log X) unconditionally,
with a claimed RH-conditional O_p(1); see `docs/guinand-theorem-framework.md` §1–§4.
**Labels:** 核验 · 引用 · 推导 · 猜想.

## 1. What the sum actually is 推导

Let N(t) be the zero-counting function (upper half-plane, multiplicity) and dN its Stieltjes measure. Then
Σ_{0<γ_k≤X} sin(γ_k log p) = ∫_{[0,X]} sin(t log p) dN(t). Split by Riemann–von Mangoldt:
dN(t) = (1/2π) log(t/2π) dt + dS(t) + (7/8 jump and O(1/t) tail), where S(t) = π^{−1} arg ζ(½ + it).
- **Smooth part:** (1/2π)∫_2^X sin(tx) log(t/2π) dt = −(1/(2πx)) log(X/2π) cos(Xx) + O(1/x), x = log p.
- **Fluctuation:** ∫_2^X sin(tx) dS(t) = sin(Xx)·S(X) − x ∫_2^X cos(tx) S(t) dt.
The sum therefore has **two O(log X)-sized pieces**: the oscillating smooth boundary term and sin(Xx)S(X).
This is the same structure as the classical statement S(T) = O(log T), and it drives the verdict in §3.

## 2. The closest known results (the S(T) literature)

*(a) Unconditional upper bound; no improvement known.* Titchmarsh, *The Theory of the Riemann Zeta-function*,
Ch. IX, §9.11 (p. 224 of the scanned 2nd edition): "At the present time no improvement on the result
S(T) = O(log T) is known." In the same section, Theorem 9.11 proves that the gaps between successive ordinates
tend to 0 — Titchmarsh derives this directly, precisely because S(T) = o(log T) is not available. 引用.

*(b) Unconditional Ω.* Selberg (1946), quoted in the Wikipedia article "Riemann hypothesis":
"S(T) ≠ o((log T)^{1/3}/(log log T)^{7/3})". 引用 (secondary; primary not retrieved in this pass).

*(c) Montgomery (1977), conditional.* Under RH, S(T) = Ω_±((log T)^{1/2}(log log T)^{−1/2}); Montgomery's
heuristic suggests this is optimal — retrieved sentence: "a heuristic argument led Montgomery to suggest that
the above conditional Ω_± bounds for S(t) are optimal; this possible conjecture is also mentioned by
Heath-Brown". 引用 (Aistleitner–Mahatab–Munsch, Math. Ann. 372 (2018) 999–1015, arXiv:1704.06158v3, intro).

*(d) Recent conditional strengthening.* Aistleitner–Mahatab–Munsch, arXiv:1704.06158v3 (Math. Ann. 372 (2018)
999–1015): on RH, max_{T^β ≤ t ≤ T}|S(t)| ≥ c·√(log T·log log log T / log log T) for every 0 ≤ β < 1; the
same introduction attributes the upper-bound side to work of Tsang. 引用.
*(e) Mirror statement (prime side).* The classical formula expressing the argument function as a **prime** sum,
S(T) = −(1/π) Σ_{n ≤ T} Λ(n)/(√n log n) sin(T log n) + O(1), is the exact dual of the project's sum: same
resonance mechanism, primes where the project has zeros. 引用 [standard formula; the exact numbering in
Titchmarsh was not verified in this pass — recorded as 未核验].
*(f) Sign changes.* Selberg's unconditional sign-change theorem for S(t), and later interval statements
(e.g. any (T, T+H] with H ≥ T^{27/82+ε} contains at least H(log T)^{1/3} e^{−c√(log log T)} sign changes):
these bound how often the phase wanders, not how large |S| gets. 引用 (Wikipedia, secondary).

## 3. Direct comparison with the project's O_p(log X)

| Question | Answer | Evidence |
|---|---|---|
| Is the project's **exact** statement in the literature? | **Not found** in this form (zero-side sum, fixed frequency log p, sharp cutoff in γ). | targeted searches, §2 |
| Is the **mechanism** known? | **Yes.** Standard explicit-formula resonance: main term from the smooth zero density; prime term finite because ∫sin(tx)cos(t log n)dt = O(1/\|x − log n\|), and at n = e^x the resonant phase degenerates (→ O(1), no blow-up). | 推导 + §2(e) |
| Is O_p(log X) the right **order**? | **Yes, and it is attained**: the smooth boundary term alone is Ω(log X/log p) along X with \|cos(X log p)\| bounded below. The exponent cannot be improved to o(log X) by any argument that keeps the main term. | 推导, §4 |
| Is the claimed **RH ⇒ O_p(1)** in `guinand-theorem-framework.md` §3 correct? | **Not as stated.** The main term comes from the zero density and is RH-independent; RH removes the off-line-zero contributions but does not remove an oscillating term of size log X/log p. The §3 numerical "final value O(1)" is a finite-range effect: log X ≈ 14 at X = 1.13×10^6. | 推导, §4 |

**Verdict on the registered question (a)/(b)/(c)/(d): ≈ (d) not comparable as a hard theorem, with the
substance being (a) known.**
- as a *named theorem about this exact sum*: not found → (d);
- as a statement about the *mechanism and the order*: classical, and in the literature under a different
  encoding → (a): the zero-side sum here is the mirror of S(T) = O(log T) plus the prime-sum formula §2(e);
- the *sharpness of the exponent* is **not** a new open problem: it is the same circle of ideas as
  "S(T) = o(log T)?", open unconditionally (Titchmarsh §9.11), with the Ω-results §2(b)(c)(d) quantifying
  what is known.
Hence the project should **not** claim the statement, nor its sharpness, as new. What could be new is only an
explicit constant and a clean zero-side write-up.

## 4. Why the exponent log X is attained 推导

(1/2π)∫_2^X sin(tx) log(t/2π) dt = −(log(X/2π) cos(Xx))/(2πx) + O(1/x). For x fixed, along any sequence
X_j → ∞ with |cos(X_j log p)| ≥ ½ (a set of positive density, and X here ranges over a continuum),
the first term has size ≥ (1/(4π log p)) log X_j. Combining with §3's decomposition,
|Σ_{γ≤X} sin(γ log p)| = Ω(log X/log p): the project's upper bound is **sharp in order**, and the registered
"sharpness unclear" can be closed as *sharp in order, by an elementary computation*. The deeper question —
whether the fluctuation can be pushed from O(log X) down to o(log X) — is the classical open problem of §2(a).

## 5. What is genuinely not found

- Any paper isolating Σ_{0<γ≤X} sin(γ log p) for fixed p as a named object with its own theorem: **not found**.
- Any published statement of the project's numerical observations (the "log 47" 1e−7 sensitivity; max|Σsin| ≤ 15
  over 2×10^6 zeros; max|Σsin| ~ c√p): **not found**.
- Any published discussion of *why* exact resonance at p gives O(1) while a 1e−7 perturbation gives thousands:
  the mathematics is the standard resonance of §2(e)/§4; the explicit **numerical demonstration** appears to be
  the project's own.

## 6. Boundary and honesty
- Primary read: Titchmarsh Ch. IX §9.9–9.11 (scan), arXiv:1704.06158v3 (metadata, abstract, intro fragments).
  Secondary: Wikipedia ("Riemann hypothesis", "Riemann zeta function") for Selberg's Ω and the sign-change
  statements; MathOverflow 82635 and 163234 for the psi(x)/zero-sum explicit formula. Tsang's monograph:
  **not retrieved**.
- "not found" means *not found by this search*, not "does not exist".
- **Closure of A5-2:** substance = known/classical; sharpness = elementary and sharp; nothing here is
  publishable as new. The only defensible new item would be a fully explicit constant, which belongs to A5-3.
