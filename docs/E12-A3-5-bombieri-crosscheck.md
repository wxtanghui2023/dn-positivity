# E12 / A3-5 — the project's inertia series against Bombieri's published observation

**Labels:** 核验 = checked here or in-repo; 引用 = quoted from an external source; 推导 = derived in this note; 猜想 = conjecture.
**Sources actually read for this note:** E. Bombieri, "Remarks on Weil's quadratic functional in the theory
of prime numbers. I", Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl. (9) **11** (2000), no. 3, 183–233
(2001) — the article was retrieved at source (abstract, §8 with Lemma 10 and (8.3)–(8.15), Theorem 8,
Theorem 9, §10); B. Conrey, survey "Riemann's Hypothesis" (AIM, `aimath.org/~kaur/publications/90.pdf`),
discussion of Bombieri's finite approximations; arXiv:2608.13637v2 §1.3 and the (Z) display.
In-repo: `docs/ALIGN-A3-weil-positivity-inertia.md`, `docs/ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`,
`docs/ERRATUM-inertia-factor2.md`, `docs/p27g1`, `p27g4`, `p27g6`, `p27g7`, `p27g8`, `p27g82`,
`p28a-inertia-transfer.md`, `p33-moving-edge-obstruction.md`, `p33b-moving-edge-strict.md`,
`p27p33-fourfold-audit.md`.
**Not claimed:** nothing below proves or disproves RH.

## 1. The published observation, quoted with location

[引用] Bombieri [Bom00], **Theorem 8** (§8, in the article's journal pages ≈ 210–213):
> "The number of negative eigenvalues of the matrix $H(\Gamma;t)$ equals the number of distinct complex
> conjugate pairs $(\gamma;\bar\gamma)$ in $\Gamma$."

[引用] Bombieri [Bom00], **Theorem 9**:
> "Let $E$ be a finite union of bounded closed intervals. Then the number of negative eigenvalues of
> $K_E(\Gamma)$ equals the number of distinct complex conjugate pairs $\{\gamma;\bar\gamma\}$ in $\Gamma$.
> Suppose also that $E$ is symmetric. Then the number of negative eigenvalues of $K^+_E(\Gamma)$ equals the
> number of distinct complex conjugate pairs $(\gamma;\bar\gamma)$ with $\Im(\gamma)>0$ [and likewise $K^-_E$]."

[引用] Bombieri [Bom00], **Abstract** — the decisive calibration:
> "... if the Riemann Hypothesis is false but only with finitely many non-trivial zeros off the critical
> line we show that the number of negative eigenvalues is precisely one-half of the number of zeros failing
> to satisfy the Riemann Hypothesis, provided the truncation is big enough."

[引用] Bombieri [Bom00], **§8 setting**: $\Gamma$ is a multiset of complex numbers with
$\sum 1/(1+|\gamma|)^{1+\varepsilon}<\infty$ and the symmetries $\Gamma=\bar\Gamma$, $\Gamma=-\Gamma$;
**Lemma 10**: $H(\Gamma;t)$ has eigenvalue $0$ iff some $\gamma$ occurs with multiplicity $>1$, the
multiplicity being $\sum'[m(\gamma)-1]$, and "if every $\gamma$ is real all eigenvalues of $H(\Gamma;t)$ are
non-negative"; the proof rests on (8.14)–(8.15), $F(u)=Z(u)-Ae^{u/2}-Be^{-u/2}$.

[引用] Bombieri [Bom00], **§10** ("The passage to the limit"): for $\Gamma$ with finitely many, but at least
one, complex pair, the truncation $H(\Gamma_N;t)$ has at least one negative eigenvalue $\lambda_N<0$.

[引用] Conrey's survey, in the Bombieri discussion: "He shows that all of the eigenvalues $\Lambda$ are real,
and that if all of the $\gamma\in\Gamma$ are real then all of the eigenvalues $\Lambda$ are positive. In
fact, the number of non-real pairs of conjugate $\gamma$ is exactly equal to the number of negative
eigenvalues." (Exact printed page not pinned: the fetched extraction carries the running heads "32 BRIAN
CONREY" and, later, "RIEMANN'S HYPOTHESIS 47", so the sentence lies in the vicinity of p. 32.)

[引用] Frontier paper arXiv:2608.13637v2, §1.3: "That the negative index of truncations of Weil's form
counts off-line zeros is due to Bombieri [Bom00]; we use rank and positive index." And in the (Z) display:
"each off-line pair $\{\rho,1-\bar\rho\}$ [contributes] a block of signature $(1,1)$ to $Q$."

## 2. The one-or-two-per-pair question, calibrated

[推导] Bombieri's $\Gamma$ for the zeta zeros is the multiset of $\gamma$ with $\rho=\tfrac12+i\gamma$ (this
is forced by his symmetries: the zeros $\rho$ themselves do not satisfy $\Gamma=-\Gamma$). One off-line
orbit $\{\beta+i\gamma_0,\ \beta-i\gamma_0,\ (1-\beta)+i\gamma_0,\ (1-\beta)-i\gamma_0\}$ maps to the four
$\gamma$-values $\{\gamma_0\pm i\delta,\ -\gamma_0\pm i\delta\}$, $\delta=\tfrac12-\beta\ne0$, which form
**two** distinct conjugate pairs, $\{\gamma_0\pm i\delta\}$ and $\{-\gamma_0\pm i\delta\}$.

