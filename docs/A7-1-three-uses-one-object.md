# A7-1 — Three uses of one object

**Status:** internal alignment note. Registered as item **A7-1** in `docs/PENDING-ITEMS-MASTER.md`
(the pending row notes it is to be folded into the E30 unified frame).
**Depends on:** `ALIGN-A7-connes-ncg.md`, `CONNES2026-read-1.md` / `-2-comparison.md` / `-3-definitions-and-strategy.md`,
`ALIGN-A3-weil-positivity-inertia.md`, `ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`,
`ERRATUM-inertia-factor2.md`, `E30-UNIFIED-CONVERSION-LAW.md`.
**Label convention:** `[核验]` verified numerically here · `[引用]` quoted from literature ·
`[推导]` derived here · `[猜想]` conjecture.
**Scope warning:** nothing here claims a proof of RH; a structure not found here is not thereby asserted
not to exist.

---

## §0 The single object

**The finite compression of the Weil quadratic form** — restrict Weil's quadratic form (equivalently, the
quadratic form attached to the explicit formula on a test family) to a finite-dimensional subspace /
truncation, and read a functional off the resulting matrix.

All three uses below operate on **this one object**. They are distinguished only by *which functional is
read off it*.

## §1 Use 1 — Extremization ⟹ zero positions `[引用]`

- `[引用]` **Connes, arXiv:2602.04022** ("Letter to Riemann"): by *extremizing a quadratic form* (the
  restriction of Weil's form) using **only primes below 13** (`2, 3, 5, 7, 11`), the optimization gives
  approximations to the **first 50 zeros**, with accuracy from `2.6×10⁻⁵⁵` to `10⁻³`.
- Functional read off: the **value / minimizer** of the restricted form.
- Output: **positional** information (where the zeros are, to finite precision).
- Analytic input: a small prime set; no moment evaluation is used.

## §2 Use 2 — Rank and inertia ⟹ counts and proportions `[引用]`

- `[引用]` **arXiv:2608.13637** decomposes `ẽG = P + Q`, where `P ⪰ 0` has `rank P ≤ s` (`s` = number of
  distinct on-line points) and `Q` has signature `(1,1)` per off-axis pair. By Sylvester's law of inertia
  the positive index of `Q` is at most `p` (number of off-axis pairs).
- `[引用]` Counting **positive** rather than negative squares — Sylvester plus Cauchy–Schwarz on the
  eigenvalues — and feeding in the unconditional prime-side second moment (`[BGSTB24]`, Montgomery's
  unconditional second moment), certifies a proportion `2 − c_MT^{−1} = 0.67250…` for the
  Montgomery–Taylor window, and `≥ 2/3 − o(1)` in general.
- Functional read off: **rank** and **positive inertia**.
- Output: **counting** information (how many zeros, and in what proportion, lie on the line).
- Analytic input: an unconditional second moment.

## §3 Use 3 — Negative index as an obstruction structure `[推导]` + `[引用]`

- `[推导]` **The project's own line (P27):** the **negative index** of the compression equals the number
  of off-axis pairs seen by it, hence functions as an **obstruction**: the negative directions register the
  off-line zeros. This is the entry point to the moving-edge line (P28–P33), which then shows the
  obstruction does **not transfer** to an infinite-dimensional negative index.
- `[引用]` This reproduces a **published observation of Bombieri's** (`[Bom00]`), recorded in Conrey's
  survey: *"the number of non-real pairs of conjugate γ is exactly equal to the number of negative
  eigenvalues"* — under the same symmetry hypotheses as the zeta zeros.
- **Priority correction (must be kept):** our P27 series is a **reproduction / independent verification**
  of that observation, **not** an original discovery.
- `[核验]` **Erratum:** the per-orbit negative inertia was corrected from **1 to 2**
  (`ERRATUM-inertia-factor2.md`); the corrected count table is `4 / 6 / 4 / 2`. Any statement of Use 3
  must quote `2` per orbit and `2N` for the truncation, not `1` and `N`.
- Functional read off: the **signature / negative index**.
- Output: **structural** information (a no-go / obstruction statement).
- Analytic input: a direct prime-side computation (the negative index there is zero).

## §4 What distinguishes the three uses

All three are the **same object**; they differ in the functional and hence in the type of output:

| Use | Functional of the compression | Output type | Source | Label |
|---|---|---|---|---|
| 1 | value / minimizer (extremization) | zero **positions** | Connes (arXiv:2602.04022) | `[引用]` |
| 2 | rank + positive inertia | zero **counts / proportions** | arXiv:2608.13637 | `[引用]` |
| 3 | signature / negative index | **obstruction** structure | our P27 (reproducing Bombieri) | `[推导]`+`[引用]` |

- The **analytic inputs also differ**: Use 1 needs only a small prime set; Use 2 needs an unconditional
  second moment; Use 3 needs a direct prime-side computation. The shared object is the compression; the
  surrounding machinery is not shared.
- Consequence: the three uses are **not** three theorems about three objects, and **not** interchangeable.
  They are three read-outs of one matrix-valued object.

## §5 Non-conflation warnings (important for future citations)

- **Do not conflate "rank" across uses.** The `rank` in Use 2 is `rank P` = number of on-line points.
  The `rank` in the Connes–van Suijlekom Toeplitz path (`arXiv:2511.23257`, Carathéodory–Fejér 1911) is a
  **Toeplitz rank deficiency** (⟺ simple minimum eigenvalue). These are **different objects**. Our
  `CVS1`–`CVS4` verified the latter mechanism `6/6` `[核验]`, but it is **not** the former.
- **Do not conflate extremization with counting.** A positional approximation (Use 1) is not a counting or
  proportion statement (Use 2).
- Connes–van Suijlekom is listed here only to **fence off** the conflation; it is a related but distinct
  object (PSD Toeplitz / finite even case), not a fourth use of the compression in the sense above.

## §6 Open point carried over from the erratum

- `[猜想/open]` Bombieri's observation equates the number of non-real **conjugate pairs** with the number
  of negative eigenvalues. **If one orbit corresponds to one pair, `n₋` should be 1; the corrected value
  is 2.** The **orbit ↔ conjugate-pair correspondence is therefore unresolved** and is registered as a
  pending verification (aligns with A3-5). Until it is resolved, this note quotes the corrected value
  `2N` while flagging that the identification "one orbit = one pair" is **not established here**.
- **Secondary boundary:** Bombieri's statement was read **through a survey (Conrey's)**, not from
  `[Bom00]` itself. It must be checked against the original before being quoted as Bombieri's exact
  wording.

## §7 What this note does NOT claim

- Not an RH proof or a step toward one.
- Not a claim that the three uses are **equivalent theorems**, nor that any one implies another.
- Not a priority claim on the negative-index observation (that is Bombieri's).
- Not a claim that Uses 1 and 2 share a technical input — they do not.
- Not a resolution of the orbit ↔ conjugate-pair correspondence; that is flagged open.

---

**Summary line.** One object (the finite compression of the Weil form); three read-outs: extremization gives
**position**, rank+inertia gives **count**, negative index gives **obstruction**. `[推导]`

**Cross-refs:** Use 1/2/3 comparison table → §3 of `ALIGN-A7-connes-ncg.md`; Bombieri observation →
§2 of `ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`; correction → `ERRATUM-inertia-factor2.md`;
unified frame → `E30-UNIFIED-CONVERSION-LAW.md`.
