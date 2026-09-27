# T5-CHECK-2026-09-27 — T-5 三点 source-first 核验：**原形态 DROP**（$n\le8$ min rank 已被 2025 ELA 收割）；**精化 T-5′（inertia set, $n=7$）＝ HOLD**

**已查地图：命中（本档为既有条目 T-5 的 source-first 核验，非新案）**
所查：`docs/TOPIC-DOSSIER-v1-six-columns-and-relations.md`（**T-5 原定义** ✓）｜`docs/CONCRETE-TOPIC-LIST-r2.md`（T-5 已知/缺口/规模/等级 ✓）｜`docs/TOPIC-INVENTORY-MASTER-v1.md`｜`docs/Zarankiewicz-A3-source-check.md`（**E5 前置问**范例 ✓）
**强制查重门** ✓：`scripts/nogo_gate.py`（本档方向）＋ `scripts/tech_word_check.sh`（五词，见 §7）✓
D0: 本档对象 ＝ **档案已有**条目 T-5（图 min rank／inertia set 小阶完备表）的**三点 source-first 核验与出口判定**（重命名：否 ✗；新对象：无 ✗）
D1: 0（source 抽取 ＋ 出口判定；不主张新自由度 ✓）

> ⛔ **勘误横幅（2026-09-27 21:10）**：本档 §0–§5 的 **HOLD** 判定**已被取代** ⟹ **T-5 ＝ DROP**（**对象级收割**：inertia set 完备阈值实为 $n\le7$（**LAA 436(12), 2012**，逐字：*"This can be used to compute the inertia sets for all graphs on at most seven vertices"*）；min rank／max nullity $n\le8$（2025 ELA））✓ 详见 `docs/ERRATUM-T5-2026-09-27-threshold-6-to-7-and-final-DROP.md` ✓
> 本档**保留**的价值：§2 的 $n\le8$ min rank 逐字证据 ＋ §1 对象指纹钉死 ＋ §3 证书状态问法 ✓

**纪律** ✓：**零计算** ✗｜未写计算脚本 ✗｜未预设 $n=8$ 首攻 ✗｜**门缺口 G-1/G-2/G-3 只登记，不改门** ✓（唐先生 21:08）

---

## §0 判定（先给 · 按唐先生四条件）

$$\boxed{\text{T-5 原形态（}n\le8\ \text{min rank 完备表）}\ =\ \textbf{DROP}\ \text{——已被 2025 ELA 收割}\ ✗}$$
$$\boxed{\text{T-5}^{\prime}\ \text{（inertia set，}n=7\text{）}\ =\ \textbf{HOLD}\ \text{——似仍 open，但差一步家族级查重 ＋ 证书状态核实}\ ⚠️}$$
**要点** ✓：(a) 原定首步（"若 $n=8$ 未完则做 $n=8$ 表"）**已不成立** —— $n\le8$ 的 **min rank 全部完成**（2025）⟹ 该形态**无空间**；(b) 但 **inertia set 侧阈值仅到 $n\le6$**（2010）⟹ $n=7$（**1044 图**）**规模友好**且似**真未决** ⟹ 值得作为**精化候选 T-5′** 继续核（本档**不 ADMIT**，因"真正未决"一条尚未过家族级门 ⚠️）✓

---

## §1 点一｜对象与数量核实（**指纹先钉死** ✓）

**对象（两个，必须分开 ✗ 不可混）**
$$\text{(a)}\ \operatorname{mr}(G)=\min\{\operatorname{rank}A: A\in\mathcal S(G)\}\quad(\mathcal S(G)=\{A\in S_n(\mathbb R): \mathcal G(A)=G\})\ ✓$$
$$\text{(b)}\ \text{inertia set}\ \mathcal I(G)=\{(i_+,i_-,i_0):\exists A\in\mathcal S(G)\ \text{其惯性为该三元组}\}\ ✓\ \text{（**比 (a) 细** ✓）}$$

**三条等价关系／对象混淆（必须显式排除 ✗）** ✓
1. **标号 vs 同构**：$n=8$ 标号图 $2^{\binom 82}=2^{28}=\mathbf{268{,}435{,}456}$ ✗ vs **同构类 12,346** ✓ ⟹ 一律用**同构类** ✓
2. **$\operatorname{mr}$ vs $M$ vs $\mathcal I$**：$\operatorname{mr}(G)+M(G)=n$ ⟹ (a) 与最大零化度 $M$ **等价** ✓；但 **inertia set $\mathcal I$ 严格更细** ✗（同一 $\operatorname{mr}$ 可有不同 $\mathcal I$）⟹ 不可用 $M$ 冒充 $\mathcal I$ ✓
3. **$Z(G)$（零强迫数）是界，不是值** ✗：$M(G)\le Z(G)$，取等**不普遍**（2025 文即专治"不取等"的 8 阶图）✓

**规模表（同构类图数 ✓）**
| $n$ | 6 | 7 | **8** | 9 |
|---|---|---|---|---|
| 图数 | 156 | **1,044** | **12,346** | 274,668 |
⟹ 库存 `~1.2×10^4` ⟹ **确指 $n=8$** ✓（本档**不预设**其为唯一目标 ✓）

