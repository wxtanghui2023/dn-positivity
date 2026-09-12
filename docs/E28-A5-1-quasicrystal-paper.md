# E28 / A5-1 — Model alignment: the 2024 quasicrystal-scattering paper (arXiv:2410.03673)

**Date:** 2026-09-12 · **Status:** read at abstract/metadata level plus retrieved HTML fragments of v12 and v4
**Labels:** 核验 = checked in this pass · 引用 = quoted from the source · 推导 = derived here · 猜想 = conjecture
**Warning:** the late versions claim to prove RH. That claim is **not accepted here**, is not independently
verifiable from the text retrieved, and is treated below purely as an object to be audited. The project does
not prove RH and nothing in this note asserts such a thing.

## 1. What the paper is

- Michael Shaughnessy, arXiv:2410.03673, primary class **quant-ph** (cross-listed cond-mat.mtrl-sci, hep-th,
  math-ph). v1 dated 13 Sep 2024; **twelve versions**, v12 dated 23 May 2026. 引用 (arXiv abs page).
- The **title changed**: v1–v6 "Quasicrystal Scattering and the **Riemann Zeta Function**"; the v7/v12 HTML
  headings read "Quasicrystal Scattering and the **Riemann Hypothesis**". 核验. This matters for all below.

## 2. The model (what it actually constructs)

- Scatterers placed at positions χ_n = ln(p_n), "the logarithms of the primes"; the map "compresses the
  primes to approximately constant density". 引用 (abstract v12).
- **Scattering amplitude** χ̂_L(k) = Σ_{n} p_n^{−2πik} — an Euler-type Dirichlet polynomial in the variable
  2πk; "the non-trivial zeros of ζ(s) enter as poles of −ζ′/ζ in the spectral decomposition, producing peaks
  at positions γ/2π". 引用 (abstract v12).
- **Spectral decomposition**, Eq. (12): χ̂_L(k) = Σ_ρ (p_L^{ρ−2πik} − 1) / (ρ(ρ − 2πik)) + R_L(k), where the
  sum is over non-trivial zeros and R_L contains the pole at s = 1 and the trivial zeros,
  R_L(k) = O(p_L^{−1} log p_L). Eq. (13) localises the ρ-term near k ≈ γ/2π as a Lorentzian peak. 引用 (v12 §4).
- **Limiting normalised amplitude**, Eq. (21), x = p_L → ∞:
  χ̃(k) = 1 − Σ_m (x^{β_m − 1/2} e^{iγ_m ln x} / ρ_m) δ(k − γ_m/2π) + O(x^{−1/2}). 引用.

## 3. The claimed result (late versions)

- **Theorem A.6 (Fourier self-duality on S′):** for every f ∈ S′(ℝ), F[F[f]](x) = f(−x) (Eq. (25)) — labelled
  "unconditional". 引用.
- **Proposition A.8 (Bounded peak coefficients):** each coefficient c_m is finite, "equivalently, the
  normalised peak amplitude p_L^{β_m−1/2}/|ρ_m| stays bounded as L → ∞". 引用.
- Deduction, Eq. (28): bounded amplitude ⇒ β_m ≤ 1/2; then self-duality (Eq. (29), F[F[χ]] = χ(−·)) plus the
  functional equation (ρ ↦ 1 − ρ̄) gives β_m = 1/2 — "which forces β_m = 1/2 for every non-trivial zero".
  引用 (abstract v12 + Appendix A fragments).

## 4. The decisive test against the project's central claim

The project's central claim (E18/E19, `docs/E19-model-alignment.md` §2, §6) is that its key object
S(t) = N(t) − N_0(t) carries **no information about real parts**, and that the physical-model analogues it
audited (log-gas, scattering, quasicrystal, DQPT, …) are γ-only.

**Answer to the test: the paper's construction DOES contain a quantity sensitive to the real parts.**
- The coefficient of the m-th peak is proportional to p_L^{β_m − 1/2} = exp((β_m − ½)·ln p_L): an explicit,
  monotone function of Re ρ_m. 引用 (abstract v12; Eq. (21), (28)).
- The paper says so itself in the v4 appendix, as a "projection" table: the scattering map
  "**Preserves**: the imaginary part γ (encoded in peak position)"; "**Transforms**: the real part β into
  peak height scaling as (L_χ log L_χ)^{2β}"; "**Does not constrain**: the values of β". 引用 (v4 Appendix A.3).
- So this paper is **not** another instance of "detection without exclusion" in a β-blind channel: it is a
  construction in which **peak heights are β-visible** while **peak positions are γ-only** — the position/
  height dichotomy already recorded in the pair-correlation audit (commit 908eadb).
