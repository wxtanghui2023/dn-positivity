# E5 — The explicit test function g_n in Lagarias (2007)

**Source read (verbatim, PDF text extracted with PyPDF2):** J. C. Lagarias, *Li coefficients for
automorphic L-functions*, Ann. Inst. Fourier (Grenoble) **57** (2007), no. 5, 1689–1740. Retrieved from
`https://www.numdam.org/item/AIF_2007__57_5_1689_0.pdf` (the article's own header gives the AIF/Cedram
identifier `AIF_2007__57_5_1689_0`). 53 PDF pages; printed pagination cited below.
**Labels:** 核验 = numerically verified here · 引用 = from the source · 推导 = derived here · 猜想 = conjecture.

## 1. What the alignment documents already recorded, and where they stop

**引用** `docs/ALIGN-A1-li-coefficients.md` §1 and `docs/ALIGN-A1-COMPLETE.md` §1/§4 quote Lagarias'
"third observation" (p. 1692): *"each positivity condition λ_n ⩾ 0 encodes 'Weil positivity' of Weil's
quadratic functional for a particular test function g_n(x)."* Both documents then recommend treating
"λ_n ≥ 0" as an instance of Weil positivity (ALIGN-A1 §4, 建议 3), and both list the missing piece as
"the explicit g_n". Neither writes g_n down. **E5 closes that gap: g_n is explicit, not variational.**

## 2. The test function in the s-variable (Lagarias §3, pp. 1703–1706)

**引用** The test-function space A = functions holomorphic in the strip 0 < Re(s) < 1 with F(s) = O(1/|s|)
for |Im s| ≥ 1 (p. 1704). The **Weil scalar product** attached to π is

  **(3.1)**  ⟨F, G⟩_{W(π)} := Σ_{ρ ∈ Z(π)} F(ρ)·G(1 − ρ̄),   sum over zeros with multiplicity (p. 1704).

**引用** The **Li class** L ⊂ A is the set of rational functions in C(s) vanishing at ∞ whose pole divisor
lies in {0, 1}; equivalently L = span{ s^{−n} (n ≥ 1) ; (1−s)^{−n} (n ≥ 1) }. The Li test functions are

  **(3.2)**  G_n(s) := 1 − (1 − 1/s)^n,   n ∈ Z        (p. 1705),

and {G_n : n ≠ 0} is a vector-space basis of L.

**引用** **Theorem 3.1** (p. 1705): for G_n(s) = 1 − (1 − 1/s)^n,

  **(3.3)**  ⟨G_n, G_m⟩_{W(π)} = λ_n(π) + λ_{−m}(π) − λ_{n−m}(π),
  **(3.4)**  ‖G_n‖²_{W(π)} = λ_n(π) + λ_{−n}(π) = 2·Re λ_n(π).

**引用** Here λ_{−n}(π) is the conjugate of λ_n(π) by the symmetry (1.9) λ_{−n}(π) = conj(λ_n(π)) (p. 1692),
which is what makes (3.4) real; λ_0(π) = 0 because G_0 ≡ 0.

## 3. The explicit form of g_n(x) — the deliverable

**引用** Appendix A, p. 1738. Lagarias states: "In [4, Lemma 2] the functions g_n(x) were explicitly
determined, as"

  **g_n(x) = P_n(log x) if 0 < x < 1;   g_n(1) = n/2;   g_n(x) = 0 if x > 1,**

  **where P_n(y) := Σ_{j=1}^{n} C(n, j)·y^{j−1}/(j−1)!.**

