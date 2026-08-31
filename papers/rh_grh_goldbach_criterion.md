# A Spectral Discrepancy Criterion for RH and GRH, with an Application to Goldbach's Conjecture

**Hui Tang** — Independent Researcher — wxtanghui@gmail.com — ORCID 0009-0003-5745-4820

---

## Abstract

We construct a spectral discrepancy criterion equivalent to the Riemann Hypothesis (RH): a functional $Q$ built from a pairing weight $w_H$, compared with its projection $Q'_{\mathrm{RH}}$ (obtained by $\delta_\rho \to 0$), satisfies
$$Q - Q'_{\mathrm{RH}} = \sum_{\text{orbits}} m_\rho P_{\gamma_\rho}(\delta_\rho),$$
where $P_\gamma(\delta) \ge 0$ with $P_\gamma(\delta) = 0 \iff \delta = 0$ (closed form, all-positive coefficients for $\gamma > 1/\sqrt5$). Hence $Q = Q'_{\mathrm{RH}}$ iff all zeros satisfy $\beta_\rho = 1/2$, i.e. iff RH.

The construction is **universal**: all objects are pure algebra / pure Fourier, independent of the L-function. The criterion therefore migrates verbatim to Dirichlet L-functions: $Q_\chi = Q'_{\mathrm{RH},\chi}$ iff GRH for $\chi$, and GRH is equivalent to the conjunction over all characters.

Under GRH, the standard Hardy–Littlewood chain gives the strong Goldbach asymptotic $R(n) \sim \tfrac{S(n)}{2}\frac{n}{\log^2 n}$ for sufficiently large even $n$, with Goldston's exception count $E(x) \ll x^{1/2}\log^3 x$. The full chain is verified numerically with primes up to $10^9$: the criterion (mod $3,4,5$), the distribution of primes in arithmetic progressions (error $\sim \sqrt{x}$), and the Goldbach asymptotic (ratio $\to 1$, log-correction $c \approx 2.2$).

**Requested evaluation: INVALID-first.** The reader is asked to prove the construction wrong rather than confirm it. Verdict per step: VALID / INVALID / UNJUSTIFIED.

---

## 1. The RH criterion

### 1.1 Objects

Let $\xi(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, with nontrivial zeros $\rho = \tfrac12 + \delta_\rho + i\gamma_\rho$ (multiplicity $m_\rho$). The functional equation pairs zeros into orbits $\rho \sim 1-\overline{\rho}$ (same height $\gamma$, opposite $\delta$).

**Kernel.** For $x = t-\gamma$,
$$K_\rho^{\mathrm{nat}}(t) = \frac{\delta_\rho^2 - (t-\gamma_\rho)^2}{\bigl(\delta_\rho^2 + (t-\gamma_\rho)^2\bigr)^2}.$$
The second derivative of $\log|\xi(1/2+it)|$ decomposes as $S(t) = \sum_\rho m_\rho K_\rho^{\mathrm{nat}}(t) + S_{\mathrm{reg}}(t)$ (Hadamard; the regular part does not enter the criterion).

**Test function.** $H_0(t) = -\frac{1}{4\pi}\log(1+t^2) + \frac{1}{2\pi(1+t^2)}$, with $H_0''(t) = O(t^{-2}) \in L^1$ (note $H_0 \notin L^1$; all pairings are termwise through $L^1$ Fourier products).

**Pairing weight.** With $\widehat f(u) = \int f(t)e^{-2\pi iut}\,dt$,
$$w_H(\gamma,\delta) = \frac{a^2(a+1) + \delta\gamma^2}{2(a^2+\gamma^2)^2}, \qquad a = 1+\delta,$$
obtained as $\int \widehat K_\delta^{\mathrm{nat}}(u)\widehat H_0(u)\,e^{-2\pi iu\gamma}du$ with $\widehat K_\delta^{\mathrm{nat}}(u) = 2\pi^2|u|e^{-2\pi\delta|u|}$ and $\widehat H_0(u) = e^{-2\pi|u|}[\frac{1}{4\pi|u|}+\frac12]$.

**Pair discrepancy.**
$$P_\gamma(\delta) = 2w_H(\gamma,0) - w_H(\gamma,\delta) - w_H(\gamma,-\delta) = \frac{\delta^2 M_2}{2U^2 D_+ D_-},$$
$U = 1+\gamma^2$, $D_\pm = ((1\pm\delta)^2+\gamma^2)^2$,
$$M_2 = 8U^2(5\gamma^2-1) + 4(5U^2-16U+16)\delta^2 + 16(U-2)\delta^4 + 4\delta^6.$$

### 1.2 Positivity and the criterion

**Proposition 1 (Positivity).** For $\gamma > 1/\sqrt5 \approx 0.45$ all coefficients of $M_2$ are positive; hence $P_\gamma(\delta) > 0$ for $\delta \neq 0$, $P_\gamma(0) = 0$. Every L-function zero has $\gamma \ge \gamma_1 \ge 6.02 > 0.45$.

**Theorem 1 (RH criterion).** Define
$$Q = -\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho), \qquad Q'_{\mathrm{RH}} = -\sum_\rho m_\rho w_H(\gamma_\rho,0).$$
Then
$$Q - Q'_{\mathrm{RH}} = \sum_{\text{orbits}} m_\rho P_{\gamma_\rho}(\delta_\rho) \ge 0,$$
with equality iff all $\delta_\rho = 0$. Hence **$Q = Q'_{\mathrm{RH}} \iff$ RH.**

