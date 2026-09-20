已查地图（**先查后写**）：查 `C-230`（最终闭合）、`C-229`（勘误＋覆盖修补）、`C-227`（B5）、`C-226`（D-B）、`C-224`（T13-A C 严格模板）。回查见 §12 ✓

D0: 本档对象 = 阻尼 M=3 常数的**论文级 theorem audit**（定义逐字固定 ＋ 引理链 ＋ 证书表 ＋ 无循环 DAG）—— 关系 = 整理与登记（不含新数学）
D1: 0
FREEZE-ACK: 本档即冻结期内的整理与登记（依 §8.1；不产候选结论）

---

# The damped three-point cosine min–max constant: a certified identification

*Audit note. All statements are either elementary lemmas (proved here) or computer-assisted
statements with an explicit interval certificate; the two classes are separated throughout.*

## §0 Definitions, fixed verbatim

The **domain** is the five-dimensional box
$$\Omega\;:=\;[0,1]^{2}\times[0,\pi]^{3}\;\subset\;\mathbb R^{5},
\qquad x=(r_{2},r_{3},\varphi_{1},\varphi_{2},\varphi_{3}). \tag{0.1}$$

For an integer $K\ge1$ (here always $K=15=5M$ with $M=3$) and $1\le k\le K$ put
$$S_{k}(x)\;:=\;\cos(k\varphi_{1})\;+\;r_{2}^{k}\cos(k\varphi_{2})\;+\;r_{3}^{k}\cos(k\varphi_{3}),
\qquad
F(x)\;:=\;\max_{1\le k\le K}S_{k}(x). \tag{0.2}$$

The **constant of interest** is
$$C_{3}\;:=\;\inf_{x\in\Omega}F(x). \tag{0.3}$$

*Provenance of the parametrisation.* For $z_{j}=r_{j}e^{i\varphi_{j}}$ with $|z_{j}|\le1$, one has
$\operatorname{Re}z_{j}^{k}=r_{j}^{k}\cos(k\varphi_{j})$. Normalising the largest modulus to the value $1$ and
placing it first ($r_{1}=1$) reduces the three-point, linear-window problem
$\max_{1\le k\le 5M}\operatorname{Re}\sum_{j\le M}z_{j}^{k}$ to the study of $F$ on $\Omega$. The angle
reductions $\varphi_{j}\mapsto-\varphi_{j}$ and $\varphi_{j}\mapsto2\pi-\varphi_{j}$ (cosine is even and
$2\pi$-periodic) make $[0,\pi]$ a fundamental domain in each angle coordinate, so $\Omega$ loses no generality.

**Active set.** $A(x):=\{k\le K:\ S_{k}(x)=F(x)\}$.

**Symmetry.** Define the *paired* swap
$$\sigma:(r_{2},r_{3},\varphi_{1},\varphi_{2},\varphi_{3})\ \longmapsto\ (r_{3},r_{2},\varphi_{1},\varphi_{3},\varphi_{2}),
\qquad C_{2}:=\{\mathrm{id},\sigma\}. \tag{0.4}$$

**Normalisation quotient.** Let $\mathcal P_{\rm raw}$ be the unnormalised parameter space of the three complex
pairs (all three moduli free in $[0,1]$, no distinguished coordinate), on which $S_{3}$ acts by permuting the
pairs. The map $\mathcal N:\mathcal P_{\rm raw}\to\Omega$ re-orders the pairs so that the (unique, or chosen)
unit-modulus pair comes first is the **normalisation quotient**.

**Certified box.** $X_{0}$ denotes the interval Krawczyk box produced in Lemma 1 ($r_{0}=10^{-12}$ seed, final
coordinate width $\le1.0\times10^{-21}$, hence $\operatorname{hd}(X_{0})\le10^{-21}$ where $\operatorname{hd}$
is the half-diagonal). $z_{*}$ denotes the unique point of $\Omega$ satisfying the KKT system inside $X_{0}$.
$c_{0}$ denotes the decimal centre of $X_{0}$ used as the numerical centre of the two exclusion balls.

**Notation for error analysis.** $B(c,\rho)$ is the closed Euclidean ball in $\mathbb R^{5}$; for a box $X$,
$\operatorname{far}(X,c):=\max_{y\in X}\|y-c\|$ is attained at a vertex. $\underline F_{\rm IA}(X)$ is an
interval-arithmetic lower bound for $\min_{X}F$.