---

## §2 点二｜已知完备阶数（**逐字** ✓ · 且区分 existence／enumeration／classification）

**(a) min rank —— 阈值 $\mathbf{n\le8}$（2025 新结果！）** ✓✓
**出处**：Barrett, Hunnell, Hutchens, Sinkovic, *The Classification of Graphs on Eight Vertices with Coinciding Zero Forcing Number and Maximum Nullity*, **ELA**（收 2025-06-12／受 2025-11-13）逐字：
> "In this article, we describe new approaches for this problem on small graphs and **completely determine the minimum rank of all graphs with eight or fewer vertices**." ✓✓✓
> "**Since the minimum rank of all graphs on seven vertices is known**, Proposition 2.5 suggests a technique to determine witnesses…" ✓
> "…although the goal was to determine which eight-vertex graphs satisfy maximum nullity equal to the zero forcing number, it also establishes several additional methods…" ✓
⟹ **$n\le8$ 的 (a) 已完备** ⟹ **T-5 原定首步被收割** ✗

**(b) inertia set —— 阈值 $\mathbf{n\le6}$（2010，未被超越）** ✓
**出处 1**：Jepsen, Lang, McHenry, Nelson, Owens, *Inertia sets for graphs on six or fewer vertices*, **ELA (2010)** 摘要逐字：
> "Because most of the associated theorems require additional hypotheses, **definitive criteria that apply to all graphs cannot be provided**. Nevertheless, these results are strong enough to be able to **determine the inertia set of each graph on 6 or fewer vertices** and can be applied to many graphs with larger order as well." ✓✓
**出处 2**：Fallat–Hogben, *Variants on the minimum rank problem: A survey II* (**arXiv:1102.5142**, 2011) 逐字：
> "**The inverse inertia problem is solved for graphs of order at most 6** in [19]" ✓
**出处 3（技术侧）**：*Using variants of zero forcing to bound the inertia set of a graph*, **ELA 30 (2015)** ⟹ 已有"用零强迫变体**界** inertia set"的工具 ✓（**是界，不等于完备表** ✗）

**⟹ 区分三态（照唐先生要求 ✓）**
| 态 | min rank | inertia set |
|---|---|---|
| **existence**（某惯性可达？） | $n\le8$ ✓ | $n\le6$ ✓（+ 树、cut-vertex 公式） |
| **enumeration**（列出所有可达惯性） | $n\le8$ ✓ | **$n\le6$** ✔；$n\ge7$ ✗ |
| **classification**（结构性充要判据） | 部分（按 $\operatorname{mr}$ 值的图族分类） | **仅 $\operatorname{mr}=2$ 及特别族** ✗⚠️ |
**⚠️ 反面告诫（照唐先生）**："已知构造多" **不得**写成"分类完成" ✗ —— 2010 文自陈**无全图充要判据** ✓

---

## §3 点三｜公开证书状态（⚠️ 本轮**未取到**，如实标注）

| 问 | 本轮读数 | 级别 |
|---|---|---|
| 可下载/可复核的**显式证书**？ | **未找到**公开数据集／证书库 ✗（2025 文述其用**界＋例外分类**，非逐图见证枚举）⚠️ | round-1 ⚠️ |
| 只是"论文声称算完"？ | 2025 文自陈实现细节："…provide the relevant update to the algorithm described therein"（**§7 述其参数工具**）；并明言旧精确算法"**cannot be used to find the minimum rank of all graphs on eight vertices**" ✓ | **逐字** ✓ |
| 独立程序／第二来源？ | **未找到** ✗（2010 inertia 文与 2025 min rank 文为**不同组**，但**标的物不同**，不构成复核 ✗） | round-1 ⚠️ |
| "有人在算"是否被误升级为"已取得"？ | 本档**未**如此升级 ✓；但**须**在下一步以**下载级**证据落实 ⚠️ | — |

---

## §4 ADMIT 四条件逐项（唐先生标准 ✓）

| 条件 | 原形态（$n\le8$ min rank 表） | 精化 T-5′（inertia set，$n=7$） |
|---|---|---|
| ① 未被预登记收割 | ✓（T-5 未被 A3 判除） | ✓ |
| ② **真正未决** | ✗✗ **不满足**（2025 已完备，逐字 ✓） | ⚠️ **似满足但未过家族级门**（阈值 6 ⇒ 7 未决；须再核 2016–2026 是否有完成者） |
| ③ 存在 P1/P2 攻击点 | —（已无目标） | ✓ **候选**：**下界侧**（不可达惯性的证书）＋ 已有"零强迫变体界 inertia set"工具（2015）可作 P1；且 2010 文自陈"无全图充要判据" ⟹ **结构性缺口在分类侧** ✓ |
| ④ 独立 deliverable | —（已被占） | ✓ $n=7$ 的**完整 inertia 表 ＋ 每图双证书**（可达：矩阵见证；不可达：界/结构性论证） |
| **出口** | **DROP** ✗ | **HOLD** ⚠️（差②的家族级核实 ＋ §3 证书状态） |

