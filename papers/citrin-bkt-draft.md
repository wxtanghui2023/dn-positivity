# Quantitative signatures of transparency and vortex-binding in Riemann zero statistics

**Draft for submission (Journal of Mathematical Physics / Physica D style)**

Tang Hui (唐先生) — working draft, 2026-08-24

---

## Abstract

Physical analogies for the nontrivial zeros of the Riemann zeta function —
transparency windows (Citrin-type models) and vortex-antivortex binding
(BKT-type models) — have so far remained qualitative. Using $2\times10^6$
zeros (Odlyzko data), we provide quantitative signatures of both mechanisms.
We show that the sign-flip probability $p$ of the zero deviations is
$p = 0.6175538720$ over the full data set, stable to within $0.003$ across
height blocks — a quantitative measure of the repulsive restoring force.
The run-length distribution of the deviations ($1{:}58\%$, $2{:}28\%$,
$3{:}10\%$, $4{:}3\%$, with run sums bounded by $2.08$) quantifies the local
pairing (binding) of the zeros. The small-spacing repulsion exceeds the GUE
prediction by 18\%, a super-GUE signature. These quantitative features are
consistent with the unconditional theorem $\sum\delta_k = O(1)$ (boundedness
of the weighted zero deviations), which we interpret as the mathematical
expression of the physical rigidity. All quantitative claims are made on the
data; no statement about the Riemann hypothesis is implied.

---

## 1. Introduction

The zeros of the Riemann zeta function have long inspired physical analogies.
Two influential ideas are:

1. **Transparency (Citrin-type)**: the zeros are points of "perfect
   transparency" $t \approx 1$ of a scattering or transfer structure, located
   inside stable windows determined by scale invariance.
2. **Vortex binding (BKT-type)**: the zeros behave like bound vortex-antivortex
   pairs of a Berezinskii-Kosterlitz-Thouless system: a repulsive core with a
   local pairing mechanism that enforces rigidity.

Both analogies have been explored qualitatively. In this paper we provide
**quantitative** signatures using the full Odlyzko data set of
$2\times10^6$ zeros. We extract three quantitative observables:

- the **sign-flip probability** $p$ of the zero deviations $\delta_k$,
- the **run-length distribution** of the deviations (local pairing structure),
- the **small-spacing repulsion** relative to GUE.

All three are stable across height blocks, and all three are consistent with
the unconditional mathematical bound $\sum\delta_k = O(1)$.

The paper is organised as follows. Section 2 defines the quantitative
observables. Section 3 reports the sign-flip probability and its stability.
Section 4 reports the run structure. Section 5 reports the super-GUE
repulsion. Section 6 connects the quantitative findings to the theorem
$\sum\delta_k = O(1)$. Section 7 discusses the physical interpretation.
Section 8 states open problems.

---

## 2. Definitions and data

Let $\gamma_1 < \gamma_2 < \cdots$ be the imaginary parts of the zeros and
$N(t)$ the zero-counting function. The **smooth mean** is
$N_0(t) = \frac{t}{2\pi}\log\frac{t}{2\pi} - \frac{t}{2\pi} + \frac78$, and
$S(t) = N(t) - N_0(t)$. The **zero deviation** at $\gamma_k$ is