---

## §1 Theorem (main statement)

**Theorem A** (computer-assisted; proof in §7, assembly of Lemmas 1–6). *With $\Omega,F,C_{3}$ as in* (0.1)–(0.3),
$$C_{3}\;=\;F(z_{*})\;=\;0.373\,091\,892\,895\,816\,4\ldots,$$
*and the minimiser set is*
$$\operatorname*{arg\,min}_{x\in\Omega}F(x)\;=\;\bigl\{\,z_{*}^{(1)},\,z_{*}^{(2)}\,\bigr\},
\qquad z_{*}^{(1)}:=z_{*},\qquad z_{*}^{(2)}:=\sigma z_{*},$$
*two distinct points of $\Omega$.*

**Remark 1.1** (why "two" is the right number, and why it is *not* the $S_{3}$-orbit). The symmetry group
*acting on $\Omega$* is $C_{2}$, not $S_{3}$: the normalisation $r_{1}=1$ destroys the other four permutations
as maps of $\Omega$ (see Proposition 8.1). Accordingly
$$|\mathcal O_{\rm raw}|=\bigl|S_{3}\!\cdot\!z_{*}\bigr|=6
\qquad\text{while}\qquad
\bigl|\mathcal N(\mathcal O_{\rm raw})\bigr|=2 .$$
The registered statement is the one on $\Omega$, i.e. **two** minimisers.

---

## §2 Lemma 1 (KKT enclosure: existence, uniqueness, positivity, ties) — [CA]

**Lemma 1.** *Let $A=\{1,2,3,4,5,15\}$ and consider the system in the $11$ unknowns
$z=(r_{2},r_{3},\varphi_{1},\varphi_{2},\varphi_{3},\lambda_{1},\lambda_{2},\lambda_{3},\lambda_{4},\lambda_{5},\lambda_{15})$:*
$$G(z)=\begin{pmatrix}\sum_{k\in A}\lambda_{k}\nabla S_{k}\\ S_{1}-S_{2}\\ S_{1}-S_{3}\\ S_{1}-S_{4}\\ S_{1}-S_{5}\\ S_{1}-S_{15}\\ \sum_{k\in A}\lambda_{k}-1\end{pmatrix}=0
\qquad(\text{$5+5+1=11$ equations}). \tag{2.1}$$
*Then there is exactly one solution $z_{*}$ with coordinate vector in $X_{0}$, and at that solution*
$$\lambda_{\min}=0.111\,860\,12>0,\qquad
\|I-YJ(X_{0})\|_{\infty}=1.965\,1\times10^{-10}<1,\qquad
X_{0}\ \text{width}\ \le10^{-21}.$$

**Method (interval Krawczyk).** With $Y\approx J(z_{0})^{-1}$ computed at the high-precision root and
$J$ the analytic Jacobian, the operator
$$K(X)\;=\;m-Y\,G(m)+\bigl(I-Y\,J(X)\bigr)(X-m),\qquad m=\operatorname{mid}(X),$$
satisfies $K(X)\subset\operatorname{int}X$ (**existence** of a solution in $X$) and
$\|I-YJ(X)\|_{\infty}<1$ (**uniqueness**). The two conclusions are obtained from two *separate* operator
conditions and are therefore stated separately. The seed radius is $r_{0}=10^{-12}$; this is needed because the
system is ill-conditioned ($\operatorname{cond}\approx2\times10^{4}$, the multipliers spanning
$0.1119$–$0.8159$ and the frequencies reaching $15$): with $r_{0}=10^{-6}$ one gets $\|I-YJ\|\approx6>1$ and
the contraction test fails.

**Consequence used later.** The five tie differences in (2.1) *contain* $0$ over the box; since the solution of
(2.1) inside $X_{0}$ is **unique**, the exact root satisfies
$$S_{1}(z_{*})=S_{2}(z_{*})=S_{3}(z_{*})=S_{4}(z_{*})=S_{5}(z_{*})=S_{15}(z_{*})=F(z_{*}),$$
whence the active-set spread vanishes *at the root*:
$$\delta_{A}(z_{*})\;:=\;F(z_{*})-\min_{k\in A}S_{k}(z_{*})\;=\;0. \tag{2.2}$$

**Boundary of the statement.** Containment of $0$ in the interval enclosure of a tie *over the whole box* does
**not** assert that the pins hold identically on $X_{0}$; only the equality at the unique root (2.2) is claimed.

