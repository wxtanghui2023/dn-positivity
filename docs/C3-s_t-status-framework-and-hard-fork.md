已查地图：命中（`C3-premise-confirmed-by-handbook`／`C3-concretized-36s-63t-family`／`C3-check-premise-conflict`）⟹ 引用，不开新案
D0: 本档对象 = `C3` **`(s,t)` 状态分框架** ＋ **硬分叉判据** ＋ 自对偶有限情形穷尽事实 ＋ 竞争风险
D1: 0 （[REVIEW] 轮次：定界与框架，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`C3`：`(s,t)` 状态框架与硬分叉**

## §1 ⭐ 三项升格（一手 `Chapter 11` 摘要，照录）

```
**(i)** `\{6,3,p\}`（`p=3,4,5,6`）：**enumeration complete** ✓；**`\{3,6,3\}`：仅 substantial partial results** ⟹ $$\boxed{\{3,6,3\}\ \text{是唯一剩余的 rank-4 主族}}$$ ✓✓
**(ii)** 适用情形下：**universal polytope 有限 `\iff` 对应 complex Hermitian form 正定** $$\boxed{P\ \text{finite}\iff H_P>0}$$ ✓✓ —— **是作者实际采用的 enumeration 机制，非我方脑补** ✓
**(iii)** 有限 polytope 的自同构群 ＝ **有限 unitary reflection group `\rtimes` 一个小有限群** ✓
```

## §2 ⚠️ 关键新风险（照录）

```
**不能把"族未分类"直接等同于"存在小的未决 `(s,t)`"** ✓✓
【自对偶子族已被穷尽】**`\{\{3,6\}_s,\{6,3\}_s\}` 的已知有限 universal 情形仅 `s=(1,1),(2,0),(3,0)`**（引用 `Table 11E1`）✓
　群数据：`s=(1,1)`：`(|D^+|,|C|,|G|)=(108,18,18)`；`s=(2,0)`：`(240,120,40)`；`s=(3,0)`：`(2916,486,486)` ✓
　**逐字**："universal regular 4-polytope `\{\{3,6\}_s,\{6,3\}_s\}` **known to be finite only when** `s=(1,1),(2,0),(3,0)`" ✓✓
【⟹ 真正的未决问题缩窄为】 $$\boxed{\text{非自对偶 }(s,t)\text{ 中，哪些尚未被已有分类机制决定？}}$$ ✓✓
```

## §3 ⭐ 四类状态表（下一刀要填）

```
参数：`s\in\{(a,0),(a,a)\}`、`t\in\{(b,0),(b,b)\}`；四列：$$\bigl((s,t)\ \big|\ \text{status}\ \big|\ \text{mechanism}\ \big|\ \text{certificate size}\bigr)$$ ✓
**【A】已由 `11E` 明确决定** —— 如 `((1,1),(1,1))`、`((2,0),(2,0))`、`((3,0),(3,0))` ⟹ **不得再碰** ✓
**【B】已由 `11D`/`11E`/`11H` 关系归约** —— duality、cut、hyperbolic honeycomb relationship 导致的**参数等价** ⟹ **非独立问题** ✓
**【C】已被 modular-linear-group 构造覆盖** —— `Monson–Schulte 2010` 对 spherical/Euclidean 型给出完整描述并产生大量 locally toroidal polytopes ⟹ **不得作新问题** ✓
**【D】真正未决** —— 必须同时满足：$$\boxed{\text{未被 }11E/11H\text{ 决定}\ \land\ \text{不是已有 modular construction}\ \land\ \text{universal finite/infinite 未知}}$$ ✓✓ **只有 D 是候选** ✓
```

## §4 ⭐ 压缩理想与硬分叉

```
【若最小未决 `(s,t)` 落入 Hermitian 机制覆盖区】**分类链极短**：$$\text{polytope classification}\to H(s,t)>0\to\det H,\ \text{principal minors}\to\text{exact finite/infinite decision}$$ ✓✓
　⟹ **若矩阵维数固定、参数仅进入少数整数/代数整数项** ⟹ **`N_{\rm eff}\sim O(1)`**，**甚至无需搜索** ✓✓ —— **这正是我们要找的 `H`-型压缩** ✓
【⚠️ 竞争风险（照录）】 `C3` 最大风险**不是计算量**，而是 $$\boxed{\text{我们可能只是重跑 }McMullen–Schulte\text{ 已完成的 Hermitian enumeration}}$$ ⟹ 若最小未决 `(s,t)` 的 `H(s,t)` **已在 `Chapter 9`/`11E` 被判定** ⟹ 重算只得 **verification，不是 `G4`** ✓✓
【⟹ 硬分叉（本轮核心输出）】 $$\boxed{\exists\,(s_*,t_*)\ \text{既未被 }11E/11H\text{ 决定，又确实落在可压缩 Hermitian 判定机制}\ \begin{cases}\textbf{之内}\ \Rightarrow\ C3\ \text{进入 }G3\\\textbf{之外}\ \Rightarrow\ C3\ \text{退出}\end{cases}}$$ ✓✓✓
```

## §5 状态表与下一步

```
$$\begin{array}{c|c}\text{未闭合族存在}&\checkmark\\\{3,6,3\}\ \text{为 partial}&\checkmark\\\text{Hermitian mechanism}&\checkmark\\\text{有限性}\iff H>0&\checkmark\ (\text{适用情形})\\(s,t)\ \text{完整表}&\textbf{OPEN}\\\text{最小未决 }(s,t)&\textbf{OPEN}\\\text{显式 }H(s,t)&\textbf{OPEN}\\N_{\rm eff}&\textbf{OPEN}\\\text{C2 concrete instance}&\textbf{OPEN}\end{array}$$ ✓
【`C3` 下一刀】 `§11E`＋`§11H` ⟹ **填 `(s,t)` 完整状态表** ⟹ 取**最小真正未决** ⟹ **写出显式 Hermitian 矩阵**（不得只写"由 Hermitian form 控制"）⟹ **再**算 `N_{\rm eff}` ✓
【`C2` 第二轨（只需两项，不做搜索）】 `(r,n,q)` ＋ **为何已知理论未决定它** ✓
【⛔ 纪律】**绝对不进入计算**；`n=38`／`TARGET-L9`／RH 未作筛选依据 ✓
【边界】 §1–§2 为**逐字级摘要**（`Cambridge` Ch.11 摘要、`Table 11E1` 转引、`Monson–Schulte 2010`）；**未读 `§11E`/`§11H` 正文**；§3–§5 为**本档框架与判据**；未制造候选／未启动搜索／未碰 RH。
