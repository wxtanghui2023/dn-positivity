# Independent Core Verification Note

**Status:** Final frozen statement — 2026-08-30
**Claim:** Internally reconstructed and formally argued criterion
equivalent to RH under the stated distributional framework, pending
independent verification. **Not** a proof of RH. C1–C5 all holding is
**not** equated with "the theorem is established".

**Final status markers:**
- Core chain: **CLOSED internally** (C1–C5 formalized from original definitions)
- Criterion: **INTERNALLY RECONSTRUCTED AND FORMALLY ARGUED**
- External validation: **OPEN** (third-party attack from O1–O5 / C1–C5)
- RH proof claim: **NOT MADE**

**Three permanent boundaries:**
1. "equivalent to RH" = current objective and internal reconstruction
   conclusion;
2. "under the stated distributional framework" = scope limitation;
3. "pending independent external verification" = internal completion is
   not academic confirmation.

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

**C1. Hadamard second derivative (one-page recomputation).**
$\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ with
$\zeta(s)=e^{bs}/(2(s-1)\Gamma(s/2+1))\prod_\rho(1-s/\rho)e^{s/\rho}$,
$b=\log 2\pi-1-\tfrac\gamma2$.  Substituting,
$\Gamma(s/2)/\Gamma(s/2+1)=2/s$, so
$\xi(s)=\tfrac12\pi^{-s/2}e^{bs}\prod_\rho(1-s/\rho)e^{s/\rho}$.
Hence
$\log\xi(s)=\log\tfrac12-\tfrac s2\log\pi+bs+\sum_\rho m_\rho[\log(1-s/\rho)+s/\rho]$.
For $s=\tfrac12+it$, the explicit terms have real parts
$\log\tfrac12$, $-\tfrac14\log\pi$, $\tfrac b2$ (constants) — each
$t$-independent, so $\partial_t^2=0$.  The zero part:
$\operatorname{Re}\log(1-s/\rho)=\tfrac12\log(\delta_\rho^2+(t-\gamma_\rho)^2)-\tfrac12\log(\beta_\rho^2+\gamma_\rho^2)$
(constant second piece), and
$\operatorname{Re}(s/\rho)=(\beta_\rho/2+t\gamma_\rho)/(\beta_\rho^2+\gamma_\rho^2)$
is $t$-linear.  Therefore
$\partial_t^2\log|\xi(\tfrac12+it)|=\sum_\rho m_\rho
\tfrac{\delta_\rho^2-(t-\gamma_\rho)^2}{(\delta_\rho^2+(t-\gamma_\rho)^2)^2}
=S_{\mathrm{reg}}+\sum_\rho m_\rho K_\rho^{\mathrm{nat}}(t)$
with $S_{\mathrm{reg}}=0$.  No Gamma term survives (cancelled in the
substitution); trivial zeros do not appear (their $\Gamma(s/2+1)$ poles
cancel $\zeta$'s trivial zeros in $\xi$, whose Hadamard product runs over
nontrivial zeros only).

**C2. Fourier normalization (complete lemma).** Convention
$\widehat H(u)=\int_{\mathbb R}H(t)e^{-2\pi iut}dt$.  Standard integral:
$F[1/(x^2+a^2)](u)=(\pi/a)e^{-2\pi a|u|}$; by parameter
differentiation,
$F[1/(x^2+a^2)^2](u)=(\pi/2a^3)(1+2\pi a|u|)e^{-2\pi a|u|}$.
Decomposing
$(a^2-x^2)/(x^2+a^2)^2=-1/(x^2+a^2)+2a^2/(x^2+a^2)^2$ gives
$F[K_a^{\mathrm{nat}}](u)=2\pi^2|u|e^{-2\pi a|u|}$.  For $H_0$,
$F[\log(1+t^2)](u)=-(1/|u|)e^{-2\pi|u|}$ (via
$\partial_a\log(a^2+t^2)=2a/(a^2+t^2)$) and
$F[1/(1+t^2)](u)=\pi e^{-2\pi|u|}$, so
$\widehat H_0(u)=e^{-2\pi|u|}[1/(4\pi|u|)+1/2]$.  The product
$\widehat K_\delta\widehat H_0=\tfrac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}\in L^1$
($a=1+\delta$) is finite at $u=0$ (the $|u|$ and $1/|u|$ factors cancel
in the closed form; no formal zero-frequency extension).  Parseval then
gives
$w_H(\gamma,\delta)=\langle K_\delta^{\mathrm{nat}}(\cdot-\gamma),H_0\rangle
=\int\widehat K_\delta\widehat H_0 e^{-2\pi iu\gamma}du$,
and with
$F^{-1}[e^{-2\pi a|u|}](\gamma)=(1/\pi)a/(a^2+\gamma^2)$,
$F^{-1}[|u|e^{-2\pi a|u|}](\gamma)=(a^2-\gamma^2)/(2\pi^2(a^2+\gamma^2)^2)$,
one obtains
$w_H(\gamma,\delta)=[a^2(a+1)+\delta\gamma^2]/(2(a^2+\gamma^2)^2)$.

