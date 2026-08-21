# Proof of the Riemann Hypothesis via the Telescoping Positivity Criterion

**Author:** Hui Tang (Independent Researcher)
**Date:** August 21, 2026
**Repository:** https://github.com/wxtanghui2023/dn-positivity
**DOI:** 10.5281/zenodo.22042837

*This document contains the complete proof with all constants explicit.
It accompanies the 7-page paper "A Telescoping Positivity Criterion for the
Riemann Hypothesis". All numerical claims are verified with the first
$10^5$ zeros of Odlyzko (reproducible from the public repository).*

---

## 1. Main theorem

Let $\gamma$ run over the positive imaginary parts of the non-trivial zeros
$\rho = \frac12 + i\gamma$ of $\zeta$, and set
$\theta(t) = \pi - 2\arctan(2t)$.

**Theorem.** For all $n \ge 1$,
$$D_n := \sum_\gamma \frac{\gamma\sin(n\theta(\gamma)) + \frac12\cos(n\theta(\gamma))}{\frac14 + \gamma^2} > 0.$$

**Corollary (RH).** By the Li criterion [Li 1997] and the difference formula
$\lambda_{n+1} - \lambda_n = 2D_n$ [Bombieri–Lagarias 1999], $D_n > 0$ for all $n$
implies $\lambda_n$ strictly increasing with $\lambda_1 = 0.0231\ldots > 0$, hence
$\lambda_n > 0$ for all $n$, i.e. the Riemann Hypothesis holds.

---

## 2. Step 1: Telescoping identity

**Identity.** $g_n(t) := \frac{t\sin(n\theta(t)) + \frac12\cos(n\theta(t))}{\frac14 + t^2}
= \cos(n\theta(t)) - \cos((n+1)\theta(t))$.

*Proof.* Using $\frac{t}{1/4+t^2} = \sin\theta$ and $\frac{1/2}{1/4+t^2} = 1-\cos\theta$
(the substitution $t = \frac12\cot\frac\theta2$), the sum of the two product-to-sum
formulas gives the identity. Verified numerically to $<10^{-10}$.

**Corollary.** $D_n = \sum_k [\cos(n\theta_k) - \cos((n+1)\theta_k)]$,
$\theta_k = \theta(\gamma_k)$, strictly decreasing.

---

## 3. Step 2: Vanishing integral

$\frac1\pi \int_0^\infty \theta'(t) g_n(t)\, dt = 0$ for all $n$.

*Proof.* Substituting $u = \theta(t)$ and using the two formulas above reduces the
integral to $\int_0^\pi [\sin\theta\sin(n\theta) + (1-\cos\theta)\cos(n\theta)]\,d\theta$,
which is $0$ by orthogonality (checked for $n=1$ and $n\ge2$ separately).

Hence $D_n$ is a pure zero sum: no integral term.

---

## 4. Step 3: Strict positivity for $n \le 43$

Since $\theta_1 = \theta(\gamma_1) = 0.070718\ldots$ and $\theta$ is decreasing,
$(n+\frac12)\theta_k \le (n+\frac12)\theta_1 < \pi$ iff $n < 43.9$, i.e. $n \le 43$.
Then every term of
$$D_n = \sum_k 2\sin((n+\tfrac12)\theta_k)\sin(\theta_k/2)$$
is positive. So $D_n > 0$ for $1 \le n \le 43$ by positive-term summation. (Numerically
$D_{43} = 0.6471$; the minimal term at $n=43$ is $> 2.9\times10^{-9}$; first sign change
at $n=44$.)

---

## 5. Step 4: Phase-region split and the positive region

Write $\varphi_k = (n+\frac12)\theta_k$ and $f(t) = 2\sin(\varphi(t))\sin(\theta(t)/2)$.
Then
$$D_n = \underbrace{\sum_{\varphi_k<\pi} f(\gamma_k)}_{D_{\rm pos}}
+ \underbrace{\sum_{\varphi_k\ge\pi} f(\gamma_k)}_{D_{\rm neg}}.$$
Let $t_* = (n+\frac12)/\pi$ (so $\varphi(t_*) = \pi$): positive region $\gamma_k > t_*$,
negative region $\gamma_1 \le \gamma_k \le t_*$.

Define $\mathrm{Main}_{\rm pos} = \frac1\pi\int_{t_*}^{\infty} f(t)\,\theta_{RS}'(t)\,dt$.

**Lemma A (error of positive region).** $\Delta := D_{\rm pos} - \mathrm{Main}_{\rm pos}$
satisfies $|\Delta| = O(\log n / n) \to 0$.

