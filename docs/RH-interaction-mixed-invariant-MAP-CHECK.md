已查地图：命中 25 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
　判定：25 命中经逐条审视，**全部为同形异义**（如 `p26a14-mixed-flow` = β-动力学系列的"混合流"；
　其余为 RH 侧 obstruction／局部-整体条目）⟹ **本仓对"mixed invariant／interaction differential"机制族无专门覆盖** ✓
　但⚠️ **同型的对应物在 RH 侧已闭**：`V196`–`V198`（Brauer／K₂／H¹ 型局部-整体：canonical ⟹ `[T]=0` 或 `Br[N]`）✓

# **MAP-INTERACTION CHECK**：mixed / cross invariant（`I_A=I_B=0` ⟹ `M(A,B;X)≠0`？）

**唐先生令（2026-09-22 21:07–21:11）**：
① 新攻击点 = **双重表示的兼容性障碍**，压窄为 **mixed / cross invariant**：`I_A(X)=0`、`I_B(X)=0`，但存在**非退化交叉量** `M(A,B;X)≠0` ✓；
② ⛔ **`secondary obstruction` 本身 = DEAD**（拓扑／`A_∞`／谱序列／交叉数中已成熟）✓；
③ **四硬条件**：1 不可由 `I_A,I_B` 单独恢复｜2 **非** cup/Massey/commutator 换符号｜3 有独立数学意义｜
　⭐ 4 **必须产生定量约束**，而不只是 obstruction class ✓；
④ **判决规则（照录）**：「如果这四项中**第 2 或第 3 项失败，就立即 DEAD**」；「**若全部被吸收 ⟹ Interaction mechanism = DEAD**；
　若出现一个**非拓扑、非纯同调、具有独立定量内容**的 mixed invariant，那才第一次真正有资格进入十三门」✓✓；
⑤ **不开案；暂时不碰 RH** ✓

D0: 本档对象 = **mixed/cross invariant 机制族的四域地图-文献核验**（档案**无专门覆盖** ⟹ 新档；**未开案** ✓）
D1: 0
FREEZE-ACK: 零计算／零 Lean／未写程序／未碰 RH／未调用 C-380／未放宽门槛 ✓

---

## §1 protocol（先写死 ✓）

```
【范围】 四独立领域：① 拓扑／同调 ② 数论／算术 ③ 信息论／熵 ④ 几何／凸性 ✓
【每实例四问】 1 `I_A=I_B=0` 是否分别容易？｜2 `I_12` 是否**真由交互**产生？｜3 是否为**已有不变量重命名／已有机器吸收**？｜4 是否有**独立问题价值**？✓
【否决】 **第 2 或第 3 项失败 ⟹ 立即 DEAD** ✓；**全部被吸收 ⟹ 机制族 DEAD** ✓
【证据等级】 **题录级**（检索标题/摘要/片段，**未**逐字全文精读）⚠️
【预算】 一轮；**不开案** ✓
```

## §2 四域结果（**题录级 ⚠️**，带来源 ✓）

| 域 | 代表实例 | 1 | 2 | 3 | 4 | 判定 |
|:--|:--|:--:|:--:|:--:|:--:|:--|
| **① 拓扑／同调** | 逐层 obstruction class／谱序列 `d_r`；**Massey／Toda** 高阶积；**secondary obstruction**（三球面 pairwise 障碍全消后仍有二级障碍）✓ | ✓ | ✓ | ⛔ **已有机器**（cup／Massey／`A_∞`／SS） | ✓ | **DEAD**（唐先生已预先判 `secondary obstruction` = DEAD ✓） |
| **② 数论／算术** | **Brauer–Manin** ＋ 有限 étale descent **不足**（Poonen, *Annals* 171 (2010) 2157–2169）；**descent obstruction**（Skorobogatov：descent ＝ étale Brauer–Manin ✓） | ✓ | ✓ | ⛔ **成熟理论**；⚠️**本仓同型已闭**（`V196`–`V198`） | ✓ | **DEAD** |
| **③ 信息论／熵** | ⭐ **non-Shannon-type 不等式**（`Zhang–Yeung 1997` 条件型／`1998` 无条件型 ⟹ `Σ̄_n ⊊ Θ̄_n`）；**证明"不由此前不等式蕴含"** ✓✓；定量用途＝网络编码率区／保密共享 ✓ | ✓ | ✓✓ **独立证明** | ⚠️ **产生机制已系统化**：**copy lemma／MAXE**（"未发现任何可由 copy lemma 迭代证出的不等式之外者"）⟹ 吸收 ✓ | ✓✓ | **DEAD（第 3 项失败）** |
| **④ 几何／凸性** | ⭐ **mixed volume**（对个体体积**不可恢复** ✓、多重线性、非负）＋ **Alexandrov–Fenchel 不等式**（**定量** ✓✓）；等价情形 2024 由 Shenfeld–van Handel（多胞形）解决 ✓；⚠️ **通用性已被识别**：van Handel 逐字「**AF 与凸几何关系不大，它是更普适的对象，源自代数结构**」✓ | ✓ | ✓ | ⚠️ **机器已通用化**（可"import"到其他领域） | ✓✓ | **GAP（见 §3）** |

