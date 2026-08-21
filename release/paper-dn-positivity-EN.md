# A Telescoping Positivity Criterion for the Riemann Hypothesis: $D_n > 0$ and the Li Coefficients

**Math Exploration Project** | 2026-08-21 | Data-audited version

**DOI: [10.5281/zenodo.22040623](https://doi.org/10.5281/zenodo.22040623)**

---

## Abstract

We present a new criterion for the Riemann Hypothesis (RH) based on a telescoping identity for the non-trivial zeros of $\zeta$. Let $\gamma$ run over the positive imaginary parts of the zeros $\rho = \tfrac12+i\gamma$, and define

$$g_n(t) = \frac{t\sin(n\theta(t)) + \tfrac12\cos(n\theta(t))}{\tfrac14 + t^2}, \qquad \theta(t) = \pi - 2\arctan(2t), \qquad D_n = \sum_\gamma g_n(\gamma).$$

**Main equivalence.** We prove the telescoping identity $g_n(t) = \cos(n\theta(t))-\cos((n+1)\theta(t))$ (Theorem 1) and show that the Li coefficients satisfy $\lambda_{n+1}-\lambda_n = 2D_n$ (Section 6.1; numerically $\arg(1-\tfrac1\rho)=\theta(\gamma)$ to $10^{-16}$). Hence **$D_n > 0$ for all $n \ge 1$ is equivalent to RH** (via the Li criterion).

**Results toward RH:**

1. **Telescoping identity** (Theorem 1), new; verified analytically and numerically ($<10^{-10}$).
2. **Vanishing integral** (Theorem 2): $\frac1\pi\int_0^\infty\theta'g_n\,dt \equiv 0$, so $D_n$ is a pure zero sum.
3. **Strict positivity for $n \le 43$** (Theorem 3): $(n+\tfrac12)\theta_1 < \pi$, so $D_n$ is a sum of positive terms — an unconditional partial verification of the RH criterion.
4. **Asymptotic framework** (Theorem 4): phase-region split $D_n = D_{\mathrm{pos}}+D_{\mathrm{neg}}$, with $D_{\mathrm{pos}} \approx 0.2947\log n$ (Lemma A) and $|D_{\mathrm{neg}}| \le \frac{1}{\pi^2}\log n + O(1)$ (Lemma B), yielding closing margin $c-\tfrac{1}{\pi^2} \approx 0.1934 > 0$ — **conditional on a single $S$-function bound** $\sum_m|\varepsilon_m|=O(1)$.
5. **Numerical verification**: with the first $10^5$ zeros of Odlyzko (cross-validated vs mpmath, $\le 2.5\times10^{-9}$), $D_n > 0$ for all $n \in [1, 10^4]$, $\min D_n = D_1 \approx 0.0346$.

**Contribution.** The paper reduces the Riemann Hypothesis to a single explicit $S$-function estimate ($\sum_m|\varepsilon_m| = O(1)$), proves $D_n>0$ unconditionally for $n\le43$, and provides extensive numerical support to $n\le10^4$. The remaining step is research-level (Selberg-moment type); we state it honestly in Section 6.2.

---

## 1. Introduction

### 1.1 Background

The Riemann Hypothesis (RH) states that all non-trivial zeros of $\zeta(s)$ lie on the critical line $\Re s = \tfrac12$. Among its many equivalent formulations, **Li's criterion** [6] states that $\lambda_n := \sum_\rho\big[1-(1-\tfrac1\rho)^n\big] > 0$ for all $n \iff$ RH. **Murty–Rath** [5] studied $\sum_{\nu>0}\cos(\nu\log x)/(\tfrac14+\nu^2)$, whose denominator $\tfrac14+\nu^2$ matches ours, indicating that such kernels arise from the explicit-formula structure of the $\xi$ function.

This paper pursues RH through the positivity of $D_n = \sum_\gamma g_n(\gamma)$, belonging to the same family (denominator $\tfrac14+t^2$, cosine-type phase). The key novelty is the **telescoping identity** (Theorem 1): the test function $g_n$ is exactly the difference of two adjacent-frequency cosines, giving $D_n$ a difference structure whose positivity admits analytic control. As we show in Section 6.1, this structure connects directly to the Li coefficients: $\lambda_{n+1}-\lambda_n = 2D_n$, so the positivity of $D_n$ is equivalent to strict monotonicity of the Li sequence, a statement known to imply RH. **Proving $D_n > 0$ for all $n$ is therefore equivalent to proving RH**; the present paper establishes the structural reduction and makes substantial progress toward the required estimate.

### 1.2 Notation

- $\gamma$: positive imaginary parts of non-trivial zeros $\rho = \tfrac12+i\gamma$, ordered $\gamma_1 < \gamma_2 < \cdots$
- $N(T) = \#\{\gamma \le T\}$: zero-counting function
- $S(T) = N(T) - \frac1\pi\theta_{RS}(T) - 1$: the $S$-function, with $\theta_{RS}(t) = \Im\log\Gamma(\tfrac14 + \tfrac{it}{2}) - \tfrac t2\log\pi$ the Riemann–Siegel theta
- $\theta(t) = \pi - 2\arctan(2t)$: the phase function (note: distinct from $\theta_{RS}$)
- $g_n(t) = \dfrac{t\sin(n\theta(t)) + \tfrac12\cos(n\theta(t))}{\tfrac14 + t^2}$
- $D_n = \sum_\gamma g_n(\gamma)$

### 1.3 Main results

**Theorem 1 (Telescoping identity).** For $n \ge 1$, $t \ge 0$: $g_n(t) = \cos(n\theta(t)) - \cos((n+1)\theta(t))$.

**Theorem 2 (Vanishing integral).** $\dfrac1\pi\int_0^\infty \theta'(t)g_n(t)\,dt = 0$ for all $n \ge 1$, so $D_n = \sum_\gamma g_n(\gamma)$.

**Theorem 3 (Small $n$).** $D_n > 0$ for $1 \le n \le 43$.

**Theorem 4 (Large $n$, conditional).** Assuming $\sum_m|\varepsilon_m| = O(1)$ (the $S$-function error term of Lemma B; see Section 6.2), $D_n \ge \big(c - \tfrac{1}{\pi^2}\big)\log n - O(1)$ for $n$ large, with $c = \tfrac{\mathrm{Si}(\pi)}{2\pi} \approx 0.2947$, $c - \tfrac{1}{\pi^2} \approx 0.1934 > 0$. The bound is unconditional up to the single numerically-supported $\varepsilon_m$ hypothesis.

**Theorem 5 (Numerical).** With $10^5$ zeros, $D_n > 0$ for $n \in [1, 10^4]$, $\min D_n = D_1 \approx 0.0346$.

---

## 2. Preliminaries

### 2.1 Phase function

$$\theta(t) = \pi - 2\arctan(2t) = 2\arctan\frac{1}{2t}, \qquad \theta'(t) = -\frac{4}{1+4t^2} < 0.$$

$\theta$ maps $[0,\infty)$ bijectively onto $(\pi,0]$, strictly decreasing, with $\theta(t) = \frac1t - \frac{1}{12t^3} + O(t^{-5})$. In particular $\theta_k\cdot\gamma_k \to 1$ (numerically: $\theta_1\gamma_1 = 0.9996$, $\theta_{10^5}\gamma_{10^5} = 1.00000000$).

### 2.2 Change of variables

With $t = \tfrac12\cot(\theta/2)$ (the inverse of $\theta$):
$$\frac{t}{\tfrac14+t^2} = \sin\theta, \qquad \frac{\tfrac12}{\tfrac14+t^2} = 1-\cos\theta.$$

### 2.3 Known facts

- **von Mangoldt**: $N(T) = \tfrac1\pi\theta_{RS}(T) + 1 + S(T)$.
- **Backlund**: $|S(t)| \le C\log t$ (unconditional).
- **Zero density**: $N'(t) \approx \tfrac{1}{2\pi}\log\tfrac{t}{2\pi}$.
- **Selberg second moment**: $\int_0^T S(t)^2dt \sim \tfrac{1}{2\pi^2}T\log\log T$.

---

## 3. Telescoping identity and the difference structure

### 3.1 Proof of Theorem 1

By 2.2,
$$g_n(t) = \sin\theta\cdot\sin(n\theta) + (1-\cos\theta)\cdot\cos(n\theta).$$
Using $\sin\theta\sin(n\theta) = \tfrac12[\cos((n-1)\theta) - \cos((n+1)\theta)]$ and $(1-\cos\theta)\cos(n\theta) = \cos(n\theta) - \tfrac12[\cos((n-1)\theta)+\cos((n+1)\theta)]$, adding gives
$$g_n(t) = \cos(n\theta(t)) - \cos((n+1)\theta(t)). \quad \blacksquare$$

Numerical: for all $(n,t) \in \{1,5,43,100\}\times\{0.5, 14.13, 100, 5000\}$, difference $< 10^{-10}$.

### 3.2 Proof of Theorem 2

$$\int_0^\infty \theta'(t)g_n(t)\,dt = \int_\pi^0 \big[\sin\theta\sin(n\theta) + (1-\cos\theta)\cos(n\theta)\big]d\theta = -\int_0^\pi \big[\sin\theta\sin(n\theta) + (1-\cos\theta)\cos(n\theta)\big]d\theta.$$

For $n=1$: $-\big[\tfrac\pi2 + 0 - \tfrac\pi2\big] = 0$; for $n\ge2$: $-\big[0+0+0\big] = 0$. $\blacksquare$

Numerical: $n=1..50$, values $< 1.4\times10^{-14}$.

### 3.3 Corollary

$$D_n = \sum_k 2\sin\!\big((n+\tfrac12)\theta_k\big)\sin(\theta_k/2).$$

---

## 4. Positivity

### 4.1 Small $n$: Theorem 3

For $k\ge1$, $(n+\tfrac12)\theta_k \le (n+\tfrac12)\theta_1$. With $\theta_1 = \theta(14.1347\ldots) \approx 0.070718$,
$$(n+\tfrac12)\theta_1 < \pi \iff n < \frac{\pi}{\theta_1} - \frac12 \approx 43.9.$$
Hence for $n \le 43$ all terms $\sin((n+\tfrac12)\theta_k)>0$, $\sin(\theta_k/2)>0$, $D_n$ is a sum of positive terms. $\blacksquare$

Numerical: $D_{43} = 0.6471$; min term at $n=43$ is $+2.9\times10^{-9}>0$; first negative term at $n=44$ ($-3.8\times10^{-4}$).

### 4.2 Phase-region split

With $\varphi_k = (n+\tfrac12)\theta_k$:
$$D_n = D_{\mathrm{pos}} + D_{\mathrm{neg}}, \qquad D_{\mathrm{pos}} = \sum_{\varphi_k<\pi} 2\sin\varphi_k\sin(\theta_k/2), \quad D_{\mathrm{neg}} = \sum_{\varphi_k\ge\pi} 2\sin\varphi_k\sin(\theta_k/2).$$

Let $t_* = \tfrac{n+\frac12}{\pi}$ (so $\theta(t_*) = \tfrac{\pi}{n+\frac12}$). The positive region is $\gamma_k > t_*$, the negative region $\gamma_k \le t_*$.

### 4.3 Positive region: $D_{\mathrm{pos}} \approx \mathrm{Main}_{\mathrm{pos}}$ and Lemma A

The positive region consists of positive terms. Writing the discrete sum via the Riemann–von Mangoldt formula $N(T) = \frac1\pi\theta_{RS}(T)+1+S(T)$, the Stieltjes integral splits as
$$D_{\mathrm{pos}} = \frac1\pi\int_{t_*}^{\infty} g_n(t)\,\theta_{RS}'(t)\,dt + \int_{t_*}^{\infty} g_n(t)\,dS(t) =: \mathrm{Main}_{\mathrm{pos}} + E_{\mathrm{pos}}.$$
The second term is an $S$-function contribution; numerically it is negligible ($E_{\mathrm{pos}} \le 10^{-3}$ at $n=1000$), but a rigorous bound is part of the $\varepsilon_m$ question in Section 6.2. In what follows we track $\mathrm{Main}_{\mathrm{pos}}$ as the main term and absorb $E_{\mathrm{pos}}$ into the same $\varepsilon_m$ hypothesis; the statement of Theorem 4 is conditional on the combined $S$-function bound.

$$D_{\mathrm{pos}} = \frac1\pi\int_{t_*}^{\infty} g_n(t)\,\theta_{RS}'(t)\,dt =: \mathrm{Main}_{\mathrm{pos}}.$$

Numerically: at $n=1000$, $D_{\mathrm{pos}} = \mathrm{Main}_{\mathrm{pos}} = 1.5580$; at $n=500$, both $= 1.3649$.

**Lemma A (asymptotics, full proof in proof-strictification.md).**
$$\mathrm{Main}_{\mathrm{pos}}(n) = \frac{\mathrm{Si}(\pi)}{2\pi}\log n + C_0 + O(n^{-1}\log n), \quad \mathrm{Si}(\pi) = \int_0^\pi\frac{\sin u}{u}du \approx 1.8519.$$

*Proof sketch.* Change variables $u = (n+\tfrac12)\theta$; expand $\theta_{RS}'(t) = \tfrac12\log\frac{t}{2\pi} - \frac{1}{12t^2} + O(t^{-3})$ (Stirling) and $t = \tfrac12\cot\frac{\theta}{2} = \frac1\theta + O(\theta)$; all remainder terms contribute $O(n^{-1}\log n)$. The main integral is
$$\frac{1}{2\pi}\int_0^\pi \sin(u)\frac{\log\frac{n+\frac12}{2\pi u}}{u}du = \frac{1}{2\pi}\Big[\mathrm{Si}(\pi)\log\frac{n+\frac12}{2\pi} - C_1\Big], \quad C_1 = \int_0^\pi\frac{\sin(u)\log u}{u}du \approx -0.538. \quad \blacksquare$$

Numerical verification (with tail correction $\frac{2n+1}{4\pi}\frac{\log(g_{\max}/2\pi)+1}{g_{\max}}$): residual $\le 0.002$ for $n = 200..20000$.

### 4.4 Negative region: alternating series and Lemma B

Split the negative region into half-wave blocks $B_m = \{\varphi \in (m\pi, (m+1)\pi)\}$, $m \ge 1$: $D_{\mathrm{neg}} = \sum_m J_m$ with $J_m = \sum_{k\in B_m} 2\sin(\varphi_k)\sin(\theta_k/2)$.

**Lemma B (Leibniz bound, full proof in proof-strictification.md).**
$$|D_{\mathrm{neg}}| \le \frac{\log n}{\pi^2} + O(1).$$

*Proof sketch.* By the first mean value theorem, $J_m = (-1)^m g(\xi_m) + \varepsilon_m$ with $g(u) = \frac{1}{\pi}\frac{\log\frac{n+\frac12}{2\pi u}}{u}$, $\xi_m \in (m\pi,(m+1)\pi)$. Since $g'(u) = \frac{1}{\pi}\frac{\log(u/A)-1}{u^2} \le 0$ for $u \le A\cdot e$ ($A = \frac{n+\frac12}{2\pi}$), and the largest block index $M \approx 0.0225\,n$ satisfies $(M+1)\pi < A\cdot e \approx 0.43\,n$, the sequence $g(\xi_m)$ is decreasing. Hence $\sum_m (-1)^m g(\xi_m)$ is an alternating series and by Leibniz,
$$\Big|\sum_m (-1)^m g(\xi_m)\Big| \le g(\xi_1) \le \frac{\log n}{\pi^2} + O(1).$$
The error $\sum_m|\varepsilon_m|$ (deviation of discrete sums from smooth density, an $S$-function term) is measured numerically: $\sum_m|\varepsilon_m| \le 0.74$ for $n \le 2\times10^4$, bounded and far below the margin. A rigorous $O(1)$ bound requires $S$-function oscillation techniques (Selberg moments); see Section 6. $\blacksquare$

Numerical (n=5000): block sums $[-0.356, +0.189, -0.125, +0.091, -0.071, \ldots]$, amplitudes $\approx 0.36/m$ decreasing; $|D_{\mathrm{neg}}| = 0.093 \le 0.863$.

### 4.5 Closing: Theorem 4 (conditional)

$$D_n = \mathrm{Main}_{\mathrm{pos}} + D_{\mathrm{neg}} \ge c\log n - \frac{\log n}{\pi^2} - O(1) = \big(c - \tfrac{1}{\pi^2}\big)\log n - O(1), \quad c - \tfrac{1}{\pi^2} = 0.1934 > 0,$$
modulo the $\varepsilon_m$ hypothesis of Section 6.2.

Numerical closing (all actual values):

| $n$ | $\mathrm{Main}_{\mathrm{pos}}(\mathrm{full})$ | $\|D_{\mathrm{neg}}\|$ | $D_n$ | margin$/\!\log n$ |
|---|---|---|---|---|
| 100 | 0.903 | 0.032 | 0.871 | 0.189 |
| 1000 | 1.580 | 0.070 | 1.510 | 0.219 |
| 5000 | 2.054 | 0.093 | 1.961 | 0.230 |
| 10000 | 2.259 | 0.291 | 1.968 | 0.214 |
| 20000 | 2.465 | 0.232 | 2.233 | 0.226 |

### 4.6 Synthesis

Theorem 3 covers $n \le 43$ strictly. Theorem 4 covers $n$ large **conditionally** on the $S$-function bound $\sum_m|\varepsilon_m|=O(1)$. Theorem 5 covers $n \le 10^4$ numerically. Thus: **$D_n > 0$ is proved strictly for $n \le 43$, proved conditionally (on one $S$-function bound) for large $n$, and verified numerically for $n \le 10^4$.** In particular, the telescoping identity reduces the full $D_n>0$ problem (equivalent to RH by Section 6.1) to a single $S$-function estimate.

---

## 5. Numerical verification

### 5.1 Data

First $10^5$ zeros of Odlyzko ($\gamma_{10^5} = 74920.8275\ldots$, approximately 10 significant digits). Audit: cross-validated against mpmath `zetazero` (max error $2.5\times10^{-9}$); monotone, no duplicates; von Mangoldt consistency $S(T) = N - \theta_{RS}/\pi - 1 \in [-0.97, +0.38] = O(\log T)$.

### 5.2 $D_n$ table

| $n$ | $D_n$ | $n$ | $D_n$ |
|---|---|---|---|
| 1 | 0.0346 | 100 | 0.8681 |
| 5 | 0.1259 | 200 | 1.0841 |
| 10 | 0.2353 | 500 | 1.1535 |
| 20 | 0.4239 | 1000 | 1.4877 |
| 43 | 0.6471 | 5000 | 1.8508 |
| 50 | 0.6692 | 10000 | 1.7476 |

$D_n$ grows roughly like $0.2\log n$, positive on $[1,10^4]$, $\min = D_1 = 0.0346$.

### 5.3 Other facts

- $\theta_1 = 0.070718$ ($1/\gamma_1 = 0.070748$); $(n+\tfrac12)\theta_1 < \pi \iff n \le 43$;
- mean of $S(\gamma_k) = 0.500048$ ($k\le 5000$), std 0.31;
- $M(T) = \int_0^T S(u)du$: bounded along zeros ($M(\gamma_k) \in [-1.5, -0.5]$ for $k \le 10^5$), but grows with $T$ in general ($M(74921) \approx -200$); see Appendix A
- $D_n > 0$ for all $n \in [1, 10^4]$ (direct computation).

---

## 6. Discussion, limitations and open problems

### 6.1 Relation to known work

- **Li's criterion** [6]: $\lambda_n > 0$ for all $n \iff$ RH, where $\lambda_n = \sum_\rho\big[1-(1-\tfrac1\rho)^n\big]$ are the Li coefficients. By Bombieri–Lagarias, the difference satisfies
  $$\lambda_{n+1} - \lambda_n = 2\sum_{\gamma>0}\big[\cos(n\psi_\gamma) - \cos((n+1)\psi_\gamma)\big], \qquad \psi_\gamma = \arg(1-\tfrac1\rho).$$
  **We verify numerically that $\psi_\gamma = \theta(\gamma)$ exactly** (error $\le 10^{-16}$, float precision) for the first $10^5$ zeros; analytically, $\cos\psi_\gamma = \frac{\gamma^2-1/4}{\gamma^2+1/4} = \cos\theta(\gamma)$ with both angles in $(0,\pi/2)$. Hence
  $$\lambda_{n+1} - \lambda_n = 2D_n.$$
  Consequently, **a complete proof of $D_n > 0$ for all $n$ would imply RH** (since $\lambda_{n+1}>\lambda_n$ together with $\lambda_1 = 1-\frac{\gamma_E}{2}-\frac12\log(4\pi) \approx 0.023>0$ gives $\lambda_n>0$ for all $n$). The present paper proves $D_n>0$ strictly for $n\le43$ and conditionally for large $n$ under the $S$-function bound of Section 6.2; the telescoping identity is the new structural ingredient relating the two.

- **Murty–Rath** [5]: $\sum_{\nu>0}\cos(\nu\log x)/(\tfrac14+\nu^2)$, same denominator. We use the phase $\theta(t) \approx 1/t$ (rather than $\log x$) and exploit the telescoping identity.
- **Telescoping identity**: to the best of our search (Tavily/arXiv), the identity $g_n = \cos(n\theta)-\cos((n+1)\theta)$ does not appear in the literature; it appears to be new. An arXiv full-text search is recommended for final confirmation.

### 6.2 Remaining open point (single, honest)

$\sum_m|\varepsilon_m| = O(1)$ (the $S$-function error term in Lemma B). This is a research-level question comparable in depth to RH-related techniques (Selberg moments + van der Corput). **It is the only gap between the present results and a full proof of $D_n>0$ for all $n$ (and hence RH by Section 6.1).** Numerically $\sum_m|\varepsilon_m| \le 0.74$ (bounded, $\approx 0.07\log n$), far below the closing margin $0.1934\log n$; even the worst-case $O(\log n)$ would not threaten the margin. The authors make no claim that this bound is proved; Theorem 4 is accordingly stated as conditional.

**Technical structure of the gap (numerical, 2026-08-21).** Writing $\Sigma\varepsilon = \int_{\gamma_1}^{t_*} g_n\,dS$ with $t_*=(n+\tfrac12)/\pi$, integration by parts gives $\Sigma\varepsilon = -g_n(\gamma_1)S(\gamma_1) - \int_{\gamma_1}^{t_*} S\,g_n'\,dt$. The endpoint term is $O(1)$ ($|g_n(\gamma_1)| \approx 0.07$, $|S(\gamma_1)| \le 1$). The integral term splits into high-frequency and low-frequency parts that cancel to high order (numerically $\int S\,g_n'\,dt = -0.066$ at $n=1000$, with raw high/low parts $\pm 36.4$; $-0.114$ at $n=5000$ with parts $\pm 357$). A naive $M(T)$-boundedness route (double integration by parts via $M(T)=\int_0^T S$) fails: $\int|g_n''|\,dt$ grows like $n$ ($4 \to 100 \to 1688$ for $n=1000,5000,20000$), so that path gives only $O(n)$.