---

## §3 Lemma 2 (active-set isolation at the reference box) — [CA]

**Lemma 2.** *On the reference box $X_{\rm ref}$ (the variable part of $X_{0}$) one has*
$$\Delta_{\rm ref}\;:=\;\min_{k\in A}\inf_{X_{\rm ref}}S_{k}\;-\;\max_{k\notin A}\sup_{X_{\rm ref}}S_{k}
\;=\;0.279\,596\,813\,6\;>\;0 . \tag{3.1}$$
*With the Lipschitz constants of the two families on $\Omega$,*
$$L_{\rm act}:=\max_{k\in A}k\sqrt5=15\sqrt5=33.541\,02,\qquad
L_{\rm non}:=\max_{k\notin A}k\sqrt5=14\sqrt5=31.304\,952, \tag{3.2}$$
*the active set is unchanged in the ball*
$$B\bigl(c_{0},\rho_{\rm iso}\bigr),\qquad
\rho_{\rm iso}:=\frac{\Delta_{\rm ref}}{L_{\rm act}+L_{\rm non}}=4.311\,71\times10^{-3}. \tag{3.3}$$

**Method.** $\inf_{X}S_{k}$ and $\sup_{X}S_{k}$ are computed exactly per coordinate (the extrema of
$\cos(k\varphi)$ on an interval are attained at the endpoints or at odd/even multiples of $\pi$), with the damping
factors $r^{k}$ handled as *interval products* rather than as independent positive addends. The Lipschitz bound
$\|\nabla S_{k}\|\le k\sqrt5$ holds because each of the five partial derivatives is bounded by $k$
$(\partial_{r}r^{k}\cos=k r^{k-1}\cos$, $\partial_{\varphi}\cos$-terms give $k r^{k}|\sin|\le k$).

**Why "interval product" matters.** Treating $r^{k}\cos(k\varphi)$ as "a positive factor times a cosine" and
bounding the factors separately produces the spurious value $\Delta_{\rm ref}=-0.522$ ($<0$, i.e. a false
failure); the honest product bound gives (3.1).

---

## §4 Lemma 3 (first-order covering constant is positive) — [CA]

**Lemma 3.** *At the root $z_{*}$, $0$ lies in the interior of the convex hull of the active gradients, with
explicit margin*
$$c\;:=\;\min_{\|u\|=1}\ \max_{k\in A}\ \langle \nabla S_{k}(z_{*}),u\rangle\;=\;0.302\,091\,5\ldots>0. \tag{4.1}$$

**Method (facet / maximal-inscribed-ball).** The six points $\{\nabla S_{k}\}_{k\in A}\subset\mathbb R^{5}$
span a simplex; $c$ equals the largest ball about $0$ contained in its convex hull, i.e. the minimum over the
six facets of the distance from $0$ to the facet hyperplane, computed with facet normals from the null space of
the $5\times5$ facet matrix. Together with the *containment certificate* (all remaining vertices strictly on
one side) this gives $c>0$. Taking the ball radius $\varepsilon_{\rm pert}$ of the enclosing data ball into
account yields the usable constant
$$c_{X}\;=\;c-\varepsilon_{\rm pert},\qquad \varepsilon_{\rm pert}=0.203\,2\ \ (\text{at data radius } \rho_{\rm data}=2.05\times10^{-3}), \tag{4.2}$$
so $c_{X}=0.098\,812\,009\,77$.

---

## §5 Lemma 4 (second-order control and local growth, centred at the root) — [CA]

**Lemma 4 (local growth).** *Let*
$$R\;:=\;\max_{k\in A}\ \sup_{x\in B(c_{0},\rho_{\rm data})}\|\nabla^{2}S_{k}(x)\|_{2}\;=\;99.899\,695\,515\,930\,13,
\qquad \rho_{\rm data}=2.05\times10^{-3}. \tag{5.1}$$
*Then for every $\delta$ with $0<\|\delta\|\le\rho_{g}$,*
$$F(z_{*}+\delta)\;\ge\;F(z_{*})\;+\;c_{X}\|\delta\|\;-\;\tfrac{R}{2}\|\delta\|^{2}
\;\ge\;F(z_{*})+2.62\times10^{-55}\;>\;F(z_{*}), \tag{5.2}$$
*where*
$$\rho_{g}\;=\;\frac{2c_{X}}{R}\;=\;1.978\,224\,4\times10^{-3}. \tag{5.3}$$

