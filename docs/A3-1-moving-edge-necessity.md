# A3-1 — Moving-edge obstruction as the explanation of why the frontier method must count the positive index

**Status:** internal alignment note. Registered as item **A3-1** in `docs/PENDING-ITEMS-MASTER.md`.
**Depends on:** `ALIGN-A3-weil-positivity-inertia.md`, `ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`,
`ARCHIVE-P28-P33.md`, `p28-p33-final-archive.md`, `ERRATUM-inertia-factor2.md`.
**Label convention (used on every claim below):**
`[核验]` verified numerically here · `[引用]` quoted from literature · `[推导]` derived here · `[猜想]` conjecture.
**Standing scope warning:** nothing below claims a proof of RH.
Nothing below asserts that a structure **not found** here **does not exist**.

---

## §0 What is being explained

The frontier paper **arXiv:2608.13637** ("More than two thirds of the zeta zeros are simple and on the
critical line") obtains an **unconditional** proportion `≥ 2/3 − o(1)`. It does **not** pass through the
negative inertia of a finite compression; it certifies a **positive** index instead. `[引用]`

This note records: **the project's own negative result is the mechanism-level explanation of why that
detour is necessary.** The relation is **complementarity, not competition** — the two lines start from the
same object (a finite compression of the Weil form) and read different functionals of it.

## §1 The project's negative result (the moving edge)

- `[推导]` **Extensive finite-section negative inertia does not imply an infinite-dimensional uniformly
  negative sector.** In symbols: `n₋(K_N) = N ⇏ ∃ε>0: dim E_K((−∞,−ε)) = ∞`.
- `[推导]` In a *consistent nested* realization, `n₋(K_N) → ∞ ⟹ n₋(K) = ∞` **can** hold while all
  additional negative directions accumulate at the spectral edge `0`, so that `inf σ₋(K) = 0` and **no
  uniform negative-form margin exists**. Infinite negative index and uniform negative margin are therefore
  logically independent.
- `[推导]` Standard 2×2 model pinning the distinction: `K_j = [[1, −(1+1/j)], [−(1+1/j), 1]]`,
  with `λ_j⁻ = −1/j → 0⁻`; then `n₋(K) = ∞` while `inf_{‖x‖=1} −⟨Kx,x⟩ = 0`.
- **Exact scope (must be reproduced verbatim when citing):** P28–P33 established an **obstruction to
  transfer**. It is **not** a theorem that `n₋(K_off)` is finite. The archive splits the gap into
  **Problem I** (`n₋(K_off) = ∞`? — not settled) and **Problem II** (uniform negative sector — strong
  moving-edge evidence, not a theorem for the actual arithmetic `K_off`).

## §2 Erratum: the per-orbit inertia is 2, not 1

- `[核验]` The per-orbit negative inertia was corrected from **1 to 2** by `ERRATUM-inertia-factor2.md`
  (found while rebuilding the G6 scripts; independently re-verified by `G6_verify_inertia_factor2.py`).
  Corrected values: `n₋(K_ρ) = 2` per off-axis pair; `n₋(K_off(N)) = 2N`; the count table becomes
  `4 / 6 / 4 / 2`. The early internal values `2 / 4 / 6` were right; a single algebraic slip (writing a
  block as `−2σ_x`, whose spectrum is `±1`, instead of `−2I₂`) propagated downward into the later 1/2/3
  table.
- `[推导]` The **qualitative** conclusions of P28–P33 are unaffected: replacing `N` by `2N` leaves the
  argument intact (the inertia is still finite, still does not transfer). Only the counts change.
- **This note uses the corrected value (2 per orbit, `2N`) throughout**, and downstream restatements of
  P27–P33 must do the same.

## §3 The frontier's audit note E2

- `[引用]` arXiv:2608.13637 records: *"Agent E2 reported that the intended upper-bound route was empty:
  computed honestly from primes, the negative index of any finite compression is zero, which bounds
  nothing."*
- `[引用]` The same note records the dual bookkeeping: counting **positive** rather than negative squares,
  via **Sylvester's law of inertia and Cauchy–Schwarz** applied to the eigenvalues.
- `[推导]` The project's own prime-side computation (`n₋ = 0`) had independently reached the same
  conclusion **before** reading E2. Two independent paths, same statement: on the prime side the negative
  index of every finite compression is zero. This is a genuine **independent confirmation**, not a new
  result.

## §4 Why this makes the positive-index construction *necessary*

- A negative index of zero yields the bound `0 ≥ 0`, which is vacuous: **the negative index bounds
  nothing.** Hence any route of this type must certify a **positive** index and a **rank**.
- `[引用]` In the frontier's decomposition `ẽG = P + Q`: `P ⪰ 0` with `rank P ≤ s` (`s` = number of
  distinct on-line points), and `Q` of signature `(1,1)` per off-axis pair, so the positive index of `Q`
  is at most `p` (number of off-axis pairs). The **rank supplies the count** of on-line points; **Sylvester
  plus Cauchy–Schwarz**, fed by the unconditional prime-side second moment, converts counting into a
  **proportion**.
- `[推导]` What the project adds is the **mechanism**: *why* finite inertia fails to transfer — the
  negative directions migrate to the moving edge. That mechanism is exactly the structural reason the
  negative-index route is empty and the positive-index route is the one that can be certified.
- **Reading:** our negative result is the **explanation** of their construction, not a rival to it.

## §5 The ceiling, and the detection≠exclusion observation

- `[引用]` The paper's own ceiling: *"The ceiling over the broader class of all bandwidth-one
  certificates is approximately 0.682"* (arXiv:2608.13637 §7.2); and `0.67250…` is **optimal within the
  window class** used (`[CCLM17, Cor. 14]`).
- `[推导]/观察` This resonates with the project's general observation that **detection is not exclusion**
  (the P49 rigidity-gap line): a proportion route that certifies a fraction `< 1` establishes an *upper
  bound below 1* on what that method family can reach, and therefore cannot reach `1`.
- **Constraint on this reading:** the resonance is an **observation about two different objects**
  (their certificate class versus our rigidity gap), not a transfer of theorems between them. It is
  recorded as such, not as a derivation of either from the other.

## §6 What this note does NOT claim

- Not a proof (or disproof) of RH; not an approach to one.
- Not a proof that `n₋(K_off)` is finite: Problem I is explicitly left open; the moving edge obstructs the
  *transfer*, nothing more.
- Not a claim that the frontier method depends on, or needs, our result. Their proof is unconditional and
  independent; we supply an explanation, not a hypothesis.
- Not a priority claim: the negative-index observation is **Bombieri's** (`[Bom00]`), read here
  second-hand through Conrey's survey; the original has not been read.
- Not a claim that `0.682` is the ceiling for *all* certificate classes — only for **bandwidth-one**
  certificates, per the paper's own statement.
- Not a claim that the 2×2 moving-edge family models the actual arithmetic `K_off`; it demonstrates an
  operator-theoretic possibility, not a property of `K_off`.

## §7 One-line summary

`[推导]` Because the negative index of a finite compression is zero on the prime side, the frontier
*had* to certify a positive index; the project's moving-edge obstruction explains why — complementarity.

---

**Cross-refs:** E2 record → §1 of `ALIGN-A3-weil-positivity-inertia.md`; corrected inertia → `ERRATUM-inertia-factor2.md`;
moving-edge statement → §5–§7 of `p28-p33-final-archive.md`; ceiling → `ALIGN-A3-COMPLETE-2-prime-side-and-bombieri.md`.
