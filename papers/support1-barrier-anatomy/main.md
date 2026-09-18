# The support‑1 barrier: a technical anatomy

**Author**: Hui Tang · **Draft**: v1, 2026‑09‑18 · **Nature**: review note (process material; not a research result)

**Status discipline.** Nothing in this note is claimed as new mathematics. It is an *anatomy*: a verbatim‑anchored account of one specific technical obstruction — the restriction to Fourier support ≤ 1 in the pair‑correlation method for zeros of the Riemann zeta function — together with a quantified statement of what would be needed to pass it, and one elementary observation about *why* a large family of attempted repairs cannot work. All literature statements are quoted with their source; our own additions are marked **[our]**.

---

## 0. Summary

Let $L=\log\frac{T}{2\pi}$, and let $N$ denote the number of zeros $\rho=\beta+i\gamma$ with $T<\gamma\le 2T$ counted with multiplicity, $N_0^s$ the number of those that are simple and on the critical line $\Re s=\tfrac12$. The state of the art at the time of writing gives
$$N_0^s\ \ge\ \Bigl(\tfrac23-o(1)\Bigr)N,\qquad N_d\ \ge\ \Bigl(\tfrac56-o(1)\Bigr)N,$$
and, with a different window, $0.67250\ldots$. All of these come from one machine (indefinite form $\to$ inertia $\to$ rank–trace $\to$ counting); its output constant is $2-R(\psi)$ where $R(\psi)=\lim\|\widetilde G\|^2_{\rm HS}/N$ is set by the prime‑side **second** moment. Within the class of "bandwidth‑one certificates" the method has a ceiling of about $0.6820$.

The obstruction to going further is located, in three independent formulations, at the same place:

1. **Montgomery's original form.** His asymptotic for $F(\alpha)$ is available for $0\le\alpha<1$; for $\alpha\ge1$ his theorem "gives little information" — and consequently attention is restricted to kernels whose Fourier transform vanishes outside $[-1+\delta,1-\delta]$.
2. **Rudnick–Sarnak's form.** Their vanishing lemma shows that a test function supported in $\sum_j|\xi_j|<\frac{2}{m}$ forces every non‑negligible term to satisfy the **product bound** $n_1n_2\cdots n_{r+s}\ll T^{2-\delta}$. For $k$ factors each of size $\asymp X$ this reads $X^k\le T^{2-\delta}$, i.e. $X\le T^{(2-\delta)/k}$.
3. **Unconditional Montgomery form.** The prime‑side second moment is evaluated unconditionally only in the range $0\le x\le T$.

These three thresholds are the same threshold. Beyond it, the evaluation of the off‑diagonal requires information about prime pairs (Hardy–Littlewood) — equivalently, pair correlation beyond Fourier support 1.

Quantitatively: an unconditional extension of the second‑moment range from $X\le T^{1-\varepsilon/2}$ to $X\le T^{1+\eta}$ with $\eta\ge0.04$ suffices to certify $0.70>0.682$. (Ladder: support $1.04/1.26/1.70$ would give $0.70/0.80/0.90$.)

Finally, an elementary observation **[our]**: because $\Lambda=\mu*\log$ is an identity, the short‑distance part of the off‑diagonal is insensitive to rearrangement. Hence the whole family of "rearrangement / majorant / sharper‑estimate" repairs cannot move this obstruction, which is a property of the *value*, not of the *bound*.

---

## 1. The machine, and where the constant comes from