and notes P_n(y) = L^1_{n−1}(−y) (Laguerre polynomial with α = 1); he attributes the same observation to
Coffey [9, Appendix E]. The source-of-the-source is **Bombieri & Lagarias, *Complements to Li's criterion
for the Riemann hypothesis*, J. Number Theory 77 (1999) 274–287, Lemma 2** (the article's ref. [4]). Its
Mellin transform is the s-variable test function of §2: ĝ_n(s) = ∫_0^∞ g_n(x) x^{s−1} dx = G_n(s).

**核验 (done here).** For n = 1, 2, 3, 5, 8 and Re(s) > 0, the numerical integral
∫_0^1 P_n(log x) x^{s−1} dx reproduces 1 − (1 − 1/s)^n to ≥ 20 digits (e.g. n = 3, s = 0.7 − 1.3i:
1.4113622166… + 0.612492075467…i both ways). For Re(s) < 0 the integral diverges, as it must: (3.2) has a
pole of order n at s = 0. I also verified P_n(y) = L^1_{n−1}(−y) for n = 1, 2, 3, 4, 6 to 25 digits.

**推导** Structural properties, all immediate from the displayed formula:
(i) g_n is supported in **(0, 1]** — one-sided in the multiplicative variable; after u = log x the support
is (−∞, 0], and g_n = L^1_{n−1}(−u) there.
(ii) g_n jumps at x = 1: g_n(1⁻) = P_n(0) = n, g_n(1⁺) = 0, and the assigned value n/2 is the half-jump.
(iii) g_n is a polynomial of degree n−1 in log x on (0,1) — in particular g_n ≢ 0 and g_n ∈ L.
(iv) ĝ_n(0) = ∫_0^∞ g_n(x) x^{−1} dx = +∞, logarithmically divergent at x → 0⁺ (leading term
(log x)^{n−1}/(n−1)!). See §5.

## 4. Explicit, not variational

The deliverable's requested alternative does **not** apply: g_n is given in closed form (a Laguerre
polynomial composed with log x, truncated to (0,1)), not as the extremiser of a variational problem.
There is therefore no "implicit extremiser" caveat on the A1↔A3 bridge. The only delicate point in g_n is
its distributional nature at s = 0 (equivalently at x = 0, 1), treated in §5.

## 5. Consequence for the A1↔A3 bridge

**引用** Theorem 3.1 immediately gives: **the Li condition is the diagonal of the Weil form on L.**
Explicitly, for every n ≥ 1,

  λ_n(π) ≥ 0 (real part nonneg.)  ⟺  2 Re λ_n(π) = ‖g_n‖²_{W(π)} = ⟨g_n, g_n⟩_{W(π)} ≥ 0,

i.e. "λ_n ≥ 0" **is** the statement that Weil's quadratic form is nonnegative on the single explicit vector
g_n. Concretely, once g_n is known the bridge reads:

  Re λ_n(π) ≥ 0 ∀ n ≥ 1  ⟺  ⟨g_n, g_n⟩_{W(π)} ≥ 0 on each of the explicit vectors
                            g_n(x) = 1_{(0,1)}(x)·L^1_{n−1}(−log x)  (+ ½n·δ at x = 1).

**引用** The full (non-diagonal) A3 statement is also in the source (p. 1706): L is large enough that
positive semidefiniteness of ⟨·,·⟩_{W(π)} on L is *equivalent* to RH for L(s,π); and RH ⟹ PSD because
ρ = 1 − ρ̄ on the critical line gives ⟨F,F⟩ = Σ_ρ |F(ρ)|² ≥ 0. Written on the basis {G_n}, the form is the
matrix

  **推导**  M_{nm} = ⟨G_n, G_m⟩_{W(π)} = λ_n(π) + conj(λ_m(π)) − λ_{n−m}(π),   n, m ≥ 1  (λ_0 = 0),

so the *entire* matrix is determined by the single sequence (λ_k)_{k ∈ Z} via (3.3).

**推导 (honest limitation of the bridge).** "diagonal ≥ 0 for all n" ⟹ "M ≥ 0" is true, but only
*formally*, because both conditions are equivalent to RH (Li's criterion on one side, Lagarias' §3
converse on the other). There is no direct linear-algebra proof inside the bridge; the implication runs
through RH. So the bridge is a concrete reformulation — it lets the A3 inertia / finite-compression and A7
(Connes) machinery be applied to *specific, explicit* test vectors g_n instead of an abstract test
function — but it does not by itself upgrade the diagonal condition into positivity of the whole form.

