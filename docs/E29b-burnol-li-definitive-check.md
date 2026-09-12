# E29b / A5-4 (definitive source check) — Burnol's projection framework vs Li's criterion

**Date:** 2026-09-12. **Question (E29 / A5-4):** "查证 Burnol↔Li 同构是否已见于文献". This note is the
follow-up to `docs/E29-A5-4-burnol-li-isomorphism-check.md`, whose §5 listed the exact sentences to look for
and whose verdict was *partial* because Burnol's full text had not been read.
**Labels used below:** 核验 (checked against a source read in this pass) · 引用 (quotation) · 推导 (our derivation) · 猜想 (conjecture). Nothing here proves, disproves, or bears on the truth of RH.

## 1. The source was obtained in full

- Jean-François Burnol, *A lower bound in an approximation problem involving the zeros of the Riemann zeta
  function*, **arXiv:math/0103058v2**, 17 pp. Open access. PDF fetched (151 216 bytes, SHA-256
  `999f05d5045fd909c3fb985677c4e40459f2a8b1e8b7d932f34b35bdc52d6e7d`) and converted to text. 核验.
- Refereed version: Adv. Math. **170** (2002), no. 1, 56–70; DOI 10.1006/aima.2001.2066. 引用. The arXiv note says
  v2 "adds two references. No mathematical changes", so the mathematics quoted is that of the published paper.
  The paywalled typeset text was **not** read page by page; instead the published bibliography was pulled from
  Crossref (§4). Quotations are from §§1–5; section numbers are Burnol's own.

## 2. The distance functional and the projection vectors (quoted)

**Distance functional** (§1 Thm 1.2, credited to Báez–Duarte–Balazard–Landreau–Saias; §3 identifies it with a
*projection* quantity in the span C_λ of the contractions D_θ(A), λ≤θ≤1): 引用
> "Let us write D(λ) for the Hilbert-space distance inf_{f∈B_λ}‖χ−f‖. We have lim inf_{λ→0} D(λ)√(log(1/λ))
> ≥ √(Σ_ρ 1/|ρ|²)." — with §3: "the Hilbert space distance between χ₁(t) and C_λ."

