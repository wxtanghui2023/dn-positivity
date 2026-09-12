# E19 — Model-analysis alignment: five physical/statistical models of the zeros

> Registered point E19 (`docs/EXPLORATION-POINTS-REGISTER.md`, row E19; restated in
> `docs/MASTER-TODO-MERGED.md` and `docs/PENDING-ITEMS-MASTER.md` as E19-1).
> Sources: this project's own archive, plus literature where fetchable.
> Labels: 核验 (verified numerically here) / 引用 (from literature) / 推导 (derived in this note) /
> 猜想 (conjecture) / 未找到 (searched, not located — *not* "does not exist").
> The project never claims to prove RH. Nothing here is a claim of proof.

## 0. The claim under test

The project's central negative finding: tools that detect the imaginary parts γ of the zeros
are blind to the real parts (β = Re ρ). Stated in `docs/physics-map-2026-08-31.md` §三 and
`docs/qm-rh-analysis.md` §三 as the "β wall", and classified in
`docs/B-candidate-space-analysis.md` row ⑦ as "物理类比族 — simulations (log-gas / crystal …),
no β channel". Below I test that claim model by model against the archived documents.

## 1. Log-gas

(a) **Established** [核验]: the 1D Coulomb gas on the γ-line reproduces GUE pair correlation and
long-range rigidity (number variance ≈ 0.25 × GUE over the tested ranges), the stiffness coming
from *prime phase locking*, i.e. arithmetic — not from any ensemble
(`docs/p26a18-loggas-crystal.md` §①; `docs/qm-rh-analysis.md` §2.2; `docs/long-range-rigidity.md`).
(b) **Model of**: the imaginary parts only. The gas lives on the γ-line; β is not a coordinate of it.
(c) **Single structural reason it cannot constrain β** [推导]: a collective statistic computed from
spacings of {γ_k} is a function of the γ-data alone, so a finite off-axis shift δ moves it by O(1/N).
The archive also carries a sharper negative [核验]: the naive zero-geometry variational functional has
the **wrong sign** — E(δ) − E(0) < 0 (log-gas: −3.9e4 → −160; Coulomb: −2.5e7 → −2.5e3), so the
critical line is a *maximum*, and the log-gas energy read as a potential drives zeros *off* the line
(commit `4f138c5`, "P8 第一枪").

## 2. Quasicrystal / scattering

(a) **Established** [核验]: phase locking S(p) = Σ_k sin(γ_k log p) = O(1) unconditionally, with
quasi-regular stepping and a quasicrystal-diffraction analogy (`docs/p26a18-loggas-crystal.md`);
BKT-type vortex binding with sign-flip probability p ≈ 0.61755 (stable across 10 blocks, |spread| < 0.003),
close to but **not** 1/φ = 0.61803 (off by 4.8e−4 and drifting), so the exact-golden-ratio reading is
*not* supported (`docs/bkt-binding-discovery.md` §3; `docs/physics-rigidity-tools.md` §2).
Scattering side [核验+推导]: the scattering determinant φ(s) = ξ(2s−1)/ξ(2s) was audited on four routes,
all insufficient (`docs/gate20-scattering-pinning-audit.md`).
(b) **Model of**: γ only — phase locking is a statement about the γ-line.
(c) **Single structural reason** [推导]: on the scattering side the resonances are eigenvalues of a
**non-self-adjoint** operator (after complex scaling, per Lax–Phillips / Sjöstrand–Zworski [引用]), so
there is no automatic realness and no coercive bound on Re ρ; Parseval positivity there lives in the
test-function variable and is position-blind. On the crystal side, nothing fixes the lattice at β = 1/2.

## 3. Dynamical quantum phase transitions (DQPT)

(a) **Established**: the project explored DQPT early as a physical analogy and concluded γ-channel
yes / β-channel no; it later audited the mature literature version —
arXiv:2511.11199, *Nat. Commun.* 17 (2026) 8163 (all details 引用·外部, not independently re-verified) —
finding it to be a **detection/verification** framework (Loschmidt amplitude, cumulative phase,
NMR 5-qubit experiment), with a self-declared asymptotic correspondence
(`docs/YM-breakthrough-5-dqpt-paper-verdict.md` §1–§2; `docs/tool-map-crossdisciplinary.md`).
(b) **Model of**: γ only — the critical times t_c are the zero heights.
(c) **Single structural reason** [推导]: *detection ≠ exclusion*. A probe that fires only when the
system sits on the line **and** at a known zero cannot exclude off-line zeros; and because the
correspondence is asymptotic, any limit-taking demands uniformity in t — the project's recurring
uniformity gap. The archive records the paper's own phrase "increasingly accurate as t increases" [引用].

## 4. Fermi surface / Luttinger

