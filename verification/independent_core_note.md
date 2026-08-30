# Independent Core Verification Note

**Status:** Draft for external verification — 2026-08-30
**Scope:** 5 objects, 5 checks. No historical context required.
**Claim:** A criterion equivalent to RH under a stated distributional
framework. **Not** a proof of RH.

---

## Objects

Let $\zeta$ be the Riemann zeta function, $\xi(s)=\tfrac12
s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, and let
$\rho=\tfrac12+\delta_\rho+i\gamma_\rho$ run over nontrivial zeros with
multiplicity $m_\rho$.

**O1. Kernel.** For $x=t-\gamma$,
$$K_\rho^{\mathrm{nat}}(t) = \frac{\delta_\rho^2-(t-\gamma_\rho)^2}
{\bigl(\delta_\rho^2+(t-\gamma_\rho)^2\bigr)^2}.$$

**O2. Test object.** $H_0(t)=-\dfrac{1}{4\pi}\log(1+t^2)
+\dfrac{1}{2\pi(1+t^2)}$, with $H_0''(t)=O(t^{-2})\in L^1$.

**O3. Pairing weight.**
$$w_H(\gamma,\delta)=\langle K_\delta^{\mathrm{nat}}(\cdot-\gamma),H_0\rangle
=\frac{a^2(a+1)+\delta\gamma^2}{2(a^2+\gamma^2)^2},\qquad a=1+\delta.$$

**O4. Pair discrepancy.**
$$P_\gamma(\delta)=2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)
=\frac{\delta^2 M_2(\gamma,\delta^2)}{2U^2D_+D_-},\quad U=1+\gamma^2,$$
$$M_2=8U^2(5\gamma^2-1)+4(5U^2-16U+16)\delta^2+16(U-2)\delta^4+4\delta^6,$$
$$D_\pm=\bigl((1\pm\delta)^2+\gamma^2\bigr)^2.$$

**O5. Functionals.** With $S(t)=\partial_t^2\log|\xi(\tfrac12+it)|$,
$Q=-\langle S,H_0\rangle$ (pairing defined distributionally through
$\langle S,H_0\rangle=\langle\log|\xi|,H_0''\rangle$), and
$Q'_{\mathrm{RH}}=-\sum_{\rho/\sim}2m_\rho w_H(\gamma_\rho,0)$ where
$\rho\sim 1-\bar\rho$ (functional equation pairs; same $\gamma$, opposite
$\delta$).

---

## Checks

**C1. Hadamard second derivative.** From
$\xi(s)=\tfrac12\pi^{-s/2}e^{bs}\prod_\rho(1-s/\rho)e^{s/\rho}$
($b=\log 2\pi-1-\tfrac\gamma2$), all explicit terms
($-\tfrac s2\log\pi$, $bs$, $\log\tfrac12$) are $t$-linear or constant,
hence their $\partial_t^2$ vanishes. The zero part gives
$$S(t)=\sum_\rho m_\rho K_\rho^{\mathrm{nat}}(t),\qquad S_{\mathrm{reg}}=0.$$
*Check:* the $t$-linearity of every explicit term; the factor
$\tfrac12$ arising from $\operatorname{Re}\log(\delta+i(\gamma-t))$; the
multiplicity $m_\rho$.

**C2. Fourier normalization.** Convention fixed as
$\widehat H(u)=\int_{\mathbb R}H(t)e^{-2\pi iut}\,dt$. Standard integrals:
$F[1/(x^2+a^2)](u)=(\pi/a)e^{-2\pi a|u|}$,
$F[(a^2-x^2)/(x^2+a^2)^2](u)=2\pi^2|u|e^{-2\pi a|u|}$,
$\widehat H_0(u)=e^{-2\pi|u|}\bigl[\tfrac{1}{4\pi|u|}+\tfrac12\bigr]$.
*Check:* every $2\pi$, sign, and constant; the product
$\widehat K_\delta\widehat H_0=\tfrac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}$
is finite at $u=0$ (no formal zero-frequency cancellation).

**C3. Distributional pairing of $H_0$.** $H_0\notin L^1$; pairings are
defined by $\langle S,H_0\rangle=\langle\log|\xi|,H_0''\rangle$
(integration by parts; $H_0''\in L^1$), and per-zero pairings through the
product $\widehat K_\delta\widehat H_0\in L^1$. *Check:* boundary terms in
the integration by parts; the interchange
$\sum_\rho|\langle K_\rho,H_0\rangle|<\infty$ via
$|\langle K_\rho,H_0\rangle|\ll|\delta_\rho||H_0''(\gamma_\rho)|$ and
$\sum_\rho|H_0''(\gamma_\rho)|<\infty$ ($N(T)=O(T\log T)$).

**C4. Factorization of $P_\gamma$.** For $|\delta|<\tfrac12$ and
$|\gamma|\ge\gamma_1=14.1347\ldots$ ($U\ge200$): $8U^2(5\gamma^2-1)>0$,
$4(5U^2-16U+16)\delta^2>0$, $16(U-2)\delta^4>0$, $4\delta^6>0$; the
denominator $2U^2D_+D_->0$ is a product of squares. Hence
$$P_\gamma(\delta)\ge0,\qquad P_\gamma(\delta)=0\iff\delta=0.$$
*Check:* the coefficient positivity for all $\gamma\ge\gamma_1$; no
uniform lower bound is claimed (only pointwise/pairwise positivity).

**C5. Spectral assembly.** $Q=-\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho)$
(over all zeros, pairs counted twice with $\delta$ and $-\delta$);
$Q'_{\mathrm{RH}}=-\sum_{\rho/\sim}2m_\rho w_H(\gamma_\rho,0)$. Then
$$Q-Q'_{\mathrm{RH}}=\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho).$$
Absolute convergence: $P_\gamma(\delta)\le C/\gamma^6$ uniformly
($C=20$ suffices), $\sum_\rho m_\rho\gamma_\rho^{-6}<\infty$.
*Check:* counting convention (no factor-2 error), convergence, and the
reverse expansion restoring $-Q'_{\mathrm{RH}}+Q$.

---

## Theorem (candidate)

With the definitions above,
$$Q=Q'_{\mathrm{RH}}\iff \delta_\rho=0\ \forall\rho
\iff \operatorname{Re}\rho=\tfrac12\ \forall\rho.$$

- **RH $\Rightarrow$ equality:** $\delta_\rho=0\Rightarrow P_{\gamma_\rho}(0)=0$.
- **Equality $\Rightarrow$ RH:** $\sum m_\rho P=0$ with $m_\rho>0$,
  $P\ge0$ forces each $P=0$, hence $\delta_\rho=0$ (C4).

---

## Honest boundaries

1. **$Q'_{\mathrm{RH}}$ naturality:** the projection
   $\rho\mapsto\tfrac12+i\gamma_\rho$ is a reference spectrum; whether
   $Q$ is a "natural" functional (vs. constructed to yield positivity)
   is an evaluation question for external experts.
2. **Distributional framework:** the exact admissible class of the
   invoked Weil/Barner explicit formula for $H_0\in C^\infty\cap\mathcal S'$,
   $H_0''\in L^1$ should be checked against the cited sources.
3. **$S_{\mathrm{reg}}=0$:** verified analytically (all explicit terms
   $t$-linear); recommended one-page independent recomputation.
4. **Status:** promising candidate criterion; independent verification
   required. Not a proof of RH.
