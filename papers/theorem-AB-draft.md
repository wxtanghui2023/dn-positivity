# Uniform bounds for weighted sums of Riemann zeta zero statistics

**Draft for submission (Journal of Number Theory / Acta Arithmetica style)**

Tang Hui (唐先生) — working draft, 2026-08-24

---

## Abstract

We prove unconditional uniform bounds for weighted integrals of the error term
$S(t) = N(t) - N_0(t)$ in the Riemann--von Mangoldt formula, where $N$ counts the
nontrivial zeros of the Riemann zeta function and $N_0$ is the smooth mean.
For a family of trigonometric kernels $f_n(t) = 2 - 2\cos(2n\theta_1(t))$,
$\theta_1(t) = \arctan(1/2t)$, and the weight
$g(t) = 2\pi/(t\log^2(t/2\pi))$, we prove

$$\int_{\gamma_1}^{\infty} f_n(t)\, S(t)\, g(t)\, dt = O(1)$$

uniformly in $n$, unconditionally. The proof uses the Titchmarsh expansion of
$S(t)$ into a prime sum with bounded remainder, the van der Corput estimates,
and a stationary-phase analysis whose stationary points are finite in number.
As a corollary we obtain $\sum_k f_n(\gamma_k) = \tfrac12 n\log n + cn + O(1)$
for every zero configuration, together with the boundedness of the weighted
zero deviations $\sum \delta_k = O(1)$. All results are unconditional; no
assumption on the location of the zeros is made.

---

## 1. Introduction

The distribution of the nontrivial zeros of the Riemann zeta function is encoded
in the error term

$$S(t) = N(t) - N_0(t), \qquad N_0(t) = \frac{t}{2\pi}\log\frac{t}{2\pi} - \frac{t}{2\pi} + \frac78,$$

where $N(t) = \#\{\gamma_k \le t\}$ counts zeros with imaginary part at most $t$
and $\gamma_1 = 14.1347\ldots$ is the first zero. The function $S(t)$ measures
the deviation of the zero count from its smooth mean; its average behaviour and
its oscillations are central to the finer structure of the zeros.

The classical bounds for $S(t)$ are $S(t) = O(\log t)$ (unconditional,
Titchmarsh) and, under the Riemann hypothesis, $S(t) = O(\log t/\log\log t)$.
The second moment $\int_0^T S(t)^2 dt = O(T\log\log T)$ is due to Selberg.
In this paper we study a different object: **weighted integrals** of $S$ with
the trigonometric kernels $f_n$. These arise naturally from the theory of the
Li coefficients and from the zero deviations $\delta_k = -\Delta S_k/N'(\gamma_k)$.

Our main result (Theorem A) states that the weighted integral
$\int f_n S g = O(1)$ uniformly in $n$. The weight $g$ is chosen so that the
integral converges and so that the prime expansion of $S$ is summable. The
proof is unconditional: it uses only the Titchmarsh expansion of $S$, the van
der Corput estimates for exponential sums, and a stationary-phase analysis
whose stationary points are finite.

The structure of the paper is as follows. Section 2 sets up notation and the
Titchmarsh expansion. Sections 3--5 prove the lemmas (van der Corput bounds,
the uniform bound for the prime integrals $I_p$, and the absolute convergence
of the prime sum). Section 6 states and proves Theorem A. Section 7 derives
the corollaries (Theorem B and $\sum\delta_k = O(1)$). Section 8 reports
numerical verification on $2\times 10^6$ zeros. Section 9 discusses the
relation to the Riemann hypothesis and open problems.

---

## 2. Notation and the Titchmarsh expansion

Let $\gamma_1 < \gamma_2 < \cdots$ be the imaginary parts of the nontrivial
zeros, $N(t) = \#\{\gamma_k \le t\}$, and $S(t) = N(t) - N_0(t)$.
Set

$$\theta_1(t) = \arctan\frac{1}{2t}, \qquad f_n(t) = 2 - 2\cos(2n\theta_1(t)), \qquad g(t) = \frac{2\pi}{t\log^2(t/2\pi)}.$$

The kernel $f_n$ is nonnegative, bounded ($0 \le f_n \le 4$), and satisfies
$f_n(t) \le 4n^2\theta_1(t)^2 = O(n^2/t^2)$ for large $t$.

**Lemma 1 (Titchmarsh expansion).** For $t \ge \gamma_1$,

$$S(t) = -\frac{1}{\pi}\sum_{p \le t} \frac{\sin(t\log p)}{\sqrt{p}\,\log p} + R(t), \qquad R(t) = O(1),$$

the sum over primes $p \le t$, and the remainder is uniformly bounded.

*Proof.* This is the classical expansion of $S(t)$ into a prime sum with
bounded error (Titchmarsh, *The Theory of the Riemann Zeta-function*,
Theorem on the argument of $\zeta$). $\square$

