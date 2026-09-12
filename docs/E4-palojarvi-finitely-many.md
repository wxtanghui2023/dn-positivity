# E4 — Extending Palojärvi's "at most one off-line zero" to finitely many

**Source read:** `docs/Palojarvi-2019-tau-Li-explicit-zero-free.pdf` = arXiv:1807.01506v3 (29 Apr 2020),
"Explicit zero-free regions and a τ-Li-type criterion", Neea Palojärvi. Text obtained with PyPDF2
(`pdftotext` is absent on this host). All quotations below are from the author's PDF.
**Labels:** 核验 = numerically verified here · 引用 = from the source · 推导 = derived here · 猜想 = conjecture.

## 1. The theorem whose proof is examined

**引用** Theorem 4.1 (source §4, pp. 18–19). Let τ > 1/e and T₀, A_F, B_F, c_{F,j}(T₀), C_{F,j}(T₀)
(j = 1,2,3) be as in condition (c), K_{F,1}(τ) as in Theorem 2.1 and K_{F,4}(τ) as in (36). Suppose
F(s) has **at most one** zero ρ₁ with |ρ₁/(ρ₁ − τ)| > 1; if such ρ₁ exists, let R > 1 satisfy
|ρ₁/(ρ₁ − τ)| ≥ R. Then, with

    N = ⌈ max{ T₀/(eτ), exp(−W₋₁(−(2/3)·log R)), 12·log(40(0.5 + K_{F,1}(τ) + K_{F,4}(τ)))/log R } ⌉

    ρ₁ exists  ⟺  |ℜ(λ_F(n,τ))| ≥ (K_{F,1}(τ) + K_{F,4}(τ))·n·log n
                  for at least one integer n ∈ [N, 5N] with N | n.

(The source prints a case distinction, "if R ≤ e^{3/2}·e" vs. otherwise, in which the W₋₁-term is
dropped; the branch value is rendered ambiguously by my text extraction, so I do **not** assert it.
K_{F,4}(τ) = 2(A_F eτ log(e^{2}τ) + |B_F| eτ + C_{F,1}(T₀)log(e^{2}τ) + C_{F,2}(T₀)/3 + C_{F,3}(T₀)/(9eτ)).)

**引用** The paper advertises this as the one place where it gets an *equivalent* condition (rather than
the one-directional Theorems 3.1/3.3), i.e. an "if and only if", at the price of assuming at most one
off-line zero.

## 2. The proof, in skeleton

**引用** The proof is one decomposition. Writing T(n) := n e τ, and using that |ρ/(ρ−τ)| = 1 ⟺ ℜ(ρ) = τ/2,

  (37) ℜ(λ_F(n,τ)) = lim_{t→∞} Σ_{T(n)<|ℑρ|≤t, 0≤ℜρ≤τ/2} ℜ(1 − (ρ/(ρ−τ))^n)
                    + Σ_{|ℑρ|≤T(n), 0≤ℜρ≤τ/2} ℜ(1 − (ρ/(ρ−τ))^n)
                    + ℜ(1 − (ρ₁/(ρ₁−τ))^n)                        [last term iff ρ₁ exists].

Then: (i) the first sum is bounded by Theorem 2.1 (the "large height" estimate) as < K_{F,1}(τ) n log n;
(ii) the second sum is bounded trivially by 2 per zero and then by the explicit zero count (3) at height
T(n) = neτ, giving < K_{F,4}(τ) n log n; (iii) the third sum is the "detection" term, bounded below via
Lemma 2.2. Hence: no off-line zero ⟹ |ℜλ| < (K_{F,1}+K_{F,4}) n log n; an off-line zero with |w| ≥ R ⟹
|ℜλ| ≥ (K_{F,1}+K_{F,4}) n log n for some n ∈ [N,5N] with N | n.

## 3. Exactly where "at most one" is used — three loci

