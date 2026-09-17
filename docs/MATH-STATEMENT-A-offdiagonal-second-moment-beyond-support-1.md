已查地图：命中 `C-26`(SUPPORT-1 合封)｜`W6-MAJORANT-1-*`｜`V300` → 本档＝**纯数学问题陈述**（无内部编号、无叙事）

# Problem A — Off-diagonal second moment of a windowed Dirichlet polynomial, beyond the support-1 threshold

## 1. Notation and objects

Let $\Lambda$ denote the von Mangoldt function. For integers $n\ge 2$ put
$$a_n\ :=\ \frac{\Lambda(n)}{\sqrt n},\qquad y_n\ :=\ \log n .$$
Fix $T\ge 2$ and write $L:=\log T$.

Let $\varphi:\mathbb R\to[0,1]$ be even, with
$$1_{[-L/2+w,\;L/2-w]}\ \le\ \varphi^2\ \le\ \varphi\ \le\ 1_{[-L/2,\;L/2]} \qquad (0\le w<L/2),$$
so $\varphi$ is a smoothed indicator of $[-L/2,L/2]$. Put
$$b:=\frac1L\int_{\mathbb R}\varphi^4,\qquad \Phi:=c\,\varphi^2\quad(\text{$c$ normalised by }\Phi(0)=aL),$$
and let $g:=\varphi^2\star\varphi^2$ denote the autocorrelation, $(v\star v)(t)=\int_{\mathbb R}v(x)v(x+t)\,dx$. One then has
$$(L-2w-|t|)_+\ \le\ g(t)\ \le\ (\varphi\star\varphi)(t)\ \le\ (L-|t|)_+ .$$

For $n\ge2$ define the two one-sided window integrals
$$\alpha_n^{+}:=\int_0^T\Phi(x)^2\,n^{ix}\,dx,\qquad \alpha_n^{-}:=\int_{-T}^0\Phi(x)^2\,n^{ix}\,dx ,$$
so that $|\alpha_n^{\pm}|\le \pi bL\le \pi L$.

The object of study is the **windowed second moment** of the Dirichlet polynomial
$$P_X(t):=-\frac1{2\pi}\sum_{n\le X}a_n\bigl(n^{it}+n^{-it}\bigr)\qquad (X\ge2,\ t\in\mathbb R),$$
namely $M_X(T):=\iint \Phi(x)\,P_X(\tau+x)\overline{P_X(\tau)}\,d\tau\,dx$ over the range $\tau\in[T,2T]$.

## 2. Decomposition and the known result

