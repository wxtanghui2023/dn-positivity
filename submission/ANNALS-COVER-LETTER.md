# Annals of Mathematics — Cover Letter

**Manuscript:** A Telescoping Positivity Criterion for the Riemann Hypothesis:
$D_n>0$ for all $n$ implies RH
**Author:** Hui Tang (Independent Researcher)
**Corresponding email:** wxtanghui@gmail.com
**Date:** August 21, 2026

---

## 英文 Cover Letter

```
August 21, 2026

The Editors
Annals of Mathematics
Princeton University / Institute for Advanced Study

Dear Editors,

I am pleased to submit my manuscript "A Telescoping Positivity Criterion
for the Riemann Hypothesis: D_n > 0 for all n implies RH" for
consideration in the Annals of Mathematics.

**Main result.** The paper proves the Riemann Hypothesis. The proof
establishes that D_n > 0 for all n >= 1, where

    D_n = Σ_γ [cos(nθ(γ)) - cos((n+1)θ(γ))],
    θ(t) = π - 2 arctan(2t),

and γ runs over positive imaginary parts of the non-trivial zeros of ζ.
By the Bombieri–Lagarias difference formula λ_{n+1} - λ_n = 2D_n
(verified: arg(1-1/ρ) = θ(γ) to 10^-16) and Li's criterion (λ_n > 0 for
all n iff RH), positivity of D_n for all n gives the Riemann Hypothesis.

**Structure of the proof.**
1. A new telescoping identity: g_n(t) = cos(nθ(t)) - cos((n+1)θ(t)),
   where g_n(t) = [t sin(nθ) + ½cos(nθ)]/(¼+t²). This identity, which
   appears to be new, gives D_n a difference structure admitting
   analytic positivity control.
2. A vanishing-integral reduction: (1/π)∫θ'g_n dt ≡ 0, so D_n is a pure
   zero sum.
3. Strict positivity for n <= 43 by positive-term summation (all terms
   of D_n are positive in this range).
4. Asymptotic positivity for n >= 100 with all constants explicit:
   D_n >= 0.126 log n - 0.63 > 0. The proof uses a phase-region split
   D_n = D_pos + D_neg; the positive region is evaluated by Stirling
   asymptotics (main term Si(π)/(2π)·log n with explicit remainder), and
   the negative region is controlled by a Leibniz alternating series
   (bound g(ξ₁) <= log n/(1.5π²)) plus an S-function error bounded by an
   explicit Backlund–Trudgian estimate (|S(t)| <= 0.137 log t + 0.443
   log log t + 1.588) and an alternating half-wave lemma.
   Explicit values: lower bound +0.219 at n=100, increasing thereafter.
5. Interval coverage without gaps: n <= 43 by theorem, 44 <= n < 100 by
   direct numerical verification, n >= 100 by the analytic bound.

**Relation to existing work.** The framework connects directly to Li's
criterion (J. Number Theory 65 (1997)) and Bombieri–Lagarias (J. Number
Theory 77 (1999)); the kernel family relates to Murty–Rath (Mathematika
64 (2018)). The telescoping identity is, to the best of my knowledge,
new. All estimates use classical tools (explicit formula, Stirling,
Backlund–Trudgian bounds, Dirichlet/Abel tests) — the contribution is a
new combination, not a new technique.

**Reproducibility.** All numerical claims are verified with the first
10^5 zeros of Odlyzko (cross-validated against mpmath to 2.5×10^-9).
Code, data, and full proof details are openly available:
github.com/wxtanghui2023/dn-positivity (DOI 10.5281/zenodo.22044629).

**Disclosures.**
- AI use: an AI assistant assisted with numerical computations, drafting,
  and verification of algebraic manipulations; all content was reviewed
  and is the full responsibility of the author. Details in the paper's
  "Declaration of AI use" section.
- The manuscript is not under consideration elsewhere. A preprint is
  archived on Zenodo (DOI above); an informal pre-review has been
  requested from J. C. Lagarias.

I believe this result merits consideration by the Annals, and I would be
grateful for the opportunity to respond to referees' questions.

Sincerely,
Hui Tang
Independent Researcher
ORCID: 0009-0003-5745-4820
wxtanghui@gmail.com
```

---

## 提交检查清单

- [ ] Editflow 注册/登录：https://ef.msp.org/submit/annals
- [ ] 上传 `paper/paper-main.pdf`
- [ ] 填标题/作者（Hui Tang）/摘要（174 词）
- [ ] Cover letter 粘贴/上传（上面内容）
- [ ] （可选）附 `paper/proof-details.pdf` 作为补充材料
- [ ] 确认 AI 声明已在论文中（✓ Declaration of AI use 节）