- Consequence: as a *construction* the paper is a candidate β-probe, i.e. exactly the kind of entry whose
  audit would test the project's "no β-probe" negative claim. But no working probe is delivered: see §5.

## 5. Where the claimed inference fails 推导

- Theorem A.6 is the elementary distributional identity F∘F = reflection. It is true for **every** tempered
  distribution and therefore constrains **no** size, no decay rate and no coefficient bound. An
  "unconditional" identity of this type cannot by itself imply anything about β.
- The content therefore sits in Prop. A.8, whose retrieved "proof" uses "spacing"/"locally finite measure"
  language: finiteness of total spectral mass on a compact K does not bound **individual** coefficients
  *uniformly* in L = p_L → ∞. And the amplitude is by Eq. (21) proportional to p_L^{β−1/2}; declaring it
  "bounded as L → ∞" is precisely an assumption on β, so the step is circular as retrieved.
- The implication Eq. (28) (bounded amplitude ⇒ β ≤ ½) is only as good as that premise; granted it,
  β ≤ ½ plus the functional equation does give β = ½. So the failure point is upstream, in Prop. A.8.
- Decisive version evidence: **v4 explicitly states the opposite conclusion.** Theorem A.3 (Projection vs.
  Constraint) there reads: "the linear arrangement of spectral peaks on the real k-axis does NOT imply that
  all RZF zeros have β = 1/2"; and "the scattering process acts as a projection … transforms the real part β
  into peak height … does not constrain the values of β". 引用 (v4 Appendix A.3). Later versions reverse this
  without a new mechanism visible at the level of text retrieved here. 核验 (titles/dates) — full v5–v11
  change history **not read**.
- Honest boundary: I read the abstract, §4 fragments and Appendix-A fragments of v12, and Appendix A.1–A.3
  fragments of v4. I did **not** read v5–v11 or the whole of v12. The judgement "the decisive step is a
  non-sequitur" is therefore a 推导 from retrieved fragments, to be re-checked against the full v12 text; the
  author may have added an argument I have not seen. This is a judgement to re-check, not a verdict on a person.

## 6. What the project would have to do to use this as a model-alignment entry

1. Read **v12** in full (it is the only version that claims the proof) and locate the exact, non-circular
   argument behind Prop. A.8. If none exists, the entry is a *methodological* entry — "the amplitude channel
   is β-visible in principle; this particular construction does not close it" — not a model entry.
2. Record the two-line interface: **position ↔ γ** (Fourier-dual data, β-blind; consistent with the project's
   S(t)-is-β-blind finding) and **amplitude ↔ β** (β-visible). This is the useful residue of the paper.
3. If the amplitude channel is ever to be used, the project must supply its own bound on the growth of peak
   amplitudes as p_L → ∞. The paper does not supply one that survives §5.
4. Do not cite the paper as evidence for or against RH. If cited at all, cite it as an example of a claimed
   β-sensitive construction whose decisive step is unavailable, and note the title change v6 → v7.

## 7. Is the model worth a deeper dive? (with reasons)

**Shallow alignment: yes. Deep dive: not as a β-probe; yes as a cautionary case.**
- *For a shallow entry:* the construction is the Guinand/Weil explicit formula in scattering language (its
  amplitudes are classical x^{β}-type objects), it names the position/height dichotomy cleanly, and it is the
  paper the A5 alignment already flags as "directly on point" — so one page of alignment is cheap and useful.
- *Against a deep dive:* the β-sensitivity is the classical x^{β} factor of the explicit formula, not a new
  handle; the claimed proof's key step is, on the retrieved text, a non-sequitur; and pursuing a claimed RH
  proof from an unaudited quant-ph preprint is exactly the kind of work the project's discipline forbids.
- **Recommendation:** keep this file as the alignment entry; no numerical work, no investment. Revisit only
  if a referee-quality version appears, or if the project itself needs the amplitude-growth bound of §6.3
  (in which case it is the project's own problem, not the paper's).
- **Registered status of E28:** closed as "model read; central claim tested; the construction's β-channel is
  open in principle and is **not** closed by the paper; the RH claim is not accepted".

## 8. Sources actually used and not used
Used: arXiv abs page 2410.03673 (metadata, submission history) · arXiv HTML v12 (abstract, Eq. (12), (13),
(21), (25), (28), (29); Thm A.6; Prop. A.8) · arXiv PDF v4 fragments (Appendix A.1–A.3, projection table) ·
project files `docs/E19-model-alignment.md` §2, §6 and `docs/ALIGN-A4-A5-with-our-results.md` §2. **Not found**
(searched, not retrieved): any referee report, published critique, journal version, or independent check.
