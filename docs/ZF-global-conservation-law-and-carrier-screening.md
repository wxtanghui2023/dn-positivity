已查地图：命中（`E-11`／`E-12`／`E-44`／`V192`／`C263`/`C264`／`A-1`（Guinand 相位锁定）／`S6` 局域锁定／`KH-5` 三非局部类 本线及既有封存档）⟹ **引用，不开新案** ✓
D0: 本档对象 = "有限资源 → 全局守恒律"的推演落档（1–14）＋ 三载体（index／spectral flow／winding）的档案碰撞通道筛查
D1: 0 （`[REVIEW]` 轮次：结构推导与载体筛查，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF`：全局守恒律要求 ＋ 载体筛查**（唐先生 2026-09-23 17:59 推演 1–14；本档落档＋续推 ✓）

## §1 **从"每零点消耗 1 单位"到全局守恒律（照录 ✓✓）**

```
【设定】 独立问题 `P` 给出全局对象 `X` 与**整数值** `\kappa(T)`（`T`＝高度截断）；希望 $$\kappa(T)\le K\ (\forall T\ge T_0)$$，且每增一个离轴零点 $$\kappa(T_2)-\kappa(T_1)\ge1$$ ⟹ 则
　$$N_{\rm off}(T_1,T_2)\le\kappa(T_2)-\kappa(T_1)\le K-\kappa(T_1)$$ ⟹ **全体离轴零点有限** ✓
【⭐ 隐藏的下一堵墙（照录 ✓✓）】 $$\boxed{\text{为什么 }\kappa(T_2)-\kappa(T_1)\text{ 能同时满足"局部识别"与"全局有界"？}}$$ ✓
```

## §2 **局部事件必须嵌入全局守恒量（照录 ✓✓）**

```
【为何 `e_j\ge1` 不够】 可能出现 $$e_1=1,\ e_2=-1,\ e_3=1,\ e_4=-1,\dots$$ ⟹ **总量不增长** ✗ ⟹ 须**定向性** ✓
【须在同一全局量中】 $$\kappa(T)=\kappa(T_0)+\sum_{\gamma_j\le T}e_j+\text{boundary term}$$；若边界项仅 `O(1)` ⟹ 无穷离轴零点 ⟹ `\kappa(T)\to\infty` ✓
【⟹ 独立问题须同时给出】 $$\boxed{\text{局部离散事件}+\text{全局可加性}+\text{全局上界}}$$ —— **比"存在有限异常类型"严格得多** ✓✓
```

## §3 **⛔ 排除一大类"有限资源"方案：有限标签 ≠ 有限零点（照录 ✓✓）**

```
【反例】 若资源仅 $$R(\rho)\in\{1,\dots,K\}$$（每零点一个**有限标签**）⟹ 即使 `N_{\rm off}=\infty` 也完全可能 $$R(\rho_1)=R(\rho_3)=\dots=1,\ R(\rho_2)=R(\rho_4)=\dots=2$$ ⟹ $$\boxed{\text{有限标签}\neq\text{有限零点}}$$ ✓✓
【⟹ 须"资源消耗的历史性"】 $$R_0<R_1<R_2<\cdots$$ ⟹ 资源**不是给零点贴标签**，而是 $$\boxed{\text{前一个异常发生后，系统状态永久改变}}$$（＝"不可复用"的最严格数学版本 ✓✓）
```

## §4 **不可复用 ⟺ 存在单调状态变量 ＋ 独立 rank（照录 ✓✓）**

```
【须独立定义的 rank】 $$r:X\to\mathbb N$$ 满足 $$X_{j+1}\succ X_j\Longrightarrow r(X_{j+1})\ge r(X_j)+1$$ ⟹ $$r(X_N)\ge r(X_0)+N$$ ⟹ 若独立定理给 `r(X)\le K` ⟹ `N\le K-r(X_0)` ✓
【⟹ 必要结构】 $$\boxed{\text{off-axis zero}\Rightarrow\text{strict rank increase}}$$ —— ⛔ **不是** "off-axis zero ⟹ some anomaly" ✓✓
【⛔ 关键限制（§5 照录 ✓✓）】 rank **不能是零点编号**（`r_j=j` 完全无效，只是把"第 `j` 个零点"改名）⟹ 须 $$r(X)\ \text{在 }P\ \text{中独立存在，不依赖 }\zeta\ \text{零点枚举}$$ ✓
```

## §6 **连续参数 `\delta\to0` 对 rank 无意义（照录 ✓✓）**

```
【危险序列】 $$\rho_j=\tfrac12+\delta_j+i\gamma_j,\qquad\delta_j\to0$$ ⟹ 若 rank 是**连续响应** `r(\delta)\to r(0)` ⟹ 无法产生 `r_j\ge j` ✗ ⟹ 须 $$\boxed{\delta\ne0\Rightarrow\text{一次完整的离散状态跃迁}}$$ ✓✓
【⟹ 比此前更强】 成功接口**甚至不能只是一个"离散标签"**，须是 $$\boxed{\text{具历史方向的离散状态跃迁}}$$ ✓
```

## §7 **三载体浮现：index／spectral flow／obstruction（照录表 ✓✓）**

| 结构 | 离散 | 可加 | 有方向 | 可有全局界 |
|:--|:--:|:--:|:--:|:--:|
| winding number | ✓ | ✓ | ✓ | 有时 |
| **index** | ✓ | ✓ | ✓ | ✓ |
| spectral flow | ✓ | ✓ | ✓ | 通常需额外界 |
| 普通连续函数 | ✗ | 可 | ✗ | 不足 |
| 有限标签 | ✓ | ✗ | ✗ | ✗ |
| 单纯 singularity | ✓/局部 | ✗ | ✗ | ✗ |

```
【最符合架构】 $$\boxed{\text{index-type obstruction}}$$ —— `\operatorname{ind}` 是整数且**可加**：$$\operatorname{ind}(AB)=\operatorname{ind}(A)+\operatorname{ind}(B)$$ ✓；
　且 `\operatorname{ind}:\text{Fredholm}\to\mathbb Z` 在连续变形下**不变**，只在穿过**非-Fredholm/singular wall** 时改变 ⟹ 正合 $$\boxed{\text{regular region}\to\text{singular wall}\to\text{integer jump}}$$ ✓✓
```

## §8–§9 **反杀条件 ＋ spectral flow 的定向（照录 ✓✓）**

```
【⛔ 不能只用 index】 普通 index 可**正负抵消** ⟹ 须 $$\boxed{\zeta(\rho)=0,\ \Re\rho\ne\tfrac12\Longrightarrow\Delta\operatorname{ind}\ge1}$$ —— ⛔ **不是** `\Delta\operatorname{ind}\ne0`（否则 `+1,-1,+1,-1,\dots` 仍可能）✓✓
【spectral flow】 $$\operatorname{SF}(A_t)=\#(\text{正向穿越})-\#(\text{反向穿越})$$；若可证"离轴 ⟹ **同向穿越一次**" ⟹ $$\operatorname{SF}(T)\ge N_{\rm off}(T)-C$$；若独立给 `\operatorname{SF}(T)\le K` ⟹ $$N_{\rm off}\le K+C$$ ✓
　⟹ 具体可检验机制：$$\boxed{\text{zero}\to\text{crossing}\to\text{positive spectral flow}\to\text{bounded global flow}}$$ ✓✓
```

## §10–§11 **方向判别 ＋ `\tau` 的独立性（照录 ✓✓）**

```
【须分裂】 $$\boxed{\text{critical zero}\Rightarrow\text{neutral/regular crossing}};\qquad\boxed{\text{off-axis zero}\Rightarrow\text{oriented non-neutral crossing}}$$ —— 该区别须来自**独立结构的对称性/兼容性**，⛔ **不能人为塞 `\beta-\tfrac12`** ✓✓
【`\tau` 须先在独立母问题中存在】 形式 `\tau A_t\tau^{-1}=A_{\sigma(t)}`，临界线对应**固定轨道** `\sigma(t)=t`；⛔ **不得**把 `\tau` 定义成 `s\mapsto1-\bar s` 再说"临界线就是固定点"（**直接违反独立问题纪律**）✓✓
```

## §12 **最小定理模板（5 可证命题，照录 ✓✓）**

```
**A.** 独立母问题：存在与 `\zeta` 无关的对象族 `A_t,\ t\in\mathcal P`；
**B.** 离散全局不变量：`\kappa(A_t)\in\mathbb Z`，沿允许变形只有**整数跃迁**；
**C.** 全局上界（独立定理）：$$\boxed{\kappa(T)\le K}$$，`K` **与高度 `T` 无关**；
**D.** 零点接口（**非循环、非定义式** realization theorem）：$$\boxed{\zeta(\rho)=0,\ \Re\rho\ne\tfrac12\Rightarrow\Delta\kappa(\rho)\ge1};\qquad\boxed{\zeta(\rho)=0,\ \Re\rho=\tfrac12\Rightarrow\Delta\kappa(\rho)=0}$$；
**E.** 可加且不可抵消：$$\kappa(T_2)-\kappa(T_1)\ge N_{\rm off}(T_1,T_2)-C$$ ⟹ $$N_{\rm off}\le K+C$$ ✓
```

## §13 **强筛选结论（照录 ✓✓）**

```
【今后遇到"独立问题候选"直接问】 $$\boxed{\text{它能不能产生一个 bounded, oriented, additive integer obstruction？}}$$ 若不能 ⟹ **不必再研究其漂亮解析结构** ✓
【四类排除】 连续 detector ⟹ **排除**｜有限标签 ⟹ **排除**｜无方向 crossing ⟹ **排除**｜有向但无全局界 ⟹ **不能证明有限** ✓
【剩下值得追者】 $$\boxed{\textbf{independent bounded oriented integer flow}}$$；最难一步：$$\boxed{\textbf{为什么 off-axis zeta zero 必然触发这种 flow，而 critical zero 不触发？}}$$ ✓✓
```

## §14 **状态表（照录 ✓✓）**

| 层级 | 状态 |
|:--|:--|
| 连续横向检测 | **CLOSED** |
| 有限标签 | **CLOSED** |
| 有限异常集但无不可复用性 | **CLOSED** |
| 无方向的 crossing | **CLOSED** |
| 有方向但无全局上界 | **INSUFFICIENT** |
| 有界 index / flow | **候选机制** |
| critical neutral / off-axis positive 分裂 | **核心 OPEN** |
| zero → flow 的独立 realization theorem | **最终 OPEN** |

## §15 ⭐⭐ **载体 × 档案碰撞通道筛查（本档新增 ✓✓）**

| 载体 | 结构条件 | **与本仓既有条目的碰撞通道** | 判定 |
|:--|:--|:--|:--|
| **index**（Fredholm） | 离散✓ 可加✓ 有向✓ 全局界⚠️ | `E-11`/`E-12`（不定型→惯性→秩→零点计数；rank–trace）**已知只给 extensive 预算**（`E-44` 已封）⟹ 若"有界 index"来自**惯性/迹型**不等式 ⟹ **撞已封路线** ✗ | **条件存活**：须有界性来自**独立源**，非惯性/迹 ✓ |
| **spectral flow** | 离散✓ 可加✓ 有向✓ 全局界⚠️ | `V192`／`C263`／`C264`（**谱实现族**：`\beta` 只经**重数/退化**进入；操作上 β-盲）⟹ 若 flow 由**谱实现族**触发 ⟹ 撞 β-盲/退化计数墙 ✗ | **条件存活**：族 `A_t` 须与谱实现族**不同源** ✓ |
| **winding number** | 离散✓ 可加✓ 有向✓ 界 有时✓ | `A-1` **Guinand 相位锁定**（相位/圈数型工具）⟹ 若用 `\zeta` 自身相位绕数 ⟹ **撞相位锁定** ✗ | **条件存活**：绕数须来自**独立母问题**，非 `\zeta` 相位 ✓ |

```
【⭐ 结构推论（本档新增 ✓✓）】 由 **(C)** 全局上界 ＋ **(E)** 可加不可抵消 ⟹ 该守恒律**不能是局部的**（若局部则可逐点装配出随 `T` 增长的预算 ⟹ 与 (C) 冲突）⟹ 与 `S6` **局域锁定**同向 ✓✓
　但 ⚠️ **守恒律型 ≠ gain 型** ⟹ `KH-5` 的封存（针对 **gain**）**不自动覆盖守恒律型** ✓（与接口拆解 `①` 的判读一致 ✓）
【⛔ 未做】 未制造候选／未启动搜索／未把 `\tau` 定义成 `s\mapsto1-\bar s`／未改任何状态 ✓
```
