# ERRATUM-T5-2026-09-27 — 阈值 **6 → 7** 修正 ＋ **T-5 最终 DROP** 记录

**已查地图：命中（本档为既有条目 T-5 的勘误与终局记录，非新案）**
所查：`docs/T5-CHECK-2026-09-27-three-point-source-verification-n8-harvested-inertia-n7-HOLD.md`（**本档所勘之档** ✓）｜`docs/TOPIC-DOSSIER-v1-six-columns-and-relations.md`（T-5 原定义）｜`docs/CONCRETE-TOPIC-LIST-r2.md`（**"阈值须核"标记处** ✓）｜`docs/ASSETS-REGISTRY.md`｜`docs/RESEARCH-CONSTITUTION.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词，见 §6）✓
D0: 本档对象 ＝ **档案已有**条目 T-5（图 min rank／inertia set 小阶完备表）的**阈值勘误与终局出口**（重命名：否 ✗；新对象：无 ✗）
D1: 0（source 抽取 ＋ 勘误 ＋ 出口；不主张新自由度 ✓）

**纪律** ✓：**零计算** ✗｜未写计算脚本 ✗｜**门缺口 G-1/G-2/G-3 只登记、不改门** ✓｜未预设 $n=8$ 首推 ✗

---

## §0 勘误与终局（先给）

$$\boxed{\textbf{勘误}：\ \text{inertia sets 完备阈值}＝\mathbf{n\le7}\ (\text{2012})\ \text{——}\textbf{不是}\ n\le6\ (\text{库存为旧指纹})\ ✗✓}$$
$$\boxed{\textbf{T-5 ＝ DROP}：\text{三个分支均为\textbf{对象级收割}}（\text{非预登记撞车、非同形赛跑}）\ ✗}$$

**最终 DROP 记录（唐先生 2026-09-27 21:10 定稿 · 逐字 · 供后续轮次直接引用）** ✓
> **T-5 / graph inertia-set small-order classification — DROPPED: complete through $n=7$ (2012); min-rank/max-nullity through $n=8$ (2025). Do not treat $n=8$ absence of a table as evidence of openness.**

---

## §1 逐字证据（**一手源** ✓✓ · 本轮补取，替代二手结论）

**源**：Wayne Barrett, Steve Butler, H. Tracy Hall, John Sinkovic, Wasin So, Colin Starr, Amy Yielding, *Computing inertia sets using atoms*, **Linear Algebra and its Applications 436(12) (15 June 2012), 4489–4502**；DOI **10.1016/j.laa.2011.08.026**（Special Issue on Matrices Described by Patterns）✓

**摘要逐字（全文）** ✓✓
> "We consider the problem of computing inertia sets for graphs. By using tools for combining the inertia sets of smaller graphs we can reduce this problem to understanding the inertia sets for three-connected graphs that are not joins. We term such graphs **atoms** and give the inertia sets **for all atoms on at most seven vertices**. **This can be used to compute the inertia sets for all graphs on at most seven vertices.**" ✓✓✓

**⟹ 两条关键读数** ✓
1. **完备阈值 ＝ $n\le7$**（"all graphs on at most seven vertices"）—— **非** $n\le6$ ✗✓
2. **机制已给出**：**atoms（3-connected 且非 join）＋ 组合工具（reduction）** ⟹ 这正是库存所谓"reduction/结构结果"的来源 ✓

**⚠️ 注意 $\operatorname{mr}$ 与 $\mathcal I$ 不可互推（照唐先生 ✓）**
$$\operatorname{mr}(G)=\min_{(p,q)\in\mathcal I(G)}(p+q)\ \Longrightarrow\ \operatorname{mr}\ \text{是}\ \mathcal I\ \text{的\textbf{投影}} \Rightarrow \text{知 mr 与 }M\ \textbf{不能}反推\ \mathcal I\ ✓$$
（呼应：2025 ELA 只做 **min rank／max nullity**（粗不变量），**不**收割 $\mathcal I(G)$ 的 $n=8$ ✓）

---

## §2 修正前后对照（**库存 vs 一手源** ✓）

| 量 | 库存（旧） | **一手源（新）** | 差 |
|---|---|---|---|
| min rank 完备阈值 | "对阶数不超过某值已解决（**阈值须核**）" ⚠️ | **$n\le8$**（ELA，收 2025-06-12／受 2025-11-13 ✓） | **库存欠 1 阶且未定** |
| inertia set 完备阈值 | **$n\le6$**（ELA 2010 ✓，**但非最佳**） | **$n\le7$**（LAA 436(12), **2012** ✓✓） | **差 1 阶**（差 **14 年**的文献 ✗） |
| inverse inertia 结构刻画 | "$n\le6$ 已解决"（Survey II 2011 ✓） | 同上 ＋ atoms 机制（2012 ✓） | 2012 后已推进 |

**⟹ 教训（本档最有价值产出 ✓✓）**：库存的"阈值 $6$"来自 **2010 ELA 文**（该文**自称**做到 6 阶）；**未追其后继**（2012 LAA 用 atoms 推到 7 阶）⟹ 阈值类事实**必须追引用链** ✓（下轮写入流程：**"阈值必查后继文献"** ⚠️）

---

## §3 T-5 四支终局表（照唐先生 ✓）

| 分支 | 状态 | 原因（依据） |
|---|---|---|
| min rank $n\le8$ | **DROP** | 2025 ELA 完成 ✓（逐字：*"completely determine the minimum rank of all graphs with eight or fewer vertices"*） |
| maximum nullity $n\le8$ | **DROP** | 与 min rank **对偶**（$\operatorname{mr}+M=n$）⟹ 同被完成 ✓ |
| **inertia set $n\le7$** | **DROP** | **2012 LAA** 完成 ✓（逐字：*"all graphs on at most seven vertices"*） |
| inertia set $n=8$ | **不判 open** ⚠️ | 2012 文只称"**can be applied to many graphs** with larger order"（**未**称全体 8 阶完成）；**但"未见表" ≠ "open"** ⟹ **不得**立为目标 ✗ |
| inverse inertia 结构刻画 | **不直接作新目标** ✗ | 已有 atoms／join／cut-vertex／tree 等**成套 reduction 结构结果** ✓ |

**⟹ 出口：T-5 ＝ DROP，不进入 P1/P2** ✓（**比 T-1 更干净**：T-1 是**预登记撞车**，T-5 是**对象指纹本身已被 2012 文献收割** ✓）

---

## §4 纪律性收获（**G-2 型风险的正确用法** ✓）

$$\boxed{\text{"我没找到 }n=8\ \text{完备表"}\ \neq\ \text{"}n=8\ \text{inertia 分类是 open target"}}$$
- 本档 §3 末两行即该风险的**当场应用** ✓：**新目标须以"正面证据"（作者自述 open／明确未做）立**，**不得**以"检索缺口"立 ⚠️
- 与 `T-1` 对照：T-1 的 open 是**作者自述**（"remains open"）✓ ⟹ 可用；T-5 的 $n=8$ 是**我方检索缺口** ⟹ 不可用 ✗
- **登记为流程条款建议**（**不改门** ✓，仅登记）：**G-4｜"阈值/缺口类事实须追后继引用链；目标 open 须有正面证据"** ⚠️

---

## §5 已做的库存更正（逐条 ✓）

| 文件 | 更正 | 状态 |
|---|---|---|
| `docs/T5-CHECK-2026-09-27-…-HOLD.md` | 加**勘误横幅**（§0 的 HOLD 判定被本档取代） | ✓ 本档同提交 |
| `docs/ASSETS-REGISTRY.md` | 新增 **C-385**（含 §0 的 DROP 记录逐字） | ✓ |
| `docs/TOPIC-DOSSIER-v1-…md` | T-5 标题下加**一行 DROP 标记**指向本档 | ✓ |
| `docs/CONCRETE-TOPIC-LIST-r2.md` | T-5 状态行加 DROP 标记指向本档 | ✓ |

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "atoms"
技术词 atoms           命中文件数=7    :: ./C3825-four-moment-joint-geometry-audit.md ./RESEARCH-CONSTITUTION.md ./C3823-four-atomic-joint-moment-geometry-audit.md
$ bash scripts/tech_word_check.sh "阈值"
技术词 阈值            命中文件数=287  :: ./EXPERIMENT-filter-misfire-audit-1.md ./W4-1e-blind-readout-growth-coordinate-NOT-resolvable.md ...
$ bash scripts/tech_word_check.sh "3-connected"
技术词 3-connected     命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`atoms`（7 档）／`阈值`（287 档）为**档案已有**；`3-connected` 命中 0 ⟹ 为**外部文献术语**（LAA 2012 摘要），**引用**，**不作新性主张** ✓）
- **本档新增条款（非技术词）**：**G-4**（阈值类事实须追后继引用链；open 须正面证据）—— **登记性建议，不改门** ✓

## §7 诚实边界

- 本档**只做勘误＋出口**，**无新计算、无新对象** ✓；不改门（G-1…G-4 **只登记**）✓
- `n=8` inertia **状态如实标注为"不判 open"**（既不声称已收割、也不声称 open）✓
- 不写"方向已死／不存在" ✗（V290）：T-5 的表述是"**该对象在小阶已被收割，故不作为目标**" ✓