(a) **Archive status**: 未找到. No dedicated document for a Fermi-surface / Luttinger analogy was
located; the analogy appears only inside grouped lists — `docs/MASTER-NOGO-AND-LIVE-PATHS.md` §"其它早期封存"
("物理类比路线 P2–P4 (log-gas / 准晶 / DQPT / 金融 / Fermi 面 / BBH 伪自伴)") and
`docs/SUMMARY-NEW-FRAMEWORK-2026-09-02.md` §2.3 ("物理模型（log-gas/晶体/Fermi 面）在 γ 通道全部有效——缺 β 通道").
The nearest archived content is the QFT/scattering entry: ζ as a scattering amplitude with zeros as
bound-state poles, audited and closed as "ζ zeros = continuous-spectrum scattering poles, not L²
spectral objects" (`docs/qm-rh-analysis.md` §2.3, P2–P4 archive).
(b) **Model of**: presumed γ (a Fermi-surface/level-density picture is a γ-spectral picture);
the archive does not state this explicitly — 未找到.
(c) **Reason**: the archive is silent on a Fermi-specific mechanism. The nearest analogous audit
(scattering, §2 above) gives non-self-adjointness ⟹ no stability of Re ρ. Recorded as *not found*,
not as *nonexistent*.

## 5. Financial-market analogy

(a) **Archive status**: 未找到. No dedicated document was located. Mentions are index-level only:
`docs/MASTER-NOGO-AND-LIVE-PATHS.md` (grouped list), the E19 row in
`docs/EXPLORATION-POINTS-REGISTER.md`, `docs/MASTER-TODO-MERGED.md`, `docs/PENDING-ITEMS-MASTER.md`.
Context [引用]: `memory/2026-08-21.md` records that 唐先生's own research background is financial
physics (arXiv groups physics + q-fin, default q-fin.ST), so the analogy most plausibly came from the
author's home field rather than from a searched frontier result.
(b) **Model of**: not recorded. A market-data-based analogy would be a statistical/γ-channel object.
(c) **Reason**: cannot be tested — the archive is silent. The classification in
`docs/B-candidate-space-analysis.md` ("simulation, no β channel") is a *grouping*, not a test.

## 6. Verdict table (one line per model)

| Model | Archived doc | (b) Models | Does "γ-tools are β-blind" hold? |
|---|---|---|---|
| Log-gas | `p26a18-loggas-crystal.md` | γ only | **Holds** [核验/推导] — γ-line gas; plus wrong-sign variational result [核验] |
| Quasicrystal/scattering | `p26a18-loggas-crystal.md`, `bkt-binding-discovery.md`, `gate20-scattering-pinning-audit.md` | γ only | **Holds** [推导] — non-self-adjoint resonances; no coercive Re ρ bound; golden-ratio reading unsupported [核验] |
| DQPT | `YM-breakthrough-5-dqpt-paper-verdict.md` | γ only | **Holds** [推导] — detection ≠ exclusion + asymptotic correspondence |
| Fermi / Luttinger | none located | (unstated) | **Archive silent** — nearest analogue (scattering) holds |
| Financial market | none located | (unstated) | **Archive silent** — grouping only, no test |

Where the archive is silent, the project's claim is *untested*, not refuted.

## 7. Where a new probe might be looked for

[推导] None of the five is currently a viable β-probe: each was retired for an identified structural
reason. The least-closed is the **log-gas with an FE-symmetric external potential**
(`docs/p26a18-loggas-crystal.md` §③): E = −Σ log|ρ_j − ρ_k| + Σ V(ρ_j) with V(β) = V(1 − β), convex,
minimum at 1/2. It is the only archived model whose basic object is β-visible — the project's
P_γ(δ) = δ²M₂/(2U²D₊D₋), i.e. ≈ δ²/γ⁶ [核验] — and the only one with a restoring-force template
(`docs/p26a15-physics-models.md` §②). For it to work, four things would have to be true:
1. **V must be derived arithmetically from the functional equation**, not posited — otherwise 1/2 is
   inserted, which is the circularity the archive already logged (§④ of `p26a15`).
2. **A variational/equilibrium principle that is not equivalent to RH** must exist; "the zeros sit at
   the minimum" is RH restated (`docs/physics-map-2026-08-31.md` §三).
3. **The second variation must be corrected**: the naive log-gas energy has the wrong sign [核验, P8],
   so the functional must differ from the plain log-gas energy.
4. **Uniformity in height**: the estimate must be limit-stable, since uniformity is the project's
   recurring gap (`docs/YM-breakthrough-3-asano-analogue-limit-obstruction.md` §3).
Two secondary pointers [猜想, flagged as conjecture]: the DQPT implementation lives in the **log scale**
(level spacings log n), so the multiplicative→log conversion is an untested candidate
(`YM-breakthrough-5` §4); and the only physical mechanism in the archive that *pins a position* is
topological protection of a zero mode (Dirac/Andreev/chiral), i.e. an arithmetic index invariant whose
value forces the fixed point (`docs/qm-rh-analysis.md` §4.2) — unconnected to arithmetic so far.

## 8. Boundaries

- 核验: the log-gas rigidity numbers, the p ≈ 0.6176 statistics, Φ/P_γ numeric values, and the P8 sign.
- 引用: GUE/Montgomery–Odlyzko, BKT, Lax–Phillips / Sjöstrand–Zworski, the DQPT paper, the 2026
  quasicrystal–scattering application (via commit `4969832`), 唐先生's q-fin background.
- 未做: no model was constructed or re-run for this note; no L2 file was touched; no claim of proof.
- 未找到 items (§4, §5) mean the archive search returned nothing; they are not assertions of absence.