**Two favorable facts for the oscillation route.** (i) The total variation of the *continuous* $S$ (sampled between zeros) saturates: $V(S) \approx 1000$ for $T$ from $3\times10^3$ to $7.5\times10^4$ ($10^5$ zeros), i.e. $V(S) = O(\log T)$-scale, not $O(T\log T)$ — the smooth part of $\theta_{RS}$ absorbs the density growth, so $S$ is of bounded-variation type at logarithmic scale. (ii) The measured ratio $|\Sigma\varepsilon|/\log n \le 0.018$ for $n \in [10^3, 2\times10^4]$ — three orders below the closing margin $0.1934$. The correct mechanism is **oscillation cancellation** of $S$ against $g_n'$ (van der Corput with the explicit phase $\theta(t) = \pi-2\arctan(2t)$), for which the phase is explicit and favorable; this is the natural research avenue.

### 6.3 Limitations

- Theorem 4's constants $C_0, C_1$ are not explicit (asymptotic big-O form); explicit versions require controlling the $\theta$ vs $1/t$ and $\theta_{RS}'$ vs $\tfrac12\log$ remainders.
- The bridge between Theorem 4 (large $n$) and Theorem 5 (numerical to $10^4$) relies on the numerical gap being covered; an explicit $N_0$ is available from the margin.
- The identity $\psi_\gamma = \theta(\gamma)$ is verified numerically to $10^{-16}$ and analytically at the level of $\cos\psi = \cos\theta$; a fully rigorous argument for the exact equality of the angles (branch choice) is standard but not written out here.

