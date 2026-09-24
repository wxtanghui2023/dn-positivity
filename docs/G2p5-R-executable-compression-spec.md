已查地图：命中（`F1-downrank-F5-F3-audit-G2p5-is-binding`／`F1-dual-audit-and-G2p5-gate`／`F2-structural-feasibility-verdict-A`／`P1-3-unresolved-finite-problem-pool`）⟹ 引用，不开新案
D0: 本档对象 = **`G2.5-R` 可执行压缩规格**（四源分解／"至少三项"硬门／竞争排除／新 `G3`／反转流水线／`S/P/H/M` 模板）
D1: 0 （[REVIEW] 轮次：规格化，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`G2.5-R`：可执行压缩规格**

## §0 ⭐ 核心反转（照录）

```
$$\boxed{\text{先搜索"压缩机制"，再由压缩机制生成问题族}}$$ ✓✓
【废】 "先搜开放问题，再问能不能压缩" ✗（旧循环：`开放问题池\to 逐个规模审计\to 全部淘汰`）✓
```

## §1 四源分解

```
定义结构压缩指数 $$\mathcal C(P)=\mathcal C_{\rm sym}\cdot\mathcal C_{\rm prop}\cdot\mathcal C_{\rm rank}\cdot\mathcal C_{\rm cert}$$ ✓
**【1】`\mathcal C_{\rm sym}`（对称压缩）**：需有**问题自身天然**的群作用 `G\curvearrowright X` 且 `|X/G|\ll|X|`；**最低要求** $$\log_{10}|X/G|\ \ll\ \log_{10}|X|$$ ✓
　反例（`F5`）：`\binom{111}{11}\sim10^{15}`、`|G|\sim10^2` ⟹ **压缩无意义** ✓
**【2】`\mathcal C_{\rm prop}`（强传播）—— 比群作用更重要**：需局部条件使**一个局部赋值引发大批后继决定/排除**；**经验传播率** $$\pi=\frac{\text{一次合法扩展后被排除/确定的状态}}{\text{当前剩余状态}}$$ 且须有理由相信 `\pi` **随深度不迅速趋于 0** ✓✓
　反例（`F2`）：约束数很多，但"放一条边"对其它边的排除**极弱** ✓
**【3】`\mathcal C_{\rm rank}`（高阶一致性）—— 我方资产最可能占优处**：$$\boxed{\text{寻找"高阶约束很多"的问题，而不是"变量很多"的问题}}$$ 形态：**低阶局部数据 ＋ 大量高阶 compatibility 方程**决定全局对象（如 `T_{ijk}\in\{\pm1\}` 且满足 `T_{ijk}T_{ijl}T_{ikl}T_{jkl}=\cdots` 型关系）⟹ **正是 `A`/`E` 的 chirotope、cocycle、rank、quadratic exclusion 用武之地** ✓✓
**【4】`\mathcal C_{\rm cert}`（小证书）**：$$\text{巨大搜索空间}\to\text{短数学证书（几十页内）}$$ 而非 `10^{12}` 节点 DRAT ⟹ $$\boxed{\text{不得因"有 DRAT"就认为 }G2.5\text{ 通过}}$$ ✓✓
```

## §2 ⭐ 硬门 `G2.5-R` ＋ 竞争排除

```
$$\boxed{\text{四源中至少满足三项，方入候选池}}$$ ✓✓
$$\boxed{\text{竞争排除：若现有专门团队已在利用同一压缩机制，则不得仅凭"我们也能实现"进入主攻}}$$ ✓✓
```

## §3 新 `G3`（照录）

```
$$\boxed{G3=\text{能否在预计计算预算内产生"新数学结果"}}$$ ✓✓
【不再接受】 "理论上 SAT 可以跑" ✗
【必须估计】 `N_{\rm eff}`（压缩后有效状态数），且要求 $$\boxed{N_{\rm eff}\lesssim10^{8}\text{–}10^{10}}\quad\text{（第一轮实际攻击的粗尺度门槛）}$$ ✓✓
【说明（照录）】 超过此数**非数学上不可能**，而是**我们的当前资产没有理由承担这种搜索** ✓
```

## §4 反转流水线（照录）

```
$$\boxed{\text{结构模板}\to G2.5\text{-R}\to\text{具体开放问题}\to G1\to G2\to G3\to G4}$$ ✓✓
（替代旧序：`开放问题池\to G2.5\to 全部被淘汰`）✓
```

## §5 结构模板（本轮只登记，不找候选）

```
**`S` 型（巨大对称群）**：`G\gg1`、`X/G` 很小，但文献**未把该群作用彻底用于目标参数** ⟹ ⚠️ 易被 `nauty/SAT` 社区占据 ✓
**`P` 型（强传播）**：局部禁形 `\Rightarrow` 级联排除；重**确定性传播结构** ⟹ ⚠️ 易退化为普通 SAT ✓
**`H` 型（高阶一致性）**：低阶局部数据 ＋ 高阶 compatibility 决定全局 ⟹ ⭐ **首选** ✓✓
**`M` 型（混合）**：大对称群 ＋ 强传播 ＋ 高阶一致性 ＋ 小证书 ⟹ ⭐⭐ **最值得认真投入** ✓✓
【为何优先 `H`/`M`（照录）】 `H`/`M` **直接匹配 `A+D+E`**（finite geometry／chirotope／cocycle／rank／quadratic exclusion／exact certificate），**且不易被普通 SAT 队伍直接复制** ✓✓
```

## §6 下一步

```
【下一轮】**按 `H`/`M` 型去寻找具体的\textbf{未决有限问题}** ✓
【本轮】**不找具体候选、不计算**（规格落档为止）✓
【⛔ 纪律】 `n=38`／`TARGET-L9`／RH 未作筛选依据 ✓
【边界】 §0–§4 为**照录您的裁示/登记**；§5 模板与优先理由为**照录＋本档登记**；未制造候选／未启动搜索／未碰 RH。