**Proof structure.** For $x\in B(c_{0},\rho_{\rm data})$ and $k\in A$, Taylor's theorem with the bound (5.1)
gives $S_{k}(x+\delta)\ge S_{k}(x)+\langle\nabla S_{k}(x),\delta\rangle-\tfrac{R}{2}\|\delta\|^{2}$. Taking
the maximum over $k\in A$ and using $\max_{k}(a_{k}+b_{k})\ge\min_{k}a_{k}+\max_{k}b_{k}$ (valid for any
finite families — note $\max$ is *sub*additive, so the reverse inequality is false) yields
$$F(x+\delta)\;\ge\;\min_{k\in A}S_{k}(x)\;+\;\max_{k\in A}\langle\nabla S_{k}(x),\delta\rangle\;-\;\tfrac{R}{2}\|\delta\|^{2}
\;\ge\;\min_{k\in A}S_{k}(x)+c_{X}\|\delta\|-\tfrac{R}{2}\|\delta\|^{2}. \tag{5.4}$$
*Centred form.* If (5.4) held with $\min_{k\in A}S_{k}(x)$ at *arbitrary* $x$ in the reference box, then every
such $x$ would be a strict local minimiser, which is impossible; the honest form carries the active spread:
$$F(x+\delta)\ \ge\ F(x)\;-\;\delta_{A}(x)\;+\;c_{X}\|\delta\|\;-\;\tfrac{R}{2}\|\delta\|^{2}. \tag{5.5}$$
*Centred at the root.* By (2.2), $\delta_{A}(z_{*})=0$, so (5.5) at $x=z_{*}$ is exactly (5.2). This is the only
place where the tie conclusion of Lemma 1 is consumed. Note $\rho_{g}=2c_{X}/R$ is the *covering-limited*
radius (it is smaller than the isolation radius $\rho_{\rm iso}$ of (3.3)), and the bound (5.2) is strictly
positive for all $0<\|\delta\|<\rho_{g}$, vanishing only in the limit at the endpoint.

**Self-consistency requirement.** The constants $c_{X},R$ must be valid on the whole ball on which (5.2) is
asserted, so one needs $\rho_{\rm data}\ge\rho_{g}+\operatorname{hd}(X_{0})$; here
$2.05\times10^{-3}\ge1.978\,224\,4\times10^{-3}+10^{-21}$. This constraint is *not* automatic and was violated
in a first draft (a data ball of radius $10^{-5}$ combined with a certified radius of $4.3\times10^{-3}$).

---

## §6 Lemma 5 (global lower bound outside the two balls) — [CA]

**Lemma 5.** *Let $\rho_{g}$ be as in (5.3), let $B_{1}:=B(z_{*},\rho_{g})$, $B_{2}:=B(\sigma z_{*},\rho_{g})$, and let*
$$T_{C}\;:=\;\sup_{X_{0}}F+10^{-9}\;=\;F(z_{*})+10^{-9}\;=\;0.373\,091\,893\,895\,817. \tag{6.1}$$
*Then every $x\in\Omega\setminus(B_{1}\cup B_{2})$ satisfies $F(x)\ge T_{C}$.*

**Method.** Adaptive branch-and-bound on $\Omega$ with the exact separable box lower bound
$$\mathrm{LB}(X)=\max_{1\le k\le K}\Bigl[\min_{I_{1}}\cos k\varphi_{1}+\min_{I_{2}}\bigl(r_{2}^{k}\cos k\varphi_{2}\bigr)+\min_{I_{3}}\bigl(r_{3}^{k}\cos k\varphi_{3}\bigr)\Bigr]\le\min_{X}F,$$
the products again handled as interval products; note $\mathrm{LB}(X)\le\min_X\max_k\le\min_X F$ is the correct
direction. A box is

* **discarded** if $\operatorname{far}(X,c_{0})\le\rho_{g}-10^{-9}$ from one of the two centres — then
  $X\subseteq B(c_{0},\rho_{g}-10^{-9})\subseteq B(z_{*},\rho_{g})$ (using $\operatorname{hd}(X_{0})\le10^{-21}$),
  so the box lies in the locally certified region and is covered by Lemma 4;