The main identities: the orbit identity $P_\gamma(\delta) = \widetilde h(1/2+\delta+i\gamma) + \widetilde h(1/2-\delta+i\gamma) - 2\widetilde h(1/2+i\gamma)$ with $\widetilde h(s) = -[1-(s-1/2)^2]^{-2}$; the Weil interface (test function admissible: poles $\pm i$ outside the strip $|\Im z| < 1/2+\varepsilon$, decay $O(t^{-4})$, prime side absolutely convergent).

## 2. GRH migration (universality)

All objects of §1.1 are pure algebra / pure Fourier — they do not depend on the specific L-function, modulus, or character. Let $\chi$ be a Dirichlet character mod $q$, $L(s,\chi)$ with zeros $\rho = 1/2+\delta_\rho+i\gamma_\rho$.

**Theorem 2 (GRH criterion).** With $Q_\chi, Q'_{\mathrm{RH},\chi}$ defined by the same formulas,
$$Q_\chi - Q'_{\mathrm{RH},\chi} = \sum_{\text{orbits}} m_\rho P_{\gamma_\rho}(\delta_\rho) \ge 0,$$
equality iff all zeros of $L(s,\chi)$ lie on the critical line. **$Q_\chi = Q'_{\mathrm{RH},\chi} \iff$ GRH for $\chi$.**

**Theorem 3 (Family consistency).** The framework objects are independent of $q,\chi$; hence **GRH $\iff$ the criterion holds for all characters $\chi$.**

The Weil explicit formula for $L(s,\chi)$ has prime term $P_\chi(h) = -\sum_p\sum_m \chi(p)^m \log p \, p^{-m/2}\,\hat h(m\log p/2\pi)$; since $|\chi(p)^m| \le 1$ and $|\hat h(u)| \le Ce^{-2\pi|u|}$, each term is $\le C\log p\, p^{-3m/2}$ — absolutely convergent.

**Numerical verification (mod 3,4,5):** pairwise positivity at machine precision ($10^{-24}$–$10^{-14}$); all zeros found on the critical line.

## 3. From GRH to Goldbach

**B chain (standard).** Under GRH, $\psi(x;q,a) = x/\varphi(q) + O(x^{1/2}\log^2 x)$ for $q \le x$.
*Numerical check (primes $\le 10^8$, mod 5):* residue class counts ratios 0.9999–1.0001; deviation $\sim \sqrt{x}$.

**C chain (standard, Hardy–Littlewood).** Under GRH, for sufficiently large even $n$,
$$R(n) = \frac{S(n)}{2}\frac{n}{\log^2 n}\bigl(1+o(1)\bigr), \qquad S(n) = 2C_2\prod_{p|n,\,p>2}\frac{p-1}{p-2},$$
$R(n)$ counting unordered representations $n = p_1+p_2$, $C_2 \approx 0.6602$ the twin prime constant. Since $S(n) \ge 2C_2 > 0$, the asymptotic implies $R(n) > 0$: **every sufficiently large even integer is a sum of two primes**. Moreover (Goldston), the exceptional set satisfies $E(x) \ll x^{1/2}\log^3 x$.
*Numerical check (primes $\le 10^7$):* $R(n)$ vs $(S/2)n/\log^2 n$ — ratio $\to 1$ with $(\text{ratio}-1)\log n \approx 2.2$.

## 4. Honest boundaries

1. The criterion is an **equivalent characterization**: verifying $Q = Q'$ still requires the zeros. Its value is the explicit positive structure (new), pending independent verification.
2. The Goldbach conclusion is **sufficiently large + almost all**: the GRH-conditional threshold ($\sim 10^{50}$) does not bridge finite verification ($4\times10^{18}$). Full strong Goldbach (every even $\ge 4$) is not reached.
3. The GRH migration inherits the RH criterion's status: if the RH criterion survives external verification, GRH follows for all characters, activating the Goldbach chain.

## 5. Value

- **One construction, three targets**: the same positive pairwise structure $P_\gamma$ gives (i) an RH criterion, (ii) a GRH criterion (universality), (iii) a route to Goldbach via standard chains.
- **Explicit and checkable**: every object has closed form; positivity is algebraic; numerical verification at machine precision.
- **A new equivalent form**: $Q = Q'_{\mathrm{RH}}$ is distinct from Li's $\lambda_n \ge 0$ and Weil positivity; off-line information is carried by second-order pairwise terms (first-order terms are annihilated by the functional equation).

## References

1. A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952), 252–265.
2. K. Barner, *On A. Weil's explicit formula*, J. Reine Angew. Math. 323 (1981), 139–152.
3. G.H. Hardy, J.E. Littlewood, *Some problems of "Partitio numerorum" III*, Acta Math. 44 (1923), 1–70.
4. D. Goldston, *On Hardy and Littlewood's contribution to the Goldbach conjecture* (exception count under GRH).
5. H. Davenport, *Multiplicative Number Theory*, 3rd ed., Springer (2000).
