已查地图：命中（`ZF-G5G6-VI-realization-parity-and-pair-separation`／`ZF-G5G6-PL-gate-and-reverse-scan`／`S6`（局部可容许性不能全局锁定）／`E-11`／`E-44` 本线与既有封存）⟹ **引用，不开新案** ✓
D0: 本档对象 = （甲）finite-points 机器类判别 ＋ （乙）局部因子族的 `\sigma`-等变性与 `S6` 撞墙；及由此得到的 `PL`/`S6` 张力
D1: 0 （`[REVIEW]` 轮次：机器判别与张力推导，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-G5G6` 续三：（甲）finite-points 机器 ＋（乙）`PL`/`S6` 张力**（本档全为自行推导 ✓✓）

## §1 ⭐⭐ **（甲）关键判别：Zilber–Pink 型是 "finite-components"，我们需要 "finite-points"**

```
【观察（本档）】 Zilber–Pink / André–Oort 的**输出形态**是：$$\text{"非常规/特殊子簇只有\textbf{有限多个}"}$$ —— 即 **finite-components（有限多个正维分支）** ✓
【而我们需要】 `VI`（强接口）要求 `\mathcal D` 本身**零维有限** ⟹ 即 **finite-points** ✗
【⟹ 判别】 $$\boxed{\text{finite-components}\ \neq\ \text{finite-points}}$$ ⟹ **Zilber–Pink 型机器不足**（除非附加 canonical 条件把分支切成点 ＝ 又回到多兼容 ✓）
【⟹ 修正后的搜索目标】 须找的是**给 finite-points 的成熟机器**，而非给 finite-components 者 ✓✓
```

## §2 ⭐⭐ **成熟的 finite-points 机器清单（本档；均为 canonical、无条件、给"有限个点"）**

```
**① 整点/有理点有限性**：Siegel（`\ge1` 亏格曲线上的**整点**有限 ✓）、Faltings（`\ge2` 亏格曲线上的**有理点**有限 ✓）、⭐ **Baker 型有效界**（对数线性形式 ⟹ 整点**高度有显式界** ⟹ 甚至满足 `Route B` ✓✓）
**② Manin–Mumford / Raynaud**：曲线与**挠点群**的交有限 ✓✓（canonical，条件是"落在挠子群"）
**③ 挠点 ＋ Northcott**：有界高度 ＋ 有限度 ⟹ 有限 ✓（`Route B`）
【共同特征（＝我们要的形态）】 结论都是"**有限个点**" ✓；条件都是 **canonical** 的算术条件（整性／有理性／落在特定子群）✓；且 `②③` 天然带**高度有界** ⟹ `∞`-分离自动 ✓✓
```

## §3 **（甲）搜索目标的精确化**

```
【须同时】 $$\boxed{\text{finite-points 型 canonical 定理}\ +\ \text{自然对合 }\tau\ +\ \text{有限点集落在 }\mathcal M\setminus\operatorname{Fix}(\tau)}$$ ✓
【⚠️ 难点前移】 整点/挠点定理的有限点集**通常不天然带 `\tau`-配对**（`\tau` 须来自**环境结构**，非来自点集本身）⟹ `\tau` 的"先在性"（您 §11／`L3`）**更难满足** ✓
【⟹ 目前状态】 (甲) 给出**明确的候选机器类**（§2 三类），但**未见同时带 `\tau` 者** ⟹ 记为 **GAP-T**（`\tau` 缺口）✓
```

## §4 ⭐ **（乙）自然的 `\sigma`-等变逐零点对象存在**

```
【候选】 **局部因子族**：$$\Phi(\rho):=\Bigl\{p\mapsto\bigl(1-p^{-\rho}\bigr)^{-1}\Bigr\}_p$$ ✓
【性质】 **(a)** 由 `\rho` **单独**决定（`PL` PASS ✓）；**(b)** 功能方程下 `\sigma`-等变（FE 把 Euler 积与 `\Gamma` 因子互换 ⟹ 族随 `\sigma` 变换 ✓）；**(c)** 分离 `\sigma`-对（`\rho\mapsto1-\bar\rho` 改变全部局部因子 ⟹ 除非 `\sigma\rho=\rho` ✓）✓✓
【⟹ 结论】 $$\boxed{\text{实现层（}\Phi\text{ 侧）是可满足的 —— 自然的 }\sigma\text{-等变、逐零点、分离对的对象确实存在}}$$ ✓✓
```

## §5 ⚠️ **（乙）但异常条件落在"局部" ⟹ 撞 `S6`**

```
【问题】 若"异常"＝局部因子的某条件（如某 `p` 处的特殊值／同余／消失），则该条件**只记录局部可容许性** ⟹ 正是本仓 `S6` 阻断者：
　$$\boxed{\text{局部可容许性}\ \not\Rightarrow\ \text{全局锁定}}$$（`S6`；亦与"第一断裂"`\alpha_p\equiv1` 同向）✗
【⟹ 结论】 (乙) 的**自然候选**死在**异常条件侧**，而非实现侧 ✓✓ —— 这是一次**困难的精确定位**：不是"找不到 `\Phi`"，而是"找不到**非局部的**异常条件" ✓
```

## §6 ⭐⭐⭐ **由此得到的核心新张力（本档最重要产出）**

```
【`PL` 要求】 异常须**逐零点可求值** ⟹ **禁止聚合**（不得依赖其它零点或截断高度）✓
【`S6` 要求】 异常须**本质非局部**（纯局部条件不能全局锁定）✓
【⟹ 两者同时成立 ⟹ 所需异常必须是】 $$\boxed{\text{在单个零点处可求值、但\textbf{本质上是全局的}}}$$ —— 即"**整体兼容型**"条件：不是"某处 `p` 的条件"，而是"**整个族 `p\mapsto(\cdot)` 的兼容性**"，且该兼容性**可在 `\rho` 处一次性求值** ✓✓✓
【⭐ 独立会合（好迹象）】 这与你 `§95-(1)` 的 **global compatibility obstruction**、`§113-I` 的 zero compatibility **独立会合** ⟹ 两条独立路线收敛到同一形态 ⟹ 结构可靠 ✓✓
【⟹ 修正后的最终搜索目标（本档）】 $$\boxed{\text{一个"逐零点可求值、本质全局"的 canonical 兼容性条件，其失败集为 finite-points 型}}$$ ✓✓
【边界】 ⛔ 未制造候选／未启动搜索／未改状态；⭐ §1–§6 全为**本档自行推导** ✓
```
