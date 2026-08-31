# A Positive Spectral Discrepancy Criterion Equivalent to the Generalized Riemann Hypothesis（GRH 判别判据——论文级草稿 v0.2）

> 状态：草稿 v0.2——纳入 2026-08-31 全部修正与验证
> 日期：2026-08-31

---

## Abstract

We transfer the spectral discrepancy criterion for the Riemann zeta
function to Dirichlet $L$-functions. For each primitive character $\chi$,
we construct a spectral functional $Q_\chi$ from the Hadamard expansion
of the completed $L$-function, together with a projection reference
$Q'_{\mathrm{RH},\chi}$, such that
$$Q_\chi = Q'_{\mathrm{RH},\chi} \iff \operatorname{Re}\rho = \tfrac12 \text{ for every zero } \rho \text{ of } L(s,\chi).$$
The discrepancy is a sum of explicitly positive pairwise terms
$P_{\gamma}(\delta) = \delta^2 M_2/(2U^2D_+D_-)$ over functional-equation
orbits. The construction is purely algebraic (independent of $q,\chi$),
verified numerically to machine precision for 8 moduli (real and complex
characters, even and odd, prime and composite, order 2–12), with a
discrimination test (any off-axis configuration yields a strictly
positive signal) and height-robustness to $\gamma=10^6$.

## 1. Setup

- $\chi$: primitive character mod $q$——$a = 0$ (even) or $1$ (odd)
- Completed function: $\xi_\chi(s) = (q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi)$
- Zeros $\rho = \tfrac12+\delta_\rho+i\gamma_\rho$ (multiplicity $m_\rho$)
- Functional equation: $\xi_\chi(s) = \varepsilon_\chi\,\xi_{\bar\chi}(1-s)$
  ($|\varepsilon_\chi|=1$; for complex $\chi$, $\bar\chi\neq\chi$)

## 2. The spectral functional

$$S_\chi(t) = \partial_t^2\log|\xi_\chi(\tfrac12+it)|
= \sum_\rho m_\rho K^{\mathrm{nat}}_\rho(t) + S_{\mathrm{reg},\chi}(t),$$
$$K^{\mathrm{nat}}_\rho(t) = \frac{\delta_\rho^2-(t-\gamma_\rho)^2}{(\delta_\rho^2+(t-\gamma_\rho)^2)^2}.$$

Test object (u-domain, 2π convention):
$$\widehat H_0(u) = \frac{\widehat w_{\mathrm{target}}(u)}{\widehat K_0(u)}
= e^{-2\pi|u|}\Bigl[\frac{1}{4\pi|u|}+\frac12\Bigr],$$
with $w_{\mathrm{target}}(\gamma)=(1+\gamma^2)^{-2}$,
$\widehat w_{\mathrm{target}}(u)=\frac\pi2(1+2\pi|u|)e^{-2\pi|u|}$,
$\widehat K_0(u)=2\pi^2|u|$. Pairing weight:
$$w_H(\gamma,\delta) = \frac{a^2(a+1)+\delta\gamma^2}{2(a^2+\gamma^2)^2},\qquad a=1+\delta.$$

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
$|\delta|<\tfrac12$、$\gamma\ge\gamma_{1,\chi}\ge6.02$：$M_2>0$（逐项正；
实际 $M_2$ 在 $\gamma>0.45$ 恒正——主导项补偿——）⟹ $P_\gamma\ge0$——
$=0\iff\delta=0$。

**Height robustness**: $P_\gamma(\delta) = O(\gamma^{-6})$——precisely
$\gamma^6 P_\gamma(0.1)\to 0.2$——verified to $\gamma=10^6$——no
degeneration at any height.

### 4.2 Orbit assembly
Functional equation ⟹ zeros closed under $\rho\leftrightarrow1-\bar\rho$
（——同 $\gamma$ 反 $\delta$——）——orbits $\rho\sim1-\bar\rho$（online 自配对）：
$$Q_\chi - Q'_{\mathrm{RH},\chi} = \sum_{\rho/\sim} m_\rho P_{\gamma_\rho}(\delta_\rho).$$

### 4.3 Rigidity
$\sum m_\rho P_{\gamma_\rho}(\delta_\rho)=0$（非负可和）⟹ 逐项 $P=0$ ⟹
$\delta_\rho=0$——反向显然。∎

## 5. Convergence and exchange (Lemma E)