[推导] Calibration: one orbit contains **four** zeros failing RH, so the abstract's "one-half of the number
of zeros failing to satisfy the Riemann Hypothesis" gives **2**. Theorem 8 gives the same 2 (two distinct
conjugate pairs per orbit). The two sentences in Bombieri's own paper therefore agree:

> **Answer to the flagged unresolved point:** the published observation's "non-real pair" is a conjugate
> pair $\{\gamma,\bar\gamma\}$, equivalently a functional-equation pair $\{\rho,1-\bar\rho\}$ of zeros, and
> it corresponds to **one** negative direction. A full four-point orbit contains two such pairs, hence
> **two** negative directions. This matches the frontier's (Z) block of signature $(1,1)$ *per off-line
> pair*.

[推导] Consequently the repo's original assertion $n_-(K_\rho)=1$ **per orbit** did **not** match Bombieri's
count, and the ERRATUM's corrected value (**two per orbit**, `ERRATUM-inertia-factor2.md` §2: sector block
$2I-4\cdot\mathbf{1}$, eigenvalues $2,2,-10$) **does** match it. The ERRATUM's open worry — "if 'a pair'
corresponds to one orbit then $n_-$ should be 1" — is thus resolved *in favour of the ERRATUM*: a pair is
not an orbit.

## 3. Per-item classification of the P27 series

[核验] What the series asserts (in-repo):
- **(A)** $n_-(K_\rho)$ per off-line orbit — G8.1 gave **1** (`p27g8`); corrected to **2**
  (`ERRATUM-inertia-factor2.md`).
- **(B)** quartet structure — G6: $K_{\delta,\gamma}=K_{\delta,-\gamma}=K_{-\delta,\gamma}=K_{-\delta,-\gamma}$,
  $Q_{\delta,\gamma}=4D_\rho$; G7.1: $K_N$ has rank $\le 6N$.
- **(C)** moving-edge non-transference — P28–P33: finite inertia $n_-(K_N)=N$ (corrected $2N$) with
  $n_-(K_{\text{off}})$ undetermined; `p33b` gives a strict block-diagonal counterexample family.
- **(D)** 2×2 negative-witness family — G4: the 2×2 Gram on a positive measure is PSD, so there is no
  negative witness; witnesses need complex measures, higher dimension, or non-Hermitian structure.
- **(E)** $n_-(K_{\text{off}}(N))=\#\{\text{distinct off-line quartets}\}$ — G8.2′.

[推导] Classification:
- **(A) → (b) an independent derivation of the same fact** (after the erratum). Its content coincides with
  Bombieri's Theorem 8 read per conjugate pair; it was derived in-repo without citing [Bom00]; it is not new.
  The pre-erratum value 1 is **(d) not comparable** — an internally identified bookkeeping error, not a claim
  about the published observation.
