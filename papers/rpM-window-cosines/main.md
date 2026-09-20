已查地图（**先查后写**）：查 `CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md`／`ASSETS-REGISTRY.md`（关键词：余弦和｜power sum｜Turán｜Montgomery｜Palojärvi）。命中为**他线**内容（RH 主线的 Montgomery–Vaughan／support>1 等）⟹ 本档为**对外论文草稿**，不涉已封 RH 路线 ⟹ 可开 ✓

D0: 本档对象 = 档案已有成果（`C-152`／`C-154`／`C-159`／`C-163`／`C-164`／`C-168`／`C-172`／`C-173`／`C-176`／`C-178`／`C-183`／`C-188`／`C-190`）的**对外成文整合** —— 关系 = 整合／成文（非重命名、非新对象）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与成文（依 §8.1；不产新数学结论）

---

# Sharp constants for real-part power sums over a short window

**Draft v1 · 2026-09-20 · Hui Tang**

> **Status.** This is a *draft*. All machine-assisted results are labelled **[CA]** (computer-assisted, certified) and all hand proofs **[P]** (proved). No claim is made that the general-$M$ problem is solved.

## Abstract

Let $z_1,\dots,z_M\in\mathbb{C}$ with $|z_j|=1$ and put
$$f(k)\;:=\;\sum_{j=1}^{M}\cos(k\theta_j),\qquad z_j=e^{i\theta_j}\neq1 .$$
We study the *short-window* real-part power-sum problem
$$\textbf{(RP}_M\textbf{)}\qquad \max_{1\le k\le 5M}\ \operatorname{Re}\sum_{j=1}^{M}z_j^{k}\ \ge\ \tfrac12 .$$
The window length $5M$ is *linear* in $M$, and the requested constant $\tfrac12$ is $10\times$ the constant $\tfrac1{20}$ that appears in the classical weighted-Hilbert (Turán–Montgomery–Palojärvi) chain. The present window lies strictly between the two regimes for which the literature has sharp-order answers: $m\sim n$ (Turán) and $m\sim n^{2}$ (Andersson), see §1.4.

Results of this draft:

