# T7-CHECK-2026-09-27 — T-7（$PG(2,q)$ 的 minimal 1-saturating sets）⟹ **DROP**

**已查地图：命中（本档为既有条目 T-7 的严格筛选，非新案）**
所查：`docs/TOPIC-DOSSIER-v1-six-columns-and-relations.md`（**T-7 原定义** ✓）｜`docs/CONCRETE-TOPIC-LIST-r2.md`（T-7 已知/缺口/等级 ✓）｜`docs/T6-CHECK-2026-09-27-…DROP.md`（**上一格** ✓）｜`docs/BFREEZE-2026-09-27-…md`（T1–T5 ✓）｜`docs/ASSETS-REGISTRY.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §8）
D0: 本档对象 ＝ **档案已有**条目 T-7（$PG(2,q)$ minimal 1-saturating sets）的**指纹／后继链／同形赛跑／资产隔离与出口判定**（重命名：否 ✗；新对象：无 ✗）
D1: 0（source 抽取 ＋ 出口判定；不主张新自由度 ✓）

**纪律** ✓：**零计算** ✗｜未写计算脚本 ✗｜**G-1…G-4 只登记、不改门** ✓

---

## §0 单一出口：**DROP**（四条独立依据 ✓ · 不预设 ADMIT）

$$\boxed{\textbf{T-7 ＝ DROP}}$$
1. **资产隔离检查：失败** ✗（唐先生 21:15 专门要求）—— 目标量 $\ell_1(2,q)$ 与 $K_q(n,1)$ 是**同一覆盖逻辑**（经典 parity-check／syndrome 桥），**只是换了表示**（射影平面 ↔ Hamming 空间）；库存**自己**就写着 T-7"与 T-6 **同机制**（syndrome 覆盖 ↔ saturating）" ⟹ **直接 DROP，不许进入计算** ✓
2. **同形赛跑：撞上** ✗ —— 同参数、同构造族、**同作者群／同血统**（Pambianco｜Bartoli｜Marcugini｜Davydov｜Faina｜Nagy），且该族**持续产出到 2026** ⚠️
3. **P1/P2 novelty gate：答不出** ✗ —— T1–T5 均为**局部修复账本**（特定码／$E$-专有耦合／有限证书），对"**全局最小尺寸**"$\ell_1(2,q)$ 不产生新约束；强行做即"**旧约束换参数／换表示**" ⟹ 依唐先生判词 DROP ✗
4. **库存"前沿"过时** ⚠️ —— 库存写"$q\le16$ 有表"；实际**分类已到 $q\le23$**（2012/2013）＋构造上界表延至**大 $q$** ⟹ 又一处**阈值漂移**（同 T-5 的 $6\to7$）⟹ 强化 **G-4** ✓

---

## §1 P0｜对象指纹

$$\ell_1(2,q)\ (\text{亦记 } s_\mu(2,q))\ =\ \min\{|S|:S\subseteq PG(2,q)\ \text{为 1-saturating}\}\ ✓$$
- **定义**：$S$ 使平面上**每一点**都落在 $S$ 的**一条割线**（2-secant）上或属于 $S$ 自身 ✓
- **等价／桥接**：**1-saturating set in $PG(n-1,q)$ ↔ $q$ 元覆盖码（半径 1）** ⟹ 与 $K_q(n,1)$ **同一 functional** ✓⚠️（库存已录此桥 ✓）
- **不可混**（显式排除 ✗）：① $k$-saturating（$k\ge2$）；② **complete arc**（同类但**不同对象**：无 3 点共线且极大）⚠️ 常被并论但须分账；③ 高维 $PG(n,q),n\ge3$ ✗
- **原始 open claim**：小 $q$ 精确值 + 大 $q$ 界（库存"档级"）；**本轮升级为逐字**（见 §2）

---

## §2 P0.5｜后继引用链（追到 2026 ✓ · 逐字）

| 环节 | 内容 | 出处 |
|---|---|---|
| 小 $q$ 表 | *Minimal 1-saturating sets in PG(2,q)*, Pambianco 等（2003, Australas. J. Combin. 28:161–169）— 表基座 ✓ | 引文逐字 ✓ |
| **分类**（关键） | **"Classification of the smallest minimal 1-saturating sets in PG(2,q), $q\le23$"**（Bartoli–Marcugini–Milani–Pambianco, ACCT 2012）✓✓；且 **"the minimal 1-saturating sets of the smallest size in PG(2,q) are classified for $16\le q\le23$"**（Bartoli–Davydov–Faina–Marcugini–Pambianco, *J. Geometry* 2013）✓✓ | 逐字 ✓ |
| 上界线（持续） | *Upper bounds on the smallest size of a saturating set in projective planes*（arXiv:1702.07939）｜*On upper bounds …*（arXiv:1505.01426）｜Nagy 渐近 $\lvert S\rvert\le(1+o(1))\sqrt{(n+1)q^{n-1}\ln q}$ ✓ | 逐字 ✓ |
| 表外延 | 同族表的构造搜索延至 **$q\le430007$ 级**（complete arcs／lexiarcs 线，共享同一算法族）⚠️ | 逐字 ✓ |
| **2026 仍在跑** | **arXiv:2606.16669**（2026）*A geometric approach to generalized covering radii of linear codes* ✓⚠️；且 **arXiv:1808.09301** 把 *covering codes of radius R* 与 *saturating sets in projective spaces* **同篇并处理** ✓ | 逐字 ✓ |
**⟹ 后继链读数**：该格**不是停滞格**——**分类已到 $q\le23$**，上界线**连续产出**，且**2026 年仍有新文** ⟹ 与 T-6 同型（**工业化的覆盖证书线**）⚠️

---

## §3 P0.75｜同形赛跑（逐项 ✗）

| 维度 | 判定 | 依据 |
|---|---|---|
| same parameter | **撞上** ✗ | 同一 $\ell_1(2,q)$ |
| same equivalence | **撞上** ✗ | 同为"最小尺寸／上下界是否重合" |
| same family | **撞上** ✗ | 割线覆盖构造（与覆盖码 direct sum／syndrome 线同族） |
| same author／lineage | **撞上** ✗ | **Pambianco｜Bartoli｜Marcugini｜Davydov｜Faina｜Nagy**（与 T-6 的 Kéri／Marosi 线**交叉同一社区**）✓ |
**⟹ 依规则：任一撞上即 DROP／HOLD，不进入计算** ✓

---

## §4 P1/P2｜新攻击点（**答不出** ⟹ DROP）+ 资产隔离检查（**失败** ✗）

**唐先生要求回答**：它的目标量是否**真的不同于** $K(10,1)$ 的**全局极小性**问题？

$$\boxed{\textbf{答：不同不了}\ ✗\ \text{——只是把 Hamming 空间的覆盖证书逻辑，换成射影平面的割线覆盖证书逻辑}}$$
- **桥接是经典的**（parity-check／syndrome）⟹ $\ell_1(2,q)$ 与 $K_q(n,1)$ **同一 functional**，**同一证书逻辑** ✓⚠️
- **T1–T5 逐项核（诚实 ✓）**
| 资产 | 对 $\ell_1(2,q)$ | 理由 |
|---|---|---|
| T1 top-4 容量恒等式 | ✗ | 关于"**删 4 个码字**后"的局部捕获账本；与"全局最小"无关 |
| T2／T4 | ✗ | $E$-专有尺寸耦合，绑定那个 124 词码 |
| T5 STAR/TRI | ✗（仅局部） | 给局部重叠计数，**不**给全局下界 |
| L3-α certificate | ✗ | 单码有限证书；换参数即"**重跑同类证书**"（禁止形态 ✗） |
⟹ **新约束：无** ⟹ 依唐先生判词 **DROP** ✓

---

## §5 P3｜deliverable（**无法预先说清** ⟹ 与 DROP 一致 ✓）

- 若强行立项，最可能的产物是"**某 $q$ 的 $\ell_1(2,q)$ 上界改进**"或"**小 $q$ 重算/形式化**" ⟹ **两者都被唐先生明确排除**（"把已有结果重新计算/形式化不算"）✗
- **不足以**承诺：新普适下界／排除参数区间／新显式构造／新分类定理 ✓

---

## §6 池级读数（**本轮真正的产出** ⚠️ 供唐先生决策）

**四连 DROP 的三类死因**（T-1／T-5／T-6／T-7）
| 条目 | 死因 |
|---|---|
| T-1 $z_L(5,5)$ | **预登记撞车** ＋ 同形赛跑（owner 活跃） |
| T-5 图 inertia 小阶表 | **对象级收割**（2012／2025）＋ **阈值漂移**（$6\to7$） |
| T-6 $K_q(n,R)$ 格子 | **同形赛跑全面** ＋ gate 答不出 ＋ **证书链工业化** |
| T-7 $\ell_1(2,q)$ | **资产隔离失败**（同一覆盖逻辑换表示）＋ 同族 ＋ **阈值漂移**（$16\to23$） |
**⟹ 结构性观察** ✓：池内"**表填空族（M1）**"的四个格子**全部**落在"覆盖／支配／饱和"这一**同一技术生态**，且该生态**已被工业化**（显式证书＋checker＋ancillary files＋形式化）⟹ **继续按池内顺序单格扫，预期收益低** ⚠️
**建议（非决定 ✓）**：下一刀可选 **(a)** 对 M1 族做**一次性族级判决**（写"该族对我方资产不可用"的族级结论，含四例证据）；或 **(b)** 转向池内**非同族**余项（如 T-4 SNIEP $n=5$、T-8 $\pm$-rank 小阶——二者属**方法族 M2：秩/惯性**，**不涉覆盖证书**）✓

---

## §7 证据表（含 ID／URL ✓）

| # | 内容 | 出处 | 级别 |
|---|---|---|---|
| E1 | $\ell_1(2,q)$ 定义＋$q\le16$ 表 | Pambianco 等 2003, Australas. J. Combin. **28**, 161–169 | **逐字** ✓ |
| E2 | **分类到 $q\le23$** | Bartoli–Marcugini–Milani–Pambianco, ACCT 2012；Bartoli–Davydov–Faina–Marcugini–Pambianco, *J. Geometry* (2013) `10.1007/s00022-013-0178-y` ✓ | **逐字** ✓ |
| E3 | 上界线（连续） | arXiv:1702.07939；arXiv:1505.01426；Nagy 渐近界 ✓ | **逐字** ✓ |
| E4 | 覆盖码 ↔ saturating 同篇处理 | arXiv:1808.09301；*Linear nonbinary covering codes and saturating sets* (AMC 2011) ✓ | **逐字** ✓ |
| E5 | **2026 仍在跑** | **arXiv:2606.16669**（2026, generalized covering radii, geometric approach）⚠️ | **逐字** ✓ |
| E6 | 库存原文自陈同机制 | `TOPIC-DOSSIER-v1` T-7"与 T-6 **同机制**（syndrome 覆盖 ↔ saturating）" ✓ | 档内 ✓ |

## §8 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "1-saturating"
技术词 1-saturating     命中文件数=8    :: ./A5-CORRECTION-17-is-reduced-reps-not-orbits.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./gen_asets-chain-explains-2-vs-17.md
$ bash scripts/tech_word_check.sh "saturating"
技术词 saturating       命中文件数=16   :: ./TARGET-L9-source-fetch-report.md ./A5-CORRECTION-17-is-reduced-reps-not-orbits.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md
$ bash scripts/tech_word_check.sh "complete arc"
技术词 complete arc     命中文件数=0    ::
$ bash scripts/tech_word_check.sh "novelty gate"
技术词 novelty gate     命中文件数=12   :: ./WHY-CANNOT-CREATE-TOOLS-bohr-and-tao.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./ASSETS-REGISTRY.md
$ bash scripts/tech_word_check.sh "资产隔离"
技术词 资产隔离         命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`complete arc`／`资产隔离` 命中 0 ⟹ 前者为**外部文献术语**、后者为**唐先生本轮用语**，均**引用**，**不作新性主张** ✓）
- **档案已有（引用，不列为提出）**：`1-saturating`（8 档）｜`saturating`（16 档）｜`novelty gate`（12 档）✓

## §9 诚实边界

- 全为 **round-1 source 快照**（未逐格清点 $\ell_1$ 全表；未跑 closure_gate）⟹ 结论**只到"该键为 DROP"** ✓
- **未动算** ✓；不改门 ✓；**不写"方向已死／不存在"** ✗（V290）—— 措辞为"**该格与 $K(10,1)$ 同证书逻辑，且已被同族持续收割，故不作为目标**" ✓
- §6 为**池级观察／建议**，**非决定** ✓（决策权在唐先生 ✓）
