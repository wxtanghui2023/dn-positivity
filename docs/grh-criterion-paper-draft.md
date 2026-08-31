# A Positive Spectral Discrepancy Criterion Equivalent to the Generalized Riemann Hypothesis（GRH 判别判据——论文级草稿）

> 状态：草稿 v0.1——结构完整——引理严格化待完善——数值支撑（6 模）
> 日期：2026-08-31

---

## Abstract

We transfer the spectral discrepancy criterion for the Riemann zeta function
to Dirichlet $L$-functions. For each primitive character $\chi$, we construct
a spectral functional $Q_\chi$ from the Hadamard expansion of the completed
$L$-function, together with a projection reference $Q'_{\mathrm{RH},\chi}$,
such that
$$Q_\chi = Q'_{\mathrm{RH},\chi} \iff \operatorname{Re}\rho = \tfrac12 \text{ for every zero } \rho \text{ of } L(s,\chi).$$
The discrepancy is a sum of explicitly positive pairwise terms
$P_{\gamma}(\delta) = \delta^2 M_2/(2U^2D_+D_-)$ over functional-equation
orbits. The construction is purely algebraic (independent of $q,\chi$),
verified numerically to machine precision for moduli $3,4,5,7,8,11$
(real and complex characters, even and odd).

## 1. Setup

- $\chi$: primitive character mod $q$——$a = 0$ (even) or $1$ (odd)
- Completed function: $\xi_\chi(s) = (q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi)$
- Zeros $\rho = \tfrac12+\delta_\rho+i\gamma_\rho$ (multiplicity $m_\rho$)
- Functional equation: $\xi_\chi(s) = \varepsilon_\chi\,\xi_{\bar\chi}(1-s)$
  ($|\varepsilon_\chi|=1$)

## 2. The spectral functional

$$S_\chi(t) = \partial_t^2\log|\xi_\chi(\tfrac12+it)|
= \sum_\rho m_\rho K^{\mathrm{nat}}_\rho(t) + S_{\mathrm{reg},\chi}(t),$$
$$K^{\mathrm{nat}}_\rho(t) = \frac{\delta_\rho^2-(t-\gamma_\rho)^2}{(\delta_\rho^2+(t-\gamma_\rho)^2)^2}.$$

Test object (u-domain definition, 2π convention):
$$\widehat H_0(u) = \frac{\widehat w_{\mathrm{target}}(u)}{\widehat K_0(u)}
= e^{-2\pi|u|}\Bigl[\frac{1}{4\pi|u|}+\frac12\Bigr],$$
with $w_{\mathrm{target}}(\gamma)=(1+\gamma^2)^{-2}$,
$\widehat w_{\mathrm{target}}(u)=\frac\pi2(1+2\pi|u|)e^{-2\pi|u|}$,
$\widehat K_0(u)=2\pi^2|u|$. Pairing weight:
$$w_H(\gamma,\delta) = \langle K^{\mathrm{nat}}_\delta(\cdot-\gamma),H_0\rangle
= \frac{a^2(a+1)+\delta\gamma^2}{2(a^2+\gamma^2)^2},\qquad a=1+\delta.$$

## 3. The criterion

$$Q_\chi = -\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho),\qquad
Q'_{\mathrm{RH},\chi} = -\sum_\rho m_\rho w_H(\gamma_\rho,0).$$

**Theorem.** $Q_\chi = Q'_{\mathrm{RH},\chi} \iff \delta_\rho=0\ \forall\rho \iff \mathrm{GRH}_\chi$.

## 4. Proof