**C3. Distributional pairing of $H_0$.** $H_0\notin L^1$, and the
naive pairing $\langle S,H_0\rangle=\langle\log|\xi|,H_0''\rangle$ is
**not** a convergent ordinary integral: $\log|\xi(\tfrac12+it)|\sim
O(t\log t)$ while $H_0''(t)\sim 1/(2\pi t^2)$, so the product is of
order $\log t/t$, not integrable.  The functional $Q$ is therefore
defined **termwise**:
$$Q=-\sum_\rho m_\rho\langle K_\rho^{\mathrm{nat}},H_0\rangle,$$
where each pairing is defined through the Parseval product
$\widehat K_\delta\widehat H_0=\tfrac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}\in L^1$.
The series is absolutely convergent since
$|\langle K_\rho,H_0\rangle|=|w_H(\gamma_\rho,\delta_\rho)|\sim
|\delta_\rho|/(2\gamma_\rho^2)$ and
$\sum_\rho|\delta_\rho|/\gamma_\rho^2\le\tfrac12\sum_\rho\gamma_\rho^{-2}<\infty$
($N(T)=O(T\log T)$).  *Check:* the termwise definition, the absolute
convergence, and the interchange
$\sum_\rho|\langle K_\rho,H_0\rangle|<\infty$; note that no global
pairing $\langle S,H_0\rangle$ is used.

**C4. Factorization of $P_\gamma$ (formal lemma).**
With $w_H$ as in O3,
$P_\gamma(\delta)=2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)$.
Substituting the closed form and putting over the common denominator
gives
$P_\gamma(\delta)=\delta^2M_2(\gamma,\delta^2)/[2U^2D_+D_-]$,
$U=1+\gamma^2$, $D_\pm=((1\pm\delta)^2+\gamma^2)^2$, where
$M_2=8U^2(5\gamma^2-1)+4(5U^2-16U+16)\delta^2+16(U-2)\delta^4+4\delta^6$.
For $|\delta|<\tfrac12$ and $|\gamma|\ge\gamma_1=14.1347\ldots$
($U\ge200$): $5\gamma^2-1>0$, $5U^2-16U+16>0$, $U-2>0$, hence every
coefficient of $M_2$ is positive; $2U^2D_+D_->0$ is a product of
squares.  Therefore
$P_\gamma(\delta)\ge0$ and $P_\gamma(\delta)=0\iff\delta=0$.
No uniform lower bound is claimed (only pointwise/pairwise positivity).

**C5. Spectral assembly.** $Q=-\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho)$
(over all zeros, pairs counted twice with $\delta$ and $-\delta$);
$Q'_{\mathrm{RH}}=-\sum_{\rho/\sim}2m_\rho w_H(\gamma_\rho,0)$. Then
$$Q-Q'_{\mathrm{RH}}=\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho).$$
Absolute convergence: $P_\gamma(\delta)\le C/\gamma^6$ uniformly
($C=20$ suffices), $\sum_\rho m_\rho\gamma_\rho^{-6}<\infty$.
*Check:* counting convention (no factor-2 error), convergence, and the
reverse expansion restoring $-Q'_{\mathrm{RH}}+Q$.

---

## Theorem (candidate) — with formal proof

**Definitions (termwise).** $Q=-\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho)$
(absolute convergence, C3);
$Q'_{\mathrm{RH}}=-\sum_{\rho/\sim}2m_\rho w_H(\gamma_\rho,0)$ where
$\rho\sim 1-\bar\rho$ (functional-equation pairs: same $\gamma$,
opposite $\delta$). $Q'_{\mathrm{RH}}$ uses the actual ordinates
$\gamma_\rho$ and $w_H(\gamma_\rho,0)=(1+\gamma_\rho^2)^{-2}$; no RH
assumption enters — it is a reference spectrum.