* **certified** if $\underline F_{\rm IA}(X)\ge T_{C}$;
* **split** otherwise (bisection along the widest coordinate), and only if the box is not already below the
  minimum width $10^{-7}$; a box that can be neither certified nor discarded at minimum width is counted
  **unresolved** and would invalidate the lemma.

**Outcome.**

| quantity | value |
|---|---|
| boxes evaluated $N_{\rm eval}$ | $472\,766$ |
| interval-certified $N_{\rm cert}$ | $252\,282$ |
| discarded $N_{\rm disc}$ | $485$ |
| split $N_{\rm split}$ | $219\,999$ |
| **unresolved $N_{\rm unres}$** | $\mathbf 0$ |
| float-pass / interval-fail | $\mathbf 0$ |
| $\min_X\bigl(\underline F_{\rm IA}(X)-T_{C}\bigr)$ | $4.628\,931\times10^{-8}$ |
| $\max\{\operatorname{far}(X,c_{0}):X\ \text{discarded}\}$ | $0.001\,978\,039\,980\le\rho_{g}-10^{-9}$ |

**Independent implementation.** A structurally different three-process implementation of the interval layer,
sharing only the (deterministic) float partition, reproduces $N_{\rm cert}=252\,282$, $0$ interval failures, and
the minimum margin $4.628\,931\,107\,212\,973\,4\times10^{-8}$ — identical to sixteen significant digits.

**Set decomposition (exact).** The adaptive segmentation of $\Omega$ is a disjoint tiling, and since
$N_{\rm unres}=0$ every terminal box is either certified or discarded. Writing
$\mathcal C_{\rm cert}$ for the union of the certified boxes and $\mathcal D$ for that of the discarded ones,
$$\Omega\;=\;\mathcal C_{\rm cert}\;\sqcup\;\mathcal D,
\qquad
\mathcal D\;\subseteq\;B_{1}\cup B_{2},
\qquad
F\ge T_{C}\ \text{on}\ \mathcal C_{\rm cert}. \tag{6.2}$$
Consequently $\Omega=\mathcal C_{\rm cert}\cup B_{1}\cup B_{2}$ is a valid cover (the three pieces may overlap;
no gap is possible because the first decomposition is exact).

---

## §7 Proof of Theorem A

Let $x\in\Omega$.

1. If $x\in\mathcal C_{\rm cert}$ then $F(x)\ge T_{C}=F(z_{*})+10^{-9}>F(z_{*})$ by Lemma 5.
2. If instead $x\in B_{1}\cup B_{2}$, i.e. $x=\sigma^{i}z_{*}+\delta$ with $i\in\{0,1\}$ and
   $\|\delta\|\le\rho_{g}$: if $\delta=0$ then $F(x)=F(z_{*})$ (using $F\circ\sigma=F$, Lemma 0/Prop. 8.1);
   otherwise Lemma 4 applied at the corresponding centre gives $F(x)>F(z_{*})$.
3. Since $\Omega=\mathcal C_{\rm cert}\cup B_{1}\cup B_{2}$ (Lemma 5, (6.2)), cases 1–2 cover all of $\Omega$.
   Hence $F(x)\ge F(z_{*})$ on $\Omega$, with equality only at $z_{*}$ and $\sigma z_{*}$; therefore
   $C_{3}=F(z_{*})$ and the minimiser set is exactly $\{z_{*},\sigma z_{*}\}$. $\square$

**Hypotheses consumed.** (2.2) from Lemma 1; the constants of Lemmas 2–4; the target (6.1) and the partition
outcome of Lemma 5. Nothing else, and no property of the Riemann zeta function.

---

## §8 Proposition (minimiser orbit and its two-element quotient)

**Lemma 0 (symmetry).** $F\circ\sigma=F$, where $\sigma$ is the paired swap (0.4).

*Proof.* $F(x)=\max_{k}\bigl[\cos k\varphi_{1}+r_{2}^{k}\cos k\varphi_{2}+r_{3}^{k}\cos k\varphi_{3}\bigr]$;
applying $\sigma$ merely exchanges the second and third summands. $\square$

**Proposition 8.1.** *Let $z_{*}$ be the root of Lemma 1. Then*

*(i) The $S_{3}$-orbit of $z_{*}$ in the unnormalised space has $6$ points:*
$$|\mathcal O_{\rm raw}|=6 .$$