**Locus A (classification; the real use).** The proof begins: "For all zeros ρ ≠ ρ₁ of the function F(s)
we have |ρ/(ρ−τ)| ≤ 1 and thus ℜ(ρ) ≤ τ/2." This single sentence is what licenses restricting *both*
explicit sums in (37) to the half-strip {0 ≤ ℜ(ρ) ≤ τ/2}: with at most one exception, the sum over that
half-strip misses nothing. Equivalently, it licenses pulling out **one** term.

**Locus B (the bound that doubles).** The step Σ_{|ℑρ|≤T(n), 0≤ℜρ≤τ/2} ℜ(1 − (ρ/(ρ−τ))^n) ≤ Σ 2 uses
|1 − w^n| ≤ 1 + |w|^n ≤ 2, which requires |w| ≤ 1 for **every zero in the sum**. That estimate is valid
precisely because Locus A removed all zeros with |w| > 1 except ρ₁.

**Locus C (single-term detection).** The lower bound is quoted as: "Similarly as in the proof of
Theorem 2.3, we obtain ℜ(1 − (ρ₁/(ρ₁−τ))^n) ≤ 1 − (1/20)R^n for some n ∈ [N, 5N] with N | n." The "5"
here is exactly 5M of Lemma 2.2 with **M = 1**.

## 4. The engine is *already* a finitely-many statement

**引用** Lemma 2.2 (source p. 6; = H. L. Montgomery, *Ten Lectures on the Interface between Analytic
Number Theory and Harmonic Analysis*, CBMS 84, AMS 1994, Ch. 5, Theorem 11; **not read here** — quoted
only as stated in the source). Let M ≥ 1 and let z₁,…,z_M be complex with **max_j |z_j| = 1**. Then

    max_{1≤n≤5M} ℜ( Σ_{j=1}^{M} z_j^n ) ≥ 1/20.

**推导** This is the crux: the pigeonhole engine driving *detection* is a statement about M complex
numbers, uniformly in M. Nothing in Lemma 2.2 assumes M = 1. The "at most one" therefore does **not**
protect the engine; it only (a) makes the exceptional term a single summand (Locus A) and (b) keeps the
factor 2 in Locus B applicable. Both are bookkeeping, not mechanism.

## 5. The modified statement that survives

**推导 (closed 2026-09-12: the closed form of N_m is now re-derived — see §5b).**
Fix an integer m ≥ 1. Let F satisfy conditions (a)–(d) and τ > 1/e. Suppose F has **at most m** zeros
with |ρ/(ρ−τ)| > 1, and suppose (if any exist) that R > 1 is such that max_j |ρ_j/(ρ_j−τ)| ≥ R. Then

    some zero has |ρ/(ρ−τ)| ≥ R  ⟺  |ℜ(λ_F(n,τ))| ≥ (K_{F,1}(τ)+K_{F,4}(τ))·n·log n
                                    for at least one n ∈ [N_m, 5m·N_m] with N_m | n,

where N_m is the published N with the constant 40(0.5 + K_{F,1} + K_{F,4}) replaced by
40(K_{F,1} + K_{F,4}) + 20m.

**推导** Proof sketch. Only the (⟹) direction changes.
(i) Decomposition: (37) is unchanged, with its last term replaced by Σ_{j=1}^{m} ℜ(1 − w_j^n), w_j = ρ_j/(ρ_j−τ).
(ii) (⟸) direction needs no change: if no zero has |w| > 1, every zero satisfies ℜρ ≤ τ/2, so both sums in
(37) capture all zeros, Locus B applies verbatim, and the bound (K_{F,1}+K_{F,4}) n log n is obtained with
unchanged constants.
(iii) Detection. Put R′ := max_j |w_j| ≥ R and z_j := w_j^{N_m}/R′^{N_m}, so max_j |z_j| = 1 exactly. Lemma 2.2
gives k ∈ [1,5m] with ℜ(Σ_j z_j^k) ≥ 1/20; set n = k·N_m ∈ [N_m, 5m N_m]. Then

    Σ_{j=1}^{m} ℜ(1 − w_j^n) = m − R′^n ℜ(Σ_j z_j^k) ≤ m − (1/20) R^n.

