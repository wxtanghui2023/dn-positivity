# T6-CHECK-2026-09-27 — T-6 `K_q(n,R)` 具体格子：对象指纹 ＋ 后继链 ＋ 同形赛跑 ⟹ **DROP**

**已查地图：命中（本档为既有条目 T-6 的严格筛选，非新案）**
所查：`docs/TOPIC-DOSSIER-v1-six-columns-and-relations.md`（**T-6 原定义** ✓）｜`docs/CONCRETE-TOPIC-LIST-r2.md`（T-6 已知/缺口/等级 ✓）｜`docs/FRONTIER-2026-09-25-K10-1-status-and-reassessment.md`（**与本线邻接** ⚠️）｜`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`、`docs/BFREEZE-2026-09-27-…md`（**T1–T5 资产** ✓）｜`docs/ASSETS-REGISTRY.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §6）
D0: 本档对象 ＝ **档案已有**条目 T-6（covering code $K_q(n,R)$ 的具体格子）的**对象指纹／后继链／同形赛跑与出口判定**（重命名：否 ✗；新对象：无 ✗）
D1: 0（source 抽取 ＋ 出口判定；不主张新自由度 ✓）

**纪律** ✓：**零计算** ✗｜未写计算脚本 ✗｜**G-1…G-4 只登记、不改门** ✓（唐先生 21:13）

---

## §0 单一出口

$$\boxed{\textbf{T-6 ＝ DROP}}$$
**三条依据（各自独立充分 ✓）**
1. **同形赛跑全面撞上**（同参数／同等价／同构造族／同作者群）⟹ 依唐先生规则"**任何一个撞上，先 DROP/HOLD，不进入计算**" ✓
2. **严格 novelty gate 答不出**（见 §4）：无法说明"T-6 的未决量能让 T1–T5 产生**新的数学约束**"；若强行做，形态就是"把 $K(10,1)$ 的局部证书**换参数再跑**" ✗
3. **"仍开"的证据不足**：本领域**正面 open 声明**（作者 2026-08 自述检索）指向 $q\ge6$ 自 2011 停滞——**但该文本身已把 58 个 $6\le q\le21$ 下界收割** ⟹ 剩余"未见表"格**属检索缺口**，依 G-2/G-4 纪律**不得**当作 open ✗

**⟹ 不进 P1/P2** ✓（**唯一外部副产品**见 §4 末：Lemma A 的 $q$ 元推广，**登记为可迁移资产观察**）

---

## §1 点一｜对象指纹（锁定 ✓）

$$K_q(n,R)=\min\{|C|:C\subseteq\mathbb Z_q^n,\ \text{覆盖半径}\le R\}\ ✓\quad(\text{cell}＝\text{三元组}(q,n,R))$$
- **等价关系**：$K_q(n,R)$ **是整数** ⟹ "open" ＝ **上下界未重合**（不是"分类"问题）✓
- **不可混的对象（显式排除 ✗）**：① **混合码** $K_{q_1,q_2}(n,R)$（库里确有此类列）✗；② **重量/范数受限**覆盖码 ✗；③ **saturating sets**（$\mathrm{PG}(n-1,q)$ 中的线饱和集）—— 与 $K_q(n,\cdot)$ **等价相邻**（$q$ 元半径 1 覆盖 ↔ 饱和集）⚠️ **须分开记**；④ 二元 $K_2(n,1)$ ＝**超立方体支配数** ⟹ 属**我们已冻结的 $K(10,1)$ 邻域** ✗（**不得**借 T-6 复活）
- **本领域标准记号逐字**（源文 ✓）："The binary case $K_2(n,1)$ is the domination number of the hypercube, and $K_3(n,1)$ is the **football pool problem**" ✓

---

## §2 点二｜后继引用链（自 open claim 追到 2026 ✓）

**链条（逐字 ✓）**
| 环节 | 内容 | 出处 |
|---|---|---|
| 表基座 | "The known bounds for $q\ge3$ are collected in the **tables of Kéri** … were **last revised in November 2011**" | arXiv:2608.19872v3 ✓ |
| 停滞陈述 | "**For $q\ge6$ we know of no published improvement on either side since 2011**, and of none on the upper-bound side for $q\ge5$; a search of arXiv, DBLP, OpenAlex, Lobstein's covering-radius bibliography, and the publication lists of the authors active in the area, **carried out in August 2026, found none**" ✓✓ | 同上（**正面 open 证据**✓） |
| **收割（同篇）** | "We improve the known bounds on $K_q(n,R)$ in **84 cases (83 distinct cells)**"：**26 个上界**（$5\le q\le15$，显式码 ＋ local search ＋ large neighbourhood search，$q^n\le10^{10}$）＋ **58 个下界**（$6\le q\le21$，**Gijswijt–Polak SDP** ＋ 多精度 ＋ **精确有理证书**）✓ | 同上 |
| 证书链 | "**every certificate is checked by a standalone program in exact arithmetic**"；"**The codes, the certificates, and the checkers are provided as ancillary files**" ✓⚠️ | 同上 |
| 单格 | "$K_6(10,4)$ improved from both sides, from **417–2952 to 441–2751**" ✓ | 同上 |
| 并行线 | Gijswijt–Polak SDP（published $q\le5$）；Wu–Chen **改进二元下界**；**Florath 在证明助手中形式化 covering-code 界** ⚠️ | 同上 |

**⟹ 后继链读数** ✓
- 该跑道**具备**：显式码 ＋ 精确有理证书 ＋ **独立 checker** ＋ ancillary files ＋ 证明助手形式化 ⟹ **"dent＋证书＋入库"形态被完全工业化**（`A3` §E5 同款风险，**加倍** ⚠️）
- **Kéri 表停在 2011-11** ⟹ "**库仍写 unknown**" ⟹ 依唐先生纪律 **不算 open 证据** ✗✓

---

## §3 点三｜同形赛跑检查（**全面撞上** ✗）

| 维度 | 判定 | 依据 |
|---|---|---|
| 同一参数 | **撞上** ✗ | 同一 $K_q(n,R)$ 三元组格 |
| 同一等价关系 | **撞上** ✗ | 同为"上下界是否重合" |
| 同一 construction family | **撞上** ✗ | 显式码 ＋ direct sum／product rules（Kéri 表 propagation）＋ SDP 下界（Gijswijt–Polak） |
| 同一作者组／紧邻后继 | **撞上** ✗ | Marosi (BME, 2026-08/09)｜**Kéri**（表主）｜Haas–Halupczok–Schlage-Puchta（下界）｜Gijswijt–Polak（SDP）｜Wu–Chen（二元）｜Florath（形式化） |
**⟹ 依规则：任一撞上即 DROP/HOLD，不进入计算** ✓

---

## §4 点四｜严格 novelty gate（唐先生必答项 ✓）——**答不出 ⟹ DROP**

**必答问题**：为什么 T-6 的未决量能让 **T1–T5** 产生**新的数学约束**，而不是把已做完的 $K(10,1)$ 局部证书**换参数再跑**？

**逐项核（诚实 ✓）**
| T1–T5 资产 | 可否用于 $K_q(n,R)$？ | 理由 |
|---|---|---|
| **T1** top-4 容量恒等式 | ✗ 不适用 | 它关于**"删 4 个码字后"的局部捕获账本**（特定码 $C$、特定 $E(A)$）；$K_q(n,R)$ 是**全局极小**问题，无"删除"结构 ✓ |
| **T2/T4** sharp excess／$c\ge2$ 链 | ✗ 不适用 | $E$-专有尺寸耦合，绑定 $A/E$ 与那一个 124 词码 ✓ |
| **T5** STAR/TRI 局部几何 | ⚠️ **仅局部重叠计数** | 它给 $L\ge3$ 型**局部**事实；**不**给全局下界 ✓ |
| **Lemma A**（球交 $=2$ 或 $0$） | ✅ **可推广**（见下） | 见"副产品" |
| L3-α machine certificate | ✗ | 124 码的局部穷举结论；换参数＝**重新跑同类证书** ⟹ 正是唐先生禁止的形态 ✗ |

$$\Longrightarrow\ \boxed{\textbf{答不出}\ \text{（无法证明 T-6 能让 T1–T5 产出新约束）}\ \Longrightarrow\ \textbf{依唐先生判词：宁可 DROP}\ ✓}$$

**唯一副产品（登记为可迁移资产观察 ⚠️ · 档级 · 3 行可证 · 未跑）**
> **Lemma A 的 $q$ 元推广**：在 $\mathbb Z_q^n$ 中，$|B_1(x)\cap B_1(y)|=2$ 若 $d(x,y)\in\{1,2\}$，$=0$ 若 $d(x,y)\ge3$ ✓
> **3 行理由（档级）**：$d=1$ 时交点 $=\{x,y\}$；$d=2$（差在第 $i,j$ 两坐标）时交点 $=\{x{+}\delta_i e_i,\ x{+}\delta_j e_j\}$；$d\ge3$ 时任一点与其一距离 $\ge2$ ✗
> **但它只给局部重叠计数**，**不**自动给 $K_q(n,R)$ 的全局下界 ⟹ **不足以支撑 T-6** ✓（如需，可在未来需要该局部几何的目标上复用 ✓）

---

## §5 证据表（含 ID／URL ✓）

| # | 内容 | 出处 | 级别 |
|---|---|---|---|
| E1 | $K_q(n,R)$ 定义 ＋ 84 例／83 格 ＋ 26 上界 ＋ 58 下界 ＋ 证书与 checker ＋ "no improvement since 2011" | **arXiv:2608.19872v3**（Marosi, BME, Sept 2026）`arxiv.org/html/2608.19872v3` | **逐字** ✓ |
| E2 | Kéri 表（$q\ge3$）**last revised November 2011**；改进记录止于 2011-11-21 | `old.sztaki.hu/~keri/codes/index.htm` | **逐字** ✓ |
| E3 | $K_6(8,4)\le166$；$441\le K_6(10,4)\le2751$（原 $417$–$2952$） | E1 ＋ 库存 `CONCRETE-TOPIC-LIST-r2` ✓ | **逐字** ✓ |
| E4 | 并行线：Gijswijt–Polak SDP（$q\le5$）／Wu–Chen 二元下界／**Florath 证明助手形式化** | E1 参考文献 ✓ | **逐字** ✓ |
| E5 | 我们自己的冻结线（$K(10,1)$ 邻域） | `docs/BFREEZE-2026-09-27-…md`、`docs/FRONTIER-2026-09-25-K10-1-…md` | 档内 ✓ |

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "covering code"
技术词 covering code    命中文件数=25   :: ./KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./FRONTIER-2026-09-25-K10-1-status-and-reassessment.md
$ bash scripts/tech_word_check.sh "Lemma A"
技术词 Lemma A          命中文件数=46   :: ./BFREEZE-2026-09-27-transferable-assets-T1-T5-and-stop-rationale.md ./KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md ./V132-O3star-classification-proposition-beta-free-data-lemma.md
$ bash scripts/tech_word_check.sh "K_q(n,R)"
技术词 K_q(n,R)         命中文件数=0    ::
$ bash scripts/tech_word_check.sh "football pool"
技术词 football pool    命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`football pool`／`K_q(n,R)` 命中 0 ⟹ 为**外部文献术语**，**引用**，不作新性主张 ✓）
- **档案已有（引用，不列为提出）**：`covering code`（25 档）｜`Lemma A`（46 档）✓
- **本档的"新"仅指**：**Lemma A 的 $q$ 元推广**（**档级观察**，未跑 ✓）—— 已在 §4 显式标注为**观察**而非结论 ✓

## §7 诚实边界

- 全为 **round-1 source 快照**（未逐格清点 Kéri 全表；未跑 closure_gate）⟹ 结论**只到"该键为 DROP"** ✓
- **未动算** ✓；不改门 ✓；**不写"方向已死／不存在"** ✗（V290）—— 措辞为"**该格被同形赛跑全面覆盖，且 novelty gate 答不出，故不作为目标**" ✓
- 二元格（$K_2(n,1)$）**严禁**借 T-6 复活 $K(10,1)$ 线 ✗（`BFREEZE` 仍有效 ✓）
