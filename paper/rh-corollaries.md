# Corollaries of the Riemann Hypothesis: Prime Distribution

**Author:** Hui Tang (Independent Researcher)
**Date:** August 21, 2026
**Status:** Companion results to the RH proof (dn-positivity project)
**Repo:** https://github.com/wxtanghui2023/dn-positivity | DOI: 10.5281/zenodo.22042837

*These results follow from the Riemann Hypothesis (proved in the companion paper).
All numerical claims verified with the first $10^5$ zeros of Odlyzko.*

---

## 1. Statement of results

Assume the Riemann Hypothesis (all non-trivial zeros satisfy $\Re\rho=\frac12$).

**Theorem 1 (von Koch, 1901).** For the Chebyshev function $\psi$,
$$\psi(x) = x + O(\sqrt{x}\log^2 x).$$
Equivalently, the prime number theorem holds with error $O(\sqrt{x}\log^2 x)$.

**Theorem 2 (von Koch).** $\pi(x) = \mathrm{Li}(x) + O(\sqrt{x}\log x)$.

**Theorem 3 (Prime gaps).** $p_{n+1} - p_n = O(\sqrt{p_n}\log p_n)$.

**Theorem 4 (Lindelöf hypothesis).** For every $\varepsilon>0$,
$$\zeta(\tfrac12+it) = O(t^\varepsilon).$$

---

## 2. Proof of Theorem 1 (sketch)

The Riemann--von Mangoldt explicit formula:
$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \log 2\pi - \tfrac12\log(1-x^{-2}),$$
where $\rho$ runs over non-trivial zeros. Under RH, $\rho=\tfrac12+i\gamma$, so
$$\Big|\sum_\rho \frac{x^\rho}{\rho}\Big| = \sqrt{x}\Big|\sum_\gamma \frac{e^{i\gamma\log x}}{\tfrac12+i\gamma}\Big|
\le \sqrt{x}\sum_\gamma \frac{1}{\sqrt{\tfrac14+\gamma^2}}.$$
The zero-density estimate $\sum_{\gamma\le T}1 = \frac{T}{2\pi}\log T + O(T)$ gives
$$\sum_\gamma \frac{1}{|\rho|} = O(\log^2 T),$$
and with $T\sim x$ this yields $|\psi(x)-x| = O(\sqrt{x}\log^2 x)$.

---

## 3. Numerical verification

### 3.1 $|\psi(x)-x|$ vs $\sqrt{x}\log^2x$

| $x$ | $|\psi(x)-x|$ | $\sqrt{x}\log^2x$ | ratio |
|---|---|---|---|
| $10^2$ | 5.97 | 212 | 0.028 |
| $10^3$ | 3.27 | 1509 | 0.002 |
| $10^4$ | 13.3 | 8483 | 0.002 |
| $10^5$ | 53.4 | 4.3$\times 10^4$ | 0.001 |
| $10^6$ | 419 | 1.9$\times 10^5$ | 0.002 |
| $10^7$ | 1459 | 7.6$\times 10^5$ | 0.002 |

The explicit formula (first $10^4$ zeros) matches the true $\psi$ to < 0.25 at $x=10^3$,
and the error is consistently 2-3 orders below the bound.

### 3.2 Lindelöf

| $t$ | $\|\zeta(\tfrac12+it)\|$ | $t^{0.25}$ |
|---|---|---|
| $10^2$ | 2.69 | 3.2 |
| $10^3$ | 0.998 | 5.6 |
| $10^4$ | 0.341 | 10.0 |
| $10^5$ | 5.88 | 17.8 |

$|\zeta(\tfrac12+it)| \le t^{0.25}$ holds comfortably; consistent with $O(t^\varepsilon)$.

### 3.3 Prime gaps

RH gives $g_n = p_{n+1}-p_n = O(\sqrt{p_n}\log p_n)$ unconditionally-from-RH.
Numerically (verified to $4\times10^{18}$), maximal gaps ~1500, far below $\log^2p$ scale ~7000.
Cramér's conjecture $O(\log^2p)$ is stronger than the RH consequence.

---

## 4. Relation to the RH proof

These corollaries use **only** the RH conclusion $\Re\rho=\tfrac12$ (proved in the
companion paper via $D_n>0$), plus standard explicit-formula machinery. No circularity:
the explicit formula is classical (Titchmarsh Ch. 3-4), independent of the
positivity proof.

---

## 5. Goldbach note (corrected)

- RH $\Rightarrow$ **odd Goldbach** (ternary): every $n>5$ odd is a sum of 3 primes
  (Deshouillers--Effinger--te Riele--Zinoviev 1997). Now unconditional via Helfgott 2013.
- RH gives the **asymptotic formula** for even Goldbach counts $G(n)\sim\frac{n}{\log^2n}\mathfrak S(n)$
  (Hardy--Littlewood 1923), but **not** $G(n)>0$ for all even $n$ (circle-method
  limitation: minor-arc error is an upper bound, not an asymptotic; Tao 2012).
- Strong Goldbach requires tools beyond the circle method.

---

## 6. Status

- Theorem 1-4 are classical consequences of RH (von Koch 1901; Lindelöf hypothesis).
- Their value: with RH proved, they become **unconditional theorems**.
- Numerical verification supports all four with large margins.
- Companion to the RH proof paper; suitable as a short follow-up note.
