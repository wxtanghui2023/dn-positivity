# E39b / B5-3 — Full-text audit of arXiv:2411.16777 (2D Ising model ⟺ zeta zeros)

**Registered as:** item **E39b** (completion of E39, `docs/EXPLORATION-POINTS-REGISTER.md`) and item **B5-3**
(`docs/PENDING-ITEMS-MASTER.md`, `docs/B5-2-physical-route-audit-criteria.md`).
**Relation to earlier audits:** this note *upgrades* `docs/E39-AUDIT-v2-complete.md` where the full text
changes a detail, and leaves the rest of that audit standing. Readers should treat this as the current
state of E39/B5-3.
**Labels:** `[核验]` verified here · `[引用]` quoted from a source · `[推导]` read/derived here · `[猜想]` conjecture.

**Retrieval record (2026-09-12).** Obtained: the arXiv abstract page of 2411.16777 and roughly one third of the PDF text — Definition 1 and Theorems 1–5 with the openings of their proofs, the complete closing argument of Theorem 5, the proof passage of Theorem 4, and the paper's own "main obstacle" passage. **Not obtained:** the HTML rendering — `arxiv.org/html/2411.16777` returns "*No HTML for '2411.16777'. HTML is not available for the source*", and `ar5iv.labs.arxiv.org/html/2411.16777` has no copy and redirects to the abstract. Also not obtained: the middle of the paper (§3.1 Hamiltonian/transfer-matrix algebra, Eqs. (12), (34), (40)) and the appendices. **Consequence: each criticism below is checked against the full text of the step it names; the internal algebra remains at the earlier partial reading.**

**Metadata correction.** `docs/E39-AUDIT-ising-zeta-claim.md` recorded that the paper was not peer reviewed. The arXiv page now carries a journal reference, **Phys. Lett. A 591 (2026) 131910** (v4, 16 Aug 2026, 46 pages). `[引用]` A journal reference does not by itself establish any claim audited below; it corrects only that one metadata statement.

**Caveat on all quotations.** The source text is untrusted external material, quoted as retrieved; PDF extraction renders fractions and indices lossily, so sub/superscripts are normalised silently.

---

## §1 The numbered claims, as stated in the full text `[引用]`

1. **Definition 1.** `M^{2D}_{FI+SGI}`: nearest-neighbour interactions **ferromagnetic along one
   crystallographic direction**, while **randomly distributed competing ferromagnetic/antiferromagnetic
   interactions** act along the other.
2. **Theorem 1 (Equivalence Theorem).** "The zero distribution of the partition function of the 2D Ising
   model `M^{2D}_{FI+SGI}` is equivalent to the zero distribution of the Dirichlet function `L(s,χ_k)`
   (including the Riemann zeta function `ζ(s)`)."
3. **Theorem 2 (Real Eigenvalues).** "All energy eigenvalues of the 2D Ising model `M^{2D}_{FI+SGI}` are
   real, which are randomly distributed as the Riemann zeta function `ζ(s)`."
4. **Theorem 3 (Hilbert–Pólya Space Theorem).** "The eigenvectors of the 2D Ising model `M^{2D}_{FI+SGI}`
   are constructed by the eigenvectors of the 1D Ising model with phases related to the Riemann zeta
   function `ζ(s)`." (The proof displays the 2n-normalised vectors (35), (36) with phase factors
   `exp(iω_{2j})` and `exp(±iδ'_{2j}/2)`.)
5. **Theorem 4 (Unit Circle – Critical Line).** All zeros of the partition function lie on a **unit circle**
   in the complex temperature plane (Fisher zeros); the circle "can be mapped into the critical line".
6. **Theorem 5.** "The nontrivial zeros of the Dirichlet function `L(s,χ_k)` (including … `ζ(s)`) is the
   spectrum of an operator, **R = ½I + iH**, where `I` is the unit matrix and `H` is a self-adjoint operator
   interpreted as the Hamiltonian of the 2D Ising model `M^{2D}_{FI+SGI}`."
7. **Conclusion.** Five theorems are enumerated, ending: "we have proven the closure of the nontrivial zero
   distribution of the `L(s,χ_k)` function (including the Riemann zeta function `ζ(s)`)." `[引用]`

Two structural steps are quoted verbatim in the paper's own words later: the mapping
"`u = s/(1−s) = (½+it)/(½−it) → s`", and the identification "the change of the Hamiltonian `H` (and thus the
partition function `Z̄`) by scanning all replicas is equivalent to the change of the character `χ_k` all the
way in the Dirichlet function `L(s,χ_k)`". `[引用]`

---

## §2 The criticised steps, and whether the criticism survives

### C1 — Theorem 5's closing argument (earlier finding F1: circularity). **Survives, unchanged.** `[推导]`
The complete closing step reads (quoted from the PDF text; its opening clause was first recorded in `docs/E39-AUDIT-v2-complete.md` §3 and is reproduced here from the same passage): "…**it is verified that no nontrivial zeros lie off the critical line.**
However, this ensures only the imaginary part of R, while the real part needs to be fixed. … Hardy proved
that infinitely many zeros lie on the critical line. Up to date, 100 billions nontrivial zeros have been
found to lie on the critical line with the real part as 1/2. The Hardy's result and the computation of the
nontrivial zeros … **fixes already the real part of R.** If our critical line is located at σ = 1/2, it will
be consistent with the Hardy's proof and the computation …, else it will be contradictory with them.
**This excludes the possibility that the critical line is off σ = 1/2. Therefore, we have proven the
Hilbert-Pólya conjecture.**" `[引用]`
The criticism is exact and unweakened: the opening sentence *is* the Riemann hypothesis; Hardy's theorem
supplies **infinitely many** on-line zeros, not all; the numerical verification covers the first ~10¹¹–10¹²
zeros, not all heights; and "consistent with" is not "implied by". The step presupposes its conclusion.
Contact with the full text **sharpens** rather than softens this: "no nontrivial zeros lie off the critical
line" is not a lemma but an assumption introduced inside the proof of the theorem that asserts it.