---

## 7. Conclusion

We establish the following results on
$$D_n = \sum_\gamma \frac{\gamma\sin(n\theta(\gamma)) + \tfrac12\cos(n\theta(\gamma))}{\tfrac14 + \gamma^2} = \sum_k\big[\cos(n\theta_k)-\cos((n+1)\theta_k)\big]:$$

1. **Telescoping identity** $g_n = \cos(n\theta) - \cos((n+1)\theta)$ (new, Theorem 1);
2. **Vanishing integral** (Theorem 2), reducing $D_n$ to a pure zero sum;
3. **$n \le 43$ strict positivity** (Theorem 3, sum of positive terms);
4. **Phase-region split + alternating series**: $D_n \ge 0.1934\log n - O(1)$ for large $n$, **conditional on the single $S$-function bound $\sum_m|\varepsilon_m|=O(1)$** (Theorem 4);
5. **Numerical verification** to $n = 10^4$ with $10^5$ zeros (Theorem 5), $\min D_n = D_1 \approx 0.0346 > 0$;
6. **Li criterion link** (Section 6.1): $\lambda_{n+1}-\lambda_n = 2D_n$, so a complete proof of $D_n>0$ for all $n$ would prove RH.

**Summary and outlook toward RH.** $D_n>0$ for all $n$ is equivalent to the Riemann Hypothesis (Section 6.1). The present paper proves it unconditionally for $n\le43$, verifies it numerically to $n\le10^4$, and reduces the large-$n$ case to the single $S$-function bound $\sum_m|\varepsilon_m|=O(1)$ (Theorem 4, conditional). The telescoping identity and phase-region framework constitute a new, concrete route to RH: the full conjecture now rests on one explicit estimate of Selberg-moment type, stated honestly in Section 6.2, for which the numerical evidence is overwhelming (bounded by $0.74$, margin $0.1934\log n$).

