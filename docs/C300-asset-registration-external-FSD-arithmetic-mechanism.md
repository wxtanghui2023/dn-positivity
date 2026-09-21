已查地图（**先查后写**）：`C-299`（核心闭环 ＋ FSD 标签 ✓）、`C-298`（q.Prime 闭合 ＋ Commuting 链 ✓）、`C-297`（Coset descent ✓）、`C-296`（逐层审计 ✓）、`C-295`（仓库枚举 ✓）、`C-294`（架构 ＋ GRH 承重 ✓）、`C-293`（核验 ＋ 状态判定 ✓）、`C-291`（事件登记 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-300：外部独立算术机制资产登记（Liouville–Goldbach／FSD）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 登记判定（✓✓）

$$\boxed{\textbf{资产名}✓：\textbf{外部独立算术机制资产 —— FSD（Failure → Symmetry → Descent）}✓}$$
$$\textbf{性质}✗✓：\textbf{外部资产}✓，\textbf{非}本项目成果 ✗（不并入我方成果列表 ✗）$$
$$\textbf{来源}✓：公开 GitHub artifact\ \texttt{CaptainSude/Liouville-Goldbach}✓；\textbf{provenance 未闭合}✗（\text{媒体归因} Astra\ \text{＝}\ \text{provenance claim}✓\ne\ \text{仓库自证}✗）$$
$$\textbf{判定人}✓：\text{唐先生，2026-09-21 13:13}✓（\text{从「审计对象」升级为「独立算术机制资产」}✓）$$

## §1 命题与对象（✓）

- **对象命题** ✓（Shusterman's Liouville-Goldbach）：∀ 偶数 `N > 2`，∃ 正 `a, b` 使 `a + b = N` 且 `λ(a) = λ(b) = −1` ✓
- **注意层级** ✗✓：这是 **Liouville 版**（λ = −1 只表示素因子数（计重数）为奇 ✓），**不是经典哥德巴赫** ✗；蕴含方向 `经典 ⟹ Liouville` ✓，反向不成立 ✗
- **与 Mangerel 的关系** ✓✓：Mangerel = **GRH 条件定理** ✓（`arXiv:2412.17199`，承重点 = **非主特征乘积 L-函数的一致零自由区** ⟹ 短素数区间特征和抵消 ✓）；本 artifact 走 **路线 B** ✓ —— **绕开** Dirichlet L／特征正交／GRH ✗✓

## §2 审计级别（**分级如实**✓✓）

| 层 | 判定 | 依据 |
|---|---|---|
| 语句级 | ✓✓ 通过 | `Main.lean` 主定理与目标命题**逐字一致** ✓；用 **Mathlib 的 `ArithmeticFunction.liouville`** ✓（无夹带定义 ✗）；假设仅 `Even N`＋`2 < N` ✓（无额外输入 ✗） |
| 公理级 | ✓✓ 通过 | 12 项关键声明只依赖 `propext`／`Classical.choice`／`Quot.sound` ✓；**无 `sorryAx`** ✗；`Audit.lean` 可复现 ✓ |
| 路线审计 | ✓ 通过 | 九项新组件全出现、七项被替换组件全缺席 ✓ |
| **核心闭环** | ✓✓ 通过 | `IntervalSigns` 四字段 → 非负／支撑 → 交换方阵 → `A=B` → `A=B=0` → `G(2x)=G(3x)=-G(x)` ✓（`C-299` 逐段有原文依据 ✓） |
| 终局 | ✓ 通过 | `exists_prime_square_below_half` ＋ **Mathlib 二次互反** ✓ ＋ `no_multiplicative_agreement` ✓ |
| **残余** | ⚠️ | `*_nat` 深层引理正文（`doubleReflection`／`upperBand`／`quarterBand`／`centralBand` ✓）＋ `oddCompletion`／`centralRepresentative` 构造正文 ✓ |
| **独立复现** | ✗ 未做 | 未自行 `lake build`／未跑 Comparator ✓ |
| **provenance** | ✗ 未闭合 | 仓库自证 Astra 关联 ✗ |

## §3 机制标签：FSD（✓，**标签非框架** ✗）

$$\boxed{\textbf{Failure} \to \textbf{Symmetry} \to \textbf{Descent}}$$

**七步模板** ✓：
```
独立算术问题 → 假设目标失败 → failure 产生局部约束 → 两个可交换的自然作用
→ defect compatibility → minimal bad object → strict descent → global algebraic rigidity
```

**发动机（本档新提炼 ✓✓）**：不是某个复杂定理，而是
$$\boxed{\textbf{4 个局部公理（sign／doubling／tripling／noPP）}＋\textbf{两个可交换作用}}✓$$
—— `IntervalSigns` 极"贫" ✓，却派生 `noNN` → `reflection` → `translation` → 三条 band → defect 正性 → defect 支撑 → 交换刚性 ✓（**全为派生 lemma，非隐藏假设** ✓✓）

**与旧范式对照**（✓）：correlation → **compatibility** ✓；local ⟹ global → **minimal-obstruction descent** ✓；谱／连续参数 → **离散代数闭包对象**（`H <= F_p^×` ✓）；invariant → **failure set** ✓；算术函数 → **作用群** ✓

## §4 纪律（✓✓，写死）

$$\textbf{① 不接}\ RH\ \text{主线}✗；\textbf{② 不照搬}✗（\text{把}\ \lambda\ \text{换成某}\ RH\ \text{对象再套一遍＝repackaging}✗）；\textbf{③ 不排序}✗（\text{不与}\ L／F／B／R\ \text{并列排序}✓）$$
$$\textbf{④ 不声称已复现／已同行评审}✗；\textbf{⑤ provenance 与逻辑正确性分离}✓✓（\text{媒体归因}\ne\ \text{定理成立}✓）$$
$$\textbf{⑥ 不建新判据体系}✗（FSD\ \text{只作标签}✓，\text{不作筛选框架}✗）$$

## §5 合法用途（✓，供后续）

- **对照样本** ✓：为"独立问题 → 内部机制"提供**已存在**的实例 ✓（非我们构造 ✓）
- **问句来源** ✓：下一刀问句 = 「在 RH 的独立算术对象里，哪里存在**两种天然可交换的算术作用**，使目标失败产生两个 defect 且其 compatibility 诱发**严格下降**？」✓（**先审问句存在性** ✓，**不先设计对象** ✗）
- **对照不并入** ✓：与 `C-286-B` 的 divisor／local→global 死墙**不是同一机制** ✓（可对照 ✗ 不并入 ✗）

## §6 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：本项目成果 ✗；已独立复现 ✗；Astra 官方成果 ✗；FSD 是新判据 ✗
- **本档新增词**：`独立算术机制资产`／`4 公理＋两交换作用`（0 命中 ✓）