So |ℜ(λ_F(n,τ))| ≥ (1/20)R^n − m − (K_{F,1}+K_{F,4}) n log n, and the claim follows from
R^n ≥ 40(K_{F,1}+K_{F,4}) n log n + 20m, i.e. (using n log n ≥ 1 for n ≥ e) from
R^n ≥ n log n · [40(K_{F,1}+K_{F,4}) + 20m].
(iv) **Consistency check at m = 1** (推导): 40(K_{F,1}+K_{F,4}) + 20·1 = 40(0.5 + K_{F,1} + K_{F,4}), and
[N₁, 5·1·N₁] = [N, 5N]. The generalized statement degenerates to Theorem 4.1 exactly, constant for constant.

## 5b. The constant-level gap, CLOSED (2026-09-12)

**引用** The source's own three-scale comparison, extracted verbatim from p. 20 (proof of Theorem 4.1):

    We want to prove that the previous formula is at least (K_{F,1}(τ)+K_{F,4}(τ)) n log n
    for all n ∈ [N, 5N].  It is sufficient to show
        R^n ≥ 40 n log n (1/2 + K_{F,1}(τ) + K_{F,4}(τ)).
    This can be equivalently written as
        (2/3)logR + (1/4)logR + (1/12)logR
          ≥ log n / n + log log n / n + log(40(0.5 + K_{F,1}(τ) + K_{F,4}(τ))) / n.
    This follows similarly from the assumptions for the number n as result (21) in the proof of
    Theorem 3.1.  Also, the coefficients 2/3, 1/4 and 1/12 are selected because of the similar
    reasons ... Indeed, the term log n grows faster than the term log log n, this grows faster
    than a constant term and for all n ≥ e we have 3 log n ≥ 8 log log n.

**推导** The three parts are what the earlier version of this note asserted without re-deriving.
Substituting the extension's constant C(m) := 40(K_{F,1}+K_{F,4}) + 20m (which is the constant the
right-hand side of the sufficient inequality acquires in §5(iii)):

    (a)  log n / n        ≤ (2/3) log R     — from the W₋₁ term in N (independent of C) **unchanged**
    (b)  log log n / n    ≤ (1/4) log R     — from 3 log n ≥ 8 log log n together with (a) **unchanged**
    (c)  log C / n        ≤ (1/12) log R    ⟺  n ≥ 12 log C / log R     **with C → C(m)**

So parts (a) and (b) never see the constant, and part (c) reproduces the published 12-term form
with C replaced by C(m). The closed form therefore *is*

    N_m = ⌈ max{ T₀/(eτ), exp(−W₋₁(−(2/3)·log R)), 12·log(40(K_{F,1}+K_{F,4}) + 20m)/log R } ⌉

**核验** `scripts/E4b_palojarvi_constant.py` → `scripts/E4b_palojarvi_constant.txt` (all numbers from there):
1. **m = 1 degeneracy is EXACT**: for five parameter sets, C(1) = 40(K₁+K₄)+20 and the published
   40(0.5+K₁+K₄) agree to the last floating-point bit (relative difference exactly 0).
2. **The inequality holds on the WHOLE window**, as the theorem requires (detection supplies only
   *some* n): scanned every (m, K₁, K₄, R) in a grid of 60 cases over n ∈ [N_m, 5m·N_m]; the worst
   log-ratio is **+32.13** (m = 1, K₁ = 0.1, K₄ = 0.2, R = 1.5), i.e. the ratio R^n/(C(m)·n·log n)
   exceeds 1 by a factor e^{32.13} ≈ 9×10¹³. No case fails.
3. **The minimum sits at the LEFT endpoint** n = N_m, because R^n/(n log n) is increasing for n ≥ e;
   so widening the window by the factor m costs nothing — the cost of m is entirely in C(m) and in
   the 5m of Lemma 2.2.
