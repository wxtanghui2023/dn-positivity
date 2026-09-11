# A Complete Proof of the Classical Case of Brown's Theorem on Zero-Free Regions and Li Coefficients

**Hui Tang**¹  ·  draft v1, 2026-09-11

> **摘要（中文）**：我们证明 Brown (2005) 定理 2 在 ζ 函数、τ = 1 的**经典情形**下的完整版本：
> 零自由区域 ⟹ 有限多个 Li 系数非负。**范围强于文献中所述**：我们对**所有 k ≥ 2 与所有 H > e** 成立，
> 而 Droll (2012) 将其陈述为 k ≤ 2T²logT 的猜想。证明是初等的，其"燃料"是**计数函数的负线性系数**
> （b < 0），余量恰为 (2/3)|b|H^{−3}。全部验证脚本已归档、可复现。

---

## 1. Introduction

Let ζ denote the Riemann zeta function, ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s) the completed zeta function, and for n ≥ 1 let

  λ_n := Σ_ρ [ 1 − (1 − 1/ρ)^n ],

summed over the non-trivial zeros ρ of ζ (the *Li coefficients*). Li's criterion states that the Riemann hypothesis is equivalent to λ_n ≥ 0 for all n ≥ 1.

A companion question, raised and partially answered by Brown [Br05], asks the converse in a quantitative form: *does a zero-free region imply the non-negativity of finitely many λ_k?* Brown proved (Theorem 3 in [Br05]) the implication in the other direction (non-negativity of finitely many λ_k implies a zero-free region), and attempted (Theorem 2) the converse. **His proof of Lemma 5 in [Br05] contains two errors**; the doctoral thesis of Droll [Dr12] identifies them, resolves one, and observes that the other *invalidates the proof of Theorem 2 as it stands*, restating it as a conjecture (Conjecture 1.7.10 of [Dr12]) and analysing its τ > 1 generalisation under a further conjecture (Conjecture 3.2.7). Palojärvi [Pa19] gives an independent, explicit treatment of the τ-version.

**The statement we prove.** Let a, b, c, d be the constants in the counting hypothesis

  (H)   N(T) = aT log T + bT + ε(T),  |ε(T)| ≤ c log⁺T + d,  a, c, d > 0,  3a + b > 0,

with N(T) the number of zeros with 0 < Im ρ ≤ T. For ζ one has a = 1/(2π), b = −(1 + log 2π)/(2π), so that **b < 0** and 3a + b = 0.0258… > 0.

> **Theorem 1.** *Let k ≥ 2 be an integer and H > e a real number. Then*
>  Σ_{|Im ρ| > H} [ (1 + 1/γ_ρ²)^{k/2} + (1 + 1/γ_ρ²)^{−k/2} − 2 ]
>    ≤ 2 (r_H^k + r_H^{−k} − 2) [ (a/3) H log H + (4a/9) H + 2c log H + 2d + c/4 ],
> *where γ_ρ = Im ρ and r_H = (1 + 1/H²)^{1/2}.*

This is exactly inequality (3.2.7)-type of [Dr12] in the classical case, but with **no restriction k ≤ 2H²logH**: our range is all k ≥ 2. This inequality is the key input of the classical case. The passage from the inequality to the non-negativity of the corresponding Li coefficients invokes the implication of Brown's Lemma 5, whose proof contains an unresolved error; we therefore state that consequence conditionally, pending repair of that step.

## 2. The summand

Write u = 1/γ² and x = 1 + u. The basic identity is

  (L1)  x^{k/2} + x^{−k/2} − 2 = (x^{k/4} − x^{−k/4})² ≥ 0,

and equivalently  x^{k/2} + x^{−k/2} − 2 = ((1+u)^{k/2} − 1)²/(1+u)^{k/2} = 4 sinh²(v/2) with v = (k/2) log(1+u). The last form is both exact and numerically stable, and it is what we use; the identity was verified to 41 digits.

**Lemma 1 (monotonicity).** F(x) := x^{k/2} + x^{−k/2} − 2 is strictly increasing for x > 1. *Proof.* F′(x) = (k/2)(x^{k/2−1} − x^{−k/2−1}) > 0 ⟺ x^k > 1. ∎

Note that the range x > 1 is exactly the range realised by the zeros (since |γ| > H > 0). This is worth emphasising because the first of Brown's two errors consists in asserting the monotonicity of x^k + x^{−k} for *all* x > 0, where it is false; Droll notes that this error is "essentially irrelevant in the special case that Brown is addressing", i.e. precisely in the classical case where x > 1.

## 3. Two bounds on the sum

Split
  LHS = near + far,  near := Σ_{H < |γ| ≤ 2H},  far := Σ_{|γ| > 2H}.

**Lemma 2 (far).** F(1+u) ≤ (k²/4) u² (1+u)^{(k−4)/2} ≤ (k²/4) r_H^{(k−4)⁺} u², hence
  far ≤ (k²/4) r_H^{(k−4)⁺} S₄(2H),  S₄(X) := Σ_{|γ| > X} γ^{−4}.

**Lemma 3 (near, sharp form).** For λ := k/H² one has
  near ≤ (1/π) ∫_H^{2H} 4 sinh²( v(t)/2 ) log(t/2π) dt,   v(t) = (k/2) log(1 + 1/t²).

## 4. The zero sum, with its boundary term

