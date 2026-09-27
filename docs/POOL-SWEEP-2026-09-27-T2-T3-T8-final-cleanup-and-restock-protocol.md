# POOL-SWEEP-2026-09-27 — T-2／T-3／T-8 终扫 ⟹ **旧池耗尽** ＋ **重新进货协议**

**已查地图：命中（本档为池级终扫与前序四档的收口，非新案）**
所查：`docs/T1-CHECK-2026-09-27-…`｜`docs/ERRATUM-T5-2026-09-27-…`｜`docs/T6-CHECK-2026-09-27-…`｜`docs/T7-CHECK-2026-09-27-…`｜`docs/T4-CHECK-2026-09-27-…`｜`docs/M1-FAMILY-CLOSURE-2026-09-27-…`｜`docs/TOPIC-DOSSIER-v1-six-columns-and-relations.md`｜`docs/CONCRETE-TOPIC-LIST-r2.md`｜`docs/ASSET-PROBLEM-REVERSE-AUDIT-table.md`（AV＝N×L×G）｜`docs/CAPABILITY-FIRST-PROBLEM-SELECTION.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §6）
D0: 本档对象 ＝ **档案已有**池内九条目（T-1…T-9）的**终扫判定**与**进货协议**（重命名：否 ✗；新对象：无 ✗）
D1: 0（清扫／出口／协议；不主张新自由度 ✓）

**纪律** ✓：**零计算** ✗（唐先生 21:24 明确）｜**G-1…G-4 只登记、不改门** ✓

---

## §0 三格终扫（**P0／P0.5 only** ✓）

| 格 | 精确目标 | 当前最佳／最新 | 出口 | 依据 |
|---|---|---|---|---|
| **T-2** | $\mathrm{cap}(AG(7,3))$ ＝ $AG(7,3)$ 最大 cap 尺寸 | $AG(6,3)=112$ 且**仿射等价唯一**（Potechin）；上界 $2.756^n$（Ellenberg–Gijswijt）；新下界 $2.218^n$（`arXiv:2209.10045`）；$n\ge7$ **大小未知**（档内逐字） | **DROP** ✗ | ①**资产匹配弱**（目标＝**全局极值/堆积型**；我方 rank／inertia／局部重叠几何**无接口**；档内自评"攻击点弱"）②生态**持续收割**（Edel 构造＋表、E–G 上界、2022 新下界）③$3^7=2187$ 点、上下界**差距大** ⟹ 属"**改进界**"的 dent 型，非可用入口 ✗ |
| **T-3** | $t(n)$ ＝ $AG(n,3)$ **最小 complete cap** | **正面证据 ✓✓**：Bishnoi 博客（**2026-03-10**）逐字——"Recently, **Cassie Grace and Felipe Voloch**（`arXiv:2602.05254v1`）found an elegant algebraic construction of size $O(3^{n/2})$, **thus solving the problem**" ✓✓ | **DROP** ✗（**有正面来源** ✓ 满足 G-4） | 该问题（$t(n)$ 上界的阶）**已被解决** ⟹ 不构成 open 目标 ✓ |
| **T-8** | $\pm$-rank of $(0,\pm1)$-matrices（**缺口未锁定**） | ILAS **2026** 报告（`indico.math.vt.edu/event/2/contributions/351/`）逐字："…rank of a $(0,\pm1)$-matrix. This 'generalizes' the binary rank and the term rank of $(0,1)$-matrices. **We establish several inequalities** relating the different ranks…" ⚠️ | **HOLD** ⚠️ | **未锁定对象/参数，且无正面 open claim** ⟹ 依唐先生规则（**做不到就 DROP/HOLD，不进 P1/P2**）⟹ **HOLD**，复活条件＝把缺口写成**精确对象＋参数＋正面 open 证据** ✓ |

**⚠️ T-3 的方法论要点（照唐先生 ✓）**：此格**不是**靠"我没找到 open claim"判 DROP ✗，而是靠**找到正面解决来源**判 DROP ✓✓（G-4 的正确用法）✓

---

## §1 旧池耗尽判定 ✓

| # | 条目 | 状态 | 依据档 |
|---|---|---|---|
| T-1 | $z_L(5,5)$ | **DROP** | 预登记 ＋ 赛跑 |
| T-2 | $AG(7,3)$ 最大 cap | **DROP** | 本档 §0 |
| T-3 | 最小 complete cap | **DROP** | 本档 §0（**正面证据**） |
| T-4 | SNIEP $n=5$ | **DROP** | M03 线（机制成功／新性失败） |
| T-5 | 图 inertia 小阶表 | **DROP** | 对象级收割（2012／2025） |
| T-6 | $K_q(n,R)$ 格子 | **DROP** | 工业化赛跑 |
| T-7 | $\ell_1(2,q)$ | **DROP** | 资产隔离失败 |
| T-8 | $\pm$-rank | **HOLD** | 缺口未锁定 |
| T-9 | Zarankiewicz frontier | **REJECT** | 他方机制更强 |
$$\Longrightarrow\ \boxed{\textbf{旧池耗尽（8 DROP ＋ 1 HOLD ＋ 1 REJECT）}}\ \text{—— 无可用入口}\ ✓$$

---

## §2 重新进货协议（把 M1／D-A／D-B／G-4 变成**生成器** ✓）

**① 黑名单（M1 CLOSED ✓）**：covering codes｜domination｜saturating sets｜syndrome-covering｜**及一切经 parity-check functional 等价的变体** ⟹ 除**新资产**外不再进池 ✗

**② 生成顺序（**问题先行** ✓ 严禁反向）**
$$\text{frontier open problem}\Rightarrow\text{object fingerprint}\Rightarrow\text{asset match}\Rightarrow P1/P2\ ✓$$
**明确禁止** ✗：$\text{手里有资产}\Rightarrow\text{到处找相似问题}$（＝`CAPABILITY-FIRST-PROBLEM-SELECTION` 的失败形态 ✓）

**③ 四问闸（每候选必答，任一否决即不入池 ✓）**
| # | 问 | 否决条件 |
|---|---|---|
| Q1 | 目标是**全局极值/覆盖型**吗？ | 是且涉覆盖 ⟹ 大概率撞 **M1** ✗ |
| Q2 | **证书逻辑**与 $K(10,1)$ 是同一 functional 吗？ | 是 ⟹ **资产隔离失败** ✗（D-B） |
| Q3 | 有**正面 open 证据**吗（作者自述 open／明确未做／未收口）？ | 仅"未见表／库写 unknown" ⟹ **不可用** ✗（D-A／G-4） |
| Q4 | 现有资产能产生**新约束**吗（非旧约束换参数/换表示）？ | 否 ⟹ 映射层关闭 ✗ |

**④ 目标生态（M1 之外 ✓）**：rank／spectral｜finite geometry（**非覆盖型**⚠️ 慎用，多为覆盖/饱和）｜extremal graph（**堆积/Turán 型**）｜additive／combinatorial invariant｜certificate-driven classification ✓

---

## §3 首批扫描清单（**提案 ⚠️ · round-1 标题级 · 下轮做 P0/P0.5** ✓）

| # | 生态 | 具体 frontier 项（**均有本轮实际检索证据** ✓） | 与资产的关系 | Q1–Q4 初判 |
|---|---|---|---|---|
| B1 | rank／spectral | **unicyclic／bicyclic 图的 inertia**（DMGAA 论文；族分类型）✓ | 直接对口（inertia） | Q4 待核（家族分类可能已被覆盖）⚠️ |
| B2 | rank／spectral | **树的 inverse eigenvalue（重数表／generalized stars）**（LAA／arXiv 族群）✓ | 直接对口（重数＝零化度） | Q1 否 ✓；Q4 待核 ⚠️ |
| B3 | rank／spectral | **spectral arbitrariness for trees fails spectacularly**（JCTA 2024）✓ | 谱约束 ↔ rank/inertia | Q1 否 ✓；Q3 待核 ⚠️ |
| B4 | extremal（**堆积型**） | **Turán $(r+1,r)$-systems 最小规模**（2026-08-25 改进界）✓ | 堆积＋局部交约束 | Q1 否 ✓；Q3 **正面证据有**（持续改进＝未封闭）⚠️ 但拥挤 |
| B5 | matrix analysis（**新对象**） | **$\pm$-rank 及各类 rank 的不等式族**（ILAS 2026 首次引入）⚠️ | rank 工具直接对口 | Q3 **无正面 open claim** ⟹ **HOLD**（与 T-8 同源）⚠️ |
**⚠️ 边界** ✓：以上**均为待扫提案**，**非 ADMIT**；下轮**必须**逐项走 P0→P0.5→P0.75→P1/P2→单一出口，**不预设 ADMIT** ✓

---

## §4 本轮沉淀的研究资产（**比单个 $K(10,1)$ 结果更重要 ✓**）

$$\boxed{\text{一个看似很大的"有限组合数学 open-problem 池"，若无【对象指纹＋后继链＋资产隔离】，会系统性产生\textbf{假开放问题}}}$$
- 五连 DROP ＋ T-4 ＋ **M1 族级关闭** ⟹ 支撑**搜索规则升级**（本档 §2 协议）✓
- 三条已固化纪律：**D-A**（形式 open ≠ 可用入口）｜**D-B**（换表示 ≠ 换问题）｜**G-4**（阈值/缺口须追后继链；open 须正面证据）✓

## §5 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "cap set"
技术词 cap set          命中文件数=6    :: ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./CAPMIX1A-I-vs-truth-sound-but-incomplete.md ./ASTRA-TYPE-OPEN-PROBLEM-TABLE.md
$ bash scripts/tech_word_check.sh "±-rank"
技术词 ±-rank          命中文件数=0    ::
$ bash scripts/tech_word_check.sh "sign rank"
技术词 sign rank        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "problem-first"
技术词 problem-first    命中文件数=4    :: ./ASSET-PROBLEM-REVERSE-AUDIT-table.md ./CAPABILITY-FIRST-PROBLEM-SELECTION.md ./S13-EXECUTION-TEST-FAIL.md
$ bash scripts/tech_word_check.sh "进货"
技术词 进货            命中文件数=0    ::
$ bash scripts/tech_word_check.sh "旧池耗尽"
技术词 旧池耗尽        命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`进货`／`旧池耗尽` 为**唐先生本轮用语／本档标签**；`±-rank`／`sign rank` 为**外部对象名** ⟹ 均**引用**，**不作新性主张** ✓）
- **档案已有（引用，不列为提出）**：`cap set`（6）｜`problem-first`（4）✓

## §6 诚实边界

- 本档为**池级清扫＋协议**；三格均**只做 P0/P0.5**（**未**跑 closure_gate；**未**动算）✓
- **T-8 ＝ HOLD 而非 DROP**（缺口未锁定，不得伪装成结论）✓；**T-3 ＝ DROP 靠正面证据**（非检索缺口）✓
- 不写"某方向已死／不存在" ✗（V290）；§3 清单为**提案**，非候选 ✓