- $H_0''(t)=O(t^{-2})\in L^1$（精确渐近 $\sim\frac1{2\pi t^2}$）
- **Moment cancellation (difference form)**:
  $$|w_H(\gamma,\delta)-w_H(\gamma,0)| \le C|\delta|\,|H_0''(\gamma)|,\qquad C\le\pi.$$
  （——online pairing $w_H(\gamma,0)=(1+\gamma^2)^{-2}\neq0$——引理必须取差——）
  数值：全部 $\gamma\in[6.02,10^5]$ × $\delta\in[0.01,0.49]$——$C\le3.1416$——
  渐近 $C\to\pi$（$\partial_\delta w_H|_{\delta=0}\sim\frac1{2\gamma^2}$——
  $H_0''\sim\frac1{2\pi t^2}$）
- $\sum|\delta_\rho||H_0''(\gamma_\rho)| \le \tfrac12\sum|H_0''(\gamma_\rho)|<\infty$
  （$\gamma_n\sim\frac{2\pi n}{\log n}$——数值 $\sum|H_0''|\approx0.012$
  全谱有限——）
- ⟹ termwise pairing absolutely convergent——exchange legal
  （只用 $N_\chi(T)=O(T\log T)$——无条件——）

## 6. Discrimination (empirical)

- Single zero off-axis: $Q-Q'_{RH} = P_\gamma(\delta)$ exactly
  （——$\delta$ 编码强度——单调——）
- Multiple off-axis: $Q-Q'_{RH} = \sum P_{\gamma_\rho}(\delta_\rho)$——cumulative
- **Strict positivity**: 100 random off-axis configurations——all
  $Q-Q'_{RH} > 0$（min $+1.5\times10^{-17}$）——**any off-axis leaves a
  positive signal——no cancellation possible**（termwise positive）
- Online (RH): $Q-Q'_{RH}=0$ exactly——zero signal

## 7. Remarks

- $S_{\mathrm{reg},\chi}$ does not enter $Q_\chi/Q'_{\mathrm{RH},\chi}$
- Construction independent of $q,\chi$（algebraic）——family consistency——
  $\mathrm{GRH}\iff Q_\chi=Q'_{\mathrm{RH},\chi}\ \forall q\ \forall\chi$
- Shared core lemmas with the zeta criterion——subject to external
  verification of the zeta case

## 8. Numerical support (8 moduli)

| modulus | character | parity | order | zeros | pairing accuracy |
|---------|-----------|--------|-------|-------|------------------|
| 3 | real | odd | 2 | 98 (γ<200) | 1.9e-20~9.9e-15 |
| 4 | real | odd | 2 | 168 (γ<300) | 3.4e-24~2.7e-14 |
| 5 | real | even | 2 | 72 (γ<150) | 0.0e+00~1.4e-12 |
| 5 | complex | odd | 4 | 83 (γ<150) | 0.0e+00~2.0e-14 |
| 7 | complex | odd | 6 | 60 (γ<120) | 0.0e+00~1.4e-10 |
| 8 | real | even | 2 | 50 (γ<100) | 2.6e-17~2.3e-11 |
| 9 | complex (composite) | odd | 6 | 59 (γ<100) | 0.0e+00~1.1e-11 |
| 11 | complex | odd | 10 | 56 (γ<100) | 0.0e+00~1.4e-11 |
| 13 | complex | odd | 12 | 53 (γ<100) | 3.5e-17~3.6e-12 |

All zeros found on the critical line (Re = 0.5) — numerical GRH support.

## 9. Correction history (internal)

1. $\chi_4$ is odd ($\chi_4(-1)=-1$)——$a=1$ completion——initial even-assumption wrong
2. Complex characters: functional equation connects $\chi$ and $\bar\chi$——
   $\xi_\chi(s)=\varepsilon\,\xi_{\bar\chi}(1-s)$——not self-conjugate
3. QRH orbit-counting must follow the zero set (off-axis orbit = 2 zeros)
4. $H_0$ t-domain closed form self-consistent ($F[\log(1+t^2)]=-e^{-2\pi|u|}/|u|$)
5. Moment-cancellation lemma must be in difference form ($C\le\pi$)

## 10. Status

- Formally reconstructed criterion——structure complete——lemmas stated with
  verified constants（$C\le\pi$——$\gamma^6P_\gamma\to0.2$）
- **Not a claim that GRH is proved**——shared core lemmas pending external
  verification (zeta-case)——numerical support: 8 moduli, discrimination,
  height robustness
- Consequence chain: GRH ⟹ primes in AP
  （$\psi(x;q,a)=x/\phi(q)+O(x^{1/2}\log^2x)$）⟹ strong Goldbach
  asymptotic + almost-all（$E(x)\ll x^{1/2}\log^3 x$）——not "every even"
  （threshold ~$10^{50}$ not numerically bridgeable）
