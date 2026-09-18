D0: 本档对象 = **Palojärvi Theorem 4.1（$m=1$）的自足重证 ＋ 常数改善 10 倍**（引擎＝初等覆盖引理 C）—— 关系 = 交付物（自足小注），非新机制
D1: 0
FREEZE-ACK: 本档即冻结期内的交付物整理（依 `§8.1`；不产候选结论、不改任何原档）

# An elementary covering lemma, and a self-contained proof of Palojärvi's Theorem 4.1 ($m=1$) with an improved constant

**Author**: Hui Tang · **Draft v1** 2026-09-18
**Nature**: short note — 一条初等引理 ＋ 对**已发表定理**的常数改进（不含新猜想的证明）
**Source theorem**: Palojärvi, arXiv:1807.01506v3, **Theorem 4.1**
**Archive basis**: `docs/E4-ENGINE-2-elementary-covering-lemma-selfcontained-m1-and-better-constant.md`

---

## §0 Abstract

We record an **elementary covering lemma**: for every $z\in\mathbb C$ with $|z|=1$,
$$\max_{1\le k\le5}\ \mathrm{Re}\,z^k\ \ge\ \frac12 .$$
We use it to give a **self-contained** proof of the $m=1$ case of Palojärvi's Theorem 4.1, **replacing** the invoked large-sieve-type bound (constant $1/20$, Montgomery, *Ten Lectures*, Ch. 5 Thm 11 $=$ Palojärvi Lemma 2.2) by an **elementary** constant $1/2$. The substitution improves the detection threshold: the coefficient of $\big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)$ becomes exactly **one tenth** of the source's, and the source's $20\,n\log n$ main term disappears.

## §1 The lemma

**Lemma C.**  Let $z\in\mathbb C$, $|z|=1$. Then
$$\max_{1\le k\le 5}\ \mathrm{Re}\,z^k\ \ge\ \frac12 .$$

**Proof.** Write $z=e^{i\theta}$, so $\mathrm{Re}\,z^k=\cos k\theta$. It suffices to show that
$$\bigcup_{k=1}^{5}\ \bigcup_{j\in\mathbb Z}\ \frac1k\Big(360^\circ j+[-60^\circ,60^\circ]\Big)\ =\ \mathbb R \pmod{360^\circ},$$
because $\theta$ lying in the set for some $k$ means $|k\theta|\le 60^\circ \pmod{360^\circ}$, hence $\cos k\theta\ge 1/2$. The intervals (in degrees) are
$$k=1:[0,60]\cup[300,360];\quad k=2:[150,210];\quad k=3:[100,140]\cup[220,260];$$
$$k=4:[75,105]\cup[165,195]\cup[255,285];\quad k=5:[60,84]\cup[132,156]\cup[204,228]\cup[276,300].$$
They cover the circle consecutively:
$$[0,60]_{(1)}\to[60,84]_{(5)}\to[75,105]_{(4)}\to[100,140]_{(3)}\to[132,156]_{(5)}\to[150,210]_{(2)}$$
$$\to[165,195]_{(4)}\to[204,228]_{(5)}\to[220,260]_{(3)}\to[255,285]_{(4)}\to[276,300]_{(5)}\to[300,360]_{(1)} .$$
$\square$

**Numerical check** (复核): minimizing numerically over a fine grid gives $\min_\theta\max_{1\le k\le5}\cos k\theta=0.5$, attained at $\theta=60^\circ$ and $300^\circ$ (finest-grid value $0.5000014$).

**Optimality.** The constant $1/2$ is best possible: at $\theta=60^\circ$, $(\cos k\theta)_{k=1}^{5}=(1/2,-1/2,-1,-1/2,1/2)$, so the maximum equals exactly $1/2$. Hence no larger constant can hold uniformly.

**Comparison with the source's engine** `[出处]`: the source invokes $\max_{1\le n\le5M}\mathrm{Re}\sum_{j\le M}z_j^n\ge \frac1{20}$; at $M=1$ Lemma C gives $\frac12>\frac1{20}$, i.e. **ten times stronger** *and* elementary (no large-sieve input).

## §2 Application: Palojärvi Theorem 4.1 at $m=1$

**Source statement** `[出处]` (Palojärvi, Thm 4.1): let $F$ satisfy (a)–(d), $\tau>1/e$, and suppose $F$ has **at most one** zero $\rho_1$ with $|\rho_1/(\rho_1-\tau)|>1$. Then
$$\rho_1\ \text{exists}\iff |\mathrm{Re}\,\lambda_F(n,\tau)|\ \ge\ \big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)\,n\log n\quad\text{for some } n\in[N,5N],\ N\mid n .$$

**Decomposition** (source (37), verbatim `[出处]`): with $w_\rho=\rho/(\rho-\tau)$,
$$\mathrm{Re}\,\lambda_F(n,\tau)=\underbrace{\lim_{t\to\infty}\sum_{T(n)<|\Im\rho|\le t,\ 0\le\Re\rho\le\tau/2}\mathrm{Re}(1-w_\rho^n)}_{(i)\ \text{large height}}+\underbrace{\sum\cdots}_{(ii)}+\underbrace{\sum\cdots}_{(iii)},$$
where $T(n)=ne\tau$ and $|w_\rho|\le1\iff \Re\rho\le\tau/2$.

