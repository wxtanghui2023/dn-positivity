# E7 / A3-2 — Is the project's kernel family inside the frontier's bandwidth-one class?

**Labels:** 核验 = checked here or in-repo; 引用 = quoted from an external source; 推导 = derived in this note; 猜想 = conjecture.
**Sources actually read for this note:** arXiv:2608.13637v2 — abstract page (accessible) and the full HTML
(§1.1, §1.2, §2.2, §2.3, §7.2, §B.5; the fetcher truncated the HTML, see §7 below). In-repo:
`docs/ALIGN-A3-weil-positivity-inertia.md`, `docs/ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`,
`docs/E8-ceiling-0682.md`, `docs/E10-rank-trace-inertia-joint.md`, `docs/ERRATUM-inertia-factor2.md`,
`docs/p27g1-orbit-weil-defect.md`, `docs/p27g7-operator-decomposition.md`, `docs/p27g8-inertia-stability.md`,
`docs/p27p33-fourfold-audit.md`.
**Not claimed:** nothing below proves or disproves RH; no bound on the proportion is produced.

## 1. Access status of the frontier source

[核验] `arxiv.org/abs/2608.13637` retrieved. Title: "More than two thirds of the zeta zeros are simple and
on the critical line". The Comments field reads verbatim: "21 pages. Proof discovered autonomously by
Claude (Anthropic); verified and communicated by the listed authors. See §1 for provenance. Lean
formalization available" [引用]. Submission history: v1 Thu, 13 Aug 2026; v2 Wed, 19 Aug 2026.

[核验] `arxiv.org/html/2608.13637v2` retrieved; the sections needed here (§1.1, §1.2, §2.2–§2.3, §7.2, §B.5)
are legible. So the definition below is quoted **from the source**, not from the repo's summaries.

## 2. The frontier's definition of the class, verbatim

[引用] arXiv:2608.13637v2, **§7.2**, in the subsection headed "The bandwidth-one ceiling", opening sentence:

> "Call a bandwidth-one certificate any function $p$ of a locally finite, $\rho\mapsto 1-\bar\rho$–symmetric
> configuration that (a) depends on the configuration only through its first two trace moments against test
> functions of Fourier support in $[-1,1]$ and the partition into on-line points and off-line pairs, and
> (b) satisfies $p \le N_0^s/N$ configuration by configuration."

[引用] Same subsection: the ceiling is produced by the Lean theorem `Zeta23.PairCeiling.ceiling_law256`,
whose constant is printed as "$p_0 := 1-a_N$ ... (rounded up, $p_0 \le 0.6818287$)" — i.e. the
"approximately 0.682" of §1.1.

[引用] §1.1: "The ceiling over the broader class of all bandwidth-one certificates is approximately 0.682;
see §7.2." and "among windows $\psi$ (equivalently, certificates of the form $2-R(\psi)$), this is
optimal [CCLM17, Cor. 14]."

[引用] §B.5: "The bandwidth-one ceiling of §7.2 ... was established after the session by Easley and
sharpened by Stephen McAleer."

[核验] Two features of the definition matter, and both are verbatim above: (i) the object in the class is a
**function p of a configuration** — a certificate, not a kernel and not a window; (ii) the accompanying
window $r$ is required to have **Fourier support in $[-1,1]$** (band-limited; $r(\pm1)=0$ for a band-limited
window). A numbered label for the definition (e.g. "Definition 7.x") was **not found** in the retrieved
text — this is a *not-found* (the HTML was truncated by the fetcher), not a claim that no number exists.

## 3. The project's kernel family, as recorded in-repo

[核验] `docs/p27g8-inertia-stability.md`, G8.1: the orbit kernel is
$K_\rho = 4\,e^{s/2}(\cosh(\delta s)-1)\cos(\gamma t)$ with $s=u+v$, $t=u-v$.
[核验] `docs/p27g1-orbit-weil-defect.md` §②: the orbit defect
$D_\delta(f;\gamma) = 4\int e^{u/2}\cos(\gamma u)[\cosh(\delta u)-1]\,d\mu(u)$ has quadratic-form kernel
$4\,e^{(u+v)/2}[\cosh(\delta(u+v))-1]\cos(\gamma(u-v))$ — the family named in the registered item, with
relatives $K_N(u,v)=\sum_{j\le N} e^{(u+v)/2}[\cosh(\delta_j(u+v))-1]\cos(\gamma_j(u-v))$
(`docs/p27g7`, rank $\le 6N$) and the $\delta^2$-jet approximations of G4/G4′/G5.
[推导] So the family consists of **two-variable kernels** $K(u,v)$, indexed by the off-line data $(\delta_j,\gamma_j)$.

## 4. Per-condition test against the definition