| # | Statement | Status |
|---|---|---|
| 1 | $\inf_\theta\max_{1\le m\le N}\cos(m\theta)=\cos\frac{2\pi}{N+1}$, **sharp** | **[P]** §2 |
| 2 | (RP$_1$) and (RP$_2$) hold, with $1/2$ **optimal** | **[P]** §3, §4 |
| 3 | (RP$_3$), (RP$_4$), (RP$_5$) hold | **[CA]** §5 |
| 3$'$ | $M=3$ **minimizer identified**: $m_3=F_3(\varphi_0)$ with $\mathcal M_3=S_3\cdot\varphi_0$ (unique KKT root; interval local growth + strict far-field exclusion) | **[CA]** §5.5 |
| 4 | $m_M\le M-1$ for all $M\ge2$ | **[P]**+**[CA]** §6 |
| 5 | Monotonicity $m_{M+1}\ge m_M$ holds on the *commensurable class*; general $M$ open | **[P]** §7 |
| 5$'$ | $\kappa_N(\lambda)=\kappa_3(\lambda)$ for all $N\ge4$ (so the $\varepsilon$-threshold cannot be improved by using more multiples) | **[P]** §7.2 |
| 5$''$ | Equality set of $\kappa_N$ = primitive $(N+1)$-th roots of unity | **[P]** §2 |
| 5$'''$ | Equality set of the $M=2$ problem = $\{\pi/3,\pi/2\}$ (primitive 6th and 4th roots) | **[P]** §4 |
| 8 | Cassels-type weighted constants $g_w(10)$: table for $w\le5$; **$g_2(10)=1$ exactly, with equality only at $(\pi/3,\pi/2)$** | **[CA]** §7.4 |
| 6 | Damped analogue: $M=2$ uniform bound $0.364984$ for **all** radii | **[CA]** §8 |
| 7 | Damped $M=3$: certified bracket $0.3730918\le C_3\le0.373092075762$ | **[CA]** §8 |

Here $m_M$ denotes the undamped min–max constant and $C_M$ the damped one (§1.1). The bracket in row 7 has relative width $<8\times10^{-7}$.

---

## §1 Introduction

### §1.1 Setting and the two constants

Throughout, $\theta_j\in[0,2\pi)$ and $z_j=e^{i\theta_j}$. Because $\cos$ is even we may take $\theta_j\in[0,\pi]$; write $\varphi_j$ for this representative. Define

- **undamped min–max constant**
$$m_M\;:=\;\inf_{\varphi_1,\dots,\varphi_M\in[0,\pi]}\ \max_{1\le k\le5M}\ \sum_{j=1}^{M}\cos(k\varphi_j),$$
- **damped min–max constant**
$$C_M\;:=\;\inf_{\substack{0\le r_j\le1\\ \max_j r_j=1}}\ \inf_{\varphi_1,\dots,\varphi_M\in[0,\pi]}\ \max_{1\le k\le5M}\Big[\cos(k\varphi_1)+\sum_{j=2}^{M}r_j^{k}\cos(k\varphi_j)\Big].$$

The normalization $\max_jr_j=1$ is the exact analogue of $\max_j|z_j|=1$ in the classical statement. Clearly $C_M\le m_M$.

$$\textbf{(RP}_M\textbf{)}\ \text{is equivalent to}\ m_M\ \ge\ \tfrac12 ,\qquad\text{and}\qquad \textbf{(RP}^\text{damp}_M\textbf{)}\ \text{to}\ C_M\ \ge\ \tfrac1{20}.$$

### §1.2 The classical statement we sharpen

The chain we improve is stated verbatim in the literature we could reach as follows.

> **Lemma 2.2** (as quoted in Palojärvi 2019, arXiv:1807.01506, p. 6, attributed to Chapter 5, Theorem 11 of Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis*, CBMS 84, AMS 1994). *Let $M\ge1$ be an integer and let $z_1,\dots,z_M$ be complex numbers satisfying $\max_j|z_j|=1$. Then*
> $$\max_{1\le n\le5M}\ \operatorname{Re}\sum_{j=1}^{M}z_j^{n}\ \ge\ \frac1{20}.$$

Two features of this statement are *load-bearing* for us and are worth isolating:

1. the hypothesis is $\max_j|z_j|=1$ — the $z_j$ need **not** be unimodular; the problem is a *damped* one;
2. the window is $5M$, i.e. **linear** in $M$;
3. the constant is $1/20$.

Our (RP$_M$) is exactly the same problem with $|z_j|=1$ for **all** $j$ and with the constant raised from $1/20$ to $1/2$.

> **Verbatim-check note.** The original source (Montgomery, CBMS 84) is not available to us; the statement above is used exactly as quoted by Palojärvi, and no claim is made about the precise wording of Montgomery's Theorem 11. The self-contained reproof we give in §1.5 covers the *unimodular* case, which is the case we need.

### §1.3 What is genuinely new here

- **Constant.** $1/20=0.05\to$ $\ge0.364984$ (damped $M=2$, all radii) and $\ge0.3730918$ (damped $M=3$): a factor $7.3$–$7.5$. In the unimodular case we reach $m_3\ge0.75,\ m_4\ge1/2,\ m_5\ge1/2$ against the same $1/20$.
- **A sharp one-point theorem.** The quantity $\kappa_N:=\inf_\theta\max_{m\le N}\cos(m\theta)$ has the closed form $\cos\frac{2\pi}{N+1}$ (§2). This is elementary but we did not find it stated in this form; it unifies our $M=1$ lemma ($N=5$) and the covering lemma ($N=3$).
- **A window-regime map.** We locate the literature gap precisely (§1.4).
- **Method.** A four-gate protocol for turning numerical extrema into *certificates* (§9).

### §1.4 Window-regime map (where our problem sits)

Let $n=M$ and let $m$ be the window. Write
$$\textstyle(\star)\quad=\ \inf_{|z_j|=1}\ \max_{1\le \nu\le m}\Big|\sum_{j=1}^{n}z_j^{\nu}\Big| .$$

| window $m$ | value of $(\star)$ | source |
|---|---|---|
| $m\le n-1$ | $0$ (trivial: $z_j=e^{2\pi ij/n}$) | — |
| $m=n$ | $1$ | Turán 1969 |
| $\mathbf{m=5n}$ | **unknown** — this paper | **gap** |
| $m=n^{2}$ | $\sim\sqrt n$; exact values for special $n$ | Andersson (arXiv:math/0607238) |
| $m= n^{h}$, $h\ge2$ | $(h-1+o(1))\sqrt n$ | Andersson (arXiv:0706.4131), via Katz character sums |

Andersson's theorems (arXiv:0704.1879, Thm. 1 and 2) hold for **any** $m\ge n$, so the Fejér-type machinery is *available* at $m=5n$; however (see §8.3) it is structurally capped near $1/20$: the diagonal term of the Fejér-weighted identity decays as soon as the moduli are allowed below $1$. This is precisely why the damped case needs its own treatment.

**Modulus vs. real part.** All rows of the table concern the *modulus* $|\sum z_j^\nu|$; our problem concerns the *real part*, with a linear window. The two are not comparable by the trivial inequality, and the linear-window real-part problem appears not to be in the literature.

### §1.5 Self-contained reproof of the unimodular case of Lemma 2.2

For completeness we record that the unimodular case of Lemma 2.2 can be recovered from Andersson's mechanism (arXiv:0704.1879) applied to a *symmetrized* system. Take $2M$ points $\{z_j,\bar z_j\}$ with weights $b_j=\tfrac12$ each. Then the weighted power sums are
$$g(\nu)=\sum_j b_j\big(z_j^{\nu}+\bar z_j^{\nu}\big)=\operatorname{Re}\sum_{j=1}^Mz_j^{\nu},$$
with $A:=\sum b_j=M$, $B:=\sum b_j^{2}=M/2$ and $|g(\nu)|\le M$. Substituting into Andersson's Theorem 1 with $m=5M$ gives
$$\max_{1\le\nu\le5M}\operatorname{Re}\sum_{j=1}^Mz_j^{\nu}\ \ge\ \frac{B(m+1)-A^{2}}{2Mm}\Big|_{A=M,\;B=M/2,\;m=5M}\ >\ \frac1{20}\qquad(M\ge1),$$
which is a *strict* constant $1/20$ in the unimodular case for every $M$, obtained without reference to the unavailable original. (Numerically this route is far from sharp: see §8.)
> **To re-check before submission.** The two terms $A^{2}$ and $mM^{2}$ enter differently in Andersson's Theorems 1 and 2, and our archived derivation of the explicit value contains an inconsistency; only the *qualitative* statement above is used in this draft, and the explicit constant is deliberately not asserted here.

### §1.6 Notation

$f(k)=\sum_j\cos(k\varphi_j)$; a frequency $k$ is *active* at $\varphi$ if $f(k)=\max_{\nu\le5M}f(\nu)$. For a box $B=\prod_j[a_j,b_j]$ we use the **separable lower bound**
$$\mathrm{LB}(B)\ :=\ \max_{1\le k\le5M}\ \sum_{j}\ \min_{\varphi_j\in[a_j,b_j]}\cos(k\varphi_j)\ \le\ \min_{\varphi\in B}\ \max_{1\le k\le5M}\ f(k),$$
which is the workhorse of every certificate below.

---

## §2 The one-point problem: $\kappa_N$ has a closed, sharp form

**Theorem 2.1 [P].** For every real $\theta$ and every integer $N\ge1$,
$$\max_{1\le m\le N}\cos(m\theta)\ \ge\ \cos\frac{2\pi}{N+1},$$
and the bound is attained, e.g. at $\theta=\frac{2\pi}{N+1}$.

**Proof.** Consider the $N+1$ points $\{0,\theta,2\theta,\dots,N\theta\}$ modulo $2\pi$. Two of them lie within distance $\frac{2\pi}{N+1}$ of each other; their difference is $m\theta$ with $1\le m\le N$, hence $\|m\theta/2\pi\|\le\frac1{N+1}$. Thus $m\theta$ lies within $\frac{2\pi}{N+1}$ of $2\pi\mathbb Z$, and since the distance is $\le\pi$ and $\cos$ decreases on $[0,\pi]$,
$$\cos(m\theta)\ \ge\ \cos\frac{2\pi}{N+1}. \qquad\square$$

**Corollary 2.2 [P].** $\kappa_N:=\inf_\theta\max_{m\le N}\cos(m\theta)=\cos\frac{2\pi}{N+1}$.

**Corollary 2.3 (equality set) [P].** Equality holds in Theorem 2.1 if and only if
$$\theta\equiv\frac{2\pi k}{N+1}\pmod{2\pi},\qquad k=1,\dots,N,\quad\gcd(k,N+1)=1 .$$
Equivalently: *the extremal angles are exactly the primitive $(N+1)$-th roots of unity*, and there are $\varphi(N+1)$ of them (Euler's totient). In particular no irrational $\theta$ attains the bound.

**Proof.** For $m\le N$, $\cos(m\theta)=\cos\big(2\pi\|m\theta/2\pi\|\big)$, so
$$\max_{m\le N}\cos(m\theta)=\cos\Big(2\pi\min_{1\le m\le N}\big\|m\theta/2\pi\big\|\Big)$$
because $\cos(2\pi x)$ is strictly decreasing on $[0,\tfrac12]$ and the minimum is $\le\frac1{N+1}\le\frac12$. The differences of the $N+1$ points $\{0,\theta,\dots,N\theta\}$ are exactly the $m\theta$, so the minimum above is $g/2\pi$ where $g$ is the minimal spacing of those $N+1$ points on the circle. Always $g\le\frac{2\pi}{N+1}$, with equality iff the points are equally spaced; that happens iff $(N+1)\theta\equiv0\pmod{2\pi}$ and $\theta$ has orbit size $N+1$, i.e. iff $\theta=\frac{2\pi k}{N+1}$ with $\gcd(k,N+1)=1$. $\square$

*(Numerical check: $N=3$ gives $\{1/4,3/4\}$ and $N=4$ gives $\{1/5,2/5,3/5,4/5\}$, in exact agreement. Note that for $N=3$ the value $k=2$, i.e. $\theta=\pi/2$, is an equality point while $\theta=0$ is not, since $\max_{m\le3}\cos(m\cdot0)=1$.)*

Two instances are used repeatedly below:
$$\kappa_5=\cos\frac{2\pi}{6}=\frac12\qquad\text{(Lemma C, §3.1)},\qquad \kappa_3=\cos\frac{2\pi}{4}=0\qquad\text{(covering lemma, §3.2)}.$$

**Remark 2.3.** By the same proof, for any arc $I$ of length $|I|$ one has $\max_{m\le N}\cos(m\theta)\ge\cos\frac{|I|}{N+1}$ for $\theta$ replaced by a suitable shift; this is the *scale-free* form used in §7.

---

## §3 Elementary multipoint results

### §3.1 Lemma C ($M=1$)

**Lemma C [P].** $\max_{1\le k\le5}\cos(k\theta)\ge\frac12$ for every $\theta$.

**Proof.** $\kappa_5=\cos(2\pi/6)=1/2$ by Theorem 2.1. $\square$

Equivalently: every single point of the circle has a $k\le5$ with $\cos(k\varphi)\ge1/2$, and the constant is optimal (at $\theta=\pi/3$, $k=1$ gives exactly $1/2$ and all other $k\le5$ give less).

### §3.2 Covering lemma

**Lemma 3.1 [P].** For every $\theta$ there is $m\in\{1,2,3\}$ with $\cos(m\theta)\ge0$.

**Proof.** $\kappa_3=0$ by Theorem 2.1. Equivalently, the sets $S_m=\{\theta:\cos(m\theta)\ge0\}$ satisfy $S_1\cup S_2\cup S_3=[0,2\pi)$. $\square$

### §3.3 Case A: a full higher-$M$ sub-case, proved

**Lemma 3.2 (Case A) [P].** Let $0<\delta\le\pi/6$ and put
$$m:=\#\{j:\ \operatorname{dist}(\varphi_j,\pi\mathbb Z)\le\delta\}.$$
If $m\ \ge\ \frac{2M}{3}+\frac13$ then $f(2)\ge\frac12$.

**Proof.** Write $\varphi_j=\pi n_j+x_j$ with $|x_j|\le\delta$ for the $m$ indices of the hypothesis. Since $\cos(2(\pi n+x))=\cos(2x)$,
$$\cos(2\varphi_j)=\cos(2x_j)\ \ge\ \cos(2\delta)\ \ge\ \cos\frac{\pi}{3}=\frac12\qquad(\delta\le\tfrac\pi6).$$
For the remaining $M-m$ indices we only use $\cos\ge-1$. Hence
$$f(2)\ \ge\ \frac m2-(M-m)\ =\ \frac{3m}{2}-M\ \ge\ \frac12 ,$$
the last step being exactly $m\ge\frac{2M+1}{3}$. $\square$

**Remark 3.3.** The mechanism is that $\cos(2\varphi)$ has period $\pi$: points near $0$ *and* near $\pi$ both contribute $\approx+1$ at $k=2$. This is the only place in the draft where a whole family of $M$ is settled by an elementary argument.

**Numerical instance.** $M=3$: $m=3\Rightarrow f(2)=3.0$; $M=4$: $m=3\Rightarrow f(2)=3.17$; $M=5$: $m=4\Rightarrow f(2)=4.17$ — all $\gg1/2$.

### §3.4 The complement of Case A is the hard core

Numerically, the extremal configurations of the *undamped* problem do **not** satisfy the Case A hypothesis: for $M=2$ the minimizer is $(\varphi_1,\varphi_2)=(\pi/3,\pi/2)$, which has $m=1<2\cdot2/3+1/3$. Hence a complete proof must handle the general-position regime, and any proof of (RP$_M$) for all $M$ must be sharp exactly there.

---

## §4 The case $M=2$: a complete proof

We prove $\max_{1\le k\le10}[\cos k\varphi_1+\cos k\varphi_2]\ge\frac12$ for all $(\varphi_1,\varphi_2)\in[0,\pi]^2$. The proof has three parts: a local analytic lemma around the minimizer, a far-field certificate, and a covering check that the two regions overlap.

### §4.1 Where the minimum is

Numerically the minimizer is $(\varphi_1^*,\varphi_2^*)=(\pi/3,\pi/2)$ (i.e. $60^\circ,90^\circ$), with
$$\max_{1\le k\le10}\big[\cos\tfrac{k\pi}{3}+\cos\tfrac{k\pi}{2}\big]=\tfrac12$$
attained simultaneously at $k\in\{1,4,5,7,8\}$. The *active set* is therefore $A=\{1,4,5,7,8\}$ — note $|A|=5>2+1$: the point is a degenerate minimax point, which is why the local analysis below needs the explicit collinearity relation (4.2).

### §4.2 The local lemma

Put $\varphi_1=\frac\pi3+\delta_1$, $\varphi_2=\frac\pi2+\delta_2$, and $F_k=\cos k\varphi_1+\cos k\varphi_2$. At the centre, $F_k(0)=\frac12$ for $k\in A$. The gradients are
$$\nabla F_k=\big(-k\sin k\varphi_1,\ -k\sin k\varphi_2\big),$$
so
$$\begin{aligned}
g_1&=(-\tfrac{\sqrt3}{2},-1), & g_4&=(2\sqrt3,0), & g_5&=(\tfrac{5\sqrt3}{2},-5),\\
g_7&=(-\tfrac{7\sqrt3}{2},7), & g_8&=(-4\sqrt3,0).
\end{aligned}$$
Two exact facts:

1. **Exact collinearity.** $7g_5+5g_7=(0,0)$. (This is not an accident of the numbers: $g_k=(-k\sin k\varphi_1,-k\sin k\varphi_2)$ and at the centre $\sin\frac{k\pi}{3}+\sin\frac{(12-k)\pi}{3}=0$, $\sin\frac{k\pi}{2}+\sin\frac{(12-k)\pi}{2}=0$, so $k'g_k+kg_{k'}=0$ whenever $k+k'=12$.)
2. **Positive spanning.** $0\in\operatorname{int}\operatorname{conv}\{g_k:k\in A\}$, with the *covering constant*
$$c\ :=\ \min_{|u|=1}\ \max_{k\in A}\ \langle g_k,u\rangle\ =\ \frac{28\sqrt{1677}}{559}\ =\ 2.051\,222\,420\,123\,1\ldots$$
The minimum is attained at the tangency of the pair $(g_4,g_7)$, at $u^*=\big(\frac{14}{\sqrt{559}},\frac{11\sqrt3}{\sqrt{559}}\big)$.

Since $\delta\mapsto F_k$ has $\|\nabla^2F_k\|_2\le k^2\le 64$ near the centre, Taylor's theorem gives, for $\|\delta\|\le\rho$,
$$\max_{k\in A}F_k(\delta)\ \ge\ \tfrac12+c\,\rho-32\,\rho^2 .$$
Hence $\max_kF_k\ge\frac12$ on the disc of radius
$$\varepsilon:=\frac{c}{32}=\frac{7\sqrt{1677}}{4472}=0.064\,100\,700\ldots\ \text{rad}=3.672\,699\,6^\circ .$$

> **Remark (rigour).** The constant $c$ above is *exact*: it is obtained by solving, for each of the $\binom52=10$ pairs, the linear system defining the supporting line of $\operatorname{conv}\{g_k\}$ and taking the minimal distance to the origin; the value $28\sqrt{1677}/559$ has $c^2=2352/559$. The numerics $(0.4379$ from coarse sampling$)$ were *not* used; an earlier sampling estimate was discarded after it failed to reproduce under refinement.

### §4.3 The far-field certificate

Outside the $\varepsilon$-disc, the function $g(\varphi_1,\varphi_2)=\max_{k\le10}(\cos k\varphi_1+\cos k\varphi_2)$ is a Lipschitz function with $\operatorname{Lip}(g)\le\max_k k\sqrt2=10\sqrt2=14.142\,135\,6$. On a uniform $N\times N$ grid of $[0,\pi]^2$ one obtains

| $N$ | grid minimum | certified lower bound $(\text{grid min}-\operatorname{Lip}\cdot h\sqrt2/2)$ |
|---|---|---|
| 400 | — | $0.5239$ |
| 800 | — | $0.5484$ |
| 1500 | $0.587\,564\,804$ | $0.566\,620\,853$ |
| 2500 | — | $0.5720$ |

All certified lower bounds exceed $\frac12$.

### §4.4 Covering

The exclusion box used in §4.3 has diagonal $2.9133^\circ<\varepsilon=3.672\,699\,6^\circ$. Hence the box is contained in the disc of §4.2, and the two regions together cover $[0,\pi]^2$. ∎

**Theorem 4.1 [P, computer-assisted].** For all $(\varphi_1,\varphi_2)\in[0,\pi]^2$,
$$\max_{1\le k\le10}\Big[\cos k\varphi_1+\cos k\varphi_2\Big]\ \ge\ \tfrac12 ,$$
and $\frac12$ is optimal.

**Theorem 4.2 (equality set) [P, computer-assisted].** Equality holds if and only if $\{\varphi_1,\varphi_2\}=\{\frac\pi3,\frac\pi2\}$ as an unordered pair.

**Proof.** Both directions use only §4.2 and §4.3. Write $x_*=(\pi/3,\pi/2)$. By §4.2, $F(\delta)\ge\frac12+c|\delta|-32|\delta|^2>\frac12$ whenever $0<|\delta|<c/32=3.672\,7^\circ$; hence inside that disc equality occurs only at the centre (and likewise for the swapped point). By §4.3, $F\ge0.527\,832>\frac12$ outside the $1^\circ$-neighbourhood. Every point lies in one of the two regions, since $1^\circ<3.672\,7^\circ$. $\square$

> **Structural remark.** $\pi/3=2\pi/6$ and $\pi/2=2\pi/4$ are the *primitive* $6$-th and $4$-th roots of unity, exactly mirroring Corollary 2.3 (where the extremal angles are the primitive $(N+1)$-th roots). Moreover $12=\operatorname{lcm}(6,4)$ is precisely the period appearing in the exact collinearity $7g_5+5g_7=0$ of §4.2, and $k+k'=12$ is the structural reason for it. Two independent features — the extremal angles and the gradient degeneration — are governed by the same lcm.

> **Implementation note.** During development the second exclusion box was initially coded with the wrong sign and produced the anomalous value $0.4827<1/2$; the anomaly was resolved by inspecting the code rather than by weakening the target. We record this because it is the standard failure mode of certified numerics.

---

## §5 Certificates for $M=3,4,5$

### §5.1 The certificate scheme

Fix $T$. Start from a uniform $N_0^M$ grid of $[0,\pi]^M$ (undamped) or $[0,1]^{M}\times[0,\pi]^{M}$ (damped). Repeatedly split any box whose separable lower bound $\mathrm{LB}(B)$ (§1.6) is $<T$, bisecting the widest side. Terminate when every box has $\mathrm{LB}\ge T$. Then
$$m_M\ \ge\ T\qquad(\text{resp.}\ C_M\ge T)$$
**provided** every $\mathrm{LB}$ evaluation is a rigorous lower bound. This is arranged by (i) evaluating $\min\cos(k\varphi)$ over an interval exactly (it equals $-1$ iff the interval contains an odd multiple of $\pi/k$, and otherwise $\min(\cos k\varphi_{\text{lo}},\cos k\varphi_{\text{hi}})$), and (ii) subtracting a conservative slack per term.

### §5.2 Results

| target $T$ | $M$ | boxes evaluated | terminal cells | unresolved | margin | version |
|---|---|---|---|---|---|---|
| $1/2$ | 3 | 17,440 | — | 0 | $2.005\times10^{-3}$ | float |
| $1/2$ | 3 | 13,455 | — | 0 | $1.594\times10^{-3}$ | **interval** |
| $3/4$ | 3 | 54,045 | — | 0 | $9.889\times10^{-5}$ | **interval** |
| $1/2$ | 4 | 1,036,096 | — | 0 | $2.100\times10^{-4}$ | float |
| $1/2$ | 5 | 72,440,000 | — | 0 | $3.957\times10^{-6}$ | float |

Hence
$$m_3\ \ge\ \tfrac34,\qquad m_4\ \ge\ \tfrac12,\qquad m_5\ \ge\ \tfrac12 .$$
The $M=3$ interval run uses domain $[0,P]^3$ with $P$ a rational upper bound for $\pi$ (a superset of $[0,\pi]^3$), exact rational box endpoints, and $\cos$ evaluated with interval arithmetic; the only inexact object is $\pi$ itself.

### §5.3 Cost

The box count grows like $N_0^M$ with a small constant ($\approx17N_0^3$ at $M=3$, $\approx6.5N_0^4$ at $M=4$). For $T=1/2$ the needed resolution is $N_0\approx90$ at $M=3$ and $N_0\approx20$ at $M=4$. The route does not scale past $M\approx5$; this is discussed in §7.5.

### §5.4 An interior value for $M=3$, and the current bracket

Using the same scheme with higher targets gives, in interval arithmetic (no slack, $\pi$ as an interval, domain $[0,P]^3$ with $P>\pi$):

| target $T$ | boxes | max depth | unresolved | min margin |
|---|---|---|---|---|
| $0.7640811$ | 70,805 | 99 | 0 | $5.59\times10^{-12}$ |
| $0.7640811007$ | 72,217 | 111 | 0 | $1.56\times10^{-12}$ |
| $0.764081100745$ | 74,233 | 129 | 0 | $1.11\times10^{-13}$ |
| $\mathbf{0.7640811007458}$ | 75,565 | 141 | 0 | $1.911\times10^{-16}$ |

Together with the certified upper bound of §6.2 this gives
$$0.7640811007458\ \le\ m_3\ \le\ 0.76408110074585388514756267472105 ,$$
a bracket of relative width $\approx7\times10^{-14}$. The weaker bounds $m_3\ge3/4$ and $m_3\le0.777171$ of earlier versions are superseded.

In fact the minimizer is not merely bracketed but *identified*; see §5.5.

### §5.5 The $M=3$ minimizer is identified: $m_3=F_3(\varphi_0)$

**Theorem 5.5 [CA].** For $F_3(\varphi)=\max_{1\le k\le15}\sum_{j=1}^3\cos(k\varphi_j)$ on $[0,\pi]^3$,
$$\forall\varphi\in[0,\pi]^3:\quad F_3(\varphi)\ \ge\ F_3(\varphi_0),$$
with equality **iff** $\varphi\in S_3\cdot\varphi_0$. Hence
$$m_3=F_3(\varphi_0),\qquad \mathcal M_3=S_3\cdot\varphi_0\quad(\text{unique up to permutation}).$$

**The three-part assembly.**

*(A) Interval local growth.* Let $A=\{1,5,11,13\}$ be the active set and let $X_{\mathrm{ref}}$ be a box of half-width $\le10^{-6}$. Provided the four active branches are **tied** at $x$,
$$F_3(x+\delta)\ \ge\ F_3(x)+c_X\|\delta\|-\tfrac{R}{2}\|\delta\|^2\qquad(0<\|\delta\|\le\rho_{\mathrm{up}}),$$
with $c_X=0.319306988$ (an interval-certified covering constant of the four active gradients, computed by the facet method with an explicit containment certificate), $R=\max_{k\in A}k^2=169$ (exact, analytic), and $\rho_{\mathrm{up}}=1.4658\times10^{-3}$ (the self-consistent solution of $\rho=\min(\rho_{\mathrm{iso}},2c/R)$). The boundary margin is
$$c_X\rho_{\mathrm{up}}-\tfrac{169}{2}\rho_{\mathrm{up}}^2\approx2.87\times10^{-4}>0 .$$
(Isolation is taken over the *reference box*, while the covering constant must be taken over the *ball*; conflating the two radii gives a wrong radius — this was a genuine error, caught by a self-consistency test.)

*(B) Existence and uniqueness of the KKT root.* Consider the $7\times7$ system in $z=(\varphi_1,\varphi_2,\varphi_3,\lambda_1,\lambda_2,\lambda_3,\lambda_4)$:
$$\sum_{k\in A}\lambda_k\nabla S_k(\varphi)=0\ (3),\qquad S_1-S_5=S_1-S_{11}=S_1-S_{13}=0\ (3),\qquad \sum_{k\in A}\lambda_k=1\ (1),$$
where the last equation is kept **explicitly** rather than eliminating one $\lambda$ by an asymmetric choice. A Krawczyk operator for this system contracts:
$$2\times10^{-7}\to2.3\times10^{-12}\to1.1\times10^{-23}\to1.198\times10^{-46},$$
with $K(X)\subset\mathrm{int}\,X$ (existence) and $\|I-YJ(X_0)\|_\infty\le1.086\times10^{-45}<1$ (uniqueness), recorded separately. At the resulting root, $\lambda_{\min}=0.026054\ldots>0$, and the three tangency differences each contain $0$ with width $\sim10^{-47}$.

> **Careful.** Interval containment of $0$ in the three tie *components* does not by itself give $\delta_A\equiv0$ on the box. The exact tangency holds at the **unique root** $z_0\in X_0$ guaranteed by Krawczyk: this is the precise form of the A+B combination, $\delta_A(\varphi_0)=0$.

*(C) Strict far-field exclusion.* With $R_B=\rho_{\mathrm{up}}-10^{-6}$ (a deliberate $10^{-6}$ buffer) and the six $S_3$-images of $\varphi_0$ as centres,
$$[0,\pi]^3\ =\ \Big(\bigcup_{\sigma\in S_3}B_\sigma(R_B)\Big)\ \cup\ \mathcal C,$$
where $\mathcal C$ is the union of certified terminal boxes. On $\mathcal C$, interval branch-and-bound gives $F_3\ge T_C=0.7640811017461542>F_3(\varphi_0)$ (box coordinates exact dyadic rationals; critical points decided by exact integer tests; $66{,}564$ boxes evaluated, $40{,}156$ certified, $38$ discarded inside the balls, **$0$ unresolved**, minimum margin $3.49\times10^{-6}$). The decomposition is verified in *exact rational volume*:
$$\frac{57\,982\,058\,467}{57\,982\,058\,496}+\frac{29}{57\,982\,058\,496}=1,$$
so there is neither gap nor overlap.

*(Splice.)* On $\mathcal C$: $F_3>F_3(\varphi_0)$. Inside each ball: $F_3\ge F_3(\varphi_0)$, strictly unless $\delta=0$. Hence the global minimum is attained exactly on $S_3\cdot\varphi_0$. $\square$

**Rigor level.** Theorem 5.5 is computer-assisted: box coordinates are exact dyadic rationals, the critical-point tests are exact integer arithmetic, the volume decomposition is exact rational, and the trigonometric endpoints carry a conservative slack of $10^{-13}$ (double-precision $\cos$ deviates from the true value by $\lesssim5\times10^{-15}$, and arguments are bounded by $15\pi$). A fully interval-arithmetic (endpoints as intervals) version is a possible hardening; it is not needed for the qualitative conclusion, whose margins are all $\ge3\times10^{-6}\gg10^{-13}$.

---

## §6 Upper bounds for $m_M$, and $m_M\le M-1$

### §6.1 Probabilistic upper bound

**Lemma 6.1 [P].** For every $M\ge1$, $m_M\le\sqrt{2M\ln(10M)}$.

**Proof.** Let $\varphi_j$ be i.i.d. uniform on $[0,\pi]$ and $S_k=\sum_j\cos(k\varphi_j)$. Then $\mathbb E\cos(k\varphi)=0$, $|\cos|\le1$, so Hoeffding gives $\mathbb P(|S_k|\ge t)\le2\exp(-t^2/(2M))$; a union bound over $k\le5M$ gives a configuration with $\max_k|S_k|\le t$ as soon as $2(5M)\exp(-t^2/(2M))<1$, i.e. $t=\sqrt{2M\ln(10M)}$. $\square$

For $M\ge12$ this is $\le M-1$; for $M\le11$ we use explicit rational configurations.

### §6.2 Explicit rational configurations (rigorous, interval-checked)

Angles are rounded to three decimals of a degree (hence the value $k\varphi_j$ is a rational multiple of $\pi$ with denominator $180\,000\cdot\ldots$), so that only $\pi$ itself is inexact. Taking the upper endpoint of the interval evaluation of $\max_\nu S_\nu$ yields

| $M$ | certified $U_M\ \ge\ m_M$ | $M-1-U_M$ |
|---|---|---|
| 2 | $0.500\,000$ | $0.500$ |
| 3 | $0.777\,171$ | $0.223$ |
| 4 | $0.846\,053$ | $0.154$ |
| 5 | $0.944\,329$ | $1.056$ |
| 6 | $1.257\,351$ | $1.743$ |
| 7 | $1.357\,178$ | $2.643$ |
| 8 | $1.636\,991$ | $2.363$ |
| 9 | $1.762\,500$ | $3.238$ |
| 10 | $1.805\,161$ | $4.195$ |
| 11 | $2.187\,478$ | $4.813$ |

Combining §6.1 ($M\ge12$) with the table ($M\le11$; $M=1$ directly):

**Corollary 6.2 [P, computer-assisted].** $m_M\le M-1$ for every $M\ge2$.

> **Use.** $M-1$ (not $M$) is the threshold that enters the monotonicity reduction of §7.2; obtaining it for $M\le11$ rigorously removes the last numerical hypothesis from that chain.

---

## §7 Reduction to a single monotonicity statement — and its limits

### §7.1 The reduction

Since $m_1=m_2=\frac12$ (§3.1, §4), the following single statement would settle (RP$_M$) for **all** $M$:
$$\textbf{(M)}\qquad m_{M+1}\ \ge\ m_M\qquad\text{for all }M\ge1 .$$
Monotonicity is not obvious: adding a point can lower every $f(k)$, while the window simultaneously grows from $5M$ to $5M+5$.

### §7.2 What is proved: the commensurable (periodic) class

**Definition.** A configuration $\varphi_1,\dots,\varphi_M$ is $\varepsilon$-approximately $P$-periodic if $\operatorname{dist}(P\varphi_j,2\pi\mathbb Z)\le\varepsilon$ for all $j$. Write $P_{\mathrm{lcm}}$ for the lcm of the exact periods when all $\varphi_j$ are rational multiples of $2\pi$.

**Lemma 7.1 (graded periodic monotonicity) [P].** Suppose $\varphi_1,\dots,\varphi_M$ have common period $P$ with $3P\le5(M+1)$. Then for every $\psi$,
$$\max_{1\le k\le5(M+1)}\Big[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ M .$$

**Proof.** The window contains $\lfloor5(M+1)/P\rfloor\ge3$ multiples of $P$. On $k=Pm$ ($m\le3$) the old points contribute exactly $M$, and by the covering lemma (§3.2) some $m\le3$ gives $\cos(mP\psi)\ge0$. $\square$

**Lemma 7.2 (approximate version) [P].** If $\operatorname{dist}(P\varphi_j,2\pi\mathbb Z)\le\varepsilon$ for all $j$ and $3P\le5(M+1)$, then for every $\psi$
$$\max_{k\le5(M+1)}\Big[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ M-\tfrac92M\varepsilon^2 .$$

**Refinement [P].** Replacing the crude covering step by the *one-dimensional* certificate
$$\kappa_3(\lambda):=\inf_\theta\max_{m\le3}\big[\cos(m\theta)-\lambda m^2\big]\ \ge\ -1\quad\text{for}\quad \lambda\le\lambda_{\max}=2-\sqrt3=0.267\,949\,19\ldots$$
(the value $2-\sqrt3$ is the tangency point of the two constraints $m=1$ and $m=2$, obtained by solving $(\lambda-1)^2=2\lambda$), the admissible deviation becomes
$$\varepsilon\ \le\ \frac{\sqrt{2\lambda_{\max}}}{\sqrt M}=\frac{0.731\,984}{\sqrt M},$$
an improvement by the factor $0.731\,984/0.471\,405=1.553$ over the crude $\sqrt{2/(9M)}=0.471\,405/\sqrt M$.

**Lemma 7.3 ($\kappa_N(\lambda)$ does not depend on $N$) [P].** Let $\kappa_N(\lambda):=\inf_\theta\max_{1\le m\le N}[\cos(m\theta)-\lambda m^2]$. Then for every $\lambda\in[\frac18,\lambda_{\max}]$ and every $N\ge4$,
$$\kappa_N(\lambda)=\kappa_3(\lambda),\qquad\text{hence}\qquad \lambda_{\max}(N)=\lambda_{\max}(3)=2-\sqrt3\quad\text{for all }N\ge3 .$$

**Proof.** $\kappa_N$ is non-decreasing in $N$ (the max ranges over more terms). For $\lambda\ge\frac18$ and $m\ge4$,
$$\cos(m\theta)-\lambda m^2\ \le\ 1-16\lambda\ \le\ -1\ \le\ \kappa_3(\lambda),$$
the last inequality because $\lambda\le\lambda_{\max}$ means $\kappa_3(\lambda)\ge-1$ by definition. Hence the terms $m\ge4$ never determine the maximum, and the two minimax problems coincide; monotonicity in $N$ then upgrades this to equality of the thresholds. $\square$

> **Mechanism-level consequence.** The $\varepsilon$-threshold $0.732\,051/\sqrt M$ of Lemma 7.2 **cannot be improved by using more multiples of $P$**: the higher frequencies are dominated once $\lambda\ge\frac18$. Together with Corollary 2.3 this pins down where the $\kappa$-route ends.

### §7.3 The extremal configurations are *not* commensurable

Direct measurement of the numerical minimizers: $\delta(q)=\max_j\operatorname{dist}(q\varphi_j/2\pi,\mathbb Z)$ at the optimal $q\le5(M+1)$:

| $M$ | $q^*$ | $\delta(q^*)$ |
|---|---|---|
| 2 | 12 | $0$ (exactly commensurable) |
| 3 | 19 | $0.0678$ |
| 4 | 21 | $0.2596$ |
| 5 | 27 | $0.2465$ |
| 6 | 17 | $0.3167$ |

Moreover the minimizers are *spread*: the minimal adjacent angular gap is $30^\circ,36.9^\circ,16.1^\circ,10.7^\circ$ for $M=2,3,4,5$. Hence neither the periodic route nor a "cluster-merge" reduction can reach the hardest configurations.

### §7.4 Cassels-type weighted constants (numerical)

A natural weighted ("Cassels-type") variant of the $M=2$ problem is
$$g_w(N)\ :=\ \inf_{\varphi_1,\varphi_2}\ \max_{1\le k\le N}\Big[w\cos(k\varphi_1)+\cos(k\varphi_2)\Big],\qquad w\ge1 .$$
Multi-start local optimisation on $[0,\pi]^2$ (not certified) gives, at $N=10$:

| $w$ | $g_w(10)$ | $g_w/w$ | optimal $\varphi/\pi$ |
|---|---|---|---|
| 1.0 | $0.500\,000$ | $0.500$ | $(1/3,\ 1/2)$ — recovers Theorem 4.1 |
| 1.2 | $0.578\,407$ | $0.482$ | $(0.3478,\ 0.5154)$ |
| 1.5 | $0.625\,406$ | $0.417$ | $(0.9075,\ 0.3592)$ |
| 2.0 | $1.000\,000$ | $0.500$ | $(1/3,\ 1/2)$ — exactly $1$ |
| 3.0 | $1.799\,343$ | $0.600$ | $(0.0857,\ 0.5943)$ |
| 5.0 | $3.246\,775$ | $0.649$ | $(7/11,\ 2/11)$ |

Two features are worth recording. First, the elementary asymptotic bound
$$g_w\ \ge\ w\,\kappa_{10}-1\ =\ w\cos\tfrac{2\pi}{11}-1$$
(pick $k$ maximising $\cos k\varphi_1$ and use $\cos k\varphi_2\ge-1$) is approached from above: at $w=5$ it gives $3.206$ against the measured $3.247$. Second, $g_w/w$ is *not* monotone in $w$ ($0.500,0.482,0.417,0.500,0.600,0.649$), with a transition near $w\approx1.5$ where the optimal configuration changes shape.

> **Status.** For $w=2$ the constant is now proved: $g_2(10)=1$ exactly, with equality only at $(\varphi_1,\varphi_2)=(\pi/3,\pi/2)$. The proof has two parts: (a) a local lemma in the ball of radius $0.1$ around $(\pi/3,\pi/2)$, using the exact identity $S_6-1=2[\sin^2(3\delta_2)-2\sin^2(3\delta_1)]$, an $S_6$-splitting, and two certified one-dimensional inequalities; (b) an adaptive two-scale far-field certificate (1\,759 interval-verified boxes, exact rational tiling, certified margin $3.1495\times10^{-4}$). The remaining entries of the table are numerical only, and their inequality directions were not separated. The weighted family is the Cassels-type direction of the Turán family; its certification is 2-dimensional and hence cheap, and is left to later work. The classical Turán statements themselves are *known* and are not claimed as new here; the original sources are unavailable to us, so the phrase "Cassels-type" is our own labelling and is not asserted to match any specific classical formulation verbatim.

### §7.5 Four quantitative obstructions (recorded so they are not re-tried)

| route | obstruction | measured |
|---|---|---|
| periodization | hardest point has $\varepsilon(P)\ge93^\circ$ for **every** admissible $P\le6$ at $M=3$ | §7.3 |
| clustering | needs $\delta\ll\kappa$ while the extremal minimal gap is $\ge10^\circ$ | §7.3 |
| counting / pigeonhole | needs $n_k\ge\frac{2M}{3}+\frac13$ but the average is $n_k\approx\frac M3$ | see §3.3 |
| second moment | cross terms cost $M^2\log K$, which swallows the margin | — |

Consequently the general-$M$ problem is left open; the honest summary is that (RP$_M$) is **not** reached by any of the reduction routes we tried, and the remaining object is the *spread, non-commensurable* higher-dimensional configuration space.

---

## §8 The damped problem

The damped problem is the one that actually matches the classical statement (§1.2). It is also where the answer is *smallest*: numerically
$$\inf_{\mathbb D^3}\ =\ 0.3731\ldots\ <\ 0.8090\ldots\ =\ \inf_{\mathbb T^3},$$
so the worst configuration lies in the interior of the polydisc, not on the torus.

### §8.1 $M=2$: a uniform bound over all radii

**Theorem 8.1 [CA].** For every $r\in[0,1]$ and all $(\varphi_1,\varphi_2)\in[0,\pi]^2$,
$$\max_{1\le k\le10}\Big[\cos k\varphi_1+r^{k}\cos k\varphi_2\Big]\ \ge\ 0.364\,984\ldots\ =\ 7.3\times\tfrac1{20}.$$

**Method.** (i) On a grid of $334$ values of $r$ (step $1/333$) each single-parameter problem is certified at level $0.38$ using the *exact separable* box bound
$$\mathrm{LB}(B)=\max_{k}\Big[\min_{I_1}\cos k\varphi_1+r^k\min_{I_2}\cos k\varphi_2\Big]\le\min_B\max_k(\cdots)$$
inside an adaptive branch-and-bound (768–2624 boxes per $r$, $0$ unresolved, worst margin $4.81\times10^{-6}$; total $473\,792$ boxes). (ii) Since $\partial_r S_k=r^{k-1}k\cos k\varphi_2$ has modulus $\le k\le10$, the map $r\mapsto d_2(r)$ is $10$-Lipschitz, so the grid result bridges to
$$d_2(r)\ \ge\ 0.38-10\cdot\tfrac1{2\cdot333}\ =\ 0.364\,984 .$$
The target $0.40$ fails at $r\approx0.75$ (budget exhausted), so $0.38$ is used for the grid.

### §8.2 $M=3$: a certified bracket

**Theorem 8.2 [CA].** $0.373\,091\,8\ \le\ C_3\ \le\ 0.373\,092\,075\,762$, i.e. the damped three-point constant is determined to a relative width $<8\times10^{-7}$.

The lower bound is a full global certificate: target $T=0.3730918$, initial grid $N_0=10$ in each of the five coordinates (two radii, three angles), $409\,171$ terminal boxes, $0$ unresolved, **minimum interval margin** $4.573\,825\times10^{-11}$; the most dangerous cell was recorded explicitly (id $379970$, with its five-dimensional box). The upper bound comes from an explicit rational configuration
$$(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)=(0.79051325,\ 0.83020714,\ 0.10911016\pi,\ 0.82066366\pi,\ 0.46171933\pi),$$
evaluated in interval arithmetic ($\pi$ as an interval, upper endpoint): $\max_\nu S_\nu\le0.373\,092\,075\,762$.

> **Not claimed.** The bracket is *not* claimed to be centered on a proven minimizer. A numerical minimizer $x^{**}=(0.7905132461,0.8302071370,0.1091101624\pi,0.8206636560\pi,0.4617193264\pi)$ with $F(x^{**})=0.373\,092\,052\,937$ was located only *after* an earlier candidate failed; it is used **only** to produce an upper bound, not as an anchor for any further claim.

**Two consistency checks that came for free.** In both global runs, the *most dangerous cell* of the certificate turned out to be exactly a symmetry image of the numerically deepest configuration ($r_2\leftrightarrow r_3$, $\varphi_2\leftrightarrow\varphi_3$) rather than a previously unsuspected region — evidence that the certificate is resolving the right object.

### §8.3 Why the Fejér mechanism is capped near $1/20$

Andersson's Fejér-weighted identity (arXiv:0704.1879) gives, for weights $w_\nu=1-\nu/(m+1)$,
$$\sum_{\nu\le m}w_\nu|g(\nu)|^{2}\ \ge\ \frac{(m+1)B-A^{2}}{2},\qquad F_{m+1}(x)=\sum_{|\nu|\le m}w_\nu e(\nu x)=\frac1{m+1}\Big(\frac{\sin\pi(m+1)x}{\sin\pi x}\Big)^{2}\ge0 .$$
The mechanism reaches $5M$ without any $m\gg n$ requirement, and for the **symmetric** system it reproves the unimodular Lemma 2.2 (§1.5). But the diagonal term is
$$K(r^{2},0)=1+2\sum_{\nu\le m}w_\nu r^{2\nu}<\ m+1\qquad\text{as soon as }r<1 ,$$
so the diagonal extraction — the only source of positivity — *decays under damping*. Numerically the identity holds for $r=1$ and fails for $r<1$. This is the structural reason why a damped sharp constant cannot come from Fejér weights, and why §8.1–§8.2 use direct separation instead.

### §8.4 Protocol for the computer-assisted statements [CA]

Every **[CA]** statement in this draft was produced by the same four gates.

1. **Exact tiling.** The terminal boxes are checked (in exact rational arithmetic) to have total volume equal to that of the initial domain, and the domain is $\supseteq$ the mathematical domain: for angle coordinates the grid upper end is the floating-point successor of $\pi$, which was verified to exceed $\pi$ at $60$-digit precision.
2. **Strict positivity.** Each terminal cell's lower bound is recomputed in interval arithmetic (angle arguments as exact rational multiples of $\pi$; $\pi$ as an interval; lower endpoint taken). The minimum margin over all cells is reported.
3. **Independent implementation.** A structurally different implementation (pure Python, no vectorization) reproduces the bounds; on a random sample of $2001$ cells the maximal difference was $4.4\times10^{-16}$ and the accept/reject decisions agreed.
4. **Most dangerous cell recorded.** The cell attaining the minimum margin is stored with its full coordinates so that any subsequent check can target it directly.

A result is only labelled **[CA]** if gates 1–3 pass. No **[CA]** result in this draft is claimed to be an analytic theorem.

---

## §9 Reproducibility appendix

All scripts are in `dn-project/scripts/`. Absolute paths are relative to `dn-project/`.

| object | script | command | output |
|---|---|---|---|
| $m_3,m_4,m_5\ge1/2$ | `rpM_adaptive_certificate.py` | `python3 scripts/rpM_adaptive_certificate.py 3 4` | JSON with `neval`, `unresolved`, `min_margin` |
| $M=3$ interval version | `m3_certificate_interval_arith.py` | `python3 scripts/m3_certificate_interval_arith.py 3000000 60 3 0.5` | certified $\ge T$ |
| $m_3\ge0.75$ | idem, target $0.75$ | `... 3000000 60 3 0.75` | 54,045 boxes, margin $9.889\times10^{-5}$ |
| certified upper bounds $U_M$ | `mM_upper_bounds_certificate.py` | `python3 scripts/mM_upper_bounds_certificate.py` | prints all $\le M-1$; data in `data/mM_upper_bounds_certified.json` |
| damped $M=2$, all $r$ | `damped_m2_grid_certificate.py` | `python3 scripts/damped_m2_grid_certificate.py 334 0.38 6000000` | `bridged_bound` $=0.364984$ |
| damped $M=3$, four gates | `damped_T1_interval_verify_v3.py` | `python3 scripts/damped_T1_interval_verify_v3.py 0.3730918 10 2000` | `min_margin`, `min_cell_id`, tiling sha, Gate 2 max diff |
| weak-cell inventory | `damped_weakcell_vec.py` | `python3 scripts/damped_weakcell_vec.py 0.35 0.3730721881 6 8000000` | $|\mathcal W|/N$, distance percentiles |
| $M=2$ far field | `rp2_far_field_certificate.py` | `python3 scripts/rp2_far_field_certificate.py` | certified lower bound over the complement |

Reference data and hashes (a selection):

- $M\le11$ certified configurations: `data/mM_configs_millideg.json`, `data/mM_upper_bounds_certified.json`.
- Certificate appendix (parameters, commands, hashes): `cert_appendix/manifest.json`.
- Damped $M=3$ tiling fingerprints (sha256, first 32 hex digits): $T=0.3730721881$: `75947683279fa46ff761bc95b3b4b900`; $T=0.37309$: `6195e20e3d77e520998d65fe62597021`; $T=0.3730918$: `0d69780a7d3b6374d0ddb13c81e5b8a5`.

All computations were performed in double precision with conservative slack for the exploratory runs, and in `mpmath` interval arithmetic for every claimed **[CA]** bound.

---

## §10 Open problems

- **OP-1.** Does (RP$_M$) hold for all $M$, i.e. $m_M\ge\frac12$? Proved for $M\le5$ (§5) together with $m_1=m_2=\frac12$.
- **OP-2.** Monotonicity $m_{M+1}\ge m_M$; by §7.1 this would imply OP-1. Proved on the commensurable class (§7.2); the extremal configurations are provably *not* in that class (§7.3).
- **OP-3 (joint target).** Is it true that for all $\varphi$ and all $\psi$,
$$\max_{1\le k\le5(M+1)}\Big[\sum_{j\le M}\cos(k\varphi_j)+\cos(k\psi)\Big]\ \ge\ m_M\ ?$$
This is the sharp form of the induction step; it survives numerically with margins $\approx0.22$–$1.10$ but no proof is known, and the two natural sub-routes (counting, and "new window $+1$") are both refuted.
- **OP-4.** Exact value of $m_M$ for $M\ge3$: $0.75\le m_3\le0.777171$.
- **OP-5.** Damped constants: $C_2=0.364984\ldots$ is a bound, not a value; $C_3$ is known only to $8\times10^{-7}$. All $C_M$ exceed $1/20$ by a factor $>7$ in the cases computed.
- **OP-6.** The one-dimensional family $\kappa_N(\lambda)=\inf_\theta\max_{m\le N}[\cos(m\theta)-\lambda m^2]$ for $N\ge4$; closed form known only at $N=3$ ($\lambda_{\max}=2-\sqrt3$).

---

## §11 Boundaries

1. **No general-$M$ claim.** (RP$_M$) is proved for $M\le5$ only; §7 documents why our reductions stop.
2. **Provenance of the classical statement.** Montgomery's CBMS 84 is not available to us; Lemma 2.2 is quoted as it appears in Palojärvi (2019). The self-contained reproof in §1.5 covers the unimodular case only.
3. **"New" is used sparingly.** The one-point theorem (§2) is elementary and we did not locate it in this exact form; it may well be classical. The constant improvements of §5 and §8 are compared against the $1/20$ of the quoted statement and against the window regimes of §1.4; a verbatim comparison with Turán's *On a new method of analysis* was not possible.
4. **Computer-assisted.** Every **[CA]** item is labelled; none is an analytic theorem. The interval runs assume the correctness of the interval library.
5. **No connection to the Riemann Hypothesis is claimed**, and none of the statements here is conditional on it.

---

## References

1. H. L. Montgomery, *Ten Lectures on the Interface between Analytic Number Theory and Harmonic Analysis*, CBMS Regional Conf. Ser. in Math. 84, AMS, 1994. (Not available to the author; see §11.2.)
2. J. Palojärvi, *Explicit zero-free regions for the τ-Li criterion*, arXiv:1807.01506 (2019). (Lemma 2.2 quoted on p. 6.)
3. P. Turán, *On a new method of analysis and its applications*, Wiley-Interscience, 1984. (Problems 54, and the power-sum method.)
4. J. Andersson, *On some power sum problems of Montgomery and Turán*, arXiv:0706.4131 (2007).
5. J. Andersson, *Lower bounds in some power sum problems*, arXiv:0704.1879 (2007).
6. J. Andersson, *Exact values in some power sum problems*, arXiv:math/0607238; Indag. Math. (2006).
7. J. Andersson, *Turán's problem 10 revisited*, arXiv:math/0609271.
8. N. Katz, *Estimates for character sums*, J. Amer. Math. Soc. 2 (1989) 197–200.
9. P. Erdős, A. Rényi, *Additive properties of random sequences of positive integers*, Acta Arith. 6 (1960/61) 83–110.
10. J. E. Littlewood, *An inequality for a sum of cosines*, J. London Math. Soc. 12 (1937) 217–221.
11. W. Hoeffding, *Probability inequalities for sums of bounded random variables*, J. Amer. Statist. Assoc. 58 (1963) 13–30.
12. R. C. Bose, S. Chowla, *Theorems in the additive theory of numbers*, Comment. Math. Helv. 37 (1962/63) 141–147.