---

## §5 下一刀（把 HOLD 提升为 ADMIT/DROP 的**唯一**动作，仍不计算 ✓）

**只做一件事**：**家族级字面查重**（AMEND-20 式）——
1. 关键词族（各自独立跑）：`"inertia set"` × {`seven vertices`, `order 7`, `n = 7`}；`"nverse inertia"` × {`7 vertices`, `complete`}；`"inertia table"` graphs；
2. 终点判据：**是否存在 2010 之后的、对 $n=7$（或 $n\ge7$ 全体）给出完备 inertia 表或充要分类的工作** ⟹ 有 ⟹ **DROP**；无 ⟹ ② 过门 ⟹ 进 **P2 机制匹配**；
3. 同轮核 **§3 证书状态**（下载级：作者主页／ELA 附件／GitHub）✓
**红线** ✓：**"存在算法" ≠ "问题已解决"** ✗；**"他人在做" ≠ 判死**（AMEND-22/24）✓；未过②不得设计计算 ✗

**⚠️ 与 T-1 的关键差异（须显式记下 ✓）**：T-1 的风险是"**有主且高产**"（同组下一步）；T-5′ 目前**未发现 owner 在跑 $n=7$ inertia 完备表**（2010 后未见），此点**须在 §5 一并核** ✓

## §6 证据表（含 ID／URL ✓ · 补可复现缺口）

| # | 对象 | 出处 | 关键读数 | 级别 |
|---|---|---|---|---|
| E1 | min rank 完备 $\le8$ | ELA, Barrett–Hunnell–Hutchens–Sinkovic（收 2025-06-12／受 2025-11-13）<br>`journals.uwyo.edu/index.php/ela/article/download/9635/7275/27321` | "**completely determine the minimum rank of all graphs with eight or fewer vertices**" | **逐字** ✓ |
| E2 | inertia set 完备 $\le6$ | ELA (2010) Jepsen–Lang–McHenry–Nelson–Owens<br>`journals.uwyo.edu/index.php/ela/article/view/715` | "determine the inertia set of each graph on 6 or fewer vertices" ＋ "**definitive criteria … cannot be provided**" | **逐字** ✓ |
| E3 | inverse inertia $\le6$ | Fallat–Hogben, Survey II, arXiv:1102.5142 | "**solved for graphs of order at most 6**" | **逐字** ✓ |
| E4 | zero forcing 界 inertia set | ELA 30 (2015) | 有"用零强迫变体**界** inertia set"工具（**界≠表** ⚠️） | 档级 ⚠️ |
| E5 | min rank 早期调查 | Fallat–Hogben survey (2007/2011) | "for all simple graphs on less than seven vertices" | **逐字** ✓ |
| E6 | 图数（OEIS 型） | 标准计数 | $n=6{:}156$；$7{:}1044$；$8{:}12346$；$9{:}274668$ | **档级** ⚠️（可核 OEIS A000088） |

## §7 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "inertia set"
技术词 inertia set      命中文件数=2    :: ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./CONCRETE-TOPIC-LIST-r2.md
$ bash scripts/tech_word_check.sh "minimum rank"
技术词 minimum rank     命中文件数=3    :: ./TOPIC-DOSSIER-v1… ./S2-BATCH-4-record-and-pool-reconciliation.md ./CONCRETE-TOPIC-LIST-r2.md
$ bash scripts/tech_word_check.sh "零强迫"
技术词 零强迫        命中文件数=1    :: ./TOPIC-DOSSIER-v1-six-columns-and-relations.md
$ bash scripts/tech_word_check.sh "balanced inertia"
技术词 balanced inertia 命中文件数=0    ::
$ bash scripts/tech_word_check.sh "图数"
技术词 图数           命中文件数=6    :: ./TOPIC-DOSSIER-v1… ./IP-5-RUN-dminus3-bounded-search-result.md ./ASSETS-REGISTRY.md
```
- **本档新增**：**0** 个术语 ✓（`balanced inertia` 命中 0 档 ⟹ 为**外部文献术语**（ELA 2010 摘要），**引用**，**不作新性主张** ✓；`T-5′` 仅为**库存条目的精化标记** ✓）
- **档案已有（引用，不列为提出）**：`inertia set`（2 档）｜`minimum rank`（3 档）｜`零强迫`（1 档）｜`图数`（6 档）✓
- **通用词（不计）**：`证书`／`表`／`阈值` ✓

## §8 诚实边界

- 本档为 **round-1 source 快照**：§3（证书状态）与 §5-②（家族级查重）**未完成** ⚠️ ⟹ **不得**据此写"T-5′ 已判 open" ✗
- 图数（E6）为**档级**，须以 OEIS 核 ⚠️；E4 为档级 ⚠️
- **未动算** ✓；不改门（G-1/G-2/G-3 **只登记**）✓；不写"方向已死／不存在" ✗（V290）——只写"该形态**已被收割**／该精化形态**待核**" ✓
