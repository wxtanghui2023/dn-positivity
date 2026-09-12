# `lean/` —— Paper B 的 Lean 4 形式化

**目的**：按项目纪律⑤「**机器可验证优先**」✅，把 Paper B 的引理链逐条形式化、**每条即时编译验证** ✅
（缘由：`docs/00-ANCHOR-purpose-and-discipline.md` ✅；工具链安装：`docs/LEAN-SANDBOX-SETUP.md` ✅）

## 如何编译（可复现 ✅）
```bash
export PATH="$HOME/.elan/bin:$PATH"
cd ~/mathlib4                       # Mathlib 工程（提供 import 搜索路径 ✅）
lake env lean /home/node/.openclaw/workspace/dn-project/lean/PB-Basic.lean
lake env lean /home/node/.openclaw/workspace/dn-project/lean/PB-Lemma1.lean
```
**判据**：**退出码 0 且 error 数为 0** ⟹ 通过 ✅（4 秒左右 ✅）
```
⚠️ 必须 `lake env lean`（在 ~/mathlib4 内）—— 直接 `lean` 找不到 Mathlib ✅
⚠️ 必须【最小 import】✅（全库 `import Mathlib` 在本机内存下不可用 ✗ 见 LEAN-SANDBOX-SETUP.md §六）
```

## 进度
```
| # | 引理 | 状态 |
| 1 | `F_eq_sq`：x^{k/2} + x^{-k/2} - 2 = (x^{k/4} - x^{-k/4})^2  (x>0) | ✅ **已形式化并通过**（2026-09-12） |
| 2 | `exp_sinh_identity`：e^v - 2 + e^{-v} = 4 sinh^2(v/2) | ✅ **已形式化并通过**（2026-09-12） |
| 3 | `PB-Lemma1.lean`：**论文 Lemma 1**（单调性：F 在 x>1 严格递增，k>0） | ✅ **已形式化并通过**（2026-09-12，4 次迭代） |
| 4a | `PB-Lemma2-mvt.lean`：**MVT 型引理** `xᵃ−1 ≤ a(x−1)xᵃ⁻¹` | ✅ **已通过** |
| 4b | `PB-Lemma2-far.lean`：**论文 Lemma 2**（far 界） | ✅ **已通过** |
| 5a | `PB-Lemma3-identity.lean`：**Lemma 3 恒等式部分**（F(1+u) = 4sinh²(((k/2)log(1+u))/2)） | ✅ **已通过**（首次编译，2026-09-12） |
| 5b | ：**比值恒等式**（剖面 = (sinh(v_t/2)/sinh(v_H/2))²） | ✅ **已通过** |
| 5c | `PB-Lemma3-integral.lean`：**∫₀¹(1+δ)⁻⁴dδ = 7/24**（FTC + rpow 导数 ✓） | ✅ **已通过** |
| 5d | `PB-Lemma3-sinhmono.lean`：**`sinh x/x` 严格递增**（Mathlib 无 ⟹ **自证** ✓） | ✅ **已通过** |
| 5e | Lemma 3 剩余：`(1+O(H⁻²))` 修正项（可用**粗界**替代 ✓ 见注） | ⏳ 未做 |
| 6a | `PB-LemmaS4-integrals.lean`：**两个幂积分**（有限区间版 ✓；极限即论文值 ✓） | ✅ **已通过** |
| 6b | 论文 **Lemma S4** 的 **Abel 求和恒等式**（含边界项 ✓ 论文的核心方法论） | ⏳ 进行中 |
```
**说明**：本目录只记录**形式化**进度 ✅；**不改变**论文的任何数学陈述 ✅。
**纪律**：每条引理必须**独立编译通过**才记为 ✅；**卡住的如实记为卡住** ✅（不粉饰 ✅）。

