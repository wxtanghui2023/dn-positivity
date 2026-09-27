# T1-CHECK-2026-09-27 — `z_L(5,5)` 三点 source-first 核验（不计算）⟹ **判定 DROP → 转 T-5**

**已查地图：命中（本档为既有条目 T-1 的 source-first 核验，非新案）**
所查：`docs/TOPIC-DOSSIER-v1-six-columns-and-relations.md`（T-1 ⭐首攻 ✓）｜`docs/TOPIC-INVENTORY-MASTER-v1.md`（**L-1 明写"下一动作＝三点确认"** ✓）｜`docs/CONCRETE-TOPIC-LIST-r2.md`（出处 `MDPI Symmetry 18(7) 1076` ✓）｜`docs/Zarankiewicz-A3-source-check.md`（**A3 批已登记该对象** ✓⚠️）
D0: 本档对象 ＝ **档案已有**条目 T-1（`z_L(5,5)`，`TOPIC-INVENTORY-MASTER-v1` L-1）的**三点 source-first 核验与归位判定**（重命名：否 ✗；新对象：无 ✗）
D1: 0（source 抽取 + 归位判定；不主张新自由度 ✓）

**纪律** ✓：**零计算** ✗；**未写新脚本** ✗；未动 SAT ✗（唐先生 21:01 指令）✓

---

## §0 判定（先给）

$$\boxed{\textbf{T-1 DROP}\ ⟹\ \textbf{转 T-5}}$$
**三条理由（各自独立充分）** ✓
1. **出处已归位**：`Zarankiewicz-A3-source-check.md`（**2026-09-24 22:33**，比 T-1 的"首攻"标记**更新** ⟹ 依"新证据优先"）已把该对象登记为**记录型入口 #4**：`owner＝是`、`在跑路线＝构造＋上界论证`、`判定＝D`，并**预登记**"**不在 Zarankiewicz 内部改参数救场**；直接进入 A4（Brouwer 表）" ✓
2. **命门子任务＝同组的下一步**：我方看中的"作者留的 exhaustive 子任务"，作者**在同一篇里已对 5×3／5×4 做过完整枚举**（附录），5×5 只是"未做" ✗ ⟹ 我方若做，**与原作者同形赛跑**（且该组 2026-09-07 仍在产出）⚠️
3. **5×5 格已被多方同时攻击**：独立第二组（`arXiv:2605.09926`，三边框架）2026-05-11 已给 `z_{3L}(5,5)\ge16` ⟹ 该格的"记录型"价值已被摊薄 ✗

**⟹ 依唐先生判据**（"只有 T-1 失败才转 T-5"）✓：**T-5 成为下一核验对象**（且**不得**预设 $n=8$ 首攻 ✓）

---

## §1 点一｜`z_L` 定义（逐字锁定 ✓✓）

**出处**：Qi, Cui, Xu, *New Lower Bounds for the Limited Augmented Zarankiewicz Number Based on Complete Graphs*, **Symmetry 18(7):1076 (2026)**, 收 2026-05-06／改 06-17／受 06-20／**发表 06-24** ✓（作者：Liqun Qi 浙江科技学院/港理工；Chunfeng Cui 北航；Yi Xu 东南大学）

**定义（§1 逐字）** ✓
> "To better capture the maximum SOS rank, Qi, Cui, and Xu [24] introduced the **limited augmented** Zarankiewicz number $z_L(m,n)$, which allows the addition of **2-edges** $(x_iy_j+x_ky_l)^2$ to a $C_4$-free graph under constraints that forbid **generalized $C_4$-cycles**. They proved $\mathrm{BSR}(m,n)\ge z_L(m,n)\ge z(m,n)$"

**构造（§2 Preliminaries 逐字）** ✓
> "Let $G_1=(S,T,E_1)$ be an $m\times n$ bipartite graph with $S=[m]$, $T=[n]$. Assume $G_1$ has no $C_4$-cycle and $|E_1|=z(m,n)$. A **limited augmented** bipartite graph $G=(S,T,E)$ augmented from $G_1$ has edge set $E=E_1\cup E_2$, where $E_1$ is the set of **1-edges** and $E_2$ the set of **2-edges**."
> "A 1-edge is a pair $(i,j)$ with $i\in S$, $j\in T$. A 2-edge is a quadruple $(i,j;k,l)$ with $i,k\in S$, $j,l\in T$."
> "**Nondegenerate** if $i\neq k$ and $j\neq l$; **Row-degenerate** if $i=k$ and $j\neq l$; **Column-degenerate** if $i\neq k$ and $j=l$. The case $i=k$ and $j=l$ is forbidden."
> 另有**简单性条件 (S)**：无 2-edge 与任何 1-edge 共享格 $(i,j)$（原文此处截断，**须取全文核** ⚠️）

$$\Longrightarrow\ \textbf{点一：锁定 ✓✓}\ \text{（另可核第二表述：}z_L\ \leftrightarrow\ \text{"2-edges }(i,j;k,l)\ \text{in a }C_4\text{-free bipartite graph, each representing }(x_iy_j+x_ky_l)^2\text{"}）$$

---

## §2 点二｜作者声称的 open gap 是否仍在（逐字 ✓✓）

**出处 A**：**arXiv:2604.04111**《A General Lower Bound for the Limited Augmented Zarankiewicz Number》（Qi–Cui；＝MDPI 文的预印本）逐字：
> "**Such a search is beyond the scope of this paper. The exact value of $z_L(5,5)$ remains open; here a lower bound of 15 was established**" ✓✓✓

**出处 B**：MDPI 文 §1 逐字：
> "Compared with the previously known lower bounds $z_L(5,3)\ge9$, $z_L(5,4)\ge12$, and **$z_L(5,5)\ge14$**, the present paper proves exactness for the first two cases, **improves the last lower bound to 15**, and gives new lower bounds for $6\times3$, $6\times5$, and $6\times6$." ✓✓