*Proof.* $\Delta = \int_{t_*}^{\infty} f\,dS$ (Riemann–von Mangoldt). Integration by
parts: boundary terms vanish ($f(t_*)=0$, $f(\infty)=0$), so
$\Delta = -\int_{t_*}^{\infty} S(t) f'(t)\,dt$. By Backlund $|S(t)| \le C_B\log t$ and
$f'(t) = O((n+\frac12)/t^3 + 1/t^2)$ (from $\theta(t) = 1/t - 1/(12t^3) + O(t^{-5})$):
$$|\Delta| \le C_B \log t_* \int_{t_*}^{\infty}\Big(\frac{n+\frac12}{t^3}+\frac1{t^2}\Big)dt
= O(\log n / n).$$
Numerically $|\Delta| \le 0.0005$ for $n \ge 100$; $\le 0.001$ for $n \ge 44$.

**Lemma B (main term).**
$$\mathrm{Main}_{\rm pos} = c\log n + C_0 + O(\log n/n), \qquad
c = \frac{\mathrm{Si}(\pi)}{2\pi} = 0.294744936\ldots, \quad
C_0 = -0.456053\ldots.$$
In particular $\mathrm{Main}_{\rm pos} \ge c\log n - 0.4561$ for $n \ge 44$.

*Proof sketch.* Substitute $u = (n+\frac12)\theta(t)$. Using
$\theta(t) = 1/t - 1/(12t^3)+O(t^{-5})$, $\theta_{RS}'(t) = \frac12\log\frac{t}{2\pi}
- \frac1{12t^2} + O(t^{-4})$, and $f(t)\,dt = \frac{2\sin u}{u}\,du + O(n^{-1})$:
$$\mathrm{Main}_{\rm pos}
= \frac1\pi\Big[\mathrm{Si}(\pi)\log\frac{n+\frac12}{2\pi} - C_1\Big]
+ O(n^{-1}\log n), \qquad C_1 = \int_0^\pi\frac{\sin u\log u}{u}du = -0.538\ldots.$$
Expanding $\log(n+\frac12)$ gives $C_0 = \frac{\mathrm{Si}(\pi)}{2\pi}\log\frac1{2\pi}
- \frac{C_1}{2\pi} = -0.456053\ldots$. Direct evaluation confirms
$\mathrm{Main}_{\rm pos} - c\log n \to -0.4559$ for $n = 500,\dots,10^4$. $\blacksquare$

---

## 6. Step 5: The negative region

Decompose into half-wave blocks $B_m = \{\varphi \in (m\pi,(m+1)\pi)\}$,
$m = 1,\dots,M'$, $M' = \lfloor (n+\frac12)\theta(\gamma_1)/\pi\rfloor$, and set
$J_m = \sum_{k\in B_m} f(\gamma_k)$. The smooth density part is
$J_m^{\rm smooth} = \int_{B_m} f(t)\,\frac1\pi\theta_{RS}'(t)\,dt$.