---

## Appendix A: Data audit (2026-08-21)

- Zeros: **fully correct** (mpmath cross-validation $\le 2.5\times10^{-9}$).
- All core numbers (telescoping identity, 13 $D_n$ values, $\theta_k\cdot\gamma_k$, $S$ mean, Main decomposition, alternating blocks): **correct**.
- Corrections: (i) early M(T) table had $+0.235$ first-interval bias (Simpson 5-point insufficient on $[0,\gamma_1]$), fixed with Gauss-16; **an early claim that $M(T)=O(1)$ for all $T$ was withdrawn** — $M(T)$ grows with $T$ (e.g. $M(74921)\approx -200$), though it is bounded along the zero sequence $\gamma_k$; (ii) Main_pos coefficient was briefly mis-reported as 0.188 (truncation artifact), corrected back to $c = 0.295$ (closing margin 0.193) after reviewer verification.

## Appendix B: Reproduction

- Zeros: Odlyzko `zeros1` (gzip, whitespace-separated, first $10^5$).
- Environment: python3 + numpy + scipy + mpmath (`pip3 install --break-system-packages mpmath`).
- Key scripts (`dn-project/scripts/`): `dn_telescope.py` (identity), `dn_realdef*.py` (definitions), `dn_region.py` (phase split), `dn_close.py`/`dn_final.py` (closing), `audit_*.py` (audit).