**⟹ 数字疑点已解** ✓：`arXiv:2605.09926`（三边文）摘要中 "the known bounds … $z_L(5,5)=14$" 指的是**前作下界 14**（非精确值）⟹ **库存记的"下界 15"正确** ✓✓（本轮自勘：一度疑为冲突）

**⟹ 点二：仍是 open ✓✓**（且**三连更新**：14 → 15 → 未定；最新外部（2026-09-07 K_{5t} 文）**未触及** 5×5 ✓）

---

## §3 点三｜extremal $C_4$-free $5\times5$ 图是否已完备分类（**决定性子问** ⚠️）

**逐字证据（MDPI §1）** ✓
> "These results are obtained by **enumerating all non-isomorphic extremal $C_4$-free graphs** and systematically checking admissible 2-edge augmentations; the detailed case analyses for $5\times3$ and $5\times4$ are provided in the appendices." ✓✓

**判读** ✓
- 作者**已掌握并已执行**"全部非同构 extremal $C_4$-free 图 × 容许 2-edge 增广"的枚举法 —— 但**只做到 $5\times3$／$5\times4$**（附录）✓
- **$5\times5$ 未做**（同文逐字："beyond the scope"）✗ ⟹ 我方看中的"前置子任务"**未被收割**，但**正是同组的下一步** ⚠️
- 另注（档级，**未核** ⚠️）：经典侧 extremal $K_{s,t}$-free 二分图分类文献（DMTCS *Extremal $K(s,t)$-free bipartite graphs*，声称含 $n=4,5,6$ 的 extremal 图刻画）可能覆盖 $z(5,5)$ 的 extremal 图 —— **但那是经典 $z$ 的 extremal 图，不是 $z_L$ 搜索所需的"全部 extremal $C_4$-free $5\times5$ 图 × 2-edge 增广"** ⟹ **不构成收割** ✓（**须取正文核** ⚠️）

**⟹ 点三：量级＝"可做但同形赛跑"** ⚠️（不是"已收割"，也不是"又一堵墙"）

---

## §4 证据表（含可复现 ID／URL —— 补 R1 的可复现缺口 ✓）

| # | 对象 | 出处（ID／URL） | 关键读数 | 级别 |
|---|---|---|---|---|
| E1 | $z_L$ 定义 + 5×5 下界 15 | MDPI **Symmetry 18(7):1076**（2026-06-24）<br>`https://www.mdpi.com/2073-8994/18/7/1076` | §1／§2 逐字（见 §1） | **逐字** ✓ |
| E2 | 5×5 **仍 open** + "beyond the scope" | **arXiv:2604.04111**（Qi–Cui 预印本）<br>`https://arxiv.org/pdf/2604.04111` | §2 逐字 | **逐字** ✓ |
| E3 | 新家族 + $z_L(10,5)=23$ | **arXiv:2609.07227**（Liu–Song，2026-09-07）<br>`https://arxiv.org/abs/2609.07227` | 摘要逐字；未触及 5×5 | **逐字** ✓ |
| E4 | 三边框架 + $z_{3L}(5,5)\ge16$ | **arXiv:2605.09926**（2026-05-11，math.CO） | 摘要逐字；指 5×5 前作下界 14 | **逐字** ✓ |
| E5 | 既有归位（记录型 #4，owner＝是，判定 D） | `docs/Zarankiewicz-A3-source-check.md`（**2026-09-24 22:33**） | 预登记"不在 Zarankiewicz 内部改参数救场" | 档内 ✓ |
| E6 | 经典 extremal $K_{s,t}$-free 分类 | DMTCS *Extremal $K(s,t)$-free bipartite graphs*<br>`https://dmtcs.episciences.org/435/pdf` | 声称 n=4,5,6 的 extremal 刻画（**未逐字核** ⚠️） | **档级** ⚠️ |

**冲突处理（按纪律）** ✓：E5（09-24 22:33）**晚于** T-1 的"首攻"标记（`TOPIC-DOSSIER-v1` 09-24 13:52／`TOPIC-INVENTORY-MASTER-v1` 09-24 13:39）⟹ **新证据优先** ⟹ T-1 的"首攻"地位**作废** ✓✓（本档即该冲突的正式归位）

---

## §5 交棒：T-5 三点核验（**下一刀**，仍不计算）

**T-5** ＝ 图 rank／inertia 小阶**完备表**（`CONCRETE-TOPIC-LIST-r2` §60 判它"规模最友好、E+D 双对口"✓）
**三点（**不得预设 $n=8$ 首攻** ✓）**
1. **规模核实**：目标阶的**图数**（库存"约 $10^4$"仅为估计 ⟹ 须以 **$n\,C_2$ 图的计数／OEIS** 核）
2. **已知完备阶数**：文献的**已解决阶数阈值**（$n\le?$ 完整）
3. **公开证书状态**：是**结果已解决**，还是**仅有算法／部分族**？是否已有公开数据库／程序产出完整表？（**E5 前置问**：AI＋SAT＋入库流水线是否已覆盖该格 ⚠️）
**红线**：**"存在算法"≠"问题已解决"** ✗；未过三点不得设计计算 ✗

## §6 诚实边界

- 全为 **source 抽取级**；点三的经典分类（E6）**未取正文核** ⚠️；MDPI §2 简单性条件 (S) 句**被截断** ⚠️ ⟹ 两点须下轮补齐
- **未动算** ✗；不改任何既有结论 ✗；不写"方向已死／不存在" ✗（V290）—— 只写"**该条目归位：记录型、有主、同形赛跑**" ✓