For a window $\psi$ (e.g. the indicator $\psi_0$ or the Montgomery–Taylor window $\psi_{\rm MT}$), set
$$L=\log\tfrac{T}{2\pi},\quad X=e^{L},\qquad \phi(u)=\chi\bigl(\tfrac L2+u\bigr)\chi\bigl(\tfrac L2-u\bigr)\psi(u/L)^{1/2},$$
so that $\operatorname{supp}\phi=[-\tfrac L2,\tfrac L2]$, and put
$$\alpha_k=T+\tfrac{2\pi k}{L}\ (0\le k<d:=\lfloor LT/2\pi\rfloor),\qquad d=N(T,2T)+O(L).$$
For each zero $\rho$ define the Gabor vector $v_\rho=(\widehat\phi(\gamma_\rho-\alpha_k))_{0\le k<d}\in\mathbb C^d$, and
$$\widetilde G=\frac1{aL^2}\sum_{\Re\gamma_\rho\in I'}m_\rho\,v_\rho v_\rho^{\mathsf T},\qquad P=\frac1{aL^2}\sum_{\rho\ \rm on}m_\rho\,v_\rho v_\rho^{\mathsf T},\qquad Q=\widetilde G-P,\qquad a=\frac{\|\phi\|_2^2}{L}.$$
Three inputs:

* **(Z) zero side.** The functional equation pairs off‑line zeros as $\{\rho,1-\bar\rho\}$, so that each pair contributes a $2\times2$ block of signature $(1,1)$ to $Q$, while each on‑line zero contributes a non‑negative rank‑one term to $P$. (Note: the functional equation is used here as a *counting device*, not as a symmetry principle.)
* **(P) prime side.** $\|\widetilde G\|^2_{\rm HS}=(R(\psi)+o(1))N$, where $R$ is computed from Montgomery's **unconditional** prime‑side second moment ([Mon73], [Ary22], [BGSTB24]); with $R(\psi_0)=\tfrac43$ and $R(\psi_{\rm MT})=c_{\rm MT}^{-1}\approx1.3275$.
* **(L) rank–trace.** $P\succeq0$, $\operatorname{rank}P\le r$, $n_+(Q)\le b$ imply, for every $c>0$, $\|P+Q\|_F^2\ \ge\ c\operatorname{tr}P-\tfrac{c^2}{4}r+2c\operatorname{tr}Q-c^2b$.

The single chain is then
$$N_0^s+o(N)\ \ge\ \operatorname{rank}P_1\ \ge\ 4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\rm HS}^2\ =\ \bigl(2-R(\psi)-o(1)\bigr)N.$$
Thus the entire output is the number $2-R(\psi)$; the case $\psi=\psi_0$ gives $2/3$, and $\psi_{\rm MT}$ gives $0.67250$.

### 1.1 The end‑point degeneracy (why the target is not $R\le1$)

Reaching $100\%$ means $n_-(Q_T)=0$ for the whole family, i.e. positivity at the limit, i.e. the Weil form is non‑negative — which is equivalent to RH. So the inertia route is a replacement for positivity *in the partial‑proportion regime only*; at the end point it returns to positivity. Hence the meaningful target is not $R\le1$ but a **strict, nontrivial decrease** of $R$ (or, equivalently, any extension of the range of the second moment). This is the target used below.

---

## 2. Montgomery's own form of the barrier

Define
$$F(\alpha)=F(\alpha,T)=\Bigl(\tfrac{T}{2\pi}\log T\Bigr)^{-1}\sum_{0<\gamma,\gamma'\le T}T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma'),\qquad w(u)=\frac4{4+u^2}.$$

**Theorem (Montgomery 1973, conditional on RH).** *For fixed $0\le\alpha<1$,*
$$F(\alpha)=(1+o(1))T^{-2\alpha}\log T+\alpha+o(1),$$
*uniformly for $0\le\alpha\le1-\varepsilon$; moreover $F$ is real, even, and $F(\alpha)\ge-\varepsilon$.*

The barrier appears in the author's own words (as reproduced in exposition of his argument):

> "Since this theorem gives little information for the case $\alpha\ge1$, attention here is restricted to kernels $\hat r$ which vanish outside $[-1+\delta,\,1-\delta]$."