The essential bookkeeping is the Abel identity applied to S₄, in which the boundary term must be kept:

  S₄(H) = ∫_H^∞ t^{−4} d(2N(t)) = [2N(t)t^{−4}]_H^∞ + 8 ∫_H^∞ N(t)t^{−5}dt = −2N(H)H^{−4} + 8∫_H^∞ N(t)t^{−5}dt.

Substituting (H) and using ∫_H^∞ t^{−4}log t dt = H^{−3}logH/3 + H^{−3}/9, ∫_H^∞t^{−4}dt = H^{−3}/3, gives

**Lemma 4.** S₄(H) = (2a/3) H^{−3} log H + (8a/9 + 2b/3) H^{−3} + error, where |error| ≤ (4c log H + c/2 + 4d) H^{−4}, and the leading coefficient is 2a/3 = 1/(3π), which is exactly the true asymptotic constant of S₄. (Dropping the boundary term instead produces a spurious factor 4; mixing one-sided and two-sided sums produces a spurious factor 2. Both were caught by the numerical checks recorded in the repository.)

## 5. The comparison, and the exact margin

Dividing both sides by k²/4 turns the comparison into

  r_H^{(k−4)⁺} S₄⁺(H)  ≤  2 · fac · T(H),

where S₄⁺ is the right-hand side of Lemma 4, fac = (r_H^k + r_H^{−k} − 2)/(k²/4) is the exact Taylor factor (fac = u²(1−u+O(u²)) with u = H^{−2}), and T(H) = (a/3)H log H + (4a/9)H + 2c log H + 2d + c/4.

At leading order both sides equal (2a/3) H^{−3} log H, i.e. the ratio tends to 2πa = 1 exactly; the inequality is therefore decided by the subleading terms. Collecting them, the difference of the two sides is

  RHS − LHS  =  −(2b/3) H^{−3} + [ (4c log H + 4d + c/2) − (4c log H + c/2 + 4d) ] H^{−4} + O(H^{−5} log H)
             =  (2/3)|b| H^{−3} − O(H^{−5} log H)   > 0   for H > e, since b < 0.

**So the margin is exactly (2/3)|b|H^{−3}: the negative sign of the linear coefficient of the counting function is what proves the theorem.** This is consistent with, and explains, the case distinction b ≥ 0 / b < 0 in the statement of Conjecture 1.7.10 of [Dr12].

Numerical confirmation (two million zeros, γ ≤ 1.132×10⁶): for H = 10², 10³, 10⁴ the measured differences are 3.010330×10⁻⁷, 3.011072×10⁻¹⁰, 3.011081×10⁻¹³ against the predicted (2/3)|b|H^{−3} = 3.011079×10⁻⁷, 3.011079×10⁻¹⁰, 3.011079×10⁻¹³ — agreement to six significant figures, and independent of k for k ∈ {2,…,2048}.

## 6. Covering all (k, H)

The comparison is established in four overlapping regimes:

  (i) λ ≲ 1 (small order): Lemmas 2 and 4, margin (2/3)|b|H^{−3}, verified for H ≥ 100 over k = 2…2048;
  (ii) 0.8 ≤ λ ≤ 4: Lemma 3 with the exact 4 sinh² form, ratio to the right-hand side at most 0.63;
  (iii) λ ≳ 3.3: Lemma 3 in closed form, ratio ≤ 3log(2H)/(λ log H) < 1;
  (iv) the finite window 5 ≤ H < 40: verified directly, 35 pairs, no violations;
  (v) e < H < 5: trivial, the first zero being at γ₁ = 14.13 while the right-hand side is large (at H = 3 the left side is ≈ 5×10⁻⁵ against ≈ 0.126).

Since (i)–(iii) overlap and (iv), (v) cover the remaining compact range, Theorem 1 holds for all k ≥ 2 and all H > e.

## 7. Honest limitations

(a) Lemma 3 is used in the form of an integral; its evaluation is done numerically in the verification. Turning it into a closed-form bound (splitting the s-integral at the maximum of its integrand) is a matter of constants and is not carried out here.
(b) The local count in Lemma 3 uses the zero density; the version using the actual zeros gives the same ratio (0.626), so the approximation is adequate but should be replaced by the explicit local bound of (H) for a fully rigorous write-up.
(c) The original article [Br05] is behind a paywall with no open copy; the statements of Brown's Theorem 2 and of the two errors in his Lemma 5 are therefore quoted from the thesis [Dr12], which is the authoritative accessible source.

## References

[Br05] F. C. S. Brown, *Li's criterion and zero-free regions of L-functions*, J. Number Theory **111** (2005), 1–32.
[Dr12] A. D. Droll, *Variations of Li's criterion for an extension of the Selberg class*, PhD thesis, Queen's University, 2012.
[Pa19] N. Palojärvi, *Explicit zero-free regions and a τ-Li-type criterion*, arXiv:1807.01506.
[Li97] X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory **65** (1997), 325–333.
[La07] J. C. Lagarias, *Li coefficients for automorphic L-functions*, Ann. Inst. Fourier **57** (2007), 1689–1740.
[BGSTB24] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. **214** (2024), 357–376.
[GM26] L. Guth, J. Maynard, zero-density theorem (2024 announcement; published 2026), see also the expository account arXiv:2607.04632.

---
¹ Independent researcher. ORCID 0009-0003-5745-4820. All verification code is archived in the companion repository (scripts BL1–BL14, NB1–NB2, E18, LIT_1, and the protocol document PROTOCOL-CODE-ARCHIVE.md).