- **($\Leftarrow$) no off-axis zero.** Then term (iii) is absent and every zero in (i)(ii) satisfies $|w_\rho|\le1$, so $|\mathrm{Re}(1-w^n)|\le|1-w^n|\le1+|w|^n\le2$. By the source's Theorem 2.1,
$$|\mathrm{Re}\,\lambda_F(n,\tau)|\le\big(K_{F,1}+K_{F,4}\big)n\log n\qquad(\forall n),$$
**with the same constants as the source** (using $|1-w^n|$ loses no constant).

- **($\Rightarrow$) an off-axis zero** $\rho_1$ with $R'\mathrel{:=}|w_1|\ge R>1$. Put $z\mathrel{:=}w_1^N/R'^N$, so $|z|=1$. By **Lemma C** choose $k\le5$ with $\mathrm{Re}\,z^k\ge\frac12$; then
$$\mathrm{Re}(1-w_1^{n})=1-R'^{\,n}\,\mathrm{Re}\,z^{k}\ \le\ 1-\tfrac12 R'^{\,n}\qquad(R'^{\,n}\ge R^n),$$
hence
$$|\mathrm{Re}\,\lambda_F(n,\tau)|\ \ge\ \tfrac12 R'^{\,n}-1-\big(K_{F,1}+K_{F,4}\big)n\log n\ \ge\ \big(K_{F,1}+K_{F,4}\big)n\log n$$
as soon as
$$\boxed{\,R^{\,n}\ \ge\ 4\big(K_{F,1}(\tau)+K_{F,4}(\tau)\big)\,n\log n+2\,}$$

**Comparison with the source** `[出处·已逐字核]`(2026-09-18): the source's threshold is
> **Verbatim (source, p.20)**: "It is sufficient to show $R^n\ge 40n\log n(\tfrac12+K_{F,1}(\tau)+K_{F,4}(\tau))$."

$$R^{\,n}\ \ge\ 40\,n\log n\Big(\tfrac12+K_{F,1}+K_{F,4}\Big)=20\,n\log n+40\big(K_{F,1}+K_{F,4}\big)n\log n,$$
so
$$\big[20n\log n+40(K_{F,1}+K_{F,4})n\log n\big]-\big[4(K_{F,1}+K_{F,4})n\log n+2\big]=20n\log n+36(K_{F,1}+K_{F,4})n\log n-2>0$$
(for $n\log n\ge e$). Thus **in the same window and with the same conclusion the threshold is strictly smaller**: the $(K_{F,1}+K_{F,4})$ coefficient drops to $1/10$ of the source's, and the $20\,n\log n$ main term is additionally saved.

**Explicit $N$.** Replacing $\frac1{20}$ by $\frac12$ in the three-scale split of the source's §5b gives
$$N_1^{\text{new}}=\Big\lceil\max\Big\{\frac{T_0}{e\tau},\ \exp\big(-W_{-1}(-\tfrac23\log R)\big),\ \frac{12\log\big(4(K_{F,1}+K_{F,4})+2\big)}{\log R}\Big\}\Big\rceil,$$
i.e. the $\frac{12}{\log R}$ slot is unchanged and only the constant $40(K_{F,1}+K_{F,4})+20$ is replaced by $4(K_{F,1}+K_{F,4})+2$; the $m$-cost in $N$ decreases accordingly.

## §3 The case $m\ge2$: still one external dependence

- **(a) Fejér-weight route** `[严格]` (self-contained, but needs a *comparability* assumption): with Fejér weights $w_k=1-k/(5M)$,
$$\sum_{k\le5M}w_k\Big|\sum_j z_j^k\Big|^2\ \ge\ \sum_j D_j-\frac{M(M-1)}2,\qquad D_j:=\sum_{k\le5M}w_k|z_j|^{2k},$$
(diagonal $\ge0$; each off-diagonal pair $\ge-\frac12$ by non-negativity of the Fejér kernel), hence
$$\max_{k\le5M}\Big|\sum_j z_j^k\Big|^2\ \ge\ \frac{\sum_j D_j-M(M-1)/2}{5M/2}.$$
Numerically `[复核]`: if all $|z_j|=1$, $\sum_j D_j\approx(5M/2)M$ gives the bound $\ge\frac45 M$, i.e. $\ge\sqrt{0.8M}$. **Limitation**: it needs $\sum_j D_j>M(M-1)/2$, i.e. most exceptional moduli close to the maximum (comparability); for widely spread moduli the route degenerates.
- **(b) Still Montgomery**: the *real-part* detection at $m\ge2$ with spread moduli still needs Lemma 2.2; we did not make it self-contained here.

## §4 Scope and honesty

- **Claimed**: Lemma C (elementary, complete proof, constant optimal) and, via it, a **self-contained** proof of the $m=1$ case of Palojärvi's Theorem 4.1 **with a strictly better threshold** ($(K_{F,1}+K_{F,4})$-coefficient reduced by a factor $10$; the $20n\log n$ term removed).
- **Not claimed**: any progress on the $m\ge2$ case; any new equivalence criterion; any RH-related statement. The source theorem's *structure* is used as-is (`[出处]`), including its decomposition (37) and Theorem 2.1.
- ✅ `[出处·已逐字核]`(2026-09-18): the source's threshold formula, including its $20\,n\log n$ term, is **verbatim confirmed** against Palojärvi arXiv:1807.01506v3 (p.20). The core comparison of this note therefore rests on verified source text, not on an archive transcription.
- No RH is used anywhere in this note; the input is the source theorem plus elementary covering.

## References

- M. Palojärvi, *On the Li criterion and the explicit zero-free region*, arXiv:1807.01506v3, Theorem 4.1 (and Lemma 2.2, Theorem 2.1).
- H. L. Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis*, Ch. 5, Thm 11 (the replaced engine).
