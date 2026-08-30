# Referee Response Appendix（v2.12.1）

> 预答审稿问题——随投稿预备——不承诺替代独立验证
> 状态：Draft v2.12.1（2026-08-30 21:45）

---

## Comment 1：Q'_RH 是否假设 RH？

**Response：** No. $Q'_{\mathrm{RH}}$ is defined by the reference projection
$$\rho=\beta+i\gamma \;\longmapsto\; \rho^\ast=\tfrac12+i\gamma_\rho,$$
preserving only ordinate and multiplicity. This is a reference spectrum,
not an assertion that $\rho^\ast$ is a zero of $\zeta$. The value
$w_H(\gamma_\rho,0)=(1+\gamma_\rho^2)^{-2}$ depends only on the actual
ordinates; no RH assumption enters.

## Comment 2：正性是否全局成立？

**Response：** The required positivity is asserted only on the support of
the nontrivial zero spectrum: for $|\gamma_\rho|\ge\gamma_1=14.1347\ldots$
and $0<|\delta_\rho|<\tfrac12$, $\Delta_H(\gamma_\rho,\delta_\rho)>0$ when
$\delta_\rho\ne0$. It is **not** a pointwise assertion on the whole
$(\gamma,\delta)$-plane (indeed $\Delta_H(0,\delta)<0$). The equality
condition only needs positivity of every term in the sum, which holds
pointwise on the spectral set.

## Comment 3：论证是否要求 H_0 ∈ L¹？

**Response：** No. Although $H_0(t)\sim\log|t|\notin L^1$, all pairings are
defined distributionally through the second derivative:
$$\langle S,H_0\rangle=\langle \log|\xi(\tfrac12+it)|,H_0''\rangle,$$
and $H_0''(t)=O(t^{-2})\in L^1$, so the pairing is finite. The zero part is
defined through the products $\widehat K_\delta\widehat H_0\in L^1$.

## Comment 4：这只是 Weil criterion 的重写？

**Response：** No. The classical Weil criterion requires positivity of a
functional for an entire class of test functions $H$. Here a single,
explicitly constructed test object $H_0$ yields a rigid discrepancy
identity
$$Q(H_0)-Q'_{\mathrm{RH}}=\sum_\rho\Delta_H(\gamma_\rho,\delta_\rho)$$
with $\Delta_H(\gamma_\rho,\delta_\rho)>0$ for $\delta_\rho\ne0$ and
$\Delta_H(\gamma_\rho,0)=0$. The contribution is the existence of a
spectral rigidity detector, not the explicit formula itself.

## Comment 5：RH 用在哪里？

**Response：** Nowhere in the construction. The critical-strip bound
$|\delta_\rho|<\tfrac12$ is unconditional; the positivity is a closed-form
algebraic statement; the interchange uses only $N(T)=O(T\log T)$; the Weil
formula is an external theorem. The Riemann Hypothesis appears only as the
equality condition: $Q(H_0)=Q'_{\mathrm{RH}}$ if and only if
$\operatorname{Re}\rho=\tfrac12$ for every nontrivial zero.

---

## 附加说明

- 本 Appendix 不承诺替代独立专家验证；最终有效性与所述分布化 Weil 框架的适用性绑定。
- 措辞红线全程遵守：criterion equivalent to RH——非 "proof of RH"。
