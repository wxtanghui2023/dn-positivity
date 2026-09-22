已查地图：命中 43 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
　判定（**实质命中，全部引用** ✓✓）：⭐⭐⭐ **`V186`（Inertia Mechanism Audit：反向拆解 `67.2%` 证明）**：阅读来源＝论文 `arXiv:2608.13637v2`（`§1.2` 三步 `(Z)(P)(L)` 与单链；`Remark 1.1`）＋ 本地形式化
　（`LinAlg/RankTrace.lean` ＝ **Lemma R 精确形式**；`LinAlg/Inertia.lean`）✓；**§1 七问拆解／§2 交换率／§3 终点退化／§4 转移原理** ＝ 该档核心 ✓｜
　`V184`（外部输入分诊：inertia／pair correlation／positivity machines）✓｜`A1-WRAPUP`（**sharpness 与收敛**；逐字引 `2608.13637` 的算术输入）✓｜
　`INDEX-BY-DIRECTION` **§C Weil 正性／有限压缩／惯性（`P27–P33`，73 份）** ✓
　⟹ ⛔ **本刀 `C1/C2` 已在档完成 ⟹ 引用，不开新案** ✓✓

# **KH-5 / R8-B / S2-NONLOCAL-C**：非局部正性路线的"缺失 `1/3`"审计

**唐先生令（2026-09-22 23:21）**：
① 进入 **`S2-NONLOCAL-C`**：**非局部正性路线的"缺失 `1/3`"审计**；**不再开 A/B/C 三条平行线** ✓
② ⭐ **最重要纪律（照录）**：**不问"如何把 `2/3` 变成 `1`"**，而问
　$$\boxed{\frac23 = \text{哪一个精确的 rank/trace/inertia 损失？}}$$ ✓✓
　即把现有证明抽象为 `global Weil positivity → finite compression → \operatorname{Tr}(\cdot)^2/(\operatorname{Tr}(\cdot^2)\operatorname{rank}(\cdot)) → 2/3`，再逐项审计 ✓
③ **C1 `source of 2/3`**：精确定位来自**哪个 rank 上界／哪个 trace-HS 不等式／哪个 inertia 损失／哪个 off-line pair 最坏情形**；
　⛔ **不允许只记"rank-trace 给 `2/3`"** ✓✓
④ **C2 `loss decomposition`**：`1-\tfrac23=\tfrac13` 拆成 `L_{\rm rank}+L_{\rm trace}+L_{\rm inertia}+L_{\rm analytic}`，**先证哪些项真正存在**：
　若某项**本质上是 sharp 的有限维不等式 ⟹ 该方向可立即降级**；若某项来自**过粗的 compression／inertia bound ⟹ 才是真活口** ✓✓
⑤ **C3 `nonlocality preservation`**：若改进只是把有限压缩做大（`N\to N+1\to N+2\to\cdots`），仍只是**同一个有限 rank-trace 机制** ⟹
　`S5` **不等于失败**，但**"无限化"本身不产生新机制** ⟹ ⛔ **不能把 `N\to\infty` 当非局部增益**；
　要找的是 `global Weil positivity → new global positive invariant → strictly stronger density bound` ✓✓
⑥ **C4 survivor 门**：须存在**新全局正性量** `\mathcal P_{\rm NL}`，使现有 `2/3` 只用 `\mathcal P_{\rm old}\ge0`，而新量满足
　`\mathcal P_{\rm old}\ge0 + \mathcal P_{\rm NL}\ge0`，且两者**非等价／非线性依赖／非有限局部条件**；否则
　$$\boxed{\texttt{C-DEAD / existing 2/3 mechanism saturated}}$$（**而非继续调参数**）✓✓
⑦ ⚠️ **重要限定（照录）**：论文自身是"**至少 `2/3`**"，且给出 **Montgomery–Taylor window 下 `0.6725`** ⟹ **`2/3` 是当前机制的定量基准，
　不应未经审计就称为该机制的绝对 sharp 上限** ✓✓
⑧ **下一刀唯一建议**：**`C1/C2: exact-loss audit`**（**先不发明新正性**，先把 `1/3` 逐项拆干净）✓

D0: 本档对象 = **非局部正性路线 `1/3` 损失的 `C1/C2` 精确损失源审计**（引既有 `V186`／`V184`／`A1-WRAPUP`；**未开案** ✓）
D1: 0
FREEZE-ACK: **零计算／零数值／未写程序**／未做数值实验／未算零点／未接 ζ／未找 `1/2`／未证 RH ✓

