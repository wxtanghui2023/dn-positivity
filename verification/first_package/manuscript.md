# A Candidate Criterion Equivalent to the Riemann Hypothesis
## First-Package Verification Material（干净版——不含研究史）

> **To the reader:** This is a self-contained mathematical exposition.
> Please evaluate it **INVALID-first**: try to prove it wrong, rather than
> confirm it. Verdict per check: **VALID / INVALID / UNJUSTIFIED**.
>
> No historical context, prior versions, or author's internal assessments
> are provided here — intentionally. The mathematics must stand alone.

---

## 1. Objects

Let $\zeta$ be the Riemann zeta function,
$\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, and let
$\rho=\tfrac12+\delta_\rho+i\gamma_\rho$ run over nontrivial zeros with
multiplicity $m_\rho$.

**O1. Kernel.** For $x=t-\gamma$,
$$K_\rho^{\mathrm{nat}}(t)=\frac{\delta_\rho^2-(t-\gamma_\rho)^2}
{\bigl(\delta_\rho^2+(t-\gamma_\rho)^2\bigr)^2}.$$

**O2. Test object.** $H_0(t)=-\frac{1}{4\pi}\log(1+t^2)
+\frac{1}{2\pi(1+t^2)}$, with $H_0''(t)=O(t^{-2})\in L^1$.

**O3. Pairing weight.** With Fourier convention
$\widehat H(u)=\int_{\mathbb R}H(t)e^{-2\pi iut}\,dt$,
$$w_H(\gamma,\delta)=\int_{\mathbb R}\widehat K_\delta^{\mathrm{nat}}(u)
\widehat H_0(u)\,e^{-2\pi iu\gamma}\,du
=\frac{a^2(a+1)+\delta\gamma^2}{2(a^2+\gamma^2)^2},\quad a=1+\delta,$$
where $\widehat K_\delta^{\mathrm{nat}}(u)=2\pi^2|u|e^{-2\pi\delta|u|}$,
$\widehat H_0(u)=e^{-2\pi|u|}[\tfrac{1}{4\pi|u|}+\tfrac12]$, and the
product $\widehat K_\delta\widehat H_0=
\tfrac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}\in L^1$.

**O4. Pair discrepancy.**
$$P_\gamma(\delta)=2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)
=\frac{\delta^2M_2(\gamma,\delta^2)}{2U^2D_+D_-},\quad U=1+\gamma^2,$$
$$M_2=8U^2(5\gamma^2-1)+4(5U^2-16U+16)\delta^2+16(U-2)\delta^4+4\delta^6,$$
$$D_\pm=\bigl((1\pm\delta)^2+\gamma^2\bigr)^2.$$

**O5. Functionals.** Termwise definitions (absolute convergence below):
$$Q=-\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho),$$
$$Q'_{\mathrm{RH}}=-\sum_\rho m_\rho w_H(\gamma_\rho,0)\quad
(\text{projection }\delta_\rho\mapsto0,\ \text{keeping }
\gamma_\rho,m_\rho;\ \text{no RH assumption}).$$

---

## 2. Checks

**C1. Hadamard second derivative.** From
$\xi(s)=\tfrac12\pi^{-s/2}e^{bs}\prod_\rho(1-s/\rho)e^{s/\rho}$
($b=\log2\pi-1-\tfrac\gamma2$), every explicit term
($\log\tfrac12$, $-\tfrac s2\log\pi$, $bs$) has $t$-independent real
part for $s=\tfrac12+it$, so $\partial_t^2$ vanishes on them; the zero
part gives $S(t)=\partial_t^2\log|\xi(\tfrac12+it)|
=\sum_\rho m_\rho K_\rho^{\mathrm{nat}}(t)$, i.e. $S_{\mathrm{reg}}=0$.

