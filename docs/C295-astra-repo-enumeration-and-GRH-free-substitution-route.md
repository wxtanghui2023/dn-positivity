已查地图（**先查后写**）：`C-294`（证明架构 ＋ GRH 单点承重 ✓）、`C-293`（核验 ＋ 状态判定 ✓）、`C-291`（事件登记 ✓）。外部来源：GitHub `openai/ten-proofs`（✓）、Ingham／Kadiri 文献（✓）。回查见 §5 ✓

D0: 本档对象 = **C-295：Astra 仓库枚举（坐实 claim only）＋ GRH 的无条件替代路线**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（三条 ✓✓）

**① Astra 侧：`claim only` 已坐实** ✗✓ —— `openai/ten-proofs` 仓库的 `.lean` 文件**可枚举**，**其中没有** Liouville／Goldbach 项 ✓
**② GRH 的无条件替代路线在文献中有标准形态** ✓✓ —— **Ingham 型**：零自由区 ＋ 零密度估计 ⟹ 短区间素数定理 ✓（这正是 Remark 6 所指的方向 ✓）
**③ 障碍已定位** ✓：**例外／非典型特征集**（Remark 6 的集合 S ✓）—— 即无法排除"个别特征在短区间上无抵消" ✓

---

## §1 Astra 侧：仓库枚举（**坐实**✓✓）

- 仓库：`github.com/openai/ten-proofs`（Lean 4 **formalizations of the results**）✓
- 工具链：**Lean 4.32.0 ＋ mathlib ＋ Lake** ✓；构建方式 `lake exe cache get` ＋ `lake build All` ✓
- **独立复核**：README 指向 **Comparator** 检查说明 ✓（与 Anthropic 侧同一验证工具 ✓）
- **文件清单（仓库根目录可见）**：`MulticolorTriangleRamsey.lean`／`NonSoficGroup.lean`／`Permanent.lean`／`QuantumParallelRepetition.lean`／`SpherePacking.lean` ＋ 若干 ✓
  ⟹ **清单中没有 Liouville、Goldbach、sign pattern 相关文件** ✗✓
- ⟹ **判定维持**：Astra 的 Liouville 版 Goldbach **无任何一手材料**（无论文／无 Lean 文件／无 OpenAI 说明 ✓）⟹ **`claim only`** ✗✓

## §2 旁证：素数间隙这条线的形式化生态（✓，仅作背景）

- **246 的 Lean 形式化由 Axiom Math 完成** ✓（AxiomProver；2026-08-17 公布；覆盖 Maynard 2013 ＋ Polymath8b 的 600→246 ✓；41 位署名贡献者 ✓）
- **OpenAI Astra 侧把短间隙改进到 186** ✓（官方页 ✓）
- ⟹ 说明：**"素数间隙"这条线有真实的、可复核的 Lean 生态** ✓ —— 而 **Liouville 版 Goldbach 不在其中** ✗✓（对照鲜明 ✓）

## §3 GRH 的无条件替代路线（**文献标准形态**✓✓）

- **核心工具**：原点-free 区域 ＋ 零密度估计的**组合** ⟹ 短区间素数定理 ✓（经典为 **Ingham 型定理** ✓）
  文献原话要点：Ingham 定理"explicitly shows the dependence of the interval length on the combination of the zero-free regions and the zero-density estimates" ✓✓
- **可用的现成部件**（供"去 GRH"路线 A 使用 ✓）：
  - **显式零自由区**（Dirichlet L-函数；如 Kadiri 等的工作 ✓，含显式常数 ✓）
  - **零密度估计**：经典形式 `N(sigma, T) << T^{b(1-sigma)} log^B T` ✓
  - **固定模数的短特征和**：已有针对"**smooth modulus**"（含素数幂 ✓）的短特征和下界改进 ✓ —— 与本题"模数 N 固定"的结构**对口** ✓✓
- **障碍**（Remark 6 的精确内容 ✓）：这些工具给出的是**平均意义**或**排除例外集后**的结论；而本法需要**对全部 ~N 个非主特征一致**的抵消 ✗ —— 即需**隔离例外集 S** 并**证明其贡献可忽略** ✓
  ⟹ **这就是"去 GRH"的具体技术任务** ✓✓（不是哲学问题，是**可判定的技术缺口** ✓）

## §4 状态判定（维持 ✓）

| 对象 | 判定 |
|---|---|
| Astra Liouville claim | **unverified claim** ✗（仓库枚举无该项 ✓） |
| Mangerel 2412.17199 | **条件定理**（GRH 型零自由区下 ✓） |
| Mangerel IMRN 2024 | **定理**（已发表 ✓） |
| 246（素数间隙） | **已验证／已形式化** ✓（Axiom Math ＋ Lean ✓；**另一条线** ✓） |

## §5 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **纪律**：不接 M-TOWER ✗；不建判据 ✗；不与 L／F／B／R 排序 ✗；先不问 RH ✓；二手报道不作证明来源 ✓
- **不得**写成：`ten-proofs` 含 Liouville ✗；Astra 已去 GRH ✗；Ingham 型路线"已经成功" ✗（它给出的是**方向与工具** ✓）
- **本档新增词**：`仓库枚举`／`无条件替代路线`（0 命中 ✓）