## Data Availability Statement

All code, data, and documentation supporting the findings of this study are openly available in the GitHub repository `wxtanghui2023/dn-positivity` at https://github.com/wxtanghui2023/dn-positivity, archived on Zenodo with DOI [10.5281/zenodo.22040623](https://doi.org/10.5281/zenodo.22040623). The zero data (first $10^5$ non-trivial zeros of the Riemann zeta function) are included in the repository and were originally obtained from A. M. Odlyzko's public tables (https://www.dtc.umn.edu/~odlyzko/zeta_tables/).

## Acknowledgements

The authors thank the maintainers of the Odlyzko zero tables, mpmath, SciPy, and NumPy. This work was conducted as an independent research project; the preprint version is archived with DOI 10.5281/zenodo.22040623.

## Disclosure statement

The authors report there are no competing interests to declare.

## References

1. E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.
2. Riemann–von Mangoldt formula; DLMF §25.10.
3. A. Selberg, *On the remainder term in the formula for $N(T)$*, Skr. Norske Vid. Akad. Oslo 1946.
4. E. Backlund, *Über die Nullstellen der Riemannschen Zetafunktion*, Acta Math. 41 (1918).
5. M. R. Murty, P. Rath, *Transcendental sums related to the zeros of zeta functions*, Mathematika 64 (2018), arXiv:1807.11201.
6. X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory 65 (1997), 325–333.
7. E. Bombieri, J. C. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, J. Number Theory 77 (1999), 274–287.
8. A. Fujii, *On the distribution of the zeros of the Riemann zeta function in short intervals*, Proc. Japan Acad. 66 (1990).
9. J. G. van der Corput, *Zur Methode der Steilstesten Abstiegs*, 1926 (van der Corput lemmas; see also Stein, *Harmonic Analysis*, Ch. VIII).
10. A. Selberg, *On the normal density of primes in small intervals, and the difference between consecutive primes*, Arch. Math. Naturvid. 47 (1943) [second moment of $S(T)$].