**C2. Fourier normalization.** As computed in O3: standard integral
$F[1/(x^2+a^2)](u)=(\pi/a)e^{-2\pi a|u|}$, parameter differentiation for
$F[(a^2-x^2)/(x^2+a^2)^2](u)=2\pi^2|u|e^{-2\pi a|u|}$,
$F[\log(1+t^2)](u)=-(1/|u|)e^{-2\pi|u|}$,
$F[1/(1+t^2)](u)=\pi e^{-2\pi|u|}$; the product is in $L^1$ and finite
at $u=0$.

**C3. Distributional pairing.** $H_0\notin L^1$; the naive global pairing
$\langle\log|\xi|,H_0''\rangle$ diverges
($\log|\xi|\sim O(t\log t)$, $H_0''\sim1/(2\pi t^2)$). Pairings are
therefore defined **termwise** through the $L^1$ products in O3.
Absolute convergence: $|w_H(\gamma,\delta)|\sim|\delta|/(2\gamma^2)$,
$\sum_\rho m_\rho\gamma_\rho^{-2}<\infty$ ($N(T)=O(T\log T)$).

**C4. Pair positivity.** For $|\delta|<\tfrac12$, $|\gamma|\ge\gamma_1$:
every coefficient of $M_2$ is positive
($5\gamma^2-1>0$, $5U^2-16U+16>0$, $U-2>0$), $2U^2D_+D_->0$ is a
product of squares. Hence $P_\gamma(\delta)\ge0$ and
$P_\gamma(\delta)=0\iff\delta=0$.

**C5. Spectral assembly.** Grouping $Q$ over functional-equation orbits
$\rho\sim1-\bar\rho$ (same $\gamma$, opposite $\delta$; on-line zeros
$\delta=0$ self-pair):
$$Q-Q'_{\mathrm{RH}}=\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho),$$
with absolute convergence ($P_\gamma\le C/\gamma^6$, $C=20$ suffices,
$\sum_\rho m_\rho\gamma_\rho^{-6}<\infty$). The orbit grouping is legal
by C3 absolute convergence; on-line zeros contribute $0$ to the
difference.

---

## 3. Theorem

$$Q=Q'_{\mathrm{RH}}\iff \delta_\rho=0\ \forall\rho
\iff \operatorname{Re}\rho=\tfrac12\ \forall\rho.$$

- RH $\Rightarrow$ equality: $\delta_\rho=0\Rightarrow P_{\gamma_\rho}(0)=0$.
- Equality $\Rightarrow$ RH: $\sum m_\rho P=0$ with $m_\rho>0$, $P\ge0$
  (C4) forces each $P_{\gamma_\rho}(\delta_\rho)=0$, hence $\delta_\rho=0$.

**Directionality.** $Q$ and $Q'_{\mathrm{RH}}$ (O5) are defined before and
independently of $P_\gamma$; $P_\gamma$ arises in C5 as the *result* of
the orbit difference, not as an input to the definitions.

---

## 4. INVALID-first Protocol

Verdict per item: **VALID / INVALID / UNJUSTIFIED**.

- **Task 1** — Recompute $K^{\mathrm{nat}}$ from the Hadamard second
  derivative; confirm $S_{\mathrm{reg}}=0$.
- **Task 2** — Recompute $H_0$ and $w_H$ under the stated $2\pi$
  convention; confirm the closed form.
- **Task 3** — Verify the factorization and strict positivity of
  $P_\gamma$ (algebra, not numerics).
- **Task 4** — Rebuild O5 from the *definitions* of $Q$ and
  $Q'_{\mathrm{RH}}$ (not from $P_\gamma$ backwards); check orbit
  counting, multiplicity, signs, factor 2, on-line self-pairs, regular
  terms.
- **Task 5** — Hunt for any implicit use of RH, illegal interchange,
  or circularity in the definitions.

## 5. Standing statement

This document presents a **candidate criterion equivalent to the Riemann
Hypothesis** under the stated distributional framework. It is **not** a
claim that RH has been proved; independent verification is required.