**Projection vectors** (§3, Definition 5.1; the projection asymptotics are computed "exactly as in the
Grenander–Rosenblatt method"): 引用
> "To each zero ρ of the Riemann zeta function on the critical line, of multiplicity m_ρ, and each integer
> 0 ≤ k < m_ρ we associate the Hilbert space vector X^λ_{ρ,k} := (log(1/λ))^{−1/2−k} · Y^λ_{ρ,k}, where
> Y^λ_{ρ,k} = l.i.m._{w→s} V^{−1}Q_λV(ψ_{w,k}), V is a unitary invariant operator, Q_λ is orthogonal
> projection to L²([λ,∞[, dt), and ψ_{w,k}(t) = (log(1/t))^k t^{−w} χ(t)." (In §3, V = (1−M)²U.)

**What k means** (§4, Corollary 4.4): 引用
> "The vector Y^λ_{s,k} is perpendicular to C_λ if and only if ζ^{(j)}(s)=0 for all j ≤ k, if and only if s is
> a zero ρ of the zeta function and k < m_ρ."

So (ρ, k) = a zero ρ plus an *order-of-vanishing budget* k at ρ. The Gram matrix is Cauchy (Thm 5.3:
(X^λ_{ρ₁,k},X^λ_{ρ₂,l}) → 0 for ρ₁≠ρ₂, → 1/(k+l+1) for ρ₁=ρ₂), and the payoff is Thm 5.5:
lim inf_{λ→0} D(λ)√(log(1/λ)) ≥ √(Σ_ρ m_ρ²/|ρ|²). 引用

## 3. Where the (ρ, k) indexing actually comes from: Connes and Hilbert–Pólya, not Li

§1 states the motivation twice, and it is **not** Li: 引用
> "subsists the problem of a natural definition of a so-called 'Hilbert-Pólya space', with orthonormal basis
> indexed by the zeros ρ of ζ and integers k varying from 0 to m_ρ−1 where m_ρ is the multiplicity of ρ.";
> "As in Connes's constructions these vectors live in a quotient space."

The reference list confirms the provenance: the only external structural inputs are Connes [8],[9] (CRAS 323
(1996); Selecta Math. 5 (1999) 29–106), Grenander–Rosenblatt [11] (TAMS 76 (1954) 112–126) and the
Nyman–Beurling/Báez-Duarte line [1]–[3],[14]. 核验. The abstract frames the vectors as "could prove useful in
the context of the so-called 'Hilbert-Polya idea'". 引用

## 4. Negative evidence: Li, Bombieri and Lagarias are simply not in the paper

- Full-text word search of v2 (17 pp.): **0** occurrences of `Bombieri`, `Lagarias`, `Weil` or `criterion`, and
  **0** occurrences of `Li` as a standalone word (the 104 substring hits are inside "limit", "linear", …).
  核验. The v2 bibliography has 14 items; none is Li (1997) or Bombieri–Lagarias (1999).
- The **published** version's deposited bibliography (Crossref, DOI 10.1006/aima.2001.2066, `reference-count`
  = 18, all 18 slots `RF1`–`RF18` populated) contains no item with an identifier pointing to
  Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory **65** (1997)
  325–333 (DOI 10.1006/jnth.1997.2137), nor to Bombieri–Lagarias, *Complements to Li's criterion for the
  Riemann hypothesis*, J. Number Theory **77** (1999) 274–287 (DOI 10.1006/jnth.1999.2392). 核验. Both are
  J. Number Theory articles — a journal that deposits DOIs — and the six DOI-less slots are books/theses/
  manuscripts (Cauchy's Oeuvres, Nyman's 1950 thesis, and similar), so neither could hide there.
- No sentence states or hints that the X^λ_{ρ,k} are Li's test functions, that D(λ) is a Li coefficient, or
  that the two criteria are one object.

## 5. Verdict

**(iii) Apparently absent from that paper.** The source named in
`docs/E29-A5-4-burnol-li-isomorphism-check.md` §5(1) has now been read, and settles the question *as a
literature question* in the negative: Burnol (2002) never mentions Li coefficients, Bombieri–Lagarias, Weil
positivity or "criterion", and gives the (ρ, k) framework a Connes/Hilbert–Pólya motivation instead. The
decisive sentences are Corollary 4.4 (what k means) and the §1 Hilbert–Pólya passage quoted in §3. This is a
*not found* statement about a paper we read, restricted to the arXiv v2 text plus the published deposited
bibliography — not a claim about the whole literature.

## 6. 推导 — shortest derivation sketch of the claimed isomorphism, with its assumptions

Assumptions: (A1) λ_n = Σ_ρ [1 − (1 − 1/ρ)^n] (Li 1997); (A2) on the critical line |1 − ρ| = |ρ|. Neither is
proved here.
- Step 1 (Li side). (1 − 1/ρ)^n = Σ_{k=0}^{n} C(n,k)(−1)^k ρ^{−k}, hence λ_n = Σ_{k≥1} C(n,k)(−1)^{k+1} ρ^{−k}:
  Li's family is indexed by *powers* ρ^{−k} with binomial weights and an order budget of size n.
- Step 2 (Burnol side). Burnol's family is (log(1/t))^k t^{−w} at w → ρ, rescaled by log(1/λ)^{−1/2−k}, with
  order index 0 ≤ k < m_ρ, i.e. bounded by the multiplicity.
- Step 3 (what actually matches). By Theorem 5.4, √(log(1/λ))(χ₁, X^λ_{ρ,k}) → 0 for k ≥ 1 and → (ρ−1)/ρ² for
  k = 0. Only k = 0 survives λ → 0, and ‖Y^λ_{ρ,0}‖² ≈ ∫_λ^1 dt/t = log(1/λ). The √log therefore comes from
  the **scale budget** log(1/λ) of the dilation range [λ,1], *not* from an order budget k ≍ log(1/λ); with
  (A1)+(A2) the squared normalised projection sums to Σ_ρ m_ρ²/|ρ|² / log(1/λ), reproducing Theorem 5.5.
- Step 4 (the bridge, if any). The only reading under which the two meet is that Burnol's scale budget
  log(1/λ) plays the role of Li's index n (a *budget/scale* dictionary), while both index by powers ρ^{−k}
  and an order of vanishing k < m_ρ. This is 推导, not quotation: Burnol never says it. 猜想 = any claim that
  the dictionary upgrades one criterion into the other.

## 7. Consequence for the project

`docs/ALIGN-A4-A5-with-our-results.md` §1/§3 attributes to Burnol a mechanism in which "√log comes from the
order budget k ~ log(1/λ)". On the text just read, that attribution is **not** correct: Burnol's Theorem 5.4
keeps only k = 0 in the limit and derives √log from the scale range [λ,1] with measure dt/t. The project's
*own* suggestion (k ↔ power of ρ) remains 推导. A5-4 closes as: *ingredients published (Li ⟺ Weil positivity:
Bombieri–Lagarias 1999 / Lagarias 2007); Burnol's framework is not presented as a Li framework; the explicit
Burnol–Li isomorphism was not found, and the mechanism previously attributed to Burnol is contradicted by
Theorem 5.4 of the source.*

## 8. Boundary

Read: arXiv:math/0103058v2 full text (17 pp., all sections); Crossref metadata for the published version
(DOI 10.1006/aima.2001.2066) with its 18-item deposited reference list; Crossref records for the Li 1997 and
Bombieri–Lagarias 1999 DOIs. 核验. Not read: the paywalled typeset Adv. Math. text, and (unchanged from the
previous pass) Bombieri–Lagarias 1999 and Lagarias 2007 full texts. "Not found" means *not found in the source
read here*, not "does not exist". Literature check only; no theorem claim.
