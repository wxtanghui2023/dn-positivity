# A3 improvement assessment — can the project's assets beat 0.6725 / 0.682?

**Date:** 2026-09-12 · **Scope:** quantitative only; no RH claim, no constant-tweaking.
**Labels:** `[核验]` verified numerically here · `[引用]` quoted from a named source · `[推导]` derived here · `[未核验]` not verified in-repo.
**Frontier input (verbatim, recorded in-repo at `docs/E46-5C-inertia-necessity.md`):** arXiv:2608.13637v2,
**Lemma 3.2** — for Hermitian `d×d` `P, Q` with `P ⪰ 0`, `rank P ≤ r`, `n₊(Q) ≤ b`:
```
(3.1)   r ≥ 2 tr P + 4 tr Q − 4b − ‖P+Q‖²_HS ,
```
equality attainable at `P = Π₁`, `Q = 2Π₂` for orthogonal projections `Π₁ ⟂ Π₂` of ranks `r, b`.
Constants: `c_MT⁻¹ = ½ + (1/√2)cot(1/√2) = 1.3274992963`, so `2 − R(ψ_MT) = 0.6725007`; ceiling `≈ 0.682`.
**Script:** `scripts/A3_improvement_check.py` → `scripts/A3_improvement_check.txt` (reads `data/zeros_2000.npy`, part D only).
**Precision caveats:** frontier §2–§6 were **not** read in this repo, so the mapping `b → constant`
below is `[未核验]` beyond the exact identity proved in Q1(d); 0.682 is `[引用]` and is not re-derived (cf. `docs/E8-ceiling-0682.md` §5).

---

## Q1 — Substituting our negative inertia into (3.1): identity, not improvement

**(a) The rewrite.** Sylvester's law of inertia gives `n₊(Q) + n₋(Q) = rank Q` `[引用, standard]`.
Our asset: each off-axis orbit (4 zeros = 2 conjugate pairs) contributes `n₋ = 2` `[核验, docs/ERRATUM-inertia-factor2.md]`,
i.e. `n₋ = 1` per pair. The frontier's zero side assigns each off-line pair a signature `(1,1)` form
`[引用, docs/ALIGN-A3-weil-positivity-inertia.md §2]`, so with `p` off-line pairs `n₊(Q) = n₋(Q) = p`,
`rank Q = 2p`. Substituting into (3.1):
```
b  ↦  b_new = rank Q − n₋(Q) = 2p − p = p = b ,
(3.1') r ≥ 2 tr P + 4 tr Q − 4(rank Q − n₋(Q)) − ‖P+Q‖²_HS ≡ (3.1) .
```
`[核验]` Script part B, over `(N_on, p) ∈ {(10,1),(10,5),(100,20),(1000,3),(2000,500)}`: always
`n₊ = n₋ = p`, `rank Q = 2p`, `b_new = b`, **and the count identity `2 tr P + 4 tr Q − 4b = 4 tr(P+Q) − 2N`
holds exactly** (with `tr P = N_on`, `tr Q = 0`, `N = N_on + 2p`).