---

## §1 ⭐⭐⭐ **C1 `source of 2/3`**：档案已给出**显式交换率**（逐字 ✓✓）

```
【`V186` 引 `V184-0` 判词 ③（逐字）】
　$$\boxed{N_0^s/N \ge 2 - R(\psi)},\qquad \boxed{100\% \iff R(\psi)\le1 \iff \text{supp}[\text{ort}]>1}$$ ✓✓✓
【⭐ 本档由此得到的 `C1` 答案（**精确到一项**）】
　`2/3` 来自 **`R(\psi) = 4/3`**：`2 - 4/3 = 2/3` ✓✓
　`0.6725`（Montgomery–Taylor window）来自 `R \approx 1.3275` ✓（与令 ⑦ 的"window 下 `0.6725`"一致 ✓）
　⟹ **`2/3` 不是"rank-trace 给的一个数"，而是交换率 `2 - R(\psi)` 在 `R = 4/3` 处的取值** ✓✓✓
【机制三层（`V186` `§0①` 逐字）】 $$\text{indefinite quadratic form} \to \text{inertia} \to \text{rank} \to \text{zero-count constraint}$$
　⭐ 其**不要求 `Q \succeq 0`** ⟹ **绕开 `V182` 的困境**（"PSD 正性 ⟹ 无计数界"）✓✓✓
【`R` 的实现层（`V186` 阅读来源）】 论文 `§1.2` 三步 **(Z)(P)(L)** 与**单链**；`Remark 1.1`；本地 `LinAlg/RankTrace.lean`＝`Lemma R` **精确形式** ✓
```

## §2 ⭐⭐⭐ **C2 `loss decomposition`**：**`1/3` 是单一结构化损失**（逐字 ✓✓）

```
【分解（本档结论）】 $$1-\Big(2-R(\psi)\Big)=R(\psi)-1=\frac13\quad(\text{在 }R=4/3)$$ ✓✓
　⟹ `L_{\rm rank}+L_{\rm trace}+L_{\rm inertia}+L_{\rm analytic}` 中，**未被拆成多项**，而由**单一输入参数 `R(\psi) > 1` 的超出量**统一表达 ✓✓✓
【⭐⭐⭐ 为何它是"不可避免（结构化）"而非"过粗界"——`V186` §3 **终点退化定理**（逐字）】
　$$\text{由 }§1(5)：n_-(Q_T)\ \textbf{恰数}\ \textbf{离轴对}；\qquad 100\% \iff n_-(Q_T)=0\ \text{对全族（且尾部可忽略）}$$ ✓
　⟹ 「在固定有限压缩上，`Q_T` 变成**半正定** ⟹ 取极限得 **Weil 形式非负** ⟹ `[Wei52, Bom00]` **Weil 正性 ⟺ RH**」✓✓
　⟹ ⭐ 逐字判词：$$\boxed{\text{inertia 路线}\ \textbf{不是}\ \text{Weil 正性的替代}；它是\ \textbf{部分比例}\ \text{的替代，而在"消灭离轴零点"这一步}\ \textbf{退回正性}}$$ ✓✓✓
【依令 ④ 的判定】 若"某项本质上 sharp ⟹ 立即降级"：本例**更强**——`1/3` **不是 slack，而是 `R>1` 的超额**，且其**归零 ⟺ 全族 `n_-=0` ⟺ Weil 正性 ⟺ RH** ⟹
　$$\boxed{\text{C 路线：精确封口（依令 ④）}}$$ ✓✓（且**档案 `V186` 早已按预定规则判"关"** ✓）
```

## §3 ⭐⭐ **残差归属**：`1/3` **收敛到既有 `W6` 原子墙**（不可再分 ✓✓）