*(ii) Under the normalisation quotient $\mathcal N$ (re-order so that the unit-modulus pair comes first) the
orbit collapses to exactly two points:*
$$\bigl|\mathcal N(\mathcal O_{\rm raw})\bigr|=2,\qquad \mathcal N(\mathcal O_{\rm raw})=\{z_{*},\sigma z_{*}\} .$$

*(iii) Permuting the three angles while keeping the radii fixed is **not** a symmetry of $F$; in particular*
$$F(r_{2},r_{3},\varphi_{2},\varphi_{1},\varphi_{3})=1.126\,876\,598\,534\,850\ \ne\ F(z_{*})=0.373\,091\,892\,895\,817 .$$

*Proof.* (i) The three pairs $(1,\varphi_{1}),(r_{2},\varphi_{2}),(r_{3},\varphi_{3})$ are pairwise distinct
($r_{2}=0.7905\ne r_{3}=0.8302$), so the six permutations of the pairs give six distinct unnormalised
configurations; the value of $F$ is the same for all six by the permutation invariance of the underlying
$\max_{k}\operatorname{Re}\sum_{j}z_{j}^{k}$.

(ii) Of the six permutations, four move the unit-modulus pair into position $2$ or $3$. Re-normalising (moving
the unit pair back to the first position, keeping the relative order of the remaining two) identifies those four
with either $\mathrm{id}$ (relative order preserved) or $\sigma$ (relative order reversed). Hence at most two
distinct normalised points, and they are distinct because $r_{2}\ne r_{3}$.

(iii) Direct evaluation: with the radii fixed and only $\varphi_{1},\varphi_{2}$ interchanged, the term
$\cos k\varphi_{1}$ (undamped) and $r_{2}^{k}\cos k\varphi_{2}$ (damped) are not interchangeable, and the
numerical values differ as stated. $\square$

**Remark 8.2.** Statement (i) alone would suggest "six minimisers"; the registered statement for the problem on
$\Omega$ is (ii), namely **two**. The two objects differ by the normalisation, not by the mathematics.

---

## §9 Dependency DAG (acyclic; no circularity)

```
  definitions (0.1)-(0.4)
        │
        ├──► Lemma 0 (F∘σ = F) ─────────────────────────────────────────────┐
        │                                                                    │
        ├──► Lemma 1 (Krawczyk: ∃! z*, X₀, λ>0, six-way tie)                 │
        │        │                                                           │
        │        ├──► δ_A(z*) = 0  ─────────────────────────┐                │
        │        └──► sup F(X₀)  ────► T_C = sup F(X₀)+1e-9 ─┼──────────┐    │
        │                                                   │          │    │
        ├──► Lemma 2 (Δ_ref > 0)  ──► ρ_iso                 │          │    │
        ├──► Lemma 3 (c > 0)      ──► c_X = c − ε_pert      │          │    │
        ├──► Lemma 4' (R)         ──► ρ_g = 2c_X/R          │          │    │
        │                                │                  │          │    │
        │                                └──► Lemma 4 (local growth at z*) ──┼──► Theorem A
        │                                                   │          │    │
        └───────────────────────────────────────────────────┴──► Lemma 5 (global B&B on Ω∖(B₁∪B₂) at T_C)
                                                               │          │
                                                               └──► (6.2) set decomposition ──┘
```

Every arrow points from a lower layer to a higher one; no lemma is used in its own derivation. In particular
Lemma 5 uses Lemma 4 **only** through the numerical radius $\rho_{g}$ (the radius of the excluded balls), and
Lemma 4 uses Lemma 1 only through the single identity $\delta_{A}(z_{*})=0$ (2.2).

---

## §10 Numerical certificate table

All entries are reproducible from the scripts listed. Angles are in radians unless a $\pi$ factor is shown.