So the support‑1 restriction is not an artefact of later work: it is the published boundary of the 1973 method. (Note also that Montgomery's *second‑moment* evaluation, unlike the asymptotic above, is unconditional; see §4.)

---

## 3. Rudnick–Sarnak: the vanishing lemma and the product bound

For an L‑function of degree $m$, Rudnick–Sarnak analyse the $n$‑level correlation via a test function $\Phi$ and the resulting sums $A_{r,s}(n,T)$. Their **vanishing lemma** reads, verbatim:

> **Lemma 3.2.** *Let $\Phi$ as in (3.6) be supported in $|\xi_1|+\cdots+|\xi_n|\le\frac{2-\delta}{m}$. Then $A_{r,s}(n,T)=0$ unless $|n_j|\ll T$ and $n_1n_2\cdots n_{r+s}\ll T^{2-\delta}$.*

The proof is an algebraic consequence of the support condition: non‑vanishing forces some $\eta\in\operatorname{Supp}\Phi$ with $\sum_j\eta_j=0$ and $|T(\eta_jL+\log n_j)|\ll1$, whence $n_j\ll T^{m|\eta_j|}$ and, multiplying, $n_1\cdots n_{r+s}\ll T^{m\sum_j|\eta_j|}\le T^{2-\delta}$.

Two consequences.

* **Support ⟺ product bound.** The support condition on $\Phi$ and the product bound on the prime powers are the *same* condition. For $k$ prime powers each of size $\asymp X$, the regime covered is $X^k\le T^{2-\delta}$, i.e. $X\le T^{(2-\delta)/k}$. For $k=2$ this is the classical range $X\le T^{1-\delta/2}$; for $k=3$ it stops at $X\le T^{2/3-\varepsilon}$, leaving a gap of $T^{1/3}$ to reach $X\asymp T$.
* **Degree‑dependence of the tool.** In the same paper the estimate that controls the diagonal after the product bound is (for general degree $m$) proved by Cauchy–Schwarz together with the absolute convergence of Rankin–Selberg L‑functions for $\Re s>1$. For $\zeta$ itself ($m=1$) the corresponding analytic input is instead the unconditional second‑moment evaluation of §4, whose proof uses a Montgomery–Vaughan‑type inequality (see §5).

---

## 4. The unconditional range for $\zeta$: $0\le x\le T$

For $\zeta$ (degree $1$) the relevant unconditional statement is Montgomery's evaluation of the prime‑side second moment, in the form quoted (verbatim) in [BGSTB24, §2]:

> "$R(x,T)$ does not depend on RH, and Montgomery [Mon73] proved unconditionally that
> $$R(x,T)=(1+o(1))\,T x^{-2}\log^2T+T(\log x+O(1))+O(x\log x).$$
> From [GM87] this was improved, so that for $0\le x\le T$,
> $$R(x,T)=x^{-2}T\log T\bigl(\log T+O(1)\bigr)+T\bigl(\log x+O(\sqrt{\log T})\bigr).$$"

Thus the unconditional range is exactly $0\le x\le T$: the same threshold as support 1. Everything beyond requires prime‑pair information.

---

## 5. The Hilbert‑inequality step, and its constant genealogy

The off‑diagonal in the second‑moment evaluation is a bilinear form
$$\sum_{n\ne m}\frac{x_nz_m}{\lambda_n-\lambda_m},\qquad \lambda_n=\log n,$$
and the tool is the **Montgomery–Vaughan weighted generalization of Hilbert's inequality** [MV74, Thm 2]: for $\delta$‑separated $\lambda$'s one has $|\sum_{r\ne s}u_r\bar u_s/(\lambda_r-\lambda_s)|\le C\sum_r|u_r|^2/\delta_r$ (and a companion form with the kernel $\csc\pi(x_r-x_s)$ bounded by $\delta^{-1}\sum|u_r|^2$). The history of the constant $C$ deserves to be recorded carefully:

| Step | Content |
|:--|:--|
| **Schur 1911** | For the classical Hilbert inequality $|\sum_{r\ne s}u_r\bar u_s/(r-s)|\le\pi\sum|u_r|^2$, the constant $\pi$ is **sharp**. |
| **Montgomery–Vaughan 1974** | Weighted generalization; $C\le\tfrac32\pi$; the optimal constant is **conjectured** to be $\pi$. |
| **Preissmann 1984** | Improved to $C=\tfrac43\pi$; can be further optimized by interpolation. |
| **Yangjit 2022/23** | For the *parametric‑family method*: a lower bound of $3.19497$ at $\alpha=\tfrac12$ — "the method in its current form cannot achieve any value below $3.19497$, so cannot achieve the conjectured constant $\pi$"; equivalently, "this method … is **incapable of proving** $c_1=\pi$". The same work proves a *generalized* Hilbert inequality **with** constant $\pi$. |
| **Rodgers 2026** | First **strict** proof that the optimal constant is **strictly greater than** $\pi$, "answering in the negative a question asked by Montgomery and Vaughan", via an explicit limiting counterexample. |

**Writing discipline.** Yangjit's $3.19497$ is a **method‑family obstruction**, not a proof that the optimal constant exceeds $\pi$; the latter is due to Rodgers. This distinction must be kept, and the ladder Schur → MV → Preissmann → Yangjit → Rodgers should be presented as a whole rather than as an isolated citation of the newest paper.

**Consequence for the barrier.** Comparing MV's $\tfrac32\pi\approx4.71239$ with the known lower bound $3.19497$ bounds the available constant‑level slack by a factor $\le1.475$; comparing with the best proved upper bound (about $1.28\pi\approx4.0212$, according to a secondary report) bounds it below by $\ge1.172$. Either way the *available* improvement is a **constant**, whereas the obstruction beyond $X=T$ requires a **power**: the diagonal‑dominance condition is $X\ll TL$, so reaching $X=T^{1+\eta}$ requires an improvement of order $T^{\eta}/\log^3T$. No constant‑level refinement of the Hilbert inequality can supply that.

---

## 6. The quantified threshold

Combining the above: to pass beyond the bandwidth‑one ceiling $0.6820$ it suffices to evaluate (or bound) the prime‑side second moment unconditionally for $X\le T^{1+\eta}$ with $\eta>0$; and by the ladder implicit in the mechanism,

| support | certified proportion |
|:--:|:--:|
| $1.04$ | $0.70$ |
| $1.26$ | $0.80$ |
| $1.70$ | $0.90$ |

so that $\eta\ge0.04$ already suffices for $0.70>0.682$. This is the concrete form of the requirement usually stated as "pair correlation beyond Fourier support 1", "unconditional third moment at $X\asymp T$", or "prime pairs".

---

## 7. Why a large family of repairs cannot work **[our]**

Set $a_n=\Lambda(n)/\sqrt n$ and $h=\log(n/m)$. The inner kernel satisfies
$$\Bigl|\int_0^Te^{ih\tau}\,d\tau\Bigr|=\Bigl|\frac{e^{ihT}-1}{ih}\Bigr|\ \le\ \min\Bigl(T,\frac2{|h|}\Bigr).$$
The dominant contribution comes from the **short‑distance region** $|h|\lesssim T^{-1}$, i.e. $|n-m|\lesssim X/T$, where the kernel is $\asymp T$, and where the relevant mass is the weighted count of prime‑power pairs at short distances — i.e. prime‑pair information. A magnitude comparison (using the standard unconditional upper‑bound sieve for such pair counts) gives a short‑distance term of order $X$ against a diagonal of order $T\log^2X$, i.e. a ratio
$$\frac{|O_1|}{D}\ \asymp\ \frac{X}{T\log^2X}\ =\ \frac{T^{\eta}}{\log^2X},$$
which exceeds $1$ precisely for $X\gtrsim T\log^2X$ — consistent with the diagonal‑dominance threshold $X\ll TL$ of §5 (up to logarithmic powers).

Now the elementary point. Since
$$\Lambda(n)=\sum_{d\mid n}\mu(d)\log\frac nd$$
is an **identity**, any rearrangement of the sum — in particular any "structured decomposition" in the style of $\mu^2(n)=\sum_{d^2\mid n}\mu(d)$, or any layered regrouping of the $d$‑sum — must return the **same total**. Regrouping can therefore change an *estimate* but not the *value*. If the obstruction is a property of the value (as the magnitude computation indicates, at the Hardy–Littlewood order, up to the constants available from sieve upper bounds), then no member of the family

> rearrangement · layered decomposition · majorant / dual positivity · sharper constants · sharpness of the $\ell^2$/large‑sieve step

can repair it. This single observation accounts for several independently recorded failures of that family in our notes, and it is the reason we record the obstruction as a property of the *value* rather than of the *bound*.

Two honest qualifications. (i) The magnitude comparison is a magnitude argument, not a theorem: it uses the Hardy–Littlewood order for short‑distance prime‑power pairs, which is unconditional only as an upper bound (sieve). (ii) The assertion that no factorization of the four‑fold sum is available is an assertion about the factorizations we could find, not an impossibility theorem.

---

## 8. Related formulations of the same threshold

For completeness we record that the same threshold has appeared, in our notes, under several equivalent guises: (a) an unconditional bound for the off‑diagonal second moment beyond support 1; (b) the evaluation of the third trace at $X\asymp T$ (the diagonal method covers only $X^3\le T^{2-\varepsilon}$); (c) the canonical signed‑cancellation threshold of the Möbius series $\sum\mu(a)/(a^c\log a)=\int_c^\infty ds/\zeta(s)$, whose legal domain is $c\ge\beta_*$ — whence, unconditionally, the signed threshold equals $1$, and pushing it to $\tfrac12$ is RH itself; (d) Mertens‑strength cancellation of $\mu$ against structured kernels. These are formulations, not four independent routes.

---

## References

* [Mon73] H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Analytic Number Theory (Proc. Sympos. Pure Math. XXIV, St. Louis 1972), AMS, 1973, 181–193. MR337821.
* [MV74] H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974), 73–82.
* [RS96] Z. Rudnick, P. Sarnak, *Zeros of principal L‑functions and random matrix theory*, Duke Math. J. **81** (1996), no. 2, 269–322. DOI 10.1215/S0012-7094-96-08115-6.
* [GM87] D. A. Goldston, H. L. Montgomery, *Pair correlation of zeros and primes in short intervals*, in: Analytic Number Theory and Diophantine Problems, Birkhäuser, 1987, 183–203.
* [Pre84] E. Preissmann, *Sur une inégalité de Montgomery–Vaughan*, Enseign. Math. **30** (1984), 95–113.
* [PL13] E. Preissmann, O. Lévêque, *On generalized weighted Hilbert matrices*, Pacific J. Math. **265** (2013), 199–219.
* [Yan23] W. Yangjit, *On the Montgomery–Vaughan weighted generalization of Hilbert's inequality*, Proc. Amer. Math. Soc. Ser. B **10** (2023), 439–454; arXiv:2203.14950.
* [Rod26] B. Rodgers, *On the optimal constant in the Montgomery–Vaughan weighted Hilbert inequality*, arXiv:2608.12315 (12 Aug 2026).
* [BGSTB24] S. A. C. Baluyot, D. A. Goldston, A. S. Suriajaya, C. L. Turnage‑Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta function*, Acta Arith. **214** (2024), 357–376; arXiv:2306.04799.
* [BGSTB25] Same authors, *Pair correlation of zeros of the Riemann zeta function I: proportions of simple zeros and critical zeros*, arXiv:2501.14545 (v3, 1 Sep 2026).
* [GLSS25] D. A. Goldston, J. Lee, J. Schettler, A. S. Suriajaya, *Pair correlation conjecture for the zeros of the Riemann zeta‑function I: simple and critical zeros*, arXiv:2503.15449.
* [AF26] (frontier, cited for the bandwidth‑one ceiling and the mechanism) *More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2608.13637v2.

**Note.** The dossier of verbatim readings, audit trails, and the corresponding internal identifiers are kept in our project archive; this note restricts itself to statements that could be quoted from the sources above.