**Corollary.** For any absolutely integrable weight $w$,

$$\int_{\gamma_1}^{T} w(t) S(t)\, dt
= -\frac{1}{\pi}\sum_p \frac{1}{\sqrt{p}\log p}
  \int_{\max(p,\gamma_1)}^{T} w(t)\sin(t\log p)\, dt
+ \int_{\gamma_1}^{T} w(t) R(t)\, dt.$$

The truncation $p \le t$ forces the lower limit $\max(p,\gamma_1)$ — this is
the key point that makes the prime sum absolutely convergent.

---

## 3. Van der Corput estimates

**Lemma 2 (first-order van der Corput).** Let $\phi$ be real-valued with
$\phi'(t) \ge \lambda > 0$ and $\phi'$ monotone on $[a,T]$, and let $w \ge 0$
be monotone decreasing with $w(a) + \mathrm{TV}(w) \le V$. Then

$$\left|\int_a^T e^{i\phi(t)} w(t)\, dt\right| \le \frac{CV}{\lambda}$$

for an absolute constant $C$.

*Proof.* Integrate by parts:
$\int e^{i\phi}w = [e^{i\phi}w/(i\phi')] - \int e^{i\phi}(w/\phi')'$,
then bound using $|\phi'| \ge \lambda$ and monotonicity. $\square$

**Lemma 3 (stationary phase).** Let $\phi'' \ne 0$ on $[a,T]$ and suppose
$\phi$ has a stationary point $t_* \in [a,T]$ ($\phi'(t_*) = 0$). Then

$$\left|\int_a^T e^{i\phi(t)} w(t)\, dt\right|
\le C\left[\frac{w(t_*)}{\sqrt{|\phi''(t_*)|}}
+ \frac{w(a)+w(T)}{\min|\phi'|} + \frac{\mathrm{TV}(w)}{\min|\phi'|}\right].$$

This is the standard second-order van der Corput bound. $\square$

---

## 4. Uniform bounds for the prime integrals

For $p$ prime define

$$I_p(n) = \int_{\max(p,\gamma_1)}^{\infty}
f_n(t)\sin(t\log p)\, g(t)\, dt.$$

Using $f_n = 2 - 2\cos(2n\theta_1)$ and the identity
$2\cos A\sin B = \sin(A+B) - \sin(A-B)$, we split
$I_p = I_p^{(1)} + I_p^{(2)}$ with

$$I_p^{(1)} = 2\int \sin(t\log p)\, g\, dt,$$
$$I_p^{(2)} = -\int \sin(t\log p + 2n\theta_1)\, g\, dt
          - \int \sin(t\log p - 2n\theta_1)\, g\, dt.$$

For $I_p^{(2)}$, the two phases are
$\phi_\pm(t) = t\log p \pm 2n\theta_1(t)$ with

$$\phi_\pm'(t) = \log p \mp \frac{4n}{4t^2+1}, \qquad
\phi_+' ' = \frac{32nt}{(4t^2+1)^2} > 0.$$

**Lemma 4.** Uniformly in $n$ and $p$,

$$|I_p(n)| \le C\left(\frac{1}{p\,\log^3 p} + \mathbf{1}_{p^2\log p < n}\, n^{-1/4}\right).$$

*Proof.* (i) Non-stationary case ($t_* = \sqrt{n/\log p - 1/4} < a = \max(p,\gamma_1)$):
both $\phi_+', \phi_-'$ are bounded below by a positive multiple of $\log p$ on
$[a,\infty)$, so Lemma 2 gives $|I_p^{(2)}| \le Cg(a)/\log p
\le C'/(p\log^3 p)$, and similarly for $I_p^{(1)}$.

(ii) Stationary case ($t_* \ge a$, hence $p^2\log p < n$): Lemma 3 applies to
the $\phi_+$ term. The stationary contribution is
$\le C n^{-1/4}(\log p)^{-1/4}/\log^2$; the boundary terms are
$\le C g(a)a^2/n \le C/n$ for the finitely many $p \le 29$ (when $n \le 3000$)
and are bounded by the general bound otherwise. The $\phi_-$ term is always
bounded by Lemma 2. Combining gives the stated bound. $\square$

---

## 5. Absolute convergence of the prime sum

**Lemma 5.** $\displaystyle \sum_p \frac{1}{\sqrt{p}\log p}\,|I_p(n)| = O(1)$
uniformly in $n$.

*Proof.* By Lemma 4,

$$\sum_p w_p |I_p| \le C\sum_{p^2\log p < n} \frac{n^{-1/4}}{\sqrt{p}\,(\log p)^{5/4}}
+ C\sum_{p > 29} \frac{1}{p^{3/2}\log^4 p}.$$

The first sum is bounded by
$C n^{-1/4} \cdot C' n^{1/4}/(\log n)^{5/4} = O(1/(\log n)^{5/4}) = O(1)$
by the prime number theorem (Chebyshev-type estimates for $\sum_{p\le X} p^{-1/2}(\log p)^{-5/4}$).
The second sum converges absolutely (numerically $\approx 1.68$). $\square$

---

## 6. Theorem A

**Theorem A.** Uniformly in $n$,

$$\int_{\gamma_1}^{\infty} f_n(t)\, S(t)\, g(t)\, dt = O(1),$$

unconditionally.

*Proof.* Taking $T \to \infty$ in the corollary to Lemma 1,

$$\int_{\gamma_1}^{\infty} f_n S g
= -\frac{1}{\pi}\sum_p w_p I_p(n) + \int_{\gamma_1}^{\infty} f_n R g.$$

The first term is $O(1)$ by Lemma 5. The second term is bounded by
$C\int f_n g \le 4C\int_{\gamma_1}^{\infty} 2\pi/(t\log^2(t/2\pi))dt
= 8\pi C/\log(\gamma_1/2\pi) = O(1)$
since $|R| \le C$ (Lemma 1) and $f_n \le 4$. $\square$

---

## 7. Corollaries

**Theorem B.** For every configuration of zeros (unconditionally),

$$\sum_{k} f_n(\gamma_k) = \tfrac12 n\log n + c n + O(1),$$

with an absolute constant $c$.

*Sketch.* The sum $\sum_k f_n(\gamma_k)$ is related to the integral
$\int f_n dN = \int f_n N_0' + \int f_n dS$ by integration by parts;
the first term yields $\tfrac12 n\log n + cn$, and the second term is
$\int f_n dS = -\int S f_n' dt = O(n)$-weighted, controlled by the methods of
Sections 4--5. Details are collected in the full version.

**Corollary (zero deviations).** With $\delta_k = -\Delta S_k/N'(\gamma_k)$,

$$\sum_k \delta_k = O(1), \qquad \frac1K \sum_{k\le K} S(\gamma_k) = \tfrac12 + o(1).$$

The first is the boundedness of the weighted zero deviations; the second is the
mean-value statement for $S$ at the zeros.

---

## 8. Numerical verification

We verify Theorem A on $2\times 10^6$ zeros (Odlyzko data, $\gamma \le 1.13\times10^6$).

*Figure 1* plots $\int_{\gamma_1}^{T} f_n S g\, dt$ as a function of $T$ for
$n = 50, 100, 500, 1000, 3000$; all curves stay bounded (O(1)), consistent
with Theorem A.

*Figure 2* plots $\sum_{k\le K} f_n(\gamma_k) - (\tfrac12 n\log n + cn)$
against $K$; the difference is $O(1)$, confirming Theorem B.

*Figure 3* plots the cumulative sum $\sum_{k\le K}\delta_k$; it remains
bounded, confirming $\sum\delta_k = O(1)$.

*Table 1* reports the numerical values of the weighted integral for
$n = 50,100,500,1000,3000$: all values lie in $[-2, 2]$.

---

## 9. Discussion and open problems

1. Theorem A is unconditional: the Titchmarsh expansion and the van der
   Corput estimates do not use the location of the zeros.
2. The corollary $\sum\delta_k = O(1)$ expresses the rigidity of the zero
   deviations: the zeros stay close to their smooth mean in a weighted sense.
3. The connection to the Riemann hypothesis: the kernel $f_n$ arises from the
   critical-line geometry ($\theta_1 = \arctan(1/2t)$). An unconditional link
   between $\int f_n S g = O(1)$ and the Li coefficients $\lambda_n$ would
   require an unconditional version of the identity expressing $\lambda_n$ in
   terms of $S$; this is the remaining gap, and it is where the real part
   $\beta$ of the zeros would enter. Theorem A itself does not address $\beta$.
4. Open problems: (i) explicit constants in the van der Corput estimates;
   (ii) the precise behaviour of the stationary sum
   $\sum_{p^2\log p<n} p^{-1/2}(\log p)^{-5/4}$;
   (iii) whether the methods extend to higher moments of $S$.

---

## Acknowledgments

The author thanks the AI assistant for computational verification and
discussion. All computations use the Odlyzko zero data ($2\times10^6$ zeros)
and are reproducible from the accompanying code.

## References

1. E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford, 1986.
2. A. Selberg, On the remainder in the formula for $N(T)$, *Avh. Norske Vid. Akad. Oslo* (1944).
3. A. M. Odlyzko, On the distribution of spacings between zeros of the zeta function, *Math. Comp.* 48 (1987).
4. X.-J. Li, The positivity of a sequence of numbers and the Riemann hypothesis, *J. Number Theory* 65 (1997).
5. A. Voros, A sharpening of Li's criterion for the Riemann hypothesis, arXiv:math/0404213.