- **(B) → (d) not comparable** as a statement about the count: it is in-repo bookkeeping about the project's
  own kernel ($\gamma$-sign symmetry, rank bound). The quartet symmetry is exactly Bombieri's hypothesis
  ($\Gamma=\bar\Gamma$, $\Gamma=-\Gamma$) re-expressed, so it re-instantiates rather than extends. The G6
  "collective phase cancellation" conclusion is additionally only a 猜想 (quasi-uniformity assumed).
- **(C) → (c) genuinely additional.** Bombieri's §10 limit statement covers *finitely many* complex pairs;
  the P28–P33 non-transference concerns the regime where negative directions accumulate on a moving edge with
  margin → 0, which his theorems do not cover. Honest caveat: the abstract proposition is a candidate, and the
  sharp counterexamples are block-diagonal models, not ζ's kernel.
- **(D) → (b)** — an independent confirmation in a special (2×2, positive-measure) case, plus a project-internal
  negative finding (no witness there).
- **(E) → (b)** — a restatement of Bombieri's count in the in-repo language (distinct off-line quartets /
  conjugate pairs / functional-equation pairs).

## 4. What would settle the remaining doubt (the one decisive item)

[推导] The pairing itself is settled by §2. What is **not** settled here is the **unit/normalisation match**
between the two counts:
- Bombieri's $H(\Gamma;t)$ is a matrix indexed by $\gamma\in\Gamma$ with the quadratic form of his
  (8.14): $\lambda\sum_{\gamma\in\Gamma}|w_\gamma|^2=\tfrac14\int_{-t}^{t}|F|^2du+\int_{-t}^{t}|F'|^2du$;
  its negative index is a count in **those** units.
- The project's $n_-(K_\rho)$ is computed with a Gram/inner product that `ERRATUM-inertia-factor2.md` §4
  records as **undocumented** for the companion series (P28-A, P31, P32); the verified factor-2 script uses one
  explicit Gram.

**Decisive question.** Is the project's per-orbit negative inertia, computed in a normalisation matching
Bombieri's $H(\Gamma;t)$, equal to two? Concretely: (i) fix the project's inner product; (ii) recompute
$n_-(K_\rho)$ in that normalisation (`scripts/G6_verify_inertia_factor2.py` already returns 2 with the
sector-block Gram — the open step is to show that this Gram corresponds to Bombieri's (8.14) units); (iii) if
it does, the series reproduces Bombieri's count exactly and item (A) upgrades from **(b) to (a)**.

[推导] **Second, independent gap** (from `p27p33-fourfold-audit.md`, verdict P-C): Bombieri's theorem holds
for an *arbitrary* $\Gamma$ carrying the two symmetries, hence is uniform in the configuration, whereas the
project's $K_\rho$ is built *from* $\delta$ — so its "off-line ⟹ negative" is a definition-level consequence
and its derivation is a **special-case re-derivation**, not a reproduction of the general theorem. This is a
difference of scope, not of count.

[推导] Bottom line: the corrected project count (two per orbit) is consistent with — and is a special-case
re-derivation of — Bombieri's 2000 observation; the one item that would fully close the cross-check is the
normalisation match just stated. RH is not addressed, and nothing here proves or disproves it.

## 5. Boundaries

[核验] Bombieri's abstract, Lemma 10, (8.3)–(8.15), Theorem 8, Theorem 9, §10 — read from the article PDF
(bdim.eu id `RLIN_2000_9_11_3_183_0`); page markers 209/210/213 appear in the extracted text.
[引用] Conrey's sentence as quoted; its exact printed page could not be pinned (the extraction mixes running
heads). [核验] in-repo: p27g1/g4/g6/g7/g8/g82, p28a, p33/p33b, ERRATUM, fourfold audit.
[未读] Bombieri §1–§7 as a whole; the full derivation of (8.14); [Yos92]; [Bom03]; [Bom05].
[推导] §2 calibration, §3 classification, §4 decisive question.
