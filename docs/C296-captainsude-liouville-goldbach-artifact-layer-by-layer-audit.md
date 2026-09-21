已查地图（**先查后写**）：`C-295`（仓库枚举／claim only ✓）、`C-294`（架构 ＋ GRH 单点承重 ✓）、`C-293`（核验 ✓）。一手材料：GitHub `CaptainSude/Liouville-Goldbach`（**tree API ＋ 原文 raw 逐字**✓）。回查见 §6 ✓

D0: 本档对象 = **C-296：CaptainSude/Liouville-Goldbach 一手 artifact 的逐层审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

**① 一手 artifact 已找到** ✓✓ —— 且**非**二手中文报道 ✓；状态从 `claim only` 升级为 **`外部 artifact · 语句级与公理级通过 · 证明内容待逐引理审计 · provenance 未闭合`** ✓
**② 主定理语句＝Shusterman 原命题** ✓✓（逐字见 §1 ✓；**无额外假设** ✗，**用 Mathlib 的 liouville** ✓）
**③ 公理审计通过** ✓✓：全部 12 个关键声明只依赖 `propext`／`Classical.choice`／`Quot.sound` ✓ —— **无 `sorryAx`、无额外数学公理** ✗✓
**④ 路线审计通过（自证式）** ✓：九项新组件全出现、七项被替换组件全缺席 ✓
**⑤ provenance 与 Astra 分离** ✗✓（按唐先生指令 ✓）：仓库公开身份是 `CaptainSude` ✓，**未见**与 Astra／OpenAI 的官方关联 ✗ ⟹ 只能写成 **`公开 GitHub proof artifact`** ✓，**不得**写成 `Astra 官方 artifact` ✗

---

## §1 主定理语句（**逐字**✓✓，`lean/LiouvilleGoldbach/Main.lean`）

```
theorem liouville_goldbach (N : ℕ) (hEven : Even N) (hN : 2 < N) :
∃ a b : ℕ, 0 < a ∧ 0 < b ∧ a + b = N ∧
ArithmeticFunction.liouville a = -1 ∧ ArithmeticFunction.liouville b = -1
```

- **对照 Shusterman 命题** ✓✓：对一切偶数 `N > 2`，存在正 `a,b` 使 `a+b=N` 且 `liouville a = liouville b = -1` ✓ —— **逐字吻合** ✓
- **关键点①（无夹带定义）** ✓✓：用的是 **Mathlib 的 `ArithmeticFunction.liouville`** ✓ —— **不是**自定义函数 ✗✓（这正是"语句层审计"最该查的项 ✓）
- **关键点②（无额外假设）** ✓✓：假设只有 `Even N` 与 `2 < N` ✓ —— **没有** GRH、没有解析输入、没有未证前提 ✓
- **文档自述**（PROOF.md 结尾 ✓）："This is a polished proof-development note; literature positioning and the paper remain separate work." ✓ —— 自我定位诚实 ✓（未声称已发表 ✓）

## §2 公理审计（**逐字**✓✓，`lean/verification-axioms.log` ＋ `lean/Audit.lean`）

- 全部 12 项关键声明均报 `[propext, Classical.choice, Quot.sound]`（`defect_commuting_square` 仅 `[propext, Quot.sound]`）✓✓
- ⟹ **无 `sorryAx`** ✗，**无额外公理** ✗✓ —— 即只用 Lean 标准逻辑基础 ✓
- `Audit.lean` 用 `#check` ＋ `#print axioms` 对 12 个声明逐条输出 ✓ ⟹ **可复现** ✓
- **待办**：`Classical.choice` 的出现是**合法但需注意**的 ✓（非构造性存在性，与 Mangerel 的"effectively computable N_0"形成对照 ✓ —— **本 artifact 的结论是存在性、非有效可计算** ✓ 需在与 Thm 1.2 对齐时标注 ✓）

## §3 路线审计（✓，`lean/verification-route.log`）

- 原文一句：`Polished proof route verified: all nine new ingredients occur, and all seven replaced ingredients are absent.` ✓
- **九项新组件**（与 §4 的六层清单对应 ✓）：`defect_commuting_square`／`commuting_completion_two`／`commuting_completion_three`／`uniform_even_descent`／`extension_descent_certificate_symmetric`／`short_representative_of_invariance`／`half_interval_extension_via_invariance`／`exists_prime_square_below_half`／`no_multiplicative_agreement_of_odd` ✓✓
- ⟹ 作者**有意识防止"旧证明残留"** ✓（对审计方是正面信号 ✓）

## §4 唐先生六层清单 × 现状（**逐层**✓✓）

| 层 | 对应声明 | 现状 |
|---|---|---|
| 1 commuting_completion（2／3） | `IntervalSigns.commuting_completion_two`／`_three` | **存在** ✓；**内容待审** ⚠️ |
| 2 A=B defect | `defect_commuting_square` | **存在** ✓；公理最干净 ✓；**内容待审** ⚠️ |
| 3 short_representative_of_invariance | 同名 ✓ | **存在** ✓；**内容待审** ⚠️ |
| 4 half_interval_extension_via_invariance | 同名 ✓ | **存在** ✓；**本路线承重步** ⚠️⚠️ |
| 5 quadratic-reciprocity small-prime | `Final.exists_prime_square_below_half` | **存在** ✓；**内容待审** ⚠️ |
| 6 归结为完整 Shusterman | `all_even_of_positivePrimePairs` ＋ `liouville_goldbach` | ✓✓ **语句级通过**（§1 ✓） |

- **我方手检已通过的两段**（可独立复核 ✓）：
  - **§1 归约** ✓：若 `2p` 无"正-正"对，则 `p` 无"负-负"对——因 `lambda(2a) = -lambda(a)` ⟹ 加倍即得"正-正"对 ✓✓
  - **§4 终结步** ✓：`N=2m`；若 `lambda(m)=-1` 用 `m+m` ✓；否则 `m = r·s·c`（`r,s` 素、`lambda(c)=1` ✓）；若某素因子 `>3` 则由 (6) 的 `2r` 正-正对乘 `s·c`（**负号** ✓）⟹ 得负-负对 ✓；否则 `2rs in {8,12,18}` 用 `8=3+5`／`12=5+7`／`18=7+11`（**逐条验证均 λ=−1** ✓）乘 `c`（λ=1 保号 ✓）✓✓
- **仍未审**（需继续读 ✓）：第 1–5 层的**实际内容** ✓（在 `Commuting.lean`／`Coset.lean`／`Extension.lean`／`Residue.lean`／`Reduction.lean`／`Character.lean`／`Completion.lean`／`Descent.lean` ✓）

## §5 provenance 与状态判定（✓）

- **provenance**：仓库身份 `CaptainSude` ✓ —— **未**见与 Astra／OpenAI 官方关联 ✗ ⟹ 证据链只到 **公开 GitHub artifact** ✓✓
- **状态判定**：`unverified claim` → **`外部 artifact（语句级 ✓／公理级 ✓／复现待做 ⚠️／内容待逐引理审计 ⚠️／provenance 未闭合 ✗）`** ✓
- **与 Astra 关系**：**未建立** ✗✓（不得写成"Astra 的证明"✗）

## §6 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **纪律**：不接 M-TOWER ✗；不建判据 ✗；不与 L／F／B／R 排序 ✗；先不问 RH ✓
- **不得**写成：该结果是 Astra 官方成果 ✗；已独立复现 ✗；已同行评审 ✗
- **本档新增词**：`逐层审计`／`语句级审计`（0 命中 ✓）