### 4.1 Pairwise positivity (Lemma P)
$$P_\gamma(\delta) = 2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)
= \frac{\delta^2 M_2(\gamma,\delta^2)}{2U^2D_+D_-},$$
$$M_2 = 8U^2(5\gamma^2-1) + 4(5U^2-16U+16)\delta^2 + 16(U-2)\delta^4 + 4\delta^6,$$
$U=1+\gamma^2$——$D_\pm = ((1\pm\delta)^2+\gamma^2)^2$。对
$|\delta|<\tfrac12$、$\gamma\ge\gamma_{1,\chi}\ge6.02$：$M_2>0$（——逐项正——
$5\gamma^2-1>0$——$5U^2-16U+16$ 判别式 $<0$ 恒正——$U-2>0$——）
⟹ $P_\gamma(\delta)\ge0$——$=0\iff\delta=0$。

### 4.2 Orbit assembly
Functional equation ⟹ zeros closed under $\rho\leftrightarrow1-\bar\rho$
（——同 $\gamma$ 反 $\delta$——）——orbits $\rho\sim1-\bar\rho$（online 自配对）：
$$Q_\chi - Q'_{\mathrm{RH},\chi} = \sum_{\rho/\sim} m_\rho P_{\gamma_\rho}(\delta_\rho).$$

### 4.3 Rigidity
$\sum m_\rho P_{\gamma_\rho}(\delta_\rho)=0$（非负可和）⟹ 逐项 $P=0$ ⟹
$\delta_\rho=0$——反向显然。∎

## 5. Convergence and exchange (Lemma E)

- $H_0''(t)=O(t^{-2})\in L^1$（——精确渐近 $\sim\frac1{2\pi t^2}$——）
- Moment cancellation: $|\langle K^{\mathrm{nat}}_\rho,H_0\rangle|
  \le C|\delta_\rho||H_0''(\gamma_\rho)|$（——M₀=M₁=0——）
- $\sum|\delta_\rho||H_0''(\gamma_\rho)| \le \tfrac12\sum|H_0''(\gamma_\rho)|<\infty$
  （$\gamma_n\sim\frac{2\pi n}{\log n}$——数值 $\sum|H_0''|\approx0.013$ 有限——）
- ⟹ termwise pairing absolutely convergent——exchange legal
  （——只用 $N_\chi(T)=O(T\log T)$——无条件——）

## 6. Remarks

- $S_{\mathrm{reg},\chi}$ does not enter $Q_\chi/Q'_{\mathrm{RH},\chi}$
  （——projection difference cancels——）
- The construction is independent of $q,\chi$ (algebraic)——family consistency
  automatic——$\mathrm{GRH}\iff Q_\chi=Q'_{\mathrm{RH},\chi}\ \forall q\ \forall\chi$
- Shared core lemmas with the zeta criterion (——moment cancellation,
  positivity, pairing——)——subject to external verification of the zeta case

## 7. Numerical support

| modulus | character | parity | zeros | pairing accuracy |
|---------|-----------|--------|-------|------------------|
| 3 | real (quadratic) | odd | 98 (γ<200) | 1.9e-20~9.9e-15 |
| 4 | real (quadratic) | odd | 168 (γ<300) | 3.4e-24~2.7e-14 |
| 5 | real (quadratic) | even | 72 (γ<150) | 0.0e+00~1.4e-12 |
| 5 | complex (4th) | odd | 83 (γ<150) | 0.0e+00~2.0e-14 |
| 7 | complex (6th) | odd | 60 (γ<120) | 0.0e+00~1.4e-10 |
| 8 | real (quadratic) | even | 50 (γ<100) | 2.6e-17~2.3e-11 |
| 11 | complex (10th) | odd | 56 (γ<100) | 0.0e+00~1.4e-11 |

All zeros found on the critical line (Re = 0.5) — numerical GRH support.

## 8. Status

- Formally reconstructed criterion——structure complete——lemmas stated
- **Not a claim that GRH is proved**——shared core lemmas pending external
  verification (zeta-case)——numerical support for 6 moduli
- Consequence chain: GRH ⟹ primes in AP (ψ(x;q,a)=x/φ(q)+O(x^{1/2}log²x))
  ⟹ strong Goldbach asymptotic + almost-all (E(x) ≪ x^{1/2}log³x)