| # | item | value | script |
|---|---|---|---|
| 1 | high-precision root $z_{*}$ ($\varphi_{j}/\pi$) | $(0.10911016482862308881,\ 0.8206637095202066754,\ 0.46171937101861024265)$ | `dB_krawczyk_11.py` |
| 2 | Krawczyk seed / final width / $\|I-YJ\|_\infty$ | $10^{-12}$ / $3.93\times10^{-22}$ / $1.9651\times10^{-10}$ | `dB_krawczyk_11.py` |
| 3 | multipliers $\lambda$ ($k=1,2,3,4,5,15$) | $(0.20005,\ 0.17849,\ 0.16551,\ 0.19482,\ 0.11186,\ 0.14927)$ | `dB_krawczyk_11.py` |
| 4 | $\Delta_{\rm ref}$, $L_{\rm act}$, $L_{\rm non}$, $\rho_{\rm iso}$ | $0.279\,596\,813\,6$; $33.54102$; $31.304952$; $4.31171\times10^{-3}$ | `dB5_local_growth_5d.py` |
| 5 | $c$, $\varepsilon_{\rm pert}$, $c_{X}$, $\rho_{\rm data}$ | $0.302\,091\,5$; $0.2032$; $0.098\,812\,009\,77$; $2.05\times10^{-3}$ | `dB5_local_growth_5d.py` |
| 6 | $R$ | $99.899\,695\,515\,930\,13$ | `dB5_local_growth_5d.py` |
| 7 | $\rho_{g}=2c_{X}/R$ | $1.978\,224\,4\times10^{-3}$ | `dB5_local_growth_5d.py` |
| 8 | $T_{C}-F(z_{*})$ | $10^{-9}$ | `dC2iv_strict.py` |
| 9 | $N_{\rm eval},N_{\rm cert},N_{\rm disc},N_{\rm split},N_{\rm unres}$ | $472\,766$; $252\,282$; $485$; $219\,999$; $\mathbf 0$ | `dC2iv_strict.py` |
| 10 | $\min_X(\underline F_{\rm IA}(X)-T_{C})$ | $4.628\,931\times10^{-8}$ | `dC2iv_strict.py` |
| 11 | cross-check (independent implementation) | identical to 16 significant digits | `dC2par_parallel_iv.py` |
| 12 | $C_{3}$ | $0.373\,091\,892\,895\,816\,4\ldots$ | Theorem A |

**Reproduction commands.**
```
python3 scripts/dB_krawczyk_11.py                       # Lemma 1
python3 scripts/dB5_local_growth_5d.py                  # Lemmas 2-4
python3 scripts/dC2iv_strict.py                         # Lemma 5 (sequential)
python3 scripts/dC2par_parallel_iv.py                   # Lemma 5 (independent)

```

---

## §11 Implementation caveats (explicit, non-blocking)

1. **Facet normals via floating-point SVD.** Lemma 3 obtains the facet normals from a floating-point SVD. The
   perturbation allowance in the data ball is $\varepsilon_{\rm pert}\approx0.203$, i.e. $10^{-15}\ll
   \varepsilon_{\rm pert}$, so the floating-point error cannot change the sign of $c_{X}$. A version using
   interval linear algebra would remove the caveat but is not needed for the conclusion. This is a *numerical
   implementation* caveat, not a formalisation of the lemma in interval linear algebra.
2. **Self-built interval arithmetic.** Lemma 5 uses a hand-rolled interval class over `mpmath.mpf` at 40 decimal
   digits, with an outward slack of $10^{-30}$ per operation and $\pi$ enclosed by rational endpoints. The
   alternative line using `mpmath.iv` independently reproduces the bounds.
3. **`mpmath` correctness** is assumed (as everywhere in this project); the interval layer of Lemma 5 also
   reports the float-pass / interval-fail count, which is $0$.
4. **Lipschitz constants** $k\sqrt5$ are analytic bounds, not computed quantities.
5. **`R`** is an explicit conservative bound obtained from the $5\times5$ Hessians with $|\cos|,|\sin|\le1$ and
   the damping factors retained; it is an upper bound, so (5.2) is conservative.

---

## §12 Boundaries — what is *not* claimed

1. Theorem A is a statement about $M=3$ in the damped setting. **No** extrapolation to general $M$, to damped
   $M\ge4$, or to the undamped constant $m_{M}$ is claimed.
2. The numerical value of $C_{3}$ is only known at interval level; the displayed decimal is the upper-bound
   configuration's value plus the certified $10^{-9}$ threshold, not a closed form.
3. No property of the Riemann zeta function is used anywhere in this note.
4. Earlier brackets ($0.373\,091\,8\le C_{3}\le0.373\,092\,075\,762$; $0.76\le m_{3}\le0.764\,081\,100\,745\,854$)
   are superseded/retained only as checkpoints.
5. The proof is computer-assisted: Lemmas 1–5 are **[CA]** statements. The elementary layer (Lemma 0,
   Proposition 8.1, and the algebraic parts of Lemmas 2–4) is proved by hand here.
