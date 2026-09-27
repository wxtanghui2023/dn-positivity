# CHAIN-REAUDIT-119-2026-09-27 — **119 线（$K(10,1)$ 覆盖码）证明／构造链逐环难点拆解**

> ⚠️ **空间隔离（2026-09-27 21:32 唐先生令）**：**本档＝空间 B 之 119 线专用** ✓。
> **与 RH 链（空间 A）严格分账** ✗ —— 两空间证据**不得互挪**、**不得并入同一论证** ✓。
> 本档**不**引用 RH 链任何环节；反向，RH 档（`CHAIN-REAUDIT-2026-09-27-…`）已加隔离横幅 ✓。

**已查地图：命中（既有 119 线全档，非新案）**
所查：`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`（**权威链条交接** ✓✓）｜`docs/P2SEARCH-2026-09-27-119-directed-repair-spec.md`｜`docs/P2SEARCH-VALIDATION-2026-09-27-m120-gate-failed.md`（**决定性** ✓）｜`docs/MIPRUN-2026-09-27-bound-honesty-and-the-p2-fork.md`｜`docs/MIPRUN2-2026-09-27-int10c-terminal-and-source-first-gate.md`｜`docs/PROJCUT-2026-09-27-projection-cuts-are-covering-sums-structural-stop.md`｜`docs/INTRELAX-2026-09-27-integer-relaxation-equals-original.md`（＋`-REFILE-…equivalent-reparameterization`）｜`docs/LEDGER-119-2026-09-27-abandoned-runs-check-and-R2-item.md`｜`docs/P1-REAUDIT-2026-09-27-E-correction-and-the-mod-11-theorem.md`｜`docs/SCOL0-…`｜`docs/A4-2026-09-27-local-consistency-theoretical-audit.md`｜`docs/A5-2026-09-27-surplus-support-coupling-audit.md`｜`docs/INCIDENCE-2026-09-27-full-relations-and-the-injectivity-theorem.md`｜`docs/C3-119-…`｜`docs/CONGRUENCE-119-…`｜`docs/TRIPLE-119-…`｜`docs/RESTART-119-2026-09-27-assessment-of-the-second-order-route.md`｜`docs/REPAIR-SHARING-2026-09-27-layer1-exact-and-layer2-spec.md`｜`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`｜`docs/CORE-2026-09-27-…`／`CORE-2026-09-27b-…`｜`docs/BFREEZE-2026-09-27-…md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §12）
D0: 本档对象 ＝ **档案已有** 119 链的**逐环难点拆解**（重命名：否 ✗；新对象：无 ✗）
D1: 0（审计型 ✓；**未动算** ✓；**未改门** ✓）

---

## §0 结论速览（**难点的分布**）

$$\boxed{\text{难点分两侧}\ :\ \textbf{构造侧（P2）卡在“实现达标”};\quad \textbf{证明侧（P1）被现有技术堵死};\quad \textbf{结构侧只剩一个核}}$$
$$\textbf{构造侧}:\ \text{自检门（}m{=}120\text{）★未过 ⟹ 一切 }119\ \text{读数无效};\ \text{且精确卡点＝“能否产出\textbf{等基数但带冗余的 124 码}”(neutral}\wedge R\ge1\text{)}$$
$$\textbf{证明侧}:\ \delta\text{-型泛函被 profile 恒等式\textbf{全钉死} ⟹ 唯一可容许者＝\textbf{支撑敏感（跨中心）}不等式};\ \text{而 }E{=}285\ \text{是强制恒等式 ⟹ “}E\ge286\text{”}\equiv P1\ \text{本身（\textbf{无弱化目标}）}$$
$$\textbf{结构侧}:\ \textbf{21 机制封口} ⟹ \text{irreducible core ＝ \textbf{Boolean covering feasibility}}$$

---

## §1 119 链骨架（**12 环** ✓）

$$\underbrace{L_0}_{\text{目标／边界}}\to\underbrace{L_1}_{\text{基准码}}\to\underbrace{L_2}_{\text{搜索代数}\times4}\to\underbrace{L_3}_{\textbf{实现自检门}}\to\underbrace{L_4}_{\text{数据卫生}}\to\underbrace{L_5}_{\text{整数形＝等价重参数化}}\to\underbrace{L_6}_{\text{MIP 下界侧}}$$
$$\to\underbrace{L_7}_{\textbf{21 机制封口}}\to\underbrace{L_8}_{\text{L3-}\alpha\ \text{残余链}}\to\underbrace{L_9}_{\textbf{精确卡点}}\to\underbrace{L_{10}}_{\textbf{可容许类}}\to\underbrace{L_{11}}_{\text{第二层 excess 记账}}$$

---

## §2 $L_0$｜目标与既有边界（**难点：两侧都极窄**）

| 项 | 逐字／读数 | 难点 |
|---|---|---|
| $P_0$ | $K(10,1)$ | — |
| $P_2$（上界） | $K(10,1)\le120$（历史构造）✓ | **120 是上界 ⟹ 不得写 $K(10,1)=120$** ✗ |
| $P_1$（下界） | $K(10,1)\ge120$ **未证** ✗ | 下界侧：**107（BÖW 2004）／LP 93.09／SDP 105.2／MIP 99.0** ⟹ 距 119 **极远** ✓ |
| **target** | $|C|\le119$ ✓ | 历史路线＝construction ＋ **SA** ＋ **tabu／local search**（**只给上界** ✓）；Östergård 1991 的 60-word mixed code 改进了该参数 ⟹ 该侧长期为**活口** ✓ |
**⟹ $L_0$ 难点** ✓：**上界侧差 1 词（120→119）**，**下界侧差 12–21** ⟹ **两侧不对称**：构造侧是"差一点"，证明侧是"差一大截" ✓

---

## §3 $L_1$｜基准码（**难点：已不可约 ⟹ 起点已最优**）

| 读数 | 难点 |
|---|---|
| 基准 $=$\texttt{work/k10/c62/keri_pool/K\_9\_1\_classif.txt}（两个 62-码 ⟹ **两半构造 124 词**，合法覆盖 ✓ **不可约** ✓） | **起点本身已不可约** ⟹ 124→123 **必须**先造出"可删词"，不能靠清理现成冗余 ✓ |
| 对照（$\S$文献基线） | `work/k10/kamenetsky120.txt` 独立复核：**120 词**、badlen＝0、dup＝0、**覆盖 1024/1024** ✓ | 基准**可达**（说明目标码存在性无问题，问题在**搜索能力**）✓ |

---

## §4 $L_2$｜搜索代数（**四代数**）与代际（**难点：已到"净中性"天花板**）

$$\text{代数 }A=\text{delete-refill repair}\ \big|\ B=1\text{-for-}1\text{ swap}\ \big|\ C=k{=}2\text{ swap}\ \big|\ D=k{=}3\text{ swap}\ ✓$$
| 代际 | 读数 | 判定 |
|---|---|---|
| lns2 | 65k 步**零接受** ✗（因"禁用 $R$"致接受门**逻辑上不可能触发**）✓ | 实现 bug |
| lns3 | 148 起点亦零下降 ✗ | — |
| lns4 | Metropolis 修复 ✓ 但**停在 143** ✗ | 未达标 |
| kopt1 | acc＝0 ✗（同因） | 实现 bug |
| **kopt2** | acc 3.1–6.3 万 ✓、neutral 3.1–6.3 万 ✓、**max\_R＝2** ✓、first $R\ge1$ ≤1517 步 ✓、**desc＝0** ✗ | **下降事件为零** |
| **kopt3** | cleanup **生效** ✓（每次真删 1 词 ✓），但净效应 **125→124 中性** ✗ | **净中性循环** |
**⟹ $L_2$ 难点** ✓：**$R\ge1$ 与 neutral 均已观测，但二者从未同时出现** ⟹ 见 $L_9$

---

## §5 $L_3$｜**实现自检门 $m=120$（★决定性）** —— 难点拆解（4 处具体缺口 ✓）

$$\boxed{\text{自检逻辑}:\ K(10,1)\le120\ \text{已知} \Longrightarrow m{=}120\ \text{时解必然存在} \Longrightarrow \text{搜不到 ⟹ 实现未达标}✗}$$
| 读数 | 值 |
|---|---|
| targeted repair ＋ tabu ＋ SA，$m{=}120$，六次 restart | **best\_unc ＝ 34／28／34／28／31／25** ✗（**全远未到 0**） |
| 对照：裸 SA，$m{=}119$ | best\_unc ＝ 24–27 ✗ |
| 对照：两半构造 | 124 词合法但不可约 ✗ |
$$\Longrightarrow\ \boxed{\text{三条实现路径\textbf{均未达文献水准}} \Longrightarrow \text{对 }m{=}119\ \text{的任何“找不到”}\textbf{无效}✗✓}$$

**归因（4 缺口，逐字 ✓）**：① **能量只用 $|H|$**（无二阶项／无"洞的分布"信息 ✗）；② **邻域只用"$B_1(y)$ 中随机取 $c'$"**（**未做精确 $\arg\min$ 评估** ✗）；③ **tabu tenure 固定随机**（未调参 ✗）；④ **无重启扰动策略／无种群** ✓
**速度不是瓶颈** ✓：$\sim8\times10^3$–$2\times10^4$ 步/秒 ⟹ **瓶颈在邻域/能量设计** ✓

---

## §6 $L_4$｜数据卫生（**难点：历史"119 候选"是坏的** ⚠️）

| 读数 | 判定 |
|---|---|
| `work/k10/code119_candidate.txt` | **119 词但只剩 1007/1024 覆盖** ⟹ 17 点未覆盖 ⟹ **不是 119-witness** ✗✓ |
| 生成于 2026-09-24 22:59，**此前从未做独立覆盖验证** ⚠️ | ⟹ "历史 $n{=}10,R{=}1$ 结果"**仍只能是 120** ✓（本档纠正 ✓） |
| `tabu_np.py` | **崩溃** `IndexError: index 92 is out of bounds…` ⟹ `np120.log` 中 $k<120$ 各行**全是坏产物** ✗ 不可用 |
**⟹ $L_4$ 难点** ✓：**搜索线曾长期在"坏产物 + 未验证候选"上运行** ⟹ 需**数据卫生门**（本档记为纪律 ✓）

---

## §7 $L_5$｜整数覆盖形 ＝ **等价重参数化**（**难点：正锥割先验无力**）

$$\min\{\mathbf 1^Tf:Tf\ge1,\ f\in\mathbb Z_{\ge0}\}=K(n,1)\ ✓\ (\textbf{等价重参数化，}\textbf{非松弛}\ ✗)$$
$$\text{投影割}＝\text{covering 约束之和} \Longrightarrow \boxed{\text{正锥内割先验无力}}✗✓\ (\text{A-PROJCUT-1};\ \text{并\textbf{结构性}解释 A4/SA 之无力}\ ✓)$$
**⟹ $L_5$ 难点** ✓：**"加割／加投影"这一整类强化在正锥内结构性无效** ⟹ 不在"参数调优"层面可救 ✓

---

## §8 $L_6$｜MIP 下界侧（**难点：有限时间界 ≠ 理论界**）

$$\texttt{int10c}\ \text{跑满预算}:\ \text{Status}=\text{Time limit};\ \textbf{Dual}=99.0;\ \textbf{Primal}=138;\ \textbf{Gap}=28.26\%;\ \text{Nodes}=3751;\ \text{Timing}=900.17\text{s}✓$$
$$\Longrightarrow\ \text{无}\le119\ \text{整数解} \Longrightarrow \text{按 (SB-1) 分支 ② MIP STOP}✓;\quad \boxed{99\ \text{是\textbf{有限时间 bound} ⟹ 不等于“}119\ \text{不存在”✗}}$$
**⟹ $L_6$ 难点** ✓：**通用 exact-MIP 900s 未解决** ⟹ 该路线属"算力型"，与 $L_3$ 同侧（**能力问题，非数学问题**）✓

---

## §9 $L_7$｜**21 机制封口**（**难点：局部／图论捷径已全关**）

$$18\ \text{档案既有}:\ \text{GAPTHEOREM}\mid\text{PROPAGATION}\mid\text{FAILSET}\mid\text{SCOL}\mid\text{MIDSUP}\mid\text{FACE}\mid\text{T3-MIN-1}\mid\text{L-GREEN-1}\mid\text{GRAM-LIFT}\mid\text{HQ1}\mid\text{L4AUDIT}\mid\text{STAR3}\mid\text{M-1}\mid\text{M-2A}\mid\text{M-2A}'{}\mid\text{M-2B}\mid\text{Fourier}\mid\text{Del6}$$
$$3\ \text{本线新增}:\ \text{A5 surplus}\times\text{支撑}\mid\text{A4 局部一致性}\mid g{=}11T^{-1}\delta\ \text{模 }11\ \text{核}$$
$$\Longrightarrow\ \boxed{\text{irreducible core ＝ Boolean covering feasibility}}✓$$
**⟹ $L_7$ 难点** ✓：**21 条局部机制全部封口** ⟹ 只剩"**纯布尔覆盖可行性**"这一核 ⟹ **不存在"换个局部引理再试"的空间** ✓

---

## §10 $L_8$｜L3-α 残余链（**难点：几何只到 $L\ge3$；第 4 个单位需 $E$-专有耦合**）

$$\text{残余全表}:\ 9{,}381{,}251=7{,}723{,}409\ (\tau\ge6)+1{,}657{,}826\ (\text{容量})+16\ (\text{完整交叠})\ ✓\ (\text{恒等式已核验})$$
$$\delta\text{-pattern 压缩}:\ 310{,}124\to56\to4\ (\text{4 模式}\ \nu{=}2)\ ✓\Longrightarrow \textbf{L3-}\alpha\ \text{＝ COMPLETE FINITE CERTIFICATE（全 residual 覆盖）}✓✓$$
$$\text{统一机制（三条定量事实）}:\ c(D)\ge2\ \wedge\ L(D)\ge4\ \wedge\ \Sigma_D|S_z|\le|E|+1 \Longrightarrow |{\textstyle\bigcup}S_z|\le|E|-3 \Longrightarrow \tau(E)\ge5✓$$
| 环节 | 状态 | 难点 |
|---|---|---|
| **T1 top-$k$ 容量恒等式** | ✓ 已归档（$\max\Sigma$＝**top-4 权重和** ⟹ **免枚举即精确判定** ✓） | 已解决 ✓ |
| **excess $\le1$（sharp）** | ✓ 16/16 例；池内 873,472 四元组 excess>1＝**0**；$+1$ **确实现** ⟹ **sharp** ✓ | 已解决 ✓ |
| $c(D)\ge2$ | ✓ 修正后成立（$c{=}0$ 排除 ＋ **$c{=}1$ 逐例 $\max\Sigma<|E|$**） | 已解决 ✓ |
| **$L(D)\ge4$（第 4 个单位）** | ⚠️ **纯几何只到 $L\ge3$**（STAR 且 $y^\ast\in E$ ⟹ $L\ge3$，1585 例**取等**）；第 4 单位需 $(A,E)$-**专有尺寸耦合** | **未解 ⟹ STOP（BFREEZE）** ✗ |
**⟹ $L_8$ 难点** ✓（**已精确收敛为一条**）：**"纯几何层的统一 overlap 下界为 $L\ge3$，而目标 $L\ge4$ 依赖 $E(A)$ 的专有尺寸耦合"** ✓✓（`BFREEZE` 逐字）

---

## §11 $L_9$｜**精确卡点**（**难点：唯一未观测事件** ✓✓）

$$\text{要得 }124\to123:\ \text{需存在}\ \boxed{|S|{=}124,\ h{=}0,\ R\ge1}\ \text{的状态} \Longrightarrow \text{此时 cleanup 立即给 }123✓$$
$$\text{现状只观测到 }r{=}k{+}1\ (|S|{=}125) \Longrightarrow \text{cleanup 只把 }125\ \text{拉回 }124✗$$
$$\Longrightarrow\ \boxed{\textbf{瓶颈}＝\text{repair 能否产出“\textbf{等基数但带冗余}的 124 码”}\quad(\textbf{不是}\text{“能不能删”——已证能删}✓)}$$
**定义（防误用 ✓）**：$U(c):=B_1(c)\setminus B_1(C\setminus\{c\})$；$U(c)=\varnothing\iff c$ 可直接删除；$R(C):=\#\{c:U(c)=\varnothing\}$ ＝ **严格可删除词数** ⟹ **$R\ge1\Longrightarrow\exists c$ 可直接删除** ✓；$\rho(H):=\min\{|X|:H\subseteq B_1(X)\}$，$\rho(H){=}1\iff$ 存在直接 $124\to123$ ✓
**唯一未观测事件** ✓：**neutral（$|S|$ 不变）∧ $R\ge1$** ✓

---

## §12 $L_{10}$｜**可容许类**（**难点：证明侧只剩一类可用** ✓✓）

$$\boxed{E:=\sum_x\delta(x)=\sum_x(b(x)-1)=\mathbf{285}}\quad(\text{无条件强制}:\ 119\cdot11=1309,\ 1309-1024=285\ ✓)$$
$$\Longrightarrow\ \boxed{\text{目标“}E\ge286\text{”}\iff\text{“}119\text{-码不存在”}\iff P_1\ \text{本身}}\quad(\textbf{不是}新的弱化目标\ ✗)$$
| 环节 | 读数 | 难点 |
|---|---|---|
| **传播引理** | ✓ 已证＋数值验证（$Q{=}0$ 时对距离-2 对之中点 $m$：$|C\cap S_2(m)|\ge\lceil(n-2)/2\rceil$；$n{=}4{:}40/40$、$n{=}5{:}28/28$） | 已解决 ✓ |
| **ladder 论断** | ✗ **数值证伪**（两条迭代断言均有反例） | 已排除 ✓ |
| **关键限制** | **该引理不给奇偶障碍、且不聚合** ✗（不同中点可**共享同一个 $z$** ⟹ 全局计数不受理） | **局部容量下界 ≠ 全局 excess 下界** ✓ |
| **可容许性判据** ★ | $E=\sum(b(x)-1)$ 是 **$\delta$-型泛函**；档案已建立：$\delta$-型泛函被 **profile 恒等式钉死**（`SUM-P1P4`：线性局部泛函与码无关；`AMEND-30` LOCAL-AVG-GATE；`GAPTHEOREM`：十类 $\sum_xf(\delta(x))$ 全被 $Q{=}1$ 指纹钉住 ✓） | ⟹ **任何只用 $b(x)$ 统计的论证不可能给出 $E\ge286$** ✗ ⟹ **唯一可容许者 ＝ 支撑敏感（跨中心）不等式** ✓✓ |

---

## §13 $L_{11}$｜REPAIR-SHARING：第一层已 STOP、第二层＝唯一出口（**难点：目标已精确化为 excess 记账**）

$$\text{第一层需求集之精确刻画}:\ \mathcal T_J=\{y:\mathrm{wt}(y)=3,\ |\mathrm{supp}(y)\cap J|\ge2\},\quad |\mathcal T_J|=\binom q2(n-q)+\binom q3✓$$
$$\text{自检}:\ q{=}10\Rightarrow\binom{10}3=\mathbf{120}✓;\ q{=}3\Rightarrow\binom32\cdot7+1=\mathbf{22}✓✓$$
$$\text{候选覆盖能力（修正）}:\ \text{weight-2 }e_p{+}e_q\ \text{覆盖 }\mathbf 8\ \text{点（}p,q\in J\ \text{时全部 8 ✓）} \Longrightarrow z_{ij}\in C\ \text{用 1 个 codeword 修掉整个 }Y_{ij}✓$$
$$\text{第一层 STOP（强化 ✓）}:\ \text{最乐观 }q+\binom q2\ \text{在 }q{=}10\ \text{时}=55\ \ll119 \Longrightarrow \textbf{第一层不可能产生 119 矛盾}✗✓$$
$$\Longrightarrow\ \text{第二层＝唯一出口} \Longrightarrow \text{目标精确化为 excess 记账}:\ \text{须产生 excess }\ge286✓$$
**⟹ $L_{11}$ 难点** ✓：**逐层记账的下一个出口已被点名，但它正是 $L_{10}$ 的"支撑敏感"不等式** ⟹ **两个终点的难点是同一个** ✓

---

## §14 难点汇总（**谁在卡、卡在哪一类** ✓）

| 类别 | 环节 | 卡点性质 |
|---|---|---|
| **能力型**（可修复，非数学） | $L_3$ 实现自检门（4 缺口）｜$L_6$ MIP 900s | **实现／算力不足** ⟹ 可升级解决（精确 $\arg\min$＋二阶能量＋tabu 调参＋SA 温度表）✓ |
| **数据卫生** | $L_4$ 坏的 119 候选／崩溃日志 | 需**验证门**（已有纪律 ✓） |
| **结构性** | $L_5$ 正锥割无力｜$L_7$ 21 机制封口 ⟹ core＝Boolean covering feasibility | **不存在局部捷径** ✓ |
| **几何—耦合型** | $L_8$ $L\ge3\to L\ge4$ 的第 4 单位 | **纯几何不足，需 $E(A)$ 专有耦合** ⟹ BFREEZE ✓ |
| **观测型** | $L_9$ neutral $\wedge R\ge1$ 从未出现 | **唯一的未观测事件** ⟹ 下一轮唯一动作 ✓ |
| **可容许型（证明侧）** | $L_{10}$ 唯一放行类＝**支撑敏感跨中心**｜$L_{11}$ 第二层＝同一不等式 | **证明侧只剩一条窄路**，且它等价于直接证 $P_1$ ✓✓ |
$$\boxed{\text{一句话}:\ 构造侧卡在\textbf{能力＋一个未观测事件};\ 证明侧卡在\textbf{可容许类只剩一条、且该条＝直接证 }P_1;\ \text{结构侧只剩}\textbf{Boolean covering feasibility}}$$

---

## §15 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "自检门"
技术词 自检门        命中文件数=9    :: ./B-2026-09-26-n9-construction-status-and-line-snapshot.md ./P2SEARCH-VALIDATION-2026-09-27-m120-gate-failed.md ./ASSETS-REGISTRY.md
$ bash scripts/tech_word_check.sh "可删除词"
技术词 可删除词        命中文件数=2    :: ./CHAIN-REAUDIT-119-2026-09-27-per-link-difficulty-decomposition.md ./HANDOFF-2026-09-27-119-line-session-handoff.md
$ bash scripts/tech_word_check.sh "支撑敏感"
技术词 支撑敏感        命中文件数=4    :: ./RESTART-119-2026-09-27-assessment-of-the-second-order-route.md ./ASSETS-REGISTRY.md ./CHAIN-REAUDIT-119-2026-09-27-per-link-difficulty-decomposition.md
$ bash scripts/tech_word_check.sh "irreducible core"
技术词 irreducible core 命中文件数=5    :: ./PROJCUT-2026-09-27-projection-cuts-are-covering-sums-structural-stop.md ./CHAIN-REAUDIT-119-2026-09-27-per-link-difficulty-decomposition.md ./CLOSED-ROUTES-MAP.md
$ bash scripts/tech_word_check.sh "第一层"
技术词 第一层        命中文件数=43   :: ./E152-double-reflection-axis-audit.md ./V316-C-layer1-prereq-gap-analysis.md ./V2-32-layer1-BC-itself-reduces-the-bilinear-structure.md
$ bash scripts/tech_word_check.sh "等基数"
技术词 等基数        命中文件数=4    :: ./KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md ./ASSETS-REGISTRY.md ./CHAIN-REAUDIT-119-2026-09-27-per-link-difficulty-decomposition.md
```
- **本档新增**：**0** 个术语 ✓（六词**全部**为 119 线既有档内用语 ⟹ **纯审计**，无新性主张 ✓✓）
- **档案已有（引用，不列为提出）**：`自检门`（9）｜`可删除词`（2，含 HANDOFF ✓）｜`支撑敏感`（4）｜`irreducible core`（5）｜`第一层`（43）｜`等基数`（4）✓

## §16 边界（硬 ✓）

- **未动算** ✗；**未改门** ✓（G-1…G-4 只登记 ✓）；**未跨空间引用** ✓（不引 RH 链任何环节 ✓）
- 全部读数**引自** 119 线既有档并标状态 ✓；**未**新造机制／未新造难点 ✗
- 不写"不可能／不存在／方向已死" ✗；找不到 ⟹ 只记"该配置／预算未找到" ✓（HANDOFF §5 红线沿用 ✓）
- `/tmp/cov` ＝ covering-**design** 搜索器（Nurmela–Östergård）⟹ 与 code 搜索**严格分账** ✗，不得称"复现" ✓