## 6. The precise obstacle (the most useful structural finding)

**引用** p. 1737: "The vector space L of Li test functions makes sense for this extended covariance form of
the 'explicit formula' with a cutoff parameter, and not for the trace form. […] In consequence the trace
function T[f] is undefined for every Li test function." p. 1738: "ĝ_n(0) is infinite, for each n ≥ 1.
[…] the unbounded contribution from ĝ_n(0) above as T → ∞ is offset by a corresponding divergence coming
from the finite primes in the 'explicit formula'." Lagarias adds that the Weil functional W[f] **is**
well-defined for all f ∈ L, and the Weil scalar product too, **whether or not RH holds**.

**推导** So the Li test vectors g_n lie outside the domain of the trace-form explicit formula
(T[f] = f̂(0) − W[f] + f̂(1), (A.4)–(A.5), p. 1736) — they are admissible only in the regularised
**covariance** form (A.6)–(A.7) with cutoff T, where the divergence of f̂(0) = ∫_0^∞ g_n(x) dx/x is
cancelled against the finite-prime (arithmetic) side. **This is a concrete, checkable obstruction for any
A1↔A3/A7 programme that plans to evaluate Weil's form on Li test vectors through an ordinary trace formula
or a finite compression: the test vector of the A1 line is not in the trace-form domain.** One must work in
the covariance form. (This is exactly the point of Bombieri–Lagarias 1999.)

**推导 (name collision warning).** This g_n(x) is *not* the project's own g_n(t) = [t·sin(nθ) + ½cos(nθ)]/(¼ + t²)
used in the withdrawn D_n-telescoping line (see `paper/LAGARIAS-REVIEW-REQUEST.md`). Different object,
different variable, different line. The two must not be conflated in the bridge write-up.

## 7. Verdict

The explicit construction exists and is one line long: **g_n(x) = 1_{(0,1)}(x)·L^1_{n−1}(−log x) (+ ½n at
x = 1), whose Mellin transform is G_n(s) = 1 − (1 − 1/s)^n**, giving ‖G_n‖²_{W(π)} = 2 Re λ_n(π)
(Lagarias 2007, (3.2), Theorem 3.1 (3.4), Appendix A p. 1738; original Bombieri–Lagarias 1999, Lemma 2).
The obstruction is not explicitness but admissibility: g_n is supported on (0,1) and has a divergent
Mellin moment at s = 0, so T[f] is undefined for it and only the regularised covariance form applies.

**Single most useful sentence for a reader deciding whether to invest:** the A1↔A3 bridge can be written
completely explicitly and cheaply — λ_n ≥ 0 is literally ⟨g_n, g_n⟩_W ≥ 0 for g_n(x) = L^1_{n−1}(−log x)
on (0,1) — but since these test functions are inadmissible in the trace form of the explicit formula and
their positivity is only the *diagonal* of Weil's form, the bridge is a reformulation of Li's criterion
rather than a new handle on it.

## 8. Boundaries

**引用** §2, §3 (definitions, (3.1)–(3.4), Theorem 3.1), §5 and §6 (pages, "trace function undefined",
"ĝ_n(0) is infinite", W well-defined for all f ∈ L), and the (3.2)/Appendix-A attribution to
Bombieri–Lagarias 1999 Lemma 2. · **核验** §3 numeric Mellin identity and Laguerre identity (n = 1,2,3,5,8
and 1,2,3,4,6; ≥ 20 digits). · **推导** §3(i)–(iv), §5 matrix M_{nm} and the "no direct algebraic
implication" remark, §6 trace-form obstruction and name-collision warning. · **未读** Bombieri–Lagarias
1999 Lemma 2 itself (cited via Lagarias 2007); Coffey 2005 Appendix E. · **猜想** none recorded. ·
No git commit; no existing file modified.
