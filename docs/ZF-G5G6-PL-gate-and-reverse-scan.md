已查地图：命中（`ZF-G5G6-DIM-screen-and-height-collapse`／`ZF-CONT-1/2/3`／`ZF-LEM`／`E-11`／`E-44` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = 对上一档 `HG` 门的自我更正 ＋ 替代门 `PL`（逐零点定位）＋ 按新门重扫 `§95` 存活清单
D1: 0 （`[REVIEW]` 轮次：更正与筛选，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-G5G6` 续：`HG` 自我更正 ＋ 替代门 `PL` ＋ `§95` 五类重扫**（本档全为自行推导 ✓✓）

## §0 ⚠️ **自我更正：上一档的 `HG`（高度塌缩门）推错了 —— 它把两条不同路线混为一谈**

```
【上一档的推导】 我由"算术侧 Northcott 只给有界高度内的有限性"推出"anomaly 须高度有界" ⟹ 进而要求 `\Phi` **高度摧毁** ⟹ 得 `HG` ✓（当时记为"统一解释本仓全部失败"）
【本档反查 —— 错在何处】 在**您 §109 的架构**下根本**不需要**这一步：
　由架构：`\mathcal D=F^{-1}(0)` **有限** ＋ `\sup_{d\in\mathcal D}|\Phi^{-1}(d)|<\infty` ⟹ 立刻
　$$\#\bigl(Z_{\rm off}\cap\Phi^{-1}(\mathcal D)\bigr)=\sum_{d\in\mathcal D}\bigl|\Phi^{-1}(d)\bigr|\le|\mathcal D|\cdot\sup_{d}|\Phi^{-1}(d)|<\infty$$ ✓✓
　⟹ **`\mathcal D` 有限本身就是 `Route A`**（直接由 `compact+discrete+\infty`-分离得）⟹ **完全不需要"高度有界"** ✓
【错因】 我把 `Route A`（`\mathcal D` **直接**有限：`closed+discrete+compact`，§107）与 `Route B`（`\mathcal D` 经**算术计数**有限：Northcott 型，只给有界高度内有限）**混为一谈** ⟹ `HG` 只对 `Route B` 成立，**对 `Route A` 不必要** ✗
【⟹ `HG` 的正确地位】 ⛔ **不是必要门**；它只是 `Route B`（走北cott/计数型有限性）时的**充分附加条件** ✓
【⟹ 连带更正】 上一档"`HG` 一次性解释本仓全部既有实现为何不可能成功"**过大** ✗ ⟹ 正确诊断见 §2（`PL`）✓✓
```

## §1 **保留部分**：`DIM`／`CAN`／`VI` 三不受影响

```
`DIM`（异常层须零维：`r\ge d` 或等价的有限容量定理）✓｜`CAN`（方程须由母理论 canonical 产生，⛔ 不可为凑维数人工拼）✓｜`VI`（强接口：`\Phi(Z_{\rm off})\subset\mathcal D^{(0)}` 零维有限子层）✓ —— 三者**不受 §0 更正影响** ✓
```

## §2 ⭐⭐ **替代门 `PL`（逐零点定位）—— 由 §109 架构直接导出，不是额外假设**

```
【导出】 §109 的结构是：`\mathcal D=F^{-1}(0)\subset\mathcal M`，`\Phi:Z(\zeta)\to\mathcal M`，判据为
　$$\rho\in Z_{\rm off}\ \Longrightarrow\ \Phi(\rho)\in\mathcal D\qquad\text{（即 }F(\Phi(\rho))=0\text{）}$$ ✓
　⟹ 这是**逐零点（pointwise）**判据：`\mathcal D` 是 `\mathcal M` 中的**点集**，其成员资格必须**由 `\Phi(\rho)` 单独决定** ✓✓
【⟹ 门 `PL`】 $$\boxed{\text{载体必须是"}\rho\mapsto\Phi(\rho)\mapsto F(\Phi(\rho))\text{"型（可在单个零点处求值）}}$$ ✓✓
【⛔ 被 `PL` 排除的形态（正是本仓全部工具）】 一切**聚合型**量：
　· `\Sigma` 于零点集之上的和（`\sum_j\log`、`\xi'/\xi`、显式公式的零点求和）✗
　· **被高度截断的族**（`S(T)`、`N(T)`、`A_t`（`t` 为高度）、`n_-(Q_T)`、Hankel 矩（到 `T`））✗
　· 任何"依赖其它零点/依赖截断高度"的量 ✗ ✓✓
【⭐ 与 `HG` 的关键差别（这决定 `PL` 是否正确）】 `PL` **不禁止** `\Phi` 本身依赖 `\gamma`（例如 `\rho\mapsto` 某个由 `\rho` 位置决定的算术对象是允许的 ✓）；它只禁止**聚合/截断**型依赖 ⟹ **`PL` 严格弱于 `HG`**，故不会误杀合法候选 ✓✓
【⭐⭐ 对既有失败的正确统一解释】 本仓既有实现失败的结构原因**不是**"保留高度"，而是 $$\boxed{\text{它们是\textbf{聚合型}的：依赖其它零点或依赖截断高度，故无法给出"逐零点"的点集判据}}$$ ✓✓
　（与 `D3`（extensive）、`D8`（偶/二阶盲）**相容且更强**：`PL` 说明即便 `D3`/`D8` 不成立，聚合型仍必死 ✓）
```

## §3 ⭐⭐ **按新门重扫 `§95` 五类存活清单（本档）**

```
【(4) monodromy / branch-type change】 ⛔ **`DIM` FAIL**：单值跳变的轨迹通常是**分支轨迹**＝除子（余维 1）⟹ 正维 ✗；且单值性是**沿族（随参数）**的概念 ⟹ 天然聚合 ⟹ `PL` FAIL ✗ ⟹ **双重判死** ✓✓
【(3) finite-degree degeneration】 ⛔ **`DIM` FAIL**（典型）：退化轨迹＝判别式轨迹＝**超曲面**（余维 1）✗ ⟹ 只有当**多重条件**（多兼容）时才可能零维 ⟹ **归约到 §111.4（multi-compatibility）分支**，**非独立存活** ✓
【(5) canonical discrete decomposition failure】 ⛔ **`DIM` FAIL**（典型）：分解失败轨迹（如可约轨迹）通常**正维** ✗ ⟹ 同样**归约到多兼容分支** ✓
【(2) finite-length / extension obstruction】 ⚠️ **`DIM` FAIL**（典型）：长度/扩张的"跳变轨迹"通常是除子 ✗ ⟹ 除非多条件，亦归约 ✓
【(1) global compatibility obstruction】 ✅ **`DIM` PASS**（非常规交轨迹可达**零维**，此即 Zilber–Pink/André–Oort 型理论的核心输出）｜✅ **`CAN` PASS**（特殊子簇/非常规交是 canonical 的）｜✅ **`PL` PASS**（兼容性是**逐点条件** ✓✓）｜⚠️ **`VI` ＝ GAP**（须 zeta 实现落入零维层，未知）✓✓
【⟹ 重扫结论】 $$\boxed{\text{五类中仅 (1) global compatibility 通过 }DIM+CAN+PL;\ \text{其余四类在 }DIM\text{ 处归约到多兼容分支}}$$ ✓✓
　⟹ 与 `§111.4` 的 `OPEN+` 判断**一致**：真正剩下的只有**多兼容型/全局兼容型**一条主干 ✓
```

## §4 **修正后的硬门集合 ＋ 下一步**

```
【硬门（修正版）】 $$\boxed{DIM\ (\text{异常零维})\ +\ CAN\ (\text{方程 canonical})\ +\ PL\ (\text{逐零点可求值})\ +\ VI\ (\text{强接口，}\mathcal D\ \text{零维有限})}$$ ✓
　（`HG` 降级为 `Route B` 专用充分条件，**不再列为必要门** ✓）
【对第 4 问（Zilber–Pink/o-minimality 型机制）的更新判定】 在修正门集下，该机制**不再被 `HG` 排除** ⟹ **它是目前唯一通过 `DIM`+`CAN`+`PL` 的机制族** ⟹ 唯一致命处仍是 `VI`（zeta 实现），即**真正的 GAP** ✓✓
【对第 5 问的更新判定】 仍 **GAP**；⛔ 但**不得**再以 `HG` 为由宣布"算术字典必然失败"（那是上一档的错推）⟹ 正确表述：**尚无已知的、满足 `PL` 的 zeta↔特殊点实现** ✓
【边界】 ⛔ 未制造候选／未启动搜索／未改状态；⭐ §0 更正、§2 `PL`、§3 重扫均为**本档自行推导** ✓
```
