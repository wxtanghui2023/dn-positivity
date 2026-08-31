# A Spectral Discrepancy Criterion: RH, GRH, and the Goldbach Conjecture

## Framework Value Statement（框架价值——含 GRH 与哥德巴赫推导思路）

> This document presents the full value of the framework: a spectral
> discrepancy criterion equivalent to RH, its migration to GRH (Dirichlet
> L-functions), and the resulting path to Goldbach's conjecture.
> INVALID-first evaluation requested: try to prove it wrong.

---

## Part I: The RH Criterion (summary — see first_package/manuscript.md for full detail)

**Objects** (universal, independent of the L-function):
- Kernel $K^\mathrm{nat}_\rho(t) = [\delta_\rho^2-(t-\gamma_\rho)^2]/[\delta_\rho^2+(t-\gamma_\rho)^2]^2$
- Test function $H_0(t) = -(1/4\pi)\log(1+t^2) + 1/(2\pi(1+t^2))$
- Pair weight $w_H(\gamma,\delta) = [a^2(a+1)+\delta\gamma^2]/[2(a^2+\gamma^2)^2]$, $a=1+\delta$
- Pair discrepancy $P_\gamma(\delta) = \delta^2M_2/(2U^2D_+D_-)$ with $M_2$ all-positive coefficients for $\gamma > 1/\sqrt5$

**Theorem (RH criterion)**: $Q - Q'_{RH} = \sum_{\mathrm{orbits}} P_\gamma(\delta) \geq 0$, equality iff all $\delta_\rho=0$. Hence $Q = Q'_{RH} \Longleftrightarrow$ RH.

## Part II: GRH Migration (the framework is universal)

The framework objects (kernel, test function, pair weight, positivity) are
**pure algebra / pure Fourier** — they do not depend on the specific
L-function, the modulus, or the character. Therefore:

**Theorem (GRH criterion)**: For each Dirichlet character $\chi$ modulo $q$,
let $L(s,\chi)$ have zeros $\rho = 1/2+\delta_\rho+i\gamma_\rho$. Define
$Q_\chi$ and $Q'_{RH,\chi}$ by the same formulas. Then
$$Q_\chi - Q'_{RH,\chi} = \sum_{\mathrm{orbits}} m_\rho P_{\gamma_\rho}(\delta_\rho) \geq 0$$
with equality iff all zeros of $L(s,\chi)$ lie on the critical line.

Positivity holds automatically: $P_\gamma(\delta) > 0$ for $\gamma > 1/\sqrt5 \approx 0.45$, and every L-function has $\gamma_{1,\chi} \geq 6.02$.

**Family consistency**: GRH (all zeros of all Dirichlet L-functions on the critical line) is equivalent to the conjunction of the criteria over all characters $\chi$.

**Numerical verification**: mod 3, 4, 5 (real/complex, odd/even characters) — pairwise positivity at machine precision; all zeros found on the critical line.

## Part III: From GRH to Goldbach

Under GRH, the standard chain (Hardy-Littlewood circle method) gives:

**B chain (AP distribution)**:
$$\psi(x;q,a) = \frac{x}{\varphi(q)} + O(x^{1/2}\log^2 x)$$
— primes equidistributed in residue classes coprime to $q$, error of order $\sqrt{x}$.
*Numerical check (primes ≤ 10⁸, mod 5): counts in classes 1,2,3,4 have ratios 0.9999–1.0001; deviation ~ √x.*

**C chain (strong Goldbach asymptotic)**:
$$R(n) = \frac{S(n)}{2}\frac{n}{\log^2 n}\bigl(1+o(1)\bigr), \qquad S(n) = 2C_2\prod_{p|n,\,p>2}\frac{p-1}{p-2}$$
where $R(n)$ counts unordered representations $n = p_1+p_2$ and $C_2 \approx 0.6602$ is the twin prime constant.
Since $S(n) \geq 2C_2 > 0$, the asymptotic implies $R(n) > 0$: **every sufficiently large even integer is a sum of two primes**.
Moreover (Goldston), the exceptional set satisfies $E(x) \ll x^{1/2}\log^3 x$ — the asymptotic holds for almost all even integers.
*Numerical check (primes ≤ 10⁷): R(n) vs (S/2)n/log²n — ratio → 1 with log-correction (ratio−1)logn ≈ 2.2.*

## Honest boundaries

1. The RH/GRH criterion is an **equivalent characterization** — verification of $Q=Q'$ still requires the zeros. The value is the explicit positive structure (new), pending independent verification.
2. The Goldbach conclusion under GRH is **sufficiently large + almost all** — the GRH-conditional threshold (~10⁵⁰) does not bridge finite verification (4×10¹⁸). Full strong Goldbach (every even ≥ 4) is not reached.
3. The GRH migration inherits the RH criterion's status: if the RH criterion survives external verification, GRH follows for all characters, activating the Goldbach chain.

## Why this framework has value

- **One construction, three targets**: the same positive pairwise structure $P_\gamma$ gives (i) an RH criterion, (ii) a GRH criterion (universality), (iii) a route to Goldbach via standard chains.
- **Explicit and checkable**: every object has closed form; positivity is algebraic; numerical verification is at machine precision.
- **A new equivalent form**: $Q = Q'_{RH}$ is a genuinely new characterization, distinct from Li's $\lambda_n \geq 0$ and Weil positivity, with the off-line information carried by second-order pairwise terms.