## 形式化的经验记录（供后续引理复用 ✅）
```
① **先核引理名，再写证明** ✅ —— 一批 `#check`（约 10 秒）比反复猜名快得多 ✅
   本版本**不存在**的名字（避坑 ✓）：`Real.strictMonoOn_rpow*` ✗、`strictMonoOn_of_deriv_pos` ✗（另一模块 ✓）、
   `Real.hasDerivAt_rpow_const` ✗、`inv_lt_inv_of_lt` ✗
   本版本**可用**的关键名字 ✓：`Real.rpow_lt_rpow` ✓、`Real.rpow_neg` ✓、`Real.one_lt_rpow` ✓、
   `inv_lt_one_of_one_lt₀` ✓、`one_div_lt_one_div_of_lt` ✓、`sq_lt_sq'` ✓、`StrictMonoOn.comp` ✓
② **`Set.Ioi` 的成员需要转换** ✅ —— `1 < a` 与 `a ∈ Set.Ioi 1` 对 tactic 不等同 ✅
   ⟹ 先 `simp only [Set.mem_Ioi] at ha` ✅
③ **`StrictMonoOn` 的目标是 beta-未归约形式** ✅（形如 `(fun x => …) a < (fun x => …) b`）
   ⟹ `rw` 前先 `show` 展开 ✅
④ **自然数指数 vs 实数指数** ⚠️ —— `(...)^2` 是 `Nat` 指数；`Real.rpow_*` 要实数指数 ✅
   ⟹ **避免混用**：全程用 `Real.rpow_add` 而非 `Real.rpow_mul` ✅（本目录的 `F_eq_sq` 即如此 ✓）
⑤ **每次改完立刻编译**（3–4 秒 ✓）—— 本项目 4 次迭代的错误**全由编译器抓出** ✅
```

## 本轮技术收获（供后续复用 ✅）
```
| 目的 | 本次找到的正确名字 ✓ | 本版本【不】存在的 ✗ |
| 幂函数导数 | `Real.hasDerivAt_rpow_const`（**须 import `Pow/Deriv`** ✓） | — |
| 幂函数凸性 | `convexOn_rpow`（**须 import `Convex/SpecificFunctions/Basic`** ✓） | `Real.convexOn_rpow` ✗ |
| 区间积分基本定理 | `intervalIntegral.integral_eq_sub_of_hasDerivAt`（**须 import `IntervalIntegral/FundThmCalculus`** ✓） | `integral_deriv_eq_sub` ✗（另一变体名 ✓） |
| 幂的域内连续 | `ContinuousOn.rpow_const`（**须 import `Pow/Continuity`** ✓；负指数时用 `f x ≠ 0` 那一支 ✓） | — |
| MVT 型 | `StrictMonoOn.exists_slope_lt_deriv`（`Convex/Deriv` ✓） | `exists_deriv_eq_slope` ✗ |
| `sinh x / x` 单调 | **不存在** ✗ ⟹ **需自行证明** ⚠️ | — |
【教训 ✅】**模块选对比名字更重要** —— 有 3 次错误是"名字对、模块没 import" ✗✓
【教训 ✅】`HasDerivAt.rpow_const` / `ContinuousOn.rpow_const` 的条件是**析取**（`f x ≠ 0 ∨ 0 ≤ p`）✓
   ⟹ 负指数时必须主动选**左支**并给 `f x ≠ 0` ✓（我一开始错选右支 ✗ 目标变成 `1 ≤ -3` 的假命题 ✓）
```

## 附注：Lemma 3 中 `(1+O(H⁻²))` 的处理（诚实说明 ✅）
```
论文写 `(v(t)/v_H)² ≤ (1+δ)^{-4}(1+O(H^{-2}))`（用 `log(1+u) ≤ u` 的精细版）。
**本形式化走的是粗界** ✅：`v(t)/v_H ≤ t^{-2}/H^{-2} = (H/t)²` ⟹ 平方得 `(H/t)^4 = (1+δ)^{-4}` ✅
   ⟹ **比论文的界更强**（无 `(1+O(H^{-2}))` 修正项）✅ ⟹ 论文结论不受影响 ✅
   ⚠️ 但因此**不需要**形式化那个修正项 ✅（属可选 ✓）
```