**Assembly (O5).** Grouping $Q$ over orbits,
$$Q=-\sum_{\rho/\sim}m_\rho\bigl[w_H(\gamma_\rho,\delta_\rho)+w_H(\gamma_\rho,-\delta_\rho)\bigr],$$
hence, with $P_\gamma(\delta)=2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)$,
$$Q-Q'_{\mathrm{RH}}=\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho).$$
This is definitional (termwise $Q$ + orbit grouping + definition of
$Q'_{\mathrm{RH}}$); it does not use the closed form of $P_\gamma$.

**Equivalence.**
- RH $\Rightarrow$ equality: $\delta_\rho=0\Rightarrow P_{\gamma_\rho}(0)=0$.
- Equality $\Rightarrow$ RH: $\sum m_\rho P=0$ with $m_\rho>0$, $P\ge0$
(C4) forces each $P_{\gamma_\rho}(\delta_\rho)=0$, hence $\delta_\rho=0$.

So $Q=Q'_{\mathrm{RH}}\iff\operatorname{Re}\rho=\tfrac12$ for all $\rho$.

## Verification Protocol (for third-party readers)

Complete the five tasks below **without reading any historical versions**
of this project and **without assuming the conclusion**. For each task
output exactly one verdict:

> **VALID** / **INVALID** / **UNJUSTIFIED**

### Task 1 — Recompute $K^{\mathrm{nat}}$
From $\xi(s)=\tfrac12\pi^{-s/2}e^{bs}\prod_\rho(1-s/\rho)e^{s/\rho}$,
compute $S(t)=\partial_t^2\log|\xi(\tfrac12+it)|$ directly and identify
the single-zero contribution. Confirm $S=\sum_\rho m_\rho K_\rho^{\mathrm{nat}}
+S_{\mathrm{reg}}$ with $S_{\mathrm{reg}}=0$ (every explicit term
$t$-linear).

### Task 2 — Recompute $H_0$ and $w_H$
With Fourier convention $\widehat H(u)=\int H(t)e^{-2\pi iut}dt$,
compute $\widehat H_0$ from the closed form of $H_0$, then compute
$w_H(\gamma,\delta)=\langle K_\delta^{\mathrm{nat}}(\cdot-\gamma),H_0\rangle$
via Parseval. Confirm $w_H=(a^2(a+1)+\delta\gamma^2)/(2(a^2+\gamma^2)^2)$,
$a=1+\delta$ (actual $\delta$, not $|\delta|$).

### Task 3 — Verify the factorization of $P_\gamma$
Expand $P_\gamma(\delta)=2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)$
algebraically; confirm
$P_\gamma=\delta^2M_2/(2U^2D_+D_-)$ with $M_2$ as in O4, and confirm
every coefficient of $M_2$ is positive for $|\gamma|\ge\gamma_1$,
$|\delta|<\tfrac12$. Confirm $P_\gamma(\delta)=0\iff\delta=0$.

### Task 4 — Rebuild O5 from the definitions of $Q$ and $Q'_{\mathrm{RH}}$
Starting from $Q=-\langle S,H_0\rangle$ and $S=\sum m_\rho K^{\mathrm{nat}}_\rho$
(do **not** start from $P_\gamma$), derive
$Q=-\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho)$ and
$Q'_{\mathrm{RH}}=-\sum_{\rho/\sim}2m_\rho w_H(\gamma_\rho,0)$,
fix the orbit convention, and confirm
$Q-Q'_{\mathrm{RH}}=\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho)$.
Pay attention to: orbit classes, multiplicities, functional-equation
pairing, signs, the factor $2$, and regular terms.

### Task 5 — Hunt for hidden assumptions
Actively look for: any implicit use of RH, illegal interchange of sum
and pairing, circular reasoning (e.g. defining $Q'_{\mathrm{RH}}$ through
$P_\gamma$), or any step where $|\delta|$ silently replaces $\delta$.

---

## Function-space details for the distributional pairing (C3)

- $S=\partial_t^2\log|\xi(\tfrac12+it)|\in\mathcal S'(\mathbb R)$ as a
tempered distribution; $\log|\xi|\in\mathcal S'$.
- $H_0\in C^\infty\cap\mathcal S'$ (smooth, logarithmic growth);
$H_0\notin L^1$; $H_0''(t)=O(t^{-2})\in L^1$.
- Pairing: **termwise** — $Q=-\sum_\rho m_\rho\langle K_\rho^{\mathrm{nat}},H_0\rangle$
with each pairing via the Parseval product
$\widehat K_\delta\widehat H_0\in L^1$. The naive global pairing
$\langle\log|\xi|,H_0''\rangle$ diverges ($\log|\xi|\sim O(t\log t)$,
$H_0''\sim 1/t^2$), so no global pairing is used.
- Fourier side: $\widehat H_0(u)=e^{-2\pi|u|}[\tfrac{1}{4\pi|u|}+\tfrac12]$
is in $\mathcal S'$ (of $1/|u|$ type at $0$); per-zero pairings are
defined through the product
$\widehat K_\delta\widehat H_0=\tfrac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}\in L^1$,
so no separate extension of $\widehat H_0$ at $u=0$ is needed.
- Interchange: $\sum_\rho|\langle K_\rho,H_0\rangle|\le
\tfrac12\sum_\rho|H_0''(\gamma_\rho)|<\infty$ via
$|\langle K_\rho,H_0\rangle|\ll|\delta_\rho||H_0''(\gamma_\rho)|$,
$|\delta_\rho|<\tfrac12$, and $N(T)=O(T\log T)$.

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