Expanding $n^{i(\tau+x)}+n^{-i(\tau+x)}$ against $\overline{P_X(\tau)}$ and splitting according to $n=m$ versus $n\ne m$ gives the decomposition
$$M_X(T)\ =\ D_X(T)\ +\ O_1\ +\ O_2 ,$$
where the **diagonal** term is
$$D_X(T)\ =\ \frac{T}{\pi}\sum_{n\le X}\frac{\Lambda(n)^2}{n}\,g(y_n)\ +\ O\!\left(L^2\log L\right),$$
the **second** term satisfies $|O_2|\ll XL$, and the **off-diagonal** term is, with $\vartheta:=y_n-y_m\ne0$,
$$O_1\ =\ \frac1{2\pi^2}\,\mathrm{Re}\!\!\sum_{n\ne m\le X}\!\!\frac{a_n a_m}{i\,\vartheta}\Bigl[\Bigl(\tfrac nm\Bigr)^{2iT}\!\bigl(\alpha_m^{+}+\alpha_n^{-}\bigr)\ -\ \Bigl(\tfrac nm\Bigr)^{iT}\!\bigl(\alpha_n^{+}+\alpha_m^{-}\bigr)\Bigr].$$
(This is the exact rearrangement produced by substituting $\tau=\tau'+x$ and integrating the inner variable; it is a sum of **four bilinear forms** of the shape $\sum_{n\ne m} x_n z_m/(y_n-y_m)$ with $x,z\in\{a_n,\ a_n|\alpha_n^{\pm}|\}$.)

**Known, unconditionally.** By the Montgomery–Vaughan bilinear (Hilbert-type) inequality [MV74, Lemma 2.2] applied with $\{\lambda_n\}=\{y_n\}_{n\le X}$ and $\delta_n^{-1}\le 2n$, each of the four forms is $\ll L\sum_n a_n^2/\delta_n\ll L^2X$; hence
$$|O_1|\ \ll\ L^2 X .$$
Since $\sum_{n\le X}\Lambda(n)^2/n\asymp\tfrac12\log^2 X$ and $g(y_n)\asymp L$ on the bulk, one has $D_X(T)\asymp T L\log^2 X$, so the diagonal dominates precisely when
$$\boxed{\ X\ \ll\ T\log T\ }\qquad(\text{the frontier takes }X\le T).$$

## 3. The target inequality

Define the threshold exponent
$$\eta^{\ast}\ :=\ \sup\Bigl\{\eta\ge0:\ |O_1(X,T)|=o\bigl(D_X(T)\bigr)\ \text{uniformly for }2\le X\le T^{1+\eta}\Bigr\}.$$
Currently $\eta^{\ast}=0$ is all that is known unconditionally. The problem:

> **Problem A.** Decide whether $\eta^{\ast}>0$; equivalently, find $\eta>0$, $\delta>0$ such that
> $$|O_1(X,T)|\ \le\ (1-\delta)\,D_X(T)\qquad\text{for all }2\le X\le T^{1+\eta}.$$

**Equivalent formulations.**
- (Second-moment form.) The $k$-th moment version of the off-diagonal sum is under unconditional control in the Rudnick–Sarnak range $X^k\le T^{2-\varepsilon}$. For $k=2$ this reads $X\le T^{1-\varepsilon/2}$. Problem A asks to extend $k=2$ from $X\le T^{1-\varepsilon/2}$ to $X\le T^{1+\eta}$.
- (Endpoint form.) At $X=T$ the condition $X^2\le T^{2-\varepsilon}$ fails *only by the factor $T^{\varepsilon}$*. So the gap is an **endpoint $\varepsilon$-gap**, not a gap of fixed power.
- (Prime-pair form.) Evaluating $O_1$ for $X\gg T$ is equivalent to input on prime pairs: it is of the strength of the Hardy–Littlewood pair conjectures, i.e. of Montgomery's pair-correlation conjecture for test functions with Fourier support $>1$.

## 4. Concretely attackable sub-questions

**(SQ1) Is Montgomery–Vaughan sharp for this kernel?** The MV bound uses only $\ell^2$ norms of the coefficient vectors. The kernel here carries extra structure: four factors $\alpha_n^{\pm}$ of size $\le\pi L$ and the modulations $(n/m)^{iT}$, $(n/m)^{2iT}$. Determine the true operator norm
$$\sup\Bigl\{|O_1|\Big/\bigl(\textstyle\sum_n n|a_n|^2\bigr)\Bigr\}$$
over the admissible coefficient configurations. If this supremum is $\ll L^2X\,T^{-c}$ for some $c>0$, then MV is not sharp, and the obstruction is an artifact of the $\ell^2$-only method rather than of the arithmetic.

**(SQ2) Direct oscillatory-sum analysis on the log-grid.** $O_1$ is a sum over $n\ne m$ with kernel $1/(y_n-y_m)$ and phase $\exp(iT\,y_{n/m})$. Grouping $n,m$ into dyadic blocks $I=[N,2N]$ and applying first- and second-derivative estimates (van der Corput) on the set $\{y_n\}=\{\log n\}$, compute an explicit bound and compare it with $L^2X$. (In the linearised model — phase $t\,y$ with $t\asymp T$ — the local phase increment is $\approx 2\pi L^2$, i.e. strongly oscillatory, which suggests the block-wise bound may be smaller than the MV bound.)

**(SQ3) A distinguishing experiment.** Replace the coefficient sequence $a_n=\Lambda(n)/\sqrt n$ by $a_n=\mu^2(n)/\sqrt n$ (squarefree indicator), keeping the window, the normalisation and the decomposition fixed. The squarefree indicator admits the factorisation $\mu^2(n)=\sum_{d^2\mid n}\mu(d)$, i.e. a degree-2 local factor $1+p^{-s}$, whereas prime extraction corresponds to a degree-1 monomial $p^{-s}$. Compare $|O_1|/D_X$ for $X\gg T$ across the two families:
- if the bound succeeds for $\mu^2$ and fails for $\Lambda$, the obstruction is localised at prime extraction;
- if both fail identically, the obstruction lies in the two-body (bilinear) structure itself.

## 5. What is *not* claimed
No claim is made that $\eta^\ast>0$ is false, nor that the two families in (SQ3) must behave differently. The only unconditional inputs used above are the Montgomery–Vaughan inequality and the Rudnick–Sarnak range; no hypothesis on the zeros of $\zeta$ is used.

---

# 附：另外两个候选（同样剥壳，供挑选）

## Problem B（区域 ⟹ 直线 的强度升级）
Let $N(\sigma,T)$ count zeros $\rho=\beta+i\gamma$ of $\zeta$ with $\beta\ge\sigma$, $|\gamma|\le T$. Known: $N(\sigma,T)\ll T^{A(1-\sigma)+o(1)}$ with $A=30/13$ (Guth–Maynard 2026), improving $A=2$ (Ingham). The conversion $N(\sigma,T)\Rightarrow$ zero-free region $\sigma>1-c/(A\log T)$ is classical, and $A\to0$ recovers RH.
**Target:** construct an upgrade mechanism from a bound of the form $N(\sigma,T)\ll T^{A(1-\sigma)+o(1)}$ to a statement of the form $\beta\le1/2$ for the relevant zeros — or prove that no such mechanism can improve the constant below $A=1$ (equivalently: identify what input type, beyond $N(\sigma,T)$, is needed).

## Problem C（余项的二阶矩）
Let $S(t):=\frac1\pi\arg\zeta(1/2+it)$ (Riemann–Siegel), and let $P_x(t)$ be a prime-side partial sum obtained from the explicit formula. For a window of length $H$ near height $T$, the question is whether one can construct the decomposition $S(t)=P_x(t)+R_S(t)$ such that
$$\|R_S\|_{L^2(T,T+H)}^2\ \ll\ \frac{H}{\log T}.$$
Known: the pointwise route forces $\sup|R_S|\int|\varphi'|$ which overshoots the required budget by a factor $\approx2.5$; and the available moment bounds for $R_S$ are stated at a different level than the $S$-level quantity required.