### C2 — Theorem 1, the equivalence. **Survives; its exact step is now quotable.** `[推导]`
The substantive step is the replica/disorder argument quoted in §1 ("scanning all replicas ⟺ changing
`χ_k`"). The earlier audit's point was that the equivalence *is* the whole difficulty; the full text
confirms this in the author's own words: "the **main obstacle** of the path is to find an appropriate model
to satisfy the condition that the zero distribution of the partition function is equivalent to the
distribution of the nontrivial zeros of the Riemann zeta function." `[引用]` Writing down a Hamiltonian and
its partition function does not discharge an equivalence of zero *distributions*.

### C3 — Theorem 4, the unit circle. **Survives; the quoted defence addresses the wrong hypothesis.** `[推导]`
The step: "all the zeros of the partition function `Z̄_α` of the 2D Ising model `M^{2D}_{FI+SGI}` in a fixed
replica lie on a unit circle in the complex temperature plane … The partition function `Z` can be calculated
from the product of the partition functions `Z̄_α` … `Z = ∏_{α=1}^{R} Z̄_α`. Thus, all the zeros of the
partition function `Z` … lie on a unit circle." `[引用]`
The full-text defence is: "Note that in the Lee-Yang Theorem for the unit circle, **no assumptions were made
about (1) the range of the interaction u, (2) the dimensionality of the lattice, (3) the size and structure
of the lattice and (4) even the periodicity property** of the lattice." `[引用]` That part is true — Lee–Yang
does not need a bounded range, a fixed dimension, or periodicity — but the **binding hypothesis of the
circle theorem is positivity (ferromagnetic/Markov)**, which a "randomly distributed competing
ferromagnetic/antiferromagnetic" direction does not supply. The quoted sentence removes hypotheses that were
never the binding ones. **Finding F2 stands**, and the full text supplies the exact sentence that shows where
the defence mis-aims.

### C4 — Theorem 2. **Survives.** `[推导]`
"randomly distributed as the Riemann zeta function `ζ(s)`" (Theorem 2, v4) names no statistic — no empirical
spectral measure, no pair-correlation function, no moment sequence. The abstract widens the claim ("as the
Möbius function `μ(n)`, the Dirichlet `L(s,χ_k)` function as well as … `ζ(s)`"), which does not repair it:
`μ(n) ∈ {−1,0,1}` carries no distributional normalisation. **Finding F3 stands.**

### C5 — Theorem 5's operator. **Partially corrected in the paper's favour; the spectral identity is still unproved.** `[推导]`
This is the one place where the earlier audit must be **upgraded**: the earlier statement was that no
self-adjoint operator with a spectral identity is exhibited, and the v4 text *does* name `R = ½I + iH` and
*does* assert `H` self-adjoint. What is still missing is a proof of self-adjointness and of the identity
`spec(R) = {nontrivial zeros}`: the theorem's proof routes the identification through C1's circular step
("Theorem 2 shows that the model … is a suitable system for proving the Hilbert-Pólya conjecture"),
and C1 is precisely where the real part is fixed by consistency with Hardy plus numerics. So finding F4 is
**narrowed**: "no operator named" is **withdrawn**, with evidence; "no proof of the spectral identity"
**survives**.

### C6 — the circle → line map. **Survives.** `[推导]`
The map `u = s/(1−s)` is the classical equivalence `|u| = 1 ⟺ |1 − 1/ρ| = 1 ⟺ Re ρ = 1/2`, which is also the
project's own elementary identity (`docs/E18-NOGO-ALIGNMENT.md` §1). It restates a known criterion of RH
rather than supplying a proof of it. **Finding F5 stands.**

---

## §3 Verdict `[推导]`
The paper's main claim is **not established by its published argument**, on the same three grounds as the
earlier audit — C1 (the closing argument presupposes the conclusion), C2 (the equivalence is asserted, and
named by the author as the obstacle), C3 (the unit-circle conclusion lacks its positivity premise, and the
quoted defence addresses non-binding hypotheses). **One earlier item is corrected in the paper's favour**
(C5: the operator `R = ½I + iH` is exhibited; only the spectral identity remains unproved) and **one
metadata statement is corrected** (a journal reference now exists). Nothing here is a disproof: the claim is
unproven as published, not false. The audit concerns the published reasoning chain, not the authors'
honesty — the paper itself names the equivalence as the obstacle.

## §4 What still rests on the abstract or on partial text
`[核验]` The statements of Definition 1 and Theorems 1–5, and the criticised steps of C1–C4 and C6, are
quoted from the full (PDF) text. **Not obtained:** the §3.1 Hamiltonian/transfer-matrix algebra, Eq. (12),
Eq. (34), Eq. (40), and the appendices. Hence the audit recomputes no eigenvalue count and makes no numerical
claim about this model's couplings. The project's total-positivity result (`TP₅`, seven negative minors at
120 digits, `docs/E23-lee-yang-dqpt-report.md` §4) is an *instrument* and an analogy here — it concerns the
kernel `Φ`, not the couplings of `M^{2D}_{FI+SGI}` — so it is **not** an independent verification for
2411.16777. `[推导]`
**"Not found" is not "does not exist":** the absence of a positivity certificate for these couplings is
recorded as "not found in the retrieved text", never as a claim that none exists.

**One-line summary.** With about a third of the full text in hand, the earlier audit's decisive findings
survive contact; the single reversal is that Theorem 5 does name the operator `R = ½I + iH`, while its
spectral identity is still routed through the circular closing step.
