# Two conversion laws for criteria equivalent to the Riemann hypothesis, and a criterion for where a breakthrough can occur

**Hui Tang** · research note, draft v1 · 2026-09-12

> **摘要（中文）**：本文比较六个与 RH 等价的判据的**可达参数范围**，观察到**两条转换律**：
> **T² 律**（系数型判据：可达指标 = 已验证高度的平方）与 **log 律**（矩/阶/相位型：有效自由度 ~ log）。
> 由此给出**突破点的可操作判据**：探针的"指标↔高度"对应 h(n) 若**慢于 √n** 增长，则可达范围优于
> 目前的 T²；理想探针的 h(n) 应尽可能接近常数（即**由首个零点而非高度控制**）。
> ⚠️ 两条律均为**跨方向的经验观察**，其机制尚未证明；本文**不主张**任何关于 RH 真值的结论。

## 1. The question

There are many criteria equivalent to RH: the non-negativity of the Li coefficients λ_n; the
hyperbolicity of the Jensen polynomials J^{d,n}; positivity of Weil's quadratic form on suitable test
functions; the vanishing of the distance d_N in the Nyman–Beurling–Báez-Duarte formulation; phase
properties of sums over zeros in the explicit formula. Each is a *conversion*: it turns arithmetic
input into a statement about zeros. The practical question is not which criterion is true — they are
all equivalent to the same statement — but **what range of the criterion's parameter a given amount of
verified arithmetic input can support**. This note records two regularities in that range, across six
criteria, and draws one operational consequence.

## 2. Law I: the T² law (coefficient-type criteria)

Let T denote a height to which RH has been verified, and let the criterion be indexed by an integer
n (or d), the n-th object being a probe of increasing resolution.

- **Li coefficients.** With λ_n = Σ_ρ[1−(1−1/ρ)^n], if all zeros with 0 < γ ≤ T are on the critical
  line, then λ_n ≥ 0 for **2 ≤ n ≤ 2T − O(1)** (a linear range, obtained elementarily; see the
  companion note on the elementary positivity range).
- **Brown's converse inequality.** For the classical case τ = 1, the inequality that supplies the
  input to Brown's theorem holds for **all k ≥ 2** with explicit dependence on a threshold H, and the
  statements found in the literature for the same object run to **k ≤ 2T² log T**.
- **Jensen polynomials.** Hyperbolicity of J^{d,n} holds for **d ≤ ⌊T⌋²** where T is the verified
  height: the thesis of Droll, and the effective version of Griffin–Ono–Rolen–Thorner–Tripp–Wagner, give the implication from
  "RH verified to height T" to "hyperbolic for d ≤ T²", and Platt's verification to 3.06·10¹⁰ then
  yields d ≤ 9.36·10²⁰.

Two of these three read off the **square** of the verified height; the third is linear (and that is a
feature of its elementary method, as shown in the companion note, where it is also shown to be
optimal in T for that method). The coincidence of the square in two independent families is the
content of Law I.

## 3. Law II: the log law (moment, order and phase-type criteria)

- **Weil positivity under finite compression.** Using the first and second moments only, the
  proportion of zeros certified to be on the line reaches ≈ 0.6725, while the method has a **proved
  ceiling of ≈ 0.682**; the reason recorded in that work is that higher moments add nothing
  unconditionally, the evaluation being available only in the Rudnick–Sarnak range.
- **Nyman–Beurling distance.** The proved lower bound and the conjectured asymptotic both carry the
  constant 2+γ−log4π over log N.
- **Burnol's projection.** The effective number of orders k in the obstructing vectors is ~ log(1/λ),
  which is the origin of the √log factor in the bound.
- **Explicit formula.** The resonance responsible for the sharp behaviour of Σ_k sin(γ_k log p)
  occurs at the prime frequencies x = log p.
- **Connes' extremal problem.** Five primes (those below 13) suffice for an approximation of the
  first fifty zeros with error down to 2.6·10⁻⁵⁵.

In each case the *effective number of degrees of freedom* — the number of orders, moments, primes, or
the logarithmic budget — is what controls the outcome.

## 4. The operational consequence

Suppose a criterion is indexed by n and that its n-th probe is sensitive to zeros only up to a height
h(n). Then a verified height T supports exactly the indices with h(n) ≤ T, i.e. n ≤ h^{−1}(T).

- If **h(n) ~ √n** (as in Law I) then the reach is **T²**.
- If **h(n) ~ n^α with α < 1/2** then the reach is **T^{1/α} > T²**.
- The floor is set by the first zero: h(n) ≥ γ₁ always, so the ideal probe has h(n) as close to the
  constant γ₁ as possible, in which case the reach is governed by γ₁ rather than by the height, and
  the method becomes insensitive to further verification.

**Hence a breakthrough point, in this framework, is a probe whose index-to-height correspondence is
slower than the square root**; and the log-type criteria of Law II are attractive precisely because a
logarithmic budget is, for practical purposes, height-independent.

## 5. Honest limitations

(a) The two laws are empirical regularities across the six criteria examined, not theorems; the
mechanism behind the square in Law I has not been established here (a naive computation of the
sensitivity of the n-th coefficient suggests a linear correspondence, which would contradict the
square, so the square must arise elsewhere, plausibly in the comparison of the test function's width
with the tail budget).
(b) The criterion of §4 is a heuristic for where to look, not a construction.
(c) Several items of §2 and §3 are quoted from the literature at reference level; the numerics
underlying the companion note's own results are archived and reproducible, those of other authors are
not re-derived here.

## References

[1] H. Tang, *An elementary explicit positivity range for the Li coefficients*, draft, 2026.
[2] H. Tang, *A complete proof of the classical case of Brown's theorem on zero-free regions and Li
coefficients*, draft, 2026.
[3] A. D. Droll, *Variations of Li's criterion for an extension of the Selberg class*, PhD thesis,
Queen's University, 2012.
[4] M. Griffin, K. Ono, L. Rolen, D. Zagier, *Jensen polynomials for the Riemann zeta function and
other sequences*, PNAS 116 (2019), 11103–11110; effective version: M. Griffin, K. Ono, L. Rolen,
J. Thorner, Z. Tripp, I. Wagner, *Jensen polynomials for the Riemann xi function*, arXiv:1910.01227.
[5] arXiv:2608.13637, *More than two thirds of the zeta zeros are simple and on the critical line*,
2026 (with its appendix on the limits of the method).
[6] J.-F. Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta
function*, Adv. Math. 170 (2002), 56–70.
[7] E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*,
Rend. Lincei 11 (2000), 183–233.
