# A13-2 — Transferring Theorem B (the classical Brown converse inequality) to L(s,χ) for the eight moduli

**Status:** reference-level note. No new verification is performed here. Labels: 核验 / 引用 / 推导 / 猜想.
**Source theorem:** `papers/brown-thm2-classical/main.md`, Theorem 1 (the τ = 1 classical case of Brown's Theorem 2, [引用] Brown 2005; [引用] Droll 2012; [引用] Palojärvi arXiv:1807.01506).
**Scope of this note:** which inputs of that argument are *character-independent*, which need the *counting hypothesis for that L-function*, and where a gap remains. We do **not** claim the classical result, let alone its L(s,χ) transfer, is a proof of anything beyond the stated inequality.

---

## 1. What "Theorem B" is, at reference level

The classical result is the **inequality** (not the Li-coefficient conclusion). For ζ, with a, b, c, d the constants of the counting hypothesis

  (H)  N(T) = aT log T + bT + ε(T),  |ε(T)| ≤ c log⁺T + d,  a, c, d > 0,  3a + b > 0,

Theorem 1 of `papers/brown-thm2-classical/main.md` states, for all integers k ≥ 2 and all H > e,

  Σ_{|Im ρ|>H} [ (1+1/γ_ρ²)^{k/2} + (1+1/γ_ρ²)^{−k/2} − 2 ]
   ≤ 2 (r_H^k + r_H^{−k} − 2) [ (a/3)H log H + (4a/9)H + 2c log H + 2d + c/4 ],  r_H = (1+1/H²)^{1/2},

and its decisive feature is an **explicit margin** (2/3)|b|H^{−3} for H > e, whose positivity is driven by the **sign of the linear coefficient** b of the zero-counting function. For ζ, a = 1/(2π) and b = −(1+log 2π)/(2π) < 0, so the margin is positive [推导; 核验, two million zeros, γ ≤ 1.13×10⁶].

**Two honest caveats carried from the source.** (1) This inequality is the *input* to Brown's Theorem 2; the passage *inequality ⟹ λ_k ≥ 0* still invokes Brown's Lemma 5, whose proof contains an unresolved error — Droll fixed one of the two errors, and Palojärvi records that "as a result of the other error Brown's Theorem 2 is left unproved" [引用; `docs/ENGINE-FOUND-brown-thm2-unproved.md`]. So even the classical ζ statement is *conditional* in its Li-coefficient consequence. (2) The range proved (all k ≥ 2) is stronger than the k ≤ 2H²log H statement attributed to Droll's conjecture.

## 2. Inputs that are character-independent

The following steps contain no χ and no q, and transfer verbatim [推导]:

- the identity x^{k/2} + x^{−k/2} − 2 = (x^{k/4} − x^{−k/4})² ≥ 0, and the monotonicity of F(x) = x^{k/2} + x^{−k/2} − 2 on the range x > 1 actually realised by zeros (since |γ| > H > 0);
- the near/far split, and the far bound via S₄(X) = Σ_{|γ|>X} γ^{−4};
- the **Abel identity with the boundary term kept**, S₄(H) = −2N(H)H^{−4} + 8∫_H^∞ N(t)t^{−5}dt;
- the comparison algebra and the margin formula (2/3)|b|H^{−3}.

These are exactly the ingredients flagged in the source paper as where the boundary term must not be dropped (a dropped boundary term gives a spurious factor 4).

## 3. Inputs that need the counting hypothesis for that L-function

Replacing N(T) by N_χ(T) for primitive χ mod q gives the hypothesis (H_χ): N_χ(T) = a_q T log T + b_q T + ε_q(T), |ε_q(T)| ≤ c_q log⁺T + d_q, with 3a_q + b_q > 0 [推导]. The Riemann–von Mangoldt formula for L(s,χ) gives

  N_χ(T) = (T/π) log(qT/(2πe)) + O(log(qT))  ⟹  a_q = 1/π,  b_q = (log(q/2π) − 1)/π  [引用/推导].

Consequences for the eight moduli (all q ≤ 13):

- 3a_q + b_q = (2 + log(q/2π))/π > 0 for every q ≥ 3 ⟹ (H_χ) is internally consistent;
- b_q < 0 ⟺ q < 2πe ≈ 17.079 ⟹ **the sign hypothesis driving the margin holds for all eight moduli**.

| q | b_q ≈ | margin coeff = (2/3)·abs(b_q) |
| 3 | −0.5537 | 0.3691 |
| 4 | −0.4621 | 0.3081 |
| 5 | −0.3911 | 0.2607 |
| 7 | −0.2839 | 0.1893 |
| 8 | −0.2414 | 0.1610 |
| 9 | −0.2040 | 0.1360 |
| 11 | −0.1400 | 0.0934 |
| 13 | −0.0869 | 0.0579 |

Two further modulus-dependent inputs: (i) the archimedean Γ-factor, with parity κ = (1−χ(−1))/2 ∈ {0,1}, and the root number affect the **constant term** (hence c_q, d_q), not a_q, b_q; (ii) the local zero density used by Lemma 3 of the source becomes (1/π)log(qt/2π) instead of (1/2π)log(t/2π), i.e. an additive log q inside the integral — harmless asymptotically, but modulus-dependent [推导].

## 4. Where the gaps remain (do not overclaim)

**G1 — the Brown Lemma 5 step (central, character-independent).** The inequality ⟹ λ_k ≥ 0 implication uses a step whose proof is *broken* [引用; Palojärvi arXiv:1807.01506, Droll 2012]. This gap is inherited by the L(s,χ) version, which would additionally need the L-function form of that step. Palojärvi's τ-version has both directions with explicit intervals, but its statement uses T(n) = neτ, i.e. a window **linear** in n, not the T ≈ √n window wanted for the classical explicit conversion [引用/推导]. Status: **open (gap)**.

**G2 — explicit constants c_q, d_q.** For ζ the constants in (H) are known, but for L(s,χ) the **explicit** constants c_q, d_q have **not been verified for any of the eight moduli** in this repository. The available data are small-range zeros (γ < 300 for q = 4, γ < 100 for q = 11, etc.), which cannot verify an asymptotic T → ∞ statement. Status: 引用 (standard RvM) but **constants unverified** [open].

**G3 — the near-count integral.** In the classical paper, Lemma 3 is used as an integral evaluated numerically; turning it into a closed-form bound is explicitly left open (§7(a) there), and the L(s,χ) local count would need the same treatment. Status: **open (gap)**.

**G4 — complex χ and trivial zeros.** For complex χ (moduli 5, 7, 9, 11, 13), L(s,χ) ≠ L(s,χ̄); the counting is for a single L-function and is unaffected in principle, but no independent check was performed. Trivial zeros of L(s,χ) (even χ: s = −2, −4, …; odd χ: s = −1, −3, …) have Im = 0, so they do not enter Σ_{|Im ρ|>H}; they do affect the constant term [推导].

| q | zeros on line, small range | P_γ positivity (criterion) | counting constants c_q, d_q |
|---|---|---|---|
| 3, 4, 5, 7, 8, 9, 11, 13 | 核验 (yes) | 核验 (yes) | **not verified** |

## 5. Boundary note on the label "Theorem B"

Within the repository the label "Theorem B" has **also** been used for Theorem B of the frontier paper arXiv:2608.13637, which is reported to hold verbatim for L(s,χ) (fixed primitive character) [引用; `docs/ALIGN-A3-COMPLETE-proof-architecture.md` §1, `docs/PENDING-ITEMS-MASTER.md` A13-2]. That is a *different* (rank/trace/inertia) argument and is **not** what this note transfers. This note concerns the classical Brown case ("Paper B", `papers/brown-thm2-classical`). If A13-2 was intended to mean the frontier Theorem B, a separate note is required.

**Summary of the transfer.** The algebraic and Abel-bookkeeping core of Theorem B is character-independent and transfers verbatim; the counting hypothesis must be re-instantiated for each L(s,χ), and for the eight moduli the sign condition b_q < 0 (which makes the margin positive) is satisfied by a direct computation; but the two recorded gaps — Brown's broken Lemma 5 step and the unverified explicit constants c_q, d_q — mean the transfer is a **conditional recipe at reference level**, not an established theorem for any modulus.