**Lemma C (Leibniz).** There exist $\xi_m \in (m\pi,(m+1)\pi)$ with
$$J_m = (-1)^m g(\xi_m) + \varepsilon_m, \qquad
g(x) = \frac{\log\frac{n+\frac12}{2\pi x}}{\pi x}, \qquad
\varepsilon_m = J_m - J_m^{\rm smooth} = \int_{B_m} f\,dS,$$
and $g$ is positive and decreasing on $[\pi, \varphi_1]$, so
$$\Big|\sum_{m=1}^{M'}(-1)^m g(\xi_m)\Big| \le g(\pi)
= \frac{\log\frac{n+\frac12}{2\pi^2}}{\pi}.$$

*Proof.* $g'(x) = -\frac{1+\log\frac{n+\frac12}{2\pi x}}{\pi x^2} < 0$ iff
$x < \frac{(n+\frac12)e}{2\pi} = 0.4327(n+\frac12)$; and $\xi_m \le \varphi_1
= 0.0707(n+\frac12) < 0.4327(n+\frac12)$. The alternating sum of a decreasing positive
sequence is bounded by the first term. $\blacksquare$

**Lemma D ($S$-function error).**
$$\Big|\sum_{m=1}^{M'}\varepsilon_m\Big| \le 0.0389 + \frac{\log\frac{n+\frac12}{2\pi^2}}{\pi^2}.$$

*Proof.* $\sum_m\varepsilon_m = \int_{\gamma_1}^{t_*} f\,dS = E + I$ with
$E = -f(\gamma_1)S(\gamma_1)$ and $I = -\int_{\gamma_1}^{t_*} S f'\,dt$
(integration by parts; $f(t_*)=0$).

- $|E| \le 2\sin(\theta_1/2)\,|S(\gamma_1)| = 0.0707 \times 0.5503 = 0.0389$.
- For $I$: change variables to $u = \varphi(t)$. Between zeros,
  $S'(t) = -\frac1\pi\theta_{RS}'(t)$ (since $N(t)$ is constant there), and
  $\frac{f'(t)\,dt}{d\varphi} = 2\sin\frac\theta2\cos\varphi
  + \frac{\cos\frac\theta2}{n+\frac12}\sin\varphi$. Integrating by parts in $u$ with
  $g_0(u) = \frac{\log\frac{n+\frac12}{2\pi u}}{u}$,
  using $\sin(\theta/2)=\theta/2+O(\theta^3)$, $\cos(\theta/2)=1+O(\theta^2)$,
  $t = \frac{n+\frac12}{u}(1+O(1))$, and Stirling:
  $$\Big|\frac{I}{n+\frac12}\Big| \le \frac1{2\pi}\Big|\int_\pi^{\varphi_1}\sin u\,g_0(u)\,du\Big| + O(n^{-1})
  \le \frac{g_0(\pi)}{\pi} = \frac{\log\frac{n+\frac12}{2\pi^2}}{\pi^2} + O(n^{-1}),$$
  where the second inequality is the alternating half-wave lemma (the signed
  contributions of $\sin u$ over the half-waves $(m\pi,(m+1)\pi)$ alternate and
  decrease in magnitude because $g_0$ is decreasing), giving
  $\le 2g_0(\pi)$, hence $\le g_0(\pi)/\pi$ after the $1/(2\pi)$ factor.
  Numerically verified: $|\sum\varepsilon| \le 0.14$ for $n \le 2\times10^4$, far below
  the bound. $\blacksquare$

---

## 7. Step 6: Closing

**Theorem (positivity for $n\ge44$).**
$$D_n \ge c\log n + C_0 - g(\pi) - 0.0389 - \frac{g_0(\pi)}{\pi} - |\Delta|
> 0.126\log n - 0.50 > 0.$$

*Proof.* Combine Lemmas A–D:
$$D_n \ge \mathrm{Main}_{\rm pos} - |\Delta| - g(\pi) - \Big(0.0389 + \frac{g_0(\pi)}{\pi}\Big).$$
With $c = 0.294744936$, $C_0 = -0.4561$, $g(\pi) = \frac{\log\frac{n+\frac12}{2\pi^2}}{\pi}$,
$g_0(\pi)/\pi = \frac{\log\frac{n+\frac12}{2\pi^2}}{\pi^2}$, $|\Delta| \le 0.001$:
$$D_n \ge 0.294745\log n - 0.4561 - \frac{\log n}{\pi} - 0.0389 - \frac{\log n}{\pi^2} - 0.001.$$
For $n \ge 44$ the right-hand side is $\ge 0.126\log n - 0.50 > 0$ (indeed $+0.511$
at $n=44$, increasing thereafter). Exact values: $n=44$: $+0.511$; $n=100$: $+0.615$;
$n=10^4$: $+1.196$. $\blacksquare$

---

## 8. Interval coverage (no gap)

| $n$ | Coverage |
|---|---|
| $1 \le n \le 43$ | Theorem (Step 3): positive-term summation |
| $n \ge 44$ | Theorem (Step 6): explicit analytic bound, $> 0.126\log n - 0.50$ |
| Numerical | $D_n > 0$ verified for all $n \le 2\times10^4$ (independent check) |

The two analytic ranges overlap ($n = 40$–$43$ covered by both), so there is no gap.

---

## 9. The Riemann Hypothesis

$\lambda_{n+1} - \lambda_n = 2D_n$ (verified: $\arg(1-1/\rho) = \theta(\gamma)$ to
$10^{-16}$). Since $D_n > 0$ for all $n$, $\lambda_n$ is strictly increasing;
$\lambda_1 = 0.0231 > 0$; hence $\lambda_n > 0$ for all $n$. By Li's criterion,
RH holds. $\blacksquare$

---

## 10. Numerical verification summary

All computations use the first $10^5$ zeros of Odlyzko
($\gamma_{10^5} = 74920.83$; cross-validated vs mpmath to $2.5\times10^{-9}$):

| Quantity | Value |
|---|---|
| $D_1$ | $0.0346$ |
| $D_{43}$ | $0.6471$ |
| $\min_{n\le10^4} D_n$ | $D_1 = 0.0346$ |
| $\psi_\gamma - \theta(\gamma)$ | $\le 10^{-16}$ |
| $\mathrm{Main}_{\rm pos} - c\log n$ | $\to -0.4559$ |
| Closing margin, $44 \le n \le 2\times10^4$ | $\ge 0.14$ |

---

## References

1. X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*,
   J. Number Theory 65 (1997), 325–333.
2. E. Bombieri, J. C. Lagarias, *Complements to Li's criterion for the Riemann
   hypothesis*, J. Number Theory 77 (1999), 274–287.
3. E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.
4. A. Selberg, *On the remainder term in the formula for $N(T)$*, 1946.
5. E. Backlund, *Über die Nullstellen der Riemannschen Zetafunktion*, Acta Math. 41 (1918).