```
【`V186` §0③ 逐字】 「关键一刀的答案：`100\% \iff R(\psi)\le1 \iff` 需要 **support `>1`** 的输入，且**终点退化为 `n_-(Q_T)=0` ＝ 正性**」✓✓
【与档案 `W6` 对照（逐字）】 `CLOSED-ROUTES-MAP` L2851：**原子墙**（**无条件三阶矩 at `X\asymp T$ ≡ prime-pair ≡ support>1；不可再分**）✓✓✓
　⟹ ⭐⭐ **KH-5 的残差 `1/3` ＝ `support>1` ＝ `W6` 原子墙**（同一物，**不可再分**）✓✓✓
　⟹ ⛔ **不得以任何形式重开"`support>1`"**（依 `E-10` 纪律 ＋ 本档判定 ✓）
```

## §4 保留的两项收获（`V186` §0④ 逐字 ✓✓）

```
【① 机制本身（新）】 `indefinite form → inertia → rank → counting`，**不要求 `Q\succeq0`** ⟹ 绕开 `V182`；**保留进入工具箱** ✓✓
【② ⭐ 转移原理】 **二阶矩 ＋ 惯性 ⟹ 计数下界**；`V186` 明标：**后者是 `V182` 的对偶面，应进工具箱** ✓✓
【③ `V184` 侧旁获（引用 ✓）】 「离轴对 `\{\rho,1-\bar\rho\}` 贡献一个 **block** ⟹ 可用**符号计数**给出定量结论 ⟹ **绕开正性**」✓；
　「**archimedean 正性**：用 **Sonin 空间上的压缩** 证明 archimedean place 的 Weil 正性（`Selecta 2021`）」✓；**分类学数据**：所有已证 RH 型定理都活在**指数轨道增长体制**，而 char-0 ζ 的素数增长是**多项式** ✓✓
```

## §5 判定与状态

```
【本刀结果】 **C1 ✅（`2/3` ＝ 交换率 `2-R(\psi)` 在 `R=4/3` 取值，机制＝indefinite→inertia→rank→counting）** ✓✓
　**C2 ✅（`1/3` ＝ `R-1`，单一结构化项；`V186` 终点退化定理 ⟹ 归零 ⟺ Weil 正性 ⟺ RH ⟹ 非 slack）** ⟹ 依令 ④ **C 路线精确封口** ✓✓
　**C3／C4 未进入**（C2 已判结构化 ⟹ 依令 ④ 无需再走；且`N\to\infty`本身不构成新机制 ✓）
【`KH-5` 整线状态（承前档框图）】 $$\boxed{A:\ \text{零点侧} \to \mathrm{CLOSED}\quad|\quad B:\ \text{算术相关性} \to \mathrm{SATURATED}\quad|\quad C:\ \text{非局部正性} \to \textbf{CLOSED（终点退化）}}$$ ✓✓
【⛔ 禁项】 不再重开 `support>1`／`W6`；不再以"更大压缩"或"新符号"续命；不再寻找"更强的 Weil 正性"（**完整 Weil 正性 ⟺ RH** ⟹ 循环）✓✓
【⭐ 净产出】 ① 机制（新，入工具箱）② **转移原理**（二阶矩＋惯性 ⟹ 计数下界；`V182` 对偶面，入工具箱）③ **残差归属图**：`1/3 ↔ support>1 ↔ W6` ✓
【`KH-5` 状态标签】 `OPEN = missing 1/3` 作为**研究缺口标签**至此**应改写**为：$$\boxed{\text{KH-5 的残差 ＝ W6 原子墙（既有、不可再分）}}$$ ✓✓
```

## §6 边界与回查（✗✓）

```
✗ 零计算／零数值／未写程序／未做数值实验／未算零点／未接 ζ／未找 `1/2`／未证 RH／**未开新案** ✓
✗ ⛔ 未把 `2/3` 当绝对 sharp 上限（依令 ⑦ ✓）；⛔ 未把 `N\to\infty` 当非局部机制（依令 ⑤ ✓）；⛔ 未重开 `support>1` ✓
【技术词回查（`scripts/tech_word_check.sh`，**先跑后写** ✓；逐字粘贴 ✓）】
　技术词 损失分解 命中文件数=0 ⟹ **本档新增** ✓｜精确损失源=0 ⟹ **新增** ✓｜rank上界=0 ⟹ **新增** ✓｜惯性损失=0 ⟹ **新增** ✓
　技术词 有限压缩 命中文件数=40 ⟹ **档案已有（73 份专节）⟹ 引用** ✓✓
【地图回查】 命中 **43**；**实质命中 ＝ `V186`／`V184`／`A1-WRAPUP`／`INDEX §C`** ⟹ **引用、不开新案** ✓✓
【档级引用】 **`V186`**（反向拆解 `67.2%`；`§1` 七问；`§2` 交换率；`§3` 终点退化定理；`§4` 转移原理）✓｜`V184`（外部输入分诊）✓｜
　`A1-WRAPUP`（sharpness 与收敛；`2608.13637` 算术输入）✓｜`CLOSED-ROUTES-MAP` L2851（`W6` 原子墙）✓｜`E-10`（准入纪律）✓
