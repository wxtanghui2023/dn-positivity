# R4-P1-2026-09-27 — **private-point deficit 引理**（纯局部推导；零计算）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:24 令 ✓）**：只做 **R4-P1**（private-point deficit 引理）；**不碰** $\mu$／PSD／Gershgorin／Fourier／SAT／124-deletion ✓；**不计算** ✓。

**已查地图：命中（接续 R3 链与前序 119 档，非新案 ✓）**
所查：`docs/R3-A3-2026-09-27-…`（**二阶压缩 terminating negative** ✓✓）｜`docs/R3-A2-2026-09-27-…`｜`docs/SECOND-ORDER-2026-09-25-…`（**$b,\delta$ 恒等式** ✓✓）｜`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`（**$U(c)$／$R$ 可删性** ✓✓）｜`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`（**$U(c),R,\rho(H)$ 定义** ✓✓）｜`docs/ASSETS-REGISTRY.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §8）
D0: 本档对象 ＝ **档案已有** private-point／可删性对象的**局部引理化**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出精确局部公式 $p(c)=10-|S(c)\cup V(H_c)|$ ＋ 可删性判据 ＋ 聚合界 451** ⟹ 并给出前提前提修正 ✓）
**[RESEARCH]**

---

## §0 结论（**一条前提修正 ＋ 三条新结果 ✓**）

$$\boxed{\textbf{前提修正（必须）}:\ P:=\sum_c p(c)=n_1=\mathbf{739}+\sum_{j\ge3}(j-2)n_j\ \ge\ \mathbf{739}\ \Longrightarrow\ \text{"}P\le118\text{"}\ \textbf{不可得}\ ✗✓}$$
$$\boxed{\textbf{新结果 1（精确局部公式 ✓✓）}:\ p(c)=10-\big|S(c)\cup V(H_c)\big|✓\quad(S(c)=\{i:c\oplus e_i\in C\},\ V(H_c)=\{i:\exists j,\ c\oplus e_i\oplus e_j\in C\})}$$
$$\boxed{\textbf{新结果 2（可删性判据 ✓✓）}:\ c\ \text{可删}\ (p(c)=0)\iff|S(c)\cup V(H_c)|=10\iff\textbf{十个坐标方向全被局部占用}✓}$$
$$\boxed{\textbf{新结果 3（不可约 ⟹ 聚合界 ✓✓）}:\ \forall c:\ |S(c)\cup V(H_c)|\le9\ \Longrightarrow\ \sum_c|S(c)\cup V(H_c)|\le\mathbf{451}\ \ (\text{平均}\le\mathbf{3.79}/10)✓✓}$$

---

## §1 私有量：定义与恒等式（**零点：前提修正 ✓✓**）

$$B_1(c)=\{c\}\cup\{c\oplus e_i\}_{i=1}^{10},\ |B_1|=11✓;\qquad p(c):=\Big|B_1(c)\setminus\bigcup_{c'\ne c}B_1(c')\Big|\ ✓$$
$$\textbf{恒等式（2 行 ✓）}:\ \sum_c p(c)=\#\{x:b(x)=1\}=:n_1\ ✓\ \text{（点被恰覆盖一次 ⟺ 它对唯一码字私有 ✓，双向 ✓）}$$
$$\text{多重度分布}:\ \sum_jn_j=1024;\quad \sum_j j\,n_j=11\cdot119=1309;\quad \sum_j(j-1)n_j=285✓$$
$$\Longrightarrow\ \sum_{j\ge2}n_j=1024-n_1;\quad \sum_{j\ge2}(j-1)n_j=285\ \Longrightarrow\ \boxed{n_1=1024-285+\sum_{j\ge3}(j-2)n_j=\mathbf{739}+\sum_{j\ge3}(j-2)n_j}✓✓$$
$$\Longrightarrow\ \textbf{私有球点总数}\ \ge739\ (\text{等号}\iff\text{无三重覆盖}\ ✓)\ \Longrightarrow\ \text{平均每码字私有}\ \ge739/119\approx\mathbf{6.21}\ ✓✓$$
$$\textbf{⚠️ 故唐先生的"证 }P\le118\text{"路线\textbf{死}}✗✓:\ P\ \text{被 }b\text{-profile 恒等式\textbf{强制}\ \ge739\ }\text{—— 它与 }119\ \text{无关（对任意 }m\text{ 同型）✓}$$

## §2 局部律：**精确公式**（**新结果 1 ✓✓**）

$$\text{两球交}:\ B_1(c)\cap B_1(c')\ne\varnothing\iff d(c,c')\le2✓;\qquad |B_1(c)\cap B_1(c')|=2\ (d\in\{1,2\})✓$$
$$\text{逐邻居的具体点（\textbf{关键} ✓）}:\quad d=1,\ c'=c\oplus e_i\Longrightarrow B_1(c)\cap B_1(c')=\{c,\ c\oplus e_i\}✓$$
$$\qquad d=2,\ c'=c\oplus e_i\oplus e_j\Longrightarrow B_1(c)\cap B_1(c')=\{c\oplus e_i,\ c\oplus e_j\}✓$$
$$\text{故非私有集}\ =\ \{c\}\cup\{c\oplus e_i:\ i\in S(c)\cup V(H_c)\}\ ✓\ \text{（\textbf{midpoint 共享}：}c\oplus e_i\ \text{被所有含 }i\ \text{的距离-2 邻居共有 ✓✓）}$$
$$\Longrightarrow\ \boxed{p(c)=11-1-\big|S(c)\cup V(H_c)\big|=10-\big|S(c)\cup V(H_c)\big|}\ ✓✓\ \text{（精确，无估计 ✓）}$$
$$\text{对照（union bound 版，}\textbf{真空} ✗）:\ p(c)\ge11-2(d_1(c)+d_2(c))\ \text{及}\ \sum_c p(c)\ge1309-4(N_1+N_2)\ \text{—— 因 }N_1+N_2\ \text{上界不足而\textbf{恒真} ✗✓}$$

## §3 可删性判据 ＋ 聚合界（**新结果 2／3 ✓✓**）

$$\boxed{\textbf{判据 ✓✓}:\ p(c)=0\iff|S(c)\cup V(H_c)|=10\iff\text{每坐标 }i\ \text{满足}\ (c\oplus e_i\in C)\ \text{或}\ (\exists j:c\oplus e_i\oplus e_j\in C)✓}$$
$$\qquad\text{（\textbf{与档案 }U(c)=\varnothing\ \text{一致 ✓}：}U(c)=B_1(c)\setminus B_1(C\setminus\{c\})=P(c)\ ✓）$$
$$\textbf{WLOG 不可约 ✓}:\ \text{若 }\exists c:p(c)=0\ \text{则 }|C|=119\Longrightarrow|C\setminus\{c\}|=118\ \text{覆盖}\Longrightarrow K\le118\ \text{（更早结束 ✓）};\ \text{故反证中可设}\ \forall c:p(c)\ge1✓$$
$$\Longrightarrow\ \forall c:\ |S(c)\cup V(H_c)|\le9\ ✓;\qquad \sum_c p(c)=1190-\sum_c|S(c)\cup V(H_c)|=n_1✓$$
$$\Longrightarrow\ \boxed{\sum_c\big|S(c)\cup V(H_c)\big|=1190-n_1=451-\sum_{j\ge3}(j-2)n_j\ \le\ \mathbf{451}}\ ✓✓\quad\Big(\text{平均}\ \le\frac{451}{119}\approx\mathbf{3.79}\ \text{个方向}/10\Big)✓✓$$
$$\textbf{读数 ✓}:\ \text{每个码字平均只在 }\sim4\ \text{个坐标方向上"局部被看见"} \Longrightarrow \text{其余 }\sim6\ \text{方向\textbf{既无距离-1 邻居也无距离-2 邻居}}✓\ \text{—— \textbf{标号}级结构性事实 ✓✓}$$

## §4 为何 §0 的前提修正**必须**（诚实 ✓）

$$\text{唐先生原设想}:\ P\ge119\ \text{（每码字至少一个私有）}\ \wedge\ \text{证}\ P\le118\Longrightarrow\ \bot\ ✓\ \text{—— \textbf{该路死} ✗：}P\ge739\ \text{被强制 ✓}$$
$$\text{更准确}:\ P=n_1\ \text{完全由 }b\text{-profile}\ \{n_j\}\ \text{决定 ✓} \Longrightarrow \textbf{私有计数\textbf{不}携带超出 }b\text{-profile 的信息}✗\ \text{（与 R3 的"}\delta\text{-型泛函被 profile 钉死"同型 ✓）}$$
$$\text{但}\ \textbf{私有量的}\textit{分配}\ (p(c))_c\ \text{不被 }b\text{-profile 决定 ✓✓}\ \text{—— 这正是 §5 的新轴 ✓}$$

## §5 **新轴：codeword-labelled（谁的重复）** vs R3 的 coordinate-labelled ✓✓

$$\text{R3（坐标标号）}:\ q_{ij}\ \text{＝哪个\textbf{坐标对}承载距离-2 对}\ \big|\ \text{R4（\textbf{码字标号}）}:\ p(c),S(c),V(H_c)\ \text{＝哪个\textbf{码字}的球被占}✓✓$$
$$\text{唐先生原话（照录 ✓）}:\ \text{"}Q=\sum\binom\delta2\ \text{把'谁造成重复'全部忘掉了"}\ ✓\ \Longrightarrow\ \textbf{codeword-labelled 正是把这一层重新装回}✓✓$$
$$\text{精确关系 ✓}:\ \sum_c d_1(c)=2N_1,\quad \sum_c d_2(c)=2N_2\ \text{（总和无新息 ✗）};\ \text{但逐 }c\ \text{的}\ (d_1(c),d_2(c),|S\cup V(H)|)\ \text{不被总量决定}✓$$

## §6 下一步（**R4-P1′ 的可攻击形态；本档不跑** ✓）

$$\textbf{目标改写（避免真空 ✓）}:\ \text{不使用 union bound};\ \text{直接用 §3 的}\ \sum_c|S(c)\cup V(H_c)|\le451\ \text{与}\ \textbf{局部图 }H_c\ \text{结构耦合}$$
$$\text{攻击面（两条 ✓）}:\ \textbf{(a)}\ \text{把 }451\ \text{与}\ \text{excess 恒等式（}285\text{）及}\ n_j\ \text{分布耦合};\quad \textbf{(b)}\ \text{证明某个全局计数迫使某 }c\ \text{的}\ |S\cup V(H)|\ge10\ ⟹\ \text{可删}\ ⟹\ \bot✓$$
$$\text{若两条都证不出} ⟹\ \textbf{登记}:\ \text{codeword-labelled 局部层\textbf{同样松弛}} ✗\ \text{（与 R3-A3 同型收束）✓}$$

## §7 与旧资产的关系（**防重复 ✓**）

$$U(c)\ \text{（档案）}\ \equiv\ P(c)\ \text{（本档）}✓;\quad R(C)=\#\{c:U(c)=\varnothing\}\ \text{（档案可删词数）}\ \equiv\ \#\{c:p(c)=0\}✓$$
$$\text{本档\textbf{新增}}:\ \textbf{(i)}\ p(c)=10-|S(c)\cup V(H_c)|\ \text{的精确性};\ \textbf{(ii)}\ \text{可删性判据（占用全 10 向）};\ \textbf{(iii)}\ \sum|S\cup V(H)|\le451\ \text{（平均 3.79）}✓$$

## §8 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "私有球点"
技术词 私有球点        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "私有分配"
技术词 私有分配        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "局部律"
技术词 局部律          命中文件数=10   :: ./ZF-3-minimal-arithmetic-input-audit.md ./RH-MODEL-FIRST-STATUS-LOCK-and-NEXT-GENERATOR.md ./C-alpha-rigidity-MAP-CHECK-and-13-gate-screen.md
$ bash scripts/tech_word_check.sh "codeword-labelled"
技术词 codeword-labelled 命中文件数=0    ::
$ bash scripts/tech_word_check.sh "不可约覆盖"
技术词 不可约覆盖      命中文件数=0    ::
$ bash scripts/tech_word_check.sh "多重度分布"
技术词 多重度分布      命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（五个 0 命中者为**本档自造标签**，作结构命名，不作新性主张 ✓；`局部律`（10）为档案已有 ✓）
- **注** ✓：本档实质＝**§1 前提修正 ＋ §2 精确公式 ＋ §3 判据与聚合界**（推导性 ✓）

## §9 边界（硬 ✓）

- **零计算** ✓；**未碰** $\mu$／PSD／Gershgorin／Fourier／SAT／124-deletion ✓（照令 ✓）；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** $K(10,1)\ge120$ ✗（V290 ✓）；**不声称** private-point 路线必然失败 ✗ —— 只写"**计数版（$P\le118$）已被证死**"＋"**标号版（$p(c)$ 分配／$S\cup V(H)$ 占用）仍开**" ✓
- §3 的 451 是**必要条件**（不可约 ⟹）✓，**不是**矛盾 ✓
