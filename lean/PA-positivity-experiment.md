# Lean 实验记录 · `positivity` 在最小 import 集下的失效（2026-09-13）

**背景**：`lean/PA-Basic.lean` 首编译 3 处 error 之一为 `positivity` 失败 ✗（修正 ③）。
为定位根因，写了一个 4 行 scratch（**不**留在 `lean/*.lean` 内 —— 避免"所有 `.lean` 应 exit 0"的检查被污染 ✓），
下列结论**均为实测**（`cd ~/mathlib4 && lake env lean …`，编译 2 秒 ✓）。

## import 集（与 `PA-Basic.lean` 相同 ✓）
```lean
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
```

## 四个候选与实测结果

| # | 目标 | 写法 | 结果 |
|---|------|------|:--:|
| 1 | `0 < (1/2 : ℝ)^2 + γ^2` | `by positivity` | ❌ `failed to prove positivity/nonnegativity/nonzeroness` |
| 2 | `(1/2 : ℝ)^2 + γ^2 ≠ 0` | `by positivity` | ❌ 同上（**同样失败**） |
| 3 | `0 < (1/2 : ℝ)^2 + γ^2` | `norm_num` + `sq_nonneg` + `add_pos_of_pos_of_nonneg` | ✅ **通过** |
| 4 | `0 < (1/2 : ℝ)^2 + γ^2` | `by nlinarith [sq_nonneg γ]` | ❌ `unknown tactic`（该 import 集**未**提供 `nlinarith` ✗） |

**候选 3 的可用写法** ✓（已写入 `PA-Basic.lean`）：
```lean
have hpos : (0 : ℝ) < (1 / 2) ^ 2 + γ ^ 2 := by
  have h1 : (0 : ℝ) < (1 / 2 : ℝ) ^ 2 := by norm_num
  have h2 : (0 : ℝ) ≤ γ ^ 2 := sq_nonneg γ
  exact add_pos_of_pos_of_nonneg h1 h2
```

## 结论（两条，均可复用 ✓）

```
① **`positivity` 的失效与"目标是正性还是非零"无关** ✗ ——
   候选 1（正性）与候选 2（非零）**同时**失败 ⟹ 我最初"否定型目标导致 positivity 失效"的诊断
   **被自己的实测推翻** ✓（同族教训：诊断也要验证 ✓）。
② **Mathlib 里"应该有"的 tactic 必须先小文件实测** ✓ ——
   `nlinarith` 在本 import 集下**根本不存在**（候选 4 ✗）；
   最小 import 策略（`LEAN-SANDBOX-SETUP.md` §六 ✓）的代价就是**默认缺 tactic** ✓ ⟹ 写证明时
   **优先用基础引理组合**（`sq_nonneg` / `add_pos_of_pos_of_nonneg` / `norm_num` ✓），
   而不是假设高阶 tactic 可用 ✓。
```

**对 `PA-Basic.lean` 的影响** ✓：纯记法/工具层 ✗，**不改变**任何数学陈述 ✓ ——
共享恒等式 `|1 − 1/ρ|² = 1 + (1−2β)/(β²+γ²)` 及其临界线推论的内容与证明结构不变 ✓。