## §3 ⭐ 判定

```
【① ②：DEAD】 拓扑／算术两域的 mixed 量**已被成熟机器吸收**（cup／Massey／`A_∞`／谱序列；descent／étale Brauer–Manin）✓
　且唐先生已预先判 `secondary obstruction` 本身 DEAD ✓；算术侧**本仓同型（`V196`–`V198`）亦已闭** ✓
【③：DEAD（第 3 项失败）】 熵域**确有** `I_1=I_2=0` 而额外约束存在的**严格证明**（这是全库最接近的样本 ✓✓），
　但**产生新不等式的方法已被"copy lemma／MAXE"系统化** ⟹ 我方提法＝**已有机器吸收** ⟹ 依令**立即 DEAD** ✓
【④：GAP（唯一保留处）】 mixed volume ＋ AF 是**非拓扑、非纯同调、具独立定量内容**的 mixed invariant ✓✓，
　且 AF 的**通用性**已被识别（源自代数结构、可跨领域 import）⟹ **不是任一新不变量**;
　⛔ 但存在**明确空白接口**（van Handel 逐字）：「**对另一些猜想 log-concavity 的问题，并不存在（mixed volume）表示**」✓✓
　⟹ **GAP 的精确陈述**：需找一个**尚无混合表示**的定量问题，其交叉量
　　(a) **不可由个体量恢复**、(b) **未被 copy lemma／AF 通用机器吸收**、(c) **带定量约束**、(d) **有独立问题价值** ✓
【机制族总判定】 **三域 DEAD ＋ 一处 GAP**：
　$$\boxed{\text{Interaction mechanism（本仓）}=\textbf{DEAD}（拓扑／算术／熵）\ \wedge\ \textbf{GAP}（"无混合表示"空白）}$$
　⟹ 依令：**不开案** ✓；**不碰 RH** ✓；GAP 处若日后出现**具体候选**，须**先地图核验 → 13 门** ✓
```

## §4 边界与回查（✗✓）

```
✗ 零计算／未写程序／未碰 RH／未调用 C-380／未放宽门槛／**未开案** ✓
✗ 不把"三域 DEAD"记为战绩 ✓；**不**声称凸几何／信息论领域无价值（两域**活跃**：熵区域刻画仍开放；AF 等价情形 2024 仍有进展 ✓）
⚠️ 证据等级＝**题录级**（未逐字全文）⟹ 若需升为**逐字全文级**须另授权 ✓
【技术词回查（`scripts/tech_word_check.sh`，**先跑后写** ✓；逐字粘贴 ✓）】
　技术词 混合不变量  命中文件数=0 ⟹ **本档新增** ✓
　技术词 交互项      命中文件数=0 ⟹ **本档新增** ✓
　技术词 交叉不变量  命中文件数=0 ⟹ **本档新增** ✓
　技术词 定量混合量  命中文件数=0 ⟹ **本档新增** ✓
　技术词 吸收判据    命中文件数=0 ⟹ **本档新增** ✓
【外部来源（**题录级**）】 Poonen, *Insufficiency of the Brauer-Manin obstruction applied to étale covers*, Annals 171 (2010) 2157–2169 ✓｜
　Skorobogatov（descent obstruction ＝ étale Brauer-Manin）✓｜Zhang–Yeung 1997／1998（首个非 Shannon 型不等式）＋ copy lemma／MAXE ✓｜
　Minkowski／Alexandrov–Fenchel（mixed volume；quermassintegrale）＋ Shenfeld–van Handel 2024（AF 等价情形，多胞形）＋ van Handel ICBS 讲稿（**AF 通用性**、Minkowski 单调性等价情形仍开放、无混合表示的 log-concavity 猜想）✓｜
　Schulze–Whiteley（轨道刚性矩阵，前档）✓｜MathOverflow／Springer（Massey／Toda 高阶积）✓
```