**(b) Verdict.** The rewrite is an **equivalent restatement**; it yields **no new inequality and no new constant**
(0.6725 unchanged). Reason: our `n₋` is *numerically the same quantity* as the frontier's `b`
(`b = n₊(Q) = n₋(Q) = p`) — the dual bookkeeping the frontier itself records ("counting positive rather
than negative squares", `[引用]` E2 note). Sylvester is a tautology here, not an extra input.

**(c) Sensitivity — why nothing is left on the table.** `d(RHS)/db = −4`, so one unit of `b` is worth `4/N`
in proportion. Reaching 0.682 from 0.6725 therefore needs
```
δb = (0.682 − 0.6725)·N/4 = 0.00238 N          [推导]
```
(script part B prints this: 0.03, 0.05, 0.33, 2.39, 7.12 for the five rows). Our asset supplies **zero** such
slack: it *certifies* `b`, so `δb = 0`. The maximal conceivable gain through this channel is `b → 0`, i.e. `4p/N`
(script column `gain|b->0`); but `b = 0` means `n₊(Q) = 0 ⇒ Q ⪯ 0`, i.e. **no off-line pairs at all = RH**,
and it contradicts the signature `(1,1)` structure. So the channel exceeds 0.682 only by proving RH.

**(d) Structural reason it cannot work.** (3.1) is **sharp**: equality is attained `[核验, part A]` at
`P = Π₁, Q = 2Π₂` (there `n₋(Q) = 0`). Any improvement must therefore come from **extra inputs**, not from
rewriting the same inequality — and our `n₋` data is not an extra input, it is the same index read the other way.
`[核验 part A]` 4000 random trials: 0 violations of (3.1) (min slack 0.6745 on non-trivial configs).

**Q1 answer: cannot improve 0.6725. The rewrite is an identity; fails the stated criterion (> 0.6725).**

---

## Q2 — Moving-edge gives **no** numeric ceiling `C*`

**(a) What moving-edge says.** `n₋(K_N) = 2N` finite does **not** transfer to a uniform negative sector:
the 2×2 family `K_j = [[1, −(1+1/j)], [−(1+1/j), 1]]` has `λ⁻_j = −1/j`, so `n₋(K_N) = N` while
`|λ⁻_N| → 0` `[推导, docs/p33c-moving-edge-obstruction.md; 核验, script part C]`.

**(b) Answer: no `C*` exists.** Three quantitative reasons.

1. **Empty intersection.** Moving-edge lives in the regime `n₋ = ∞`, margin `→ 0`. The frontier's inequality is
   finite-dimensional `d×d`, and — decisively — its **equality configuration has `n₋(Q) = 0`** `[核验, part A]`.
   Moving-edge constrains a configuration the frontier never enters; it cannot cap that method.
2. **The class contains the frontier's own proof.** Any `C* < 0.682` for the whole "finite compression +
   rank/trace/inertia" family would need an *information-availability* argument (moments), not an inertia
   argument. Moving-edge supplies no moment information.
3. **Quantitative leverage is `o(1)`.** In the moving-edge family the total negative spectral mass is
   `Σ_{j≤N}|λ⁻_j| = H_N = log N + γ + O(1/N) = o(N)` `[核验, part C: N=10⁶ → 14.39, H_N/N = 1.4·10⁻⁵]`,
   and the edge `|λ⁻_N| = 1/N → 0`. Any inequality linear in `n₋` or in the negative mass thus contributes
   `o(1)` to a proportion of size `O(1)`.

**(c) Conclusion.** Moving-edge yields only the **qualitative** statement "inertia-based arguments have no
infinite-dimensional conclusion" (it *explains* why the frontier must count the positive index — real value, but
not numeric). It delivers **no constant**; in particular no `C*`. The only known numerical ceiling of the family
remains the frontier's `0.682`, and that is a **moment-availability** statement (unconditional third moment at
`X ≍ T` blocked by multiplicative relations among prime powers, `[引用]` frontier §7.2(e)), untouched by moving-edge.

---

## Q3 — Toeplitz/CF counting: the **same** constant, provably equivalent

**(a) The mechanism.** PSD Hermitian Toeplitz `T ∈ M_{n+1}` of rank `n` plus a kernel vector ⟹ all roots of
`P(z) = Σ ξ_j z^j` lie on the unit circle (Carathéodory–Fejér 1911; C–vS Cor. 1.1) `[引用, docs/CVS4-...]`,
verified 6/6 in `scripts/CVS1c_final.py` `[核验]`. Structural dictionary (`[引用, docs/ALIGN-A3-...]`):
rank deficiency `1 ⟺` minimal eigenvalue `0` of multiplicity 1 `⟺` simple `⟺` unit-circle root.