[推导] (i) **Is it a function of a configuration (a certificate p)?** No. $K(u,v)$ is a quadratic-form
kernel on test functions — a function on $\mathbb{R}^2$ — not a functional of a zero configuration. **FAIL.**
(ii) **Does it depend on the configuration only through the first two trace moments against band-limited
test functions?** No. $K$ depends on the configuration through the individual parameters $(\delta_j,\gamma_j)$
(and on the partition only implicitly), not through two trace moments; and its $\gamma$-dependence is the
phase $e^{\pm i\gamma(u-v)}$, which is not a moment against a Fourier-supported test function. **FAIL.**
(iii) **Non-negative / of the required sign form?** No. $\cos(\gamma(u-v))$ changes sign; `ERRATUM-inertia-factor2.md`
records that the correct sector block is $2I-4\cdot\mathbf{1}$ with eigenvalues $2,2,-10$, so $K$ is
sign-indefinite, with two negative directions per orbit. **FAIL.**
(iv) **Supported in a fixed bandwidth (Fourier support in $[-1,1]$)?** No. $e^{(u+v)/2}$ and
$\cosh(\delta(u+v))$ have unbounded Fourier support along the diagonal direction $u+v$, and
$\cos(\gamma(u-v))$ has Fourier support at frequencies $\pm\gamma$, with $\gamma$ a zero ordinate that is
unbounded over the window $[T,2T]$. The kernel is not band-limited in any fixed band. **FAIL.**
(v) **An even function of one variable of the required form, $\psi(u/L)$?** No — it is a function of two
variables, not of $u$ alone; the "relatives" are likewise two-variable. **FAIL.**

⇒ **Verdict ([推导]): the project's kernel family satisfies no condition of the definition.** It is not a
bandwidth-one certificate, and not even a window of the class.

## 5. Consequence for plugging into the frontier's inequality

[推导] The frontier's chain needs a Hermitian $G̃$ that is the compression of Weil's form on $d$ modulated
copies of a band-limited window, with $P_1\succeq0$ the on-line part:

> (1.1) $\operatorname{rank}P_1 \ge 2\operatorname{tr}P_1+4\operatorname{tr}Q'-4b-\|P_1+Q'\|_{\mathrm{HS}}^2$ [引用]
> (1.2) $N_0^s+o(N) \ge \operatorname{rank}P_1 \ge 4\operatorname{tr}G̃-2N-\|G̃\|_{\mathrm{HS}}^2 = (2-R(\psi)-o(1))N$ [引用]

[推导] Our $K$ is not such a $G̃$: it is not band-limited (iv), not positive semidefinite (iii), is not a
certificate (i)–(ii), and is built **from** the off-line data $\delta$ it is meant to detect — the
circularity recorded in `docs/p27p33-fourfold-audit.md`, verdict P-C. It therefore cannot be substituted
into (1.1)/(1.2), and it yields no proportion statement.

[推导] Of the two standard objects in the repo, the relevant one is the **inertia computation** — the
negative-index bookkeeping ($n_-(K_\rho)$, $n_-(K_N)$, the P28–P33 moving-edge results), i.e. precisely the
object the frontier declines to use ("we use rank and positive index", §1.3). The **Toeplitz compression** of
the C–vS rank-deficiency line is a *different* object: the repo's audit records that its "rank" is the rank
of a Toeplitz/CF object, not the frontier's $\operatorname{rank}P_1$ = number of on-line points, and the two
must not be conflated. Neither belongs to the bandwidth-one certificate class.

## 6. The registered sub-question, answered

**Sub-question:** if our family is outside the class, does that give a route to beating the ceiling, given
that E8 shows the window functional is saturated within the class?

[推导] **No.** Four reasons:
1. *Non-membership is necessary, not sufficient.* The ceiling is an upper bound on the class; failing to be
   in the class merely means the theorem is silent about our family. Beating 0.682 still requires an
   **admissible** certificate (some p with $p\le N_0^s/N$) whose bound exceeds 0.682.
2. *The window side is closed.* [核验] E8's numerical result (`scripts/E8_ceiling_check.py`) is that
   $\min R(\psi)$ over the whole bandwidth-one class — non-negative windows (simplex) and signed windows
   (exact KKT), $N$ up to 1600 — equals $c_{\mathrm{MT}}^{-1}=1.3274993\ldots$; hence
   $\max(2-R(\psi))=0.6725$. No window optimisation passes 0.6725.
3. *The residual 0.01 is not a window effect.* [推导] E8 shows the gap $0.682-0.6725$ comes from using the
   two known moments sharply, through the Christoffel bound $\Lambda_1(0)=1-m_1^2/m_2$, not from a window;
   and exceeding 0.682 requires an **unconditional third moment** at $X\asymp T$. [引用] §7.2(e) states that
   unconditionally higher moments add nothing — the Rudnick–Sarnak range $X^k\le T^{2-\varepsilon}$ admits
   only $k=1$ at $X\asymp T$ — a barrier about multiplicative relations among prime powers, not about windows.
4. *Our family is outside the class for the wrong reason.* [推导] It is not an admissible certificate at all
   (sign-indefinite, unbounded Fourier support, two-variable, $\delta$-dependent), so it cannot be converted
   into any proportion bound, let alone one above the ceiling.

⇒ **The ceiling stands; the project's kernel family offers no route around it.** This is the honest answer.

## 7. Boundaries

[核验] Frontier §7.2 definition, the constant 0.6818287 ≤ 0.682, §1.1, §B.5 — read at source (HTML v2).
The body of the Lean statement and its two hypotheses (`hvalid`, `EnclOK`) were only partially legible: the
extraction elided the formula following "ceiling_law256 establishes [...]", so the constant is 引用 as printed.
[核验] In-repo: p27g1/g6/g7/g8, ERRATUM-inertia-factor2, E8, E10, p27p33-fourfold-audit.
[引用] only: the quoted definition; 0.682 / 0.6818287; (1.1); (1.2); §7.2(e). [推导]: §4 verdicts, §5, §6.
[未读] the frontier's derivation of the ceiling in §7.2; the Lean sources; [CCLM17]. RH is not addressed.