4. **The cost of m is logarithmic**: with K₁ = 1, K₄ = 2, R = 2, N_m/N₁ runs 1.00 (m=1) → 1.16
   (m=10) → 1.55 (m=100) → 3.40 (m=10⁶). The linear factor is only the window and the 5m.
5. **Control: the 12 is load-bearing.** Replacing 12 log C / log R by the naive ⌈log C / log R⌉
   fails at the left endpoint (log-ratio −2.2 to −3.4), so the comparison is not vacuous — the 12
   is exactly the reciprocal of the (1/12) slot, and the need for it comes from the *n log n* factor
   on the right-hand side, not merely from C.

**⚠️ Honest note on tightness** (核验): the margins in (2) are enormous (e^{32} and up), so the
published form 12 log C / log R is **sufficient but far from optimal**; a much smaller threshold
would also work. This note does not claim optimality of the constant — only that the published
closed form, with C replaced by C(m), is valid.

## 6. What is genuinely new input, and what I did not verify

- **New hypothesis, not new mechanism.** The generalization is *conditional on an a priori bound m* on the
  number of zeros with ℜρ > τ/2. For Dirichlet L-functions m = 1 is available classically (McCurley 1984;
  Brown, Cor. 1 — both cited by the source); for a general F no such explicit bound is known. So the
  generalized theorem is *provable* but only *applicable* when an external count of off-line zeros is
  supplied — which is close to the kind of input the whole τ-Li framework was built to avoid needing.
- **Financial cost of m.** The n-window stretches linearly in m ([N, 5mN]) and the constants inside N grow
  linearly in m. This is exactly what Lemma 2.2's "5M" forces; it cannot be avoided by rescaling.
- **~~Not verified here (honest gap).~~ CLOSED 2026-09-12 — see §5b.** The step that converts
  "R^n ≥ n log n · C" into the closed form of N is result (21)-type in the proof of Theorem 3.1, with the
  split log R = (2/3)log R + (1/4)log R + (1/12)log R. The comparison has now been re-run at constant
  C(m) := 40(K_{F,1}+K_{F,4}) + 20m: parts (a),(b) do not involve C, part (c) is exactly the 12-term with C
  replaced, and the resulting closed form is verified numerically on the whole window (§5b, items 1–5).
  The only thing *not* claimed is optimality of the constant.
- **R vs R′.** The source's hypothesis uses a *lower* bound R for the exceptional modulus; detection uses
  the *maximum* R′. I used R′ ≥ R, which is legitimate but means the generalized hypothesis must read
  "∃ zero with |w| ≥ R", not "the (unique) zero has |w| ≥ R".

## 7. Verdict on the registered claim ("has precedent and is bounded")

**推导** The claim **survives contact with the proof**, and for a clean reason: the only load-bearing use of
"at most one" is the bookkeeping in Locuses A and B, while the detection engine (Lemma 2.2) is already
stated for M numbers. The extension costs an a priori bound m, a factor-m longer n-window and m-degraded
constants, and it reproduces Theorem 4.1 exactly at m = 1. The precise obstruction is therefore not in the
proof but in the *hypothesis*: m is a new, non-trivial input, and for general F it is not known.

**Single most useful sentence for a reader deciding whether to invest:** the "at most one" in Palojärvi's
Theorem 4.1 is used only to pull a single term out of a sum and to charge every remaining zero at 2 apiece
by the explicit zero count — because the actual detection engine, Lemma 2.2, is a statement about M complex
numbers — so the extension to finitely many zeros is a genuine, cheap generalization, but it buys nothing
unless you can independently bound the number of off-line zeros.

## 8. Boundaries

**引用** Theorem 4.1, formula (37), K_{F,4}(τ), Lemma 2.2 as quoted, the three proof loci, and the
"equivalent condition" remark. · **推导** §5 (modified statement, m = 1 consistency check), §6 (m as new
input), §7 verdict. · **未读** Montgomery, *Ten Lectures*, Ch. 5 Thm 11 (Lemma 2.2's proof); Brown 2005;
McCurley 1984. · **核验** none — this item is proof-level, not numerical. · No git commit; no existing file
modified.