**(b) The alternative count and its collapse.** Count **nonzero eigenvalues (atoms)** of the Toeplitz matrix
(instead of trace + Cauchy–Schwarz). But rank is a **congruence invariant** (Sylvester), hence the *same*
functional as the frontier's `rank P`; and the sharp unconditional bound from the two available moments is the
Christoffel value `1 − Λ₁(0) = m₁²/m₂` `[核验, docs/E8-ceiling-0682.md §3]`. Numbers (script part D):
```
measure                                1−Λ₁      1−Λ₂      1−Λ₃      m₁²/m₂
0.6725 δ₁ + 0.3275 δ₀ (Montgomery)   0.672500  0.672500  0.672500  0.672500
0.682 δ_c + 0.318 δ₀  (ceiling data) 0.682000  0.682000  0.682000  0.682000
0.3275 δ₀ + 0.6725 · (empirical zeros) 0.538311 0.622996  0.648907  0.538311
```
Toeplitz rank-deficiency device `[核验]`: rank `T = 2r`, deficiency 1 for generic `r`-atom measures — exactly
the CVS1c result; it adds the *dictionary*, no new bound.

**(c) Verdict: equivalent, not different.** Both routes bound the same functional (number of nonzero
eigenvalues / atoms) from the same input (the two unconditional moments), so they return the **same constant**:
`0.6725` in the Montgomery normalisation path and the `0.682` two-moment ceiling. This is an equivalence, stated
as such. A moment-poor variant is strictly **worse** (0.538/0.623/0.649 above), and a `tr/λ_max` variant
coincides with `m₁²/m₂` on two-atom measures `[核验]`. Our own variational theorem
(`S_proj(a) = Σ 1/(a²+γ²)²`, on-line ordinates uniquely minimise; `D = 2[S_proj(γ_ρ) − S_proj(γ_k)] ≥ 0`
`[引用, docs/E14-bom03-variational-check.md §2]`) runs the **opposite direction** — a lower bound, where counting
needs the reverse upper bound `S_proj(γ_ρ) ≤ W(a)/2` `[引用, docs/r3-archaeology-variational.md]` — so it cannot
be turned into a count without new input. `[未核验 beyond the cited in-repo notes]`

**Q3 answer: same constant (0.6725 / ceiling 0.682). Equivalent to the rank–trace+Sylvester route.**

---

## 对本项目的意义

**方法上：不能改善。** 三条通道逐一被定量关闭：Q1 的改写是恒等式（我们的 `n₋ = 2/orbit` 恰是前沿的 `b`，
双记账），Q2 不存在 moving-edge 决定的 `C*`（其负质量 `Σ|λ⁻| = H_N = log N = o(N)`，且与前沿极值构型
`n₋(Q)=0` 无交集），Q3 给出同一常数（同一泛函 + 同一矩输入，已证明等价）。且 (3.1) 本身在 `P=Π₁, Q=2Π₂`
处取等号 `[核验]`，所以"改写不等式"这条路在原理上就无余量。
**结果上：不能更好。** 在 0.6725→0.682 这条线上，我们的最好产出是**机制解释**（负指标路线为何为空 = moving-edge），
而非数字——而这一点前沿的 E2 记录已独立确认。唯一未被关闭的定量口子：若能证明 `n₊(Q) < p`（等价 `rank Q < 2p`，
即离轴零点非简单/线性相关），可得 `4(p−b)/N` 增益；但本项目资产给不出该输入，且与我们自己的 signature `(1,1)`
模型冲突。要超过 0.682 需要 `X ≍ T` 的无条件**三阶矩**（障碍 = 素数幂的乘性关系），与本项目全部资产无关。
**缺什么（诚实清单）：** 前沿 §2–§6 正文本地缺失 ⟹ `b → 比例` 的归一化映射标 `[未核验]`；0.682 未从第一性原理复现；
真实 `K_off` 的负质量无无条件控制（`H_N` 论证只对 moving-edge 族成立）。**结论：A3 方向对前沿无结果性改进，
宜定位为"机制澄清 + 必要性说明"，不宜作为主攻方向。**