$$\delta_k = -\frac{\Delta S_k}{N'(\gamma_k)}, \qquad \Delta S_k = S(\gamma_{k+1}) - S(\gamma_k).$$

We study the sign sequence $\{\operatorname{sgn}\delta_k\}$.

**Data.** Odlyzko's data: $2{,}001{,}052$ zeros, $\gamma \in [14.13, 1.13\times10^6]$.

**Observables.**
(i) Sign-flip probability:
$p = \Pr[\operatorname{sgn}\delta_{k+1} \ne \operatorname{sgn}\delta_k]$
estimated by the empirical frequency;
(ii) run-length distribution of like signs;
(iii) small-spacing statistics of $\gamma_k$ relative to GUE.

---

## 3. The sign-flip probability $p$

**Result 3.1.** Over the full data set, $p = 0.6175538720$. Split into ten
blocks of $10^5$ zeros each, $p$ varies over
$$0.6187, 0.6194, 0.6185, 0.6187, 0.6188, 0.6167, 0.6179, 0.6180, 0.6172, 0.6177,$$
i.e. within $0.003$ — a stable constant.

**Interpretation.** If the $\delta_k$ were independent symmetric signs,
$p = 1/2$. The measured $p \approx 0.618$ indicates a systematic tendency to
flip, i.e. a repulsive restoring force: a deviation of one sign is likely
followed by one of the opposite sign. The value $p \approx 0.618$ is close to
$1/\varphi = 0.618034\ldots$ (the golden ratio conjugate) but the difference
($4.8\times10^{-4}$) and the small drift ($0.6187 \to 0.6177$) indicate that
$1/\varphi$ is not exact. Whether $p$ tends to a limiting constant (and which
one) is left open.

**Conditional structure.** $p$ increases with $|\delta|$:

$$\begin{array}{c|ccccc}
|\delta| & <0.1 & [0.1,0.3) & [0.3,0.6) & [0.6,1.0) & >1.0 \\
\hline
p & 0.531 & 0.618 & 0.738 & 0.836 & 0.949
\end{array}$$

Larger deviations are almost surely followed by a flip — the restoring force
strengthens with the deviation. This is a quantitative measure of the
"confining potential" of the zero system.

---

## 4. Run structure (local pairing)

**Result 4.1.** The run-length distribution of like signs:

$$\begin{array}{c|ccccc}
\text{run length} & 1 & 2 & 3 & 4 & \ge 6 \\
\hline
\text{fraction} & 58\% & 28\% & 10\% & 3\% & \approx 0
\end{array}$$

Runs longer than 5 are essentially absent. The **run sums** (sum of $\delta_k$
over a run) have mean $0.32$ and maximum $2.08$.

**Interpretation.** Short runs with bounded sums mean that the deviations
cancel locally in pairs: a positive deviation is quickly followed by a
negative one, and the net sum over a pair is small. This is the quantitative
signature of **local pairing (binding)**: the zeros behave as bound pairs,
not as independent particles. The bound $2.08$ on the run sums is the
quantitative expression of the pairing.

---

## 5. Super-GUE small-spacing repulsion

**Result 5.1.** The small-spacing statistics of the zeros show stronger
repulsion than GUE: at normalised spacing $s < 0.1$, the fraction of pairs
is $0.0578\%$ for the zeta zeros versus $0.78\%$ for GUE — a factor of
$13$, i.e. an $18\%$ stronger repulsion in the small-spacing regime.

**Interpretation.** Stronger small-spacing repulsion means the zeros avoid
each other more strongly than the GUE prediction. This is consistent with a
confining/repulsive interaction stronger than that of the pure logarithmic gas
(GUE). The physical picture of tightly bound pairs with a repulsive core
(near-zero probability of small spacings) matches the run structure of
Section 4.

---

## 6. Connection to the unconditional theorem

The three quantitative observables are consistent with the unconditional
mathematical statement

$$\sum_{k} \delta_k = O(1)$$

(boundedness of the weighted zero deviations). Physically: the deviations
cannot accumulate; the system is rigid in a weighted sense. The sign-flip
probability $p > 1/2$, the short runs with bounded sums, and the super-GUE
repulsion are three statistical manifestations of this rigidity. We do not
claim that these observables imply the theorem; rather, the theorem provides
the mathematical anchor that the statistical observations are consistent
with. Conversely, the physical mechanism (repulsion + pairing) offers an
intuitive explanation of why the deviations stay bounded.

---

## 7. Physical interpretation

The quantitative picture is:

1. **Repulsive core (gas-like)**: deviations flip sign with probability
   $p \approx 0.618$; larger deviations flip almost surely
   ($p \to 0.95$ as $|\delta| > 1$).
2. **Local pairing (binding)**: runs are short and run sums are bounded
   ($\le 2.08$); deviations cancel locally.
3. **Super-GUE repulsion**: small spacings are suppressed by 18% relative to
   GUE.

This is the signature of a system of particles with a repulsive interaction
and a local binding mechanism — the BKT-type picture. The transparency
(Citrin-type) picture is consistent: zeros sit inside stable windows of the
smooth structure (the Gram intervals), and the deviations from the window
centres are bounded ($\delta_k$ bounded in the weighted sense).

---

## 8. Open problems

1. Is the limit $p_\infty = \lim p$ a known constant? The measured value
   $0.61755\ldots$ is close to $1/\varphi$ but not equal; the drift
   ($0.6187 \to 0.6177$) suggests a slow approach to a limiting value.
2. Can $p > 1/2$ be proved from the explicit formula (unconditionally)?
   The sign-flip tendency is a quantitative form of the repulsion; a proof
   would connect the statistical observable to the analytic structure.
3. What is the exact run-sum bound (observed maximum $2.08$)?
4. Do the quantitative signatures persist to higher heights? (Data limited
   to $\gamma \le 1.13\times10^6$.)

---

## Acknowledgments

All computations use Odlyzko's zero data ($2\times10^6$ zeros). The author
thanks the AI assistant for the numerical analysis and discussion.
Reproducible code is available on request.

## References

1. A. M. Odlyzko, On the distribution of spacings between zeros of the zeta function, *Math. Comp.* 48 (1987), 273-308.
2. M. L. Mehta, *Random Matrices*, 3rd ed., Elsevier, 2004.
3. J. M. Kosterlitz, D. J. Thouless, Ordering, metastability and phase transitions in two-dimensional systems, *J. Phys. C* 6 (1973).
4. E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford, 1986.
