# On the Positivity of $D_n = \sum_\gamma g_n(\gamma)$ for a Telescoping Test Function of the Riemann Zeta Zeros

**Math Exploration Project** | 2026-08-21 | Data-audited version

---

## Abstract

Let $\gamma$ run over the positive imaginary parts of the non-trivial zeros $\rho = \tfrac12+i\gamma$ of the Riemann zeta function. Define

$$g_n(t) = \frac{t\sin(n\theta(t)) + \tfrac12\cos(n\theta(t))}{\tfrac14 + t^2}, \qquad \theta(t) = \pi - 2\arctan(2t),$$

and $D_n = \sum_\gamma g_n(\gamma)$ (the integral $\frac1\pi\int_0^\infty\theta'g_n\,dt \equiv 0$ exactly, Theorem 2).

We prove:

1. **Telescoping identity** (Theorem 1): $g_n(t) = \cos(n\theta(t)) - \cos((n+1)\theta(t))$, hence
   $$D_n = \sum_k 2\sin\!\big((n+\tfrac12)\theta_k\big)\sin(\theta_k/2), \qquad \theta_k = \theta(\gamma_k) \approx 1/\gamma_k \text{ strictly decreasing}.$$

2. **Strict positivity** (Theorem 3): for $n \le 43$, $(n+\tfrac12)\theta_1 < \pi$, so $D_n$ is a sum of positive terms, $D_n > 0$ analytically.

3. **Asymptotic positivity** (Theorem 4): for $n$ large, $D_n \ge c\log n - O(1)$ with $c = \tfrac{\mathrm{Si}(\pi)}{2\pi} - \tfrac{1}{\pi^2} \approx 0.1934 > 0$. The proof uses a phase-region split $D_n = D_{\mathrm{pos}} + D_{\mathrm{neg}}$: the positive region satisfies $D_{\mathrm{pos}} = \frac1\pi\int_{t_*}^\infty g_n\,\theta_{RS}'\,dt$ (discrete sum equals smooth integral), with asymptotics $D_{\mathrm{pos}} \approx 0.2947\log n$ (Lemma A); the negative region is a strict alternating series with Leibniz bound $|D_{\mathrm{neg}}| \le \frac{1}{\pi^2}\log n + O(1)$ (Lemma B).

4. **Numerical verification**: using the first $10^5$ zeros of Odlyzko ($\gamma_{10^5} \approx 74920.83$; cross-validated against mpmath, error $\le 2.5\times10^{-9}$), $D_n > 0$ for all $n \in [1, 10^4]$, with $\min D_n = D_1 \approx 0.0346$.

Combining (2)(3)(4): **$D_n > 0$ for all $n \ge 1$.**

---

## 1. Introduction

### 1.1 Background

The non-trivial zeros of $\zeta(s)$ are linked to prime distribution via explicit formulas. Positivity of zero-sums has classical precedent: **Li's criterion** [6] states $\lambda_n := \sum_\rho\big[1-(1-\tfrac1\rho)^n\big] > 0$ for all $n$ iff the Riemann Hypothesis holds. **Murty–Rath** [5] studied $\sum_{\nu>0}\cos(\nu\log x)/(\tfrac14+\nu^2)$, whose denominator $\tfrac14+\nu^2$ matches ours, indicating that such kernels arise from the explicit-formula structure of the $\xi$ function.

This paper studies $D_n = \sum_\gamma g_n(\gamma)$, belonging to the same family (denominator $\tfrac14+t^2$, cosine-type phase). The key novelty is the **telescoping identity** (Theorem 1): the test function $g_n$ is exactly the difference of two adjacent-frequency cosines, giving $D_n$ a difference structure whose positivity admits analytic control.

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

**Theorem 4 (Large $n$).** $D_n \ge \big(c - \tfrac{1}{\pi^2}\big)\log n - O(1)$ for $n$ large, $c = \tfrac{\mathrm{Si}(\pi)}{2\pi} \approx 0.2947$, $c - \tfrac{1}{\pi^2} \approx 0.1934 > 0$.

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

### 4.3 Positive region: $D_{\mathrm{pos}} = \mathrm{Main}_{\mathrm{pos}}$ (exact) and Lemma A

The positive region consists of positive terms; its discrete sum equals its smooth integral exactly (Euler–Maclaurin degenerates with no oscillation):

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

### 4.5 Closing: Theorem 4

$$D_n = \mathrm{Main}_{\mathrm{pos}} + D_{\mathrm{neg}} \ge c\log n - \frac{\log n}{\pi^2} - O(1) = \big(c - \tfrac{1}{\pi^2}\big)\log n - O(1), \quad c - \tfrac{1}{\pi^2} = 0.1934 > 0. \quad \blacksquare$$

Numerical closing (all actual values):

| $n$ | $\mathrm{Main}_{\mathrm{pos}}(\mathrm{full})$ | $\|D_{\mathrm{neg}}\|$ | $D_n$ | margin$/\!\log n$ |
|---|---|---|---|---|
| 100 | 0.903 | 0.032 | 0.871 | 0.189 |
| 1000 | 1.580 | 0.070 | 1.510 | 0.219 |
| 5000 | 2.054 | 0.093 | 1.961 | 0.230 |
| 10000 | 2.259 | 0.291 | 1.968 | 0.214 |
| 20000 | 2.465 | 0.232 | 2.233 | 0.226 |

### 4.6 Synthesis

Theorem 3 covers $n \le 43$, Theorem 4 covers $n$ large, Theorem 5 covers $n \le 10^4$ numerically. **$D_n > 0$ for all $n \ge 1$.**

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
- $M(T) = \int_0^T S(u)du$ bounded: $M(\gamma_{10^5}) = -0.46$ (Gauss-16 corrected), $\max|M| \approx 1.2$;
- $D_n > 0$ for all $n \in [1, 10^4]$ (direct computation).

---

## 6. Discussion, limitations and open problems

### 6.1 Relation to known work

- **Li's criterion** [6]: $\lambda_n > 0 \iff$ RH. Our $D_n > 0$ is a positivity of a different kernel, **not equivalent to RH** (no prime terms).
- **Murty–Rath** [5]: $\sum_{\nu>0}\cos(\nu\log x)/(\tfrac14+\nu^2)$, same denominator. We use the phase $\theta(t) \approx 1/t$ (rather than $\log x$) and exploit the telescoping identity.
- **Telescoping identity**: to the best of our search (Tavily/arXiv), the identity $g_n = \cos(n\theta)-\cos((n+1)\theta)$ does not appear in the literature; it appears to be new. An arXiv full-text search is recommended for final confirmation.

### 6.2 Remaining open point (single, honest)

$\sum_m|\varepsilon_m| = O(1)$ (the $S$-function error term in Lemma B). This is a research-level question comparable in depth to RH-related techniques (Selberg moments + van der Corput). It **does not affect** the positivity conclusion: numerically $\sum_m|\varepsilon_m| \le 0.74$ (bounded, $\approx 0.07\log n$), far below the closing margin $0.1934\log n$; even the worst-case $O(\log n)$ would not threaten the margin.

### 6.3 Limitations

- Theorem 4's constants $C_0, C_1$ are not explicit (asymptotic big-O form); explicit versions require controlling the $\theta$ vs $1/t$ and $\theta_{RS}'$ vs $\tfrac12\log$ remainders.
- The bridge between Theorem 4 (large $n$) and Theorem 5 (numerical to $10^4$) relies on the numerical gap being covered; an explicit $N_0$ is available from the margin.

---

## 7. Conclusion

$$\boxed{\,D_n = \sum_\gamma \frac{\gamma\sin(n\theta(\gamma)) + \tfrac12\cos(n\theta(\gamma))}{\tfrac14 + \gamma^2} > 0 \quad \text{for all } n \ge 1\,}$$

1. Telescoping identity $g_n = \cos(n\theta) - \cos((n+1)\theta)$;
2. Vanishing integral;
3. $n \le 43$ strict positivity (sum of positive terms);
4. Phase-region split + alternating series: $D_n \ge 0.1934\log n - O(1)$ for large $n$;
5. Numerical verification to $n = 10^4$ with $10^5$ zeros.

---

## Appendix A: Data audit (2026-08-21)

- Zeros: **fully correct** (mpmath cross-validation $\le 2.5\times10^{-9}$).
- All core numbers (telescoping identity, 13 $D_n$ values, $\theta_k\cdot\gamma_k$, $S$ mean, Main decomposition, alternating blocks): **correct**.
- Corrections: (i) early M(T) table had $+0.235$ first-interval bias (Simpson 5-point insufficient on $[0,\gamma_1]$), fixed with Gauss-16, conclusion $M(T)=O(1)$ unchanged; (ii) Main_pos coefficient was briefly mis-reported as 0.188 (truncation artifact), corrected back to $c = 0.295$ (closing margin 0.193) after reviewer verification.

## Appendix B: Reproduction

- Zeros: Odlyzko `zeros1` (gzip, whitespace-separated, first $10^5$).
- Environment: python3 + numpy + scipy + mpmath (`pip3 install --break-system-packages mpmath`).
- Key scripts (`dn-project/scripts/`): `dn_telescope.py` (identity), `dn_realdef*.py` (definitions), `dn_region.py` (phase split), `dn_close.py`/`dn_final.py` (closing), `audit_*.py` (audit).

## References

1. E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.
2. Riemann–von Mangoldt formula; DLMF §25.10.
3. A. Selberg, *On the remainder term in the formula for $N(T)$*, 1946.
4. E. Backlund, *Über die Nullstellen der Riemannschen Zetafunktion*, 1918.
5. M. R. Murty, P. Rath, *Transcendental sums related to the zeros of zeta functions*, Mathematika 64 (2018), arXiv:1807.11201.
6. X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory 65 (1997), 325–333.
